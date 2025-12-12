# Ecosistema Web3: Protocolos

Un protocolo es el mecanismo que te indica cómo puedes participar, qué tienes que hacer para poder interactuar con la infraestructura abierta de Web3.

Pero en Web3, un protocolo no es simplemente un documento de especificaciones ni un conjunto abstracto de reglas, en la práctica se implementan en los componentes fundamentales de la infraestructura básica, como los smart contracto, que operan sin necesidad de permisos, cuando los inicias se ejecutan de forma automática, siguiendo reglas predefinidas.

En Web3, los nodos de una red pueden entenderse desde múltiples dimensiones. Desde una perspectiva técnica, estos nodos son redes de ordenadores o servidores, donde los protocolos desempeñan un papel indispensable. Por ejemplo, los protocolos de consenso como PoW (Proof of Work), PoS (Proof of Stake) y PoA (Proof of Authority) son fundamentales para alcanzar acuerdos en la red. Además, existen protocolos específicos para oráculos, capas base (layer 0), y otros componentes críticos. Estas reglas técnicas son esenciales para garantizar que los sistemas funcionen de manera coherente y segura, y son ampliamente conocidas y aplicadas por los ingenieros que construyen la infraestructura de Web3.

En Web3, una red no solo está compuesta por nodos técnicos como ordenadores o servidores, sino también por redes de individuos. Así como existen redes sociales, en Web3 también se forman redes humanas que alcanzan acuerdos y consensos. Estas redes operan bajo protocolos diferentes, adaptados a la interacción humana, donde la economía juega un papel crucial. Por ejemplo, se pueden crear DAOs (Organizaciones Autónomas Descentralizadas) guiadas por smart contracts que siguen un protocolo definido. Igualmente, suele haber un protocolo informal o "invisible" de comunicación, que puede incluir discusiones en plataformas como X (anteriormente Twitter), coordinación en Discord, acuerdos preliminares off-chain mediante Snapshot, y finalmente votaciones on-chain. Este proceso ilustra cómo las redes humanas y técnicas se entrelazan en el ecosistema Web3, guiadas tanto por protocolos explícitos como por acuerdos implícitos o de facto.

Existen protocolos diseñados para emprendedores que buscan lanzar soluciones Web3. En la fase inicial, un fundador puede iniciar una ICO (Initial Coin Offering), optar por un launchpad en plataformas especializadas que además ofrecen pools de liquidez mediante IDOs (Initial DEX Offerings), seguir protocolos de lanzamiento justo como Fair Launch, o incluso coordinar equipos y obtener financiación a través de plataformas como Gitcoin. Pero una vez lanzado el proyecto, entran en juego otros protocolos fundamentales: los protocolos de incentivos y construcción de comunidad. Aquí es donde se definen las tokenomics (distribución de tokens, vesting, burning, staking), protocolos de recompensas (airdrops, liquidity mining, yield farming), programas de embajadores, sistemas de retroalimentación cuadrática para asignación de recursos, o mecanismos de gobernanza progresiva que van descentralizando el control del proyecto. Cada capa representa un protocolo diferente, adaptado tanto al momento del proyecto como a las necesidades de alineación entre fundadores, inversores y comunidad.

Igualmente, en el diseño de una DApp que tiene unos fundadores, que sigue un modelo de negocio, existen protocolos que ayudan a cubrir los casos de uso necesarios, que serían en realidad patrones de diseño, normas aceptadas que se implementan en smart contracts. Por ejemplo, especificaciones como ERC-20 para tokens fungibles, ERC-721 para NFTs, ERC-4824 (DAO URI) para metadatos de DAOs o Governor de OpenZeppelin para gobernanza on-chain. También están los protocolos de identidad descentralizada como DID (Decentralized Identifiers), Verifiable Credentials, ENS (Ethereum Name Service) para nombres legibles, o Soulbound Tokens (SBT) para identidad no transferible. Y protocolos para reputación como POAP (Proof of Attendance Protocol), Gitcoin Passport, o mecanismos de resolución de conflictos como Kleros o Aragon Court.

Como vemos, el poder del protocolo es fundamental en Web3: es lo que le da la propiedad de la composabilidad, la capacidad de componer como piezas de Lego sistemas complejos que interactúan entre ellos.

