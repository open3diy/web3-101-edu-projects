# Ataques a Smart Contracts y Patrones de Defensa

Los smart contracts representan programas que controlan valor real, ejecutándose en entorno público y adversarial donde cualquiera puede intentar explotarlos. Esta combinación de valor económico significativo, inmutabilidad de código desplegado, irreversibilidad de transacciones y adversarios motivados crea uno de los entornos más desafiantes para desarrollo de software seguro. Los bugs en smart contracts no son simplemente inconvenientes que pueden parchearse más tarde; frecuentemente resultan en pérdida permanente e irrecuperable de millones o incluso cientos de millones de dólares.

Este documento explora los vectores de ataque más críticos contra smart contracts, desde el infame reentrancy que causó el hack de DAO hasta técnicas modernas más sutiles. Más importante, documenta patrones de defensa: prácticas de diseño, técnicas de implementación y herramientas que previenen estas vulnerabilidades. El conocimiento de estos ataques no es solo académico; es absolutamente necesario para cualquier desarrollador que escriba código que maneje fondos de usuarios.

La historia de ataques exitosos es simultáneamente aleccionadora e instructiva. Cada exploit mayor ha resultado en evolución de mejores prácticas, desarrollo de herramientas mejoradas y eventual codificación de patrones seguros en librerías estándares. Los desarrolladores modernos tienen ventaja de aprender de errores costosos de pioneros, pero solo si estudian esos errores cuidadosamente y implementan las lecciones aprendidas consistentemente.

## Reentrancy: El ataque más infame

El ataque de reentrancy es uno de los más peligrosos y prevalentes en historia de smart contracts. Fue el vector de exploit en el hack de DAO de 2016, resultando en robo de 3.6 millones de ETH (aproximadamente $70 millones en ese momento, valorado en billones al pico de 2021). Este único incidente llevó al controversial hard fork de Ethereum que creó Ethereum Classic. La importancia histórica y el impacto técnico hacen reentrancy el primer ataque que todo desarrollador debe comprender profundamente.

### Mecanismo del ataque

Un ataque de reentrancy ocurre cuando contrato vulnerable hace llamada externa a contrato no confiable antes de completar actualización de su propio estado interno. El contrato malicioso aprovecha esta llamada para re-entrar al contrato vulnerable, llamando nuevamente la misma función o función relacionada. Debido a que el estado no se actualizó entre las llamadas, el contrato vulnerable opera con información obsoleta, permitiendo al atacante violar invariantes críticos.

El ejemplo clásico involucra función de retiro. El contrato vulnera mantiene balances de usuarios y proporciona función `withdraw()`. Una implementación naive verifica que el usuario tiene balance suficiente, envía ETH al usuario, luego actualiza el balance a cero. El problema ocurre en la transferencia de ETH: si el destinatario es contrato, su función fallback se ejecuta, pudiendo llamar nuevamente `withdraw()` en el contrato vulnerable antes de que balance sea actualizado. El balance todavía muestra fondos, permitiendo retiro adicional. Este proceso puede repetirse muchas veces en una sola transacción, drenando el contrato.

```solidity
// CONTRATO VULNERABLE - NO USAR
contract VulnerableBank {
    mapping(address => uint) public balances;
    
    function withdraw() public {
        uint amount = balances[msg.sender];
        require(amount > 0, "Insufficient balance");
        
        // VULNERABLE: llamada externa antes de actualizar estado
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
        
        // Estado actualizado DESPUÉS de llamada externa
        balances[msg.sender] = 0;
    }
}

// CONTRATO ATACANTE
contract Attacker {
    VulnerableBank bank;
    
    constructor(address _bankAddress) {
        bank = VulnerableBank(_bankAddress);
    }
    
    // Iniciar ataque
    function attack() external payable {
        bank.deposit{value: msg.value}();
        bank.withdraw();
    }
    
    // Fallback re-entra al contrato vulnerable
    fallback() external payable {
        if (address(bank).balance >= 1 ether) {
            bank.withdraw();
        }
    }
}
```

El código atacante deposita primero cantidad pequeña para establecer balance. Luego llama `withdraw()`, que transfiere ETH al contrato atacante, trigger fallback. El fallback re-entra llamando `withdraw()` nuevamente. Debido a que `balances[msg.sender]` aún no se actualizó a cero, la verificación `require` pasa. El proceso continúa hasta que el banco está drenado o alcanza límite de gas.

### Variantes de reentrancy

El reentrancy simple involucra re-entrar la misma función. Pero existen variantes más sutiles. El cross-function reentrancy ocurre cuando atacante re-entra función diferente que lee el mismo estado no actualizado. Si un contrato tiene función `withdraw()` y función `transfer()` que ambas verifican `balances`, un atacante podría llamar `withdraw()` que hace transferencia externa, re-entrar via `transfer()` antes de que `withdraw()` actualice balance, moviendo fondos de nuevo.

