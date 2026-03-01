# Servicios Web3: as-a-Service

En el ecosistema Web3, muchas funcionalidades clave están disponibles como servicios bajo modelo SaaS, facilitando la integración rápida y eficiente de capacidades avanzadas sin necesidad de desarrollar toda la infraestructura desde cero. Estos servicios permiten a los equipos enfocarse en la lógica de negocio y la experiencia de usuario, delegando aspectos técnicos complejos a proveedores especializados.

Por supuesto, la desventaja general de utilizar servicios as-a-Service en Web3 es la reducción de la resiliencia y la introducción de un punto único de falla. Además, este enfoque no es el más descentralizado, ya que limita la capacidad de abrir el control del proyecto a una DAO o a la comunidad.

A veces se habla de “SaaS descentralizados”, pero en realidad se trata de servicios centralizados que actúan como capas de abstracción sobre protocolos descentralizados. Funcionan como un “atajo” para mejorar la usabilidad, pero no son verdaderamente descentralizados: siguen siendo servicios gestionados por un único proveedor y, por tanto, representan un único punto de acceso.

A continuación, se presenta una lista de categorías de servicios Web3 as-a-Service que pueden ser utilizados para acelerar el desarrollo de un MVP:

## [blockchain-as‑a‑Service (BaaS)](https://ciberseguridad.com/guias/recursos/blockchain-as-a-service-baas/)

Esta categoría se refiere a los proveedores que ofrecen una plataforma gestionada para construir, alojar y operar aplicaciones y soluciones blockchain en la nube. En lugar de que una empresa cree, configure y mantenga su propia infraestructura de blockchain desde cero, puede utilizar un proveedor de BaaS para externalizar toda la gestión de la infraestructura. Estos servicios se encargan del aprovisionamiento de nodos, la gestión de la red y la seguridad, permitiendo a los equipos centrarse en el desarrollo de sus aplicaciones.

**Ventajas**:

- Reducción de complejidad y costes: Elimina la necesidad de tener experiencia interna en infraestructura blockchain, seguridad y mantenimiento de redes.
- Despliegue rápido: Permite a las empresas lanzar aplicaciones blockchain (dApps) o redes privadas/permisionadas en mucho menos tiempo.
- Enfoque en el negocio: Los equipos pueden centrarse en la lógica de la aplicación y la experiencia de usuario en lugar de en la infraestructura subyacente.
- Escalabilidad gestionada: Los proveedores ofrecen infraestructura optimizada que puede escalar según la demanda del proyecto.

**Desventajas**:

- Centralización: La infraestructura depende de un único proveedor, lo que introduce un punto de fallo y va en contra del principio de descentralización.
- Menor control y personalización: Las opciones de configuración, los tipos de blockchain y las herramientas están limitadas a lo que ofrece el proveedor.
- Dependencia del proveedor (Vendor lock-in): Migrar de un proveedor de BaaS a otro o a una infraestructura propia puede ser extremadamente complejo y costoso.

**Ejemplos**:

- [Kaleido](https://www.kaleido.io/): Una plataforma BaaS que ofrece herramientas para construir y ejecutar soluciones blockchain empresariales en redes públicas y privadas.
- [Amazon Managed Blockchain](https://aws.amazon.com/managed-blockchain/): El servicio de AWS para crear y gestionar redes blockchain escalables utilizando frameworks populares como Hyperledger Fabric y Ethereum.
- [ConsenSys Quorum](https://consensys.io/quorum): Ofrece una suite de herramientas para construir y gestionar redes Ethereum permisionadas para casos de uso empresariales.

**Cuándo usar**:

Perfecto para empresas y consorcios que necesitan desarrollar aplicaciones en una red blockchain privada o permisionada, sin invertir en la creación y mantenimiento de la infraestructura. Ideal para pruebas de concepto (PoCs), cadenas de suministro o sistemas que requieren control de acceso y gobernanza centralizada.

## [Node-as‑a‑Service (NaaS)](https://www.alchemy.com/overviews/ethereum-node-as-a-service)

Esta categoría agrupa a los proveedores que ofrecen acceso a nodos blockchain como un servicio gestionado. En vez de operar tus propios nodos, depender de soluciones como Infura o Alchemy, o construir sistemas de indexación desde cero, estas plataformas proporcionan acceso a APIs, paneles de control y herramientas que simplifican enormemente el desarrollo y la integración con distintas blockchains.

**Ventajas**:

- Robusto: Utilizan infraestructura optimizada y de alta disponibilidad, garantizando que tu aplicación sea estable y escalable.
- Rápido: Permiten a los desarrolladores centrarse en la lógica de la aplicación y la experiencia de usuario, en lugar de en la gestión de la infraestructura subyacente.
- Sin gestionar infraestructura: Eliminan la necesidad de mantener nodos, sincronizarlos y asegurar su correcto funcionamiento, lo que ahorra tiempo y recursos significativos.

**Desventajas**:

- Límites de UX/lógica: Aunque son muy potentes, las APIs y herramientas pueden tener ciertas limitaciones que restrinjan la personalización de la experiencia de usuario o la implementación de lógicas de negocio muy específicas.

**Ejemplos**:

- [Alchemy](https://www.alchemy.com/): Es una de las plataformas de infraestructura Web3 líderes. Proporciona acceso a nodos súper rápidos y fiables, APIs para obtener datos de la blockchain (como historiales de transacciones o balances) y herramientas de monitorización.
- [QuickNode](https://www.quicknode.com/): Similar to Alchemy, QuickNode offers fast and reliable access to blockchain nodes for over 20 different chains. They provide a powerful API, analytics tools, and a marketplace for add-ons.
- [Tatum](https://tatum.io/): Es una plataforma que acelera el desarrollo de aplicaciones blockchain con una API unificada para más de 40 protocolos. Ofrece funcionalidades no-code para la creación de NFTs y tokens.

**Cuándo usar**:

Esencial para cualquier dApp que necesite interactuar con una blockchain. Si tu aplicación necesita leer datos de la red, enviar transacciones o escuchar eventos, un NaaS es la forma más rápida y fiable de hacerlo sin gestionar tu propia infraestructura de nodos.

## [Indexer-as-a-Service](https://thegraph.com/docs/en/about/)

Las blockchains son bases de datos muy ineficientes para realizar consultas complejas. Obtener datos como "todos los NFTs que posee una dirección" o "el historial de transacciones de un usuario con un contrato específico" puede ser extremadamente lento y difícil si se hace directamente contra un nodo. Los servicios de indexación resuelven este problema procesando los datos de la blockchain y organizándolos en bases de datos optimizadas a las que se puede acceder a través de una API (generalmente GraphQL).

Aunque a veces no se clasifican estrictamente como *as-a-Service* porque existen protocolos descentralizados para ello, en la práctica muchos desarrolladores consumen estos recursos a través de proveedores gestionados (como la versión alojada de The Graph o las APIs de datos de Alchemy) para evitar operar sus propios indexadores. Son recursos fundamentales para DApps que necesitan recuperar datos históricos de forma eficiente.

**Ventajas**:

- Consultas rápidas y eficientes: Permiten a las dApps obtener datos complejos de la blockchain casi instantáneamente.
- Ahorro de infraestructura: Evita la necesidad de construir y mantener un costoso sistema de indexación propio.
- Facilidad de uso: Proporcionan APIs sencillas que abstraen la complejidad de la estructura de datos de la blockchain.

**Desventajas**:

- Centralización (en algunos casos): Aunque el protocolo puede ser descentralizado, a menudo las dApps dependen de un punto de acceso (endpoint) alojado por un proveedor, lo que introduce un punto de centralización.
- Retraso en la sincronización: Los datos indexados pueden tener un pequeño retraso con respecto al estado más reciente de la blockchain.

**Ejemplos**:

- [The Graph](https://thegraph.com/): Es el protocolo de indexación descentralizado líder en el ecosistema Web3. Permite a cualquiera crear y publicar APIs abiertas, llamadas "subgraphs", que las aplicaciones pueden consultar con GraphQL.
- [Alchemy NFT API](https://www.alchemy.com/nft-api): Como parte de su suite de productos, Alchemy ofrece APIs especializadas y de alto rendimiento para obtener todo tipo de datos relacionados con NFTs, eliminando la necesidad de un indexador propio para este caso de uso.
- [Covalent](https://www.covalenthq.com/): Proporciona una API unificada para acceder a datos de miles de millones de transacciones en docenas de blockchains, incluyendo balances de tokens, transacciones históricas y datos de NFTs.

**Cuándo usar**:

Es una pieza de infraestructura esencial para casi cualquier dApp que necesite mostrar datos de la blockchain en su interfaz de usuario. Sin un servicio de indexación, la mayoría de las dApps serían inutilizables por su lentitud.

## [DAO-as-a-Service (DAOaaS)](https://medium.com/@DAOaaS/how-does-daoaas-rebuild-daos-0d8592c47617)

Estas plataformas ofrecen un conjunto de herramientas "todo en uno" para crear, gestionar y gobernar Organizaciones Autónomas Descentralizadas (DAOs) sin necesidad de escribir código desde cero. Abstraen la complejidad de los contratos de gobernanza, votación y tesorería.

**Ventajas**:

- Lanzamiento rápido de DAOs: Permiten desplegar una DAO funcional en minutos.
- Gobernanza estandarizada: Utilizan modelos de gobernanza probados y seguros.
- Interfaz de usuario incluida: Ofrecen un panel de control para que los miembros de la DAO puedan crear propuestas y votar.

**Desventajas**:

- Poca personalización: La estructura de la DAO y los mecanismos de votación están limitados a las plantillas que ofrece la plataforma.
- Dependencia de la plataforma: La gestión de la DAO está ligada a la interfaz y la infraestructura del proveedor.

**Ejemplos**:

- [Aragon](https://aragon.org/): Es la plataforma pionera y más conocida. Permite lanzar DAOs altamente configurables con un sistema de aplicaciones modulares (finanzas, votaciones, etc.).
- [Syndicate](https://syndicate.io/): Se enfoca en la creación de clubes de inversión y DAOs de forma sencilla, integrando herramientas para la gestión de tesorerías y la distribución de tokens.
- [Snapshot](https://snapshot.org/): Aunque no es una plataforma de creación de DAOs de "extremo a extremo", es la herramienta de facto para la votación "off-chain" (sin coste de gas), utilizada por la gran mayoría de las DAOs para la toma de decisiones.

**Cuándo usar**:

Ideal para comunidades que quieren organizarse y tomar decisiones de forma descentralizada sin la complejidad técnica de desarrollar un sistema de gobernanza propio. Perfecto para colectivos, grupos de inversión o proyectos que necesitan una estructura de gobernanza formal rápidamente.

## [Wallet-as-a-Service (WaaS)](https://www.wepin.io/en/blog/how-global-blockchain-services-leverage-waas-wallets)

Estos servicios proporcionan la infraestructura para crear y gestionar carteras de criptomonedas para los usuarios finales, a menudo a través de SDKs que se integran en una aplicación. El objetivo principal es abstraer la complejidad de la gestión de claves privadas y frases semilla, permitiendo experiencias de usuario similares a las de la Web2 (por ejemplo, inicio de sesión con correo electrónico o redes sociales).

**Ventajas**:

- Mejora radical de la UX: Elimina la principal barrera de entrada para los usuarios novatos al no requerirles que gestionen frases semilla.
- Onboarding sin fricción: Permite a los usuarios empezar a usar una dApp con métodos de autenticación familiares.
- Seguridad gestionada: Pueden utilizar técnicas como la [computación multipartita (MPC)](https://www.coinbase.com/es-es/learn/wallet/what-is-a-multi-party-computation-mpc-wallet) o [carteras de contratos inteligentes](https://oneroyal.academy/es/faqs/smart-contract-wallet-guidance/) para securizar las claves sin que el usuario tenga que custodiarlas directamente.

**Desventajas**:

- Centralización operativa: Aunque la cartera sigue siendo técnicamente “no custodial”, el proveedor controla uno de los *shares* y participa en todas las firmas, introduciendo un punto de confianza y un posible punto de fallo.

- Menor soberanía del usuario: El usuario no gestiona una clave privada completa, sino un *share*, lo que reduce el nivel de control comparado con una cartera tradicional basada en una clave EOA íntegra.

- Dependencia del proveedor: La operativa de la cartera (firmas, recuperación, políticas) depende de la disponibilidad del servicio WaaS. Si el proveedor deja de operar o tiene una interrupción, la cartera puede quedar temporal o permanentemente inutilizable, salvo mecanismos explícitos de exportación/portabilidad de *shares*.

**Ejemplos**:

**Ejemplos (WaaS reales)**:

- [Privy](https://www.privy.io/): Wallets embebidas con onboarding por email/redes sociales y opción de exportación a autocustodia.
- [Magic](https://magic.link/): Wallets sin contraseña integrables en cualquier app mediante enlaces por email y métodos Web2.
- [Web3Auth](https://web3auth.io/): Infraestructura modular para crear wallets seedless con login social y control flexible de claves.
- [Alchemy](https://www.alchemy.com/): Plataforma para crear smart wallets directamente desde tu backend o frontend, con APIs de firma y relayers.
- [Particle Network](https://particle.network/): Wallets embebidas con login social, MPC y compatibilidad multi-chain.
- [Thirdweb Wallet](https://thirdweb.com): SDK para integrar wallets y smart accounts con gasless, relayers y recuperación integrada.
- [Safe](https://safe.global/): Proporciona la infraestructura para crear y gestionar "Safes" (anteriormente Gnosis Safes), que son monederos multi-firma programables. Es el estándar de facto para la gestión de tesorerías de DAOs y proyectos.

**Cuándo usar**:

Si el objetivo es que la experiencia de usuario sea indistinguible de una aplicación Web2, un WaaS es la solución correcta.

## [Identity-as-a-Service (IDaaS)](https://www.cloudflare.com/es-es/learning/access-management/what-is-identity-as-a-service/)

Estos servicios se centran en la gestión de la identidad digital descentralizada. Permiten a los usuarios controlar sus propios datos y a las aplicaciones verificar atributos o credenciales (como la edad, la nacionalidad o la posesión de un título) sin necesidad de almacenar información personal sensible. Se basan en estándares como los Identificadores Descentralizados (DIDs) y las Credenciales Verificables (VCs).

**Ventajas**:

- Soberanía del usuario: El usuario tiene el control total sobre su identidad y quién puede acceder a sus datos.
- Privacidad: Permite la verificación selectiva de atributos sin revelar toda la identidad.
- Interoperabilidad: Una identidad descentralizada puede ser utilizada en múltiples aplicaciones y plataformas.

**Desventajas**:

- Ecosistema emergente: La adopción y la estandarización todavía están en desarrollo.
- Complejidad de la recuperación: La recuperación de una identidad perdida puede ser más compleja que en los sistemas centralizados.

**Ejemplos**:

- [SpruceID](https://www.spruceid.com/): Ofrece un conjunto de herramientas para que los desarrolladores integren DIDs y VCs en sus aplicaciones, permitiendo, por ejemplo, el inicio de sesión con Ethereum (SIWE).
- [Ceramic Network](https://ceramic.network/): Es una red de datos descentralizada para gestionar contenido dinámico y mutable, a menudo utilizada para construir perfiles de usuario descentralizados y sistemas de reputación.
- [Worldcoin](https://world.org/): Aunque controvertido, es un ejemplo de identidad como servicio que busca proporcionar una "prueba de humanidad" a través de la verificación biométrica, creando un identificador único por persona.

**Cuándo usar**:

Cuando una aplicación necesita verificar la identidad o los atributos de un usuario de una manera que respete la privacidad, o cuando se quiere construir un sistema de reputación o perfiles de usuario portátiles.

## [Messaging-as-a-Service (MaaS)](https://www.meetri.in/products/message-as-a-service.html)

Estos protocolos y servicios proporcionan la infraestructura para la comunicación segura y encriptada entre direcciones de blockchain (wallets). La idea de una capa de comunicación nativa para Web3 no es nueva; el whitepaper original de Ethereum ya contemplaba un protocolo llamado **Whisper**, diseñado para la comunicación P2P anónima. Sin embargo, Whisper enfrentó desafíos de escalabilidad que dificultaron su adopción. Como sucesor, surgió **Waku**, un protocolo modular que busca resolver estos problemas, ofreciendo un equilibrio entre privacidad, resistencia a la censura y eficiencia.

Los servicios MaaS modernos, como XMTP, se basan en estos principios para ofrecer a los desarrolladores SDKs y APIs que facilitan la integración de funcionalidades de chat, notificaciones o bandejas de entrada directamente en sus dApps, sin tener que gestionar la complejidad de la red P2P subyacente.

**Ventajas**:

- Resistencia a la censura: La comunicación no depende de un servidor central que pueda ser apagado o moderado.
- Privacidad y seguridad: Los mensajes suelen estar encriptados de extremo a extremo, garantizando que solo el emisor y el receptor puedan leerlos.
- Interoperabilidad: Al basarse en protocolos abiertos, un mensaje enviado desde una aplicación puede ser leído en cualquier otra que integre el mismo estándar.

**Desventajas**:

- Gestión de spam: Filtrar el spam de forma descentralizada sin comprometer la privacidad es un reto técnico significativo.
- Experiencia de usuario: Puede ser menos fluida que las aplicaciones de mensajería Web2, especialmente en lo que respecta a la gestión de claves y la sincronización de mensajes.
- Efecto de red: El crecimiento de usuarios cause congestión, degrada el rendimiento y aumenta los costos si no se implementan soluciones avanzadas de escalabilidad.

**Ejemplos**:

- [XMTP](https://xmtp.org/): Es un protocolo abierto y una red para la mensajería segura entre wallets. Ofrece SDKs para construir rápidamente funcionalidades de chat en cualquier dApp.
- [Push Protocol](https://push.org/): Anteriormente conocido como EPNS, se especializa en el envío de notificaciones descentralizadas a las direcciones de los usuarios, permitiendo a las dApps comunicar información importante (ej. "tu subasta está a punto de terminar").
- [Dialect](https://www.dialect.to/): Ofrece un SDK para notificaciones y mensajería wallet-a-wallet, con un enfoque en la creación de experiencias de usuario ricas e interactivas.
- [Waku](https://waku.org/): No es un SaaS en sí, sino el protocolo de comunicación P2P modular en el que se pueden construir soluciones de mensajería. Es el sucesor de Whisper y la capa de comunicación de proyectos como Status.

**Cuándo usar**:

Para cualquier dApp que necesite una capa de comunicación, ya sea para notificaciones, soporte al cliente, interacción entre usuarios o la creación de una aplicación de mensajería nativa de Web3.

## [Storage-as-a-Service (STaaS)](https://www.purestorage.com/la/knowledge/what-is-storage-as-a-service.html)

Estos servicios proporcionan acceso a infraestructura de almacenamiento descentralizado Web3, como [IPFS](https://ipfs.tech/), [Arweave](https://arweave.org/use) o [Sia](https://sia.tech/). Funcionan como capas de abstracción que facilitan el uso de estas redes, ofreciendo interfaces más amigables y herramientas de gestión similares a las de la nube tradicional. En otro caso [Storj](https://www.storj.io/) la propia red ofrece una experiencia de almacenamiento compatible con S3 vía API, actuando como un STaaS que da acceso a una red descentralizada nativa que cuenta con un ecosistema propio basado en tokens e incentivos internos.

**Ventajas**:

- Abstracción de la complejidad: Permiten usar redes como IPFS o Arweave a través de APIs sencillas (ej. S3), sin necesidad de gestionar nodos, criptomonedas o la complejidad del protocolo subyacente.
- Experiencia de desarrollador mejorada: Ofrecen interfaces y herramientas familiares, similares a las de la nube tradicional, acelerando la integración y el desarrollo.
- Modelo de costes predecible: Generalmente funcionan con suscripciones (ej. pago mensual en USD), lo que facilita la planificación de costes frente a la volatilidad de los tokens nativos de las redes de almacenamiento.
- Acceso unificado: Plataformas como Filebase actúan como agregadores, permitiendo interactuar con múltiples redes de almacenamiento descentralizado desde una única API.

**Desventajas**:

- Punto de centralización: Aunque utilizan redes descentralizadas, el servicio STaaS es un intermediario centralizado. Si el proveedor sufre una interrupción, el acceso a los datos puede verse afectado.
- Dependencia del proveedor: Se genera una dependencia de la plataforma, sus APIs y su modelo de negocio. Una migración a otro servicio o al uso directo del protocolo puede ser compleja.
- Menor soberanía: Se delega en un tercero la interacción con la red de almacenamiento, lo que reduce el control directo y la soberanía sobre los datos en comparación con el uso nativo del protocolo.
- Posibles costes ocultos: El modelo de precios puede no ser siempre el más eficiente a largo plazo, especialmente para grandes volúmenes de datos, en comparación con los modelos de pago único de algunas redes como Arweave.

**Ejemplos**:

- [filecoin](https://filecoin.io/) y [https://filecoin.cloud](https://filecoin.cloud): Filecoin y Filecoin Cloud — la primera es la red de incentivos de almacenamiento, y la segunda la capa de servicios que, como STaaS descentralizado, permite gestionar, programar y consumir almacenamiento verificable de forma directa desde aplicaciones. Se consideran STaaS pero realmente son descentralizados en este particular caso.

> **Nota**: No se incluyen ejemplos de servicios de pinning ni de gateways de IPFS porque son categorías distintas.  
> – Los pinning services pueden ofrecer planes de suscripción, pero no son STaaS: solo mantienen copias fijadas en sus propios nodos sin garantías incentivadas ni durabilidad verificable.  
> – Los gateways de IPFS no almacenan datos ni ofrecen suscripción orientada a almacenamiento; únicamente proporcionan acceso HTTP a contenido ya existente en la red IPFS.  

- [NFT.Storage](https://nft.storage/): Servicios STaaS centralizado construidos sobre Filecoin que abstraen la complejidad de la red subyacente, ofreciendo APIs simples para gestionar almacenamiento verificable, con casos de uso desde datos generales hasta NFTs especializados.
- [Irys](https://irys.xyz/): Plataformas STaaS sobre Arweave que proporcionan almacenamiento permanente con interfaces intuitivas, cifrado integrado y cargas instantáneas, optimizando la integración de datos inmutables en aplicaciones.
- [Storj](https://www.storj.io/): Plataforma STaaS de almacenamiento descentralizado compatible con S3, ofreciendo APIs familiares, cifrado nativo y redundancia distribuida. Es un sistema de almacenamiento completo y autónomo, ideal para migrar aplicaciones existentes a infraestructura descentralizada sin cambios arquitectónicos significativos porque ofrece ese API de fácil acceso.
- [Filebase](https://filebase.com/): Plataforma STaaS sobre SIA, IPFS y Storj que unifica el acceso a estas redes mediante una API compatible con S3. Actúa como un agregador que simplifica la experiencia de desarrollo, permitiendo almacenar datos en múltiples redes descentralizadas sin necesidad de gestionar criptomonedas o configuraciones complejas para cada protocolo.

**Cuándo usar**:

Ideal para almacenar archivos como aplicaciones DApps, activos de colecciones de NFTs, etc, garantizando que permanezcan accesibles pero con un modelo de subscription más accesible para muchos equipos de desarrollo.

## [Encryption-as-a-Service (EaaS)](https://medium.com/digitalfrontiers/encryption-as-a-service-buzzword-or-valuable-technology-47eb1e43a0a3)

Estos servicios proporcionan herramientas para el cifrado de datos con descifrado condicional basado en reglas on-chain. A diferencia del cifrado tradicional donde una única clave privada da acceso a todo el contenido, estos sistemas permiten cifrar datos y que solo puedan ser descifrados si se cumplen ciertas condiciones verificables en la blockchain (por ejemplo, "solo los poseedores de este NFT pueden descifrar el contenido" o "solo después de cierta fecha").

Utilizan técnicas criptográficas avanzadas como el cifrado basado en umbrales (threshold encryption), donde múltiples nodos deben cooperar para generar la clave de descifrado, o el cifrado por proxy (proxy re-encryption), que permite delegar derechos de descifrado sin revelar la clave original. La clave está en que los datos permanecen criptográficamente inaccesibles hasta que se cumplan las condiciones, no solo protegidos por verificaciones en servidor.

**Ventajas**:

- Cifrado condicional programable: Los datos están criptográficamente protegidos y solo se descifran si se cumplen las condiciones on-chain, sin depender de verificaciones en servidores centralizados.
- Descentralización de las claves: La gestión de claves de descifrado se distribuye entre múltiples nodos, eliminando puntos únicos de falla en la custodia criptográfica.
- Privacidad garantizada: Los datos pueden almacenarse en cualquier lugar (incluso en redes públicas como IPFS o Arweave) porque permanecen cifrados; solo las condiciones on-chain determinan quién puede descifrarlos.

**Desventajas**:

- Complejidad de implementación: La integración de sistemas de cifrado descentralizado requiere un conocimiento profundo de criptografía y de la arquitectura de la red utilizada.
- Latencia y rendimiento: El proceso de solicitar y obtener las claves de descifrado desde una red descentralizada puede introducir latencia en comparación con soluciones centralizadas.
- Dependencia de la disponibilidad de la red: Si la red de nodos que gestiona las claves no está disponible o suficiente número de nodos están offline, el descifrado puede fallar o retrasarse.

**Ejemplos**:

- [Lit Protocol](https://litprotocol.com/): Es una red descentralizada para la gestión de claves y la computación confidencial. Permite encriptar contenido y definir condiciones de acceso on-chain para su descifrado.
- [Threshold Network](https://threshold.network/): Proporciona un conjunto de servicios criptográficos descentralizados, incluyendo el cifrado por proxy (proxy re-encryption), que permite a un propietario de datos delegar derechos de descifrado a otros sin revelar su clave privada.

**Cuándo usar**:

Cuando necesitas que los datos permanezcan criptográficamente inaccesibles y solo puedan ser descifrados bajo condiciones específicas on-chain. Casos de uso incluyen contenido premium cifrado para holders de NFTs (videos, música, documentos que nadie puede ver sin el token correcto), sistemas de gestión de datos médicos donde el paciente controla criptográficamente quién puede leer su información, o documentos confidenciales que solo se descifran bajo condiciones temporales o de gobernanza verificables en blockchain.

## [Access-Control-as-a-Service (ACaaS)](https://tapkey.io/en/access-control-as-a-service-what-does-that-mean/)

Estos servicios proporcionan infraestructura para implementar control de acceso basado en la posesión de activos on-chain (tokens, NFTs, saldo mínimo, membresía en una DAO, etc.) sin necesidad de cifrar el contenido. A diferencia de EaaS donde los datos están criptográficamente protegidos, ACaaS verifica las credenciales on-chain del usuario y otorga o deniega acceso a recursos, aplicaciones o funcionalidades.

La técnica más conocida es el [**token gating**,](https://www.coinbase.com/es-es/learn/crypto-basics/what-is-token-gating-and-what-are-the-benefits-of-doing-it) que restringe el acceso a contenido, eventos, comunidades o funcionalidades exclusivas basándose en la posesión de ciertos tokens o NFTs. El contenido en sí no está cifrado, pero el sistema verifica la wallet del usuario contra la blockchain antes de permitir el acceso. Esto habilita experiencias como comunidades privadas para holders, acceso a eventos exclusivos, funcionalidades premium en aplicaciones, o contenido restringido en plataformas.

**Ventajas**:

- Implementación sencilla: No requiere conocimientos avanzados de criptografía, solo verificación de balances o propiedad de tokens mediante llamadas a contratos inteligentes o APIs.
- Baja latencia: La verificación es rápida, ya que solo implica consultar el estado actual de la blockchain sin procesos de cifrado/descifrado.
- Flexibilidad en las reglas: Permite condiciones complejas como "poseer al menos 100 tokens Y ser miembro de esta DAO" o "haber participado en cierto evento on-chain".
- Experiencia de usuario fluida: Los usuarios pueden acceder a contenido inmediatamente tras la verificación, sin pasos adicionales de descifrado.

**Desventajas**:

- Sin protección criptográfica: El contenido no está cifrado, por lo que si alguien obtiene acceso directo al servidor o a la URL, puede ver el contenido sin verificación.
- Dependencia del servidor: La verificación suele ocurrir en el backend o frontend, creando un punto centralizado que puede ser vulnerado o sufrir interrupciones.
- Posibilidad de evasión: Un usuario técnico podría intentar bypassear la verificación si el contenido no está adecuadamente protegido a nivel de infraestructura.
- Verificación en tiempo real: Requiere consultas constantes a la blockchain para validar la posesión actual de tokens, lo que puede generar costes o limitaciones de rate limit en APIs.

**Ejemplos**:

- [Lit Protocol](https://litprotocol.com/): Además de cifrado, ofrece herramientas de token gating para controlar acceso a contenido web sin necesidad de cifrarlo.
- [Guild.xyz](https://guild.xyz/): Plataforma especializada en token gating que permite crear comunidades y roles en Discord, Telegram o plataformas web basándose en la posesión de tokens, NFTs o participación on-chain.
- [Collab.Land](https://www.collab.land/): Bot para Discord y Telegram que gestiona roles y acceso a canales basándose en la posesión de tokens o NFTs, verificando automáticamente las wallets de los miembros.
- [Tokenproof](https://tokenproof.xyz/): Servicio que permite demostrar la propiedad de NFTs sin exponer tu wallet, habilitando token gating para eventos físicos, experiencias digitales y comunidades.
- [Unlock Protocol](https://unlock-protocol.com/): Protocolo para crear membresías y suscripciones basadas en NFTs, permitiendo token gating para contenido, eventos y servicios.

**Cuándo usar**:

Ideal para implementar acceso exclusivo a comunidades, eventos, contenido o funcionalidades basándose en la posesión de tokens o NFTs, cuando no se requiere protección criptográfica del contenido. Casos de uso incluyen comunidades privadas en Discord para holders de NFTs, acceso a eventos virtuales o presenciales exclusivos, contenido premium en plataformas educativas o de entretenimiento, funcionalidades avanzadas en aplicaciones (como trading bots solo para holders de un token de gobernanza), o sistemas de recompensas y beneficios escalonados según el nivel de participación on-chain.

## [Automation-as-a-Service (AaaS)](https://www.blinno.ch/en/blog/was-ist-automation-as-a-service)

Estos servicios, a menudo llamados "redes de guardianes" (keeper networks), proporcionan una forma de automatizar la ejecución de transacciones en la blockchain. Permiten a los desarrolladores definir trabajos que se ejecutan cuando se cumplen ciertas condiciones (de tiempo o de estado) sin necesidad de operar su propia infraestructura de bots.

**Ventajas**:

- Fiabilidad: Utilizan una red descentralizada de "keepers" para garantizar que los trabajos se ejecuten a tiempo.
- Ahorro de infraestructura: Evita tener que mantener un servidor o un bot solo para enviar transacciones programadas.
- Descentralización: La ejecución de la lógica automatizada no depende de un único actor centralizado.

**Desventajas**:

- Coste: La ejecución de estos trabajos tiene un coste, que suele ser pagado en el token nativo de la red de automatización.
- Limitaciones de complejidad: Pueden no ser adecuados para tareas de automatización extremadamente complejas o que requieran una latencia muy baja.

**Ejemplos**:

- [Gelato](https://www.gelato.network/): Es una de las redes de automatización más populares. Permite a los desarrolladores ejecutar transacciones futuras basadas en tiempo, eventos o lógica computacional arbitraria.
- [Chainlink Automation](https://chain.link/automation): Anteriormente conocido como Chainlink Keepers, es un servicio de automatización de transacciones descentralizado y fiable que forma parte del ecosistema de Chainlink.
- [OpenZeppelin Defender Autotasks](https://www.openzeppelin.com/defender): Permite a los desarrolladores escribir scripts (Autotasks) que se pueden ejecutar de forma programada o ser disparados por una llamada a una API, integrándose con un Relayer para la gestión de las transacciones.

**Cuándo usar**:

Para cualquier tarea que necesite ser ejecutada de forma regular o en respuesta a un evento on-chain, como la recolección de recompensas de un protocolo de finanzas descentralizadas (DeFi), la ejecución de órdenes límite en un DEX, o el mantenimiento regular de un contrato inteligente.

### [Smart Contract Factory / NFT-as-a-Service](https://medium.com/@emma.onyedika.okeke/understanding-factory-contracts-in-solidity-f1b7f901683c)

Estos servicios se especializan en la creación, gestión y distribución de tokens (tanto fungibles como no fungibles) mediante plantillas pre-auditadas y el patrón de contract factory. Esta categoría engloba lo que a menudo se denomina **NFT-as-a-Service**, permitiendo a las empresas lanzar colecciones y activos digitales sin escribir una sola línea de Solidity. El usuario configura parámetros y el sistema despliega una instancia nueva de un contrato estándar.

**Ventajas**:

- Abstracción de la complejidad: Simplifican enormemente el proceso de desplegar y gestionar la economía de un token o una colección de NFTs sin necesidad de escribir contratos inteligentes.
- Funcionalidades avanzadas: A menudo incluyen herramientas para airdrops, vesting, drops, royalties, permisos y otros módulos habituales.
- Rapidez: Permiten integrar la capa de tokenización en un producto con mucho menos esfuerzo de desarrollo.

**Desventajas**:

- Menor personalización: La lógica del token está limitada a las funcionalidades que ofrece la plantilla o el proveedor.
- Dependencia del proveedor: Aunque el contrato desplegado es tuyo, la operación a través del panel, SDK o API depende de su infraestructura.

**Ejemplos**:

- [Thirdweb](https://thirdweb.com/): Plataforma completa de contract factories con SDKs y dashboard para desplegar y gestionar contratos ERC20, ERC721 y ERC1155.
- [Manifold](https://www.manifold.xyz/): Enfocada en NFTs; permite a artistas desplegar sus propios contratos ERC721/1155 mediante una factory personalizada.
- [Tatum](https://tatum.io/): Ofrece creación y gestión de tokens mediante API, abstrayendo la necesidad de escribir contratos inteligentes en múltiples blockchains.
- [Crossmint](https://www.crossmint.com/): Plataforma líder en NFT-as-a-Service que permite crear, distribuir y custodiar NFTs mediante APIs sencillas, facilitando el pago con tarjeta de crédito para usuarios finales.
- [Niftory](https://niftory.com/): Proporciona APIs y herramientas para lanzar y gestionar aplicaciones basadas en NFTs de forma rápida, encargándose de la infraestructura de blockchain, wallets y metadatos.

**Cuándo usar**:

Cuando el objetivo principal es lanzar un token o una colección de NFTs (para una comunidad, un juego o un programa de lealtad) de forma rápida y fiable, aprovechando funcionalidades estándar sin tener que desarrollar contratos desde cero.

## [Farming-as-a-Service (FaaS)](https://agtecher.com/es/blog/exploring-farming-as-a-service-a-complete-guide/)

Estos servicios representan la evolución de DeFi 3.0 y, aunque no son tanto un recurso de desarrollo tradicional, constituyen una capa de orquestación financiera que maximiza la rentabilidad del capital en DeFi. FaaS automatiza y optimiza las estrategias de [yield farming](https://finematics.com/yield-farming-explained/) a través de múltiples protocolos y blockchains, moviendo el capital dinámicamente entre diferentes pools de liquidez, protocolos de préstamos y oportunidades de staking para obtener los mejores rendimientos.

La idea central es que el usuario deposita sus activos en una bóveda (vault) gestionada por el servicio FaaS, y este se encarga de ejecutar estrategias complejas de forma automatizada: rebalanceo de posiciones, reinversión de recompensas (auto-compounding), arbitraje entre protocolos y optimización de rutas cross-chain. Todo esto ocurre sin intervención manual del usuario, quien simplemente recibe los rendimientos netos.

**Ventajas**:

- Optimización automática: Los algoritmos buscan constantemente las mejores oportunidades de rendimiento, algo inviable para un usuario individual.
- Ahorro de costes: Al ejecutar operaciones de forma agregada para múltiples usuarios, se reducen significativamente los costes de gas por persona.
- Gestión profesional: Las estrategias son diseñadas y monitorizadas por equipos especializados en DeFi, reduciendo errores y mejorando la eficiencia.
- Acceso democratizado: Permite a usuarios con capital limitado acceder a estrategias que normalmente requieren grandes cantidades para ser rentables.
- Cross-chain sin fricción: Mueve capital entre diferentes blockchains automáticamente para aprovechar las mejores oportunidades sin que el usuario tenga que gestionar puentes o múltiples wallets.

**Desventajas**:

- Riesgo de contratos inteligentes: Al interactuar con múltiples protocolos, la superficie de ataque aumenta. Un exploit en cualquiera de ellos puede afectar los fondos.
- Complejidad opaca: Las estrategias pueden ser difíciles de entender para usuarios no técnicos, lo que dificulta evaluar los riesgos reales.
- Comisiones de gestión: Aunque optimizan rendimientos, estos servicios cobran comisiones (típicamente un porcentaje del rendimiento o de los activos gestionados).
- Pérdida impermanente: Las estrategias que involucran provisión de liquidez están expuestas a pérdida impermanente si el mercado se mueve bruscamente.
- Dependencia del mercado: En periodos de baja volatilidad o mercados bajistas, los rendimientos pueden ser mínimos o negativos tras descontar comisiones.

**Ejemplos**:

- [Yearn Finance](https://yearn.finance/): El pionero y referente de FaaS. Sus yVaults ejecutan estrategias automatizadas de yield farming optimizadas por la comunidad de estrategas.
- [Beefy Finance](https://beefy.finance/): Plataforma multi-chain que ofrece auto-compounding de recompensas en múltiples protocolos DeFi, con estrategias optimizadas para diferentes niveles de riesgo.
- [Harvest Finance](https://harvest.finance/): Agrega yield farming de diferentes protocolos y automatiza la reinversión de recompensas, optimizando los retornos netos.
- [Convex Finance](https://www.convexfinance.com/): Especializado en optimizar rendimientos de Curve Finance, simplificando el proceso de staking y maximizando recompensas CRV y CVX.
- [Idle Finance](https://idle.finance/): Protocolo que rebalancea automáticamente entre diferentes protocolos de lending para obtener los mejores rendimientos con el nivel de riesgo seleccionado.

**Cuándo usar**:

Ideal para usuarios o protocolos que buscan maximizar rendimientos en DeFi sin dedicar tiempo a gestionar estrategias manualmente. Especialmente útil cuando se tiene capital que genera rendimientos pasivos pero se quiere optimizar su rentabilidad sin la complejidad de operar directamente en múltiples protocolos. También es valioso para proyectos que necesitan gestionar tesorerías de forma eficiente, maximizando el valor de sus reservas mientras mantienen liquidez disponible.

## Plataformas multi-categoría

Algunas plataformas no encajan en una única categoría porque integran varias capas de infraestructura en un solo stack. En lugar de forzarlas dentro de una categoría concreta, conviene entenderlas como stacks completos de ejecución onchain, donde la wallet, la automatización y la orquestación DeFi forman parte de un producto cohesionado.

### [Biconomy](https://www.biconomy.io/)

Biconomy comenzó en 2019 como una solución de meta-transacciones (relayers gasless) y ha evolucionado hasta convertirse en una plataforma de ejecución onchain completa. Su propuesta es ofrecer experiencia Web2 en aplicaciones Web3, eliminando la fricción del gas, la gestión de múltiples chains y la complejidad de la firma de transacciones.

Su arquitectura se articula alrededor de tres componentes principales que cubren categorías distintas de este documento. En el plano de WaaS, ofrece **Nexus**, su smart account propia compatible con [ERC-7579](https://eips.ethereum.org/EIPS/eip-7579), que es la más eficiente en gas del mercado con un 25% menos de coste que alternativas. Nexus incluye arquitectura modular para instalar módulos de recuperación, límites de gasto o session keys, y funciona tanto con wallets EOA (vía EIP-7702) como con smart accounts propias.

En el plano de AaaS, Biconomy introduce el **MEE (Modular Execution Environment)**, que va más allá de ERC-4337. Con MEE, el usuario firma una sola vez y el sistema ejecuta operaciones encadenadas en múltiples chains, gestionando bridges, orden de ejecución y gas de forma automática. Esto incluye ejecución condicional basada en oráculos de precio, TWAPs y otras lógicas complejas que los keepers tradicionales no pueden orquestar de forma composable.

Las **Smart Sessions** son el mecanismo que conecta WaaS con AaaS: permiten delegar permisos de ejecución scoped a agentes (bots, estrategias automatizadas, agentes de IA) con límites precisos por contrato, función y monto, sin requerir firmas adicionales del usuario en cada operación. Un agente puede, por ejemplo, rebalancear fondos entre AAVE, Morpho y Yearn, pero únicamente con USDC y con un techo de 10.000 USDC, sin ningún acceso fuera de esos parámetros.

Finalmente, en el plano de orquestación DeFi, la **Supertransaction API** ofrece swaps cross-chain con routing óptimo entre DEXs, zaps de un clic para entrar o salir de vaults y mercados de lending, y acceso unificado a más de 200 protocolos a través de una sola API REST, sin necesidad de escribir contratos ni gestionar encodings.

**Ventajas**:

- Stack completo: combina smart accounts, gasless, automatización y orquestación DeFi en una sola integración.
- Una firma, múltiples chains: el usuario no gestiona bridges ni secuenciación de transacciones entre redes.
- Compatibilidad universal: funciona con EOAs existentes (MetaMask, Rabby), wallets embebidas (Privy, Dynamic) e institucionales (Fireblocks, Safe), sin migración.
- Smart Sessions para agentes: delega ejecución autónoma con políticas de seguridad on-chain, ideal para estrategias DeFi automatizadas y agentes de IA.
- Eficiencia de gas: Nexus reduce coste por transacción frente a otras smart accounts.

**Desventajas**:

- Complejidad del stack: la amplitud de capacidades implica una curva de aprendizaje mayor que soluciones de una sola categoría.
- Dependencia del proveedor: el MEE y el bundler son infraestructura centralizada de Biconomy; una interrupción afecta a todas las capas simultáneamente.
- Madurez del ecosistema: aunque battle-tested con 70M+ transacciones, el MEE y las Smart Sessions son componentes más recientes con menor historial en producción.

**Cuándo usar**:

Cuando se necesita construir una dApp con experiencia de usuario sin fricciones y con lógica de ejecución compleja: onboarding sin gas, operaciones multi-step en múltiples chains con una sola firma del usuario, o delegación de ejecución a agentes autónomos con límites de seguridad precisos. Es especialmente relevante para aplicaciones DeFi avanzadas, juegos onchain y cualquier producto que quiera eliminar todas las barreras técnicas de la blockchain para el usuario final.

---