A diferencia de los protocolos Web2, como HTTP (estándares que implementas en tu servidor), los protocolos Web3 son infraestructura pública activa que tiene un modelo económico detrás. Por ejemplo, Uniswap no es solo una especificación de cómo hacer un DEX, sino un conjunto de contratos inteligentes desplegados que procesan miles de millones de dólares diariamente y que cualquier desarrollador puede invocar directamente.

Insistimos porque esta distinción es fundamental: los protocolos Web3 son las **piezas base del ordenador mundial descentralizado**, componentes autónomos y verificables que se combinan para crear aplicaciones complejas, que tienen la propiedad de **composabilidad permissionless**. Un desarrollador puede construir una aplicación DeFi que use Uniswap para intercambios, Aave para préstamos, Chainlink para precios, Safe para custodia multi-firma, ENS para identidad y Aragon para gobernanza, integrando contratos inteligentes de terceros sin APIs propietarias, sin negociaciones comerciales, y sin que nadie pueda revocarle el acceso.

Yearn Finance ejemplifica esta composabilidad: no creó pools de liquidez propios, sino que mediante smart contacts orquesta Aave, Compound y Curve para mover capital automáticamente hacia los mejores rendimientos. NFTfi combina ERC-721 (NFTs), ERC-20 (tokens), oráculos de precio y pools DeFi para crear mercados de colaterales NFT que no existían antes. Una DAO puede custodiar fondos en Safe, votar con Snapshot y usar ENS para identificar miembros: tres protocolos independientes interoperando sin intermediarios. Account Abstraction permite que un usuario pague gas con USDC en lugar de ETH gracias a que su wallet delega el pago a un Paymaster, eliminando la fricción de tener saldo en la moneda nativa de la red.

Esta capacidad de combinar protocolos sin permisos equivale a cómo HTTP, TCP/IP, DNS y TLS se apilan para formar internet. Pero mientras internet estandarizó protocolos técnicos neutros, Web3 añade protocolos de coordinación económica y social: mecanismos de consenso que acuerdan la verdad, tokenomics que distribuyen valor, gobernanza que descentraliza decisiones, e incentivos que alinean comportamientos.

La relevancia de un protocolo en Web3 no se mide por documentos técnicos en repositorios académicos, sino por su capitalización de mercado en CoinMarketCap, CoinGecko y plataformas similares. Estos sitios no son meras herramientas para especuladores: son de facto el inventario valorado del ordenador mundial descentralizado. Cada activo o token listado representa un componente del ecosistema, y su capitalización refleja la confianza del mercado en su utilidad, adopción y sostenibilidad. Uniswap con $5B de capitalización no es una apuesta financiera abstracta; es la valoración de mercado del protocolo de intercambio descentralizado más usado del mundo, comparable a cómo se valoraría la infraestructura crítica de AWS o Cloudflare. En Web3, tokenomics no es accesorio del diseño técnico, es el mecanismo que alinea incentivos, distribuye ownership, financia desarrollo y captura valor creado. **Un protocolo sin modelo económico viable es código sin sostenibilidad**.

Este documento no pretende ser un catálogo técnico exhaustivo de estándares (sería interminable y obsoleto en meses), sino una taxonomía donde los protocolos resuelven problemas fundamentales.

Cada sección representa una categoría de protocolos que te emplazará a otro documento.

Conocer este panorama acelera desarrollo (compones protocolos battle-tested en lugar de reinventar), mejora interoperabilidad (tu aplicación funciona con el resto del ecosistema), reduce riesgos (protocolos auditados y usados por millones son más seguros que código propietario), y desbloquea modelos de negocio (entender lanzamientos, gobernanza y tokenomics es crítico para sostenibilidad). Los mejores protocolos no nacen de comités ISO, sino de builders experimentando con soluciones a problemas reales y compartiendo aprendizajes.

No todos los protocolos actuales sobrevivirán. Muchos experimentos fallarán, algunos estándares serán reemplazados por mejores alternativas, y nuevas categorías de protocolos emergerán para resolver problemas que aún no anticipamos. Esta incertidumbre no debe paralizarte; al contrario, representa una oportunidad para contribuir a definir cómo funcionará la próxima generación de internet.

## Protocolos de infraestructura