El read-only reentrancy es particularmente insidioso. El atacante no modifica estado del contrato vulnerable durante reentrancy, solo lo lee. Esto es problemático en arquitecturas multi-contrato donde contratos dependen de estado consistente entre ellos. Un contrato A hace llamada externa antes de actualizar estado. El contrato malicioso re-entra a contrato B que consulta estado de contrato A. Contrato B ve estado obsoleto y toma decisiones incorrectas basadas en esa información, aunque contrato A mismo eventualmente se actualiza correctamente.

El reentrancy cruzado entre contratos en protocolos complejos con múltiples interdependencias es vector de ataque emergente. Los protocolos DeFi modernos frecuentemente involucran docenas de contratos interconectados. La reentrancy en un contrato puede propagarse inesperadamente a través de call chains complejos, violando invariantes en contratos que parecen no relacionados.

### Patrón Checks-Effects-Interactions

El patrón Checks-Effects-Interactions es la defensa fundamental contra reentrancy, codificando orden apropiado de operaciones en funciones de contratos.

La primera fase, Checks, ejecuta todas las validaciones y verificaciones de pre-condiciones. Verifica que `msg.sender` está autorizado, que balances son suficientes, que parámetros están en rangos válidos y cualquier otra condición que debe ser verdadera para que operación sea legítima. Estas validaciones usan `require()` que revierte si la condición falla, asegurando que código subsecuente solo se ejecuta si todos los checks pasan.

```solidity
// CHECKS: Verificaciones
require(balances[msg.sender] >= amount, "Insufficient balance");
require(amount > 0, "Amount must be positive");
require(msg.sender != address(0), "Invalid address");
```

La segunda fase, Effects, actualiza todo el estado interno del contrato. Modificaciones a variables de estado, emisiones de eventos y cualquier cambio al estado del contrato ocurren aquí. Crucialmente, esto ocurre ANTES de cualquier interacción externa. El contrato actualiza sus libros internos completamente antes de hablar con mundo externo.

```solidity
// EFFECTS: Actualizar estado
balances[msg.sender] -= amount;
emit Withdrawal(msg.sender, amount);
```

La tercera fase, Interactions, ejecuta llamadas externas a otros contratos o transferencias de ETH. Estas operaciones son inherentemente inseguras: ceden control a código externo que puede ser malicioso. Al realizar todas las actualizaciones de estado primero, el contrato garantiza que si código externo re-entra, encuentra estado consistente y actualizado.

```solidity
// INTERACTIONS: Llamadas externas al final
(bool success, ) = msg.sender.call{value: amount}("");
require(success, "Transfer failed");
```

Este patrón es simple conceptualmente pero requiere disciplina estricta en implementación. Los desarrolladores deben resistir tentación de "solo hacer una verificación rápida" después de llamada externa o actualizar "un último campo" después de interacción. Cualquier desviación del orden estricto puede introducir vulnerabilidad.

### OpenZeppelin ReentrancyGuard

OpenZeppelin, la librería de contratos estándares más ampliamente usada, proporciona `ReentrancyGuard` como mecanismo plug-and-play para prevenir reentrancy. Este contrato implementa modificador `nonReentrant` que puede aplicarse a cualquier función vulnerable.

```solidity
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract SecureBank is ReentrancyGuard {
    mapping(address => uint) public balances;
    
    function withdraw(uint amount) public nonReentrant {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        balances[msg.sender] -= amount;
        
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
    }
}
```

El modificador `nonReentrant` funciona mediante lock de estado. Establece flag al entrar función y lo verifica al inicio de cualquier llamada subsecuente. Si función ya está ejecutándose (indicado por flag establecido), la re-entrada es rechazada. Después de que función completa, el flag se limpia, permitiendo llamadas futuras.

La implementación internamente usa variable de estado que cambia entre valores indicando "no entered" y "entered". Este mecanismo es gas-efficient (SSTORE es costoso pero solo ocurre dos veces por invocación) y probado en batalla: miles de contratos usan `ReentrancyGuard` sin incidentes.

La protección es efectiva contra reentrancy simple, cross-function y muchas variantes. Sin embargo, no protege automáticamente contra read-only reentrancy cruzado entre contratos separados que no comparten el mismo ReentrancyGuard. Para protocolos multi-contrato complejos, diseño cuidadoso de interacciones y potencialmente locks globales coordinados pueden ser necesarios.

## Ataques de front-running y MEV

