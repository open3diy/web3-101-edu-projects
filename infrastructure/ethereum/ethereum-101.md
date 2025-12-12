# Ethereum 101

Ethereum es el primer computador con estado distribuido del mundo, un espacio donde se ejecutan contratos inteligentes que sirven a aplicaciones, principalmente descentralizadas (DApps). A diferencia de Bitcoin, que fue diseñado principalmente como un sistema de dinero digital, Ethereum permite la programación de cualquier tipo de lógica gracias a que es Turing completo, pero limitado por el sistema de Gas: cada operación tiene un coste computacional medido en Gas, que debe pagarse en Ether, evitando así bucles infinitos y asegurando que toda ejecución tenga un costo finito.

Ethereum nació como una alternativa a Bitcoin (altcoin), pero ampliando significativamente su funcionalidad mediante contratos inteligentes. Fue fundado por Vitalik Buterin y cuenta con una Fundación Ethereum que actúa como punto de referencia técnico y organizativo, aunque no como autoridad centralizada.

En esencia, un smart contract redefine la confianza en el software: en lugar de confiar en un servidor centralizado, se confía en una red descentralizada que verifica, ejecuta y certifica acuerdos mediante código.

Propósito principal: Actúan como registro contable de liquidaciones, consolidando acuerdos entre partes de forma:

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

## La Máquina Virtual de Ethereum (EVM)

La EVM es el entorno de ejecución donde se ejecutan los contratos inteligentes de Ethereum.

La especificación formal de la EVM se encuentra en el Yellow Paper, un documento técnico que define el comportamiento de la máquina virtual, sus instrucciones (opcodes), y cómo procesa las transacciones y el estado de la red.

Estas operaciones tienen un coste denominado Gas, que no es la moneda Ether en sí, sino una unidad de medida del esfuerzo computacional. El Gas se paga en Gwei (una fracción de Ether, 10^-9 ETH) y sirve para evitar bucles infinitos y recompensar a los validadores.

## Contratos Inteligentes y Solidity

Un smart contract es el lugar donde se codifican las condiciones que debe cumplir un acuerdo entre partes.

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

La estandarización a través de Propuestas de Mejora de Ethereum (EIPs) ha sido clave para la interoperabilidad, permitiendo que wallets, exchanges y otras DApps interactúen con cualquier token que siga las reglas. Los estándares más importantes son:

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

Este cambio redujo el consumo de energía en más de un 99% y cambió el modelo de seguridad de gasto energético a riesgo económico. La red genera un nuevo bloque aproximadamente cada 12-15 segundos.

### Arquitectura de Capas

Ethereum adoptó una arquitectura modular que separa responsabilidades en dos capas principales que operan en conjunto:

**Capa de Ejecución (Execution Layer):**

Es el entorno donde se procesan las transacciones, se ejecutan los contratos inteligentes (EVM) y se gestiona el estado de la red (cuentas, balances, etc.). Esta capa es la evolución de lo que antes se conocía como "Ethereum 1.0". Los clientes de ejecución, como Geth, Besu o Nethermind, se encargan de estas tareas y de propagar las nuevas transacciones por la red.

**Capa de Consenso (Consensus Layer):**

Es la responsable de la seguridad de la red mediante el mecanismo de Proof of Stake. Esta capa no ejecuta transacciones, sino que se encarga de ordenar y validar los bloques propuestos por los validadores, asegurando que la red llegue a un acuerdo sobre el estado de la cadena. También gestiona la comunicación P2P entre nodos y es fundamental para la **disponibilidad de datos** (Data Availability), una función crucial para la escalabilidad con Rollups. Esta capa corresponde a la antigua "Beacon Chain" y es gestionada por clientes como Prysm, Lighthouse o Teku.

Ambas capas se comunican a través de una interfaz específica (la *Engine API*), permitiendo que cada una se desarrolle y optimice de forma independiente.

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

## Protocolos en Desarrollo

Ethereum tiene varios protocolos complementarios que aún están en desarrollo o no han alcanzado adopción masiva, pero que forman parte de la visión original de un ecosistema descentralizado completo:

### Swarm

Swarm es un protocolo de almacenamiento descentralizado diseñado para Ethereum, que permite almacenar datos de forma distribuida en la red. Aunque está en desarrollo, actualmente no se usa de forma amplia. En la práctica, el ecosistema utiliza alternativas como IPFS (InterPlanetary File System) o Siacoin para necesidades de almacenamiento descentralizado.

Algunos nodos de Ethereum podrían utilizar Swarm en el futuro para no tener que almacenar la base de datos completa de la blockchain, permitiendo nodos más ligeros y accesibles.

### Whisper y Waku

Whisper es un protocolo de mensajería descentralizada diseñado para permitir comunicaciones privadas, cifradas y anónimas entre usuarios o aplicaciones dentro del ecosistema Ethereum. Es importante destacar que **no es parte del protocolo principal** que maneja transacciones o consenso en la red Ethereum, sino una capa complementaria para comunicaciones.

Se usa principalmente para comunicación entre contratos inteligentes y aplicaciones descentralizadas que requieren mensajería privada y resistente a la censura.

**Waku** está emergiendo como la evolución de Whisper, con mejoras en eficiencia, escalabilidad y privacidad. Waku está siendo desarrollado activamente y podría convertirse en el estándar de mensajería descentralizada del ecosistema Ethereum en el futuro.

## Escalabilidad

Ethereum tiene una capacidad limitada de transacciones por segundo en su capa base (Layer 1), lo que puede elevar los costos. El problema fundamental es que cada nodo de la red replica y valida todas las transacciones, lo que garantiza descentralización pero limita el rendimiento. Para solucionar esto sin sacrificar completamente la seguridad, existen varias estrategias de escalabilidad.

### Sharding (Fragmentación)

Sharding es una estrategia que divide la blockchain en fragmentos (shards) dentro de la propia red de nodos de Ethereum. A diferencia de otras soluciones de escalabilidad que funcionan como capas externas (Rollups, State Channels) o redes paralelas independientes (Sidechains, Plasma), el Sharding modifica la arquitectura interna de Ethereum. Cada shard funciona como una cadena semi-independiente con su propio estado y conjunto de validadores, pero todos los shards forman parte de la misma red Ethereum.

En el sharding cada fragmento mantiene su propio libro contable separado de forma permanente, a diferencia de los State Channels o Rollups que consolidan transacciones.

El concepto clave: En lugar de que todos los nodos repliquen todas las transacciones (lo cual es costoso en almacenamiento y hace que solo organizaciones con recursos puedan mantener nodos completos, centralizando el sistema), cada nodo solo valida un subconjunto de fragmentos. Esto permite que la red procese múltiples cadenas en paralelo sin salir de la infraestructura base de Ethereum.

Estado actual en Ethereum:

Originalmente, Ethereum 2.0 planeaba implementar 64 shards. Sin embargo, tras el éxito de los Rollups, la hoja de ruta cambió hacia "Danksharding", un modelo donde los shards se usan principalmente para disponibilidad de datos (data availability) que beneficia a los Rollups, en lugar de ejecutar transacciones directamente.

Es importante destacar que Danksharding completo aún no está implementado. Lo que existe actualmente es "proto-danksharding" (introducido con EIP-4844), una versión preliminar que sienta las bases para el sistema completo, permitiendo a los Rollups publicar datos de forma más eficiente mediante "blobs" de datos temporales.

La idea es que los shards almacenen grandes cantidades de datos de forma descentralizada y económica, permitiendo que los Rollups publiquen sus datos de transacciones de manera más barata, aumentando así el rendimiento general del ecosistema sin comprometer la descentralización.

Desafío principal: Coordinar la seguridad entre fragmentos y evitar que atacar un solo shard comprometa el sistema completo requiere mecanismos complejos de consenso y sincronización.

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

Existen dos tipos principales:

- Optimistic Rollups: Asumen que las transacciones son válidas por defecto. Si alguien detecta un fraude, tiene un periodo de tiempo (generalmente 7 días) para demostrarlo mediante pruebas de fraude. Ejemplos: Optimism, Arbitrum.