Los protocolos de infraestructura operan en las capas más bajas del stack tecnológico de Web3, definiendo cómo funciona la red subyacente. Incluyen mecanismos de consenso (PoW, PoS, PoA), almacenamiento descentralizado (IPFS, Arweave, Filecoin), redes P2P, bridges cross-chain para interoperabilidad entre blockchains, oráculos como Chainlink para conectar datos externos, protocolos de escalabilidad (rollups, sidechains, state channels), y soluciones de disponibilidad de datos.

Aunque estos protocolos son fundamentales para el funcionamiento de Web3, para el emprendedor o desarrollador de DApps la interacción directa con ellos suele ser limitada. La decisión más relevante es elegir la red en la que operarás (Ethereum, Optimism, Arbitrum, Polygon, Base, etc.), ya que cada una ofrece diferentes trade-offs en términos de costos, velocidad, seguridad y ecosistema de herramientas.

Comprender a profundidad todos los protocolos de infraestructura no solo es impracticable, sino innecesario para la mayoría de casos de uso. Sin embargo, conocer sus fundamentos te ayudará a tomar mejores decisiones arquitectónicas y a entender las limitaciones y capacidades de la plataforma elegida.

Te emplazo a leer el artículo sobre [ecosistema de infraestructura](6-1-web3-ecosystem-infrastructure.md) para una visión panorámica del tema. Para análisis más profundos, consulta el [apartado de infraestructura](../infrastructure/about.md) donde se documentan los principales componentes técnicos.