Los ataques de front-running explotan visibilidad pública de mempool y capacidad de atacantes de priorizar sus transacciones mediante fees más altos. Aunque no son vulnerabilidad de código del contrato per se, representan vector de explotación de valor significativo que diseñadores de contratos deben considerar y mitigar cuando posible.

### Mecanismo de front-running

Las transacciones Ethereum pasan tiempo en mempool antes de ser incluidas en bloques. El mempool es público: cualquiera puede ver transacciones pendientes, incluyendo sus datos completos. Un atacante monitorizando mempool identifica transacción rentable (por ejemplo, compra de token en DEX que moverá precio), crea su propia transacción aprovechando la misma oportunidad y la envía con gas price más alto. Los mineros/validadores incluyen transacciones con fees más altos primero, ejecutando transacción del atacante antes que la víctima original.

El ejemplo clásico es arbitraje de DEX. Alicia detecta oportunidad de arbitraje: comprar token en Uniswap y vender en Sushiswap para ganancia instantánea. Crea transacción ejecutando el arbitraje. Bob, ejecutando bot que monitoriza mempool, ve transacción de Alicia, copia la estrategia, y transmite con gas price 50% más alto. Transacción de Bob se ejecuta primero, capturando la ganancia. Transacción de Alicia posteriormente falla o ejecuta con mucho peor precio debido a que Bob ya movió el mercado.

### MEV: Maximal Extractable Value

El MEV (Maximal Extractable Value, anteriormente Miner Extractable Value) generaliza este concepto. Los validadores pueden reordenar, insertar o censurar transacciones dentro de bloques que producen. Esto les permite extraer valor mediante diversos esquemas: front-running, back-running (insertar transacción después de otra para aprovecharse de cambio de estado), sandwich attacks (front-run y back-run simultáneamente, capturando víctima entre dos transacciones del atacante).

La transición de Ethereum a Proof of Stake no eliminó MEV; simplemente cambió quién tiene capacidad de extraerlo. Los validadores de PoS tienen mismo control sobre ordenamiento de transacciones que los mineros de PoW. La diferencia es que bajo PoS, comportamiento malicioso puede resultar en slashing de stake, creando desincentivo económico. Sin embargo, si las ganancias MEV exceden el riesgo de slashing, los validadores racionales económicamente aún explotarán MEV.

#### Condiciones de carrera en la cola de bloques

Las condiciones de carrera (race conditions) en blockchain ocurren cuando múltiples transacciones compiten por ejecutarse primero, y el orden de ejecución determina quién obtiene valor. A diferencia de sistemas concurrentes tradicionales donde race conditions son bugs de sincronización, en blockchain son features del diseño que los atacantes explotan sistemáticamente.

La **manipulación del orden de transacciones** es el vector central de extracción MEV. Los validadores tienen control absoluto sobre qué transacciones incluyen en sus bloques y en qué orden las ejecutan (subject a reglas de consenso que son laxas en este aspecto). Este control permite múltiples estrategias de extracción:

La **queue reordering** implica que el validador reorganiza transacciones pendientes en mempool para maximizar su propio beneficio. Puede priorizar transacciones que le pagan directamente (propinas MEV), insertar sus propias transacciones entre transacciones de usuarios para capturar arbitraje, o excluir transacciones que competirían con sus operaciones. Esta manipulación es invisible para usuarios: solo ven que su transacción eventualmente se ejecutó, no que su posición en la cola fue degradada artificialmente.

El **transaction stuffing** ocurre cuando el validador llena el bloque con sus propias transacciones o transacciones de partners, desplazando transacciones de usuarios comunes. Durante períodos de alta congestión, esto puede retrasar confirmaciones de usuarios por múltiples bloques mientras el validador monopoliza espacio del bloque para extracción MEV. Los usuarios pagan fees altos creyendo que garantizan inclusión rápida, pero son superados por coaliciones de validadores-searchers.

La **censura selectiva** permite al validador excluir transacciones específicas completamente. Pueden censurar transacciones que competirían con arbitrajes propios, bloquear liquidaciones de posiciones donde el validador es contraparte o prevenir actualización de oráculos que invalidarían operaciones MEV planificadas. La censura temporal (retrasar transacción por algunos bloques) es suficiente para capturar oportunidades time-sensitive sin dejar evidencia obvia de censura permanente.

#### Categorías especializadas de MEV

El **liquidation MEV** se extrae de protocolos de lending cuando posiciones se vuelven subcollateralizadas. Los liquidadores compiten por ejecutar liquidaciones primero, obteniendo bonos de liquidación (típicamente 5-15% del valor liquidado). Los bots especializados monitorean posiciones continuamente, y cuando precio de colateral cae suficientemente, compiten por ser primeros en ejecutar liquidación. Los validadores pueden front-run bots de liquidación públicos, ejecutando liquidación ellos mismos o priorizando liquidaciones de searchers asociados.

