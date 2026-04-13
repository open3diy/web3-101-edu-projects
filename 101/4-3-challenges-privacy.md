# Privacidad en blockchain: transparencia como fortaleza y la necesidad de privacidad selectiva

Cuando hablamos de blockchain y Web3, la privacidad suele presentarse como un problema a resolver. Sin embargo, esta perspectiva puede ser engañosa. La transparencia de blockchain no es un defecto de diseño, sino una característica fundamental que habilita casos de uso únicos e imposibles en sistemas tradicionales.

Blockchain representa el sistema de reputación más transparente que existe. Cada acción, cada transacción, cada interacción queda registrada públicamente de forma inmutable y verificable. Esta transparencia radical es precisamente lo que permite construir confianza sin intermediarios, auditar protocolos de forma independiente y crear sistemas verdaderamente descentralizados.

Sin embargo, esta misma transparencia plantea desafíos legítimos en contextos donde la confidencialidad es necesaria. No todos los casos de uso requieren o se benefician de la exposición pública total. El reto está en entender cuándo la transparencia es fortaleza y cuándo es limitación.

## La transparencia como característica, no como limitación

Las blockchains públicas como Bitcoin y Ethereum fueron diseñadas intencionalmente para ser transparentes. Esta decisión responde a una pregunta fundamental: ¿cómo crear un sistema de valor donde nadie tenga que confiar en una autoridad central para verificar que las reglas se cumplan?