Recuerda que este repositorio educativo se complementa con [web3-101](https://github.com/open3diy/web3-101), que ofrece un enfoque más práctico mediante laboratorios hands-on, y con [web3-101-dapp-playground](https://github.com/open3diy/web3-101-dapp-playground), un entorno de experimentación para desarrollar DApps.

## Protocolos de tokens

Los protocolos de tokens son fundamentales para entender cómo se crean, gestionan e intercambian los activos digitales en el ecosistema Web3. Estos protocolos definen estándares que garantizan interoperabilidad, seguridad y funcionalidad en las aplicaciones descentralizadas.

Por ejemplo, los estándares ERC-20 para tokens fungibles y ERC-721 para tokens no fungibles (NFTs) han sido pilares en la creación de economías digitales. Además, existen protocolos más avanzados como ERC-1155, que permite la gestión de tokens fungibles y no fungibles en un solo contrato, o ERC-4626, diseñado para tokens de bóvedas de rendimiento.

Estos estándares no solo facilitan la creación de tokens, sino que también habilitan casos de uso como la gobernanza, la representación de activos físicos o digitales, y la implementación de incentivos económicos. Por ejemplo, los Soulbound Tokens (SBT) representan identidades no transferibles, mientras que los POAP (Proof of Attendance Protocol) se utilizan para registrar eventos o logros.

Te emplazo a leer el artículo creado al respecto sobre la [taxonomía de criptoactivos](6-3-web3-ecosystem-DeFI.md) para explorar más a fondo cómo los protocolos de tokens están transformando la economía digital.

## Protocolos DeFi (Finanzas Descentralizadas)

Las Finanzas Descentralizadas (DeFi) representan una de las aplicaciones más transformadoras de la tecnología blockchain, al replicar y mejorar servicios financieros tradicionales sin necesidad de intermediarios centralizados.

Sus protocolos son fundamentales: desde una perspectiva, definen cómo funciona el mercado; desde otra, indican cómo participar, ya sea como inversor o como emisor de un token para iniciar un proyecto.

Te emplazo a leer el artículo creado al respecto sobre el [ecosistema DeFi](6-3-web3-ecosystem-DeFI.md).

## Protocolos de gobernanza descentralizada (DAO)

Las Organizaciones Autónomas Descentralizadas (DAO) representan el modelo fundamental para la gobernanza de proyectos y protocolos en Web3, permitiendo la toma de decisiones colectiva sin jerarquías centralizadas.

Te emplazo a leer el artículo creado al respecto sobre [DAO](7-3-DAO.md).

## Protocolos de identidad, reputación y resolución de conflictos

La identidad descentralizada, la construcción de reputación verificable y los mecanismos para resolver disputas sin intermediarios centralizados son componentes críticos para la madurez del ecosistema Web3.

Te emplazo a leer los artículos creados al respecto sobre [identidad](7-1-identity-web3.md), [reputación](7-2-web3-reputation.md) y [resolución de conflictos](7-4-conflict-resolution.md).

## Protocolos de roles y control de acceso

Los protocolos de roles y control de acceso definen quién puede ejecutar qué acciones en smart contracts, DAOs y protocolos DeFi. A diferencia de sistemas centralizados donde un administrador controla permisos desde una base de datos, en Web3 el control de acceso es inmutable, verificable on-chain y auditable públicamente.

El patrón más utilizado es Role-Based Access Control (RBAC) mediante OpenZeppelin AccessControl, donde se asignan roles específicos (ADMIN, MINTER, PAUSER) a direcciones autorizadas. Pero el ecosistema incluye soluciones más sofisticadas: multi-signature wallets como Safe para custodia compartida, timelock controllers que introducen delays para transparencia, Access Control Lists granulares, y capability-based security donde NFTs otorgan permisos transferibles.

Estos protocolos no son abstractos: cada exploit mayor en DeFi (DAO hack, Ronin bridge, Poly Network) involucró fallos en control de acceso. La diferencia entre un protocolo robusto y uno explotado suele estar en la correcta implementación de estos mecanismos.

Te emplazo a leer el artículo creado al respecto sobre [Protocolos de roles y control de acceso](7-5-roles-access-control.md).

## Protocolos de experiencia de usuario

La experiencia de usuario en Web3 representa la asignatura pendiente más crítica del ecosistema. La introducción de conceptos complejos, los tiempos de acceso, la espera para confirmar transacciones y las dudas razonables sobre privacidad son barreras que limitan la adopción masiva. No se trata solo de diseñar interfaces visualmente impactantes, sino de hacer Web3 accesible: introducir conceptos de forma progresiva, ofrecer contenido en idiomas nativos de la audiencia, y explicar no solo para que tú lo entiendas, sino para que puedas comunicarlo a otros.

Se suele hablar de mejoras mediante Account Abstraction (AA) o gestión optimizada del gas, pero la experiencia de usuario debe ser integral: desde el primer acceso hasta la conversión de valor Web3 a moneda fiat para gastar en el mundo real. Todos estos aspectos y sus protocolos asociados son fundamentales y representan un área de estudio crítica para cualquier builder comprometido con la adopción.

Te emplazo a leer la introducción del apartado creado al respecto sobre [Experiencia del usuario](./9-user-experience.md).

## Protocolos de lanzamiento, financiación y crecimiento

Los mecanismos de lanzamiento de tokens, financiación inicial y estrategias de crecimiento determinan cómo los proyectos Web3 recaudan capital, distribuyen ownership inicial y alinean incentivos entre fundadores, inversores y comunidad. Estos protocolos son críticos para el éxito temprano y la adopción sostenible.

Te emplazo a leer la introducción del apartado creado al respecto sobre [Visión inicial de lanzamiento, financiación y crecimiento de un proyecto](../launch-funding-and-growth/launch-funding-and-growth-overview.md).

## Protocolos de aplicaciones: patrones de diseño en smart contracts

Los protocolos no solo operan en las capas de infraestructura, finanzas o gobernanza. También existen a nivel de aplicación, donde se materializan como patrones de diseño recurrentes implementados en smart contracts para resolver casos de uso específicos.

Cuando diseñas una DApp, no partes de cero: heredas décadas de aprendizajes colectivos del ecosistema. Patrones como upgradeable contracts (proxies), pausable tokens, access control mediante roles, vesting schedules, merkle airdrops, o staking mechanisms son soluciones battle-tested que puedes componer directamente. OpenZeppelin, por ejemplo, no es solo una librería de código seguro, sino un repositorio de protocolos de aplicación documentados y auditados.

Comprender estos patrones acelera desarrollo, reduce vulnerabilidades (muchos exploits nacen de reinventar lógica crítica), y mejora composabilidad (tu DApp se integra mejor con otras si sigue convenciones conocidas). Pero la teoría sin práctica es incompleta: necesitas experimentar, deployar, debuggear y romper contratos para interiorizar cómo funcionan realmente.

Por eso te emplazo a trabajar con [web3-101-dapp-playground](https://github.com/open3diy/web3-101-dapp-playground), el entorno de experimentación diseñado para desarrollar DApps. Ahí encontrarás implementaciones reales de estos protocolos de aplicación, ejemplos de composabilidad, y ejercicios prácticos que consolidan lo aprendido en este documento.

Recuerda: los mejores protocolos emergen de builders resolviendo problemas reales, no de especificaciones abstractas.

---