Los **arbitrage bots** explotan discrepancias de precio entre DEXs. Cuando precio de token difiere significativamente entre Uniswap y Sushiswap, arbitragistas compran en el mercado barato y venden en el caro, capturando diferencia. El MEV ocurre cuando múltiples bots detectan mismo arbitraje: el validador decide quién lo ejecuta, frecuentemente eligiendo bot que paga mayor propina o ejecutando arbitraje directamente.

Las **NFT mint snipes** ocurren cuando colecciones populares de NFTs se lanzan. Los bots intentan mintear múltiples NFTs en bloque de lanzamiento. Los validadores pueden priorizar sus propias transacciones de mint o de asociados, garantizando obtención de NFTs deseables antes que participantes retail. Esto es particularmente lucrativo para lanzamientos altamente anticipados donde valor de reventa puede ser 10-100x el precio de mint.

### Sandwich attacks

Los sandwich attacks son variante particularmente dañina común en DEXs. Víctima intenta swap grande de token A a token B en AMM. Atacante detecta esto en mempool y crea dos transacciones: una comprando token B antes del swap de víctima (empujando precio hacia arriba), y otra vendiendo token B después del swap de víctima (cuando precio es más alto debido a compra de víctima). La víctima recibe peor precio debido a front-run del atacante, y atacante obtiene ganancia de diferencia.

La víctima efectivamente paga dos veces: slippage natural de su trade grande más extracción adicional por sandwich. Para trades grandes, esto puede ser pérdida de varios porcentajes. Los bots especializados escanean mempool 24/7 ejecutando sandwich attacks automáticamente. Flashbots y servicios similares han institucionalizado MEV, permitiendo a validadores cooperar explícitamente con searchers que identifican oportunidades MEV.

El ecosistema MEV ha evolucionado hacia infraestructura sofisticada. **Flashbots** creó mercado de dos lados: searchers identifican oportunidades MEV y pujan por inclusión de bundles (conjuntos de transacciones que deben ejecutarse atómicamente en orden específico) a validadores. Los validadores ejecutan bundles que maximizan sus ingresos. Este proceso es subasta eficiente pero concentra extracción MEV en actores profesionales con recursos computacionales significativos.

Los **Dark Pools MEV** son servicio adicional donde transacciones se ocultan completamente de mempool público. Los usuarios envían transacciones directamente a pools privados operados por constructores de bloques especializados. Esto previene sandwich attacks de bots comunes pero crea opacidad: usuarios deben confiar que operador del pool no explotará acceso privilegiado a su flujo de transacciones. La efectividad depende de reputación a largo plazo de operadores.

#### Impacto económico y sistémico del MEV

El MEV total extraído de Ethereum supera billones de dólares acumulativamente. Esto representa transferencia de valor desde usuarios retail hacia operadores sofisticados y validadores. Los críticos argumentan que MEV es efectivamente "impuesto invisible" en todas las transacciones DeFi, reduciendo eficiencia de mercados y desincentivando participación de usuarios que no pueden competir con bots profesionales.

La **centralización de validadores** es consecuencia preocupante. La extracción MEV requiere sofisticación técnica: infraestructura para monitorizar mempool en tiempo real, algoritmos de optimización, relaciones con searchers profesionales y stake significativo para validar frecuentemente. Esto favorece validadores grandes sobre individuales, contribuyendo a tendencias centralizadoras en consenso que contradicen objetivos descentralizadores de blockchain.

Los **time-bandit attacks** son escenario teórico extremo donde MEV disponible en bloques pasados es tan grande que economicamente es racional reorganizar historia de blockchain. Si un validador puede extraer más valor reorganizando últimos N bloques (para capturar MEV perdido) que el costo de producir esos bloques (stake slashing risk, hardware), la seguridad de consenso se degrada. Hasta ahora esto es teórico, pero MEV suficientemente grande podría hacer real esta amenaza.

### Mitigaciones

El diseño de contratos puede mitigar pero no eliminar completamente front-running. Los commit-reveal schemes dividen operación en dos fases: primero usuario envía hash de su intención (commit), luego en transacción subsecuente revela los detalles. El atacante ve el commit pero no sabe qué contiene hasta demasiado tarde para front-run. Sin embargo, esto añade fricción (dos transacciones en lugar de una) y latencia.

Los slippage limits permiten a usuarios especificar precio mínimo aceptable. Si front-run mueve precio más allá de límite, transacción revierte en lugar de ejecutar a precio pésimo. Esto previene peor explotación pero no elimina front-running: atacante simplemente puede ajustar su trade para permanecer bajo límite de slippage mientras extrae máximo valor posible.

