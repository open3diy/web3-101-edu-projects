# Ecosistema Web3: Infraestructura

El ecosistema Web3 es complejo de entender y, además, está en construcción. Está formado por lo que se considera la infraestructura, compuesta por redes blockchain, capas de escalado, almacenamiento, oráculos, servicios y herramientas de desarrollo o stack tecnológico.

Este ecosistema funciona, en esencia, en diferentes capas de redes de nodos que siguen un protocolo para que todo encaje como piezas de lego, es decir la composabilidad.

En el ecosistema conviven organizaciones, DAOs, proyectos con token... es decir, un amplio abanico que permite añadir esa capa de gestión y valor a internet, es decir, la Web3.

Esta diversidad, aunque puede resultar abrumadora al principio, es clave para comprender las oportunidades y desafíos que ofrece Web3. Además, cada capa —desde las blockchains, protocolos, servicios, organizaciones y aplicaciones descentralizadas— cumple una función específica y, una vez comprendida, resulta más fácil participar.

Pero también es cierto que Web3 puede ser algo caótica, ya que está impulsada por organizaciones, comunidades, empresas, grandes tecnológicas, startups, DAOs, agencias, laboratorios y, en ocasiones, gobiernos. Estos actores o jugadores llegan a acuerdos, pero también impulsan el ecosistema en distintas direcciones, lo que genera diversidad y dinamismo, pero también demasiadas alternativas que debemos filtrar. Por eso, ante tantas posibilidades, debes elegir tu propia hoja de ruta, es decir, pensar qué es lo que buscas tú de Web3.

Conocer el panorama general te permitirá identificar las áreas más relevantes según tus intereses, ya sea el desarrollo de aplicaciones, la participación en comunidades, la exploración de nuevas tecnologías o la contribución a la descentralización.

Este artículo busca ofrecer una visión de conjunto de la infraestructura blockchain como parte fundamental para elegir y empezar a construir, pero también filtra eligiendo un camino o "path" que es la propuesta de valor de este repositorio `web3-101`; de lo contrario, tanta dispersión haría imposible avanzar.

## Redes blockchain

