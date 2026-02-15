# Roadmap y Visión de Ethereum

El desarrollo de Ethereum es un proceso continuo y orgánico que busca resolver los desafíos fundamentales de las cadenas de bloques: descentralización, seguridad y escalabilidad. Estos tres objetivos conforman lo que Vitalik Buterin formuló en 2017 como el [trilema de blockchain](https://vitalik.eth.limo/general/2021/04/07/sharding.html), donde históricamente optimizar una propiedad implicaba comprometer al menos otra. El 4 de enero de 2026, Buterin declaró que Ethereum ha [resuelto técnicamente este trilema](https://www.binance.com/es/square/post/34641989280370), señalando que los avances del roadmap finalmente permiten combinar las tres propiedades sin sacrificios estructurales, aunque persisten desafíos de distribución de poder y gobernanza.

En Ethereum, a diferencia de un producto de software tradicional con versiones lineales (v1.0, v2.0), el roadmap se estructura en líneas de investigación paralelas que convergen en actualizacione o forks concretas de la red.

Desde su lanzamiento en 2015, Ethereum ha evolucionado de ser una plataforma experimental para contratos inteligentes a convertirse en la infraestructura base para aplicaciones descentralizadas, finanzas descentralizadas (DeFi) y activos digitales. Sin embargo, esta adopción masiva reveló limitaciones técnicas significativas: costos de transacción prohibitivos durante períodos de alta demanda, tiempos de confirmación lentos y requisitos de almacenamiento que dificultaban la operación descentralizada de nodos.

Este documento analiza en detalle la estructura técnica del roadmap de Ethereum y expone la visión estratégica que guía su evolución, explicando cómo cada decisión de diseño responde a desafíos concretos que la comunidad ha enfrentado a lo largo del tiempo.

Para una comprensión completa de la arquitectura de Ethereum, se recomienda consultar el [Yellow Paper de Ethereum](https://ethereum.github.io/yellowpaper/paper.pdf), el documento técnico fundamental que especifica formalmente el protocolo.

Para profundizar en la hoja de ruta técnica oficial y seguir las actualizaciones más recientes, se recomienda consultar la [documentación de ethereum.org](https://ethereum.org/en/roadmap/) y el [blog de investigación de la Ethereum Foundation](https://blog.ethereum.org/).

## Las Líneas de Investigación

El [roadmap de Ethereum](https://ethereum.org/es/roadmap/) se organiza en seis líneas de investigación paralelas que llevan nombres simbólicos en inglés, utilizados universalmente por la comunidad y documentación oficial:

Estas líneas representan los objetivos a largo plazo del protocolo. No ocurren secuencialmente; se desarrollan en paralelo. Esta estructura refleja la naturaleza distribuida del desarrollo de Ethereum, donde múltiples equipos avanzan investigaciones complementarias que eventualmente se integran en actualizaciones coordinadas.

**The Merge**:

La Unión: Simboliza la fusión de dos cadenas (PoW y PoS) en una sola, unificando el mecanismo de consenso.

Enfocado en el mecanismo de consenso. Su hito principal fue la transición de Proof of Work (PoW) a Proof of Stake (PoS), completada en septiembre de 2022. Esta transición no solo redujo el consumo energético en un 99.95%, sino que también estableció las bases para mejoras futuras en escalabilidad. Bajo PoS, los validadores reemplazan a los mineros, bloqueando ETH como garantía económica en lugar de resolver puzzles computacionales intensivos. Este cambio fundamental permite la implementación de técnicas como el sharding, que serían incompatibles con PoW.

**The Surge**:

El Impulso: Representa la oleada masiva de escalabilidad que transformará el throughput de la red.

Centrado en la escalabilidad masiva. El objetivo es alcanzar más de 100.000 transacciones por segundo (TPS) utilizando estrategias como Rollups y Sharding. Para contextualizar esta meta: Ethereum procesa actualmente alrededor de 15-30 TPS en la L1, mientras que Visa maneja aproximadamente 1.700 TPS en promedio. Los Rollups son soluciones de L2 que ejecutan transacciones fuera de la cadena principal pero heredan su seguridad, agrupando cientos de transacciones en una única transacción L1. El Sharding, por su parte, divide la red en múltiples cadenas paralelas (shards) que procesan transacciones simultáneamente.

**The Verge**:

El Límite: Marca la frontera hacia la verificación ultra-ligera, el límite de lo técnicamente posible para que sea la red más descentralizada.

Busca facilitar la verificación de la red. La meta es que validar la cadena sea tan ligero computacionalmente que pueda realizarse desde un teléfono móvil o reloj inteligente. Actualmente, ejecutar un nodo completo de Ethereum requiere varios terabytes de almacenamiento y sincronización constante. Una de los soluciones, como los Verkle Trees, son estructuras de datos criptográficas que permiten probar la inclusión de datos con pruebas mucho más pequeñas que los Merkle Trees actuales, reduciendo los requisitos de almacenamiento y ancho de banda. Esta tecnología habilita la "verificación sin estado" (stateless verification), donde un nodo puede validar bloques sin almacenar el estado completo de la blockchain.

**The Scourge**:

El Azote: Denota la lucha contra el MEV, un "azote" que amenaza la descentralización económica.

Dedicado a la resistencia a la censura y la descentralización económica. Busca evitar que los validadores o los constructores de bloques acumulen demasiado poder mediante la extracción de MEV (Maximal Extractable Value). El MEV representa el beneficio que un validador puede obtener al reordenar, incluir o excluir transacciones dentro de un bloque. Por ejemplo, un validador podría detectar una operación de intercambio grande en un exchange descentralizado y ejecutar su propia operación justo antes (front-running) para beneficiarse del cambio de precio resultante. Esta práctica, aunque técnicamente posible, genera inequidad y puede incentivar la centralización del poder de validación.

**The Purge**:

La Purga: Describe la limpieza de datos históricos innecesarios que congestionan la red.

Enfocado en la limpieza y eficiencia del protocolo. Trata de eliminar datos históricos innecesarios para evitar que los requisitos de almacenamiento de los nodos crezcan indefinidamente. Con el tiempo, la blockchain de Ethereum acumula gigabytes de datos antiguos que la mayoría de las aplicaciones nunca consultan. The Purge propone mecanismos como la "expiración de historia" donde los nodos solo mantienen datos recientes (por ejemplo, del último año), mientras que los datos históricos se archivan en sistemas especializados accesibles para quienes los necesiten pero no requeridos para la operación normal de la red.

**The Splurge**:

El Derroche: Agrupa todas las demás mejoras "extras" que no encajan en las categorías anteriores.

Categoría para mejoras generales, la experiencia de usuario, mantenimiento y ajustes finos esenciales, como la optimización de la Ethereum Virtual Machine (EVM). Incluye investigación en nuevos opcodes, mejoras de rendimiento en la ejecución de contratos inteligentes y compatibilidad con tecnologías emergentes. Por ejemplo, se investiga cómo integrar primitivas criptográficas resistentes a computadoras cuánticas directamente en el protocolo, o cómo optimizar los costos de gas para operaciones específicas que actualmente resultan prohibitivamente caras.

## El Motor de la Innovación: Quiénes construyen el Roadmap

El roadmap de Ethereum no emerge de una autoridad central, sino de un ecosistema descentralizado de investigación donde múltiples actores con diferentes especializaciones colaboran hacia objetivos compartidos. En el centro de esta red se encuentra la [Ethereum Foundation](https://ethereum.foundation/) (EF), una organización sin ánimo de lucro que coordina e impulsa la investigación fundamental del protocolo, pero que opera bajo un modelo deliberadamente no jerárquico. La EF mantiene [grupos de investigación especializados](https://ethereum.org/community/research/) que publican sus hallazgos abiertamente para que cualquier equipo pueda implementarlos, criticarlos o mejorarlos.

Sin embargo, la EF no trabaja aislada. El desarrollo de Ethereum incluye contribuciones críticas de empresas como [ConsenSys](https://consensys.io/) (que mantiene clientes como Teku y Besu), [Paradigm](https://www.paradigm.xyz/) (que financia investigación en MEV y desarrolla Reth), equipos de L2s como [Offchain Labs](https://offchainlabs.com/) (Arbitrum) y [Optimism](https://www.optimism.io/) que presionan por mejoras en disponibilidad de datos, investigadores independientes que publican en [ethresear.ch](https://ethresear.ch/), y académicos de universidades como Stanford y MIT que validan formalmente los mecanismos propuestos. Este modelo distribuido asegura que ninguna entidad pueda capturar la dirección técnica del protocolo.

Cada una de las seis líneas de investigación del roadmap (The Merge, The Surge, The Verge, The Scourge, The Purge, The Splurge) avanza gracias a la especialización complementaria de estos grupos. A continuación se detalla cómo los principales equipos de investigación de la EF se mapean con las distintas categorías del roadmap, aunque es importante notar que muchos grupos contribuyen transversalmente a múltiples objetivos debido a la naturaleza interconectada de los desafíos técnicos:

**[Privacy & Scaling Explorations (PSE)](https://pse.dev/)**:

The Verge, The Surge.

Este laboratorio explora las fronteras de la criptografía aplicada con una misión dual: habilitar la verificación ultra-ligera de la red (The Verge) y potenciar la escalabilidad mediante técnicas avanzadas de privacidad (The Surge). Su trabajo en Zero-Knowledge Proofs (ZKPs) es fundamental para permitir que dispositivos con recursos limitados, como teléfonos móviles, verifiquen la validez de la blockchain sin descargar terabytes de datos. Técnicamente, esto se logra mediante circuitos criptográficos que comprimen la verificación del estado completo de Ethereum en pruebas de apenas kilobytes.

En el frente de escalabilidad, PSE investiga cómo los ZK-Rollups pueden procesar transacciones fuera de la L1 mientras generan pruebas matemáticas compactas que demuestran su validez. Además, desarrollan soluciones de privacidad como las *stealth addresses* (direcciones temporales que protegen la identidad del receptor) y sistemas de identidad descentralizada donde se puede demostrar atributos específicos, por ejemplo que eres mayor de edad o resides en cierto país, sin revelar tu identidad completa. Su trabajo se materializa en herramientas concretas: [zkEVM](https://www.pse.dev/projects/zkevm) para ejecutar contratos inteligentes con privacidad, [Semaphore](https://semaphore.pse.dev/) para votaciones anónimas verificables, y [TLSNotary](https://tlsnotary.org/) para demostrar datos de APIs web sin exponer credenciales.

**[Robust Incentives Group (RIG)](https://efdn.notion.site/Robust-Incentives-Group-RIG-Homepage-802339956f2745a5964d8461c5ccef02)**:

The Scourge, The Merge.

Se dedica a la teoría de juegos y el diseño de mecanismos económicos que alinean incentivos individuales con la seguridad colectiva. Su contribución a The Scourge es central: analizar cómo la extracción de MEV (Maximal Extractable Value) concentra poder económico y diseñar contramedidas como ePBS (enshrined Proposer-Builder Separation), que redistribuye esos beneficios entre todos los validadores en lugar de permitir que unos pocos se especialicen en arbitraje sofisticado.

Para The Merge, RIG fue fundamental en el diseño de la curva de emisión de recompensas de staking y las penalizaciones (slashing) que garantizan que atacar la red sea económicamente suicida. Modelan escenarios adversariales: ¿qué pasa si un grupo controla el 33% del stake? ¿Y el 51%? ¿Cuánto deberían perder económicamente para que la coordinación maliciosa sea irracional incluso con beneficios de MEV? Su trabajo combina matemáticas formales con simulaciones computacionales de comportamiento estratégico, produciendo modelos que predicen cómo actores racionales reaccionarán ante cambios en las reglas del protocolo.

**[Consensus R&D](https://github.com/ethereum/consensus-specs)**:

The Merge, The Surge.

Este equipo especifica el corazón del protocolo: cómo miles de nodos distribuidos globalmente convergen a un acuerdo sobre el estado de la blockchain sin autoridad central. Fueron los arquitectos principales de The Merge, diseñando el mecanismo completo de Proof of Stake que reemplazó a la minería. Esto incluyó definir cómo se seleccionan validadores pseudoaleatoriamente para proponer bloques, cómo se agregan las firmas de cientos de validadores en cada época mediante [BLS signature aggregation](https://datatracker.ietf.org/doc/html/draft-irtf-cfrg-bls-signature-04), y cómo se penaliza matemáticamente a validadores que intenten crear bifurcaciones maliciosas.

Para The Surge, Consensus R&D desarrolla el Data Availability Sampling (DAS) que permite escalar la red sin expulsar a validadores con hardware modesto. PeerDAS, implementado en Fusaka, es su solución para que cada nodo solo verifique muestras aleatorias pequeñas de los datos mientras se mantiene garantía criptográfica de disponibilidad total. Además, investigan mejoras como Single Slot Finality (SSF), que reduciría el tiempo de confirmación final de transacciones de ~15 minutos actuales a un único slot de 12 segundos, aproximando Ethereum a la experiencia de redes de pago tradicionales sin comprometer descentralización. Su trabajo se basa en adaptar décadas de investigación académica en consenso distribuido, particularmente teoremas como [CAP](https://groups.csail.mit.edu/tds/papers/Gilbert/Brewer2.pdf) y [FLP Impossibility](https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf), al contexto específico de blockchain pública económicamente incentivada.

**[Cryptography Research](https://crypto.ethereum.org/)**:

The Verge, The Purge, The Splurge.

Este grupo se enfoca en las matemáticas avanzadas que definen el futuro a largo plazo del protocolo. Su contribución clave para The Verge son los Verkle Trees, estructuras de datos criptográficas que reemplazan los Merkle Trees actuales. La diferencia técnica es significativa: mientras que demostrar que una cuenta existe en un Merkle Tree requiere una prueba de ~3KB (que crece logarítmicamente con el tamaño del estado), un Verkle Tree reduce esto a menos de 200 bytes mediante el uso de compromisos vectoriales basados en [KZG polynomial commitments](https://dankradfeist.de/ethereum/2020/06/16/kate-polynomial-commitments.html). Esta reducción es fundamental para habilitar "stateless clients" que validan bloques sin almacenar el estado completo de la blockchain.

Para The Purge, investigan mecanismos de expiración del estado que permitan archivar datos antiguos sin comprometer la verificabilidad histórica, reduciendo los requisitos de almacenamiento de nodos que actualmente superan los 1TB. En The Splurge, trabajan en seguridad post-cuántica, preparando la migración de ECDSA (el algoritmo de firmas actual vulnerable a computadoras cuánticas) a alternativas resistentes como [Dilithium](https://pq-crystals.org/dilithium/) o [SPHINCS+](https://sphincs.org/). Aunque las computadoras cuánticas prácticas están estimadas para dentro de 10-15 años, las transacciones firmadas hoy podrían ser vulnerables en el futuro mediante "ataques de cosecha" (harvest now, decrypt later), donde un adversario almacena datos cifrados esperando tecnología futura para romperlos. El equipo también desarrolla primitivas criptográficas optimizadas para la EVM, como operaciones nativas para curvas elípticas más eficientes que las actuales, reduciendo los costos de gas de operaciones criptográficas avanzadas usadas en ZK-Rollups y esquemas de privacidad.

## Las Actualizaciones (The Hard Forks)

Si las categorías anteriores son el "qué", los hard forks son el "cómo y cuándo". Son actualizaciones de software específicas que combinan avances de varias líneas de investigación. Utilizan nombres de ciudades (para la capa de ejecución) y estrellas (para la capa de consenso), una convención de nomenclatura que refleja la arquitectura dual de Ethereum post-Merge: la capa de ejecución gestiona transacciones y contratos inteligentes, mientras que la capa de consenso coordina a los validadores.

**The Merge (Septiembre 2022)**:

Transición Energética.

Combinación de Paris y Bellatrix. El hito histórico que completó la transición a Proof of Stake, eliminando la minería intensiva en energía. The Merge fue literalmente una fusión: la red principal (mainnet) PoW se unió con la Beacon Chain, una cadena PoS paralela que llevaba operando desde diciembre de 2020 para probar y asegurar el nuevo mecanismo de consenso. Técnicamente ocurrió en dos pasos: primero la actualización "Bellatrix" en la capa de consenso, y días después "Paris" en la capa de ejecución, que activó la fusión real. Este evento marcó el fin de siete años de desarrollo incremental y redujo las emisiones de carbono de Ethereum en un 99.95%."

> Este hito lo llaman "The Merge", luego ya empezaron a llamarlo como combinación de ciudades y estrellas.

**Shapella (Abril 2023)**:

Cumpliendo la Promesa. Cierre de The Merge.

Combinación de Shanghai y Capella. Fue el hito final de The Merge, permitiendo por primera vez el retiro del ETH estakeado. No se trataba de un error, sino de una medida de seguridad planificada: desde el lanzamiento de la Beacon Chain en 2020 (años antes de The Merge), el contrato de staking funcionó como un "viaje de ida" para asegurar la nueva red de consenso. Los validadores pioneros depositaron sus fondos sabiendo que quedarían bloqueados indefinidamente hasta que la transición fuera segura. Shapella cumplió finalmente esa promesa, habilitando la liquidez y completando el ciclo económico del Proof of Stake.

**Dencun (Marzo 2024)**:

Abaratando las L2. El inicio de The Surge (el impulso).

Combinación de Deneb y Cancun. Parte crucial de The Surge, introdujo el concepto de "blobs" de datos efímeros mediante el [EIP-4844 (Proto-Danksharding)](https://eips.ethereum.org/EIPS/eip-4844). Los blobs son espacios de datos temporales adjuntos a los bloques que expiran después de aproximadamente 18 días. Antes de Dencun, las redes L2 debían publicar todos sus datos de transacciones permanentemente en la L1, pagando altos costos de gas. Con los blobs, los costos de las L2 se redujeron hasta un 90%, haciendo que transacciones que antes costaban varios dólares ahora cuesten centavos. Los datos aún están disponibles el tiempo suficiente para que cualquiera pueda verificar la validez de las transacciones L2, pero no ocupan espacio permanente en la blockchain.

**Pectra (Mayo 2025)**:

Experiencia de Usuario y Consolidación. Avances en The Splurge (la experiencia de usuario), avance en The Verge (explorar límites de la red) y The Surge (escalabilidad / impulso).

Combinación de Prague y Electra, representa un avance fundamental en tres frentes complementarios que transforman tanto la experiencia de usuario como la economía de validación. El primer frente introduce [Account Abstraction](https://ethereum.org/en/roadmap/account-abstraction/) mediante el [EIP-7702](https://eips.ethereum.org/EIPS/eip-7702), permitiendo que las direcciones tradicionales (EOA) deleguen funcionalidades a contratos inteligentes sin migrar fondos. Esta capacidad es la base técnica que habilita la experiencia unificada o [Chain Abstraction](https://www.binance.com/en/academy/articles/what-is-chain-abstraction), donde los usuarios interactúan con múltiples redes sin gestionar manualmente las complejidades de cada una.

El segundo frente aborda la eficiencia operacional para validadores mediante el aumento del balance efectivo máximo. En lugar del límite histórico de 32 ETH por validador (que obligaba a operadores grandes a fragmentar su capital en cientos de instancias separadas), los stakers pueden ahora depositar hasta 2048 ETH en un único validador y recibir recompensas proporcionales sobre todo el balance, simplificando drásticamente la gestión institucional.
Sin embargo, esta mejora abre un debate económico crítico vinculado a The Scourge: con ~28% del ETH en staking y [Lido Finance](https://lido.fi/) (el protocolo de liquid staking dominante) controlando ~30% de ese total, existe riesgo de centralización de consenso y reducción de liquidez circulante. La comunidad técnica debate activamente ajustar la curva de emisión (reducir recompensas base o implementar techos de staking dinámicos) para equilibrar seguridad sin incentivar concentración excesiva en pocas entidades. Este debate, documentado en [Ethereum Magicians](https://ethereum-magicians.org/t/eip-reduce-eth-issuance-by-limiting-the-max-effective-balance-to-1-eth/18985) y [ethresear.ch](https://ethresear.ch/t/staking-equilibrium/20394), reconoce que la descentralización económica es tan vital como la técnica para la resiliencia del protocolo. Las métricas actuales pueden consultarse en [rated.network](https://www.rated.network/).

El tercer frente profundiza el trabajo iniciado en Dencun al expandir la capacidad de [blobs](https://www.nervos.org/knowledge-base/what_are_blobs_in_ethereum_(explainCKBot)): el objetivo por bloque aumenta de 3 blobs a 6 blobs, con un máximo técnico de 9 blobs. Esta expansión continúa presionando a la baja los costos de las L2, consolidando el modelo de escalabilidad modular donde la L1 proporciona seguridad y disponibilidad de datos mientras que las L2 ejecutan la computación intensiva.

**Fusaka (Diciembre 2025)**:

Descentralización a Escala. The Surge (escalabilidad avanzada) y The Verge (verificación ligera para nodos pequeños).

Fusión de Fulu y Osaka, implementada en diciembre de 2025, introdujo tres mejoras técnicas complementarias que simultáneamente expanden la capacidad de escalabilidad mientras reducen las barreras de entrada para operar nodos validadores.

La primera mejora, PeerDAS (Peer Data Availability Sampling), contribuye simultáneamente a The Surge y The Verge al resolver un problema crítico de escalabilidad sin excluir a operadores pequeños. Al expandir de 6 a 16+ blobs por bloque, descargar y verificar gigabytes completos de datos expulsaría a los validadores con hardware doméstico. PeerDAS permite que cada nodo tome muestras aleatorias pequeñas de los datos. Si suficientes nodos obtienen exitosamente sus muestras correspondientes, queda matemáticamente garantizada la disponibilidad total de los datos. Esto significa que un validador operando desde una laptop con conexión WiFi doméstica puede validar tan confiablemente como uno ejecutando en un servidor dedicado de alta capacidad, democratizando la participación en el consenso.

La segunda mejora, BPO Forks (Blob Parameter Only forks), proporciona agilidad operacional ante cambios en la demanda. Antes de Fusaka, ajustar la capacidad de blobs requería meses de coordinación para ejecutar un hard fork completo del protocolo. BPO habilita ajustes mediante actualizaciones ligeras que pueden implementarse en semanas. Funciona como un "dial de emergencia" que responde a demanda real sin necesidad de esperar el próximo upgrade mayor planificado.

La tercera mejora expande los límites de gas por bloque, aumentando de 45M a 60M de gas. Sin embargo, mantiene un tope de 16.7M de gas por transacción individual. Esta combinación previene ataques de denegación de servicio donde un único contrato malicioso monopolice los recursos computacionales del bloque, mientras proporciona más espacio general para el procesamiento de transacciones normales.

**Glamsterdam (2026+)**:.

Validación sin Privilegios. The Scourge (el azote).

Combinación de Glarus y Amsterdam. Mientras tú envías una transacción esperando que se ejecute al precio que viste en pantalla, hay actores con acceso privilegiado reordenando operaciones para extraer valor de tu intercambio antes de que se confirme. Este problema, conocido como MEV (Maximal Extractable Value), concentra beneficios en validadores técnicamente sofisticados que pueden permitirse infraestructura especializada. Glamsterdam ataca esta inequidad desde dos ángulos: redistribuyendo esos beneficios entre todos los validadores mediante [ePBS](https://eips.ethereum.org/EIPS/eip-7732), y reduciendo la carga computacional con BALs para que más personas puedan validar sin hardware costoso.

> ePBS (enshrined Proposer-Builder Separation) institucionaliza la separación de roles: unos construyen bloques optimizados compitiendo por ofrecer la mejor comisión, y los validadores regulares simplemente eligen cuál bloque incluir, recibiendo su parte sin necesitar conocimiento técnico avanzado. Las BALs (Block-level Access Lists) permiten declarar anticipadamente qué datos se necesitarán, evitando que los nodos desperdicien tiempo buscándolos en el momento crítico de validación. El resultado práctico: validar se vuelve más accesible económicamente y tus transacciones sufren menos arbitraje invisible.

## El Horizonte 2026-2030

Más allá de las actualizaciones formalmente especificadas, la comunidad técnica de Ethereum proyecta una evolución continua que transformaría la naturaleza fundamental de cómo opera la red. Esta visión no se basa en especulación, sino en líneas de investigación activas cuyos fundamentos matemáticos ya se están validando en entornos controlados. La trayectoria apunta hacia tres fases superpuestas que redefinen los límites de lo que una blockchain pública descentralizada puede lograr.

**2026: Procesamiento Paralelo y Eficiencia Extrema**:

El año 2026 marca la transición hacia el procesamiento masivamente paralelo de transacciones en la L1. Los límites de gas actuales, que se expandieron de 30M a 60M tras Fusaka, proyectan alcanzar rangos de 180M-200M gas por bloque hacia finales de año. Este salto cuantitativo solo es posible mediante innovaciones cualitativas: ePBS y BALs introducidos en Glamsterdam permiten que múltiples constructores de bloques trabajen simultaneamente en distintas secciones del estado, eliminando el cuello de botella histórico donde un único proponente secuencial procesaba todas las operaciones.

La segunda mitad de 2026 verá el despliegue gradual de nodos experimentales ZK-EVM en mainnet. Estos validadores pioneros no re-ejecutarán transacciones computacionalmente, sino que verificarán pruebas SNARKs (Succinct Non-interactive ARguments of Knowledge) que comprimen la corrección de miles de operaciones en evidencia criptográfica de kilobytes. Este es el primer paso hacia la validación sin estado a escala, donde el costo computacional de confirmar un bloque se desacopla de su contenido transaccional.

**2027-2029: Reestructuración del Estado y Maduración ZK**:

Durante este período se materializa The Purge y The Verge en su expresión más profunda: la expiración del estado (state expiry) y la migración completa a Verkle Trees. El problema de la "inflación de estado" amenaza la descentralización porque obliga a que los nodos almacenen terabytes de información histórica que raramente consultan. La solución técnica implica que los nodos solo mantengan estado reciente, por ejemplo del último año, mientras que datos antiguos se archivan mediante protocolos de almacenamiento distribuido accesibles bajo demanda pero no requeridos para operación normal.

Paralelamente, los datos de ejecución migran hacia formatos blob-like optimizados. Esta convergencia estructural entre cómo se almacenan transacciones de L1 y cómo se publican datos de L2 reduce duplicación técnica y simplifica el modelo mental del protocolo.

El re-tarifado de gas (repricing) ajusta los costos de operaciones EVM para reflejar hardware moderno: operaciones criptográficas avanzadas como verificación de firmas BLS o hashing Poseidon se abaratan significativamente al volverse nativas, mientras que operaciones de almacenamiento que inflan el estado se encarecen para desincentivar acumulación innecesaria.

Para 2029, se estima que entre 30-50% de los validadores operan en modo ZK, validando bloques mediante pruebas en lugar de re-ejecución. Esta coexistencia de métodos es intencional: mantiene redundancia durante la transición mientras la comunidad gana confianza empírica en la seguridad de los sistemas ZK en condiciones adversariales reales.

**2030 y Más Allá: La Computadora Mundial Descentralizada**:

La visión culminante proyecta que para 2030, la validación mediante ZK se convierte en el método predominante, desbloqueando capacidades antes fundamentalmente imposibles. Un teléfono móvil o smartwatch podría ejecutar un nodo validador ligero de Ethereum que verifica la corrección de toda la blockchain descargando menos de 100MB de datos y ejecutando verificaciones que toman segundos, no horas. Esta democratización radical de la validación invierte la tendencia histórica donde escalar significaba mayor concentración en operadores con infraestructura costosa.

El throughput del ecosistema asegurado por la L1 alcanza rangos superiores a 10.000 TPS sostenidas, un orden de magnitud mayor que los sistemas actuales, mientras mantiene tiempos de finalidad de 12 segundos (single slot finality). Este rendimiento no compite con blockchains centralizadas sacrificando descentralización, sino que la refuerza: al delegar la ejecución intensiva a las L2, la L1 se preserva como una capa ligera enfocada en seguridad y disponibilidad de datos. Esta especialización mantiene bajos los requisitos de hardware para los validadores, garantizando que la participación en el consenso permanezca al alcance de usuarios independientes.

Paralelamente, el ecosistema trabaja para integrar la privacidad como un servicio accesible y opcional. Aunque la transparencia total ha sido clave para la seguridad de Ethereum, también expone a los usuarios a riesgos financieros y de vigilancia. La visión a largo plazo no es ocultarlo todo, sino devolver el control al usuario: que los saldos y movimientos sean visibles solo si el dueño así lo desea, o solo para las partes involucradas, similar a cómo funciona el efectivo o las cuentas bancarias tradicionales pero en un entorno descentralizado. Hacia 2030, se espera que tecnologías avanzadas de criptografía (como las pruebas de conocimiento cero) maduren lo suficiente para permitir este "anonimato selectivo" de manera estándar en wallets y aplicaciones. Esto permitiría, por ejemplo, demostrar solvencia o realizar pagos sin revelar ante el mundo entero cuánto dinero tienes exactamente ni en qué lo gastaste ayer, conciliando finalmente la libertad financiera individual con la seguridad pública de la red.

Esta evolución de la L1 redefine fundamentalmente el rol de las L2s en el ecosistema. Cuando Ethereum alcance 10.000+ TPS con costos de centavos por transacción, la propuesta de valor histórica de las L2s (ofrecer escalabilidad que la L1 no puede proveer) o privacidad, se erosiona considerablemente. Vitalik Buterin ha señalado que las L2s necesitarán diferenciarse más allá de solo ser "Ethereum pero más barato", sugiriendo que necesitan un nuevo camino evolutivo. Las L2s que sobrevivan probablemente serán aquellas que se especialicen en nichos específicos: zkVMs que permiten ejecución privada de lógica compleja que la L1 no pueda ofrecer, cadenas optimizadas para gaming con latencias sub-segundo, entornos experimentales para features que aún no son seguras para L1 (como opcodes nuevos o modelos de gas alternativos), o ecosistemas verticalmente integrados con identidad y experiencia de usuario radicalmente simplificada. Las L2s genéricas que simplemente replican la funcionalidad de L1 enfrentarán presión competitiva creciente: cuando operar en L1 cuesta similar pero ofrece máxima seguridad y composabilidad nativa con todo el ecosistema DeFi, el incentivo para fragmentarse en una L2 disminuye drásticamente. Esta dinámica no elimina las L2s, pero las obliga a evolucionar de ser "soluciones de escalabilidad" a ser "plataformas de especialización".

Aunque esta visión se construye sobre los cimientos de la disponibilidad de datos y la gestión eficiente del estado, su culminación depende críticamente de que la tecnología ZK madure sin encontrar limitaciones fundamentales. La complejidad de los circuitos ZK para validar la EVM completa es inmensa: cada opcode, cada caso edge del protocolo debe expresarse como restricciones algebraicas verificables. Proyectos como PSE's zkEVM y esfuerzos comerciales de equipos como Scroll, Polygon zkEVM y zkSync están validando iterativamente que esta complejidad es manejable, pero el camino hacia producción a escala de consenso de Ethereum es progresivo y prudente, no abrupto.

## La Diversidad de Clientes como pilar de descentralización

Más allá de los grupos de investigación que diseñan el roadmap, existe un mecanismo de descentralización que opera en una capa diferente y que es fundamental para la resiliencia de Ethereum: la diversidad de implementaciones del protocolo. A diferencia de blockchains donde una única implementación de software domina la red, Ethereum opera bajo un modelo de pluralidad de clientes, donde múltiples equipos independientes implementan la especificación del protocolo en distintos lenguajes de programación y arquitecturas.
Esta arquitectura no es un lujo académico, es una defensa existencial contra fallas catastróficas. Cuando una única implementación controla más del 66% de los nodos, un bug en ese software puede detener la red completa o, peor aún, permitir un ataque de consenso donde nodos comprometidos finalicen bloques inválidos. La historia lo ha demostrado: el incidente de Merge de agosto de 2023, donde un bug en el cliente mayoritario Prysm causó una división temporal de la cadena, reveló las consecuencias de la concentración. Los nodos ejecutando Lighthouse, Teku y Nimbus continuaron operando correctamente, evitando una parada total. Si todos los nodos hubieran usado Prysm, la red habría quedado paralizada hasta un parche manual.

En la capa de ejecución (donde se procesan transacciones y se ejecutan contratos inteligentes), operan múltiples implementaciones producidas por equipos independientes: [Geth](https://geth.ethereum.org/) (Go Ethereum, implementación histórica en Go), [Nethermind](https://www.nethermind.io/) (C#, enfocada en rendimiento y casos enterprise), [Besu](https://www.hyperledger.org/projects/besu) (Java, bajo Hyperledger con énfasis en compliance), [Erigon](https://github.com/ledgerwatch/erigon) (Go, optimizada para eficiencia de almacenamiento) y [Reth](https://paradigmxyz.github.io/reth/) (Rust, nueva generación de alto rendimiento). En la capa de consenso (donde se coordina a los validadores de PoS), la diversidad es igualmente robusta: [Lighthouse](https://lighthouse.sigmaprime.io/) (Rust), [Prysm](https://prysmaticlabs.com/) (Go), [Teku](https://consensys.io/teku) (Java), [Nimbus](https://nimbus.team/) (Nim, diseñado para dispositivos de recursos limitados) y [Lodestar](https://lodestar.chainsafe.io/) (TypeScript/JavaScript).

Esta multiplicidad de equipos y lenguajes es lo que hace que el roadmap avance "lento pero seguro". Cada EIP (Ethereum Improvement Proposal) debe ser implementada independientemente por todos los equipos, probada en múltiples arquitecturas y verificada mediante testeos cruzados antes de activarse en mainnet. Cuando Dencun introdujo los blobs con EIP-4844, no fue simplemente escribir código nuevo, fue coordinar cinco equipos de ejecución y cinco de consenso para que sus implementaciones alcanzaran consenso bit-a-bit sobre el mismo comportamiento. Este proceso deliberadamente lento detecta bugs que una implementación única jamás encontraría: lo que funciona en Go podría fallar sutilmente en Rust, lo que pasa desapercibido en Java podría explotar en C#.

La gobernanza técnica de clientes opera mediante coordinación social y económica, no mediante autoridad central. Cuando un hard fork se aproxima, los equipos de clientes se sincronizan mediante llamadas públicas semanales ([All Core Devs](https://github.com/ethereum/pm/)), especificaciones compartidas en GitHub y testnets comunes donde se valida compatibilidad. Si un cliente mayoritario introduce un cambio incompatible, la comunidad de validadores puede simplemente no actualizar o migrar a clientes minoritarios, forzando correcciones sin necesidad de gobernanza formal. Este balance de poder distribuido es lo que garantiza que ningún equipo individual pueda capturar el protocolo.

Para comprender la importancia teórica de esta diversidad, consultar ["On the Importance of Client Diversity for Ethereum's Security"](https://mirror.xyz/jmcook.eth/S7ONEka_0RgtKTZ3-dakPmAHQNPvuj15nh0YGKPFriA) de Josh Csik. Para seguir las métricas actuales de distribución de clientes en la red, revisar [clientdiversity.org](https://clientdiversity.org/), sitio mantenido por la comunidad que monitorea en tiempo real qué porcentaje de nodos ejecuta cada implementación.

---