Los private mempools como Flashbots Protect permiten a usuarios enviar transacciones directamente a validadores, bypassing mempool público. Esto previene front-running por bots genéricos pero no protege contra validadores mismos que pueden front-run o colaborar con searchers especializados. La efectividad depende de adopción: si solo minoría de validadores participan, transacciones privadas pueden experimentar latencia.

Los protocolos futuros están explorando cifrado de transacciones en mempool, revelando detalles solo después de inclusión en bloque. Esto requiere cambios a nivel de protocolo (no factible en Ethereum actual) pero es dirección prometedora para Layer 2s diseñados desde cero con resistencia MEV.

## Ataques de manipulación de precio de oráculos

Los smart contracts frecuentemente necesitan información del mundo real: precios de activos, resultados de eventos, datos meteorológicos. Los oráculos proporcionan estos datos. Sin embargo, los contratos que dependen de oráculos tienen superficie de ataque expandida: la seguridad depende tanto de código del contrato como de confiabilidad y resistencia a manipulación del oráculo.

### Manipulación de oráculos on-chain

Los oráculos on-chain derivados de DEXs son particularmente vulnerables. Si un contrato de lending usa precio spot de Uniswap para determinar valor de colateral, un atacante puede manipular temporalmente ese precio con flash loan. El atacante toma prestado cantidad masiva de token A, vende en Uniswap hundiendo precio, ejecuta operación en contrato víctima aprovechándose del precio manipulado (por ejemplo, liquidando posición subcollateralizada), luego compra token A de vuelta (precio ahora bajo) y repaga flash loan. Todo ocurre en una transacción atómica sin riesgo de capital para atacante.

El ataque a bZx en 2020 explotó exactamente este vector. El protocolo usaba precios de Uniswap directamente. El atacante manipuló precio usando flash loans, tomó posiciones que eran beneficiosas solo con precio manipulado, y extrajo ~$600,000. El ataque podía ejecutarse repetidamente (y fue ejecutado múltiples veces con variaciones) porque la vulnerabilidad fundamental no fue parcheada inmediatamente.

Los protocolos DeFi modernos han aprendido: el uso de precio spot de un DEX para operaciones financieras significativas es considerado anti-patrón. Cualquier fuente de precio que puede ser manipulada dentro de una transacción es inadecuada para decisiones de seguridad críticas.

### Time-Weighted Average Price (TWAP)

Los TWAPs promedia precio sobre período de tiempo (por ejemplo, últimos 30 minutos). Esto hace manipulación más costosa: atacante necesitaría sostener precio manipulado por múltiples bloques, pagando fees y riesgo de mercado. Uniswap V2 y V3 proporcionan TWAPs implementados eficientemente on-chain mediante tracking de precio cumulativo.

Los TWAPs no son invulnerables. Si período de tiempo es corto o liquidez en pool es baja, manipulación es más factible. Los atacantes pueden intentar manipular precio gradualmente sobre período pre-TWAP, luego ejecutar exploit cuando TWAP finalmente refleja precio manipulado. Sin embargo, TWAPs son significativamente más robustos que precio spot.

Los protocolos deben configurar período TWAP apropiadamente: lo suficientemente largo para resistir manipulación práctica (típicamente 10-30 minutos) pero no tan largo que precio quede peligrosamente desactualizado en mercados volátiles. Este balance depende de liquidez del activo, volatilidad histórica y criticidad de precisión de precio.

### Oráculos descentralizados: Chainlink

Chainlink es el oráculo descentralizado más ampliamente usado, proporcionando feeds de precio agregados desde múltiples fuentes off-chain. Múltiples nodos independientes reportan precios, y valor mediano se publica on-chain. Esta agregación hace manipulación extremadamente difícil: atacante necesitaría comprometer mayoría de nodos o fuentes de precio subyacentes.

Los feeds de Chainlink son actualizados basado en threshold de desviación (si precio cambia más de X%) y heartbeat de tiempo (al menos cada Y segundos). Esto balancea costos de gas de actualizaciones con requerimientos de frescura de datos. Los contratos consultando Chainlink deben verificar freshness: rechazar datos si timestamp es demasiado antiguo, indicando que oracle no está actualizándose apropiadamente.

Las limitaciones incluyen dependencia en infraestructura off-chain (nodos de oracle, fuentes de datos), posible latencia en actualizaciones durante volatilidad extrema y costos de operación de feeds (subsidados por Chainlink Labs para muchos feeds principales pero eventualmente requiriendo sostenibilidad económica).

### Diseño defensivo en profundidad

