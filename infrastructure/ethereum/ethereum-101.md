# Ethereum 101

Ethereum es el primer computador con estado distribuido del mundo, un espacio donde se ejecutan contratos inteligentes que sirven a aplicaciones, principalmente descentralizadas (DApps). A diferencia de Bitcoin, que fue diseñado principalmente como un sistema de dinero digital, Ethereum permite la programación de cualquier tipo de lógica gracias a que es Turing completo, pero limitado por el sistema de Gas: cada operación tiene un coste computacional medido en Gas, que debe pagarse en Ether, evitando así bucles infinitos y asegurando que toda ejecución tenga un costo finito.

Ethereum nació como una alternativa a Bitcoin (altcoin), pero ampliando significativamente su funcionalidad mediante contratos inteligentes. Fue fundado por Vitalik Buterin y cuenta con una Fundación Ethereum que actúa como punto de referencia técnico y organizativo, aunque no como autoridad centralizada.

En esencia, un smart contract redefine la confianza en el software: en lugar de confiar en un servidor centralizado, se confía en una red descentralizada que verifica, ejecuta y certifica acuerdos mediante código.

## Historia de Ethereum

La historia de Ethereum comienza en 2013, cuando Vitalik Buterin, un joven programador y escritor de Bitcoin Magazine, propuso la idea de una plataforma blockchain que fuera más allá del simple sistema de pagos de Bitcoin. Buterin había observado las limitaciones del lenguaje de scripting de Bitcoin y visualizó una plataforma donde los desarrolladores pudieran crear cualquier tipo de aplicación descentralizada mediante contratos inteligentes.

En noviembre de 2013, Buterin publicó el whitepaper de Ethereum, un documento que describía una blockchain con un lenguaje de programación Turing completo incorporado. Esta propuesta atrajo la atención de varios desarrolladores y emprendedores del ecosistema blockchain, entre ellos Gavin Wood, quien escribió el Yellow Paper en abril de 2014, la especificación técnica formal de la máquina virtual de Ethereum.

El equipo fundador se amplió para incluir a Charles Hoskinson, Anthony Di Iorio, Mihai Alisie, Amir Chetrit y Joseph Lubin, quienes trabajaron en diferentes aspectos del proyecto. En julio de 2014, Ethereum realizó uno de los crowdsales más exitosos de la historia de las criptomonedas, recaudando más de 18 millones de dólares en Bitcoin (aproximadamente 31,000 BTC en ese momento) mediante la venta de aproximadamente 60 millones de tokens ETH.

La red principal de Ethereum (Mainnet) se lanzó oficialmente el 30 de julio de 2015, marcando el inicio de una nueva era en la tecnología blockchain. El lanzamiento siguió una serie de releases con nombres inspirados en la criptografía y la historia de las ciencias de la computación: Frontier (la versión inicial de julio 2015), Homestead (marzo 2016), Metropolis dividido en Byzantium (octubre 2017) y Constantinople (febrero 2019), y finalmente Serenity, que abarcó la transición completa a Ethereum 2.0 y Proof of Stake.

### El Hack de The DAO y la División de Ethereum Classic

Uno de los eventos más controvertidos y definitorios en la historia de Ethereum ocurrió en 2016 con el hack de The DAO (Decentralized Autonomous Organization). The DAO fue un fondo de inversión descentralizado implementado como un conjunto de contratos inteligentes en Ethereum, que recaudó aproximadamente 150 millones de dólares en ETH durante su crowdsale en mayo de 2016, convirtiéndose en el proyecto de crowdfunding más grande de la historia hasta ese momento.

En junio de 2016, un atacante explotó una vulnerabilidad de reentrancia en el código del contrato inteligente de The DAO, drenando aproximadamente 3.6 millones de ETH (alrededor del 5% de todo el ETH en circulación en ese momento, valorado en unos 50 millones de dólares). La comunidad Ethereum se enfrentó a una decisión fundamental: permitir que el hack permaneciera como parte del historial inmutable de la blockchain, o intervenir mediante un hard fork para revertir las transacciones y devolver los fondos a los inversores originales.

Esta decisión generó un intenso debate filosófico sobre los principios fundamentales de la blockchain: la inmutabilidad versus la intervención pragmática para corregir errores catastróficos. Tras semanas de discusión y una votación comunitaria, la mayoría de la comunidad decidió implementar un hard fork el 20 de julio de 2016 (bloque 1,920,000) que efectivamente revirtió el hack y devolvió los fondos.

Sin embargo, una minoría de la comunidad rechazó esta intervención, argumentando que violaba el principio fundamental de inmutabilidad de la blockchain expresado en el lema "Code is Law" (el código es ley). Este grupo continuó operando la cadena original sin el fork, que se convirtió en Ethereum Classic (ETC). Así, se crearon dos blockchains separadas:

**Ethereum (ETH)**:

La cadena que implementó el hard fork y devolvió los fondos. Esta se convirtió en la implementación principal y cuenta con el apoyo de la Fundación Ethereum, la mayoría de los desarrolladores core y la mayor parte de la comunidad. Ha continuado evolucionando con múltiples actualizaciones, incluida la transición a Proof of Stake con The Merge.

**Ethereum Classic (ETC)**:

La cadena original que mantuvo el historial completo, incluyendo el hack de The DAO. Ethereum Classic se posiciona como la blockchain Ethereum "original e inmutable" y continúa utilizando Proof of Work con el algoritmo Ethash. Aunque tiene una comunidad más pequeña y menos desarrollo activo, mantiene compatibilidad con la EVM y representa una visión alternativa de los principios blockchain centrada en la inmutabilidad absoluta.

Este evento tuvo profundas implicaciones para el ecosistema blockchain, estableciendo precedentes sobre gobernanza, intervención comunitaria y la tensión entre idealismo técnico y pragmatismo. La existencia de ambas cadenas permite que diferentes filosofías coexistan, y el incidente del DAO se ha convertido en un caso de estudio fundamental en seguridad de smart contracts y gobernanza descentralizada.

### Ethereum Foundation

La Ethereum Foundation es una organización sin fines de lucro fundada en Suiza en 2014, antes del lanzamiento de la mainnet. Su misión es apoyar el desarrollo, investigación y adopción del protocolo Ethereum y sus tecnologías relacionadas. A diferencia de empresas centralizadas que controlan blockchains privadas, la Fundación actúa como coordinadora y facilitadora, pero no como autoridad única sobre el protocolo.

La estructura de la Fundación refleja el carácter descentralizado de Ethereum. No tiene control unilateral sobre cambios al protocolo; en cambio, funciona mediante consenso social entre desarrolladores core, investigadores, y la comunidad más amplia. Las decisiones técnicas se toman a través del proceso de Propuestas de Mejora de Ethereum (EIPs), donde cualquiera puede proponer cambios que luego se discuten abiertamente.

Las actividades principales de la Fundación incluyen el financiamiento de equipos de desarrollo de clientes de Ethereum (como Geth, Besu, Nethermind en la capa de ejecución, y Prysm, Lighthouse, Teku en la capa de consenso), investigación en criptografía y escalabilidad, organización de eventos como Devcon (la conferencia anual de desarrolladores de Ethereum), y programas de becas para investigadores y desarrolladores del ecosistema.

El programa de becas de la Fundación ha sido fundamental para impulsar innovación en áreas como escalabilidad (Rollups, sharding), privacidad (pruebas de conocimiento cero), herramientas de desarrollo, educación y seguridad. Miles de proyectos han recibido financiamiento a través de diferentes rondas de grants, contribuyendo al crecimiento exponencial del ecosistema.

La Fundación también coordina la investigación en criptoeconomía, el estudio de cómo los incentivos económicos y la criptografía pueden combinarse para crear sistemas descentralizados seguros y eficientes. Este campo ha sido crucial para el diseño de mecanismos de consenso como Proof of Stake, sistemas de penalización (slashing), y modelos económicos sostenibles.

## Ficha técnica y características

### Ecosistema

- Fundadores: Vitalik Buterin, Gavin Wood, Charles Hoskinson, Anthony Di Iorio, Joseph Lubin, entre otros.
- Sitio: <https://ethereum.org/>.
- Propósito: Crear una plataforma global y descentralizada para ejecutar contratos inteligentes, funcionando como un "ordenador mundial" con estado.
- Generación: 2ª Generación (Blockchain programable con contratos inteligentes).
- Tipo de Arquitectura: Monolítica (Capa 1). La escalabilidad se aborda con soluciones de escalabilidad, principalmente de capa 2.
- Modelo de Consenso de la red: Proof of Stake (PoS) desde "The Merge" (septiembre 2022). Anteriormente utilizaba Proof of Work (PoW) con el algoritmo Ethash.
- Modelo de Autorización: Pública y sin permisos (Permissionless). Cualquiera puede unirse a la red, validar transacciones o desplegar contratos.
- Modelo de gobernanza de la red: Off-chain, basada en la comunidad a través de Propuestas de Mejora de Ethereum (EIPs - Ethereum Improvement Proposals), discusiones de desarrolladores del núcleo (Core Devs) y consenso social. La Fundación Ethereum coordina el desarrollo pero no controla el protocolo; el equipo de Core Devs es diverso y descentralizado. Los EIPs son propuestas formales para mejoras de usabilidad, estándares y cambios en el protocolo que se pueden consultar en <https://eips.ethereum.org/>.
- Roadmap de la red: Sigue una hoja de ruta evolutiva. Fases clave: The Merge (transición a PoS), The Surge (escalabilidad con Rollups y Danksharding), The Scourge (resistencia a la censura), The Verge (verificación simplificada), The Purge (reducción de carga de nodos) y The Splurge (mejoras generales).

### Capacidad y rendimiento

- Modelo de cuenta y estado: modelo de cuenta-saldo (account-based model). Cada cuenta mantiene un balance y un estado asociado que puede incluir datos arbitrarios. Las transacciones modifican directamente estos balances y estados, lo que hace más natural la programación de contratos inteligentes complejos que necesitan mantener información persistente más allá del simple saldo de tokens.
- Completitud de Turing: Turing complete (limitado por gas). Esto significa que puede ejecutar cualquier programa computable, pero el gas evita bucles infinitos y garantiza que toda ejecución tenga un costo finito.
- Tiempo para nuevo bloque: Aproximadamente 12 segundos.
- Transacciones por Segundo (TPS): ~15-30 TPS en la Capa 1. La escalabilidad se logra a través de soluciones de Capa 2 (Rollups) que pueden alcanzar miles de TPS.
- Capacidad efectiva: Con el límite de gas de ~30M por bloque y considerando que una transferencia simple de ETH consume ~21,000 gas, un bloque puede procesar aproximadamente 1,400 transacciones simples. En la práctica, las transacciones con contratos inteligentes consumen mucho más gas, reduciendo este número.
- Límite de bloque: cada bloque en Ethereum tiene un límite de gas —actualmente alrededor de 30M de gas por bloque— que determina cuánta computación puede incluirse. Este límite es dinámico y los validadores pueden ajustarlo gradualmente, pero solo dentro de variaciones pequeñas por bloque
- Escalabilidad: La estrategia principal se centra en un ecosistema de Capas 2 (Rollups) que procesan transacciones fuera de la cadena y publican datos en la Capa 1. El roadmap futuro (Danksharding) busca hacer la Capa 1 una capa de disponibilidad de datos ultra-eficiente para estos Rollups.
- Personalización: Limitada en la Capa 1. La personalización se logra a través de frameworks como OP Stack o Arbitrum Orbit, que permiten crear cadenas de Capa 2 (Appchains) a medida sobre la seguridad de Ethereum.

### Resumen tokenomics