La respuesta fue hacer que todo sea público y verificable. Cada bloque, cada transacción, cada cambio de estado puede ser auditado por cualquier participante de la red. Esto elimina la necesidad de confiar en intermediarios porque cualquiera puede verificar directamente la validez de las operaciones. Este principio se conoce como [transparencia radical](https://en.wikipedia.org/wiki/Radical_transparency) y es fundamental para entender cómo funcionan los sistemas descentralizados.

En el contexto del [trilema de la blockchain](./4-1-challenges-the-trilemma-modular-solution.md), la transparencia está profundamente vinculada con la descentralización y la seguridad. Un sistema donde cualquiera puede verificar el estado completo de la red es más resistente a la censura y más difícil de manipular que uno donde la información está restringida a ciertos participantes privilegiados.

Esta transparencia habilita casos de uso que serían imposibles en sistemas tradicionales:

En el ecosistema [DeFi](https://ethereum.org/es/defi/), los contratos inteligentes son auditables públicamente, las reglas de los protocolos son transparentes, y cualquier interacción puede ser verificada. Esto genera confianza sin necesidad de intermediarios y permite la composabilidad que caracteriza a Web3.

En sistemas de reputación y gobernanza, la transparencia permite verificar trayectorias, contribuciones y comportamientos de forma objetiva. Puedes demostrar tu historial de participación en DAOs, tus contribuciones a proyectos open source mediante NFTs de asistencia a eventos ([POAPs](https://poap.xyz/)), credenciales no transferibles vinculadas a tu wallet ([Soulbound Tokens o SBTs](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763)), o attestations verificables on-chain emitidas por terceros ([EAS](https://attest.org/)), todo ello sin depender de instituciones centralizadas que certifiquen tu identidad.

En auditorías y cumplimiento regulatorio, la transparencia facilita que proyectos demuestren públicamente que cumplen con reglas establecidas, que fondos están respaldados adecuadamente, o que operaciones son legítimas sin requerir intermediarios de confianza.

Es importante reconocer que muchas plataformas digitales exitosas operan con transparencia similar sin que esto se perciba como problema. Twitter/X publica todos los mensajes públicamente, GitHub expone todo el código y contribuciones, y nadie considera esto una carencia de privacidad, sino una característica que habilita la colaboración abierta y la construcción de reputación verificable.

## Cuándo la transparencia se convierte en limitación

Si bien la transparencia es fortaleza en muchos contextos, existen situaciones legítimas donde la confidencialidad es necesaria. Esta misma transparencia plantea un desafío para la adopción masiva, ya que expone datos sensibles. Por ello, investigaciones recientes como [Blockchain Privacy and Regulatory Compliance](https://www.sciencedirect.com/science/article/pii/S2096720923000519) proponen sistemas de privacidad verificable que permiten cumplir con las leyes sin renunciar a la seguridad del sistema.

El problema fundamental radica en que blockchain ofrece pseudonimato, no anonimato verdadero. Aunque utilizamos direcciones alfanuméricas en lugar de nombres reales, ese identificador es persistente y todas las transacciones quedan registradas públicamente y vinculadas a él de forma permanente e inmutable.

Esto permite realizar análisis de cadena cada vez más sofisticados. Empresas especializadas en análisis blockchain pueden rastrear el flujo de fondos entre direcciones, identificar patrones de comportamiento característicos, vincular múltiples direcciones que probablemente pertenecen al mismo usuario, y correlacionar actividad on-chain con información off-chain (exchanges, direcciones IP, etc.).

Incluso sin revelar tu identidad real, usar la misma dirección en múltiples servicios crea un perfil de correlación. Cada interacción con un protocolo DeFi, cada NFT que compras, cada DAO en la que votas, queda registrada bajo el mismo identificador. La combinación de estos datos forma un perfil de comportamiento detallado: qué tipo de usuario eres, qué capital manejas, en qué horarios operas, qué estrategias utilizas. Este perfil es legible para cualquiera que consulte la cadena, sin necesidad de conocer tu nombre.

Cuando tu dirección se vincula con tu identidad real, por ejemplo al usar un exchange centralizado que requiere KYC, todo tu historial de transacciones queda expuesto. No solo las operaciones actuales, sino todas las operaciones pasadas y futuras asociadas a esa dirección.

Como argumenta [Vitalik Buterin](https://vitalik.eth.limo/general/2025/04/14/privacy.html), la falta de privacidad crea desequilibrios de poder peligrosos. Si toda tu actividad económica es pública, te vuelves vulnerable a discriminación de precios (vendedores que ajustan precios según tu historial), vigilancia corporativa (empresas que construyen perfiles detallados de tus hábitos), riesgos de seguridad física (conocer tu patrimonio te hace objetivo de ataques), censura financiera (servicios que te bloquean basándose en tus transacciones pasadas), y manipulación comercial (competidores que analizan tu actividad para obtener ventajas estratégicas).

Para empresas, publicar toda la actividad comercial expone estrategias, proveedores, márgenes y clientes a competidores. No se trata de ocultar actividades ilícitas, sino de proteger información sensible en contextos donde la exposición pública genera riesgos reales.

Es fundamental diferenciar entre contextos públicos donde la transparencia es deseable (gobernanza, reputación, auditoría de fondos públicos) y contextos privados donde la confidencialidad es legítima (pagos personales, información médica, estrategias comerciales sensibles).

## Identidad y atributos privados: DIDs y VCs

Cuando hablamos de privacidad, es posible que pensemos no solo en saldos o movimientos, sino en nuestros atributos personales como edad, identificadores o nombres legales, pero en realidad Web3 y Ethereum ya han resuelto esto: las wallets de identidad basadas en [Decentralized Identifiers (DIDs)](https://www.w3.org/TR/did-core/) y [Verifiable Credentials (VCs)](https://www.w3.org/TR/vc-data-model/), estándares formalizados por el W3C.

En este modelo, tú controlas una wallet de identidad que almacena credenciales emitidas por terceros: una institución educativa que certifica tu título, un gobierno que avala tu mayoría de edad, o una organización que acredita tu membresía. Cuando necesitas demostrar un atributo ante un servicio, no lo revelas directamente. En su lugar, puedes combinar estas credenciales con ZK Proofs para demostrar únicamente lo que necesitas. Por ejemplo, probar que eres mayor de edad sin revelar tu fecha de nacimiento exacta, o demostrar que perteneces a cierto grupo sin revelar tu identidad completa.

Sin embargo, es importante entender los límites de este enfoque. Los DIDs y las VCs resuelven el problema de la identidad y los atributos off-chain: quién eres, qué credenciales tienes, qué afirmaciones puedes demostrar sobre ti mismo. Lo que no resuelven es el problema de la transparencia on-chain que hemos descrito a lo largo de este capítulo y es realmente el problema a resolver en Web3.

Si usas Privado ID para demostrar de forma privada que cumples ciertos requisitos para acceder a un protocolo DeFi, habrás protegido tu identidad en ese paso concreto. Pero todas las transacciones que realices después en ese protocolo seguirán siendo públicas y rastreables. El historial de actividad on-chain de tu wallet, los volúmenes que mueves, las estrategias que ejecutas, los contratos con los que interactúas: nada de eso queda oculto por el hecho de haber autenticado tu identidad de forma privada. Y sobre todo no queda oculto si pueden correlacionar off-chain algún atributo de estos con tu dirección.

La distinción es fundamental: los sistemas de identidad descentralizada con privacidad resuelven "quién eres sin revelarlo", pero no resuelven "qué haces sin que se vea". Son soluciones complementarias que operan en capas diferentes. Si tu preocupación principal es que nadie sepa que estás moviendo cierta cantidad de fondos o interactuando con ciertos contratos, un sistema de credenciales privadas no te ayuda en ese aspecto.

## Privacidad selectiva: la solución práctica

La estrategia más pragmática no es hacer que blockchain sea privada por defecto, sino proporcionar herramientas para privacidad selectiva según el contexto. En la práctica, los usuarios pueden gestionar su privacidad mediante una estrategia simple: usar diferentes wallets para diferentes propósitos.

Una wallet principal que vinculas conscientemente con tu identidad real, útil para participación en gobernanza, contribuciones open source y construcción de reputación verificable. Esta dirección se beneficia de la transparencia porque te permite demostrar trayectoria y generar confianza pública.

Otras wallets que mantienes sin vincular con tu identidad pública, reservadas para transacciones personales, experimentación o actividades donde prefieres no exponerte. Al mantener estas direcciones separadas y evitar transacciones entre ellas, dificultas el análisis que podría correlacionarlas.

Esta separación de contextos es similar a cómo usamos redes sociales: puedes tener un perfil profesional público en LinkedIn y conversaciones privadas en mensajería. Ambos modos coexisten según las necesidades de cada situación.

## El avance hacia herramientas de privacidad en Ethereum

Si la privacidad selectiva usando diferentes cuentas no nos gusta evidentemente porque dispersa nuestra identidad, podemos estar tranquilos en parte, porque el ecosistema Ethereum trabaja activamente en desarrollar herramientas que permitan privacidad selectiva donde sea necesaria en nuestra cuenta, sin comprometer la transparencia verificable que caracteriza al sistema. No se trata de abandonar la transparencia, sino de añadir opciones de confidencialidad para casos de uso que lo requieran.

La [Ethereum Foundation](https://ethereum.foundation/) ha lanzado el [Privacy Stewards of Ethereum (PSE)](https://pse.dev/), un equipo dedicado a investigar y desarrollar tecnologías de privacidad. Este grupo coordina investigación en criptografía avanzada, stealth addresses (direcciones sigilosas), herramientas de identidad preservando privacidad y sistemas de pagos privados.

Sin embargo, estas tecnologías aún están en desarrollo y [no ofrecen anonimato completo](https://arxiv.org/abs/2308.01703). Los análisis académicos muestran que las implementaciones actuales de stealth addresses pueden ser vulnerables a ataques de correlación bajo ciertas condiciones. La investigación continúa para fortalecer estas garantías.

Existe una [hoja de ruta de privacidad para Ethereum](https://ethereum-magicians.org/t/a-maximally-simple-l1-privacy-roadmap/23459) que describe mejoras incrementales: privacidad de pagos mediante pruebas de conocimiento cero, anonimización parcial de direcciones, privacidad en el nivel de red para proteger metadatos de transacciones, y mecanismos para que los usuarios puedan controlar qué información revelan.

La estrategia no es hacer que todo sea privado por defecto, sino proporcionar herramientas para que los usuarios y aplicaciones puedan elegir el nivel de privacidad apropiado según sus necesidades. Esto permite mantener la transparencia verificable donde es necesaria (por ejemplo, en auditorías de contratos DeFi) mientras se protege la confidencialidad donde importa (como en pagos personales).

**Tecnologías de privacidad: ZK Proofs y más allá**:

Tenemos que aclarar que las tecnologías de ZK Proofs son tanto herramientas de privacidad como de escalabilidad y depende del contexto entenderás como tal. La tecnología de pruebas de conocimiento cero (Zero-Knowledge Proofs o ZK Proofs) son pruebas criptográficas que permiten demostrar que una afirmación es verdadera sin revelar la información subyacente que la sustenta. Es eso, no implica privacidad en el diseño.

Al respecto existen dos líneas principales en Ethereum:

Redes de capa 2 orientadas a privacidad usando ZK como [Aztec Network](https://aztec.network/) están construyendo infraestructura específicamente orientada a este modelo: privacidad programable en contratos inteligentes donde las transacciones son verificables pero opacos sus detalles.

En los **ZK-rollups de escalabilidad** (como [StarkNet](https://www.starknet.io/) o [zkSync](https://zksync.io/), y el zkEVM que la propia Ethereum Foundation tiene en su hoja de ruta), el proof demuestra que un conjunto de transacciones son válidas sin que los nodos tengan que re-ejecutarlas. Esto reduce la carga computacional. Sin embargo, los datos concretos siguen existiendo: o se publican en L1, o viven en la propia L2. En ningún caso desaparecen. El proof comprime la verificación, pero no oculta nada. La actividad sigue siendo completamente legible para quien acceda a esos datos.

## Mixers y privacidad regulada: el caso Tornado Cash

Dentro de las herramientas de privacidad más controvertidas están los mixers o mezcladores. Estos son contratos inteligentes o protocolos que "mezclan" fondos de múltiples usuarios para romper el vínculo trazable entre direcciones de origen y destino.

El funcionamiento es conceptualmente simple: múltiples usuarios depositan fondos en un pool común, y luego pueden retirar esos fondos a direcciones completamente nuevas que no están vinculadas públicamente con sus direcciones originales. La mezcla de fondos dificulta rastrear qué salida corresponde a qué entrada.

[Tornado Cash](https://tornado.cash/) fue el mixer más prominente en Ethereum, utilizando pruebas de conocimiento cero para garantizar que los depósitos y retiros no pudieran correlacionarse. Sin embargo, en agosto de 2022, la Oficina de Control de Activos Extranjeros de EE.UU. (OFAC) [añadió Tornado Cash a su lista de entidades sancionadas](https://home.treasury.gov/news/press-releases/jy0916), prohibiendo a cualquier empresa estadounidense interactuar con él, argumentando que había sido utilizado para lavar fondos robados en hackeos de criptomonedas.

OFAC es la agencia del Departamento del Tesoro estadounidense encargada de administrar sanciones económicas. Añadir direcciones de Tornado Cash a su lista de Specially Designated Nationals (SDN) significa que cualquier empresa estadounidense o que opere con clientes de EE.UU. está legalmente prohibida de procesar transacciones que involucren esas direcciones, bajo riesgo de multas millonarias y cargos criminales. Esta obligación legal de "OFAC compliance" es lo que impulsa a los exchanges centralizados a implementar sistemas agresivos de listas negras y análisis de blockchain.

Esta sanción generó un debate fundamental sobre privacidad y regulación en blockchain. Por un lado, es innegable que herramientas de privacidad pueden ser utilizadas para actividades ilícitas. Por otro lado, las mismas herramientas son necesarias para proteger la privacidad legítima de usuarios honestos en un sistema transparente por diseño.

El caso es especialmente complejo porque Tornado Cash es un contrato inteligente inmutable desplegado en Ethereum, no una empresa o servicio centralizado. ¿Cómo se puede "sancionar" código que no puede ser apagado ni controlado? ¿Es ético criminalizar el desarrollo de herramientas de privacidad porque puedan ser mal utilizadas?

Varios desarrolladores asociados con Tornado Cash fueron [arrestados en diferentes jurisdicciones](https://www.bitdefender.com/en-gb/blog/hotforsecurity/tornado-cash-crypto-mixer-co-founder-sentenced-to-five-years-in-prison), generando preocupación en la comunidad de desarrolladores sobre los riesgos legales de trabajar en tecnologías de privacidad. De forma similar, en abril de 2024 los [fundadores de Samourai Wallet](https://observatorioblockchain.com/ciberseguridad/eeuu-cierra-samourai-wallet-y-detiene-a-sus-fundadores-por-lavado-de-dinero/), una wallet de Bitcoin enfocada en privacidad, fueron arrestados por cargos relacionados con blanqueo de dinero y operación de un negocio de transmisión de dinero sin licencia.

Este patrón de criminalización de desarrolladores de herramientas de privacidad, tanto en Ethereum como en Bitcoin, ilustra la tensión no resuelta entre privacidad individual, transparencia regulatoria y libertad de desarrollo tecnológico. Es un área donde las soluciones técnicas chocan con realidades legales y políticas complejas.

### Listas negras y censura financiera: el problema de las "monedas contaminadas"

La sanción a herramientas de privacidad ha generado otro problema colateral: la proliferación de listas negras en exchanges centralizados (CEX) y la censura financiera basada en análisis de blockchain.

Los CEX utilizan empresas especializadas en análisis de cadena como [Chainalysis](https://www.chainalysis.com/), [Elliptic](https://www.elliptic.co/) o [TRM Labs](https://www.trmlabs.com/) para rastrear y clasificar direcciones según su "riesgo". Estas empresas mantienen listas de direcciones consideradas "contaminadas" porque han interactuado con servicios sancionados, fondos robados, mixers o actividades ilícitas.

El problema es que esta "contaminación" es transitiva. Si recibes fondos de una dirección que previamente interactuó con Tornado Cash (incluso si esa interacción fue legítima), tu dirección puede quedar marcada como "de alto riesgo". Esto genera situaciones donde usuarios honestos sufren consecuencias:

Los exchanges pueden bloquear tus depósitos sin previo aviso, congelar tu cuenta y exigir explicaciones sobre el origen de fondos que recibiste hace meses o años, reportarte a autoridades financieras bajo sospecha de lavado de dinero, o simplemente rechazar tu negocio permanentemente.

Este fenómeno crea un incentivo perverso: mientras más personas usen herramientas de privacidad legítimas, más direcciones quedan "manchadas" en las listas negras, lo que aumenta el riesgo de censura para usuarios ordinarios. La transparencia de blockchain, combinada con análisis automatizado y listas negras, genera un sistema de vigilancia y censura financiera que no existía en el sistema financiero tradicional con la misma escala y permanencia.

> Uno se pregunta si aquí en España o cualquier país, si no podríamos usar dinero que viene de la corrupción o narcotráfico o explotación, tampoco podríamos ingresarlo al banco. Es evidente que sí podemos y es también evidente que es un caso de discriminación más de los sistemas tradicionales.

No hay apelación, no hay debido proceso, y la "culpa por asociación" es automática e inmutable en el historial de la blockchain. Esto representa un riesgo real para la fungibilidad del dinero: no todos los ETH o BTC son iguales si algunos están "manchados" y otros no.

## El estado actual: privacidad parcial y en construcción

Entonces, ¿ofrece Ethereum privacidad hoy? La respuesta honesta es: parcialmente, y depende de qué herramientas utilices.

Por defecto, Ethereum es completamente transparente. Todas las transacciones estándar son públicas y rastreables. Si usas tu wallet de la forma más común, tu actividad es visible para cualquiera.

Existen herramientas y técnicas para mejorar tu privacidad (stealth addresses experimentales, utilizar múltiples wallets, mezclar fondos mediante servicios residuales no sancionados, o operar en redes L2 orientadas a privacidad como [Aztec Network](https://aztec.network/)), pero todas tienen limitaciones, fricción de uso y riesgos regulatorios. No hay una solución integrada, fácil de usar y completamente segura disponible para el usuario promedio.

Para casos de uso empresariales que requieren confidencialidad fuerte, las soluciones actuales suelen ser blockchains privadas o permisionadas (como [Hyperledger Fabric](https://www.hyperledger.org/use/fabric) o [Quorum](https://consensys.net/quorum/)), que sacrifican apertura y descentralización a cambio de control sobre quién puede ver qué información. Estas soluciones no forman parte del ecosistema Web3 público que discutimos en este repositorio.

El [camino hacia la privacidad nativa en Ethereum](https://ethresear.ch/t/ethereum-privacy-the-road-to-self-sovereignty/22115) es largo y requiere cambios profundos en protocolos, estándares y herramientas. La hoja de ruta existe, la investigación avanza, pero no podemos afirmar que la privacidad esté garantizada o resuelta hoy.

## Reflexión: transparencia y privacidad, un nuevo paradigma

Con este panorama, la solución más deseable sería que el equipo [PSE](https://pse.dev/) consiga integrar herramientas de privacidad directamente en el protocolo Ethereum. Es posible navegar en un ecosistema de apps para cada caso de uso, unos con mejor privacidad que otros, por ejemplo usando Aztec para ciertas operaciones. Gracias a la experiencia unificada o Account Abstraction suavizar parte de la experiencia de usuario, no sería necesario navegar entre redes, pero la fragmentación no desaparece del todo. La privacidad nativa a nivel de protocolo eliminaría esa fricción de raíz.

Web3 requiere hoy un nivel de responsabilidad y criterio que no puede esperarse del usuario medio. Es comparable a Linux en sus primeros años: una herramienta poderosa para quien sabe usarla, pero no necesariamente para todos. Quizás no tenga que serlo todavía. Web3 puede entenderse como un espacio donde convivimos entre el mundo tradicional y la cadena, eligiendo deliberadamente qué exponemos y qué no. Para algunos, exponer su actividad económica no solo no es un problema sino una señal de reputación, una forma de demostrar trayectoria verificable, como el developer que expone que gana 50K al año como parte de su reputación. Para otros, la exposición es un riesgo inaceptable y simplemente solo entraran en Web con el patrimonio mínimo que desean exponer.

En todo esto, hay un problema estructural que las soluciones técnicas no pueden resolver por sí solas: cuando los marcos regulatorios obligan a correlacionar direcciones con identidad real, exponen a los usuarios a riesgos que van más allá de la privacidad financiera. Web3 dispone del modelo correcto con DIDs y VCs para gestionar atributos de identidad bajo el control del usuario, pero ese modelo choca de frente con regulaciones ineptas que exigen identificación directa. El resultado es que la puerta que la tecnología cierra, la legislación la vuelve a abrir para delincuentes. Problemas que exponemos en [el desafio de la integración off-chain](4-4-challenges-off-chain-integration.md).

La discriminación basada en perfil económico es otro ángulo del problema. En un sistema donde toda la actividad es pública y rastreable, el historial on-chain puede usarse contra el usuario de formas que no existen en el sistema financiero tradicional, donde los datos también existen pero están más fragmentados y son menos accesibles. Dicho esto, la reputación verificable también tiene valor: en ciertos contextos, demostrar un historial de actividad puede ser una ventaja, no una vulnerabilidad.

Lo que queda claro es que Web3 es hoy un espacio de emprendedores y adoptadores tempranos. Pero para que llegue a ser un espacio retail, son precisamente ellos quienes tienen que usar Web3 y dar feedback para que se adapte a sus necesidades; si no lo hacen, Web3 simplemente no será un espacio retail.

Lo que hoy parece más probable es que Web3 no sea un ecosistema uniforme sino un conjunto de capas especializadas accesibles mediante apps dentro de un marco de experiencia unificada, de forma similar a como funciona el móvil o la web actual: una app para gaming donde el valor económico en juego es limitado y la transparencia no plantea riesgos graves, una app de DeFi on-chain donde el pseudoanonimato es suficiente mientras no haya conversión a fiat, y una app institucional, representada por protocolos de RWA o redes como [Polygon](https://polygon.technology/), donde la regulación exige KYC completo porque los activos subyacentes son instrumentos financieros regulados. Pareciese que se fragmenta la experiencia de usuario, porque elegirías una app para privacidad, otra para jugar, otra para finanzas, pero es exactamente como haces hoy cuando navegas entre apps en el móvil sin que esto se perciba como fragmentación problemática. La diferencia importante es que en Web3 el salto entre estas capas puede dejar rastro on-chain y crear puntos de correlación que en el mundo móvil no existen: cuando cambias de Gmail a tu app bancaria, nadie puede rastrear esa transición en una cadena pública. Ese es el reto de orquestación real: que las garantías de privacidad de cada capa no se anulen en entre ellas. Y es precisamente ahí, en esos puntos de transición entre capas, donde la experiencia unificada y la abstracción de cadena cruzada (cross-chain / Account Abstraction) tienen su mayor desafío: no basta con ocultar la complejidad técnica al usuario, hay que hacerlo sin crear nuevos vectores de correlación en el proceso.

## Referencias

- [Privacidad en Ethereum — documentación oficial](https://ethereum.org/es/privacy/)
- [Vitalik Buterin: Why I support privacy (2025)](https://vitalik.eth.limo/general/2025/04/14/privacy.html)
- [Blockchain Privacy and Regulatory Compliance — artículo académico (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S2096720923000519)
- [Privacy Stewards of Ethereum (PSE) — Ethereum Foundation](https://pse.dev/)
- [Hoja de ruta de privacidad para Ethereum L1](https://ethereum-magicians.org/t/a-maximally-simple-l1-privacy-roadmap/23459)
- [Ethereum privacy: the road to self-sovereignty — ethresear.ch](https://ethresear.ch/t/ethereum-privacy-the-road-to-self-sovereignty/22115)
- [An Analysis of Privacy in Stealth Address Schemes — análisis académico sobre vulnerabilidades (arXiv)](https://arxiv.org/abs/2308.01703)
- [Aztec Network — L2 de privacidad programable](https://aztec.network/)
- [Sanción de OFAC a Tornado Cash (agosto 2022)](https://home.treasury.gov/news/press-releases/jy0916)
- [Condena al cofundador de Tornado Cash — Bitdefender](https://www.bitdefender.com/en-gb/blog/hotforsecurity/tornado-cash-crypto-mixer-co-founder-sentenced-to-five-years-in-prison)
- [Arresto de los fundadores de Samourai Wallet — Observatorio Blockchain](https://observatorioblockchain.com/ciberseguridad/eeuu-cierra-samourai-wallet-y-detiene-a-sus-fundadores-por-lavado-de-dinero/)
- [Chainalysis — análisis de blockchain](https://www.chainalysis.com/)
- [Elliptic — análisis de blockchain](https://www.elliptic.co/)
- [TRM Labs — análisis de blockchain](https://www.trmlabs.com/)
- [Polygon — red L2 con enfoque institucional](https://polygon.technology/)
- [Radical transparency — Wikipedia](https://en.wikipedia.org/wiki/Radical_transparency)

---