Los contratos críticos frecuentemente usan múltiples fuentes de precio redundantes. Ejemplo: precio principal desde Chainlink, con sanity checks contra TWAP de Uniswap. Si discrepancia excede threshold, transacción revierte o entra modo conservador. Esto protege contra fallo de cualquier fuente individual o intento de manipulación.

Los circuit breakers automáticos pausan operaciones si precio reportado se desvía dramáticamente desde precio reciente histórico o desde mediana de múltiples fuentes. Esto previene explotación durante eventos de oracle anómalos (bug en oracle, manipulación exitosa, fuente de datos upstream comprometida).

Los contratos deben diseñarse asumiendo que oráculos pueden fallar, ser manipulados o proporcionar datos incorrectos. La defensa en profundidad con múltiples verificaciones, límites y fallbacks es esencial para operaciones financieras de alto valor.

## Ataques de denegación de servicio

Los ataques de denegación de servicio (DoS) en smart contracts buscan hacer contrato no funcional o extremadamente costoso de usar, sin necesariamente robar fondos directamente. Estos ataques explotan limitaciones de gas, comportamientos de revert y patrones de diseño incautos.

### DoS mediante revert

Algunos contratos distribuyen fondos a conjunto de destinatarios en loop. Si cualquier destinatario rechaza transferencia (mediante reverting en fallback), el loop completo falla, bloqueando distribución a todos. Un participante malicioso puede denegar servicio a todos mediante rechazo de su porción.

```solidity
// VULNERABLE a DoS
function distributeRewards(address[] memory recipients) public {
    for (uint i = 0; i < recipients.length; i++) {
        (bool success, ) = recipients[i].call{value: reward}("");
        require(success, "Transfer failed"); // Si uno falla, todos fallan
    }
}
```

Solución: usar patrón pull-over-push. En lugar de empujar fondos a destinatarios, permitir que reclamen activamente. Cada destinatario llama función separada para retirar su porción. Fallo de un retiro no afecta disponibilidad para otros.

```solidity
// SEGURO: patrón pull
mapping(address => uint) public pendingRewards;

function claimReward() public {
    uint reward = pendingRewards[msg.sender];
    require(reward > 0, "No reward");
    pendingRewards[msg.sender] = 0;
    (bool success, ) = msg.sender.call{value: reward}("");
    require(success, "Transfer failed");
}
```

### DoS mediante consumo de gas

Los loops sobre estructuras de datos no acotadas pueden consumir gas ilimitado. Si array crece suficientemente, transacciones que iteran sobre ella exceden límite de gas de bloque, haciendo función inoperante.

```solidity
// VULNERABLE: loop no acotado
address[] public participants;

function rewardAll() public {
    for (uint i = 0; i < participants.length; i++) {
        // operación para cada participante
    }
}
```

Si `participants` crece a miles de entradas, `rewardAll()` puede requerir más gas que límite de bloque, haciendo función permanentemente inoperable. Solución: evitar loops no acotados. Usar procesamiento por batch con paginación, permitir operaciones individuales, o usar estructuras de datos que escalan (merkle trees para membership proofs en lugar de arrays on-chain).

### Block stuffing

Un atacante adinerado puede llenar bloques completos con sus propias transacciones (ofreciendo fees extremadamente altos), previniendo que transacciones de otros usuarios sean incluidas. Esto puede usar para denegar acceso a funciones time-sensitive: liquidaciones, opciones expirando, subastas cerrando.

Esto es ataque económico más que vulnerabilidad de contrato. La defensa es limitada: diseño de contratos debe minimizar dependencia en timing preciso, proporcionar ventanas de tiempo extensas para operaciones críticas y considerar mecanismos off-chain de coordinación donde apropiado.

## Funciones administrativas y control de acceso

Las funciones administrativas en contratos controlan parámetros críticos: tasas, límites, direcciones de destino de fondos, pausability. Los ataques contra control de acceso buscan obtener privilegios administrativos no autorizados, permitiendo al atacante reconfigurar contrato maliciosamente, drenar fondos o destruir funcionalidad.

### Problemas comunes de control de acceso

La verificación insuficiente de propietario permite llamar funciones privilegiadas sin validación apropiada. Código olvidando `onlyOwner` modifier o implementándolo incorrectamente es vulnerable directo.

```solidity
// VULNERABLE: falta verificación
function setFeeRate(uint newRate) public {
    feeRate = newRate; // Cualquiera puede cambiar!
}

// CORRECTO: verificación de propietario
function setFeeRate(uint newRate) public onlyOwner {
    feeRate = newRate;
}
```

La inicialización insegura permite a atacante front-run deployment y llamar función initialize antes que owner legítimo, estableciéndose como owner. Los contratos proxy son particularmente vulnerables: lógica está separada de almacenamiento, y inicialización debe ocurrir en transacción separada después de deployment.