Las redes blockchain constituyen la base de Web3 y forman parte de su infraestructura fundamental. Bitcoin fue la pionera, considerada como "oro digital" por su escasez programada y su enfoque en la reserva de valor. Es el ejemplo de blockchain de primera generación, considerada una red de [capa 1](https://www.bitstamp.net/es/learn/blockchain/what-is-a-layer-1-blockchain/) (Layer 1 o L1), centrada en la seguridad y la resistencia a la censura, pero con capacidades limitadas de programación. Ethereum, como blockchain de segunda generación y también L1, introdujo los contratos inteligentes y la programabilidad Turing-completo (limitada por el coste o gas), permitiendo el desarrollo de DApps y protocolos complejos.

Posteriormente, aunque ya se estaban desarrollando desde hace tiempo, aparecen redes de tercera generación que, desde su diseño inicial, abordan los desafíos de escalabilidad, sostenibilidad y comisiones bajas. La escalabilidad no solo implica mejorar el rendimiento, sino también abordar la personalización para casos de uso específicos y la interconexión entre redes, mediante dos enfoques principales que no son excluyentes: modularidad e interoperabilidad.

La modularidad permite diseñar blockchains como componentes especializados que pueden combinarse según las necesidades (como se ve en las [appchains](https://cointelegraph.com/learn/articles/appchain-application-specific-blockchain)), mientras que la interoperabilidad facilita la comunicación y transferencia de activos entre diferentes redes. Ejemplos de arquitecturas modulares con interoperabilidad nativa incluyen [redes de capa 0](https://www.coinbase.com/es-es/learn/crypto-glossary/what-are-layer-0-protocols) (Layer 0 o L0) como [Polkadot](https://es.wikipedia.org/wiki/Polkadot) y [Cosmos](https://cointelegraph.com/learn/articles/what-is-cosmos-a-beginners-guide-to-the-internet-of-blockchains), que actúan como infraestructura base sobre la cual se pueden construir múltiples blockchains L1 interconectadas.

Por otro lado, existen [blockchains monolíticas optimizadas](https://www.alchemy.com/overviews/modular-vs-monolithic-blockchains) de capa 1 que integran todas las funciones en una arquitectura cohesionada, como [Cardano](https://cardano.org/discover-cardano) (con enfoque académico y sostenible), [Avalanche](https://www.avax.network/about), [Algorand](https://algorand.co/learn), [Near](https://www.near.org/) o [Aptos](https://academy.bit2me.com/que-es-aptos/).

Ethereum, por su parte, continúa evolucionando e incorporando tecnologías de tercera generación para mantenerse competitiva, adoptando soluciones modulares sin renunciar a su arquitectura base.

  > No es fácil generalizar, cada red blockchain tiene su propio enfoque y busca atraer comunidades específicas. Las blockchains monolíticas suelen centrarse en el marketing y en ofrecer una experiencia Web3 completa e integrada. Otras, en cambio, actúan como redes de infraestructura. Muchas adoptan compatibilidad con la EVM para facilitar la interoperabilidad y atraer a las comunidades ya existentes en Ethereum y otras tienen enfoques diferentes...en realidad es un ecosistema tan amplio que es difícil de definir.

Muchas de estas redes de segunda y tercera generación, especialmente las monolíticas, adoptan una arquitectura que integra todas las funciones principales junto con un ecosistema completo de aplicaciones. Esta aproximación ofrece un "stack" más accesible y cohesionado, que abarca desde herramientas para el desarrollo y despliegue de contratos inteligentes, ayudas o grants para hacer crecer el ecosistema, hasta la gestión de identidades y cualquier necesidad para crear soluciones Web3, generando un entorno propio más amigable para desarrolladores y usuarios.

Esta integración tiene ventajas claras: simplifica la experiencia de desarrollo, reduce la complejidad técnica inicial y puede acelerar la adopción en casos de uso específicos como gaming, aplicaciones sociales o plataformas orientadas al usuario final. Por otro lado, esta cohesión puede implicar mayor dependencia de los equipos fundadores y ecosistemas más integrados verticalmente, lo que plantea consideraciones sobre el grado de descentralización y apertura comparado con modelos más modulares. Ethereum, por su parte, mantiene un modelo más abierto y comunitario —aunque no exento de desafíos como la concentración de validadores—, priorizando la descentralización y la neutralidad a costa de mayor complejidad técnica.

  > Cada red blockchain tiene su propia evolución en gobernanza y descentralización. Muchas redes monolíticas están transitando activamente hacia modelos más abiertos y descentralizados, y algunas han logrado balances interesantes entre eficiencia operativa y participación comunitaria. Es fundamental analizar cada caso individualmente, ya que los grados de descentralización, apertura y compromiso con la comunidad varían significativamente entre proyectos. Las generalizaciones pueden ser injustas con redes que realmente están innovando en gobernanza y experiencia de usuario.

Como comentamos, Ethereum evoluciona constantemente para alcanzar la escalabilidad y conectividad y mejorar la experiencia de usuario. Aunque no avanza tan rápido como otras redes de tercera generación, prioriza la seguridad, no solo de la red, sino también en la consolidación de cada paso evolutivo, guiado por una visión clara de lo que debería ser una blockchain abierta y neutral. Por eso, muchos la consideramos como la red de referencia, especialmente en lo que respecta a descentralización y robustez del ecosistema.

Ethereum, para abordar los problemas de escalabilidad y costes, ha impulsado soluciones de segunda capa ([Layer 2](https://www.coinbase.com/es-es/learn/crypto-basics/what-are-ethereum-layer-2-blockchains-and-how-do-they-work)), como [Optimistic Rollups y ZK-Rollups](https://www.nervos.org/es/knowledge-base/zk_rollup_vs_optimistic_rollup). Estas tecnologías permiten procesar transacciones fuera de la cadena principal (Layer 1) y luego consolidar los resultados en ella, lo que incrementa la capacidad de procesamiento y reduce las comisiones. Ejemplos destacados de redes Layer 2 son [Optimism](https://optimism.io/), [Arbitrum](https://arbitrum.io/), [StarkNet](https://www.starknet.io/) y [Polygon zkEVM](https://docs.polygon.technology/zkEVM/), cada una con enfoques técnicos propios. La variante [validium](https://academy.bit2me.com/que-son-los-validium-y-como-funcionan/), también considerada como capa L2, ofrece mayor flexibilidad al utilizar la capa 1 para registrar la prueba criptográfica pero no el resumen de transacciones, reduciendo así costes y mejorando la velocidad; un ejemplo representativo es [Immutable X](https://www.immutable.com/), una solución validium optimizada para NFTs y gaming.

  > Si quieres saber qué soluciones de capa 2 (L2) tienen mayor adopción y actividad, puedes consultar [L2Beat](https://l2beat.com/scaling/summary), donde encontrarás un resumen actualizado de las principales redes y su evolución.

Mencionamos las L2 como la solución destacada, pero no debemos olvidar otras opciones como las [sidechains](https://academy.bit2me.com/que-es-cadena-lateral-sidechain/) o cadenas laterales, que aunque tienden puentes con Ethereum, no lo usan para la seguridad principal. Existen redes muy importantes como [Polygon PoS](https://polygon.technology/) (antes Matic Network), [Gnosis Chain](https://www.gnosis.io/) (anteriormente xDai) y [Ronin](https://roninchain.com/) (orientada a gaming, especialmente Axie Infinity). Estas sidechains ofrecen mayor velocidad y comisiones reducidas, pero comprometen parte de la seguridad al mantener su propio consenso independiente, lo que las diferencia de las soluciones L2 que heredan la seguridad de Ethereum. Aunque las sidechains pueden ser adecuadas para ciertos casos de uso, las Layer 2 representan un enfoque más alineado con la seguridad y descentralización de Ethereum.

Existen propuestas de capa 3 (Layer 3) orientadas a la personalización y aplicaciones especializadas, e incluso se menciona una posible capa 4 con seguridad mejorada mediante pruebas de conocimiento cero (ZK Proofs), pero son escenarios aún lejanos y experimentales. Lo relevante en este momento es centrarse en la adopción y consolidación de las soluciones actuales de capa 1 y capa 2, que ya ofrecen un amplio margen de mejora y casos de uso prácticos.

Ethereum se ha consolidado como la principal red de liquidación (settlement layer), donde se registran y validan las transacciones más relevantes, incluso aquellas originadas en otras redes compatibles con la EVM. Este estatus no se debe solo a su adopción, sino a que su modelo descentralizado (aunque con imperfecciones) sigue siendo el más resistente a ataques y censura.

Esta es una reflexión personal e implica tomar posición sobre una solución concreta. Debemos reconocer que, por adopción y comunidad, Bitcoin se ha consolidado como la opción ganadora en su propósito, al igual que Ethereum en su rol como red programable de referencia. Si bien depender de una única red puede parecer contrario al ideal de descentralización, en la práctica representa una decisión pragmática para no quedar paralizado ante la amplitud del ecosistema.

Sin embargo, existen otras visiones igualmente válidas de Web3: un ecosistema diverso compuesto por múltiples redes especializadas —algunas monolíticas optimizadas para casos de uso específicos como gaming o aplicaciones sociales, otras modulares orientadas a componibilidad— todas coexistiendo e interconectándose mediante arquitecturas como Polkadot, Cosmos o puentes cross-chain. Cada enfoque tiene sus fortalezas: las redes monolíticas ofrecen simplicidad y experiencia de usuario optimizada; las arquitecturas modulares priorizan composabilidad y descentralización. Es probable que el tiempo, la adopción real y la evolución tecnológica terminen validando múltiples enfoques coexistentes, cada uno dominando sus nichos específicos.

  > Siempre hace falta un plan B; cualquier solución con una comunidad fuerte es necesaria en el ecosistema. No se debe malinterpretar la elección personal de Ethereum, con considerar que el resto son innecesarias o poco valiosas.

### Otros modelos de redes blockchain

Además de las blockchains generalistas y las soluciones de capa 2, existen otros modelos de redes blockchain diseñados para casos de uso específicos o sectores verticales. Aunque no representan el enfoque mayoritario en el ecosistema Web3 orientado al usuario final (retail), es importante conocerlos para comprender la diversidad del panorama blockchain:

- Custom Blockchains: Redes blockchain personalizadas que se diseñan desde cero o mediante frameworks para atender funcionalidades particulares, requisitos de privacidad, modelos de consenso específicos o integración con sistemas existentes. Permiten un control total sobre la arquitectura y las reglas de la red. Ejemplo: Blockchains empresariales desarrolladas con [Hyperledger Fabric](https://www.hyperledger.org/use/fabric) o [Substrate](https://substrate.io/).

- Vertical Blockchains: Redes blockchain centradas en una industria, sector o función específica, como salud, cadena de suministro, finanzas o identidad digital. Estas blockchains optimizan sus capacidades técnicas, privacidad y regulación para resolver problemas concretos de su dominio. Ejemplo: [VeChain](https://www.vechain.org/) (cadena de suministro y trazabilidad), [Hedera](https://hedera.com/) (aplicaciones empresariales con consenso único).

Estos modelos no suelen mencionarse en la narrativa principal de Web3 porque su adopción es más limitada, su enfoque es especializado y su público objetivo no es el usuario general, sino organizaciones, empresas o comunidades técnicas con necesidades específicas. Sin embargo, representan una parte importante del ecosistema blockchain y reflejan la flexibilidad y modularidad que caracteriza a esta tecnología.

  > Estos modelos blockchain suelen estar más orientados a casos de uso empresariales (B2B), gobierno o sectores regulados, donde la personalización, privacidad y cumplimiento normativo son prioritarios frente a la apertura y descentralización radical que caracteriza a las redes públicas de Web3.

### Características de las redes blockchain

Cuando hablamos de redes blockchain, no debemos olvidar que tienen diferentes características en base a las necesidades que cubren. En este repositorio de `web3-101` nos centramos sobre todo en redes blockchain que adoptan un modelo de confianza "trustless", que son públicas o con variantes permisionadas, y emplean modelos de gobernanza lo mas abiertas posibles, preferiblemente descentralizada o DAOs, que resultan especialmente útiles en una Web3 abierta. Siendo conscientes que existen otros tipos orientadas a empresas, gobiernos u organizaciones, que pueden ser privadas o permisionadas, con gobernanza centralizada o federada, no aporta ningún valor al emprendedor que quiere participar en el ecosistema, por lo menos, no es del interés de este autor, cuando el objetivo es la divulgación de un ecosistema abierto.

> Te animo a leer más en [introducción a redes p2p](../infrastructure/miscelanea/p2p_overview.md).

### Escalabilidad e interoperabilidad en las redes blockchain

Aunque ya lo hemos resumido anteriormente, es fundamental entender las soluciones de escalabilidad e interoperabilidad en redes blockchain.

Como vimos, las redes blockchain de capa 1 (L1) son fundamentales porque proporcionan la seguridad base sobre la que se construyen contratos inteligentes y aplicaciones. Sin embargo, la escalabilidad se ha convertido en un requisito esencial, no solo en términos de rendimiento y tarifas, sino también en funcionalidad, personalización y soporte para nuevos casos de uso. En la práctica, la mayoría de usuarios y desarrolladores acabarán construyendo sobre capas de escalabilidad de capa 2 (L2), donde se concentra la innovación, las comunidades y la adopción masiva.

Antes de profundizar en los enfoques de escalabilidad, es importante recordar las diferentes capas de redes que podemos encontrar en el ecosistema blockchain:

- **Capa 0 (Layer 0 o L0):** Actúa como infraestructura base que facilita la interoperabilidad entre múltiples blockchains L1, permitiendo arquitecturas modulares donde cada capa cumple una función específica. Ejemplos: Polkadot, Cosmos, Celestia.

- **Capa 1 (Layer 1 o L1):** Son las redes blockchain principales que gestionan el consenso, la seguridad y la ejecución de transacciones. Pueden clasificarse según su arquitectura y dependencias normalmente como:
  - L1 independientes monolíticas: Integran todas las funciones (consenso, ejecución, disponibilidad de datos) en una arquitectura cohesionada autónoma. Ejemplos: Solana, Cardano, Avalanche.
  - L1 independientes modulares: Operan de forma autónoma pero delegan ciertas funciones a otras capas, especialmente escalabilidad mediante L2 (capa 2). Ejemplo: Ethereum con su enfoque de rollups.
  - L1 construidas sobre L0: Blockchains que dependen estructuralmente de una infraestructura de capa 0 (L0, capa inferior) para seguridad compartida e interoperabilidad nativa. Ejemplos: parachains en Polkadot, subnets en Avalanche.

- **Capa 2 (Layer 2 o L2):** Soluciones de escalabilidad que procesan transacciones fuera de la cadena principal (off-chain) y luego consolidan los resultados en la L1, heredando su seguridad. Permiten mayor capacidad de procesamiento y menores comisiones sin comprometer la descentralización de la capa base. Ejemplos: Optimism, Arbitrum, StarkNet, Polygon zkEVM.

En cuanto a interoperabilidad, una de las soluciones más conocidas —y también la más problemática en términos de seguridad— son los bridges o puentes. Los bridges permiten transferir activos y datos entre diferentes blockchains o capas, facilitando la interoperabilidad entre ecosistemas que, de otro modo, serían incompatibles. Sin embargo, estos puentes suelen ser el punto más vulnerable de la infraestructura Web3; de hecho, la mayoría de los mayores hackeos en Web3 han ocurrido en bridges.

Por eso, para evitar el uso de puentes externos y mejorar la seguridad, han surgido soluciones de interoperabilidad más seguras y nativas integradas en la propia arquitectura de capas que hemos mencionado. Para mostrarte estas soluciones, lo mejor es que veamos a continuación los siguientes enfoques o diseños arquitectónicos que quizás ayudan a entender mejor la solución:

#### Orientado a la personalización: appchain

Las [appchains](https://cointelegraph.com/learn/articles/appchain-application-specific-blockchain), o cadenas de aplicaciones, representan una evolución en la infraestructura blockchain orientada a la personalización. A diferencia de las blockchains públicas y generalistas, las appchains están diseñadas para servir a aplicaciones o comunidades específicas, permitiendo adaptar parámetros como la gobernanza, el consenso, la privacidad y el rendimiento según las necesidades concretas del caso de uso.

Este enfoque modular facilita la creación de redes independientes que pueden optimizarse para requisitos particulares, como escalabilidad, comisiones bajas, reglas de validación personalizadas o integración con sistemas externos. Las appchains suelen desplegarse sobre arquitecturas que soportan interoperabilidad nativa, como [Cosmos](https://cosmos.network/) (mediante el protocolo IBC), [Polkadot](https://polkadot.network/) (parachains), [Avalanche](https://www.avax.network/) (subnets) o mediante frameworks como [Polygon CDK](https://polygon.technology/polygon-cdk/) y [OP Stack](https://stack.optimism.io/) en el ecosistema Ethereum.

**Arquitecturas típicas de appchains:**

Las appchains pueden implementarse mediante diferentes arquitecturas según el nivel de personalización, seguridad e interoperabilidad requeridos:

- **Appchains como L1 independientes:** Blockchains autónomas con su propio consenso, validadores y seguridad totalmente independientes. Operan de forma soberana y pueden conectarse a otras redes mediante puentes externos o protocolos de interoperabilidad, pero **no dependen** de ninguna infraestructura base para su seguridad o funcionamiento. Ejemplo: una blockchain construida con [Cosmos SDK](https://cosmos.network/sdk) que opera de manera autónoma, aunque pueda comunicarse con otras cadenas mediante IBC.

- **Appchains como L2 o rollups personalizados:** Soluciones de capa 2 que **heredan la seguridad** de una blockchain principal (como Ethereum), procesando transacciones fuera de la cadena base pero consolidando los resultados en ella. Permiten personalizar la ejecución y lógica para aplicaciones específicas sin renunciar a la seguridad de la L1. Frameworks como [OP Stack](https://stack.optimism.io/) (Optimistic Rollups) y [Polygon CDK](https://polygon.technology/polygon-cdk/) (ZK Rollups) facilitan la creación de estas appchains L2 con interoperabilidad dentro de su ecosistema.

- **Appchains sobre infraestructura L0 (parachains/subnets modulares):** Redes especializadas que se conectan a una **infraestructura de capa 0 (L0)** que actúa como base modular, proporcionando seguridad compartida, interoperabilidad nativa y comunicación entre cadenas. A diferencia de las L1 independientes, estas appchains **dependen estructuralmente** de la L0 para su seguridad y conectividad. Ejemplo: [parachains en Polkadot](https://polkadot.network/features/parachains/), que comparten seguridad mediante la relay chain (L0), o [subnets en Avalanche](https://www.avax.network/subnets), que pueden personalizar consenso y reglas dentro de la arquitectura modular de Avalanche.

> **Diferencia clave:** Las L1 independientes tienen seguridad y consenso propios, y la interoperabilidad es opcional mediante puentes. Las appchains sobre L0 **dependen** de una infraestructura base que les proporciona seguridad compartida e interoperabilidad nativa desde el diseño, formando parte de un ecosistema modular integrado.

La principal ventaja de las appchains es la flexibilidad: cada aplicación puede definir su propio entorno, reglas y recursos, sin depender de las limitaciones de una red principal. Esto permite casos de uso avanzados en gaming, DeFi, identidad, privacidad, gestión de datos o comunidades autónomas, donde la personalización es clave para la adopción y el éxito.

Sin embargo, la proliferación de appchains plantea retos en interoperabilidad, seguridad y liquidez, ya que cada red debe garantizar su conectividad y protección frente a ataques. Por ello, las soluciones de infraestructura que facilitan la comunicación entre appchains y la reutilización de seguridad (como EigenLayer en Ethereum) son cada vez más relevantes en el ecosistema Web3.

Esta opción se menciona por cuestiones académicas y de divulgación, pero construir una red personalizada a partir de un stack tecnológico propio o mediante frameworks como [Cosmos SDK](https://cosmos.network/sdk), [Substrate](https://substrate.io/) o [OP Stack](https://stack.optimism.io/) representa un desafío técnico, organizativo y económico considerable. No es una opción para todos los proyectos ni para todas las comunidades; de hecho, no es el caso común en el ecosistema. La mayoría de desarrolladores y emprendedores encontrarán suficiente flexibilidad y escalabilidad en las soluciones existentes de capa 1 y capa 2, sin necesidad de asumir la complejidad y los riesgos de crear y mantener una blockchain independiente.

#### Orientados en la escalabilidad: sub‑10 ms / 100.000+ TPS

Dentro del ecosistema se busca un objetivo claro para la adopción masiva que soporte el mismo volumen de transacciones de la web2, con una medida clara: latencia inferior a 10 ms y capacidad mayor de 100.000 transacciones por segundo (TPS).

**Arquitecturas de alto rendimiento:**

Las redes blockchain orientadas a la escalabilidad extrema pueden implementarse mediante diferentes enfoques arquitectónicos según el modelo de ejecución, seguridad y descentralización:

- **Redes L1 monolíticas de alto rendimiento:** Blockchains de capa 1 que integran todas las funciones (consenso, ejecución, disponibilidad de datos) en una arquitectura cohesionada optimizada para velocidad. Priorizan el rendimiento extremo mediante innovaciones en consenso y ejecución paralela, aunque pueden comprometer parte de la descentralización. Ejemplo: [Solana](https://solana.com/) con Proof of History y ejecución paralela, [Aptos](https://aptosfoundation.org/) y [Sui](https://sui.io/) con consenso optimizado y procesamiento concurrente.

- **Redes L2 de ultra-baja latencia:** Soluciones de capa 2 especializadas que **heredan la seguridad** de una blockchain principal pero optimizan radicalmente la ejecución para alcanzar latencias sub-10ms y alto TPS. Procesan transacciones de forma centralizada o semi-centralizada para máxima velocidad, consolidando resultados en L1 periódicamente. Ejemplo: [MegaEth](https://www.megaeth.com/), diseñado como infraestructura de alto rendimiento dentro del ecosistema Ethereum.

- **Ecosistemas de rollups interconectados (L2):** Arquitecturas basadas en **múltiples rollups L2** que comparten estándares técnicos (el stack) y se comunican de forma nativa, escalando horizontalmente. Cada rollup puede especializarse en casos de uso específicos mientras mantiene interoperabilidad dentro del ecosistema. Ejemplo: [OP Stack](https://stack.optimism.io/) con la implementación de red [Superchain](https://docs.optimism.io/superchain/superchain-explainer), [zkStack](https://zkstack.io/) con ZK rollups interconectados.

- **Redes modulares con L0 de disponibilidad de datos:** Arquitecturas donde una **capa 0 especializada** proporciona disponibilidad de datos, permitiendo que múltiples L2 o appchains publiquen sus datos de forma eficiente sin depender completamente de una L1 para este propósito. Ejemplo: [Celestia](https://celestia.org/) como capa de disponibilidad de datos modular que puede servir a múltiples rollups.

> **Diferencia clave:** Las L1 monolíticas optimizan todo el stack para rendimiento sacrificando modularidad. Las L2 especializadas heredan seguridad de L1 pero centralizan ejecución para velocidad extrema. Los ecosistemas de rollups interconectados escalan horizontalmente mediante múltiples L2 que comparten estándares. Las redes modulares con L0 separan la disponibilidad de datos como capa independiente.

**Principales candidatos en la competición:**

En esta competición por alcanzar sub-10ms y 100.000+ TPS, [Solana](https://solana.com/) lidera el enfoque monolítico de capa 1, apostando por rendimiento extremo directamente en la capa base. Otras redes L1 como [Aptos](https://aptosfoundation.org/), [Sui](https://sui.io/) y [Avalanche](https://www.avax.network/) exploran variantes arquitectónicas propias para lograr alta escalabilidad.

En el ecosistema de Ethereum, la estrategia se orienta hacia soluciones modulares de capa 2: [MegaEth](https://www.megaeth.com/) busca velocidad extrema como infraestructura especializada, [OP Stack](https://stack.optimism.io/) construye una red estandarizada de rollups interoperables (Superchain), y [zkStack](https://zkstack.io/) aprovecha pruebas de validez para escalar con mayor seguridad criptográfica. [Celestia](https://celestia.org/) actúa como capa 0 modular que puede soportar múltiples soluciones de escalabilidad.

La competencia no solo está en el rendimiento bruto, sino en la combinación de descentralización, seguridad, escalabilidad y experiencia de usuario que cada enfoque pueda ofrecer al desarrollador y al usuario final. Al igual que con las appchains, construir o mantener estas soluciones de ultra-alto rendimiento representa un desafío técnico considerable, y la mayoría de desarrolladores encontrarán suficiente escalabilidad en las soluciones L1 y L2 ya consolidadas sin necesidad de operar infraestructura propia de este nivel.

#### Seguridad compartida: restaking con EigenLayer

Como mencionamos anteriormente en la sección de appchains, uno de los desafíos clave del ecosistema es la fragmentación de la seguridad: cada nueva red, servicio o protocolo tradicionalmente necesita construir su propio conjunto de validadores, lo que diluye la seguridad global y aumenta los costes de arranque. Este problema es especialmente relevante para oráculos, puentes (bridges), redes de disponibilidad de datos y appchains que requieren garantías de seguridad robustas pero no tienen recursos para competir con redes establecidas.

En respuesta a este desafío, surge el concepto de **seguridad compartida mediante restaking**, un mecanismo que permite reutilizar la seguridad económica ya comprometida en Ethereum para proteger múltiples servicios y aplicaciones del ecosistema simultáneamente. [EigenLayer](https://www.eigenlayer.xyz/) es la plataforma principal que implementa este modelo en Ethereum.

**¿Cómo funciona el restaking?**

Los validadores de Ethereum (stakers) que ya han depositado ETH para asegurar la red principal pueden "restakear" esos mismos fondos mediante contratos inteligentes de EigenLayer. Al hacerlo, optan voluntariamente por asumir obligaciones adicionales de validación para otros servicios del ecosistema (llamados "Actively Validated Services" o AVS), como:

- **Oráculos descentralizados**: Servicios que proveen datos del mundo real a contratos inteligentes
- **Puentes cross-chain (bridges)**: Infraestructura para transferir activos entre diferentes blockchains
- **Redes de disponibilidad de datos**: Capas especializadas que garantizan que los datos de rollups estén disponibles
- **Appchains y rollups personalizados**: Redes específicas de aplicaciones que necesitan validación independiente
- **Protocolos de consenso alternativos**: Servicios que requieren validación distribuida

A cambio de este servicio adicional, los validadores reciben recompensas extra de los protocolos que aseguran. Sin embargo, también asumen riesgos adicionales: si no cumplen correctamente con sus obligaciones en los servicios AVS, pueden sufrir penalizaciones económicas (slashing) más allá de las del protocolo Ethereum base.

**Ventajas de la seguridad compartida:**

- Reducción de barreras de entrada: Nuevos protocolos pueden acceder inmediatamente a un alto nivel de seguridad económica sin necesidad de construir su propia red de validadores desde cero
- Mayor eficiencia de capital: El mismo capital (ETH) asegura múltiples servicios simultáneamente, maximizando su utilidad económica
- Reducción de fragmentación: Consolida la seguridad del ecosistema en lugar de dispersarla entre múltiples redes independientes
- Flexibilidad para innovación: Permite experimentar con nuevos servicios y protocolos sin los costes prohibitivos de arrancar una red de validación independiente

**Implicaciones para el ecosistema:**

EigenLayer representa un cambio paradigmático en cómo se estructura la seguridad en Web3. En lugar de que cada servicio compita por validadores y seguridad económica, se crea un mercado de seguridad compartida donde los validadores pueden ofrecer sus servicios a múltiples protocolos. Esto es especialmente relevante para el desarrollo de appchains, que como mencionamos anteriormente, enfrentan desafíos significativos de seguridad y conectividad.

Sin embargo, también introduce nuevos riesgos sistémicos: si muchos validadores restakean en servicios de alto riesgo, una cascada de penalizaciones (slashing) podría afectar la seguridad de Ethereum mismo. Por ello, el diseño cuidadoso de incentivos y límites de exposición es crucial para el éxito de este modelo.

En el contexto de este repositorio `web3-101`, aunque EigenLayer representa una innovación importante, la mayoría de desarrolladores no necesitarán interactuar directamente con estos mecanismos. Es más relevante entender que la seguridad compartida mejora la viabilidad de servicios críticos del ecosistema (como oráculos confiables y puentes más seguros) que sí utilizarás al construir aplicaciones descentralizadas.

#### Orientado a la interoperabilidad: capas de mensajería cross-chain

Las capas de mensajería cross-chain representan un intento de mejorar la interoperabilidad blockchain frente a los puentes tradicionales (bridges), aunque **no resuelven completamente los problemas de seguridad** inherentes a la comunicación entre cadenas independientes. A diferencia de los bridges, que típicamente mantienen activos bloqueados en contratos inteligentes de una cadena mientras emiten representaciones envueltas en otra (creando puntos de fallo centralizados), las capas de mensajería facilitan la **comunicación de datos y la ejecución de lógica entre diferentes blockchains** sin custodiar activos directamente.

Es fundamental aclarar que estas soluciones **no son atomic swaps verdaderos**: no garantizan que las operaciones en ambas cadenas se ejecuten de forma atómica (todo o nada) sin depender de intermediarios o supuestos de confianza adicionales. La atomicidad real requeriría que ambas blockchains compartan el mismo contexto de consenso, algo imposible entre redes independientes. Por tanto, las capas de mensajería introducen sus propios vectores de ataque y dependencias de confianza, aunque de naturaleza diferente a los bridges tradicionales.

Este enfoque permite casos de uso más amplios que la simple transferencia de tokens: desde la sincronización de estados entre cadenas, la ejecución de contratos multi-cadena, hasta la construcción de aplicaciones descentralizadas que operan simultáneamente en múltiples ecosistemas blockchain. Las capas de mensajería funcionan mediante servicios off-chain que monitorizan eventos en múltiples blockchains (pulling) y publican mensajes verificados en contratos inteligentes de las cadenas de destino (pushing), donde otros contratos pueden acceder a esta información cross-chain de forma determinista.

Estas soluciones emplean diversas arquitecturas (validadores independientes, redes oracle descentralizadas, light clients o protocolos nativos en ecosistemas modulares como IBC en Cosmos), con ejemplos como [LayerZero](https://layerzero.network/), [Chainlink CCIP](https://chain.link/cross-chain) y [Wormhole](https://wormhole.com/). Todos estos protocolos dependen de servicios intermedios off-chain que verifican y transmiten mensajes entre cadenas, integrándose a través de contratos inteligentes en cada blockchain participante.

> **Diferencia clave con bridges:** Los bridges tradicionales transfieren activos bloqueándolos en una cadena y acuñando representaciones en otra (lock-and-mint), creando riesgos de custodia centralizada. Las capas de mensajería transmiten datos y comandos entre cadenas sin custodiar activos directamente, aunque igualmente dependen de validadores o mecanismos intermedios, por lo que no eliminan los riesgos fundamentales de la interoperabilidad cross-chain.

**Casos de uso y ventajas:**

Las capas de mensajería cross-chain permiten casos de uso avanzados que van más allá de la simple transferencia de activos:

- Aplicaciones multi-cadena (omnichain): DApps que operan simultáneamente en múltiples blockchains, sincronizando estados y liquidez entre ellas sin fragmentar la experiencia de usuario.
- Lending y DeFi cross-chain: Protocolos que permiten depositar colateral en una cadena y obtener préstamos en otra, aprovechando liquidez distribuida.
- Gobernanza cross-chain: DAOs que pueden ejecutar decisiones y controlar activos en múltiples redes desde un único sistema de gobernanza.
- NFTs interoperables: Tokens no fungibles que pueden moverse entre diferentes ecosistemas manteniendo su unicidad y propiedades.
- Agregación de liquidez: Aplicaciones que consolidan liquidez desde múltiples DEXs en diferentes cadenas para optimizar ejecución de trades.

**Riesgos y limitaciones fundamentales:**

Las capas de mensajería cross-chain **no eliminan los riesgos fundamentales de la interoperabilidad entre cadenas independientes**. Los problemas principales incluyen: imposibilidad de atomicidad real sin terceros de confianza, dependencia de validadores externos que pueden comprometerse, ventanas de vulnerabilidad durante la finalidad asíncrona entre cadenas, alta complejidad técnica que multiplica puntos de fallo, latencia y costes elevados, fragmentación de estándares incompatibles, y riesgo de censura por validadores centralizados.

**Importante**: Los mayores hackeos en Web3 (miles de millones de dólares en pérdidas) han ocurrido precisamente en soluciones de interoperabilidad. La interoperabilidad cross-chain sigue siendo el eslabón más débil de la infraestructura Web3.

**Relevancia en el ecosistema:**

Las capas de mensajería cross-chain representan un área de innovación activa en Web3, pero **deben usarse con extrema precaución**. La visión de un ecosistema verdaderamente interoperable sigue siendo más aspiracional que real: la interoperabilidad segura entre blockchains independientes enfrenta limitaciones fundamentales de diseño que ninguna solución técnica ha resuelto completamente.

La alternativa más segura sigue siendo la **interoperabilidad nativa dentro de ecosistemas que comparten infraestructura común**, como Superchain (OP Stack), Elastic Chain (ZK Stack) o AggLayer (Polygon CDK), donde las cadenas comparten seguridad, estándares y mecanismos de verificación desde el diseño, reduciendo drásticamente los vectores de ataque.

#### El ecosistema Ethereum de capas en construcción 🚧

Ante la amplitud del ecosistema blockchain y la complejidad de las soluciones disponibles, existe una visión más pragmática centrada en el ecosistema de Ethereum con capas 2 que comparten el mismo stack tecnológico, lo que se conoce como ecosistemas L2 intra-stack. Aunque este modelo está todavía en construcción y requiere acuerdos entre diferentes actores, representa un enfoque más centrado, seguro y sensato, al menos en mi opinión.

Si pensamos en soluciones de interoperabilidad en Ethereum, la red no se destaca por ofrecer una interoperabilidad amplia entre diferentes tipos de redes de capa 2. En la práctica, la aproximación predominante es conectar ecosistemas L2 que comparten el mismo stack tecnológico. Por ejemplo, [Optimism](https://optimism.io/) y [Base](https://base.org/) pueden comunicarse de forma nativa porque ambos se construyen con [OP Stack](https://stack.optimism.io/), el framework tecnológico que permite crear rollups interoperables formando [Superchain](https://docs.optimism.io/superchain/superchain-explainer), la red de rollups interconectados del ecosistema OP Stack. De manera similar, [ZkSync](https://zksync.io/) impulsa la [Elastic Chain](https://launchpad.ripio.com/blog/elastic-chain-la-nueva-era-de-la-interoperabilidad-en-blockchain) para rollups creados con [ZK Stack](https://zkstack.io/), y [Polygon](https://polygon.technology/) desarrolla [AggLayer](https://www.agglayer.dev/) para conectar las soluciones basadas en su [CDK (Chain Development Kit)](https://polygon.technology/polygon-cdk/). Estos modelos permiten que los rollups construidos con la misma infraestructura se comuniquen y compartan liquidez de forma nativa. Lo cierto es que la interoperabilidad entre diferentes stacks o arquitecturas L2 sigue siendo un reto pendiente.

> Vamos a aclarar el concepto de Superchain porque es complejo: no es una red nueva, sino una red lógica o superpuesta formada por el conjunto de redes que usan el mismo stack, compuesta por los nodos de redes como Optimism, Base, etc. Sobre esos nodos se define una ‘nueva red’ orientada a funciones de interoperabilidad. Es como darle a los nodos no solo el doble rol clásico de cliente y servidor, sino un tercero más: cliente, servidor y participante del protocolo Superchain.

La organización Ethereum incentiva y mantiene en su hoja de ruta el desarrollo de un ecosistema capaz de alcanzar en conjunción con el resto de capas un rendimiento superior a 100.000 TPS y latencias cercanas a 10 ms, con el objetivo de soportar volúmenes de transacciones similares a la Web2. En este objetivo, conocido en la hoja de ruta como "The Surge", soluciones como [MegaEth](https://www.megaeth.com/) juegan un papel de infraestructura especializada en ultra-alto rendimiento, no como parte de un ecosistema de rollups interconectados tipo Superchain, sino como una L2 independiente orientada a aplicaciones de alta frecuencia como trading o gaming avanzado.

Este enfoque modular de Ethereum acepta conscientemente ciertos trade-offs: mientras ecosistemas como Superchain priorizan la interoperabilidad nativa entre rollups que comparten el mismo stack, soluciones como MegaEth sacrifican esa interoperabilidad fácil a cambio de rendimiento extremo para casos de uso muy específicos. Ambas visiones coexisten porque no todas las aplicaciones necesitan las mismas características; el ecosistema se beneficia de tener opciones especializadas para diferentes necesidades, todas liquidando finalmente en Ethereum L1.

Para lograrlo, uno de los principales desafíos está en la propia red Ethereum. Esto se aborda mediante la implementación del sharding, que ahora se centra en optimizar la disponibilidad de datos para las soluciones de capa 2 (L2s), en lugar de procesar transacciones directamente. Esta estrategia, conocida como danksharding, permite que las L2s, como los rollups, procesen transacciones en paralelo y luego publiquen los datos en la Capa 1 de forma más eficiente, lo que reduce significativamente las tarifas. Además, la propia Capa 1 está explorando la ejecución de transacciones en paralelo dentro de la EVM para aumentar su propio rendimiento, una iniciativa complementaria al sharding que, en conjunto, ayuda a reducir las tarifas de gas.

Además, Ethereum está integrando tecnologías de Zero-Knowledge Proofs (ZK Proofs) en los validadores de la capa principal, que permiten verificar información sin revelar su contenido, mejorando la escalabilidad, seguridad y privacidad de las transacciones. Este enfoque es crucial para la fase "The Verge", que busca mejorar la verificación de la red utilizando Verkle Trees para hacerla más ligera.

En cuanto a la experiencia de usuario y la seguridad, Ethereum avanza con iniciativas como la abstracción de cuentas y la autenticación reforzada mediante técnicas de conocimiento cero aplicadas a dispositivos móviles, como ZK ID. Estas mejoras forman parte de la fase "The Splurge", que busca pulir la red para garantizar una experiencia fluida y robusta.

La hoja de ruta de Ethereum también incluye fases como "The Scourge", centrada en la resistencia a la censura y la centralización, es decir evitar que grandes validadores o pools de staking bloqueen transacciones, y "The Purge", que busca limpiar el historial de la red para reducir el almacenamiento de datos y hacer los nodos más eficientes a largo plazo.

Este resumen, incompleto y posiblemente con fallos y matices, solo pretende evidenciar que el ecosistema de Ethereum está en plena evolución. El desafío actual es identificar qué arquitectura será la más estable, segura y escalable para una adopción masiva. Aún no está claro si serán [Base](https://base.org/), [OP Stack](https://stack.optimism.io/), [Polygon](https://polygon.technology/) las que lideren el desarrollo de aplicaciones a gran escala. Se perfila que Polygon tiende al sector empresarial, OP Stack a comunidades abiertas, y Base a captar usuarios masivos desde productos Web2. Sin embargo, el ecosistema permanece abierto y en pleno desarrollo, y no hay una respuesta definitiva a día de hoy. Por otra parte [MegaEth](https://www.megaeth.com/) parece que se perfila como una pieza de infraestructura concreta para un mercado gaming y de DeFi de alta frecuencia, no como una plataforma de adopción masiva.

#### IOTA: La red IoT de coste ~0 / ~real-time para el RWA automatizado

Existe una visión alternativa, quizá minoritaria pero coherente, que cuestiona la complejidad creciente del ecosistema blockchain. La coordinación necesaria entre múltiples actores en entornos modulares como Ethereum puede ralentizar la implementación de mejoras, mientras que arquitecturas monolíticas como Solana pueden iterar más rápidamente al tener gobernanza más centralizada. El hecho de que Solana haya logrado métricas de rendimiento competitivas con un enfoque integrado es un recordatorio de que no existe una única solución arquitectónica correcta: hay trade-offs legítimos entre descentralización, velocidad de innovación y experiencia de usuario.

Además, existe un debate conceptual importante: ¿Web3 debe soportar toda la carga transaccional de Web2 desde el inicio, o debe crecer orgánicamente según la adopción real? Según algunos enfoques, la blockchain debería registrar principalmente acuerdos y liquidaciones finales, delegando microtransacciones intermedias a capas superiores o soluciones off-chain. Sin embargo, otros argumentan que la infraestructura debe estar preparada anticipadamente para facilitar la adopción masiva cuando llegue. Ambas visiones tienen mérito y no son necesariamente excluyentes.

Igualmente, se debate si estas mismas redes deben soportar también la tokenización de activos del mundo real ([RWA, Real World Assets](https://academy.bit2me.com/que-son-real-world-assets-rwa/)) en entornos automatizados, donde el volumen de transacciones entre dispositivos puede ser masivo y requerir costes casi nulos. Este caso de uso podría beneficiarse de redes especializadas optimizadas para IoT industrial, donde los requisitos de seguridad y los trade-offs son diferentes a los de aplicaciones orientadas al usuario final y transacciones financieras.

En este ámbito de IoT industrial y RWA automatizado, las implicaciones no son las mismas que en la Web enfocada en usuarios finales y transacciones financieras. Estamos hablando de un mundo donde millones de dispositivos [IoT](https://es.wikipedia.org/wiki/Internet_de_las_cosas), potenciados por la automatización y la inteligencia artificial, necesitan registrar interacciones, estados y transferencias de valor con coste cercano a cero y latencia mínima. En ese contexto surgen requisitos diferentes que las soluciones actuales no satisfacen adecuadamente.

Las soluciones de escalabilidad mencionadas anteriormente, como Solana o incluso las Layer 2 de Ethereum, están optimizadas para el rendimiento en un entorno Web donde la criptoeconomía y los incentivos económicos son fundamentales. Sin embargo, en un entorno industrial IoT donde el coste por transacción debe ser prácticamente nulo, estas soluciones presentan limitaciones estructurales. Solana, aunque rápida, no alcanza el coste cero necesario; las Layer 2, aunque más baratas que Ethereum L1, todavía tienen comisiones que imposibilitan ciertos casos de uso IoT masivos.

Por eso es relevante mencionar a [IOTA](https://www.iota.org/), una red que, a pesar de sus problemas históricos —[vulnerabilidades de seguridad](https://cointelegraph.com/news/iota-founder-confirms-he-will-repay-victims-of-197-million-hack), disputas internas, cambios de orientación, ajustes monetarios y una centralización que intentó superar con [Coordicide](https://eurocoinpay.io/blog/iota-presenta-coordicide-y-se-convierte-en-una-red-100-descentralizada/)— sigue siendo, por sus fundamentos técnicos, la candidata más natural para el ecosistema IoT: arquitectura DAG (Directed Acyclic Graph) sin bloques, ejecución paralela masiva y transacciones sin comisiones.

Hay muchas razones para ser escéptico con IOTA: su historial de problemas, la pérdida de momentum comunitario y su debilitado posicionamiento frente a proyectos con mejor marketing y comunidades más activas. El mercado, hasta ahora, no ha validado su propuesta de valor. Sin embargo, desde una perspectiva técnica y de caso de uso, IOTA representa el enfoque más alineado con las necesidades reales de IoT industrial y RWA automatizado.

Quizás el ecosistema blockchain está explorando simultáneamente múltiples hipótesis arquitectónicas porque aún no sabemos cuáles prevalecerán. La complejidad actual puede ser una fase necesaria de experimentación antes de que emerjan estándares consolidados. Es natural que convivan redes monolíticas optimizadas para experiencia de usuario, arquitecturas modulares priorizando descentralización, y soluciones especializadas para nichos específicos como IoT industrial.

  Lo importante es adoptar un enfoque pragmático: elegir la arquitectura más adecuada según las necesidades reales del proyecto, sin dogmatismos. Para algunos casos de uso, una red monolítica con excelente UX y rendimiento será la elección correcta; para otros, la composabilidad y descentralización de arquitecturas modulares será prioritaria. El tiempo, la adopción real y los casos de uso exitosos —no solo el marketing o la especulación— determinarán qué enfoques prosperan en cada nicho.

#### El enfoque rollup-centric y la elección del stack

El futuro de Ethereum está claro: la visión rollup-centric posiciona a Ethereum L1 como capa de liquidación final (settlement layer), donde se registran acuerdos, transferencias de valor y estados críticos que requieren inmutabilidad y verificabilidad descentralizada. La mayoría de las interacciones y el procesamiento ocurren en las L2 (rollups), que heredan la seguridad de Ethereum mientras ofrecen mayor escalabilidad y menores costes.

Esta arquitectura no favorece un único stack tecnológico, sino un ecosistema diverso de L2 donde cada solución tiene cabida según sus características y caso de uso:

- **OP Stack / Superchain ([Optimism](https://optimism.io/), [Base](https://base.org/)):** Orientado a interoperabilidad nativa entre rollups que comparten el mismo framework. Ideal para aplicaciones que necesitan comunicación fluida entre múltiples cadenas dentro del mismo ecosistema, enfoque comunitario abierto y estándares consolidados. Optimism se ha posicionado como referente en gobernanza descentralizada y desarrollo colaborativo.

- **ZK Stack / Elastic Chain ([ZkSync](https://zksync.io/)):** Rollups con pruebas de validez (ZK proofs) que ofrecen mayor seguridad criptográfica y finalidad más rápida. Adecuado para aplicaciones que priorizan privacidad, verificación instantánea o casos de uso donde la validez matemática es crítica.

- **Polygon CDK / AggLayer ([Polygon](https://polygon.technology/)):** Infraestructura modular con enfoque empresarial y soluciones personalizadas. Fuerte presencia en casos de uso corporativos, gaming y NFTs, con herramientas para crear appchains específicas.

- **L2 especializadas ([MegaEth](https://www.megaeth.com/), [Arbitrum](https://arbitrum.io/), [Starknet](https://www.starknet.io/)):** Soluciones optimizadas para casos de uso específicos como DeFi de alta frecuencia, gaming masivo con miles de transacciones por segundo, o aplicaciones sociales con requisitos de ultra-baja latencia. Estas L2 sacrifican cierta interoperabilidad generalista a cambio de rendimiento extremo en sus nichos.

**El verdadero desafío no es elegir un único stack, sino resolver la interoperabilidad entre todas estas L2.** Mientras las soluciones intra-stack (como Superchain para OP Stack) ofrecen comunicación nativa y segura entre rollups del mismo ecosistema, la interoperabilidad inter-stack —entre L2 de diferentes arquitecturas— sigue siendo el reto pendiente.

Los [puentes tradicionales](https://ethereum.org/en/developers/docs/bridges/) actuales introducen riesgos de seguridad significativos, y las [capas de mensajería cross-chain](https://chain.link/education-hub/cross-chain-bridge) intentan mejorar esto pero aún no resuelven completamente el problema de confianza. Un intercambio atómico verdadero entre L2 independientes requeriría que todas compartan el mismo contexto de consenso, algo prácticamente imposible sin acuerdos fundamentales en el protocolo.

**En la práctica, esto implica que:**

- La mayoría de usuarios y aplicaciones operarán dentro de un ecosistema L2 específico (OP Stack, ZK Stack, etc.) donde la interoperabilidad es nativa y segura.
- Las transferencias entre ecosistemas diferentes seguirán requiriendo puentes o protocolos de mensajería que, inevitablemente, introducen riesgos adicionales de confianza.
- Ethereum L1 actuará como punto de anclaje común: todas las L2 liquidan en L1, lo que permite cierta composabilidad indirecta aunque con mayor latencia y coste.

**Para este repositorio `web3-101-edu-projects` y su laboratorio `web3-101`,** adoptamos [OP Stack](https://stack.optimism.io/) con [Optimism](https://optimism.io/) como red principal de despliegue, aprovechando su interoperabilidad nativa con [Base](https://base.org/) dentro de Superchain. Esta elección responde al enfoque comunitario abierto, la madurez del ecosistema y la visión de descentralización colaborativa que caracteriza a Optimism.

Sin embargo, **esto no significa que otras soluciones sean menos válidas.** Dependiendo de tu caso de uso —gaming, DeFi, privacidad, casos empresariales— otras L2 pueden ser más adecuadas. Lo importante es entender que todas estas soluciones coexisten en el ecosistema rollup-centric de Ethereum, y que la elección del stack debe basarse en requisitos técnicos y objetivos de producto, no en preferencias dogmáticas.

## Almacenamiento distribuido

Como redes de almacenamiento, destacan [IPFS](https://ipfs.tech/), que permite guardar y compartir archivos de forma distribuida y resistente a la censura, y [Filecoin](https://filecoin.io/), que añade una capa de incentivos económicos para asegurar la permanencia de los datos mediante pagos a quienes ofrecen espacio de almacenamiento. También sobresale [Arweave](https://www.arweave.org/), orientada a la preservación permanente de información, donde los datos se almacenan de forma inmutable y accesible a largo plazo gracias a su propio modelo de incentivos.

[Swarm](https://www.ethswarm.org/) merece una mención especial como la solución de almacenamiento distribuido desarrollada específicamente por la Ethereum Foundation. A diferencia de IPFS, que es agnóstico de blockchain, Swarm está diseñado nativamente para el ecosistema Ethereum, ofreciendo almacenamiento descentralizado con incentivos económicos mediante tokens BZZ. Su principal ventaja radica en la integración profunda con DApps de Ethereum, permitiendo hosting completo de aplicaciones descentralizadas (incluyendo HTML, CSS, JavaScript y metadatos) con direccionamiento nativo desde contratos inteligentes. Aunque su adopción ha sido más lenta comparada con IPFS, representa la visión más integrada de almacenamiento para el ecosistema Ethereum.

## Oráculos

Los oráculos son servicios que conectan las blockchains con el mundo exterior, proporcionando datos del mundo real a los contratos inteligentes. Los contratos inteligentes en la EVM no pueden iniciar conexiones de red hacia el exterior por sí mismos, por lo que requieren mecanismos externos que traigan la información hacia la blockchain. Los oráculos funcionan mediante servicios off-chain que obtienen datos del mundo real (pulling) y los publican en contratos inteligentes on-chain (pushing), donde otros contratos pueden acceder a esta información de forma determinista y verificable.

[Chainlink](https://chain.link/) es la red de oráculos descentralizada más consolidada, ofreciendo feeds de precios, generación de números aleatorios verificables (VRF), automatización de tareas (Automation) y, como vimos anteriormente, soluciones de interoperabilidad cross-chain (CCIP). Su arquitectura descentralizada reduce el riesgo de manipulación mediante múltiples fuentes de datos independientes.

Otros proyectos relevantes incluyen [API3](https://api3.org/), que permite a proveedores de APIs ofrecer datos directamente a contratos inteligentes sin intermediarios, y [Pyth Network](https://pyth.network/), especializada en datos financieros de alta frecuencia. [UMA](https://uma.xyz/) ofrece un enfoque diferente basado en resolución de disputas optimista para oráculos de datos arbitrarios.

Los oráculos representan uno de los puntos críticos de seguridad en Web3, ya que un oráculo comprometido puede manipular datos y provocar pérdidas millonarias en protocolos DeFi que dependen de esa información. Por ello, la descentralización y los mecanismos de verificación son fundamentales en cualquier solución de oráculos robusta.

### Price Feeds

Los price feeds proporcionan datos de precios de activos del mundo real a contratos inteligentes, siendo esenciales para protocolos DeFi que necesitan valorar colaterales, ejecutar liquidaciones o calcular conversiones de tokens. El patrón técnico consiste en obtener datos off-chain y publicarlos on-chain mediante firmas criptográficas verificables. Múltiples nodos independientes obtienen precios de diversas fuentes (exchanges, DEXs), agregan los valores (típicamente mediante mediana para resistir outliers) y publican el resultado firmado en contratos on-chain.

Chainlink representa el estándar de facto, utilizando redes de oráculos descentralizadas (Decentralized Oracle Networks) donde los nodos recuperan datos de múltiples fuentes y los publican on-chain. Pyth Network, por otro lado, está optimizado para datos de alta frecuencia, conectándose directamente con proveedores institucionales, lo que es ideal para aplicaciones de trading. Redstone implementa un modelo "push" eficiente en gas, donde los datos se incluyen en las transacciones del usuario solo cuando son necesarios, reduciendo costes.

### Verifiable Randomness (VRF)

La generación de números aleatorios verificables on-chain es crítica para aplicaciones que requieren aleatoriedad demostrable, como loterías, sorteos de NFTs o juegos. El patrón técnico (Verifiable Random Function o VRF) consiste en que el oráculo genera un número aleatorio off-chain junto con una prueba criptográfica que demuestra que fue generado correctamente, garantizando que no es predecible ni manipulable.

Chainlink VRF es el estándar más usado, empleado en proyectos como loterías y acuñaciones de NFTs para garantizar la aleatoriedad. Como alternativa, API3 QRNG utiliza aleatoriedad cuántica (Quantum Randomness) proporcionada por la Australian National University, ofreciendo una fuente de aleatoriedad física verdadera.

### Automation (Keepers)

Los contratos inteligentes no pueden ejecutarse automáticamente; necesitan transacciones externas que activen sus funciones. Los servicios de automatización monitorizan condiciones predefinidas y ejecutan funciones cuando se cumplen. Estos nodos off-chain (keepers) reciben una compensación por el servicio y el gas consumido.

Chainlink Automation (antes Keepers) es una red descentralizada de nodos que compiten por ejecutar tareas automatizadas, usada para liquidaciones en protocolos de lending o rebalanceo de vaults. Gelato Network ofrece un "Relay-as-a-Service" que, además de automatización, facilita meta-transactions, permitiendo a los usuarios interactuar con DApps sin necesidad de tener ETH para el gas.

### Proof of Reserves

La prueba de reservas (Proof of Reserves o PoR) verifica que activos tokenizados (como wrapped tokens o stablecoins) están respaldados por reservas reales off-chain, lo cual es fundamental para la transparencia. El patrón consiste en que los oráculos auditan balances en cuentas bancarias o wallets de custodia y publican pruebas criptográficas on-chain.

Chainlink PoR audita y publica las reservas que respaldan activos como WBTC o algunas stablecoins, permitiendo que los protocolos DeFi verifiquen automáticamente que el colateral que aceptan está realmente respaldado.

## VI. PROTOCOLOS DE INTEROPERABILIDAD

La interoperabilidad entre diferentes blockchains es uno de los mayores desafíos de Web3. Permite la transferencia de activos y datos entre redes, pero también es el punto más vulnerable de la infraestructura, concentrando la mayoría de los hackeos.

### 1. Bridges

Los puentes o bridges facilitan la transferencia de activos entre blockchains, pero sus arquitecturas implican diferentes riesgos.

**Lock-and-Mint:**

Este patrón bloquea activos en la cadena de origen y acuña una representación "envuelta" (wrapped) en la de destino. El riesgo es que el bridge actúa como custodio, y si es comprometido, los fondos pueden ser robados. Ejemplos como Wormhole y el ya desaparecido Multichain han sufrido hackeos millonarios por esta vulnerabilidad.

**Burn-and-Mint:**

Quema el activo en el origen y acuña una versión nativa en el destino, evitando la custodia directa. Sin embargo, requiere confianza en los validadores que certifican la operación. El Polygon PoS Bridge (para MATIC) y el CCTP de Circle (para USDC) usan este modelo.

**Liquidity Networks:**

Utiliza pools de liquidez en ambas cadenas para realizar swaps atómicos, sin custodia centralizada. Es un modelo no custodial y rápido, implementado por protocolos como Connext, Hop Protocol y Across. El riesgo se distribuye entre los proveedores de liquidez.

**Optimistic Bridges:**

Asume que las transferencias son válidas por defecto, pero permite un período de disputa (generalmente 7 días) para presentar pruebas de fraude. Este retraso en la retirada (withdrawal delay) es su principal inconveniente. El bridge nativo de Optimism y Across Protocol son ejemplos de este enfoque.

### 2. Cross-Chain Messaging

Estos protocolos permiten una comunicación más generalizada entre cadenas, no solo de activos, sino de datos y comandos.

**Generalized Message Passing:**

Permite enviar mensajes arbitrarios para ejecutar funciones en otras cadenas. LayerZero lo hace combinando "Ultra Light Nodes" con oráculos y relayers, asumiendo que no coluden entre sí. Axelar utiliza su propio conjunto de validadores en Proof-of-Stake para retransmitir mensajes, centralizando la confianza en su red. Hyperlane ofrece un enfoque modular que permite a cada aplicación definir su propia configuración de seguridad.

## Comunicación descentralizada

La comunicación descentralizada constituye una pieza fundamental para la infraestructura Web3, permitiendo que las aplicaciones intercambien información sin depender de servidores centralizados. Estas soluciones son especialmente relevantes para DApps que requieren mensajería en tiempo real, notificaciones, coordinación entre usuarios o comunicación off-chain que complementa las transacciones on-chain.

[Whisper](https://github.com/ethereum/whisper), desarrollado por la Ethereum Foundation, fue uno de los primeros protocolos diseñados específicamente para comunicación peer-to-peer en el ecosistema Ethereum. Whisper permite el intercambio de mensajes cifrados y efímeros entre nodos, con características como privacidad por defecto, resistencia a la censura y integración nativa con DApps. Los mensajes tienen un tiempo de vida limitado (TTL) y no se almacenan permanentemente, priorizando la privacidad y reduciendo la sobrecarga de la red.

[Waku](https://waku.org/), desarrollado por Status como evolución de Whisper, representa la implementación más moderna y eficiente de comunicación descentralizada. Waku mejora significativamente el rendimiento, reduce el consumo de recursos y ofrece mayor escalabilidad mediante una arquitectura modular que separa las funciones de relay, store y filter. Es especialmente adecuado para aplicaciones de mensajería, notificaciones push descentralizadas y coordinación de comunidades, siendo utilizado por aplicaciones como Status y otras DApps que requieren comunicación en tiempo real.

[XMTP (Extensible Message Transport Protocol)](https://xmtp.org/) se enfoca en la mensajería entre direcciones de wallet, permitiendo que los usuarios se comuniquen utilizando sus direcciones Ethereum sin revelar información personal. XMTP está ganando tracción en aplicaciones de Web3 social y comunicación entre usuarios de DeFi, ya que facilita la interacción directa entre participantes del ecosistema sin comprometer la privacidad.

Otras soluciones incluyen [Matrix](https://matrix.org/) como protocolo de comunicación federado que, aunque no es específico de blockchain, se integra cada vez más con aplicaciones Web3 para proporcionar comunicación descentralizada y resistente a la censura. [Gun.js](https://gun.eco/) ofrece una base de datos descentralizada en tiempo real que puede usarse para construir aplicaciones de comunicación peer-to-peer.

La comunicación descentralizada es crucial para la adopción masiva de Web3, ya que permite crear experiencias de usuario completas sin depender de infraestructura centralizada. Sin embargo, estos protocolos enfrentan desafíos en escalabilidad, latencia y experiencia de usuario comparados con soluciones centralizadas. Para la mayoría de proyectos en fase inicial, es recomendable evaluar si realmente necesitan comunicación totalmente descentralizada o si pueden beneficiarse de soluciones híbridas que combinen eficiencia centralizada con verificabilidad descentralizada.

## Servicios

El ecosistema Web3 incluye una gran variedad de servicios tipos SaaS, servicios centralizados o no o aplicaciones descentralizadas DApps con enfoque B2B que se han convertido en estándar (Gnosis Safe, Dune Analytics, ENS, WalletConnect).

Hablar de servicios, es considerar una lista interminable, por lo tanto, en lugar de hacer una introduccion explicativa larga, y puesto que el objeto de este canal es emprender una solucion web, te emplazo a leer para mas detalle la [sección de servicios del repositorio](../infrastructure/services/about.md) para una mejor explicación.

## Herramientas de desarrollo o stack tecnológico

El ecosistema Web3 incluye una gran variedad de herramientas y stack tecnologico para desarrollar una DApp.

Tienes que considerar que antes de iniciar un proyecto, debes tomar decisiones de diseño, en algunas casos las normales para un nuevo producto, pero en el caso de Web3, tienes la nueva dimension de asegurar la descentralizacion, la sostenibilidad economica y la particioacion comunitaria en una DAO, por eso te aplazo a ir a la [sección de lanzamiento de un proyecto y tokenomic](../project-launch-and-tokenomics/about.md).

Igualmente sobre las herramientas y el stack tecnologico, he creado un repositorio para aprender jugando, el cual te emplazo a ir para ver al respecto: <https://github.com/open3diy/web3-101-dapp-playground>.

## DePIN: Infraestructura física descentralizada

La Infraestructura Física Descentralizada (DePIN, Decentralized Physical Infrastructure Networks) representa una evolución del paradigma blockchain hacia el mundo físico, permitiendo la coordinación y monetización de recursos tangibles mediante incentivos tokenizados. A diferencia de las aplicaciones puramente digitales, DePIN conecta hardware real (sensores, servidores, antenas, dispositivos de almacenamiento) con protocolos descentralizados que recompensan a los operadores por proporcionar servicios.

El modelo DePIN invierte la lógica de infraestructura tradicional: en lugar de que una empresa centralizada invierta capital masivo para desplegar redes físicas, permite que individuos y pequeños operadores aporten recursos de forma distribuida, recibiendo tokens como compensación. Esto reduce barreras de entrada, democratiza el acceso a infraestructura y crea redes más resilientes y resistentes a la censura.

**Categorías principales de DePIN:**

- Redes inalámbricas descentralizadas: [Helium](https://www.helium.com/) permite desplegar redes IoT y 5G mediante hotspots operados por individuos que reciben tokens por proporcionar cobertura. Aunque ha enfrentado críticas por su modelo económico y adopción real, representa el caso de uso más visible de DePIN.

- Computación descentralizada: [Akash Network](https://akash.network/) ofrece cloud computing mediante un mercado descentralizado donde proveedores compiten por ofrecer capacidad de cómputo. [Render Network](https://rendernetwork.com/) especializa este modelo en renderizado GPU para creadores de contenido 3D.

- Almacenamiento descentralizado: Más allá de IPFS y Filecoin mencionados anteriormente, proyectos como [Storj](https://www.storj.io/) ofrecen almacenamiento en la nube distribuido con cifrado nativo.

- Energía y sostenibilidad: Redes emergentes exploran la tokenización de recursos energéticos renovables y certificados de carbono mediante DePIN.

- Sensores y datos geoespaciales: Proyectos como [DIMO](https://dimo.zone/) (datos de vehículos) o [Hivemapper](https://hivemapper.com/) (mapas descentralizados) recompensan a usuarios por aportar datos del mundo real.

**Desafíos y consideraciones:**

Aunque DePIN ofrece una propuesta conceptualmente atractiva, enfrenta retos significativos: la mayoría de proyectos luchan por alcanzar masa crítica de oferta y demanda real (más allá de especuladores de tokens), los modelos económicos suelen ser insostenibles a largo plazo, y la calidad de servicio puede ser inconsistente comparada con proveedores centralizados. Además, la regulación de servicios físicos tokenizados sigue siendo incierta en muchas jurisdicciones.

Para proyectos en fase inicial, DePIN representa más una oportunidad de futuro que una solución inmediata. Es relevante conocer el concepto y su potencial, pero la mayoría de desarrolladores se beneficiarán más de enfocarse en aplicaciones que aprovechen la infraestructura descentralizada existente (almacenamiento, oráculos, computación) antes de intentar construir nuevas redes DePIN, que requieren coordinación masiva, inversión en hardware y retos de adopción considerables.

---
