# El stack para Account abstraction en Ethereum

## Fundamentos de Account Abstraction

Account Abstraction (AA) surge como respuesta a las limitaciones estructurales del modelo de cuentas original de Ethereum: las Externally Owned Accounts (EOAs). Una EOA es un par de claves criptográficas, y toda su rigidez operativa deriva de ese modelo: el usuario debe gestionar directamente su clave privada sin mecanismo de recuperación nativo, pagar gas siempre en ETH, firmar cada transacción de forma individual e inmediata, y no puede delegar autorización de forma programable ni establecer lógica condicional sobre sus propias operaciones. Esta fricción convierte cada interacción blockchain en una barrera que los usuarios de aplicaciones Web2 no esperan ni toleran, y que ha sido históricamente uno de los principales obstáculos para la adopción masiva.

La base técnica sobre la que se construye es el concepto de [Smart Contract Wallet (SCW)](https://defiantapp.medium.com/qu%C3%A9-son-las-smart-contract-wallets-bf558c2b915c): una cuenta gestionada por código en lugar de una clave privada de la EOA. A diferencia de las EOAs tradicionales, una SCW puede definir sus propias reglas de validación, delegar autorización de forma programable y ejecutar lógica compleja antes de confirmar cualquier operación. Proyectos como Safe demostraron el potencial de este modelo años antes de que existiera un estándar unificado, pero su adopción quedaba limitada a casos avanzados por la complejidad de integración que suponía para cada DApp.

La visión de AA, como [explica MetaMask](https://support.metamask.io/configure/accounts/what-is-a-smart-account), consiste precisamente en hacer que las SCW sean el modelo por defecto en lugar de la excepción. Desde la perspectiva del usuario, esto significa poder recuperar el acceso sin depender de una clave privada única —mediante recuperación social implementada en el SCW o passkeys como mecanismo de firma—, autorizar una aplicación para que opere en su nombre dentro de límites estrictos en lugar de firmar cada transacción individualmente, y no necesitar ETH para pagar gas, ya sea porque un protocolo lo patrocina o porque se paga con otro token. Desde la perspectiva de la aplicación, significa poder ofrecer operaciones en lote atómicas, multi-firma nativa y permisos granulares sin depender de que el usuario comprenda la infraestructura subyacente.

**Inicio con ERC-4337**:

Inicialmente [ERC-4337](https://eips.ethereum.org/EIPS/eip-4337) (2023) estandarizó el acceso a las SCW sin modificar el protocolo base de Ethereum: cualquier aplicación podía integrarse con smart accounts siguiendo ese estándar, sin depender de cambios en el consenso de la red. La limitación era que los usuarios con EOAs tradicionales tenían que migrar a una nueva dirección de smart account para beneficiarse, lo que supuso una barrera de adopción significativa: al cambiar de dirección, el usuario perdía el historial y la reputación on-chain acumulada en su EOA. La idea subyacente, sin embargo, era más profunda: la EOA pasaría a entenderse solo como una credencial de acceso, con el SCW desplegado a su nombre como la cuenta operativa real. Esto habilitaría rotar claves sin perder la dirección, o integrar passkeys y recuperación social como mecanismos de autorización al SCW, desacoplando el acceso de la identidad on-chain.

Esto trajo no solo un nuevo tipo de smart contract en la blockchain, sino también un cambio de paradigma en cómo la DApp interactúa con la infraestructura subyacente. Ya no hablamos de la DApp conectada a una red con la wallet enviando transacciones directamente: la arquitectura se fragmenta en capas con roles distintos.

Por una parte, la wallet inicialmente seguía siendo agnóstica al cambio. Bajo demanda un SCW se crea la primera vez que se usa, mediante un contrato factoría que recibe los parámetros de inicialización. En implementaciones como Safe, la EOA puede actuar como owner del SCW, pero en otras —Kernel, Biconomy Nexus— la lógica de validación está completamente dentro del contrato y no hay un "owner" EOA explícito. Lo que sí es común es el uso del patrón proxy para que todos los SCWs de un mismo tipo compartan la misma lógica desplegada, reduciendo costes.

La DApp aporta el callData —qué quiere ejecutar— y el SDK de infraestructura (wallet SDK o bundler SDK) ensambla el objeto UserOperation completo. La wallet firma ese objeto, que actúa como envoltorio para que un tercero realice el trámite. El SDK es quien envía la petición a ese tercero; no existe transacción directa a la red desde el usuario.

Esa UserOperation encapsula todo lo necesario: el callData al contrato destino, las evidencias del pago de gas con Paymaster o el pago con otro token, validaciones mejoradas como passkeys para autorizar la firma en lote, y cualquier otro parámetro que habilite una mejor experiencia. Cuando hablamos de evidencia del paymaster, es importante aclarar que esta operación es off-chain: usas un proveedor externo, como Pimlico o Alchemy, que te proporciona una firma sobre el pago de gas, que luego será validada y aplicada on-chain.

Ese tercero es el bundler o agrupador: recibe UserOperations de un mempool alternativo específico de ERC-4337, las valida off-chain mediante simulación, selecciona cuáles incluir, agrupa varias UserOperations en una única transacción y la envía a un contrato de la red llamado EntryPoint.

El EntryPoint o punto de acceso es el contrato estándar que recibe las UserOperations, coordina su validación y ordena su ejecución on-chain. Normalmente lo despliega el equipo mantenedor de la implementación de referencia de ERC-4337. Recibe las peticiones de los bundlers, delega la validación al SCW correspondiente, aplica la lógica de Paymaster para el pago de gas y finalmente llama a la función de ejecución del SCW dentro de la misma transacción.

Desde la perspectiva del usuario, la experiencia es fluida; desde la perspectiva técnica, su UserOperation viaja a través de esta infraestructura antes de llegar a la blockchain. Esto no invalida la seguridad del sistema —las garantías criptográficas del contrato se mantienen— pero sí significa que, en muchas implementaciones reales, la infraestructura subyacente sigue dependiendo de APIs y operadores específicos, más que de una red P2P abierta y homogénea como Ethereum.

**El ecosistema normaliza: EIP-7702**:

Ante este panorama, con la actualización Pectra de 2025, este flujo se mejora y estandariza mediante [EIP-7702](https://eips.ethereum.org/EIPS/eip-7702). Funcionalmente, permite que una EOA delegue su ejecución a un SCW sin perder su dirección de origen, lo que es fundamental para no perder la reputación on-chain acumulada y para habilitar funciones de SCW en cuentas antiguas que no fueron creadas con ERC-4337.

En detalle, EIP-7702 introduce un nuevo tipo de transacción (tipo 4) que incluye una `authorization_list`. Esta lista modifica el campo de código de la EOA para que apunte al contrato delegado, y esa delegación es persistente: se mantiene para todas las transacciones posteriores hasta que el propio usuario envíe otra transacción tipo 4 que la revoque o la cambie. Por eso se dice que EIP-7702 permite que tu wallet tenga código: lo que ocurre exactamente es que tu EOA ejecuta la lógica del contrato delegado manteniendo su propia dirección, sin migrar a una cuenta nueva.

Las motivaciones de EIP-7702 se centran en batching, patrocinio de gas y de-escalada de privilegios (privilege de-escalation), que tiene su implementación práctica en [session keys](session-keys.md).

Existen casos donde este modelo se adapta peor. Al ser la EOA la que referencia el SCW, las firmas multisig se complican; en esos escenarios puede ser preferible confiar en wallets ERC-4337 puras como Safe. Igualmente, otros mecanismos de propiedad como passkeys o recuperación social se resuelven con un cambio de diseño: en wallets como MetaMask, el [login social](https://metamask.io/es/news/introducing-metamask-social-login) forma parte de la propia wallet y no del SCW, usando soluciones descentralizadas como MPC según el caso. Hay que aclarar que soluciones como Safe aún siguen el modelo anterior, por lo que no existe un cambio único ni universal. Lo que sí parece claro es que EIP-7702 simplificó varios de estos casos para implementaciones nuevas.

La autorización también habilita un cambio de paradigma respecto a ERC-4337: ya no es necesaria la infraestructura compleja de bundlers para todos los casos. Permite que existan relayers u otros servicios de terceros que paguen gas con su propia infraestructura, y la autorización de EIP-7702 facilita ese proceso sin necesitar el EntryPoint.

Aunque existe este nuevo modelo, la infraestructura ERC-4337 no desaparece sino que se adapta. Los bundlers siguen existiendo, al igual que los EntryPoints en la red, posiblemente más simples porque pueden gestionar la autorización directamente. En muchos casos se usa la misma infraestructura y, por practicidad, incluso el mismo objeto UserOperation.

Por parte de la wallet, ya no es agnóstica al cambio. Igualmente, la DApp debe prepararse para este nuevo tipo de operaciones.

Para que funcione, la wallet necesita soportar el stack de comunicación que lo hace posible:

- **[EIP-5792](https://eips.ethereum.org/EIPS/eip-5792)** (`wallet_sendCalls`): permite que la DApp indique a la wallet "envía estas N llamadas como un lote". Sin esto, no hay forma estándar de coordinar batch calls entre DApp y wallet.
- **[EIP-7677](https://eips.ethereum.org/EIPS/eip-7677)**: permite que la wallet coordine con un paymaster externo para que el gas lo pague el paymaster, no el usuario.
- **[EIP-7702](https://eips.ethereum.org/EIPS/eip-7702)**: permite que una EOA delegue ejecución a lógica de contrato, habilitando lotes y lógica programable sin cambiar de dirección.

Para encontrar wallets que soporten este stack, directorios como [ethereum.org wallets](https://ethereum.org/es/wallets/find-wallet/) o el [directorio de DApps de Alchemy](https://www.alchemy.com/dapps/top/wallets?childCategories=Smart+Contract+Wallets) permiten filtrar por "Smart Contract Wallets". Este filtro es la forma más directa de distinguir wallets que soportan patrocinación de gas, recuperación social o permisos granulares de las que no lo hacen.

## El reparto de responsabilidades entre protocolo, wallet y DApp

La experiencia que experimenta el usuario no surge de una sola pieza, sino de la combinación de tres capas con responsabilidades bien distintas: el protocolo AA, la wallet y la DApp. Confundirlas lleva a asumir que AA resuelve más de lo que resuelve, o a delegar en el protocolo problemas que solo la aplicación puede abordar.

**Lo que resuelve AA como protocolo:**

AA opera fundamentalmente en la capa de coordinación on-chain: define cómo se validan y ejecutan las operaciones, quién puede pagar el gas y bajo qué condiciones, y qué lógica puede expresar una cuenta inteligente. Concretamente, el protocolo habilita patrocinación de gas (paymaster), batching de llamadas atómicas, ejecución delegada con permisos acotados mediante session keys, y la posibilidad de que la validación de autorización sea arbitrariamente programable —una firma ECDSA estándar, una passkey WebAuthn, una aprobación multifirma o cualquier combinación de ellas—. El protocolo garantiza que estas operaciones sean correctas y no falsificables en la cadena; no dice nada sobre cómo se presentan al usuario antes de firmar.

**Lo que gestiona la wallet:**

La wallet es la capa de custodia y firmado. Es quien genera o custodia el material criptográfico (clave privada, passkey, clave de sesión), quien presenta al usuario la solicitud de firma y quien construye o rechaza el objeto que se envía al bundler. Una buena wallet puede enriquecer notablemente la experiencia: mostrar una decodificación legible del calldata, advertir si el contrato destino no está verificado, simular el impacto esperado de la transacción antes de confirmar, o pedir autenticación biométrica adicional para operaciones por encima de un umbral. Pero ninguna de estas capacidades forma parte del estándar AA; son decisiones de producto de cada wallet. Una wallet mínimamente correcta puede limitarse a mostrar bytes hexadecimales y pedirte que confirmes, cumpliendo el protocolo igualmente.

**Lo que recae en la DApp:**

AA no resuelve la comunicación con el usuario sobre el significado de lo que está a punto de firmar. Eso es responsabilidad de la DApp. Los mensajes claros y legibles que describen la operación, las listas visuales de direcciones autorizadas por una session key, las alertas cuando una operación parece anómala respecto al contexto habitual del usuario, los límites sugeridos en función del historial o el riesgo, y la simulación del impacto esperado —"vas a gastar X, vas a recibir Y, estas son las direcciones involucradas"— son todos problemas de presentación e información que la DApp debe resolver de forma activa. El protocolo puede garantizar que la operación es técnicamente válida; no puede garantizar que el usuario entiende lo que firmó.

Esta distinción no es solo académica. Un exploit habitual en Web3 es el phishing de firma: el usuario firma una operación técnicamente válida cuyo calldata hace algo distinto de lo que cree. AA no protege contra esto porque AA valida criptografía y condiciones on-chain, no intenciones. EIP-712 acerca la presentación estructurada de mensajes, pero el trabajo de traducir esa estructura a lenguaje comprensible para el usuario sigue siendo de la DApp. En el contexto de AA, donde las operaciones pueden ser más complejas —un batch con varias llamadas encadenadas, la configuración de una session key con múltiples parámetros, el pago de gas a través de un paymaster externo— la responsabilidad de comunicar claridad es mayor, no menor.

## Mecanismos del protocolo: dónde ocurre realmente cada capacidad

Hasta aquí hemos descrito la arquitectura: UserOperations, bundlers, EntryPoint, SCW, ERC-4337 y EIP-7702. Ahora vale la pena anclar las capacidades concretas que AA habilita a los mecanismos del protocolo que las hacen posibles, porque la diferencia entre lo que permite y cómo ocurre es importante a la hora de entender qué puedes esperar y qué no del sistema.

### Batching y atomicidad: el callData como orquestador

En el modelo EOA, cada llamada a un contrato es una transacción independiente. En ERC-4337, el campo `callData` de la UserOperation no está limitado a una sola llamada: puede codificar una secuencia de llamadas que el SCW desplegará en orden dentro de la misma transacción. La función `execute` o `executeBatch` del SCW recibe el array de targets, values y calldata codificados, y los ejecuta en secuencia dentro del mismo contexto de transacción. Si cualquier llamada revierte, toda la secuencia revierte. Esto no es una característica opcional del protocolo; es consecuencia directa de que quien ejecuta ya no es la EOA sino un contrato con lógica propia.

Con EIP-7702, el mecanismo es distinto en la superficie pero equivalente en resultado: la transacción tipo 4 incluye la `authorization_list` que delega la EOA al contrato, y a partir de ese momento la EOA ejecuta la lógica del contrato delegado —incluyendo su función de batch— manteniendo su dirección. Desde la perspectiva de la DApp, `wallet_sendCalls` (EIP-5792) abstrae esta distinción: si hay una wallet externa (MetaMask, Coinbase Wallet), es ella quien decide cómo cumplirlo; si la DApp usa un SDK de smart account embebido (Alchemy Account Kit, Permissionless.js), es el propio SDK quien construye la UserOperation y la envía directamente al bundler.

### Session keys: validación condicional en `validateUserOp`

El punto clave es `validateUserOp`: el EntryPoint llama a esta función en el SCW antes de ejecutar cualquier operación, y el SCW decide si la autoriza. Por defecto solo acepta la firma de la clave maestra del propietario. Las session keys amplían esa lógica: el SCW también acepta una clave efímera si existe un permiso registrado on-chain que la autorice.

El flujo es: el usuario firma un permiso (contrato destino autorizado, límite de gasto, expiración) con su clave maestra, y el SCW lo almacena on-chain. A partir de ahí, la DApp puede firmar operaciones con la clave efímera sin pedir nada más al usuario. Cuando esa UserOperation llega al EntryPoint, el SCW comprueba en `validateUserOp` que la firma efímera es válida y que la operación respeta los límites del permiso. Si algo no cuadra, rechaza sin ejecutar.

Con EIP-7702 el patrón es idéntico. La única diferencia es que la EOA no necesita migrar a una nueva dirección: adquiere la lógica del contrato delegado directamente en su propia dirección. El mecanismo de session keys que ese contrato implementa funciona exactamente igual.

### Paymasters y relayers: gas sponsorship en ERC-4337 y EIP-7702

**Con ERC-4337**, el patrocinio de gas pasa por un contrato on-chain llamado paymaster, coordinado por el EntryPoint en dos fases. Cuando una UserOperation incluye un campo `paymasterAndData`, el EntryPoint llama a `validatePaymasterUserOp` en el contrato del paymaster antes de ejecutar nada: el paymaster puede aceptar o rechazar la operación. Si acepta, el EntryPoint ejecuta y después llama a `postOp` para que el paymaster liquide la contabilidad final —ajustando si el gas real difirió del estimado—. El paymaster debe tener fondos depositados previamente en el EntryPoint; sin ese depósito, el EntryPoint rechaza cualquier UserOperation que lo referencie.

El pago en otro token funciona dentro de este mismo flujo: el paymaster verifica en `validatePaymasterUserOp` que el usuario ha aprobado suficiente USDC, y en `postOp` ejecuta la transferencia del token hacia sí mismo, habiéndose encargado del gas en ETH. La conversión ocurre dentro del paymaster, invisible al usuario.

**Con EIP-7702**, no hay EntryPoint ni contrato paymaster on-chain. El equivalente es un **relayer**: un servicio externo que simplemente envía la transacción tipo 4 y paga el gas de su propio saldo. No hay dos fases de validación, no hay `postOp`, no hay depósito en ningún contrato. El acuerdo de compensación entre la DApp y el relayer es off-chain —API de pago, prepago, cuota por uso—. El resultado para el usuario es el mismo: no necesita ETH para operar. Pero la infraestructura es considerablemente más simple, y no requiere que ningún contrato paymaster esté desplegado en la red.

## Descentralización real: quién puede participar y cómo

Account Abstraction introduce una capa de infraestructura con un modelo de participación que no tiene el mismo precedente claro que Ethereum. En Ethereum, la pregunta "¿cómo participo en la red?" tiene una respuesta concreta: descargas un cliente de ejecución como Geth o Reth y un cliente de consenso como Lighthouse o Prysm, los conectas entre sí, sincronizas la cadena y, si quieres validar, haces stake de 32 ETH o delegas a un pool. Es técnicamente exigente, pero el camino está definido y el protocolo tiene incentivos explícitos para atraer a ese tipo de participante.

En el ecosistema de Account Abstraction, la pregunta se fragmenta en roles distintos, cada uno con requisitos y barreras propias.

Cualquiera puede técnicamente ejecutar un bundler. Existen implementaciones de referencia en código abierto como el [bundler de infinitism](https://github.com/eth-infinitism/bundler) o Rundler, el bundler de Alchemy. Pero en la práctica, operar un bundler competitivo exige capital para adelantar el gas de las UserOperations antes de recuperarlo, infraestructura siempre disponible con baja latencia y capacidad técnica para gestionar el mempool alternativo de ERC-4337.

Aunque hoy existen implementaciones más maduras y se han desplegado mempools compartidos reales en varias redes, la descentralización operativa sigue estando lejos de la de Ethereum L1. El estándar existe, pero la adopción de una red verdaderamente abierta y neutral entre wallets, bundlers y paymasters sigue siendo desigual y dependiente de proveedores concretos.

Los paymasters son aún más diferentes: no son nodos de red, sino cuentas financiadas con ETH que un operador —un protocolo, una empresa o una dApp— despliega para patrocinar el gas de sus usuarios. No hay forma de "unirse" a la red de paymasters como usuario individual interesado en la salud del ecosistema; se trata de proveedores de servicios con un modelo de negocio propio.

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

El primero es la comprobación `tx.origin == msg.sender`. Esta línea, históricamente usada para verificar que el llamador es directamente una EOA y no un contrato intermediario, rechaza silenciosamente cualquier SCW porque en ese caso `tx.origin` es la EOA que inició la cadena de llamadas pero `msg.sender` es el contrato de la wallet. El reemplazo correcto depende del propósito original: si la intención era prevenir llamadas desde otros contratos, la solución moderna pasa por lógica explícita de autorización mediante patrones como `Ownable` o `AccessControl` de OpenZeppelin. La guía de [Ethereum sobre compatibilidad de AA](https://docs.alchemy.com/docs/smart-contract-compatibility-for-account-abstraction) documenta los patrones problemáticos más habituales.

El segundo es la verificación de firmas. Si el contrato verifica firmas con `ecrecover` directamente, es incompatible con todas las SCW. La solución es implementar soporte para [EIP-1271](https://eips.ethereum.org/EIPS/eip-1271): antes de llamar a `ecrecover`, comprobar si la dirección firmante es un contrato; si lo es, llamar a su función `isValidSignature()` para delegar la verificación. OpenZeppelin ofrece el helper [`SignatureChecker`](https://docs.openzeppelin.com/contracts/4.x/api/utils#SignatureChecker) que abstrae esta lógica de forma compatible con ambos modelos (EOA y SCW) sin reescribir la lógica de verificación del contrato.

Para los mensajes que el usuario debe firmar, adoptar [EIP-712](https://eips.ethereum.org/EIPS/eip-712) es el mínimo exigible: estructura el payload en tipos con nombre que las wallets pueden mostrar como campos legibles en lugar de bytes hexadecimales. La wallet ve "Transferir 100 USDC a 0xabc..." en lugar de calldata crudo. Viem expone `signTypedData` y `hashTypedData` para construir y verificar mensajes EIP-712 desde el frontend, y la documentación de [wagmi sobre `useSignTypedData`](https://wagmi.sh/react/api/hooks/useSignTypedData) cubre el patrón completo incluyendo verificación on-chain posterior.

### Lo que debe cambiar en el frontend

El modelo tradicional de envío de transacciones —construir un objeto de transacción, llamar a `eth_sendTransaction`, esperar el hash— sigue funcionando con EOAs pero no aprovecha ninguna capacidad de AA. La transición hacia AA en el frontend ocurre en dos capas.

La primera es adoptar [EIP-5792](https://eips.ethereum.org/EIPS/eip-5792) como interfaz de comunicación con la wallet. En lugar de `eth_sendTransaction`, la DApp usa `wallet_sendCalls` para enviar lotes de operaciones, y `wallet_getCapabilities` para preguntar a la wallet conectada qué soporta antes de intentar cualquier cosa. Este patrón de detección de capacidades con fallback graceful es el núcleo de la compatibilidad agnóstica: si la wallet responde que soporta patrocinado de gas y batch, la DApp activa esas rutas; si no, cae al flujo EOA estándar. [Wagmi](https://wagmi.sh/) soporta EIP-5792 desde la versión 2.x con los hooks `useCapabilities` y `useSendCalls`, lo que convierte esta detección en pocas líneas desde el frontend sin conocer el tipo de wallet conectada.

La segunda capa es elegir un proveedor de infraestructura de bundler y paymaster si se quiere ofrecer patrocinio de gas o experiencia SCW completa independientemente de la DApp del usuario. [Pimlico](https://pimlico.io/) y [Alchemy Account Kit](https://accountkit.alchemy.com/) son los proveedores con mayor adopción en el ecosistema ERC-4337: ofrecen bundlers, paymasters y SDKs de alto nivel que se integran con wagmi o directamente con [viem](https://viem.sh/) para construir `UserOperations` sin gestionar manualmente la lógica del mempool de ERC-4337. [Permissionless.js](https://docs.pimlico.io/permissionless) es la librería de nivel medio que Pimlico mantiene open-source: permite construir smart accounts (Safe, Kernel, Biconomy Nexus) y enviar `UserOperations` con control total sobre cada decisión sin depender de un SDK propietario cerrado.

Para equipos que despliegan en Base y quieren aprovechar el ecosistema ya construido de Coinbase, el [OnchainKit](https://onchainkit.xyz/) y el [Coinbase Smart Wallet SDK](https://www.smartwallet.dev/sdk/intro) ofrecen componentes React listos para usar (botones de conexión, flujos de onboarding con passkeys) con infraestructura de bundler y paymaster operada por Coinbase sin coste adicional para el desarrollador.

### Cómo conectar wallets de forma agnóstica

Más allá de AA, la selección del conector de wallets determina directamente si la DApp padece el problema de la gran dispersión del login descrito antes. El ecosistema ha generado varias soluciones que implementan [EIP-6963](https://eip6963.org/) —el estándar que permite detectar automáticamente las wallets instaladas por el usuario— como comportamiento por defecto.

[RainbowKit](https://www.rainbowkit.com/) es el conector más utilizado junto a wagmi: muestra automáticamente las wallets que el usuario tiene instaladas, soporta EIP-6963 y WalletConnect para wallets móviles, y ofrece UI configurable. [ConnectKit](https://docs.family.co/connectkit) de Family es la alternativa con diseño más cuidado y soporte nativo para Safe y Coinbase Smart Wallet. [Dynamic](https://www.dynamic.xyz/) y [Privy](https://www.privy.io/) son soluciones de nivel superior orientadas a onboarding progresivo: gestionan tanto wallets externas como Embedded Wallets con login social, y son especialmente relevantes si la DApp quiere soportar usuarios sin wallet previa. La evaluación independiente de [0xpass sobre RainbowKit](https://blog.0xpass.io/p/exploring-rainbowkit-assessing-its) documenta con detalle las limitaciones actuales de cada librería en cuanto a detección y priorización de wallets.

### Compatibilidad, incompatibilidad y degradación graceful

Aplicar todo lo anterior no garantiza experiencia idéntica en todas las wallets, pero sí garantiza que la DApp siempre funciona y que nadie queda excluido. El modelo es de degradación controlada hacia abajo, no de paridad hacia arriba.

Hay cuatro medidas y tres perfiles de cuenta posibles, y su cruce determina qué funciona, qué mejora y qué queda sin efecto.

**EIP-6963 — detección de wallets:**

Compatible universalmente. Una EOA sin AA, una EOA con EIP-7702 y una SCW como Safe o Coinbase Smart Wallet se detectan y aparecen en el selector de la DApp sin configuración adicional. Nadie queda excluido del login por el tipo de wallet que tiene.

**Eliminar `tx.origin == msg.sender` + EIP-1271 — compatibilidad de contratos:**

Compatible universalmente. Las EOAs funcionan exactamente igual que antes. Las SCW, que antes podían fallar silenciosamente al llamar a contratos que asumían EOA, ahora ejecutan sin errores. Sin estos cambios, un usuario de Safe encontraría la DApp rota sin mensaje de error comprensible.

**EIP-712 — mensajes legibles al firmar:**

Compatible universalmente en cualquier wallet que implemente el estándar, que incluye MetaMask, Rainbow, Rabby, Safe y Coinbase Smart Wallet. El usuario ve campos con nombre en lugar de calldata hexadecimal independientemente de si tiene una EOA o una SCW.

**EIP-5792 `wallet_getCapabilities` — capacidades de AA:**

Aquí aparece la diferencia. Una EOA sin soporte 7702 no reporta capacidades avanzadas y la DApp cae al flujo estándar de siempre: el usuario opera normalmente pero sin batch, sin gas sponsoring y sin session keys. Una EOA con EIP-7702 activo reporta las capacidades que su wallet decida exponer, que pueden ser parciales según el proveedor. Una SCW nativa reporta el conjunto completo y la DApp activa operaciones atómicas, pago de gas en stablecoins y session keys para esa sesión.

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