```solidity
// VULNERABLE: inicialización no protegida
function initialize(address _owner) public {
    owner = _owner; // Cualquiera puede llamar primero!
}

// CORRECTO: inicialización protegida
bool private initialized;

function initialize(address _owner) public {
    require(!initialized, "Already initialized");
    owner = _owner;
    initialized = true;
}
```

OpenZeppelin proporciona `Initializable` que implementa protección de inicialización robusta, incluyendo prevención de re-inicialización y verificación de versión para upgrades.

### Roles granulares vs owner omnipotente

El patrón tradicional de `owner` único con control total es punto único de fallo. Si clave privada del owner es comprometida, atacante obtiene control completo. Diseño moderno usa roles granulares donde diferentes funciones requieren diferentes permisos.

OpenZeppelin AccessControl implementa sistema de roles flexible. Defines roles específicos (`PAUSER_ROLE`, `MINTER_ROLE`, `UPGRADER_ROLE`) y asignas a diferentes addresses. Cada función verifica rol específico requerido. Esto implementa principio de mínimos privilegios: entidades tienen solo permisos necesarios para sus funciones.

```solidity
import "@openzeppelin/contracts/access/AccessControl.sol";

contract SecureVault is AccessControl {
    bytes32 public constant WITHDRAWER_ROLE = keccak256("WITHDRAWER_ROLE");
    bytes32 public constant PAUSER_ROLE = keccak256("PAUSER_ROLE");
    
    constructor() {
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
    }
    
    function withdraw(uint amount) public onlyRole(WITHDRAWER_ROLE) {
        // solo WITHDRAWER puede retirar
    }
    
    function pause() public onlyRole(PAUSER_ROLE) {
        // solo PAUSER puede pausar
    }
}
```

La separación de roles limita impacto de compromiso de cualquier clave individual. Si PAUSER es comprometido, atacante puede pausar contrato (disruptivo pero no roba fondos). Si WITHDRAWER es comprometido pero no PAUSER, owner puede pausar contrato antes de que atacante drene fondos.

### Timelocks y gobierno descentralizado

Los timelocks retrasan ejecución de funciones administrativas, proporcionando ventana de tiempo para que comunidad detecte cambios maliciosos y responda. Cuando admin propone cambio (por ejemplo, actualizar dirección de fee recipient), cambio no ejecuta inmediatamente. Espera período (24-48 horas típicamente). Si cambio es malicioso, usuarios pueden exit durante timelock.

OpenZeppelin TimelockController implementa sistema de timelock robusto. Operaciones se programan con delay mínimo configurable. Durante período de delay, operación es visible on-chain pero no ejecutable. Después de expiración de delay, cualquiera puede ejecutar operación programada. Mecanismo de cancelación permite admin legítimo cancelar operación si fue iniciada maliciosamente.

Los DAOs frecuentemente usan gobernanza descentralizada donde cambios requieren votación de holders de tokens. Esto descentraliza control, previniendo que cualquier individuo único actúe maliciosamente. Sin embargo, gobernanza introduce complejidades propias: ataques de whale, voter apathy, manipulación de propuestas. Diseño de gobernanza es campo completo de estudio en diseño de protocolos blockchain.

## Mejores prácticas y testing

Las vulnerabilidades en smart contracts no son inevitables. Prácticas de desarrollo disciplinadas, uso de librerías probadas en batalla, testing comprehensivo y auditorías profesionales pueden prevenir la vasta mayoría de bugs catastróficos.

### Uso de librerías estándares

OpenZeppelin Contracts es la librería más ampliamente usada y auditada de implementaciones estándares. Implementar tu propia versión de ERC20, access control, pausability o reentrancy guards es reinventar rueda con riesgo enorme de bugs. Usa OpenZeppelin a menos que tengas razón excepcionalmente buena para no hacerlo.

La API de OpenZeppelin es diseñada con seguridad como prioridad. Modificadores como `nonReentrant`, `onlyOwner`, `whenNotPaused` proporcionan protecciones probadas en batalla. Contratos base como `Ownable`, `Pausable`, `ReentrancyGuard` han sido usados en miles de contratos manejando miles de millones de dólares sin incidentes mayores.

Mantén dependencias actualizadas. OpenZeppelin emite patches de seguridad cuando vulnerabilidades son descubiertas. Usa herramientas de dependency management apropiadas y actualiza regularmente, verificando release notes para security advisories.

### Testing comprehensivo

Los unit tests verifican comportamiento de funciones individuales bajo condiciones normales y edge cases. Cada función pública debe tener tests cubriendo casos exitosos, fallos esperados (reverts apropiados) y límites (valores máximos, mínimos, cero).

