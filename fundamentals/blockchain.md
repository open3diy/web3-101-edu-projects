
# Blockchain

## ¿Qué es una blockchain?

Una blockchain es una cadena lineal y cronológicamente ordenada de bloques que funciona como un libro mayor distribuido e inmutable. Cada bloque contiene un conjunto de transacciones validadas y está enlazado criptográficamente al bloque anterior mediante funciones hash, formando una estructura de datos que garantiza la integridad histórica de la información registrada.

El concepto fue introducido por primera vez en el [whitepaper de Bitcoin](https://bitcoin.org/bitcoin.pdf) de Satoshi Nakamoto en 2008, donde se propuso como la estructura de datos fundamental para mantener un registro de transacciones sin necesidad de una autoridad central. Desde entonces, la tecnología ha evolucionado más allá de las criptomonedas, encontrando aplicaciones en contratos inteligentes, trazabilidad de activos, gestión de identidad digital y sistemas de gobernanza descentralizada.

Esta tecnología representa un modelo de base de datos descentralizada donde la seguridad criptoeconómica se logra mediante protocolos de consenso que permiten a múltiples participantes acordar el estado del sistema sin confiar en una entidad central. Las características fundamentales que proporciona son privacidad selectiva, transparencia verificable y auditabilidad completa del histórico de transacciones.

## Distributed Ledger Technology (DLT)

Es importante distinguir que blockchain es una implementación específica dentro de un concepto más amplio conocido como [Distributed Ledger Technology (DLT)](https://research.ibm.com/projects/privacy-preserving-and-interoperable-digital-assets). Mientras que todas las blockchains son DLTs, no todas las DLTs utilizan bloques encadenados.

Existen otras implementaciones de DLT que emplean estructuras de datos alternativas:

**Tangle (IOTA):**

El protocolo [Tangle](https://www.iota.org/) utiliza un grafo acíclico dirigido (DAG) en lugar de bloques lineales. En este sistema, cada nueva transacción debe validar dos transacciones anteriores, creando una red de validaciones interconectadas. Este diseño elimina la necesidad de mineros y teóricamente mejora la escalabilidad, ya que el throughput aumenta con el número de transacciones.

**Hashgraph:**

[Hashgraph](https://hedera.com/learning/hashgraph/what-is-hashgraph) emplea un algoritmo de consenso basado en "gossip about gossip" y "virtual voting". Las transacciones se estructuran en un DAG donde los nodos comparten información sobre el orden de los eventos, logrando consenso sin necesidad de bloques tradicionales. Este mecanismo promete alta eficiencia y rapidez en la confirmación de transacciones.

**Holochain:**

[Holochain](https://www.holochain.org/) adopta un enfoque radicalmente diferente: no utiliza bloques ni busca consenso global. Cada agente mantiene su propia cadena de datos y las interacciones se gestionan de forma descentralizada mediante validación por pares. Este diseño se enfoca en la autonomía de los nodos y la escalabilidad horizontal.

## Distribución versus descentralización

Los términos "distributed" y "decentralized" frecuentemente se confunden, pero representan conceptos distintos que es crucial diferenciar en el contexto de blockchain y sistemas distribuidos.

**Sistema distribuido:**

Se refiere a que los datos o procesos están replicados en múltiples ubicaciones geográficas o lógicas. Un sistema puede ser distribuido pero mantener control centralizado, como ocurre con los servidores replicados de una empresa que operan en diferentes regiones para mejorar la disponibilidad y el rendimiento, pero donde una única organización mantiene el control total sobre la infraestructura.

**Sistema descentralizado:**

Implica que no existe una autoridad central que controle completamente el sistema. Las decisiones, el control y la gobernanza están distribuidos entre múltiples participantes que operan de forma autónoma. La descentralización fomenta la resistencia a la censura y reduce los puntos únicos de fallo tanto técnicos como de gobernanza.

Ethereum con su diseño de sharding ilustra bien esta distinción. Es un sistema tanto distribuido como descentralizado, pero con matices importantes. La carga de datos y procesamiento se distribuye entre los nodos y, con [sharding](https://ethereum.org/en/roadmap/danksharding/), cada shard procesa un subconjunto de transacciones aumentando la escalabilidad. Sin embargo, la gobernanza y la seguridad se mantienen descentralizadas mediante la Beacon Chain, donde los validadores se distribuyen entre shards y participan en el consenso global.

Es crucial entender que el término DLT se refiere a un libro mayor distribuido, pero no implica necesariamente descentralización completa. Una DLT puede ser centralizada, descentralizada o semi-centralizada, dependiendo de su diseño y modelo de gobernanza. El enfoque de distribución se centra en la ubicación física de los datos entre nodos, mientras que la descentralización aborda quién controla y toma decisiones sobre el sistema. Blockchain, en su concepción original, está diseñada principalmente para sistemas descentralizados, aunque existen implementaciones permisionadas con diferentes grados de centralización.

## Tipos de blockchain según permisos

Las blockchains se pueden clasificar según el modelo de acceso y permisos que implementan, determinando quién puede participar en el consenso y acceder a los datos:

**Blockchain pública:**

Cualquier persona puede unirse a la red, participar en el proceso de consenso y leer todas las transacciones. Bitcoin y Ethereum son ejemplos prominentes. La seguridad se basa en incentivos criptoeconómicos y la transparencia total. Son ideales para casos de uso que requieren máxima descentralización y resistencia a la censura.

**Blockchain privada:**

El acceso está restringido a participantes autorizados por una entidad u organización. Típicamente empleadas por empresas que necesitan las propiedades de inmutabilidad y trazabilidad de blockchain, pero requieren control sobre quién puede participar. [Hyperledger Fabric](https://www.hyperledger.org/use/fabric) es un framework común para implementar blockchains privadas.

**Blockchain consorcio:**

Un modelo híbrido donde un grupo predefinido de organizaciones controla el proceso de consenso. Combina elementos de descentralización con requisitos de gobernanza específicos. Útil para industrias donde múltiples entidades necesitan colaborar manteniendo cierto control, como en cadenas de suministro o consorcios bancarios.

## Forks y evolución de la blockchain

Durante la operación de una blockchain, pueden surgir situaciones donde la cadena se bifurca, creando caminos alternativos. Comprender estos escenarios es fundamental para entender la evolución y gobernanza de redes blockchain.

**Fork nativo:**

Ocurre temporalmente cuando dos mineros encuentran bloques válidos casi simultáneamente, creando dos versiones competidoras de la cadena. La mayoría de los nodos eventualmente convergen hacia una de las cadenas siguiendo las reglas del protocolo de consenso, típicamente la cadena más larga o la que representa más trabajo acumulado.

**Cadena huérfana (orphaned chain):**

Es la cadena alternativa que termina siendo abandonada cuando la red alcanza consenso sobre cuál es la cadena válida. Los bloques en la cadena huérfana, aunque válidos, no forman parte del histórico principal y sus transacciones deben ser reincluidas en bloques posteriores de la cadena principal.

**Soft fork:**

Una actualización del protocolo que es retrocompatible. Los nodos que no actualicen su software pueden seguir validando transacciones, aunque no podrán aprovechar las nuevas características. Un ejemplo significativo es [SegWit (Segregated Witness)](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki) en Bitcoin, que optimizó el uso del espacio en bloques sin requerir que todos los nodos actualizaran simultáneamente.

**Hard fork:**

Representa un cambio significativo en las reglas del protocolo que rompe la compatibilidad con versiones anteriores. Los nodos deben actualizar su software para continuar participando en la red actualizada. Si parte de la comunidad no acepta los cambios, puede resultar en dos blockchains separadas que comparten historia hasta el punto de bifurcación. Ejemplos notables son [Bitcoin Cash](https://bitcoincash.org/) (fork de Bitcoin) y [Ethereum Classic](https://ethereumclassic.org/) (fork de Ethereum tras el incidente de The DAO).

## Regla de la cadena canónica

Un principio fundamental en blockchain es la determinación de cuál es la cadena válida cuando existen múltiples versiones. La regla general es que la cadena con mayor "peso" es considerada la cadena canónica.

En Bitcoin, el peso se calcula según el trabajo computacional acumulado (Proof of Work), siguiendo la regla de la cadena más larga en términos de dificultad acumulada, no simplemente el número de bloques. Los mineros invierten recursos computacionales para resolver puzzles criptográficos, y la cadena que representa más trabajo acumulado se considera la válida.

En Ethereum post-merge, el peso viene determinado por el stake acumulado respaldando una cadena particular. Los validadores depositan ETH como garantía y participan en el consenso mediante [Proof of Stake](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/). La cadena respaldada por más stake y que sigue las reglas del protocolo Gasper (combinación de Casper FFG y LMD GHOST) se considera canónica.

Este mecanismo de selección de cadena es crucial para la seguridad y funcionalidad de la red, proporcionando una forma objetiva de resolver disputas sobre el estado del sistema sin requerir coordinación centralizada.

## Escalabilidad y sidechains

A medida que las blockchains principales enfrentan limitaciones de escalabilidad, han surgido diversas soluciones para procesar más transacciones sin comprometer la descentralización o seguridad.

**Sidechains:**

Son blockchains independientes que se conectan a la blockchain principal mediante un puente bidireccional, permitiendo transferir activos entre ambas cadenas. Las sidechains pueden implementar reglas de consenso diferentes, optimizadas para casos de uso específicos, mientras aprovechan la seguridad de la cadena principal para el asentamiento final de transacciones. Ejemplos incluyen [Polygon](https://polygon.technology/) (anteriormente Matic Network) para Ethereum.

**Layer 2:**

Son protocolos construidos sobre la blockchain principal que procesan transacciones fuera de la cadena principal (off-chain) pero heredan sus garantías de seguridad. Tecnologías como [Lightning Network](https://lightning.network/) para Bitcoin y [Optimistic Rollups](https://ethereum.org/en/developers/docs/scaling/optimistic-rollups/) o [ZK-Rollups](https://ethereum.org/en/developers/docs/scaling/zk-rollups/) para Ethereum permiten throughput significativamente mayor mientras mantienen la finalidad en la blockchain base.

**Sharding:**

Particiona la blockchain en múltiples fragmentos (shards) que procesan transacciones en paralelo. Cada shard mantiene un subconjunto del estado global, y los validadores rotan entre shards para garantizar seguridad. Ethereum está implementando sharding como parte de su roadmap de escalabilidad, coordinado por la Beacon Chain.

Estas soluciones representan diferentes compromisos en el trilema blockchain de escalabilidad, seguridad y descentralización, buscando optimizar el rendimiento sin sacrificar las propiedades fundamentales que hacen valiosa la tecnología blockchain.

---
