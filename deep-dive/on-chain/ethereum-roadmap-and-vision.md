# Roadmap y Visión de Ethereum

El desarrollo de Ethereum es un proceso continuo y orgánico que busca resolver los desafíos fundamentales de las cadenas de bloques: descentralización, seguridad y escalabilidad. A diferencia de un producto de software tradicional con versiones lineales (v1.0, v2.0), el roadmap de Ethereum se estructura en líneas de investigación paralelas que convergen en actualizaciones concretas de la red.

Desde su lanzamiento en 2015, Ethereum ha evolucionado de ser una plataforma experimental para contratos inteligentes a convertirse en la infraestructura base para aplicaciones descentralizadas, finanzas descentralizadas (DeFi) y activos digitales. Sin embargo, esta adopción masiva reveló limitaciones técnicas significativas: costos de transacción prohibitivos durante períodos de alta demanda, tiempos de confirmación lentos y requisitos de almacenamiento que dificultaban la operación descentralizada de nodos.

Este documento explora la estructura técnica del roadmap actual de Ethereum y analiza la reciente evolución de la visión estratégica presentada por Vitalik Buterin respecto al rol de la Capa 1 (L1) y la Capa 2 (L2), contextualizando cómo estas decisiones de diseño responden a problemas reales que la comunidad ha enfrentado.