Los integration tests verifican interacciones entre contratos múltiples. Protocolos complejos con dependencias entre contratos requieren testing de flujos completos end-to-end, verificando que invariantes se mantienen a través de operaciones complejas.

Los fuzzing tools generan inputs aleatorios o semi-aleatorios, ejecutando funciones con combinaciones inesperadas de parámetros. Echidna y Foundry's fuzzer son herramientas populares. Fuzzing descubre edge cases que desarrolladores no consideraron manualmente.

Los tests de cobertura de código miden qué porcentaje de código es ejecutado por test suite. La cobertura 100% no garantiza ausencia de bugs pero cobertura baja garantiza presencia de código no tested. Herramientas como Solidity Coverage generan reportes de cobertura.

### Auditorías profesionales

Las auditorías por firmas especializadas (Trail of Bits, ConsenSys Diligence, OpenZeppelin, Quantstamp, CertiK) son estándar para protocolos manejando valor significativo. Los auditores expertos revisan código línea por línea, buscan vulnerabilidades conocidas, verifican que mejores prácticas son seguidas y frecuentemente usan herramientas de análisis formal.

Las auditorías no son garantía absoluta de seguridad. Código auditado ha sufrido hacks. Sin embargo, auditorías reducen dramáticamente probabilidad de vulnerabilidades mayores. Las auditorías múltiples por firmas independientes son aún mejores: cada equipo trae perspectivas y experticias diferentes.

Los programas de bug bounty incentivan a investigadores independientes a buscar vulnerabilidades después de deployment. Immunefi, HackerOne y programas custom ofrecen recompensas significativas (frecuentemente $100k-$1M+ para bugs críticos) a quien descubra y reporte responsablemente vulnerabilidades. Este crowdsourced security testing añade capa adicional de escrutinio.

### Prácticas de desarrollo seguro

El desarrollo iterativo despliega primero a testnet, observa comportamiento real bajo condiciones de red, luego despliega a mainnet con límites inicialmente bajos, incrementando gradualmente a medida que confianza crece. Los lanzamientos big-bang con todo valor desde día uno maximizan impacto de cualquier bug no descubierto.

Las pausas de emergencia permiten a admin detener operaciones si vulnerabilidad es descubierta post-deployment. OpenZeppelin Pausable implementa esto mediante modifier `whenNotPaused`. Usa juiciosamente: pausability es poder centralizado que contradice descentralización, pero puede prevenir pérdidas catastróficas.

Los límites de rate y caps limitan daño potencial. Contratos pueden imponer máximos por transacción, por período de tiempo o totales. Si bug permite drenaje, estos límites restringen cuánto puede extraerse antes de detección y respuesta.

El monitoreo continuo observa contratos desplegados en busca de comportamiento anómalo. Las herramientas como Forta, OpenZeppelin Defender y monitoring custom detectan patrones sospechosos: transacciones inusualmente grandes, cambios de estado inesperados, calls desde direcciones no reconocidas. Las alertas tempranas permiten respuesta antes de explotación completa.

## Conclusión: Paranoia justificada

En desarrollo de smart contracts, la paranoia no solo está justificada sino que es requisito profesional. Cada línea de código debe escribirse asumiendo que atacantes leerán, analizarán e intentarán explotar. Los bugs que en desarrollo tradicional serían inconvenientes menores aquí resultan en pérdidas financieras permanentes. No hay parches de emergencia después de deployment en blockchain inmutable.

Las mejores prácticas documentadas aquí no son opcionales ni exageraciones. Son lecciones aprendidas mediante pérdida acumulada de miles de millones de dólares en exploits reales. Cada patrón de defensa existe porque alguien no lo siguió y pagó el precio. Los desarrolladores que ignoran estas lecciones están condenados a repetir errores catastróficos de pioneros.

La buena noticia es que herramientas, librerías y conocimiento comunitario han madurado significativamente. Los desarrolladores modernos no necesitan descubrir estos patrones independientemente; están codificados en OpenZeppelin, documentados extensivamente, y enseñados en programas educativos. Sin embargo, conocimiento sin aplicación disciplinada es inútil. La seguridad requiere vigilancia constante, humildad sobre límites de tu conocimiento, y voluntad de invertir tiempo en testing, auditorías y aprendizaje continuo.

El futuro de finanzas descentralizadas, economías de DAOs y contratos programáticos depende fundamentalmente de seguridad de smart contracts. Cada bug mayor erosiona confianza, atrae escrutinio regulatorio y retarda adopción. Los desarrolladores que toman seguridad seriamente no solo protegen usuarios individuales sino que contribuyen a credibilidad y viabilidad del ecosistema completo. Esta responsabilidad es inmensa, pero también es privilegio de construir infraestructura financiera del futuro.