- ZK-Rollups: Usan matemáticas avanzadas (pruebas de conocimiento cero) para demostrar criptográficamente que las transacciones son válidas al instante, sin periodos de espera. Ejemplos: zkSync, Starknet.

Los Rollups son actualmente la solución de escalabilidad más adoptada porque combinan seguridad de Ethereum con costos significativamente menores. En la práctica, los **Optimistic Rollups** han demostrado ser una solución robusta y fiable en producción durante años, dando lugar a un ecosistema de "superchains" como **Base** (desarrollada por Coinbase sobre el OP Stack de Optimism), que buscan escalar Ethereum de forma masiva.

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

## Interoperabilidad y Appchains

El ecosistema blockchain ha evolucionado hacia una arquitectura multi-cadena. Las Appchains son blockchains dedicadas exclusivamente a una aplicación específica, optimizadas para su caso de uso.

Frameworks populares para crear Appchains:

- OP Stack: El framework de Optimism que permite crear rollups L2 personalizados de forma modular. Base (de Coinbase) y otros proyectos lo utilizan.
- Arbitrum Orbit: Similar al OP Stack, permite crear L2s o L3s personalizados sobre Arbitrum.
- Cosmos SDK: Para crear blockchains soberanas e interoperables mediante IBC (Inter-Blockchain Communication).
- Polkadot Substrate: Para crear parachains que se conectan al ecosistema Polkadot.
- Celestia: Modelo de disponibilidad de datos modular que separa consenso y ejecución, permitiendo crear rollups más eficientes.

## Herramientas y Ecosistema

Para interactuar con este ecosistema, los usuarios necesitan herramientas básicas:

- Etherscan: Un explorador de bloques centralizado que usa nodos completos (full nodes) y nodos históricos (archive nodes) para mostrar todas las transacciones, saldos y códigos de contratos de forma transparente. Cualquiera puede ejecutar su propio nodo completo descargando software como Geth o Besu y sincronizándose con la red.
- MetaMask: Una billetera (wallet) que actúa como puente entre el navegador web y la blockchain, permitiendo a los usuarios gestionar sus claves y firmar transacciones. Otras opciones incluyen MyEtherWallet.
- ENS (Ethereum Name Service): Sistema que permite usar nombres legibles (ej. nombre.eth) en lugar de direcciones hexadecimales largas.
- Redes de Prueba (Testnets): Redes como Sepolia o Holesky que simulan el entorno de Ethereum pero usan ETH sin valor real. Son fundamentales para que desarrolladores y usuarios prueben aplicaciones sin riesgo económico antes de usarlas en la red principal (Mainnet).

## Objetivos y Hoja de Ruta Futura

Ethereum tiene varios objetivos ambiciosos en su roadmap para mejorar la descentralización, escalabilidad y eficiencia:

### Single-Slot Finality (SSF)

Propuesta para reducir el tiempo de finalización de bloques a un solo slot (~12 segundos), en lugar del sistema actual que requiere aproximadamente 15 minutos (2 epochs) para lograr finalidad. Esto haría las transacciones confirmadas de forma definitiva mucho más rápido, mejorando la experiencia de usuario.

### Account Abstraction (ERC-4337)

Una mejora implementada a nivel de capa superior (no en el consenso base) que permite crear "carteras inteligentes" con funcionalidades avanzadas como:

- Recuperación de cuentas sin frases semilla
- Transacciones patrocinadas (gasless transactions)
- Operaciones por lotes
- Lógica de firma personalizable

ERC-4337 permite que las cuentas de usuario se comporten como contratos inteligentes sin modificar el protocolo base.

### Statelessness

Objetivo de reducir la necesidad de que los nodos mantengan todo el estado de la blockchain, permitiendo verificaciones parciales mediante técnicas como "Verkle Trees". Esto disminuiría drásticamente los requisitos de cómputo y almacenamiento para ejecutar nodos, mejorando la descentralización al hacer más accesible la participación en la red.

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