Para una comprensión completa de la arquitectura de Ethereum, se recomienda consultar el [Yellow Paper de Ethereum](https://ethereum.github.io/yellowpaper/paper.pdf), el documento técnico fundamental que especifica formalmente el protocolo.

Para profundizar en la hoja de ruta técnica oficial y seguir las actualizaciones más recientes, se recomienda consultar la [documentación de ethereum.org](https://ethereum.org/en/roadmap/) y el [blog de investigación de la Ethereum Foundation](https://blog.ethereum.org/).

## Estructura del Roadmap: Objetivos vs. Implementación

Para entender hacia dónde va Ethereum, es crucial distinguir entre las líneas de investigación conceptuales y los paquetes de actualización reales que se instalan en la red (Hard Forks).

### Las Líneas de Investigación

El [roadmap de Ethereum](https://ethereum.org/es/roadmap/) se organiza en seis líneas de investigación paralelas que llevan nombres simbólicos en inglés, utilizados universalmente por la comunidad y documentación oficial:

- **The Merge** (La Unión): Simboliza la fusión de dos cadenas (PoW y PoS) en una sola, unificando el mecanismo de consenso.
- **The Surge** (El Impulso): Representa la oleada masiva de escalabilidad que transformará el throughput de la red.
- **The Scourge** (El Azote): Denota la lucha contra el MEV, un "azote" que amenaza la descentralización económica.
- **The Verge** (El Límite): Marca la frontera hacia la verificación ultra-ligera, el límite de lo técnicamente posible.
- **The Purge** (La Purga): Describe la limpieza de datos históricos innecesarios que congestionan la red.
- **The Splurge** (El Derroche): Agrupa todas las demás mejoras "extras" que no encajan en las categorías anteriores.

Estas líneas representan los objetivos a largo plazo del protocolo. No ocurren secuencialmente; se desarrollan en paralelo como departamentos de ingeniería distintos trabajando simultáneamente. Esta estructura refleja la naturaleza distribuida del desarrollo de Ethereum, donde múltiples equipos avanzan investigaciones complementarias que eventualmente se integran en actualizaciones coordinadas.

**The Merge**:

Enfocado en el mecanismo de consenso. Su hito principal fue la transición de Proof of Work (PoW) a Proof of Stake (PoS), completada en septiembre de 2022. Esta transición no solo redujo el consumo energético en un 99.95%, sino que también estableció las bases para mejoras futuras en escalabilidad. Bajo PoS, los validadores reemplazan a los mineros, bloqueando ETH como garantía económica en lugar de resolver puzzles computacionales intensivos. Este cambio fundamental permite la implementación de técnicas como el sharding, que serían incompatibles con PoW.

Para comprender la teoría económica detrás de PoS, consultar el paper ["Casper the Friendly Finality Gadget"](https://arxiv.org/abs/1710.09437) de Buterin y Griffith. Documentación oficial sobre The Merge disponible en [ethereum.org/en/roadmap/merge](https://ethereum.org/en/roadmap/merge/).

**The Surge**:

Centrado en la escalabilidad masiva. El objetivo es alcanzar más de 100,000 transacciones por segundo (TPS) utilizando estrategias como Rollups y Sharding. Para contextualizar esta meta: Ethereum procesa actualmente alrededor de 15-30 TPS en la L1, mientras que Visa maneja aproximadamente 1,700 TPS en promedio. Los Rollups son soluciones de L2 que ejecutan transacciones fuera de la cadena principal pero heredan su seguridad, agrupando cientos de transacciones en una única transacción L1. El Sharding, por su parte, divide la red en múltiples cadenas paralelas (shards) que procesan transacciones simultáneamente.

Documentación oficial de The Surge en [ethereum.org/en/roadmap/scaling](https://ethereum.org/en/roadmap/scaling/). Para especificaciones técnicas de Danksharding, consultar la [propuesta de investigación](https://notes.ethereum.org/@dankrad/new_sharding) de Dankrad Feist.

**The Scourge**:

Dedicado a la resistencia a la censura y la descentralización económica. Busca evitar que los validadores o los constructores de bloques acumulen demasiado poder mediante la extracción de MEV (Maximal Extractable Value). El MEV representa el beneficio que un validador puede obtener al reordenar, incluir o excluir transacciones dentro de un bloque. Por ejemplo, un validador podría detectar una operación de intercambio grande en un exchange descentralizado y ejecutar su propia operación justo antes (front-running) para beneficiarse del cambio de precio resultante. Esta práctica, aunque técnicamente posible, genera inequidad y puede incentivar la centralización del poder de validación.

Para comprender MEV en profundidad, consultar ["Flash Boys 2.0: Frontrunning in Decentralized Exchanges"](https://arxiv.org/abs/1904.05234). Documentación de The Scourge y PBS disponible en [ethereum.org/en/roadmap/pbs](https://ethereum.org/en/roadmap/pbs/). El repositorio de investigación sobre PBS está en [ethereum/research](https://github.com/ethereum/research/tree/master/papers).

**The Verge**:

Busca facilitar la verificación de la red. La meta es que validar la cadena sea tan ligero computacionalmente que pueda realizarse desde un teléfono móvil o reloj inteligente. Actualmente, ejecutar un nodo completo de Ethereum requiere varios terabytes de almacenamiento y sincronización constante. Los Verkle Trees son estructuras de datos criptográficas que permiten probar la inclusión de datos con pruebas mucho más pequeñas que los Merkle Trees actuales, reduciendo los requisitos de almacenamiento y ancho de banda. Esta tecnología habilita la "verificación sin estado" (stateless verification), donde un nodo puede validar bloques sin almacenar el estado completo de la blockchain.

Especificación técnica de Verkle Trees en [EIP-6800](https://eips.ethereum.org/EIPS/eip-6800). Documentación oficial de The Verge en [ethereum.org/en/roadmap/verkle-trees](https://ethereum.org/en/roadmap/verkle-trees/). Para la teoría matemática detrás de Verkle Trees, consultar el paper ["Verkle Trees"](https://math.mit.edu/research/highschool/primes/materials/2018/Kuszmaul.pdf) de John Kuszmaul.

**The Purge**:

Enfocado en la limpieza y eficiencia del protocolo. Trata de eliminar datos históricos innecesarios para evitar que los requisitos de almacenamiento de los nodos crezcan indefinidamente. Con el tiempo, la blockchain de Ethereum acumula gigabytes de datos antiguos que la mayoría de las aplicaciones nunca consultan. The Purge propone mecanismos como la "expiración de historia" donde los nodos solo mantienen datos recientes (por ejemplo, del último año), mientras que los datos históricos se archivan en sistemas especializados accesibles para quienes los necesiten pero no requeridos para la operación normal de la red.

Propuesta de History Expiry en [EIP-4444](https://eips.ethereum.org/EIPS/eip-4444). Documentación de The Purge disponible en [ethereum.org/en/roadmap/statelessness](https://ethereum.org/en/roadmap/statelessness/). Para contexto sobre reducción del estado, ver el análisis de Vitalik sobre [State Expiry and Statelessness](https://notes.ethereum.org/@vbuterin/state_expiry_eip).

**The Splurge**:

Categoría para mejoras generales, mantenimiento y ajustes finos esenciales, como la optimización de la Ethereum Virtual Machine (EVM). Incluye investigación en nuevos opcodes, mejoras de rendimiento en la ejecución de contratos inteligentes y compatibilidad con tecnologías emergentes. Por ejemplo, se investiga cómo integrar primitivas criptográficas resistentes a computadoras cuánticas directamente en el protocolo, o cómo optimizar los costos de gas para operaciones específicas que actualmente resultan prohibitivamente caras.

Especificación de la EVM en el [Yellow Paper de Ethereum](https://ethereum.github.io/yellowpaper/paper.pdf). Propuestas de mejora a la EVM se rastrean en [EIPs oficiales](https://eips.ethereum.org/). Para investigación sobre criptografía post-cuántica, consultar [NIST Post-Quantum Cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography) y su relevancia para blockchain discutida en [ethresear.ch](https://ethresear.ch/t/post-quantum-security/8469).

### Las Actualizaciones (The Hard Forks)

Si las categorías anteriores son el "qué", los hard forks son el "cómo y cuándo". Son actualizaciones de software específicas que combinan avances de varias líneas de investigación. Utilizan nombres de ciudades (para la capa de ejecución) y estrellas (para la capa de consenso), una convención de nomenclatura que refleja la arquitectura dual de Ethereum post-Merge: la capa de ejecución gestiona transacciones y contratos inteligentes, mientras que la capa de consenso coordina a los validadores.

**The Merge (Septiembre 2022)**:

Transición Energética.

Paris. El hito histórico que completó la transición a Proof of Stake, eliminando la minería intensiva en energía. The Merge fue literalmente una fusión: la red principal (mainnet) PoW se unió con la Beacon Chain, una cadena PoS paralela que llevaba operando desde diciembre de 2020 para probar y asegurar el nuevo mecanismo de consenso. Técnicamente ocurrió en dos pasos: primero la actualización "Bellatrix" en la capa de consenso, y días después "Paris" en la capa de ejecución, que activó la fusión real. Este evento marcó el fin de siete años de desarrollo incremental y redujo las emisiones de carbono de Ethereum en un 99.95%."

**Shapella (Abril 2023)**:

Cumpliendo la Promesa.

Combinación de Shanghai y Capella. Fue el hito final de The Merge, permitiendo por primera vez el retiro del ETH estakeado. No se trataba de un error, sino de una medida de seguridad planificada: desde el lanzamiento de la Beacon Chain en 2020 (años antes de The Merge), el contrato de staking funcionó como un "viaje de ida" para asegurar la nueva red de consenso. Los validadores pioneros depositaron sus fondos sabiendo que quedarían bloqueados indefinidamente hasta que la transición fuera segura. Shapella cumplió finalmente esa promesa, habilitando la liquidez y completando el ciclo económico del Proof of Stake.

**Dencun (Marzo 2024)**:

Abaratando las L2.

Combinación de Deneb y Cancun. Parte crucial de The Surge, introdujo el concepto de "blobs" de datos efímeros mediante el [EIP-4844 (Proto-Danksharding)](https://eips.ethereum.org/EIPS/eip-4844). Los blobs son espacios de datos temporales adjuntos a los bloques que expiran después de aproximadamente 18 días. Antes de Dencun, las redes L2 debían publicar todos sus datos de transacciones permanentemente en la L1, pagando altos costos de gas. Con los blobs, los costos de las L2 se redujeron hasta un 90%, haciendo que transacciones que antes costaban varios dólares ahora cuesten centavos. Los datos aún están disponibles el tiempo suficiente para que cualquiera pueda verificar la validez de las transacciones L2, pero no ocupan espacio permanente en la blockchain.

**Pectra (Mayo 2025)**:

Experiencia de Usuario y Consolidación.

Combinación de Prague y Electra, representa un avance fundamental en tres frentes complementarios que transforman tanto la experiencia de usuario como la economía de validación. El primer frente introduce [Account Abstraction](https://ethereum.org/en/roadmap/account-abstraction/) mediante el [EIP-7702](https://eips.ethereum.org/EIPS/eip-7702), permitiendo que las direcciones tradicionales (EOA) deleguen funcionalidades a contratos inteligentes sin migrar fondos. Esta capacidad es la base técnica que habilita [Chain Abstraction](https://www.binance.com/en/academy/articles/what-is-chain-abstraction), donde los usuarios interactúan con múltiples redes sin gestionar manualmente las complejidades de cada una.

El segundo frente aborda la eficiencia operacional para validadores mediante el aumento del balance efectivo máximo. En lugar del límite histórico de 32 ETH por validador (que obligaba a operadores grandes a fragmentar su capital en cientos de instancias separadas), los stakers pueden ahora depositar hasta 2048 ETH en un único validador y recibir recompensas proporcionales sobre todo el balance, simplificando drásticamente la gestión institucional.

Sin embargo, esta mejora abre un debate económico crítico vinculado a The Scourge: con ~28% del ETH en staking y [Lido Finance](https://lido.fi/) (el protocolo de liquid staking dominante) controlando ~30% de ese total, existe riesgo de centralización de consenso y reducción de liquidez circulante. La comunidad técnica debate activamente ajustar la curva de emisión (reducir recompensas base o implementar techos de staking dinámicos) para equilibrar seguridad sin incentivar concentración excesiva en pocas entidades. Este debate, documentado en [Ethereum Magicians](https://ethereum-magicians.org/t/eip-reduce-eth-issuance-by-limiting-the-max-effective-balance-to-1-eth/18985) y [ethresear.ch](https://ethresear.ch/t/staking-equilibrium/20394), reconoce que la descentralización económica es tan vital como la técnica para la resiliencia del protocolo. Las métricas actuales pueden consultarse en [rated.network](https://www.rated.network/).

El tercer frente profundiza el trabajo iniciado en Dencun al expandir la capacidad de [blobs](https://www.nervos.org/knowledge-base/what_are_blobs_in_ethereum_(explainCKBot)): el objetivo por bloque aumenta de 3 blobs a 6 blobs, con un máximo técnico de 9 blobs. Esta expansión continúa presionando a la baja los costos de las L2, consolidando el modelo de escalabilidad modular donde la L1 proporciona seguridad y disponibilidad de datos mientras que las L2 ejecutan la computación intensiva.

**Fusaka (Diciembre 2025)**:

Descentralización a Escala.

Fusión de Fulu y Osaka. Introduce tres mejoras técnicas para escalar blobs sin comprometer descentralización:

PeerDAS (Peer Data Availability Sampling): Cuando escales de 6 a 16+ blobs por bloque, descargar gigabytes completos expulsaría validadores caseros. Con PeerDAS, cada nodo toma muestras aleatorias pequeñas. Si suficientes nodos obtienen sus muestras exitosamente, matemáticamente se garantiza disponibilidad total. Tu laptop con WiFi doméstica valida tan confiablemente como un servidor dedicado.

BPO Forks (Blob Parameter Only forks): Antes de Fusaka, ajustar capacidad de blobs ante picos de demanda requería meses coordinando un hard fork completo. BPO habilita ajustes mediante actualizaciones ligeras que toman semanas. Es un "dial de emergencia" que responde a demanda real sin esperar el próximo upgrade mayor.

Expansión de gas limits: El límite por bloque crece de 45M a 60M de gas, pero con tope de 16.7M por transacción individual. Esto previene ataques DoS donde un contrato monopoliza recursos mientras da más espacio general para transacciones normales.

**Glamsterdam (2026+)**:.

Validación sin Privilegios.

Combinación de Glarus y Amsterdam. Mientras tú envías una transacción esperando que se ejecute al precio que viste en pantalla, hay actores con acceso privilegiado reordenando operaciones para extraer valor de tu intercambio antes de que se confirme. Este problema, conocido como MEV (Maximal Extractable Value), concentra beneficios en validadores técnicamente sofisticados que pueden permitirse infraestructura especializada. Glamsterdam ataca esta inequidad desde dos ángulos: redistribuyendo esos beneficios entre todos los validadores mediante ePBS, y reduciendo la carga computacional con BALs para que más personas puedan validar sin hardware costoso.

ePBS (enshrined Proposer-Builder Separation) institucionaliza la separación de roles: unos construyen bloques optimizados compitiendo por ofrecer la mejor comisión, y los validadores regulares simplemente eligen cuál bloque incluir, recibiendo su parte sin necesitar conocimiento técnico avanzado. Las BALs (Block-level Access Lists) permiten declarar anticipadamente qué datos se necesitarán, evitando que los nodos desperdicien tiempo buscándolos en el momento crítico de validación. El resultado práctico: validar se vuelve más accesible económicamente y tus transacciones sufren menos arbitraje invisible.

## El Motor de la Innovación: Quiénes Construyen el Roadmap

El roadmap no avanza por inercia, sino gracias al trabajo coordinado de [grupos de investigación especializados dentro de la Ethereum Foundation y la comunidad extendida](https://ethereum.org/community/research/). Este modelo de gobernanza técnica distribuida, donde múltiples equipos independientes contribuyen a un objetivo común, es una característica distintiva de Ethereum que contrasta con blockchains más centralizadas. Cada grupo tiene un enfoque que alimenta las distintas categorías:

**[Privacy & Scaling Explorations (PSE)](<https://pse.dev/)>)**:

Este laboratorio explora las fronteras de la Criptografía Programable con una misión clara: hacer que la privacidad y la escalabilidad sean compatibles en una red pública. Su trabajo busca resolver paradojas cotidianas mediante matemáticas avanzadas: ¿cómo demostrar que tienes derecho a entrar a un lugar sin revelar tu identidad? ¿Cómo verificar que un cálculo es correcto sin ver los datos privados que lo generaron? En la práctica, esto se traduce en herramientas para **Identidad Digital** (como demostrar que eres un humano único basándose en un pasaporte real, pero sin revelar tus datos personales), **Votación Privada** (donde se cuenta el voto pero se protege matemáticamente al votante) y mecanismos de privacidad financiera (conceptualmente similares a las *stealth addresses*). A nivel de red, investigan cómo "comprimir" la verificación de la blockchain para que dispositivos cotidianos, como un teléfono móvil, puedan validar la seguridad de la red sin descargar terabytes de información. Su enfoque va más allá de ocultar datos; se trata de permitir la verificación pública sin comprometer la privacidad individual.

**[Robust Incentives Group (RIG)](https://efdn.notion.site/Robust-Incentives-Group-RIG-Homepage-802339956f2745a5964d8461c5ccef02)**:

Se encarga de la teoría de juegos y la economía del protocolo. Su trabajo es crítico para The Scourge, diseñando mecanismos que alineen los incentivos individuales con el bienestar colectivo de la red. Por ejemplo, RIG analiza escenarios donde un validador podría obtener mayor ganancia comportándose maliciosamente (como censurando transacciones específicas a cambio de sobornos) y diseña penalizaciones económicas (slashing) que hacen que tales comportamientos sean financieramente irracionales. También investigan dinámicas de coalición: ¿qué pasa si grupos de validadores coordinan para extraer MEV conjuntamente? ¿Cómo asegurar que incluso con coordinación, el sistema permanezca resistente a la censura?

**[Consensus R&D](https://github.com/ethereum/consensus-specs)**:

Centrados en el corazón del protocolo, especifican cómo los nodos se ponen de acuerdo sobre el estado de la blockchain. Son los arquitectos principales detrás de The Merge y The Surge (incluyendo PeerDAS), asegurando que la base de la red pueda escalar sin comprometer la finalidad o la seguridad. Este equipo debe resolver problemas fundamentales de sistemas distribuidos: ¿cómo garantizar que todos los nodos honestos eventualmente converjan al mismo estado incluso con nodos maliciosos o fallidos en la red? ¿Cómo minimizar la latencia de confirmación sin sacrificar garantías de seguridad? Su trabajo se basa en décadas de investigación académica en consenso distribuido, adaptando teoremas clásicos como el de [CAP](https://groups.csail.mit.edu/tds/papers/Gilbert/Brewer2.pdf) y el [FLP Impossibility Theorem](https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf) al contexto específico de blockchain.

**[Cryptography Research](https://crypto.ethereum.org/)**:

Dedican sus esfuerzos a las matemáticas avanzadas necesarias para el futuro, como los Verkle Trees para clientes ligeros y la seguridad post-cuántica. Los Verkle Trees combinan árboles de Merkle con compromisos vectoriales, reduciendo el tamaño de las pruebas de aproximadamente 3KB (en Merkle Trees) a menos de 200 bytes. Esto es crucial porque cada nodo debe transmitir y verificar estas pruebas constantemente. Respecto a seguridad post-cuántica, aunque las computadoras cuánticas aún no amenazan Ethereum hoy, se estima que en 10-15 años podrían romper los algoritmos criptográficos actuales (como ECDSA usado para firmas). El equipo investiga la migración gradual a algoritmos resistentes a ataques cuánticos, asegurando que Ethereum permanezca seguro en el futuro a largo plazo.

### La Diversidad de Clientes como Pilar de Descentralización

Más allá de los grupos de investigación que diseñan el roadmap, existe un mecanismo de descentralización que opera en una capa diferente y que es fundamental para la resiliencia de Ethereum: la diversidad de implementaciones del protocolo. A diferencia de blockchains donde una única implementación de software domina la red, Ethereum opera bajo un modelo de pluralidad de clientes, donde múltiples equipos independientes implementan la especificación del protocolo en distintos lenguajes de programación y arquitecturas.

Esta arquitectura no es un lujo académico, es una defensa existencial contra fallas catastróficas. Cuando una única implementación controla más del 66% de los nodos, un bug en ese software puede detener la red completa o, peor aún, permitir un ataque de consenso donde nodos comprometidos finalicen bloques inválidos. La historia lo ha demostrado: el incidente de Merge de agosto de 2023, donde un bug en el cliente mayoritario Prysm causó una división temporal de la cadena, reveló las consecuencias de la concentración. Los nodos ejecutando Lighthouse, Teku y Nimbus continuaron operando correctamente, evitando una parada total. Si todos los nodos hubieran usado Prysm, la red habría quedado paralizada hasta un parche manual.

En la capa de ejecución (donde se procesan transacciones y se ejecutan contratos inteligentes), operan múltiples implementaciones producidas por equipos independientes: [Geth](https://geth.ethereum.org/) (Go Ethereum, implementación histórica en Go), [Nethermind](https://www.nethermind.io/) (C#, enfocada en rendimiento y casos enterprise), [Besu](https://www.hyperledger.org/projects/besu) (Java, bajo Hyperledger con énfasis en compliance), [Erigon](https://github.com/ledgerwatch/erigon) (Go, optimizada para eficiencia de almacenamiento) y [Reth](https://paradigmxyz.github.io/reth/) (Rust, nueva generación de alto rendimiento). En la capa de consenso (donde se coordina a los validadores de PoS), la diversidad es igualmente robusta: [Lighthouse](https://lighthouse.sigmaprime.io/) (Rust), [Prysm](https://prysmaticlabs.com/) (Go), [Teku](https://consensys.io/teku) (Java), [Nimbus](https://nimbus.team/) (Nim, diseñado para dispositivos de recursos limitados) y [Lodestar](https://lodestar.chainsafe.io/) (TypeScript/JavaScript).

Esta multiplicidad de equipos y lenguajes es lo que hace que el roadmap avance "lento pero seguro". Cada EIP (Ethereum Improvement Proposal) debe ser implementada independientemente por todos los equipos, probada en múltiples arquitecturas y verificada mediante testeos cruzados antes de activarse en mainnet. Cuando Dencun introdujo los blobs con EIP-4844, no fue simplemente escribir código nuevo, fue coordinar cinco equipos de ejecución y cinco de consenso para que sus implementaciones alcanzaran consenso bit-a-bit sobre el mismo comportamiento. Este proceso deliberadamente lento detecta bugs que una implementación única jamás encontraría: lo que funciona en Go podría fallar sutilmente en Rust, lo que pasa desapercibido en Java podría explotar en C#.

La gobernanza técnica de clientes opera mediante coordinación social y económica, no mediante autoridad central. Cuando un hard fork se aproxima, los equipos de clientes se sincronizan mediante llamadas públicas semanales ([All Core Devs](https://github.com/ethereum/pm/)), especificaciones compartidas en GitHub y testnets comunes donde se valida compatibilidad. Si un cliente mayoritario introduce un cambio incompatible, la comunidad de validadores puede simplemente no actualizar o migrar a clientes minoritarios, forzando correcciones sin necesidad de gobernanza formal. Este balance de poder distribuido es lo que garantiza que ningún equipo individual pueda capturar el protocolo.

Para comprender la importancia teórica de esta diversidad, consultar ["On the Importance of Client Diversity for Ethereum's Security"](https://mirror.xyz/jmcook.eth/S7ONEka_0RgtKTZ3-dakPmAHQNPvuj15nh0YGKPFriA) de Josh Csik. Para seguir las métricas actuales de distribución de clientes en la red, revisar [clientdiversity.org](https://clientdiversity.org/), sitio mantenido por la comunidad que monitorea en tiempo real qué porcentaje de nodos ejecuta cada implementación.


---