- Incentivo de la red: Los validadores reciben dos tipos de recompensas: (1) Nuevas emisiones de ETH por proponer y atestiguar bloques (emisión dinámica basada en el número de validadores activos, aproximadamente 0.5-1% anual), y (2) Comisiones de transacción que incluyen las propinas (tips) que van directamente a los validadores. La tarifa base de cada transacción se quema según EIP-1559. La tasa de emisión no es fija como en PoW, sino que se ajusta dinámicamente según la cantidad de ETH en staking.
- Tipo de suministro: Sin límite máximo definido (sin [hard cap](https://www.cointracker.io/learn/hard-cap)). La emisión es dinámica y depende del número de validadores activos y la actividad de la red. Tras EIP-1559, puede ser deflacionario en periodos de alta demanda cuando la cantidad de ETH quemado supera la nueva emisión, o ligeramente inflacionario (~1% anual) en periodos normales. El suministro actual ronda los 120 millones de ETH.
- Distribución inicial: Aproximadamente 72 millones de ETH fueron creados en el bloque génesis (2015). De estos, ~60 millones se distribuyeron en la venta pública (crowdsale de 2014), ~12 millones a los fundadores y desarrollo temprano de la Fundación Ethereum. El proyecto nació gracias a este crowdsale que se realizó en 2014.
- Mecanismo de quema: EIP-1559 introduce la quema automática de la tarifa base de cada transacción, retirando permanentemente ETH de circulación. Esto hace que el activo tienda hacia un modelo deflacionario ultrasónico (ultrasound money) cuando la demanda es alta. El término "ultrasound money" hace referencia a que, en periodos de alta actividad, se destruyen (burn) más tokens de los que se crean mediante nuevas emisiones, convirtiendo a ETH en un activo deflacionario más "sólido" que el dinero tradicional.
- Staking y rendimiento: Los validadores que bloquean 32 ETH reciben recompensas anuales que varían entre 3-5% APR aproximadamente, dependiendo del número total de validadores activos y la actividad de la red.

## La Trinidad de Ethereum: EVM, Swarm y Whisper

La visión original de Ethereum, a menudo denominada la "Trinidad de Ethereum", se concibió como un ecosistema descentralizado integral compuesto por tres pilares tecnológicos fundamentales:

**Ethereum (EVM)**:

El componente de **cómputo**. La Máquina Virtual de Ethereum (EVM) es el cerebro del sistema, donde se ejecutan los contratos inteligentes y se procesa la lógica de las aplicaciones. Es la capa que garantiza la ejecución determinista y segura de las reglas de negocio.

**Swarm**:

El componente de **almacenamiento**. Swarm es un sistema de almacenamiento de archivos distribuido y resistente a la censura, concebido como el "disco duro" de este ordenador mundial. Su función es alojar los datos, contenidos y recursos de las DApps de forma persistente y descentralizada, complementando la capacidad de almacenamiento limitada y costosa de la propia blockchain.

**Whisper (ahora Waku)**:

El componente de **mensajería**. Whisper fue el protocolo original de comunicación diseñado para permitir que DApps y usuarios intercambien mensajes de forma privada y segura. Actúa como la capa de comunicación P2P del ecosistema, permitiendo interacciones directas sin depender de servidores centralizados. Whisper ha evolucionado hacia **Waku**, un protocolo más eficiente y escalable que cumple con la misma visión.

Juntos, estos tres componentes fueron diseñados para ofrecer una alternativa completamente descentralizada a la pila de tecnología web tradicional, proporcionando cómputo, almacenamiento y mensajería como una infraestructura pública y abierta. Aunque el desarrollo y la adopción de cada componente han seguido ritmos diferentes, esta visión de una "computadora mundial" sigue siendo una referencia clave en el ecosistema.

## La Máquina Virtual de Ethereum (EVM)

La EVM es el entorno de ejecución donde se ejecutan los contratos inteligentes de Ethereum. Es el componente de cómputo de la Trinidad y el corazón del "ordenador mundial" descentralizado.

La especificación formal de la EVM se encuentra en el Yellow Paper, un documento técnico que define el comportamiento de la máquina virtual, sus instrucciones (opcodes), y cómo procesa las transacciones y el estado de la red.

### Arquitectura y Proceso de Compilación

La EVM es una **máquina virtual basada en pila** (stack-based) que opera con **bytecode**, un conjunto de instrucciones de bajo nivel. El proceso de ejecución de un contrato inteligente sigue esta cadena:

1. **Código Fuente (Solidity u otros lenguajes)**: Los desarrolladores escriben contratos inteligentes en lenguajes de alto nivel como Solidity, Vyper o Yul.

2. **Compilación a Bytecode**: El código fuente se compila utilizando herramientas como `solc` (el compilador de Solidity), que genera bytecode hexadecimal. Este bytecode es el código máquina que la EVM puede interpretar y ejecutar.

3. **Opcodes**: El bytecode está compuesto de opcodes, instrucciones de bajo nivel que representan operaciones individuales (como `ADD`, `MUL`, `SSTORE`, `CALL`, etc.). Cada opcode tiene un costo específico en Gas. Por ejemplo:
   - `ADD` (sumar dos números): 3 gas
   - `SSTORE` (almacenar datos): 20,000 gas (escritura nueva) o 5,000 gas (actualización)
   - `CREATE` (desplegar un nuevo contrato): 32,000 gas + código

4. **Ejecución Descentralizada**: Cuando se invoca un contrato, cada nodo de la red ejecuta el mismo bytecode de forma independiente y determinista, garantizando que todos lleguen al mismo resultado.

Este diseño hace que la EVM sea **determinista** (siempre produce el mismo resultado para las mismas entradas) y **aislada** (el código se ejecuta en un entorno seguro sin acceso directo al sistema operativo del nodo).

Cada operación en la EVM tiene un coste denominado Gas, que no es la moneda Ether en sí, sino una unidad de medida del esfuerzo computacional. El Gas se paga en Gwei (una fracción de Ether, 10^-9 ETH) y sirve para evitar bucles infinitos y recompensar a los validadores.

## Contratos Inteligentes y Solidity

Un smart contract es el lugar donde se codifican las condiciones que debe cumplir un acuerdo entre partes. Actúan como registro contable de liquidaciones, consolidando acuerdos de forma transparente, verificable, auditable y resiliente.

Es el programa que:

- Recibe transacciones iniciadas por cuentas externas (EOA)
- Valida condiciones según la lógica programada
- Ejecuta automáticamente las consecuencias definidas o revierte la operación si no se cumplen
- Puede invocar otros contratos formando cadenas de promesas.

Características clave:

- No se auto-ejecutan: Necesitan ser iniciados por una transacción externa
- Ejecución determinista: Siempre producen el mismo resultado para las mismas entradas
- Inmutables: Una vez desplegados, su código no puede modificarse
- Transparentes: El código y el estado son públicos y verificables
- Transparente y verificable
- Auditable (historial inmutable)
- Resiliente (sin punto único de fallo)
- Propiedad del usuario (estados firmados reutilizables)

Aunque los contratos son inmutables por diseño, en la práctica existen patrones para permitir su actualización. El más común es el **"Proxy Pattern"**, donde un contrato (el proxy) gestiona los datos y delega las llamadas a otro contrato que contiene la lógica. Esto permite cambiar el contrato de lógica en el futuro sin perder el estado ni la dirección del contrato original.

## Tokenización: La Representación del Valor en Ethereum

La capacidad de crear "tokens" es una de las innovaciones más poderosas de Ethereum. La tokenización es el proceso de convertir derechos sobre un activo en una ficha digital (token) en una blockchain. Estos tokens se gestionan mediante contratos inteligentes y pueden representar desde una moneda (tokens fungibles) hasta un objeto de colección único (tokens no fungibles).

La estandarización ha sido clave para la interoperabilidad del ecosistema Ethereum. Este proceso se articula a través de un sistema formal de propuestas que cualquier persona puede presentar, debatir e implementar.

**EIP (Ethereum Improvement Proposal)**: es el mecanismo principal de gobernanza técnica de Ethereum. Un [EIP](https://eips.ethereum.org/) es un documento formal que propone un cambio en el protocolo, una nueva funcionalidad, un proceso o un estándar de la red. Cualquier desarrollador puede abrir un EIP siguiendo una plantilla establecida; después pasa por revisión de la comunidad y, si alcanza consenso, se incluye en una actualización de red. Los EIPs cubren desde cambios al mecanismo de consenso (como EIP-1559 que introdujo la quema de tarifas base) hasta mejoras de infraestructura o experiencia de usuario.

**ERC (Ethereum Request for Comments)**: es una categoría específica de EIP orientada a definir estándares a nivel de aplicación. Mientras que un EIP puede proponer un cambio en el propio protocolo de Ethereum, un ERC define interfaces y convenciones que los contratos inteligentes deben seguir para ser interoperables entre sí. El nombre proviene de la tradición de los RFCs de Internet. Cuando un ERC es aceptado, cualquier wallet, exchange o DApp puede interactuar con cualquier contrato que lo implemente sin necesidad de adaptaciones adicionales.

**RIP (Rollup Improvement Proposal)**: es una categoría más reciente creada a medida que las soluciones Layer 2 se convirtieron en parte central de la estrategia de escalabilidad de Ethereum. Los [RIPs](https://github.com/ethereum/RIPs) proponen estándares y mejoras específicas para el ecosistema de Rollups, como interfaces comunes entre diferentes L2, mecanismos de interoperabilidad cross-rollup o convenciones de secuenciación. Su existencia refleja la madurez del ecosistema de capas 2 como una capa de ejecución paralela con sus propias necesidades de estandarización.

Los estándares de token más importantes, todos definidos mediante ERCs, son:

### ERC-20: El Estándar para Tokens Fungibles

Define la interfaz para tokens intercambiables, donde cada token tiene el mismo valor que otro (como un billete de un dólar). Es la base de la mayoría de las criptomonedas creadas en Ethereum.

- **Funciones clave:** `balanceOf`, `transfer`, `approve`, `transferFrom`.
- **Campos comunes:** `name`, `symbol`, `decimals`.
- **Casos de uso:** Criptomonedas, stablecoins, tokens de gobernanza.

### ERC-721: El Estándar para Tokens No Fungibles (NFTs)

Establece un estándar para tokens únicos e indivisibles. Cada token tiene un ID único y no es intercambiable directamente por otro.

- **Características:** Propiedad verificable, procedencia y escasez digital.
- **Funciones clave:** `ownerOf`, `safeTransferFrom`.
- **Casos de uso:** Arte digital, coleccionables (CryptoKitties), identidad, certificados, entradas a eventos.

### ERC-1155: El Estándar Multi-Token

Un estándar más avanzado que permite gestionar múltiples tipos de tokens (tanto fungibles como no fungibles) en un único contrato inteligente. Esto optimiza costes de gas y simplifica la gestión de activos, especialmente en aplicaciones complejas.

- **Casos de uso:** Videojuegos (ítems, monedas), marketplaces, y cualquier aplicación que necesite combinar diferentes tipos de activos.

## Incentivos de la red: PoS

En PoS (Proof of Stake) existen participantes (validadores) depositan (hacen staking) 32 ETH como garantía de honestidad. Este depósito se "congela" como participación (stake) y el algoritmo elige pseudoaleatoriamente entre los apostantes quién propone el siguiente bloque.

Una vez el ganador propone el bloque, el resto de validadores lo validan para decidir si es correcto. Si un validador actúa maliciosamente (ej. doble gasto, apuntes incorrectos, fondos sin respaldo), sufre "slashing" y pierde parte o la totalidad de su depósito. El validador arriesga su participación económica.

A diferencia del modelo de PoW, donde la principal recompensa era la creación de nuevas monedas, en PoS el incentivo para los validadores es doble. Por un lado, reciben nuevas emisiones de ETH por proponer y validar bloques, con un rendimiento anual (APR, del inglés *Annual Percentage Rate*) sobre su capital en staking que suele rondar el 3-5%. Por otro lado, obtienen las propinas (tips o priority fees) que los usuarios pagan para priorizar sus transacciones. La tarifa base (base fee) de cada transacción no va al validador, sino que se quema, contribuyendo al modelo deflacionario de ETH. Aunque se necesita capital inicial (32 ETH) para ser un validador, es posible unirse a pools de staking con cantidades menores.

Características del PoS en Ethereum:

- No se asienta en energía computacional, sino en la apuesta económica que se puede perder
- Se premia la fidelidad y mayor participación
- Un validador con X% de posesión de ETH puede validar bloques en proporción similar
- Los validadores compiten por mantener su ETH, no por conseguirlo
- No premia la inclusión de nuevos validadores, sino a quienes más ETH tienen y no quieren perderlo

Este cambio redujo el consumo de energía en más de un 99% y cambió el modelo de seguridad de gasto energético a riesgo económico.

### Estructura Temporal: Slots y Epochs

Ethereum PoS organiza el tiempo en unidades estructuradas:

- **Slot**: Es la unidad básica de tiempo, con una duración de 12 segundos. En cada slot se propone un nuevo bloque. Un validador es seleccionado pseudoaleatoriamente para proponer el bloque de cada slot.

- **Epoch**: Es una agrupación de 32 slots, lo que equivale a 6.4 minutos (32 × 12 segundos). Los epochs son fundamentales para el proceso de finalidad y la reorganización de validadores en comités.

Al inicio de cada epoch, los validadores activos se distribuyen aleatoriamente en **comités** (committees), que son grupos de validadores asignados a validar bloques específicos. Cada slot tiene asignado un comité que debe **atestiguar** (attest) que el bloque propuesto es válido. Una atestación (attestation) es un voto criptográfico firmado por un validador que confirma que un bloque cumple con las reglas del protocolo.

El sistema requiere que al menos 2/3 de los validadores activos (supermayoría) atesten correctamente para que un bloque sea considerado válido. Esta arquitectura garantiza que, incluso si hasta 1/3 de los validadores actúan maliciosamente o están desconectados, la red puede seguir funcionando y alcanzar consenso.

### Arquitectura de Capas y Redes P2P

Desde "The Merge" (septiembre 2022), Ethereum adoptó una arquitectura modular que separa responsabilidades en **dos capas principales** que operan en conjunto dentro del mismo nodo físico:

#### Capa de Ejecución (Execution Layer)

Es el entorno donde se procesan las transacciones, se ejecutan los contratos inteligentes (EVM) y se gestiona el estado de la red (cuentas, balances, storage de contratos). Esta capa es la evolución de lo que antes se conocía como "Ethereum 1.0".

**Clientes de ejecución:** Geth, Besu, Nethermind, Erigon.

**Red P2P de ejecución:**

- **Protocolo:** DevP2P (protocolo P2P específico de Ethereum sobre TCP)
- **Descubrimiento:** Discv4 (sobre UDP), migrando gradualmente a Discv5
- **Funciones de red:** Propagar transacciones nuevas entre nodos, sincronizar bloques ejecutados, gestionar el mempool (transacciones pendientes)
- **Descubrimiento de peers:** DHT (Distributed Hash Table) mediante el protocolo Kademlia modificado
- **Formato de identificación:** ENR (Ethereum Node Records) con clave eth1

#### Capa de Consenso (Consensus Layer)

Es la responsable de la seguridad de la red mediante el mecanismo de Proof of Stake. Esta capa no ejecuta transacciones, sino que se encarga de ordenar y validar los bloques propuestos por los validadores, asegurando que la red llegue a un acuerdo sobre el estado de la cadena. También es fundamental para la **disponibilidad de datos** (Data Availability), función crucial para la escalabilidad con Rollups. Esta capa corresponde a la antigua "Beacon Chain".

**Clientes de consenso:** Prysm, Lighthouse, Teku, Nimbus.

**Red P2P de consenso:**

- **Protocolo:** libp2p (protocolo P2P modular y extensible)
- **Descubrimiento:** Discv5 (sobre UDP) con adaptador a libp2p
- **Funciones de red:** Propagar atestaciones de validadores, distribuir bloques propuestos, gestionar comités y sincronización de epochs
- **Diseminación de mensajes:** Gossipsub (protocolo pub/sub eficiente) para bloques, atestaciones, exits y slashings
- **Formato de identificación:** ENR con clave eth2 y campos adicionales (attestation subnet bitfield)

#### Comunicación entre Capas y Arquitectura de Red

**Engine API (RPC local):** Ambas capas se comunican a través de una interfaz específica que permite el intercambio de información sin necesidad de red externa. Un nodo completo ejecuta **un cliente de cada capa simultáneamente** en la misma máquina física.

**Dos redes P2P independientes:** Cada capa mantiene su propia red de comunicación peer-to-peer con protocolos, peers y mensajes distintos. Un nodo puede tener diferentes peers en cada red, y cada capa sincroniza su información por su propia red de forma independiente.

**Identidad única compartida:** Aunque operan dos redes P2P separadas, ambos clientes comparten un único **ENR (Ethereum Node Record)** que contiene claves separadas para cada capa (eth1 key y eth2 key), presentando una única identidad de red hacia el exterior.

**Bootnodes:** Nodos especiales con direcciones hardcoded en los clientes que facilitan el descubrimiento inicial de peers cuando un nuevo nodo se une a la red. Los bootnodes solo introducen nuevos nodos a la red, no participan en tareas normales como sincronización de cadena.

Esta arquitectura modular permite que cada capa se desarrolle, optimice y actualice de forma independiente, mejorando la mantenibilidad del protocolo sin comprometer la seguridad o interoperabilidad.

### Finalidad y Seguridad de la Red

La **finalidad** (finality) es la garantía criptoeconómica de que una transacción confirmada es irreversible y no puede ser alterada sin destruir una cantidad masiva de ETH. A diferencia de Bitcoin, donde las transacciones simplemente ganan más confirmaciones con el tiempo (finalidad probabilística), Ethereum PoS ofrece **finalidad económica** mediante el algoritmo de consenso **Casper FFG** (Friendly Finality Gadget).

**Proceso de Finalidad:**

1. Cuando un bloque es propuesto en un slot, los validadores del comité correspondiente lo atestiguan.
2. Cada epoch, los validadores votan sobre dos "checkpoints": el bloque al inicio del epoch anterior (justified) y el bloque al inicio del epoch actual.
3. Si un checkpoint recibe atestaciones de al menos 2/3 del total del ETH en staking, ese checkpoint se considera **justificado** (justified).
4. Si en el siguiente epoch el nuevo checkpoint también se justifica, el anterior se convierte en **finalizado** (finalized).

Este proceso normalmente toma **dos epochs (~12.8 minutos)** para alcanzar finalidad completa. Una vez que un bloque está finalizado, revertirlo requeriría que los atacantes quemaran al menos 1/3 de todo el ETH en staking (miles de millones de dólares), lo que hace económicamente inviable cualquier ataque.

**¿Qué Sucede si se Pierde la Finalidad?**

Si la red no logra finalizar bloques (porque menos de 2/3 de validadores están atestando correctamente), entra en un estado degradado:

- **Reorganizaciones (reorgs):** Sin finalidad, bloques pueden ser revertidos, creando incertidumbre sobre qué cadena es la canónica.
- **Inactivity Leak:** Un mecanismo de seguridad que penaliza gradualmente a los validadores inactivos, reduciendo su stake hasta que los validadores activos recuperen la supermayoría de 2/3 necesaria para retomar la finalidad.

Este sistema fue diseñado para que la red pueda recuperarse incluso si un tercio de los validadores se desconectan simultáneamente (por ejemplo, en un ataque coordinado o fallo masivo de infraestructura).

**Penalizaciones: Slashing vs Inactivity Leak:**

- **Slashing:** Es una penalización severa que se aplica a validadores que actúan maliciosamente (por ejemplo, firmando dos bloques conflictivos para el mismo slot o atestando bloques contradictorios). El validador pierde una parte significativa de su stake (mínimo 1 ETH, pero puede ser mucho más si muchos validadores son "slasheados" simultáneamente) y es expulsado de la red.

- **Inactivity Leak:** Es una penalización gradual que se aplica cuando la red no logra finalizar bloques. Los validadores inactivos (que no están atestando) pierden progresivamente su stake hasta que los validadores activos representan nuevamente 2/3 del total y la red puede retomar la finalidad. Esta es una medida de seguridad para recuperar el consenso en escenarios de ataques graves o fallos masivos.

Estos mecanismos garantizan que comportarse honestamente es siempre la estrategia más rentable económicamente.

## Economía del Ether (ETH)

Ether es la criptomoneda nativa de la red. Se usa para pagar el Gas de las transacciones y como garantía en el staking.

Unidades:

- Wei: La unidad más pequeña de Ether, como un céntimo (1 ETH = 10^18 Wei)
- Gwei: 10^9 Wei, usada comúnmente para expresar el precio del Gas

### Inflación y "Ultrasound Money"

A diferencia de Bitcoin, Ether (ETH) no tiene un suministro máximo fijo. Su política monetaria ha evolucionado para priorizar la seguridad de la red y la sostenibilidad económica. Con la transición a Proof of Stake y la introducción del EIP-1559, el modelo cambió radicalmente:

**Emisión de ETH**: Se crea nuevo ETH como recompensa para los validadores que aseguran la red. Esta emisión es mucho menor que en la era PoW.

**Quema de Tarifas**: Una parte de las comisiones de cada transacción, la **tarifa base (base fee)**, se destruye permanentemente (se "quema").

Este mecanismo dual hace que, en periodos de alta actividad en la red, la cantidad de ETH quemado pueda superar la cantidad de ETH nuevo que se emite. Como resultado, el suministro total de ETH disminuye, convirtiéndolo en un **activo deflacionario**. Este concepto se conoce popularmente como **"Ultrasound Money"**, una evolución del término "Sound Money" (como el oro o Bitcoin) para describir un activo cuyo suministro puede reducirse con el uso.

### El Modelo de Tarifas (Gas)

Toda operación en Ethereum (desde una transferencia hasta la ejecución de un contrato complejo) tiene un coste computacional medido en Gas. El Gas es una unidad abstracta que representa el esfuerzo de cálculo, y su precio se paga en Gwei (una fracción de ETH).

El coste total de una transacción se calcula con la siguiente fórmula:

`Coste Total = Gas Usado * (Tarifa Base + Propina)`

El modelo de tarifas, introducido con EIP-1559, se descompone en los siguientes elementos:

- Tarifa Base (Base Fee): Es el precio mínimo por unidad de Gas que una transacción debe pagar para ser incluida en un bloque. El protocolo la ajusta automáticamente según la congestión de la red. Esta tarifa se quema por completo, lo que significa que se retira permanentemente de la circulación, siendo un pilar del modelo deflacionario de Ethereum.

- Propina (Priority Fee o Tip): Es un pago adicional y voluntario que el usuario ofrece al validador para incentivar que su transacción se procese con mayor rapidez. Esta propina constituye un ingreso directo para el validador.

A diferencia de sistemas como Bitcoin, en Ethereum no existe una recompensa fija por bloque (block subsidy). Los ingresos de los validadores provienen de las propinas de las transacciones y del MEV (Maximal Extractable Value), que es el valor que pueden obtener al reordenar, incluir o excluir transacciones dentro de un bloque.

A continuación, se detallan los conceptos técnicos clave del sistema de gas:

- gasUsed: La cantidad total de gas que una transacción ha consumido.
- gasLimit: El máximo de gas que un usuario está dispuesto a gastar en una transacción. Sirve como un mecanismo de seguridad para evitar que errores en un contrato consuman todos los fondos de una cuenta.
- baseFee: La tarifa base calculada por el protocolo, que se quema.
- gasPremium: La propina o "priority fee" que se paga al validador.
- gasFeeCap: El precio máximo total (baseFee + propina) que el usuario está dispuesto a pagar por unidad de gas.
- gasPrice: Un concepto del modelo de tarifas antiguo (legacy) que ha sido mayormente reemplazado por el sistema de `baseFee` y `gasPremium` tras el EIP-1559.

## Oráculos

Los contratos inteligentes en Ethereum no pueden ver el mundo exterior por sí mismos (no pueden consultar una API de precios, el clima, o cualquier dato externo a la blockchain). Los oráculos solucionan esto inyectando datos del mundo real en la blockchain de forma segura y verificable.

Chainlink es el ejemplo más destacado y el estándar de facto, permitiendo que las aplicaciones DeFi funcionen con precios de mercado actualizados, datos meteorológicos, resultados deportivos, etc. Otros proyectos como Gnosis se enfocan en mercados de predicción y servicios financieros relacionados.

## Estado Actual de la Trinidad: Swarm y Waku

Mientras que la EVM se ha consolidado como el estándar de facto para la ejecución de contratos inteligentes, los otros dos pilares de la Trinidad han seguido caminos diferentes pero siguen siendo componentes activos del ecosistema web3.

### Swarm: Almacenamiento Descentralizado

Swarm es un protocolo de almacenamiento distribuido y sistema de distribución de contenidos diseñado específicamente para el ecosistema Ethereum. Proporciona infraestructura descentralizada y resistente a la censura para alojar datos de DApps, como sitios web, videos y bases de datos de aplicaciones. A diferencia del almacenamiento on-chain en Ethereum (que es muy costoso), Swarm está diseñado para ser económico y escalable.

Swarm es un **proyecto funcional y operativo**, con su propia red principal (mainnet) lanzada en 2021 y su token nativo BZZ. Los usuarios pueden ejecutar nodos Swarm para proporcionar almacenamiento a la red y recibir incentivos económicos a cambio.

**Estado del ecosistema:** Aunque Swarm cumple con la visión original de la Trinidad, en la práctica el ecosistema web3 utiliza una diversidad de soluciones de almacenamiento. **IPFS (InterPlanetary File System)** ha ganado mayor adopción para casos de uso como almacenamiento de NFTs y contenido estático, mientras que alternativas como Arweave se especializan en almacenamiento permanente. Swarm continúa siendo relevante como la solución de almacenamiento nativa de Ethereum, especialmente para aplicaciones que priorizan la integración profunda con el ecosistema Ethereum.

### Waku: La Evolución de Whisper

Whisper fue el protocolo de mensajería originalmente propuesto como parte de la Trinidad, diseñado para permitir comunicaciones privadas y cifradas entre DApps. Sin embargo, su diseño original presentaba limitaciones significativas de escalabilidad que dificultaban su adopción práctica.

**Waku** ha surgido como la evolución natural de Whisper, manteniendo la visión original pero con una arquitectura completamente rediseñada. Es un protocolo de mensajería P2P modular, eficiente y escalable, adaptable a diferentes necesidades: desde chats privados hasta la coordinación de nodos en redes descentralizadas, pasando por notificaciones push y sincronización de estado.

Waku es un **proyecto activo y en producción**, siendo utilizado por aplicaciones reales como Status (aplicación de mensajería descentralizada) y el cliente de Ethereum Nimbus. Se está posicionando como el estándar de facto para la capa de comunicación en el ecosistema web3, cumpliendo finalmente con el tercer pilar de la visión original de Ethereum.

## Escalabilidad

Ethereum tiene una capacidad limitada de transacciones por segundo en su capa base (Layer 1), lo que puede elevar los costos. El problema fundamental es que cada nodo de la red replica y valida todas las transacciones, lo que garantiza descentralización pero limita el rendimiento. Para solucionar esto sin sacrificar completamente la seguridad, existen varias estrategias de escalabilidad.

### Sharding (Fragmentación)

Sharding es una estrategia que divide la blockchain en fragmentos (shards) dentro de la propia red de nodos de Ethereum. A diferencia de otras soluciones de escalabilidad que funcionan como capas externas (Rollups, State Channels) o redes paralelas independientes (Sidechains, Plasma), el Sharding modifica la arquitectura interna de Ethereum. Cada shard funciona como una cadena semi-independiente con su propio estado y conjunto de validadores, pero todos los shards forman parte de la misma red Ethereum.

En el sharding cada fragmento mantiene su propio libro contable separado de forma permanente, a diferencia de los State Channels o Rollups que consolidan transacciones.

El concepto clave: En lugar de que todos los nodos repliquen todas las transacciones (lo cual es costoso en almacenamiento y hace que solo organizaciones con recursos puedan mantener nodos completos, centralizando el sistema), cada nodo solo valida un subconjunto de fragmentos. Esto permite que la red procese múltiples cadenas en paralelo sin salir de la infraestructura base de Ethereum.

Estado actual en Ethereum:

Originalmente, Ethereum 2.0 planeaba implementar 64 shards que ejecutarían transacciones. Sin embargo, tras el éxito de los Rollups como solución de escalabilidad, la hoja de ruta cambió radicalmente hacia **"Danksharding"**, un modelo donde los shards se especializan exclusivamente en **disponibilidad de datos** (data availability) para beneficiar a los Rollups, en lugar de ejecutar transacciones directamente.

**Proto-Danksharding (EIP-4844):**

Danksharding completo aún no está implementado. Lo que existe actualmente es **"proto-danksharding"**, introducido con **EIP-4844** (activado en marzo de 2024 con la actualización "Dencun"). Esta es una versión preliminar que sienta las bases para el sistema completo.

La innovación principal de EIP-4844 es la introducción de **"blobs"** (Binary Large Objects):

- Los blobs son paquetes de datos grandes (~125 KB cada uno) que se adjuntan a las transacciones de forma temporal.
- A diferencia de los datos de transacciones normales (calldata), que se almacenan permanentemente en la blockchain, los blobs se eliminan automáticamente después de ~18 días.
- Los Rollups pueden publicar sus datos de transacciones comprimidos en estos blobs a un coste mucho menor que usando calldata tradicional.
- Cada bloque puede incluir hasta 6 blobs (con capacidad de ráfaga temporal hasta 9), lo que significa ~750 KB de espacio adicional para datos de Rollups por bloque.

**Impacto en el Ecosistema:**

Proto-danksharding redujo los costos de las transacciones en Rollups L2 en un 90-95% al hacer la publicación de datos mucho más barata. Esto aceleró la adopción masiva de soluciones L2 como Optimism, Arbitrum y zkSync.

**Danksharding Completo:**

La visión final de Danksharding incluye:

- **Separación completa entre productores y constructores de bloques mediante ePBS (EIP-7732)**: La [Proposer-Builder Separation](https://ethereum.org/en/roadmap/pbs/) (PBS) es un cambio arquitectónico fundamental que separa las responsabilidades de consenso y ejecución durante la creación de bloques. Actualmente implementada mediante middleware externo (MEV-Boost), la visión a largo plazo es integrarla directamente en el protocolo mediante [EIP-7732](https://eips.ethereum.org/EIPS/eip-7732) (enshrined PBS o ePBS).

  **Motivación y Problema Actual:**

  En el modelo actual de Ethereum PoS, los validadores (proposers) son responsables tanto de alcanzar consenso sobre el estado de la blockchain como de construir el bloque de ejecución que contiene las transacciones. Esto crea varios problemas: los validadores deben tener recursos técnicos sofisticados para optimizar el ordenamiento de transacciones y extraer MEV (Maximal Extractable Value), lo que favorece la centralización hacia validadores profesionales con acceso a infraestructura avanzada. Además, el modelo actual depende de middleware de confianza (MEV-Boost) que introduce riesgos de seguridad y centralización.

  **Arquitectura Técnica de ePBS (EIP-7732):**

  La propuesta introduce una separación clara de roles y responsabilidades:

  **Builders (Constructores de Bloques)**:

  Son participantes especializados que compiten por construir el bloque de ejecución más rentable. Recopilan transacciones del mempool, optimizan su ordenamiento para maximizar MEV y comisiones, y crean un compromiso criptográfico (SignedExecutionPayloadHeader) que especifica el hash del bloque de ejecución y el valor que pagarán al proposer. Este compromiso se envía al proposer sin revelar el contenido completo del bloque, evitando que el proposer pueda robar las oportunidades de MEV identificadas por el builder.

  **Proposers (Validadores/Proponentes)**:

  Son los validadores seleccionados por el protocolo para proponer el siguiente bloque de consenso (BeaconBlock). Su responsabilidad se simplifica: seleccionan el compromiso del builder que ofrece el mayor pago, lo incluyen en el bloque de consenso, y reciben el pago comprometido. No necesitan validar el contenido del bloque de ejecución en este momento, solo verifican el compromiso criptográfico.

  **Payload Timeliness Committee (PTC)**:

  Un subconjunto de validadores asignado aleatoriamente a cada slot tiene la responsabilidad de certificar si el builder reveló oportunamente (within-slot) el bloque de ejecución completo después de que el proposer incluyó su compromiso en el bloque de consenso. Los miembros del PTC transmiten un PayloadAttestationMessage confirmando que el builder publicó el execution payload con el hash correcto. Estos validadores no están obligados a validar la ejecución de las transacciones (eso se pospone hasta el siguiente bloque), solo verifican disponibilidad y correspondencia del hash.

  **Flujo del Proceso ePBS:**

  El proceso de creación de bloques bajo ePBS sigue estos pasos: (1) Los builders construyen bloques de ejecución optimizados y envían compromisos firmados a los proposers especificando el hash del bloque y el pago ofrecido. (2) El proposer selecciona el compromiso con mayor pago, lo incluye en el BeaconBlock, y el valor comprometido se deduce automáticamente del saldo del builder en la Beacon Chain y se acredita al proposer. (3) El builder debe revelar el execution payload completo dentro del slot. (4) El PTC certifica si el payload fue revelado oportunamente y corresponde al hash comprometido. (5) La validación completa de la ejecución se realiza en el siguiente bloque de consenso, permitiendo que la red progrese sin esperar la validación inmediata.

  **Beneficios de ePBS:**

  Eliminar dependencia de middleware centralizado como MEV-Boost reduce vectores de ataque y puntos de fallo únicos. La separación permite que validadores regulares compitan sin necesitar infraestructura sofisticada para extraer MEV, democratizando la participación. Los builders compiten en un mercado abierto por construir bloques, garantizando pagos justos y transparentes a proposers mediante smart contracts del protocolo. Los validadores pueden concentrarse en consenso sin preocuparse por optimización de transacciones, utilizando mejor el tiempo de slot disponible. La certificación del PTC asegura que builders no puedan comprometer sin entregar, mientras que posponer validación de ejecución permite propagación más rápida de bloques de consenso.

  **Estado Actual y Roadmap:**

  EIP-7732 aún está en fase de discusión y diseño dentro de la comunidad Ethereum. La implementación requiere cambios significativos en la capa de consenso (Beacon Chain) y coordinación entre todos los clientes de consenso y ejecución. Actualmente, PBS se implementa mediante MEV-Boost, un middleware externo desarrollado por Flashbots que simula la separación pero introduce supuestos de confianza. La transición a ePBS es parte de la visión de Danksharding completo y representa uno de los cambios arquitectónicos más importantes del roadmap de Ethereum.

- **Múltiples shards de datos**: Escalado a 64 shards de disponibilidad de datos, cada uno con su propio conjunto de blobs, incrementando exponencialmente la capacidad de datos disponible para Rollups.
- **Muestreo de Disponibilidad de Datos (DAS)**: Permite que los nodos ligeros verifiquen que los datos están disponibles sin descargarlos completamente, usando técnicas criptográficas avanzadas.

Con Danksharding completo, Ethereum se convertiría en una capa de disponibilidad de datos ultra-eficiente capaz de soportar cientos de miles de TPS a través de su ecosistema de Rollups, manteniendo la descentralización y seguridad.

Desafío principal: Coordinar la seguridad entre fragmentos y evitar que atacar un solo shard comprometa el sistema completo requiere mecanismos complejos de consenso y sincronización. La implementación de ePBS añade complejidad técnica significativa que requiere evaluación cuidadosa de trade-offs entre descentralización, eficiencia y seguridad.

### State Channels (Canales Estatales)

Los State Channels funcionan como subredes temporales que permiten realizar múltiples transacciones fuera de la cadena principal (off-chain), registrando en Ethereum solo el estado inicial y final. El concepto es similar a abrir una pestaña en un bar: realizas múltiples consumiciones sin pagar cada una individualmente, y al final se consolida todo en una única transacción.

Funcionamiento:

- Dos o más participantes abren un canal depositando fondos en un contrato inteligente en Ethereum.
- Realizan múltiples transacciones entre ellos off-chain, actualizando el estado del canal sin publicar cada transacción en la blockchain.
- Cuando terminan, cierran el canal y solo el estado final se registra en Ethereum, confirmando el resultado de todas las transacciones.

El ejemplo más conocido es Lightning Network (para Bitcoin), aunque el concepto también existe en Ethereum con implementaciones como Raiden Network y Connext. Los State Channels son ideales para pagos recurrentes entre las mismas partes (micropagos, juegos, streaming de pagos), pero no funcionan bien para interacciones que requieren muchos participantes diferentes.

Limitación: Solo funciona para interacciones predefinidas entre participantes conocidos. No escala para aplicaciones que requieren estado global compartido entre miles de usuarios desconocidos.

### Layer 2 (Rollups)

Son redes que funcionan sobre Ethereum. Procesan muchas transacciones fuera de la cadena principal, las comprimen y envían solo el resultado final a Ethereum. A diferencia de los State Channels, los Rollups consolidan transacciones de múltiples usuarios en lotes y publican pruebas criptográficas en la cadena principal. Heredan la seguridad de Ethereum pero son mucho más rápidas y baratas.

Los Rollups se dividen en dos categorías principales según su mecanismo de validación: Optimistic Rollups, que asumen validez por defecto con un período de disputa para detectar fraudes, y ZK-Rollups, que emplean pruebas de conocimiento cero para verificación matemática instantánea.

#### Optimistic Rollups: Arquitectura y Funcionamiento

Los [Optimistic Rollups](https://ethereum.org/en/developers/docs/scaling/optimistic-rollups/) representan una de las soluciones de escalabilidad más maduras y adoptadas del ecosistema Ethereum. Su nombre proviene de su premisa fundamental: asumen de forma optimista que todas las transacciones procesadas son válidas, a menos que se demuestre lo contrario mediante un mecanismo de disputa.

**Arquitectura técnica:**

La arquitectura de un Optimistic Rollup consta de varios componentes clave que interactúan para procesar transacciones off-chain mientras mantienen la seguridad de Ethereum:

**Secuenciadores (Sequencers)**:

Son los nodos responsables de ordenar, ejecutar y agrupar transacciones off-chain en la rollup chain. Reciben transacciones de usuarios, las ejecutan en una copia local de la EVM (idéntica a la de Ethereum), calculan el nuevo estado resultante y agrupan cientos de transacciones en un único lote (batch). Los secuenciadores proporcionan confirmaciones instantáneas a los usuarios (soft confirmations) antes de que el estado se publique en L1, mejorando significativamente la experiencia de usuario al ofrecer feedback inmediato.

Actualmente, la mayoría de Optimistic Rollups operan con un secuenciador centralizado controlado por el equipo del proyecto (Optimism PBC para Optimism, Offchain Labs para Arbitrum). Esta centralización mejora el rendimiento y simplifica la coordinación, pero introduce un único punto de fallo y riesgo de censura. El roadmap de estos proyectos incluye la descentralización gradual de secuenciadores mediante conjuntos rotatorios de operadores que compiten por el derecho a secuenciar, similar al modelo de validadores de Ethereum.

**Agregadores (Aggregators) y State Roots**:

Periódicamente (típicamente cada pocos minutos), el secuenciador consolida los lotes de transacciones procesados y calcula un nuevo state root, un hash criptográfico que representa el estado completo de la rollup chain tras ejecutar todas las transacciones del lote. Este state root, junto con los datos comprimidos de las transacciones, se publica en un contrato inteligente en Ethereum L1.

A diferencia de las transacciones normales de Ethereum donde cada transacción individual se valida por todos los nodos, en Optimistic Rollups solo se publica el resultado agregado (el state root) on-chain, reduciendo drásticamente la carga de datos y cómputo en L1. Los datos de transacciones se publican como calldata (o blobs desde EIP-4844) para garantizar la disponibilidad de datos y permitir que cualquiera pueda reconstruir el estado de la rollup chain de forma independiente.

**Fraud Proofs (Pruebas de Fraude)**:

El mecanismo de seguridad central de los Optimistic Rollups se basa en pruebas de fraude que permiten a cualquier observador desafiar state roots incorrectos. Cuando un secuenciador publica un state root on-chain, se inicia un período de desafío (challenge period o dispute window), típicamente de 7 días. Durante este tiempo, cualquier participante puede presentar una prueba de fraude si detecta que el state root publicado no corresponde al resultado correcto de ejecutar las transacciones del lote.

Las pruebas de fraude funcionan mediante un juego de bisección interactivo: el desafiante y el secuenciador dividen repetidamente el lote de transacciones en partes cada vez más pequeñas hasta identificar la instrucción individual que causó la discrepancia. Esta única instrucción se ejecuta on-chain en Ethereum L1 mediante un contrato especial (Fraud Proof Verifier), que determina qué parte tiene razón. Si el desafiante demuestra fraude, el secuenciador pierde su depósito (stake) y el state root incorrecto se revierte; si el desafío es infundado, el desafiante pierde su depósito.

Este mecanismo asume un modelo de seguridad de "1-of-N honestidad": solo se necesita un participante honesto monitoreando la rollup chain para detectar y prevenir fraudes. La penalización económica hace que intentar fraudes sea costoso y arriesgado para los secuenciadores.

**Período de Disputa y Finalidad**:

El período de disputa de 7 días es una característica inherente de los Optimistic Rollups que introduce latencia en la finalidad económica. Aunque los usuarios reciben confirmaciones instantáneas al enviar transacciones y pueden continuar interactuando dentro de la rollup chain sin restricciones, retirar activos desde la L2 hacia Ethereum L1 requiere esperar la finalización del período de disputa. Esto garantiza que cualquier fraude sea detectado antes de que los fondos salgan del sistema.

Para mitigar la fricción de este período de espera, han surgido soluciones como proveedores de liquidez especializados que ofrecen retiros rápidos (fast withdrawals): adelantan fondos a los usuarios en L1 a cambio de una pequeña comisión, asumiendo el riesgo del período de disputa y reclamando los fondos originales una vez transcurrido el plazo. Esto permite a usuarios que necesitan liquidez inmediata evitar la espera de 7 días sin comprometer la seguridad del sistema.

**Disponibilidad de Datos (Data Availability)**:

Para que el sistema sea seguro y sin confianza (trustless), los datos de todas las transacciones procesadas en la rollup chain deben publicarse en Ethereum L1. Esto permite que cualquier participante pueda:

- Reconstruir el estado completo de la rollup chain de forma independiente
- Verificar que el state root publicado por el secuenciador es correcto
- Presentar pruebas de fraude si detectan discrepancias

Originalmente, estos datos se publicaban como calldata en transacciones de Ethereum, lo que era costoso. Con la introducción de EIP-4844 (proto-danksharding), los Optimistic Rollups pueden publicar datos en blobs, estructuras temporales de datos mucho más económicas que solo persisten ~18 días. Esto es suficiente para el período de disputa de 7 días, reduciendo los costos de publicación de datos en un 90-95%.

Existen variantes experimentales llamadas Optimistic Validiums que almacenan datos off-chain para reducir aún más costos, pero sacrifican la propiedad de disponibilidad de datos garantizada por Ethereum, introduciendo supuestos de confianza adicionales.

**Compatibilidad EVM y Experiencia de Desarrollo**:

Una de las mayores ventajas de los Optimistic Rollups es su compatibilidad con la EVM. Optimism implementa una EVM casi idéntica (con pequeñas diferencias en opcodes relacionados con contexto L1), mientras que Arbitrum desarrolló su propia máquina virtual Arbitrum Virtual Machine (AVM) que traduce bytecode EVM de forma equivalente.

Esta compatibilidad permite a desarrolladores desplegar contratos de Solidity existentes en rollups sin modificaciones, reutilizar herramientas del ecosistema (Hardhat, Foundry, Remix), y aprovechar bibliotecas y estándares consolidados (OpenZeppelin, ERC-20, ERC-721). La migración de DApps desde Ethereum L1 a L2 se reduce a cambiar configuraciones de red.

**Implementaciones Principales:**

**Optimism**:

Pionero en Optimistic Rollups, desarrolló el OP Stack, un framework modular de código abierto que permite crear rollups personalizados. Ha construido una visión de "Superchain", una red de rollups interoperables que comparten seguridad, estándares de comunicación y liquidez. Base (desarrollada por Coinbase), OP Mainnet, Zora Network y otros proyectos utilizan el OP Stack, formando un ecosistema cohesionado.

**Arbitrum**:

Competidor directo de Optimism con ligeras diferencias técnicas. Arbitrum introdujo Arbitrum Nitro, una reimplementación completa que ejecuta código WASM (WebAssembly) compilado desde Go, logrando mayor rendimiento. Ofrece Arbitrum One (rollup generalista) y Arbitrum Nova (optimizado para gaming y aplicaciones sociales con datos off-chain). Arbitrum Orbit permite crear L3s personalizados sobre Arbitrum.

**Comparación con ZK-Rollups:**

Aunque los Optimistic Rollups han alcanzado gran adopción, compiten con ZK-Rollups que utilizan pruebas de conocimiento cero (Zero-Knowledge Proofs) para validación instantánea sin períodos de disputa. Los ZK-Rollups ofrecen finalidad más rápida (minutos vs 7 días para retiros), mayor eficiencia en publicación de datos (solo pruebas criptográficas vs datos completos) y mejor privacidad potencial.

Sin embargo, los Optimistic Rollups mantienen ventajas significativas: compatibilidad EVM más madura y simple, menor complejidad técnica, costos de cómputo on-chain menores (no requieren verificar pruebas ZK costosas), y un ecosistema de herramientas más desarrollado. Los ZK-Rollups aún enfrentan desafíos en compatibilidad EVM completa (zkEVM) y requieren circuitos criptográficos complejos.

Es probable que ambas tecnologías coexistan: Optimistic Rollups para aplicaciones generalistas que priorizan compatibilidad y costos, ZK-Rollups para casos de uso que requieren finalidad rápida o privacidad (DeFi de alta frecuencia, pagos, identidad). La evolución del ecosistema determinará qué arquitectura prevalece en cada nicho.

#### ZK-Rollups: Validación Criptográfica Instantánea

Los ZK-Rollups utilizan pruebas de conocimiento cero para demostrar matemáticamente que las transacciones procesadas son válidas, sin necesidad de publicar todos los datos ni depender de períodos de disputa. Al enviar cada lote de transacciones, el rollup genera una prueba criptográfica (SNARK o STARK) que un contrato en Ethereum L1 puede verificar en segundos.

Esta arquitectura ofrece finalidad casi instantánea (retiros en minutos vs 7 días), mayor eficiencia de datos (solo se publica la prueba criptográfica), y fundamentos matemáticos más sólidos que la economía de incentivos de fraud proofs. Sin embargo, requieren computación intensiva para generar pruebas y enfrentan desafíos en compatibilidad EVM completa.

Proyectos destacados incluyen zkSync Era (zkEVM tipo 4 con compilador personalizado), StarkNet (usa Cairo y STARK proofs), Polygon zkEVM (zkEVM tipo 3 equivalente a EVM), Scroll (zkEVM tipo 3) y Linea (por ConsenSys).

**Conclusión sobre Rollups:**

Los Rollups son actualmente la solución de escalabilidad más adoptada porque combinan seguridad de Ethereum con costos significativamente menores y throughput superior. En la práctica, los Optimistic Rollups han demostrado ser una solución robusta y fiable en producción durante años, dando lugar a un ecosistema de "superchains" como Base (desarrollada por Coinbase sobre el OP Stack de Optimism) que buscan escalar Ethereum de forma masiva. La visión rollup-centric de Ethereum posiciona a L1 como capa de liquidación y disponibilidad de datos, mientras L2s manejan la ejecución y experiencia de usuario.

### Sidechains

Son blockchains independientes que corren en paralelo a Ethereum. Tienen sus propios mecanismos de seguridad y consenso, lo que las hace menos seguras que los Rollups, pero muy baratas. Polygon PoS es el ejemplo más conocido.

A diferencia de los Rollups que heredan la seguridad de Ethereum, las Sidechains dependen de su propio conjunto de validadores. Esto las hace más flexibles pero también más vulnerables si su red de validadores es pequeña o está comprometida.

### Plasma (Child Chains)

Plasma es una arquitectura de cadenas hijas (child chains) que funcionan como blockchains independientes ancladas a Ethereum. Cada Plasma chain procesa sus propias transacciones y periódicamente envía resúmenes (commitments) a la cadena principal.

Diferencias clave con otros enfoques:

- A diferencia de los State Channels, Plasma puede manejar muchos usuarios simultáneos.
- A diferencia de los Rollups, Plasma no publica todos los datos de las transacciones en Ethereum, solo compromisos criptográficos (hashes).
- A diferencia de las Sidechains, Plasma mantiene un mecanismo de salida de emergencia hacia Ethereum si la child chain actúa maliciosamente.

El problema principal de Plasma es que los usuarios deben monitorear constantemente la child chain para detectar comportamientos fraudulentos y ejecutar "salidas masivas" si es necesario. Esto lo hace complejo de implementar en la práctica. Por esta razón, Plasma ha sido mayormente superado por los Rollups en términos de adopción, aunque algunos proyectos como Polygon (originalmente Matic) comenzaron como implementaciones de Plasma antes de evolucionar hacia otras arquitecturas.

### Validiums

Similares a los ZK-Rollups, los Validiums también utilizan pruebas de conocimiento cero para garantizar la validez de las transacciones. Sin embargo, a diferencia de los ZK-Rollups, los Validiums almacenan los datos de las transacciones fuera de la cadena de Ethereum (off-chain), lo que reduce significativamente los costos de almacenamiento en la blockchain principal. Esto los hace ideales para aplicaciones que manejan grandes volúmenes de datos, como juegos o plataformas de redes sociales.

Un ejemplo destacado de implementación de Validiums es Immutable X, una solución de escalabilidad diseñada específicamente para NFTs (tokens no fungibles). Immutable X permite a los usuarios acuñar, comprar y vender NFTs sin pagar tarifas de Gas, mientras mantiene la seguridad de Ethereum para la validación de las transacciones mediante pruebas criptográficas.

Los Validiums representan una opción interesante para aplicaciones que priorizan la escalabilidad y los costos bajos, aunque sacrifican disponibilidad de datos al depender de un operador externo para almacenarlos.

## Puentes (Bridges)

Como cada blockchain es un sistema aislado, los puentes permiten mover activos de una red a otra. Funcionan bloqueando los tokens en la red de origen y creando una copia (token envuelto) en la red de destino. Son puntos críticos de seguridad en el ecosistema.

### ERC-7683: Cross-Chain Intents

El estándar [ERC-7683](https://www.erc7683.org/), propuesto conjuntamente por Across y Uniswap Labs, introduce un nuevo enfoque para las transacciones cross-chain basado en **intenciones** (intents) en lugar de mensajes específicos. A diferencia de los protocolos de mensajería tradicionales que transmiten instrucciones concretas entre cadenas, ERC-7683 permite a los usuarios expresar el **resultado final deseado** y deja que una red competitiva de actores especializados determine la mejor forma de ejecutarlo.

**Arquitectura de ERC-7683:**

El estándar define tres componentes técnicos principales:

1. **`CrossChainOrder`**: Estructura que especifica la intención del usuario con todos los parámetros necesarios:
   - `settlementContract`: Dirección del contrato que procesará la orden
   - `swapper`: Usuario que inicia la transacción
   - `nonce`: Valor único para prevenir repeticiones
   - `originChainId`: Identificador de la cadena de origen
   - `initiateDeadline`: Límite temporal para iniciar la orden
   - `fillDeadline`: Límite temporal para completar la orden
   - `orderData`: Datos específicos de implementación (tokens, cantidades, tarifas, etc.)

2. **`ISettlementContract`**: Interfaz estándar que deben implementar los contratos de liquidación:
   - `initiate()`: Función llamada por el filler para iniciar la liquidación en la cadena de origen, verificando la firma del usuario y procesando fondos
   - `resolve()`: Convierte una `CrossChainOrder` en `ResolvedCrossChainOrder`, descomponiendo los datos en formato genérico interoperable

3. **`ResolvedCrossChainOrder`**: Representación genérica de una orden que facilita la integración con diferentes sistemas de liquidación:
   - `swapperInputs`: Lista de tokens/activos que se toman del usuario
   - `swapperOutputs`: Lista de tokens/activos que recibirá el usuario
   - `fillerOutputs`: Lista de tokens/activos que recibirá el filler como compensación

**Flujo de trabajo intent-based:**

El proceso de ejecución de una transacción cross-chain bajo ERC-7683 sigue estos pasos:

1. **Firma de la orden**: El usuario (swapper) firma off-chain un mensaje definiendo su intención (por ejemplo, "quiero intercambiar 1000 USDC en Ethereum por 1000 USDC en Arbitrum").

2. **Diseminación**: La orden firmada se disemina a una red de **fillers** (actores especializados que compiten por ejecutar órdenes). Esta infraestructura puede ser compartida entre múltiples protocolos que implementen el estándar.

3. **Evaluación competitiva**: Los fillers evalúan si pueden cumplir la orden de forma rentable, considerando liquidez disponible, costes de gas, tarifas y rutas de ejecución.

4. **Iniciación**: El filler seleccionado llama a `initiate()` en el contrato de liquidación de la cadena de origen, presentando la orden firmada. El contrato verifica la firma y custodia los tokens del usuario.

5. **Cumplimiento**: El filler ejecuta las operaciones necesarias para entregar los tokens en la cadena de destino dentro del plazo definido (`fillDeadline`).

6. **Liquidación**: El contrato de liquidación finaliza la transacción, transfiriendo fondos al usuario en la cadena de destino y compensando al filler.

**Ventajas del modelo intent-based:**

- **Flexibilidad en la ejecución**: Los fillers pueden usar múltiples rutas y fuentes de liquidez para cumplir la intención, no están limitados a una implementación específica.
- **Descubrimiento de precios mediante competencia**: Múltiples fillers compiten por ejecutar órdenes, mejorando potencialmente las tasas de ejecución.
- **Infraestructura compartida**: Diferentes protocolos pueden usar la misma red de fillers y servicios de diseminación, mejorando la eficiencia del ecosistema.
- **Separación de intención y ejecución**: El usuario solo necesita expresar qué resultado desea, no cómo lograrlo técnicamente.

**Integración con otros estándares:**

ERC-7683 puede integrarse con estándares complementarios como [Permit2](https://github.com/Uniswap/permit2), simplificando la gestión de permisos y aprobaciones. Con Permit2, los usuarios pueden aprobar tanto la transferencia de tokens como la ejecución de la orden cross-chain con una única firma, mejorando la experiencia de usuario y reduciendo el número de transacciones necesarias.

**Limitaciones y riesgos:**

Aunque ERC-7683 estandariza el proceso de órdenes cross-chain y mejora la eficiencia, **hereda las limitaciones fundamentales de la interoperabilidad entre cadenas independientes**:

- **No garantiza atomicidad real**: Las operaciones en ambas cadenas no se ejecutan de forma atómica (todo o nada) sin confiar en actores externos.
- **Dependencia de fillers**: La red depende de que existan fillers con suficiente liquidez e incentivos económicos para cumplir las órdenes.
- **Ventanas de vulnerabilidad**: Durante la ejecución asíncrona existe una ventana temporal donde los fondos están en custodia o en tránsito.
- **Riesgo de fallo del filler**: Si el filler no cumple en el plazo establecido, pueden necesitarse mecanismos de reembolso o recuperación.

Como cualquier solución de interoperabilidad cross-chain, ERC-7683 debe usarse entendiendo sus vectores de riesgo, especialmente considerando el historial de miles de millones de dólares perdidos en vulnerabilidades de bridges e infraestructura cross-chain.

**Estado actual y adopción:**

ERC-7683 está siendo implementado por Across Protocol y Uniswap Labs como parte de su infraestructura de interoperabilidad. El estándar busca crear un ecosistema donde múltiples protocolos puedan compartir la misma capa de liquidación cross-chain, reduciendo la fragmentación y mejorando la experiencia de usuario. Sin embargo, como estándar relativamente nuevo, su adopción amplia y la madurez de sus implementaciones aún están en desarrollo.

## Interoperabilidad y Appchains

El ecosistema blockchain ha evolucionado hacia una arquitectura multi-cadena. Las Appchains son blockchains dedicadas exclusivamente a una aplicación específica, optimizadas para su caso de uso.

### EVM-Compatible Blockchains: Un Estándar de Facto

Uno de los desarrollos más significativos en el ecosistema blockchain es la adopción masiva de la **compatibilidad con EVM** como estándar de interoperabilidad. Decenas de blockchains han implementado la EVM como su máquina virtual, permitiendo que los contratos inteligentes escritos para Ethereum se desplieguen sin modificaciones en estas redes alternativas.

**Ventajas de la compatibilidad EVM:**

- **Portabilidad de código**: Los desarrolladores pueden reutilizar contratos existentes sin reescribirlos.
- **Ecosistema de herramientas compartido**: Wallets como MetaMask, frameworks como Hardhat y Foundry, y servicios de indexación funcionan en todas las cadenas EVM-compatible.
- **Reducción de la curva de aprendizaje**: Los desarrolladores solo necesitan aprender Solidity y el ecosistema Ethereum.
- **Liquidez y usuarios compartidos**: Los usuarios pueden interactuar con múltiples cadenas usando las mismas herramientas.

**Ejemplos de blockchains EVM-compatible:**

- **BNB Chain** (antes Binance Smart Chain): Blockchain de alto rendimiento con tarifas bajas, compatible con EVM.
- **Avalanche C-Chain**: Blockchain de alto rendimiento que implementa la EVM para contratos inteligentes.
- **Fantom Opera**: Red asíncrona con tiempos de bloque de ~1 segundo y compatibilidad total con EVM.
- **Polygon PoS**: Sidechain de Ethereum que ejecuta la EVM con transacciones más rápidas y baratas.
- **Arbitrum y Optimism**: Rollups L2 que implementan la EVM de forma nativa.

Esta compatibilidad ha convertido a la EVM en el **estándar de facto** para contratos inteligentes, similar a cómo SQL se convirtió en el estándar para bases de datos. Sin embargo, también existen alternativas como la **Solana Virtual Machine (SVM)**, **Move VM** (Aptos, Sui), o **CosmWasm** (Cosmos) que ofrecen diferentes paradigmas de programación y optimizaciones.

### Frameworks para Crear Appchains

Frameworks populares para crear Appchains:

- OP Stack: El framework de Optimism que permite crear rollups L2 personalizados de forma modular. Base (de Coinbase) y otros proyectos lo utilizan.
- Arbitrum Orbit: Similar al OP Stack, permite crear L2s o L3s personalizados sobre Arbitrum.
- Cosmos SDK: Para crear blockchains soberanas e interoperables mediante IBC (Inter-Blockchain Communication).
- Polkadot Substrate: Para crear parachains que se conectan al ecosistema Polkadot.
- Celestia: Modelo de disponibilidad de datos modular que separa consenso y ejecución, permitiendo crear rollups más eficientes.

## Herramientas y Ecosistema

Para interactuar con este ecosistema, los usuarios necesitan herramientas básicas:

- Etherscan: Un explorador de bloques centralizado que usa nodos completos (full nodes) y nodos históricos (archive nodes) para mostrar todas las transacciones, saldos y códigos de contratos de forma transparente. Cualquiera puede ejecutar su propio nodo completo descargando software como Geth o Besu y sincronizándose con la red.
- Ethernodes.org: Un servicio de monitoreo que proporciona estadísticas en tiempo real sobre la infraestructura de nodos de Ethereum. Muestra métricas clave como distribución geográfica de nodos, diversidad de clientes de ejecución y consenso (fundamental para la resiliencia de la red), historial de sincronización, y tendencias de descentralización. Es una herramienta valiosa para entender la salud y robustez de la red desde una perspectiva de infraestructura.
- MetaMask: Una billetera (wallet) que actúa como puente entre el navegador web y la blockchain, permitiendo a los usuarios gestionar sus claves y firmar transacciones. Otras opciones incluyen MyEtherWallet.
- ENS (Ethereum Name Service): Sistema que permite usar nombres legibles (ej. nombre.eth) en lugar de direcciones hexadecimales largas.
- Redes de Prueba (Testnets): Redes como Sepolia o Holesky que simulan el entorno de Ethereum pero usan ETH sin valor real. Son fundamentales para que desarrolladores y usuarios prueben aplicaciones sin riesgo económico antes de usarlas en la red principal (Mainnet).

## Objetivos y Hoja de Ruta Futura

Ethereum tiene varios objetivos ambiciosos en su roadmap para mejorar la descentralización, escalabilidad y eficiencia:

### Single-Slot Finality (SSF)

Single-Slot Finality (SSF) es una propuesta fundamental del roadmap de Ethereum que busca lograr finalidad económica de transacciones en un único slot de 12 segundos, eliminando el período actual de ~15 minutos (2 epochs) requerido por el mecanismo de finalidad de Casper FFG. Esta mejora transformaría la experiencia de usuario de Ethereum, ofreciendo garantías de irreversibilidad comparables a sistemas de pagos tradicionales mientras mantiene las propiedades de seguridad criptoeconómica de la blockchain.

**Problema Actual: Latencia de Finalidad en Casper FFG**

El mecanismo de consenso actual de Ethereum, Gasper (combinación de Casper FFG para finalidad y LMD-GHOST para selección de fork), requiere un proceso de dos pasos para alcanzar finalidad:

1. **Justificación (Justified):** Un checkpoint (bloque al inicio de un epoch) es justificado cuando al menos 2/3 del ETH en staking ha atestiguado a favor de él.

2. **Finalización (Finalized):** Cuando en el epoch siguiente un nuevo checkpoint es justificado, el checkpoint anterior se considera finalizado.

Este proceso típicamente toma 2 epochs completos (~12.8 minutos con 32 slots por epoch de 12 segundos cada uno), aunque en condiciones de red adversas puede extenderse indefinidamente si no se alcanza el umbral de 2/3 de attestations. Bajo condiciones óptimas, la finalidad se logra en aproximadamente 15 minutos desde que una transacción es incluida en un bloque.

Esta latencia introduce fricciones significativas en casos de uso sensibles al tiempo:

- **Exchanges centralizados:** Requieren múltiples confirmaciones antes de acreditar depósitos de usuarios, típicamente esperando finalidad o cerca de ella (~10-20 confirmaciones).
- **Bridges cross-chain:** Deben esperar finalidad antes de desbloquear activos en la cadena destino para evitar riesgos de reorganizaciones.
- **Pagos de alto valor:** Comerciantes que aceptan pagos grandes no pueden estar seguros de irreversibilidad hasta después de ~15 minutos.
- **Aplicaciones DeFi:** Protocolos que dependen de finalidad para liquidaciones o settlement enfrentan ventanas de incertidumbre.

**Arquitectura Técnica de SSF**

Single-Slot Finality propone una reestructuración del protocolo de consenso para que validadores voten tanto sobre la cabeza de la cadena (head vote, para selección de fork) como sobre finalidad (finality vote) dentro del mismo slot. La diferencia fundamental con el sistema actual es que las attestations combinarían ambas funciones: los validadores atestiguan simultáneamente que un bloque es el mejor candidato para la cabeza de la cadena Y que debería ser finalizado si 2/3 de validadores están de acuerdo.

El proceso simplificado funcionaría así:

1. **Propuesta del bloque (slot N):** Un validador seleccionado aleatoriamente propone un bloque para el slot N.

2. **Votación combinada:** Todos los validadores asignados al slot N publican una attestation que declara:
   - Este bloque es la cabeza canónica de la cadena (LMD-GHOST vote)
   - Este bloque debería ser finalizado (Casper FFG vote)

3. **Agregación de votos:** Si al menos 2/3 del ETH total en staking atestigua a favor del bloque dentro del slot, el bloque alcanza finalidad inmediatamente.

4. **Finalidad en 12 segundos:** Al final del slot (~12 segundos después de la propuesta), el bloque está económicamente finalizado y no puede ser revertido sin destruir >1/3 del ETH en staking.

Este modelo elimina la estructura de epochs para finalidad, aunque puede mantenerla para otras funciones administrativas como rotación de comités de validadores o distribución de recompensas.

**Desafíos Técnicos Fundamentales**

La implementación de SSF enfrenta obstáculos técnicos significativos que han retrasado su desarrollo:

**1. Carga de Firma y Agregación**

Con aproximadamente 900,000 validadores activos en Ethereum (enero 2026), cada uno con 32 ETH en stake, procesar y agregar firmas de todos los validadores en un solo slot de 12 segundos presenta desafíos masivos de throughput:

- **Firmas BLS:** Cada attestation requiere una firma BLS12-381 (96 bytes). Aunque BLS permite agregación eficiente de firmas, procesar y agregar ~900,000 firmas en 12 segundos requiere:
  - Propagación de mensajes en la red P2P en subsegundo
  - Agregación distribuida mediante subcomités
  - Verificación de firmas agregadas por todos los nodos

- **Throughput de mensajes:** 900,000 attestations en 12 segundos = ~75,000 mensajes/segundo que deben propagarse por la red gossip, agregarse y verificarse.

- **Ancho de banda:** Incluso con agregación perfecta, la firma final agregada y los datos asociados (bitmask de participantes, metadatos) representan carga significativa de comunicación.

El protocolo actual distribuye esta carga a través de 32 slots en un epoch, permitiendo que diferentes subconjuntos de validadores atesten en diferentes slots. SSF requiere concentrar toda esta actividad en una ventana de 12 segundos.

**2. Escalabilidad del Conjunto de Validadores**

El crecimiento del conjunto de validadores agrava el problema. Con el staking se volviendo cada vez más popular y la introducción de servicios de liquid staking (Lido, Rocket Pool) que permiten participación con menos de 32 ETH, el número de validadores puede crecer a varios millones:

- **Proyecciones:** Si el ETH en staking crece de ~30M ETH actuales a 60M ETH, el número de validadores se duplicaría a ~1.8 millones.
- **Límite físico:** En algún punto, el número de validadores excede lo que puede procesarse en 12 segundos incluso con las optimizaciones más agresivas de agregación y propagación.

Este problema fundamental requiere mecanismos que limiten o estructuren la participación de validadores en cada slot.

**3. Latencia de Propagación y Sincronización Global**

Ethereum es una red P2P global donde nodos están distribuidos geográficamente. La latencia de propagación de mensajes entre nodos puede variar de decenas de milisegundos (conexiones continentales de baja latencia) a cientos de milisegundos (conexiones intercontinentales o nodos con conectividad limitada):

- **Tiempo disponible:** En un slot de 12 segundos, los primeros ~4 segundos se usan para proponer y propagar el bloque. Quedan ~8 segundos para que validadores atesten y sus attestations se agreguen y propaguen.
- **Sincronización:** Validadores en diferentes regiones pueden ver el bloque en momentos ligeramente diferentes, causando que algunos atesten antes que otros. La agregación debe esperar a recibir suficientes attestations antes de publicar la firma agregada.
- **Condiciones adversas:** Particiones temporales de red o congestión podrían prevenir que validadores atesten a tiempo, fallando en alcanzar el umbral de 2/3 necesario para finalidad.

La robustez del protocolo requiere que funcione incluso cuando una fracción significativa de validadores experimenta latencia elevada o pérdida de paquetes temporaria.

**Soluciones Propuestas y Research Directions**

**1. Comités de Finalidad Rotatorios**

En lugar de requerir que todos los validadores atesten en cada slot, SSF podría usar comités rotatorios donde solo un subconjunto representativo de validadores (por ejemplo, 10,000-50,000) atestigua para finalidad en cada slot. Estos comités rotarían periódicamente para garantizar que todos los validadores participen a lo largo del tiempo:

- **Selección aleatoria:** Usar RANDAO para seleccionar aleatoriamente comités de finalidad de forma impredecible y resistente a manipulación.
- **Peso de voto:** Cada miembro del comité vota proporcional al ETH que tiene en stake, permitiendo que comités más pequeños representen el peso económico total.
- **Umbral ajustado:** Requerir 2/3 del peso del comité (no de todo el ETH en staking) para alcanzar finalidad, con penalizaciones para validadores en el comité que no participan.

Este enfoque reduce la carga de mensajes en el protocolo mientras mantiene seguridad criptoeconómica comparable, asumiendo que el comité es suficientemente grande y seleccionado aleatoriamente para que atacar requiera comprometer una fracción sustancial del ETH total en staking.

**2. Agregación Jerárquica y Subnets Especializadas**

Mejorar la eficiencia de agregación de firmas mediante estructura jerárquica:

- **Subnets de agregación:** Dividir validadores en subnets que agregan firmas localmente antes de propagar agregados parciales a nivel global.
- **Aggregators especializados:** Validadores designados (rotatorios) actúan como agregadores que reciben attestations de sus subnets, producen firmas agregadas parciales, y las combinan en una firma final global.
- **Propagación optimizada:** Usar estructura de árbol o DAG para diseminación de agregados parciales, reduciendo redundancia en la red.

Protocolos como Ethereum ya usan aggregation committees para attestations; SSF extendería y optimizaría estos mecanismos para manejar la carga aumentada.

**3. Horn Protocol y Otros Algoritmos de Consenso Alternativos**

Investigación activa explora algoritmos de consenso completamente nuevos que logran finalidad en tiempo lineal con el número de participantes:

- **Horn:** Propuesta de Francesco D'Amato que utiliza estructura de DAG y voting por rounds para finalidad en tiempo O(n) en lugar de requerir broadcast completo.
- **Two-Phase Protocols:** Diseños donde la primera fase alcanza consenso tentativo rápidamente y la segunda fase (posiblemente más lenta) provee finalidad económica.
- **Tendermint-inspired:** Algoritmos BFT (Byzantine Fault Tolerant) tradicionales adaptados para el contexto de PoS de Ethereum, que logran finalidad en número fijo de rounds de comunicación.

Estos enfoques requieren cambios fundamentales en el protocolo de consenso pero podrían habilitar SSF sin compromisos de seguridad o descentralización.

**4. Reducción del Tamaño del Conjunto de Validadores**

Estrategias para limitar o estructurar el crecimiento del número de validadores:

- **Requisito de stake aumentado:** Incrementar el mínimo de 32 ETH requeridos para ser validador (polémico porque reduciría accesibilidad).
- **Delegación nativa:** Permitir que múltiples depositantes deleguen su ETH a un único validador profesional, reduciendo el número de participantes activos mientras manteniendo distribución económica.
- **Liquid Staking:** Fomentar uso de protocolos de liquid staking donde fondos de muchos usuarios se pooling en un número menor de validadores técnicamente competentes.

Estas opciones generan tensiones con objetivos de descentralización y deben equilibrarse cuidadosamente.

**Estado Actual de la Investigación y Roadmap**

Single-Slot Finality es actualmente objeto de investigación activa por parte de la Ethereum Foundation y equipos académicos. Documentos clave incluyen:

- **Research posts en ethresear.ch:** Comunidad de investigadores publica propuestas y análisis técnicos detallados.
- **Vitalik Buterin's roadmap updates:** Actualizaciones periódicas sobre priorización de SSF en el contexto del roadmap general de Ethereum.
- **Prototype implementations:** Clients como Prysm y Lighthouse están experimentando con variantes de SSF en testnets privadas.

La implementación de SSF en mainnet no tiene fecha definida y depende de resolver los desafíos técnicos mencionados. Es probable que requiera un hard fork significativo y coordinación extensa entre todos los clientes de consenso. Estimaciones conservadoras sugieren que SSF podría implementarse en el horizonte 2027-2028, aunque esto depende críticamente de avances en investigación y testing exhaustivo en testnets públicas.

**Beneficios Esperados de SSF**

Una vez implementado, SSF transformaría múltiples aspectos del ecosistema Ethereum:

- **UX radicalmente mejorada:** Usuarios verían transacciones confirmadas como finales en ~12-15 segundos, comparable a sistemas de pagos instantáneos tradicionales.
- **Bridges más seguros y eficientes:** Cross-chain bridges podrían operar con ventanas de confirmación cortas, reduciendo riesgos de reorganizaciones y mejorando capital efficiency.
- **DeFi de menor latencia:** Protocolos de trading, lending y derivatives podrían ofrecer settlement más rápido sin sacrificar seguridad.
- **Compatibilidad con Web2:** Aplicaciones que requieren confirmación rápida (e-commerce, gaming, micropagos) se volverían viables en Ethereum L1.
- **Simplificación del protocolo:** Eliminar la complejidad de epochs y finalidad retardada simplificaría implementaciones de clientes y razonamiento sobre seguridad.

SSF representa uno de los objetivos técnicos más ambiciosos del roadmap de Ethereum, requiriendo innovación en criptografía, teoría de consenso distribuido, ingeniería de redes P2P y coordinación social a escala de ecosistema completo.

### Account Abstraction (ERC-4337)

Mejora a nivel de aplicación (no requiere cambios en el protocolo) que permite Smart Contract Wallets con recuperación social, transacciones patrocinadas (paymasters), batching, firmas flexibles y lógica programable. Implementado mediante UserOperations procesadas por bundlers que envían transacciones al contrato EntryPoint. Ver [Experiencia de usuario](../../101/9-1-user-experience.md) para detalles completos de arquitectura e implementaciones.

### Statelessness

Objetivo de reducir la necesidad de que los nodos mantengan todo el estado de la blockchain, permitiendo verificaciones parciales mediante técnicas como "Verkle Trees". Esto disminuiría drásticamente los requisitos de cómputo y almacenamiento para ejecutar nodos, mejorando la descentralización al hacer más accesible la participación en la red.

### RANDAO: Aleatoriedad Descentralizada en Proof-of-Stake

RANDAO es el mecanismo de generación de aleatoriedad que Ethereum utiliza desde The Merge para seleccionar aleatoriamente validadores que proponen bloques y forman comités de attestation. La aleatoriedad verificable es crítica para la seguridad del protocolo: si atacantes pudieran predecir o manipular qué validador será seleccionado, podrían ejecutar ataques dirigidos o censurar transacciones específicas.

El proceso funciona mediante un esquema de commit-reveal donde cada validador propone un número aleatorio secreto mediante un hash, luego revela ese número en su bloque propuesto. Estos números revelados se combinan mediante XOR para generar el valor aleatorio final que determina selecciones de validadores futuros. La clave está en que ningún validador individual puede predecir el resultado final porque depende de las contribuciones de todos los demás validadores, y manipular el resultado requeriría colusión masiva o control de la mayoría de validadores seleccionados en ese epoch.

El beacon chain mantiene un RANDAO mix acumulativo que se actualiza cada epoch combinando el mix anterior con las nuevas revelaciones de validadores. Este mix se usa como seed para el algoritmo de shuffling que asigna validadores a slots específicos y comités de attestation. El protocolo garantiza que las asignaciones se conocen con suficiente anticipación para que validadores puedan prepararse, pero no con tanta anticipación que atacantes puedan organizar manipulaciones complejas.

Las limitaciones de RANDAO incluyen que el último validador en revelar su número tiene pequeña capacidad de influencia: puede elegir no proponer su bloque si el resultado aleatorio no le favorece, aunque esto significa perder las recompensas de ese slot. Para aplicaciones que requieren aleatoriedad con garantías criptográficas más fuertes, Ethereum está investigando integración de VDFs (Verifiable Delay Functions).

Los VDFs son funciones que requieren un tiempo computacional mínimo secuencial para evaluarse, pero cuyos resultados pueden verificarse rápidamente. Un VDF aplicado sobre el output de RANDAO agregaría un delay obligatorio antes de que el número aleatorio final sea conocible, eliminando la capacidad del último validador de manipular el resultado mediante decisión de publicar o no su bloque. Este delay debe ser suficiente para que sea computacionalmente imposible calcular el resultado antes del deadline de propuesta del bloque, pero lo suficientemente corto para no ralentizar el protocolo significativamente.

La implementación práctica de VDFs enfrenta desafíos técnicos sustanciales. Requiere hardware especializado para computación del VDF que debe ser ampliamente accesible para evitar centralización, verificación eficiente de outputs en smart contracts para que el protocolo pueda usar el resultado on-chain sin costos prohibitivos de gas, y consensus sobre parámetros de timing que balanceen seguridad con rendimiento de la red. Proyectos como el VDF de la Ethereum Foundation y colaboraciones con Protocol Labs están desarrollando implementaciones prácticas.

### Verkle Trees: Eficiencia Radical para Stateless Clients

Verkle Trees representan una evolución fundamental de la estructura de datos que Ethereum usa para almacenar su estado, reemplazando los Merkle Patricia Trees actuales con una construcción criptográfica que reduce dramáticamente el tamaño de witnesses necesarios para verificar porciones del estado. Esta optimización es crítica para hacer viable la visión de stateless clients donde nodos pueden verificar bloques sin mantener copia completa del estado de Ethereum.

En el modelo actual, cada transacción que accede cuentas o storage slots requiere un witness: una prueba criptográfica de que esos datos existen en el estado global. Los Merkle Patricia Trees generan witnesses cuyo tamaño crece logarítmicamente con el número de cuentas en Ethereum, alcanzando múltiples kilobytes por transacción en bloques complejos. Un bloque con 200 transacciones podría requerir witnesses de varios megabytes, haciendo impráctico sincronizar o verificar bloques en dispositivos con ancho de banda limitado o recursos computacionales restringidos.

Verkle Trees utilizan compromisos de Pedersen basados en curvas elípticas que permiten construir pruebas mucho más compactas. La diferencia arquitectural clave es que Merkle Trees tradicionales requieren incluir todos los nodos hermanos del path desde la hoja hasta la raíz para verificación, mientras que Verkle Trees usan propiedades matemáticas de los compromisos para agregar múltiples pruebas en una sola proof compacta. Un witness de Verkle Tree para un bloque completo típicamente ocupa ~20-50 KB independientemente del número de cuentas accedidas, comparado con varios MB en el sistema actual.

La estructura específica divide el state en chunks de 32 bytes, organiza estos chunks en una estructura de árbol con branching factor alto (típicamente 256 hijos por nodo interno), y usa compromisos de Pedersen en cada nivel que permiten agregación eficiente de pruebas. Los clientes pueden verificar que un chunk específico pertenece al state root combinando un vector de commitment con un índice, sin necesitar el camino completo de hermanos.

Las implicaciones para descentralización son profundas. Stateless clients que solo almacenan block headers y verifican transactions mediante witnesses pueden ejecutarse en hardware extremadamente limitado: smartphones, dispositivos IoT, navegadores web. Esto hace técnicamente viable que millones de usuarios ejecuten nodos completos de verificación sin requisitos de almacenamiento de cientos de gigabytes. La red se vuelve más resistente a censura porque verificar la cadena no requiere recursos institucionales.

La transición a Verkle Trees es un hard fork complejo que requiere migrar todo el estado existente de Ethereum desde Merkle Patricia Trees a la nueva estructura. La estrategia de migración contempla un período de transición donde ambas estructuras coexisten, permitiendo que nodos gradualmente conviertan el estado mientras mantienen capacidad de verificar bloques antiguos. Los testnet de shadow forks ya han demostrado la viabilidad técnica de esta migración, pero el despliegue en mainnet requiere coordinación cuidadosa para evitar disrupciones.

### Data Availability Sampling: Escalando sin Comprometer Verificabilidad

Data Availability Sampling (DAS) es una técnica criptográfica que permite a light clients verificar con alta probabilidad que los datos de un bloque están disponibles en la red sin descargar el bloque completo. Este mecanismo es fundamental para scaling mediante Danksharding, donde el throughput de datos crece dramáticamente pero los nodos individuales no pueden almacenar todo.

El problema que DAS resuelve es crítico para rollups y L2s. Cuando un rollup publica un batch de transacciones a Ethereum, necesita garantizar que los datos están públicamente disponibles para que cualquiera pueda reconstruir el estado del rollup y detectar comportamiento malicioso del operador. Si el operador pudiera publicar un commitment a datos pero no hacer los datos disponibles, podría robar fondos de usuarios sin que nadie pueda probar el robo reconstruyendo el estado correcto.

La solución tradicional requiere que todos los nodos descarguen y verifiquen todos los datos, limitando el throughput a lo que un solo nodo puede procesar. DAS permite a cada nodo muestrear aleatoriamente pequeñas porciones de los datos mediante erasure coding. El bloque se extiende mediante códigos de corrección de errores de forma que si más del 50% de las porciones están disponibles, el bloque completo puede reconstruirse. Un light client que muestrea aleatoriamente 30-50 chunks puede alcanzar confianza del 99.99% de que el bloque completo está disponible.

La mecánica técnica utiliza códigos Reed-Solomon para extender el bloque original de tamaño N a 2N chunks donde cualquier N chunks permiten reconstruir el bloque original. Los chunks se organizan en un grid bidimensional y se publican compromisos KZG (Kate-Zaverucha-Goldberg) a las filas y columnas. Un light client solicita chunks aleatorios a peers de la red, verifica que coinciden con los compromisos KZG publicados, y si recibe exitosamente sus samples aleatorios, concluye con alta probabilidad que el bloque completo está disponible.

El networking layer implementa un protocolo de muestreo distribuido donde nodos propagan chunks a subnets específicas determinadas por IDs de nodo. Un light client se suscribe a múltiples subnets aleatorias, recibe los chunks correspondientes, y ejecuta el sampling. Si detecta chunks faltantes, publica fraud alert que activa recuperación colaborativa donde nodos con los chunks completos los redistribuyen.

Proto-Danksharding (EIP-4844) implementa una versión simplificada de esta arquitectura introduciendo blob-carrying transactions donde los blobs contienen datos de rollup verificables mediante compromisos KZG. Full Danksharding expandirá esto con DAS completo permitiendo throughput de varios megabytes por segundo de datos de disponibilidad garantizada, suficiente para soportar cientos de rollups escalando Ethereum a millones de transacciones por segundo efectivas sin comprometer descentralización.

Los desafíos incluyen garantizar diversidad de red suficiente para que muestreo aleatorio no permita ataques donde atacantes controlan regiones de la topología de red y pueden ocultar selectivamente chunks de ciertos nodos, implementar incentivos para que nodos honestos almacenen y sirvan chunks correctamente sin recompensas explícitas en todos los casos, y manejar condiciones de red adversarias donde conectividad temporalmente degradada podría causar falsas alarmas de disponibilidad.

### MegaETH: Hacia la Latencia Ultrabaja

MegaETH es un proyecto de investigación y desarrollo que busca construir un cliente de ejecución de Ethereum de altísimo rendimiento. Con el respaldo de figuras como Vitalik Buterin y Joseph Lubin, su objetivo es alcanzar más de 100,000 TPS con latencias de sub-milisegundo. Esto habilitaría una nueva generación de aplicaciones en tiempo real sobre Ethereum, como juegos de alta frecuencia, exchanges de derivados perpetuos (perps), y agentes de IA autónomos que operan on-chain.

### Restaking y EigenLayer

Aunque no es nativo del protocolo Ethereum, EigenLayer ha surgido como una solución externa relevante en el ecosistema que permite el "restaking": validadores de Ethereum pueden reutilizar su ETH en stake para asegurar servicios adicionales (middleware, oráculos, puentes, etc.), extendiendo la seguridad económica de Ethereum a otras aplicaciones. Esto mejora la eficiencia del capital y crea nuevos modelos de seguridad compartida.

EigenLayer abre la puerta a nuevos modelos de arquitectura como las **"Superchains"** (un concepto popularizado por Optimism), que son redes L2 interconectadas que comparten seguridad y comunicación, funcionando como un ecosistema cohesionado. Esto ofrece a las DApps una elección estratégica: pueden operar como cadenas independientes aseguradas por restaking para tener soberanía total, o desplegarse en un L2 para maximizar la interoperabilidad y consolidar su estado directamente en Ethereum. La elección depende del modelo de seguridad y del nivel de integración que la aplicación necesite.

### Resistencia Cuántica

Uno de los objetivos a largo plazo de Ethereum es lograr resistencia contra ataques de computadoras cuánticas. Las computadoras cuánticas podrían, en teoría, romper los algoritmos criptográficos actuales (como ECDSA usado para firmar transacciones). La comunidad de Ethereum está investigando e implementando algoritmos criptográficos post-cuánticos que sean resistentes a este tipo de ataques, asegurando la viabilidad del protocolo en el futuro cuando la computación cuántica se vuelva práctica.

## Referencias

- [Ethereum Whitepaper & Yellowpaper](https://ethereum.org/en/whitepaper/)
- [Bit2Me Academy - Ethereum](https://academy.bit2me.com/que-es-ethereum-eth-criptomoneda/)
- [EVM Explained](https://academy.bit2me.com/que-es-ethereum-virtual-machine-evm/)

---
