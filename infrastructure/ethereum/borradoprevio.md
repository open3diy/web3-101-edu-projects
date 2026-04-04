# El stack para Account abstraction en Ethereum

Account abstraction surge como necesidad de mejorar la experiencia de usuario... etc .. mejorar intro

La base técnica sobre la que se construye es el concepto de [Smart Contract Wallet (SCW)](https://defiantapp.medium.com/qu%C3%A9-son-las-smart-contract-wallets-bf558c2b915c): una cuenta gestionada por código en lugar de una clave privada estática de la EOA. A diferencia de las EOAs tradicionales, una SCW puede definir sus propias reglas de validación, delegar autorización de forma programable y ejecutar lógica compleja antes de confirmar cualquier operación. Proyectos como Safe demostraron el potencial de este modelo años antes de que existiera un estándar unificado, pero su adopción quedaba limitada a casos avanzados por la complejidad de integración que suponía para cada DApp.

La visión de AA, como [explica MetaMask](https://support.metamask.io/configure/accounts/what-is-a-smart-account), consiste precisamente en hacer que las SCW sean el modelo por defecto en lugar de la excepción. Esto desbloquea capacidades imposibles con EOAs tradicionales: recuperación social nativa o login social, inicio de sesion con passkeys, límites de gasto programables, multi-firma nativa, listas blancas (listas de confianza), firmas en lotes con session keys para autorizar operaciones repetidas sin firmar cada una individualmente, la legibilidad de lo que firmas, automatización (como pagos recurrentes), y crucialmente, la capacidad de que alguien más (un patrocinador) pague el gas por ti o pagar gas con otro token diferente.

**Inicio con ERC-7337**:

Inicialmente [ERC-4337](https://eips.ethereum.org/EIPS/eip-4337) (2023) estandarizó el acceso a las SCW sin modificar el protocolo base de Ethereum: cualquier aplicación podía integrarse con smart accounts siguiendo ese estándar, sin depender de cambios en el consenso de la red. La limitación era que los usuarios con EOAs tradicionales tenían que migrar a una nueva dirección de smart account para beneficiarse, lo que supuso una barrera de adopción significativa dibde perdina su historia y reputacion de su EOA, porque lo cierto es que la idea tambien era que podrias rotar de claves, la EAO se entendía sola como una credencial de acceso, además este modelo se apoyaba en una mejor integracion de acceso con passkey o recuperación social que podria autorizarse al SCW

Esto trajo no solo un nuevo tipo de smart contract (SCW) en la blockchain, tambien un cambio de paradigma en la propia Dapp y en la creación de una infraestructura subyacente. Por una parte, ya no hablaamos de la DApp conectada a una red y la wallet que envia a la red conectada, hablamos de algo mas...

Por una parte la wallet inicialmente seguia siendo agnostica al cambio, pero para cada cuenta EAO, usando el patron proxy, se despliega un SCW para la cuenta usando el patron factoria donde la cuenta EOA es el owner, y esto es importante porque es lo que hace que la cuenta te pertenezca, junto a otras adicionales.

La Dapp genera lo que se denomimado UserOperations y la wallet es solo usada para firmar el mensaje que es como un envoltorio para que un tercero haga el tramite, siendo la Dapp quien envia la peticion a un tercero, no existe transaccion a la red.

Esa UserOperation envuelve todo lo necesario, pero ¿que es necesario? la user operations incluye por su puesto el callData al contrato desinto, pero puede incluyir las evidencias del pago de gas con Paymaster o pago con otro token, validaciones mejoradas como passkeys para autorizar la firma en lote, es decir, cualquier necesidad,que habilita una mejor esperiencia.
Ademas tenemos que aclarar, cuando decimos evidencia del paymaster, es que esta operación es off-chain, usas un proveedor como ... el que te proporciona uan firma firma sobre el pago de gas, que luego será validado y aplicado on-chain.

Ese tercero es el bundlers o agrupador agrupan: Recibe UserOperation en una mempool, La valida off-chain (simulación),  La mete en un alt mempool, Selecciona cuáles incluir,  Agrupa varias UserOperation y lo envía a un nuevo contrato de la red llamda EntryPoint

EntryPoint o punto de acceso, es el contrato estándar que recibe las UserOperation, coordina su validación y ordena su ejecución on-chain.
Normalmente lo despliega el equipo / mantenedores de la implementación de referencia de 4337.
Recibe las peticiones de los bundlers que son UserOperations, es como el centro de operaciones, las manda validar al SCW, como la delegacion, realiza las operaciones adicionales AA como pago de gas con Paymaster y envía la transaccion al SCW.

Desde la perspectiva del usuario, la experiencia es fluida; desde la perspectiva técnica, su UserOperation viaja muchas veces a un endpoint concreto que la procesa, empaqueta y envía a la blockchain. Esto no invalida la seguridad del sistema —las garantías criptográficas del contrato se mantienen— pero sí significa que, en muchas implementaciones reales, la infraestructura subyacente sigue dependiendo de APIs y operadores específicos, más que de una red P2P abierta y homogénea como Ethereum.

**El ecosistema normaliza: EIP-7702**:

Ante este panorama, una propuesta de cambio de la red tubo ejefecto, con la actualizacion Pectra 2025, este flujo se mejora y estandariza mediante [ERC-7702](https://eips.ethereum.org/EIPS/eip-7702). Se puede resumir que funcionalmente permite que delegemos la ejecucion de nuestra cuenta EAO en un SCW que peude ser temporal o persistente, sin que perdamos nuestra dirección de origen EOA y sobre todo habilitando funciones SCW a viejas direcciones que no fueran creados con ERC-4337, algor fundamental para no perder reputación.

Un poco mas en detalle, una nueva transaccion de tipo 4 con una authorization_list permite una persistencia de delegacion para futuras transacciones (aunque no sean tipo 4) o sino no es persistente con delegacion para esa sesion en la transaccion. Es por esto por lo que se dice que EIP-7702 permite que tú wallet tenga codigo, no es eso exactamente, es que tu EOA puede usar una SCW on-chaim pudiendo usar tu propia dirección de EOA temporalmente para esa transaccion.

Las motivaciones de EIP-7702 se centra en batching, gas sponsor y escakad de privilegios (privilege de-escalation) que tiene su implementación en [session keys](session-keys.md). 

Existen quizas no incompatibilidades, pero si donde este modelo se adapta peor al ser la cuenta EOA la que referencia el SCW, por una parte las firmas multisig se complican, quizas aqui es mejor confiar en wallets ERC-4337 puras como Safe. Igualmente otroas cuentas propietarias como passkey, recuperación social se resuelven peor, asi que aqui hay tambien un cambio de de paradigma. Realmente hay un cambio de diseño, quizás más logico, lo vemos en wallets como metamask, donde el [login social](https://metamask.io/es/news/introducing-metamask-social-login) forma parte de la wallet y no del SCW, cosa que igual tiene mas sentido, donde se usa soluciones descentralias, segun su caso, como MPC, etc. Aunque tenemos que aclarar que soluciones como Safe aun siguen el modelo anterior, no se puede decir que exista un cambio unico, lo que sí parece que EIP-7702 simplifico esto tambien para muchos casos nuevos.

La autorizacion habilita tambien un cambio de paradigma a ERC-4337, no tiene porque ser una infraestructura compleja de bundlers, permite que exisnta relayers u otros servicios de terceros que paguen gas por nosotros, etc y que tengan su propia infraestructura y la autorización de EIP-7702 habilita que podamosa autorizarlo facilmente sin el entrypoint.

AUnque existe un nuevo modelo, tenemos que aclarar que la infraestructura ERC-4337 no desaparece, simplemente se adapta, los bundlers siguen existiendo e incluso los entrypoint en la red, quizás mas simples porque pueden pasar la autorizacion, asi que en muchos casos tenemos esa misma infraestructura  y en la practica es la misma e incluso por practicidad usan el mismo objeto UserOperation para su uso.

Por parte de la  wallet, ya no es agnositca, e igualmente la DApp debe prepararse a este nuevo tipo de operaciones.

Para que funcione la wallet necesita soportar el stack de comunicación que lo hace posible:

- **[EIP-5792](https://eips.ethereum.org/EIPS/eip-5792)** (`wallet_sendCalls`): permite que la DApp indique a la wallet "envía estas N llamadas como un lote". Sin esto, no hay forma estándar de coordinar batch calls entre DApp y wallet.
- **[EIP-7677](https://eips.ethereum.org/EIPS/eip-7677)**: permite que la wallet coordine con un paymaster externo para que el gas lo pague el relayer, no el usuario.
- **[EIP-7702](https://eips.ethereum.org/EIPS/eip-7702)**: permite que una EOA delegue ejecución a lógica de contrato, habilitando lotes y lógica programable sin cambiar de dirección.

Para encontrar wallets que soporten este stack, directorios como [ethereum.org wallets](https://ethereum.org/es/wallets/find-wallet/) o el [directorio de DApps de Alchemy](https://www.alchemy.com/dapps/top/wallets?childCategories=Smart+Contract+Wallets) permiten filtrar por "Smart Contract Wallets". Este filtro es la forma más directa de distinguir wallets que soportan patrocinación de gas, recuperación social o permisos granulares de las que no lo hacen.

**Lo que la wallet ofrece y lo que no**:

Hablamos de account abstraction en el proceso de experiencia de usuario, como forma de coordinar on-chain, pero no todo es on-chain, mucho ocurre off-chain y en primer lugar en la wallet. Aqui podemos ver qué ofrece AA y que no:

Ofece como vimos en motivaciones: paymaster / sponsor, batching de mensajes, ejecucion delegaga mucho mas acotada, con sessio keys como ejemplo fecha límite, solo para contrato X, máximo 0.1 ETH, 
    
Lo que no ofrece y suele ser parte de la DApp, mensajes mas claros, listas visuales de direcciones permitidas, alertas, limites sugeridas, simulacion previa

### Capacidades fundamentales de Account Abstraction

La transición de EOA a Smart Contract Wallet desbloquea un conjunto de capacidades que redefinen lo posible en UX blockchain. A diferencia de una EOA donde cada acción requiere una firma manual inmediata, una SCW puede implementar lógica programable que automatiza, protege y simplifica la interacción sin comprometer la custodia.

**Operaciones atómicas:**

Muchas operaciones en Web3 requieren múltiples pasos encadenados: primero aprobar el gasto de un token, después ejecutar el swap, a veces confirmar un destino adicional. En el modelo EOA, cada paso es una transacción independiente que el usuario debe firmar por separado, con el riesgo de que el estado cambie entre pasos o de que la aprobación quede huérfana si la segunda transacción falla. AA agrupa estas llamadas en una única transacción atómica: o todos los pasos tienen éxito o ninguno se aplica. Más allá de la comodidad, esto elimina vectores de ataque que explotan el estado intermedio entre aprobaciones, como el front-running sobre autorizaciones de tokens expuestas en el mempool.

**Session keys y autorización delegada:**

Cuando el patrón no es una operación puntual sino interacciones repetidas, la fricción cambia de naturaleza. Si juegas a un juego blockchain donde cada movimiento es una transacción, firmar con tu wallet cada cinco segundos destruye la experiencia. Las session keys resuelven esto delegando autorización temporal. El mecanismo es conceptualmente similar a dejar la llave de tu casa a un amigo para que riegue las plantas: no le das control permanente, sino permiso limitado para una acción específica durante un tiempo acotado. Tu smart account genera una clave temporal con permisos estrictos, por ejemplo "interactuar con el contrato del juego X gastando hasta 10 USDC durante las próximas 24 horas". El juego usa esa clave para ejecutar transacciones sin pedir aprobación constante, pero no puede acceder al resto de tus fondos ni operar fuera del contexto autorizado. Este patrón no solo mejora gaming; es fundamental para aplicaciones sociales donde publicar, dar like o comentar pueden requerir microtransacciones constantes on-chain.

**Límites de gasto programables:**

Puedes configurar que ninguna transacción superior a 100 USDC se ejecute sin autenticación biométrica adicional, que transferencias a direcciones nuevas requieran confirmación mediante un segundo dispositivo, o que ciertos contratos en listas blancas de seguridad comunitarias operen sin restricción mientras que interacciones con contratos desconocidos disparen alertas. En Web2, si alguien obtiene tu contraseña puede hacer daño limitado porque existen mecanismos de reversión. En Web3 tradicional, si alguien obtiene tu clave privada, puede vaciar tu wallet irreversiblemente en segundos. Con límites programables, incluso si un atacante compromete tu sesión, el daño potencial está acotado: solo puede gastar hasta el límite configurado antes de que el sistema bloquee más transacciones y te alerte.

**Multi-firma y listas blancas:**

La multi-firma nativa permite que una wallet requiera aprobación de múltiples claves antes de ejecutar transacciones críticas, sin necesidad de contratos externos. Esto es fundamental para gestión corporativa o tesorería de DAOs donde ningún individuo debería tener control unilateral. Las listas blancas (allowlists) permiten definir direcciones o contratos de confianza que pueden operar sin restricciones adicionales, mientras que interacciones con entidades no verificadas disparan validaciones extra. Esta capacidad es particularmente útil para usuarios no técnicos que pueden pre-aprobar aplicaciones auditadas por la comunidad, reduciendo la superficie de ataque sin requerir expertise sobre cada transacción individual.

**Automatización:**

La posibilidad de programar pagos recurrentes, rebalanceos periódicos de portfolio, o cualquier lógica condicional ejecutable sin intervención manual. Por ejemplo, una DApp de suscripción puede cobrar mensualmente de forma automática, o una estrategia de inversión puede vender activos cuando alcanzan cierto precio, sin que el usuario tenga que firmar cada operación manualmente. Esto replica la experiencia de domiciliación bancaria o trading automatizado que los usuarios esperan, sin centralizar la custodia.

### Gestión de gas sin fricciones

El problema circular histórico de Web3 es que necesitas poseer la criptomoneda nativa de una cadena (ETH, MATIC, etc.) para pagar gas antes de poder operar, pero para obtener esas monedas primero necesitas ejecutar transacciones. AA desbloquea dos soluciones complementarias que eliminan esta barrera.

**Sponsorship de gas (paymasters):**

Los paymasters son contratos que pagan el gas en nombre del usuario. Históricamente, Wallet-as-a-Service lo resolvió de forma centralizada: el proveedor paga el gas y después te cobra. AA lo descentraliza: cualquier aplicación puede integrar un paymaster sin custodiar fondos del usuario. Un juego blockchain puede permitir que nuevos jugadores reclamen su primer NFT sin poseer ninguna criptomoneda, pagando el protocolo el coste de gas. Un exchange descentralizado puede subsidiar el gas para usuarios que aporten liquidez significativa. Una DAO puede cubrir los costes de gobernanza para que votar no sea una barrera económica. Este patrón elimina la fricción de entrada más citada en encuestas de adopción.

**Pago de gas en cualquier token:**

Más sofisticado aún, con AA puedes pagar comisiones en USDC aunque la red requiera ETH: tu smart account autoriza al paymaster a tomar USDC de tu saldo, el paymaster paga el gas en ETH, y el intercambio se resuelve internamente mediante un swap atómico. El usuario nunca percibe la conversión ni necesita gestionar múltiples tokens para gas. Esto es especialmente transformador en entornos cross-chain donde cada red requiere su propia moneda nativa: el usuario mantiene un único saldo en stablecoins y la infraestructura resuelve transparentemente el pago de gas en cualquier cadena.

## Descentralización real: quién puede participar y cómo

Account Abstraction introduce una capa de infraestructura con un modelo de participación que no tiene el mismo precedente claro que Ethereum. En Ethereum, la pregunta "¿cómo participo en la red?" tiene una respuesta concreta: descargas un cliente como Geth o Lighthouse, sincronizas la cadena y, si quieres validar, haces stake de 32 ETH o delegas a un pool. Es técnicamente exigente, pero el camino está definido y el protocolo tiene incentivos explícitos para atraer a ese tipo de participante.

En el ecosistema de Account Abstraction, la pregunta se fragmenta en roles distintos, cada uno con requisitos y barreras propias.

Cualquiera puede técnicamente ejecutar un bundler. Existen implementaciones de referencia en código abierto como el [bundler de infinitism](https://github.com/eth-infinitism/bundler) o Rundler, el bundler de Alchemy. Pero en la práctica, operar un bundler competitivo exige capital para adelantar el gas de las UserOperations antes de recuperarlo, infraestructura siempre disponible con baja latencia y capacidad técnica para gestionar el mempool alternativo de ERC-4337.

Aunque hoy existen implementaciones más maduras y se han desplegado mempools compartidos reales en varias redes, la descentralización operativa sigue estando lejos de la de Ethereum L1. El estándar existe, pero la adopción de una red verdaderamente abierta y neutral entre wallets, bundlers y paymasters sigue siendo desigual y dependiente de proveedores concretos.

Los paymasters son aún más diferentes: no son nodos de red, sino cuentas financiadas con ETH que un operador —un protocolo, una empresa o una dApp— despliega para patrocinar el gas de sus usuarios. No hay forma de "unirse" a la red de paymasters como usuario individual interesado en la salud del ecosistema; se trata de proveedores de servicios con un modelo de negocio propio.

Los solvers, por su parte, requieren gestión activa de liquidez en múltiples cadenas, estrategias de ejecución sofisticadas y capital suficiente para cubrir posiciones abiertas entre cadenas. Es un mercado técnico y financiero, no una infraestructura de participación abierta.

El resultado práctico es que Account Abstraction, tal como está desplegado hoy, no es una red P2P en el sentido en que lo es Ethereum. No tiene todavía incentivos de protocolo equivalentes al staking, no tiene un mecanismo de descubrimiento universal entre wallets y bundlers, y su infraestructura operativa real sigue concentrada en pocos proveedores. Esto no es accidental ni ignorado: ERC-4337 fue diseñado deliberadamente para no requerir cambios en la capa 1 de Ethereum, porque eso permitía desplegarlo sin una hard fork y hacerlo funcionar de inmediato. El precio de esa pragmaticidad fue exactamente esta ausencia de incentivos y descentralización estructural.

La comunidad es consciente del problema. Una línea de trabajo como [RIP-7560 (Native Account Abstraction)](https://ethereum-magicians.org/t/rip-7560-native-account-abstraction/16664) busca resolver esto en profundidad integrando la abstracción de cuentas de forma más nativa en el protocolo de Ethereum, lo que permitiría un mempool P2P más real para UserOperations, incentivos más directos para la infraestructura de ejecución y una menor dependencia de servicios externos. Sin embargo, este camino sigue siendo una dirección técnica relevante más que una pieza cerrada e inminente del roadmap principal.

En la práctica, el ecosistema ha adoptado la postura de "desplegar primero, descentralizar después", una pauta habitual en Web3 que a veces se cumple y a veces queda pendiente indefinidamente.

La pregunta de si este es un elefante en la habitación o un problema en vías de solución depende del horizonte temporal que se considere. A corto plazo, es una limitación estructural real que conviene tener presente al evaluar la resiliencia de cualquier sistema que dependa de esta infraestructura. A largo plazo, hay trabajo técnico serio orientado a resolverlo. Lo que no existe, todavía, es un camino claro y comprometido entre los dos puntos.

## Ecosistema y seguimiento de la adopción

El ecosistema de Account Abstraction ha generado una infraestructura de recursos paralela que resulta útil tanto para desarrolladores como para analistas.

[Awesome Account Abstraction](https://github.com/4337Mafia/awesome-account-abstraction) es un repositorio comunitario que funciona como directorio curado del ecosistema ERC-4337: reúne wallets compatibles, bundlers activos, paymasters, SDKs, ejemplos de contratos y artículos técnicos de referencia. Su valor está en la amplitud y la curaduría — en lugar de buscar fragmentado por la red, este repositorio actúa como punto de entrada único para cualquier desarrollador que quiera construir sobre Account Abstraction o simplemente orientarse en el ecosistema.

[BundleBear](https://www.bundlebear.com/erc4337-account-activation/all) ofrece una dimensión distinta: métricas en tiempo real sobre la adopción real de ERC-4337 en producción. Rastrea el número de cuentas activadas, UserOperations procesadas, bundlers activos y paymasters desplegados por cadena y en el tiempo. Su utilidad principal es empírica: permite contrastar el discurso teórico sobre Account Abstraction con los datos reales de uso, observar qué cadenas lideran la adopción y entender el ritmo al que el ecosistema avanza en la práctica.

## Guía de referencia para el desarrollador de DApps con AA

El análisis previo describe el ecosistema desde la perspectiva del usuario. Esta sección sintetiza las implicaciones prácticas para el equipo que construye la DApp: qué debe cambiar en el contrato, qué debe cambiar en el frontend y qué herramientas existen hoy para hacerlo sin implementar cada pieza desde cero.

### Lo que debe cambiar en el contrato inteligente

La mayoría de contratos escritos antes de la era AA asumen implícitamente que el caller es siempre una EOA. Hay dos patrones concretos que rompen la compatibilidad con SCW y que deben auditarse antes de declarar una DApp compatible con AA.

El primero es la comprobación `tx.origin == msg.sender`. Esta línea, históricamente usada como protección contra reentrancy o como verificación de "llamada directa humana", rechaza silenciosamente cualquier SCW porque en ese caso `tx.origin` es la EOA que inició la cadena de llamadas pero `msg.sender` es el contrato de la wallet. El reemplazo correcto depende del propósito original: si la intención era prevenir llamadas desde otros contratos, la solución moderna pasa por lógica explícita de autorización o por adoptar el modelo de sesiones de ERC-4337. La guía de [Ethereum sobre compatibilidad de AA](https://docs.alchemy.com/docs/smart-contract-compatibility-for-account-abstraction) documenta los patrones problemáticos más habituales.

El segundo es la verificación de firmas. Si el contrato verifica firmas con `ecrecover` directamente, es incompatible con todas las SCW. La solución es implementar soporte para [EIP-1271](https://eips.ethereum.org/EIPS/eip-1271): antes de llamar a `ecrecover`, comprobar si la dirección firmante es un contrato; si lo es, llamar a su función `isValidSignature()` para delegar la verificación. OpenZeppelin ofrece el helper [`SignatureChecker`](https://docs.openzeppelin.com/contracts/4.x/api/utils#SignatureChecker) que abstrae esta lógica de forma compatible con ambos modelos (EOA y SCW) sin reescribir la lógica de verificación del contrato.

Para los mensajes que el usuario debe firmar, adoptar [EIP-712](https://eips.ethereum.org/EIPS/eip-712) es el mínimo exigible: estructura el payload en tipos con nombre que las wallets pueden mostrar como campos legibles en lugar de bytes hexadecimales. La wallet ve "Transferir 100 USDC a 0xabc..." en lugar de calldata crudo. Viem expone `signTypedData` y `hashTypedData` para construir y verificar mensajes EIP-712 desde el frontend, y la documentación de [wagmi sobre `useSignTypedData`](https://wagmi.sh/react/api/hooks/useSignTypedData) cubre el patrón completo incluyendo verificación on-chain posterior.

### Lo que debe cambiar en el frontend

El modelo tradicional de envío de transacciones —construir un objeto de transacción, llamar a `eth_sendTransaction`, esperar el hash— sigue funcionando con EOAs pero no aprovecha ninguna capacidad de AA. La transición hacia AA en el frontend ocurre en dos capas.

La primera es adoptar [EIP-5792](https://eips.ethereum.org/EIPS/eip-5792) como interfaz de comunicación con la wallet. En lugar de `eth_sendTransaction`, la DApp usa `wallet_sendCalls` para enviar lotes de operaciones, y `wallet_getCapabilities` para preguntar a la wallet conectada qué soporta antes de intentar cualquier cosa. Este patrón de detección de capacidades con fallback graceful es el núcleo de la compatibilidad agnóstica: si la wallet responde que soporta patrocinado de gas y batch, la DApp activa esas rutas; si no, cae al flujo EOA estándar. [Wagmi](https://wagmi.sh/) soporta EIP-5792 desde la versión 2.x con los hooks `useCapabilities` y `useSendCalls`, lo que convierte esta detección en pocas líneas desde el frontend sin conocer el tipo de wallet conectada.

La segunda capa es elegir un proveedor de infraestructura de bundler y paymaster si se quiere ofrecer patrocinio de gas o experiencia SCW completa independientemente de la DApp del usuario. [Pimlico](https://pimlico.io/) y [Alchemy Account Kit](https://accountkit.alchemy.com/) son los proveedores con mayor adopción en el ecosistema ERC-4337: ofrecen bundlers, paymasters y SDKs de alto nivel que se integran con wagmi o directamente con [viem](https://viem.sh/) para construir `UserOperations` sin gestionar manualmente la lógica del mempool de ERC-4337. [Permissionless.js](https://docs.pimlico.io/permissionless) es la librería de nivel medio que Pimlico mantiene open-source: permite construir smart accounts (Safe, Kernel, Biconomy Nexus) y enviar `UserOperations` con control total sobre cada decisión sin depender de un SDK propietario cerrado.

Para equipos que despliegan en Base y quieren aprovechar el ecosistema ya construido de Coinbase, el [OnchainKit](https://onchainkit.xyz/) y el [Coinbase Smart Wallet SDK](https://www.smartwallet.dev/sdk/intro) ofrecen componentes React listos para usar (botones de conexión, flujos de onboarding con passkeys) con infraestructura de bundler y paymaster operada por Coinbase sin coste adicional para el desarrollador.

### Cómo conectar wallets de forma agnóstica

Más allá de AA, la selección del conector de wallets determina directamente si la DApp padece el problema de la gran dispersión del login descrito antes. El ecosistema ha convergido en dos soluciones principales que implementan [EIP-6963](https://eip6963.org/) —el estándar que permite detectar automáticamente las wallets instaladas por el usuario— como comportamiento por defecto.

[RainbowKit](https://www.rainbowkit.com/) es el conector más utilizado junto a wagmi: muestra automáticamente las wallets que el usuario tiene instaladas, soporta EIP-6963 y WalletConnect para wallets móviles, y ofrece UI configurable. [ConnectKit](https://docs.family.co/connectkit) de Family es la alternativa con diseño más cuidado y soporte nativo para Safe y Coinbase Smart Wallet. [Dynamic](https://www.dynamic.xyz/) y [Privy](https://www.privy.io/) son soluciones de nivel superior orientadas a onboarding progresivo: gestionan tanto wallets externas como Embedded Wallets con login social, y son especialmente relevantes si la DApp quiere soportar usuarios sin wallet previa. La evaluación independiente de [Rabby sobre RainbowKit](https://blog.0xpass.io/p/exploring-rainbowkit-assessing-its) documenta con detalle las limitaciones actuales de cada librería en cuanto a detección y priorización de wallets.

### Compatibilidad, incompatibilidad y degradación graceful

Aplicar todo lo anterior no garantiza experiencia idéntica en todas las wallets, pero sí garantiza que la DApp **siempre funciona** y que nadie queda excluido. El modelo es de degradación controlada hacia abajo, no de paridad hacia arriba.

Hay cuatro medidas y tres perfiles de cuenta posibles, y su cruce determina qué funciona, qué mejora y qué queda sin efecto.

**EIP-6963 — detección de wallets:** compatible universalmente. Una EOA sin AA, una EOA con EIP-7702 y una SCW como Safe o Coinbase Smart Wallet se detectan y aparecen en el selector de la DApp sin configuración adicional. Nadie queda excluido del login por el tipo de wallet que tiene.

**Eliminar `tx.origin == msg.sender` + EIP-1271 — compatibilidad de contratos:** compatible universalmente. Las EOAs funcionan exactamente igual que antes. Las SCW, que antes podían fallar silenciosamente al llamar a contratos que asumían EOA, ahora ejecutan sin errores. Sin estos cambios, un usuario de Safe encontraría la DApp rota sin mensaje de error comprensible.

**EIP-712 — mensajes legibles al firmar:** compatible universalmente en cualquier wallet que implemente el estándar, que incluye MetaMask, Rainbow, Rabby, Safe y Coinbase Smart Wallet. El usuario ve campos con nombre en lugar de calldata hexadecimal independientemente de si tiene una EOA o una SCW.

**EIP-5792 `wallet_getCapabilities` — capacidades de AA:** aquí aparece la diferencia. Una EOA sin soporte 7702 no reporta capacidades avanzadas y la DApp cae al flujo estándar de siempre: el usuario opera normalmente pero sin batch, sin gas sponsoring y sin session keys. Una EOA con EIP-7702 activo reporta las capacidades que su wallet decida exponer, que pueden ser parciales según el proveedor. Una SCW nativa reporta el conjunto completo y la DApp activa operaciones atómicas, pago de gas en stablecoins y session keys para esa sesión.

Lo que esto implica en la práctica: un usuario con MetaMask EOA sin soporte 7702 usa la DApp exactamente igual que siempre, sin errores ni bloqueos, pero sin las mejoras de UX de AA. Un usuario de Safe o Coinbase Smart Wallet obtiene la experiencia enriquecida si la DApp consulta `wallet_getCapabilities` y activa esas rutas. En ningún caso alguien queda excluido por el tipo de wallet que tiene.

La frontera entre compatibilidad plena y degradación no la fija la DApp, la fija la wallet del usuario. La DApp solo decide si detecta esa frontera con `wallet_getCapabilities` y adapta la experiencia en consecuencia, o si la ignora y fuerza a todos al denominador común. Adoptar EIP-5792 es precisamente lo que convierte ese ajuste en automático.

### Referencias para el desarrollador

- [Documentación oficial de EIP-5792](https://eips.ethereum.org/EIPS/eip-5792) — wallet_sendCalls y wallet_getCapabilities
- [Wagmi — useCapabilities y useSendCalls](https://wagmi.sh/react/api/hooks/useCapabilities) — implementación frontend de EIP-5792
- [Permissionless.js](https://docs.pimlico.io/permissionless) — librería open-source para smart accounts con ERC-4337
- [Alchemy Account Kit](https://accountkit.alchemy.com/) — SDK de alto nivel para AA con bundler y paymaster integrados
- [Compatibilidad de contratos con AA](https://docs.alchemy.com/docs/smart-contract-compatibility-for-account-abstraction) — patrones a auditar (`tx.origin`, firmas)
- [OpenZeppelin SignatureChecker](https://docs.openzeppelin.com/contracts/4.x/api/utils#SignatureChecker) — verificación de firmas compatible con EOA y SCW
- [EIP-6963](https://eip6963.org/) — detección multi-wallet en DApps
- [OnchainKit de Coinbase](https://onchainkit.xyz/) — componentes React para Base con AA integrado

---
