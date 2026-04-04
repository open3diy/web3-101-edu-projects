# Web3 como arquitectura híbrida: coordinación off-chain, verificación on-chain

El ecosistema Web3 ha aprendido algo que sus fundadores tardaron en aceptar: la descentralización no es un valor absoluto, sino una herramienta que tiene sentido aplicar donde importa. La presión económica real, más que cualquier ideal, ha sido el motor de esa madurez. El ecosistema ha sobrevivido porque ha aprendido a distinguir dónde la descentralización añade valor sostenible y dónde simplemente añade fricción operativa.

En ese proceso de adaptación ha emergido un patrón arquitectónico que hoy parece consolidado: la blockchain actúa como ancla de seguridad y verificación final, no como motor de toda la experiencia. Alrededor de esa ancla opera una capa de servicios que hace posible la experiencia real de usuario. Y en el centro de ese sistema, tomando decisiones y concediendo autorizaciones, está la wallet.

La wallet ya no es solo un almacén de claves. Es el sistema de permisos personal del usuario: el único lugar donde se expresa la intención, se firma la autorización y se define quién puede actuar en nombre del usuario, bajo qué condiciones y durante cuánto tiempo.

## El sistema de capas del ecosistema

La arquitectura que ha adoptado Web3 descansa sobre tres capas con responsabilidades distintas. Ninguna puede reemplazar a las otras y la solidez del conjunto depende de que cada una haga bien lo que le corresponde.

**La wallet como motor de autorización**:

La cartera gestiona las claves privadas del usuario, pero su función real es mucho más amplia: es el mecanismo de consentimiento. Cuando un usuario firma con [ECDSA](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm), está autorizando una operación concreta de forma criptográficamente verificable. Cuando usa [EIP-712](https://eips.ethereum.org/EIPS/eip-712), estructura esa firma en un formato legible y auditable que el usuario puede revisar antes de aprobar. Las smart contract wallets derivadas de [ERC-4337](https://eips.ethereum.org/EIPS/eip-4337) van más allá y permiten definir políticas programables: límites de gasto por período, listas blancas de contratos autorizados, reglas de aprobación múltiple o [claves de sesión](../../infrastructure/ethereum/session-keys.md) con permisos acotados que no requieren autorización manual en cada operación.

**La infraestructura intermedia como capa de orquestación**:

Entre la wallet y la blockchain existe una capa de coordinación construida con pragmatismo. Se puede organizar en tres grupos según su función.

El primer grupo gestiona el acceso y el enrutamiento: los frontends que presentan la interfaz al usuario y los nodos RPC y APIs que reciben, validan y enrutan las solicitudes hacia la red.

El segundo grupo gestiona la retransmisión y la agrupación de operaciones: los relayers que retransmiten transacciones meta-firmadas sin que el usuario pague gas directamente, los bundlers que agrupan múltiples UserOperations bajo ERC-4337 en una sola transacción on-chain, y los paymasters que pueden asumir el coste del gas en nombre del usuario o aceptar su pago en tokens distintos al nativo.

El tercer grupo gestiona la optimización de la ejecución: los motores de intents como [CoW Protocol](https://cow.fi/) o [UniswapX](https://uniswap.org/whitepaper-uniswapx.pdf), donde una red de solvers compite off-chain para encontrar la mejor forma de cumplir la intención firmada por el usuario, y los indexadores como [The Graph](https://thegraph.com/) que hacen consultable el estado histórico y actual de la blockchain.

Muchos de estos componentes son servicios centralizados, y eso no es un defecto estructural sino una decisión de diseño coherente. La seguridad del sistema no depende de ellos porque no tienen capacidad de alterar el estado de la blockchain ni de mover fondos del usuario sin su firma. Si un proveedor falla, es censurado o desaparece, se puede cambiar por otro sin perder acceso a los activos ni al historial on-chain.

**Los smart contracts como árbitros finales**:

Aquí reside lo esencial. El smart contract verifica de forma autónoma e imparcial si la autorización presentada es válida: comprueba la firma criptográfica, los límites definidos, el nonce para prevenir ataques de repetición y el deadline de validez de la operación. No importa qué servicio retransmitió la transacción ni qué frontend la construyó; la ejecución final no puede ser influida por ninguna capa intermedia. Solo si todas las condiciones son correctas, el contrato actúa.

Este principio es el que mantiene la confianza en todo el sistema: la capa de orquestación puede ser opaca o incluso hostil, pero no puede falsificar una firma ni ejecutar lo que el usuario no autorizó.

## Por qué este patrón es inevitable

La blockchain es excepcionalmente buena en verificación criptográfica, ejecución determinista, consenso distribuido y liquidación final irrevocable. Pero es lenta, costosa y poco adecuada para coordinación de alto volumen o lógica computacional intensiva.

Poner toda la lógica on-chain no es una opción viable: el coste de gas haría imposible la mayoría de casos de uso, y la latencia del bloque haría inaceptable la experiencia de usuario. Pero prescindir de la blockchain como capa de verificación final significaría confiar en intermediarios que pueden actuar de forma arbitraria o fraudulenta.

El patrón de coordinación off-chain con verificación on-chain resuelve exactamente esa tensión. La coordinación ocurre donde es barata y rápida; la verificación ocurre donde es confiable e irrevocable. No es un compromiso: es la única combinación que tiene coherencia económica y que escala hacia usuarios masivos sin sacrificar las garantías que hacen a Web3 diferente.

## ¿Es esto centralización disfrazada?

La pregunta es legítima y merece una respuesta honesta. Que un sistema no sea peer-to-peer en todas sus capas no significa que no sea descentralizado en lo que importa. La soberanía del usuario sobre sus activos e identidad no la garantiza que el frontend sea descentralizado; la garantiza que la blockchain como capa final sea verificable e imparcial.

Dicho esto, el riesgo de disponibilidad y censura existe en los servicios orbitales y ha ocurrido: tras las sanciones a Tornado Cash en 2022, una parte significativa de los builders y relayers de Ethereum empezaron a filtrar transacciones por criterios externos al protocolo. El incidente demostró que la centralización en la capa de orquestación tiene consecuencias reales.

La respuesta del ecosistema va en varias direcciones. A nivel de protocolo, el [roadmap de Ethereum](https://ethereum.org/en/roadmap/) incluye mecanismos de resistencia a la censura como las inclusion lists, que fuerzan a los validadores a incluir transacciones pendientes aunque el builder no quiera. A nivel de aplicación, redes de nodos RPC descentralizados como [Pocket Network](https://www.pokt.network/) ofrecen alternativas al duopolio de Infura y Alchemy, y el modelo de bundlers abierto de ERC-4337 permite que cualquier operador compita sin permiso. Ninguna de estas soluciones está completamente madura, pero el problema es reconocido y hay presión económica e ideológica para resolverlo. El modelo de proveedores especializados no es intrínsecamente problemático si los servicios son reemplazables y la capa on-chain garantiza que ningún intermediario puede actuar sin la firma del usuario.

## Evidencias del cambio

Este patrón no es una propuesta teórica. Tres desarrollos concretos muestran que la industria ha tomado decisiones de diseño que solo tienen sentido si se acepta que la coordinación debe ocurrir off-chain y la verificación on-chain.

**ERC-4337 y la arquitectura de bundlers**: el estándar introduce un nuevo actor, el bundler, cuyo trabajo es recoger UserOperations off-chain, validarlas localmente y agruparlas en una sola transacción que el EntryPoint verifica on-chain. Si la industria creyera que toda la lógica debe vivir en la cadena, los bundlers no existirían: cada operación se enviaría directamente como transacción. El hecho de que ERC-4337 haya sido desplegado en mainnet en 2023 y adoptado por wallets en producción como [Safe](https://safe.global/) o [Coinbase Smart Wallet](https://www.coinbase.com/wallet) es el respaldo formal de ese diseño.

**Motores de intents (CoW Protocol, UniswapX)**: el usuario firma off-chain qué quiere conseguir —intercambiar X tokens por al menos Y de otro— sin especificar cómo. Una red de solvers compite off-chain para encontrar la mejor ruta de ejecución. La solución ganadora se liquida on-chain, donde el contrato verifica que las condiciones firmadas por el usuario se cumplen. El contrato no sabe nada del proceso de optimización: solo comprueba el resultado. Este modelo ha ganado cuota de mercado real frente a los AMMs tradicionales precisamente porque la separación entre intención y ejecución produce mejores precios para el usuario.

**Session keys y EIP-7715**: el usuario negocia off-chain con su wallet qué permisos concede a una dApp —qué contratos puede llamar, cuánto puede gastar, durante cuánto tiempo— y esa negociación se registra on-chain en la smart account. A partir de ahí, cada operación de la dApp se firma con la clave de sesión y se verifica on-chain contra los permisos registrados, sin requerir intervención manual del usuario. Es la aplicación más directa del patrón: la sesión de uso completa ocurre off-chain con supervisión on-chain.

En conjunto, estos tres desarrollos no son mejoras incrementales sobre una arquitectura anterior: son la formalización de un patrón que el ecosistema ha validado con adopción real y con dinero en juego.

---
