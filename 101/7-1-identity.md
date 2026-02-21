# Identidad Web3

Una de las promesas fundamentales de web3 es devolver el control de la identidad a los individuos, no solo por soberanía personal, sino porque concentrar este control en manos de terceros genera vulnerabilidades sistémicas de seguridad.

El objetivo es que cada persona pueda poseer y gestionar su propia identidad de forma autosoberana, a la que puedas relacionar certificados de terceros que acrediten tu identidad, y que interesados puedan validarlo. En la práctica, esta visión no difiere radicalmente de lo que ya conocemos en el mundo físico: posees un DNI en España o un pasaporte que te pertenece, del cual eres custodio, y donde acumulas sellos y validaciones que acreditan tus accesos.

Esta aspiración se ha materializado como [Self-Sovereign Identity (SSI)](https://en.wikipedia.org/wiki/Self-sovereign_identity), o identidad autosoberana. Este principio establece que los individuos deben tener control completo sobre sus credenciales, datos personales y decidir cómo se comparten, sin depender de autoridades centrales para validación o almacenamiento. El término fue popularizado en el artículo [The Path to Self-Sovereign Identity](https://www.lifewithalacrity.com/article/the-path-to-self-sovereign-identity/) de Christopher Allen.

Tanto legisladores como la comunidad web3 han convergido en la [identidad descentralizada](https://www.entrust.com/blog/2023/06/decentralized-identity) como marco técnico de referencia, aunque desde posiciones opuestas: web3 la adopta para lograr validación y almacenamiento genuinamente descentralizados, mientras que los legisladores la adoptan como infraestructura técnica manteniendo emisores cualificados y validación bajo control institucional. No es un consenso sobre el modelo, sino una convergencia en el estándar técnico con visiones irreconciliables sobre quién tiene el control.

Ese estándar técnico fue definido por [W3C](https://www.w3.org/) (World Wide Web Consortium), el organismo internacional que desarrolla estándares web abiertos, mediante tres especificaciones complementarias: los [Decentralized Identifiers (DIDs)](https://www.w3.org/TR/did-core/) definen cómo se componen y resuelven los identificadores descentralizados, las [Verifiable Credentials (VCs)](https://www.w3.org/TR/vc-data-model/) establecen cómo estructurar credenciales que acrediten atributos de la identidad, y las [Verifiable Presentations (VPs)](https://www.w3.org/TR/vc-data-model/#presentations) definen cómo presentarlas selectivamente ante un verificador. Cabe aclarar que estos estándares no son una infraestructura en sí mismos, sino especificaciones que cada implementación concreta debe materializar.

> Si quieres saber más al respecto, puedes acceder al documento del [protocolo DID](../infrastructure/identity/did-protocol.md).

Como veremos más adelante, los reguladores han sido más estrictos en la adopción de estas especificaciones de W3C. Web3 sí les da soporte, por ejemplo, cualquier dirección de Ethereum tiene su DID y es posible custodiar VCs en wallets como MetaMask mediante Snaps, pero la prioridad de composabilidad on-chain hace que el ecosistema prefiera otras primitivas, como las atestaciones.

Ahora que hemos visto esta introducción y antes de continuar, debemos aclarar los términos técnicos que la identificación maneja para que no exista ambigüedad sobre lo que hablamos, porque solemos confundirlos o, sobre todo, tratarlos como si fueran lo mismo:

Un **identificador** es un código único que te representa en el sistema. Tu wallet de [MetaMask](https://metamask.io/), como [EOA](https://www.binance.com/es/academy/glossary/externally-owned-account-eoa), tiene una dirección hexadecimal (0x1234...abcd) que funciona como tu identificador en la blockchain, un código que permite a los sistemas localizarte y comunicarse contigo. Este es un ejemplo simple, existen otros identificadores más formales como el [DID (Decentralized Identifier)](https://www.w3.org/TR/did-core/), que veremos más adelante. Lo importante es que un identificador no es una identidad, lo es según las relaciones que establecemos con él.

Una **atestación** es una declaración firmada digitalmente por un emisor que da fe o certifica ciertos atributos, afirmaciones o hechos sobre un sujeto. En términos simples, es cuando un emisor (una universidad, un empleador, una organización, una red) confirma algo sobre ti de forma verificable. Por ejemplo, una universidad puede atestiguar que completaste un grado académico, o una empresa puede atestiguar que trabajaste para ella durante cierto período.

Un **certificado** es el documento formal que materializa el resultado de una atestación. Cuando esa universidad atestigua que completaste un grado, el certificado es el documento —físico o digital— que puedes conservar y presentar como prueba. En ese sentido, un certificado es una forma específica y reconocible de credencial: el término proviene del lenguaje institucional tradicional e implica un emisor con autoridad reconocida, mientras que "credencial" es el término adoptado por [W3C](https://www.w3.org/) para este mismo concepto en entornos descentralizados.

Una **credencial** es cualquier evidencia o documento firmado que puede presentar el propio sujeto para demostrar algo o probar que tiene ciertos derechos o atributos. Habrás notado que se parece a una atestación y a un certificado, y es normal porque los tres conceptos están relacionados: la atestación es el acto del emisor, el certificado es el documento que lo materializa, y la credencial es ese mismo documento visto desde la perspectiva de quien lo porta y lo usa. Para [W3C](https://www.w3.org/), la especificación [Verifiable Credential (VC)](https://www.w3.org/TR/vc-data-model/) es el estándar técnico concreto que define cómo representar una credencial de forma verificable y portable en entornos digitales descentralizados.

Una **identidad** es la representación reconocible y significativa de quién eres en un contexto social. No puedes decirle a alguien "envíame dinero a cero-equis-uno-dos-tres-cuatro...a-be-ce-de" sin que sea confuso y propenso a errores. Necesitas algo que los humanos puedan entender y recordar. Aquí entra en juego tu *marca personal*: un nombre legible y una imagen (foto de perfil) que te distingan. Una identidad se construye y verifica gracias a una o varias credenciales, y preferimos este término en lugar de "atestación" en este contexto porque la identidad es algo que tú posees y gestionas, mientras que la atestación es algo que otros dicen sobre ti.

## Los actores del ecosistema

No existe consenso sobre cómo debe resolverse la identidad digital. Hay varios actores con visiones e intereses genuinamente distintos, y ninguno tiene razón absoluta, podemos verlo como:

**Las bigtech en web2: Siloed/Traditional**:

Por una parte, las grandes tecnológicas (*Big Tech*), dominadoras de la [Web2](https://ethereum.org/en/developers/docs/web2-vs-web3/) en plataformas centralizadas como redes sociales y servicios cloud, gestionan una identidad digital que no te pertenece realmente. Cuando creas una cuenta en Facebook, Google o cualquier plataforma digital, la empresa almacena tu información, controla el acceso a ella y puede modificarla, censurarla o eliminarla sin tu consentimiento previo. Esta fragmentación de identidad entre múltiples plataformas que no se comunican entre sí es lo que técnicamente se conoce como [siloed identity](hhttps://medium.com/evernym/the-three-models-of-digital-identity-relationships-ca0727cb5186), donde cada servicio mantiene tu información aislada en su propio silo.

Este modelo centralizado genera varios problemas fundamentales. Primero, existe un riesgo de seguridad significativo porque todas tus credenciales están almacenadas en servidores centralizados que se convierten en objetivos atractivos para cyber criminales. Segundo, no tienes portabilidad: tu reputación en Amazon no sirve en eBay, tu historial profesional en LinkedIn no se transfiere a otras plataformas. Tercero, dependes completamente de la plataforma: si deciden cerrar tu cuenta, pierdes años de datos, conexiones y reputación acumulada. Esta dependencia crea lo que se denomina [vendor lock-in](https://en.wikipedia.org/wiki/Vendor_lock-in), donde quedas atrapado en el ecosistema de un proveedor específico sin capacidad real de migrar tu identidad y datos a alternativas.

Además, el modelo centralizado crea problemas de privacidad. Para usar la mayoría de servicios digitales, debes revelar más información de la necesaria. Si quieres entrar a un sitio para mayores de edad, tienes que proporcionar tu fecha de nacimiento completa cuando en realidad solo necesitan saber que eres mayor de 18 años.

**Identidad federada: cuando BigTech se convierte en el intermediario**:

La industria reconoció tempranamente que obligar a usuarios a crear cuentas separadas en cada sitio web era insostenible. La solución que emergió fue el modelo de identidad federada: permite que un proveedor de identidad externo actúe como intermediario de confianza. Cuando hoy encuentras botones de "Sign in with Google", "Sign in with Apple" o "Sign in with Facebook" en prácticamente cualquier aplicación o servicio digital, estás usando este modelo basado principalmente en [OpenID Connect (OIDC)](https://openid.net/connect/), una capa de identidad construida sobre [OAuth 2.0](https://oauth.net/2/) que extiende su framework de autorización con capacidades de autenticación. [SAML](https://en.wikipedia.org/wiki/Security_Assertion_Markup_Language) es un protocolo alternativo más antiguo que todavía se usa en contextos empresariales.

Este enfoque resolvió problemas prácticos significativos: ya no necesitas recordar docenas de contraseñas diferentes, ni repetir procesos de registro tediosos en cada sitio. Sin embargo, simplemente trasladó la centralización a un nivel superior. En lugar de tener tu identidad fragmentada en múltiples silos, ahora depende de un puñado de gigantes tecnológicos que actúan como guardianes. Google, Apple, Facebook y Microsoft se han convertido en los IDPs dominantes, intermediando la mayoría de relaciones digitales en Internet. Si una de estas compañías cierra tu cuenta o decide que no cumples sus términos de servicio, pierdes acceso simultáneamente a docenas o cientos de servicios que dependen de esa identidad federada.

En 2026, este modelo no solo persiste sino que se ha convertido en el método de autenticación más usado globalmente en aplicaciones Web2. Su relevancia para Web3 es doble y aparentemente contradictoria. Por una parte, muchas dApps pragmáticamente implementan autenticación híbrida: ofrecen "Sign-In with Ethereum" para usuarios nativos crypto, pero también "Sign-In with Google" para facilitar onboarding gradual desde Web2 sin la fricción de gestionar claves privadas desde el primer momento.

**DID en Gobiernos y reguladores**:

Por otra parte los gobiernos y reguladores están desarrollando sus propios marcos normativos para la identidad digital. En concreto en Europa como el mayor referente, 

La implementación la define la W3C y se base en la identificación descentralizada DID,

**Identidad y privacidad off-chain**:

El modelo off-chain con credenciales privadas basado en [Decentralized Identifiers (DIDs)](https://www.w3.org/TR/did-core/), [Verifiable Credentials (VCs)](https://www.w3.org/TR/vc-data-model/) y [Verifiable Presentations](https://www.w3.org/TR/vc-data-model/#presentations) maximiza privacidad mediante control del usuario. Tus credenciales viven en tu wallet bajo tu custodia exclusiva, solo tú decides cuándo y a quién mostrarlas, y puedes usar [Zero-Knowledge Proofs](https://ethereum.org/en/zero-knowledge-proofs/) para revelar el mínimo necesario. Un smart contract no puede simplemente "leer" si tienes un diploma universitario, necesitas activamente presentar una prueba. Esto protege tu privacidad pero destruye la composabilidad automática: los protocolos DeFi no pueden consultar instantáneamente tu historial crediticio, las DAOs no pueden verificar automáticamente membresías, los NFT marketplaces no pueden filtrar automáticamente usuarios por jurisdicción.

Esta ha sido la elección para reguladores y gobiernos al ser la más segura y ha sido incluido como marco normativo, la regulación [eIDAS 2.0](https://digital-strategy.ec.europa.eu/en/policies/eidas-regulation) y su implementación de European Digital Identity Wallet, ofrece un equilibrio entre el control institucional y la autonomía del usuario.

Además, viendo el problema de Web2, a partir de 2026, plataformas de gran tamaño como Meta (Facebook, Instagram), Amazon, Apple, Booking.com, TikTok y Zalando, etc estarán obligadas por ley a aceptar la European Digital Identity Wallet (EUDI Wallet) como método válido de autenticación e identificación.

Para los ciudadanos: El uso de la cartera digital europea es voluntario. Los ciudadanos pueden elegir si desean obtener y utilizar esta identidad digital, y los Estados miembros deben proporcionar métodos alternativos de identificación tradicionales para aquellos que no deseen adoptarla. No existe obligación legal de que los ciudadanos usen este sistema para su vida cotidiana, sin embargo, la regulación cubre sectores amplios donde los servicios deben aceptar eIDAS 2.0: banca, transporte, energía, seguridad social, sanidad, suministro de agua, infraestructura postal, infraestructura digital, educación y telecomunicaciones. Este hecho en la la práctica, se convierte en un estándar de facto para identidad digital en Europa.

Proyectos como [Privado ID](https://www.privado.id/) (anteriormente Polygon ID) representan esta visión de identidad SSI más purista, priorizando la privacidad aunque afectando la composabilidad en Web3. Existen además emisores como [Fractal ID](https://www.fractal.id/) o [Civic](https://www.civic.com/) que facilitan el cumplimiento de KYC necesario para ciertas dApps, actuando como puentes entre la identidad legal y el ecosistema descentralizado.

Podrás encontrar más detalles y especificaciones técnicas sobre este tema en el documento de [protocolo DID](../infrastructure/identity/did-protocols.md).

**Web3 con KYC/AML**:

Adicionalmente, en lo referente al cumplimiento normativo (*compliance*) de plataformas cripto o Web3 con KYC/AML, debemos reconocer una realidad incómoda: [KYC](https://en.wikipedia.org/wiki/Know_your_customer) (*Know Your Customer*) y [AML](https://en.wikipedia.org/wiki/Money_laundering#Anti-money_laundering) (*Anti-Money Laundering*) no representan identidad descentralizada, sino identidad centralizada tradicional operando dentro de Web3 por obligación legal. Esta distinción es fundamental para entender correctamente el ecosistema.

Cada exchange donde compras ETH o BTC requiere procesos KYC rigurosos: pasaporte, prueba de domicilio, selfie sosteniendo tu documento, declaraciones de fuente de fondos. Este proceso es completamente centralizado y contradice frontalmente los principios de identidad autosoberana. Entregas tus datos personales más sensibles a una empresa privada que los almacena en sus servidores, exactamente el modelo centralizado que queremos superar.

¿Por qué existe esta contradicción en un ecosistema que promete descentralización? Regulación. Los gobiernos han implementado marcos regulatorios estrictos que obligan a cualquier entidad que facilite conversión entre fiat y criptomonedas a implementar controles KYC/AML. Regulaciones como la [5th Anti-Money Laundering Directive (5AMLD)](https://eur-lex.europa.eu/eli/dir/2018/843/oj) en Europa o el [Bank Secrecy Act](https://www.fincen.gov/resources/statutes-and-regulations/bank-secrecy-act) en Estados Unidos existen para prevenir lavado de dinero, financiamiento del terrorismo y evasión fiscal.

El resultado es que la mayoría de usuarios comprometen su privacidad desde el momento cero. Tu primer contacto con crypto probablemente fue entregar tu identidad legal completa a Coinbase o Binance. Incluso protocolos [DeFi](https://ethereum.org/en/defi/) descentralizados como [Uniswap](https://uniswap.org/) o Aave enfrentan presión regulatoria para implementar restricciones geográficas y verificación de identidad cuando alcanzan volúmenes significativos.

Protocolos como [Aave Arc](https://aave.com/) experimentaron con "DeFi permisionado" donde solo usuarios KYC-verificados podían participar. [MakerDAO](https://makerdao.com/) discute implementar KYC para activos del mundo real (RWA). DAOs grandes enfrentan dilemas similares: ¿cómo cumplir obligaciones fiscales sin comprometer pseudonimidad de miembros?

La identidad descentralizada teórica choca con las realidades del sistema financiero tradicional. Mientras los estados-nación controlen las rampas de entrada y salida del ecosistema crypto, KYC centralizado será inevitable para la mayoría de participantes. Los puristas argumentan que esto es temporal, que eventualmente viviremos completamente on-chain. Los pragmáticos reconocen que la regulación no desaparecerá, y que sistemas híbridos son el futuro más probable.



**OpenID4VC: cuando los IDPs se transforman en emisores de credenciales**:

Por otra parte, el estándar [OpenID4VC (OpenID for Verifiable Credentials)](https://openid.net/sg/openid4vc/) está transformando el panorama al convertir IDPs tradicionales en emisores de credenciales verificables. Esto significa que Google o Apple pueden emitir VCs que el usuario guarda en su wallet Web3 o [EUDI Wallet europeo](https://digital-strategy.ec.europa.eu/es/factpages/european-digital-identity-wallet), creando un puente entre la identidad federada Web2 y las credenciales autosoberanas.

La diferencia fundamental con la federación tradicional es arquitectónica: en lugar de que Google intermedie cada login manteniendo control perpetuo, ahora Google puede emitir una credencial verificable una vez que tú guardas en tu wallet y presentas donde quieras sin su participación posterior. El IDP sigue siendo el emisor inicial, pero pierde el rol de intermediario permanente que caracteriza a la federación clásica.

Paralelamente, emisores especializados como [Fractal ID](https://www.fractal.id/) o [Civic](https://www.civic.com/) operan como emisores nativos de VCs para KYC, realizando verificación una vez y emitiendo una credencial que tú custodias y presentas donde necesites, sin intermediación posterior. Estos proveedores nunca fueron IDPs en el sentido federado, desde su diseño inicial operan bajo el paradigma de credenciales verificables autosoberanas.

La distinción crucial es que eIDAS 2.0 establece dos niveles de confianza: **credenciales cualificadas**, emitidas por Qualified Trust Service Providers (QTSPs) certificados bajo eIDAS con reconocimiento legal pleno en toda la UE, y **credenciales no cualificadas**, emitidas por proveedores privados como Fractal ID o Civic, técnicamente compatibles con EUDI Wallet pero sin el mismo peso legal que las gubernamentales. Para casos críticos como identidad oficial o edad legal, predominarán las credenciales cualificadas; para casos de uso menos regulados como membresías o reputación, las credenciales privadas seguirán siendo válidas y útiles.

**Identidad, reputación on-chain y grafo social**:

Esta visión nació de la propuesta conocida como [DeSoc (Decentralized Society)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763), formulada en 2022 por Vitalik Buterin, E. Glen Weyl y Puja Ohlhaver. El paper "Decentralized Society: Finding Web3's Soul" planteaba que la identidad en Web3 debería construirse desde la reputación emergente on-chain, no desde credenciales emitidas por autoridades externas. La primitiva técnica propuesta para materializar esta visión eran los Soulbound Tokens (SBTs): NFTs no transferibles vinculados permanentemente a una dirección, capaces de acumular logros, membresías y relaciones de confianza directamente en la blockchain. La metáfora era poderosa: igual que los objetos vinculados al alma en World of Warcraft no pueden venderse, tus credenciales de reputación no deberían poder comprarse. Esta visión está diseñada específicamente para el ecosistema [Ethereum](https://ethereum.org/): tanto la mainnet L1 como todas las L2s compatibles con EVM ([Optimism](https://www.optimism.io/), [Arbitrum](https://arbitrum.io/), [Base](https://base.org/), [Polygon](https://polygon.technology/), etc.).

Sin embargo, los SBTs como estándar técnico diferenciado nunca llegaron a consolidarse. En los años posteriores al paper, no emergió ningún ERC ampliamente adoptado específicamente para SBTs, y los problemas prácticos los fueron diluyendo: la inmutabilidad absoluta generaba fricción cuando una credencial debía revocarse o corregirse, la exposición pública de tokens no transferibles planteaba serios problemas de privacidad, y la falta de estándar impedía la interoperabilidad. El ecosistema encontró una solución más flexible en las [on-chain attestations mediante EAS (Ethereum Attestation Service)](https://attest.org/), que permiten emitir credenciales verificables tanto on-chain como off-chain, con soporte de revocación y esquemas personalizados, sin necesidad de un nuevo tipo de token. Los [POAPs](https://poap.xyz/), que técnicamente son NFTs transferibles pero tratados socialmente como pruebas de asistencia o logros, siguieron siendo los "SBTs de facto" más usados. En la práctica, lo que el paper DeSoc imaginaba como ecosistema de SBTs se materializó, de forma más pragmática y fragmentada, a través de attestations de EAS, POAPs y el grafo social on-chain.

La filosofía de fondo sigue siendo relevante: todo debe estar on-chain para máxima composabilidad, con smart contracts leyendo directamente credenciales y relaciones verificables sin infraestructura off-chain compleja. La privacidad, desde esta perspectiva, se resuelve en capas superiores mediante Zero-Knowledge Proofs, [stealth addresses](https://vitalik.eth.limo/general/2023/01/20/stealth.html) o L2s con privacidad integrada, no es responsabilidad del sistema de identidad base. Si no estás dispuesto a aceptar que blockchain es fundamentalmente pública y transparente, quizás Web3 no es el ecosistema adecuado, visión que ya explicamos en [privacidad web3](4-3-challenges-privacy.md). La portabilidad cross-chain no es una preocupación central porque asumen que el ecosistema Ethereum (L1 + L2s compatibles) dominará.

Aquí es donde [Account Abstraction](https://ethereum.org/en/roadmap/account-abstraction/) transforma arquitectónicamente el concepto de identidad on-chain. En el modelo tradicional de EOA, tu identidad y tu método de autenticación son inseparables: la clave privada que controla tu wallet es tu identidad. Con Account Abstraction mediante [ERC-4337](https://eips.ethereum.org/EIPS/eip-4337), tu identidad migra completamente on-chain al vivir en un Smart Contract Wallet (SCW). Este smart contract se convierte en tu contenedor de identidad persistente: recibe attestations verificables, acumula tu reputación, posee tus POAPs, mantiene tu historial de gobernanza. La EOA, que antes era tu identidad misma, se convierte simplemente en una credencial de acceso, una de potencialmente múltiples formas de autenticarte ante tu identidad real que vive en el contrato.

Esta separación es fundamental porque desacopla tu identidad (la cuenta smart contract con su dirección pública) de tus métodos de autenticación (las claves que usas para controlarla). Puedes rotar tus EOAs periódicamente por seguridad, añadir autenticación biométrica, implementar recuperación social mediante guardianes, todo sin cambiar tu identidad pública ni perder tu historial acumulado. Si tu EOA actual es comprometida, simplemente revocas su permiso en el smart contract y añades una nueva, pero tu identidad on-chain permanece intacta en la misma dirección del contrato. Sin embargo, esta flexibilidad tiene un precio: intercambias la simplicidad y superficie de ataque mínima de las EOAs por la complejidad y riesgos de bugs en smart contracts, tema que exploraremos en detalle más adelante.

Esta arquitectura materializa la visión de identidad on-chain que el paper DeSoc anticipó: tu reputación emerge de tus relaciones y acciones verificables que quedan registradas en la blockchain, no de tokens con un nombre especial sino de attestations, POAPs y participación verificable. Tu reputación se construye mediante quién te sigue, qué DAOs te aceptan como miembro, qué contribuciones open-source has hecho, qué eventos has atendido ([POAPs](https://poap.xyz/)), cuánto has participado en gobernanza. No necesitas que Stanford certifique tu inteligencia si has contribuido código a protocolos importantes que la comunidad valora. Este modelo es inherentemente descentralizado y resistente a censura porque ninguna autoridad única puede revocar tu reputación social, pero es vulnerable a manipulación (comprar seguidores, crear narrativas falsas) y no satisface requisitos legales en la mayoría de jurisdicciones.

Proyectos como [Lens Protocol](https://www.lens.xyz/), [Farcaster](https://www.farcaster.xyz/) y [CyberConnect](https://cyberconnect.me/) representan una aproximación a esta idea del grafo social. Aunque enfrentan desafíos de interoperabilidad, materializan la reputación construida mediante interacciones verificables. Con Account Abstraction, estos protocolos pueden construir sobre smart contract wallets que separan identidad social de métodos de acceso, haciendo la experiencia más robusta y recuperable.

En resumen, bajo esta perspectiva evolucionada con AA, la identidad vive completamente on-chain en tu smart contract wallet, a la que puedes asociar un nombre (por ejemplo, con [ENS](https://ens.domains/)) y un NFT como foto de perfil, consolidando toda tu reputación de forma persistente. Tu EOA deja de ser tu identidad y se convierte en una credencial más, intercambiable y revocable, que te permite acceder a esa identidad on-chain sin comprometer su continuidad.

**Wallet-as-a-Service: abstracción total para onboarding masivo**:

Proveedores de infraestructura como [Privy](https://www.privy.io/), [Dynamic](https://www.dynamic.xyz/), [Magic](https://magic.link/) y [Biconomy](https://www.biconomy.io/) representan una visión pragmática que prioriza la adopción masiva sobre el purismo ideológico de Web3. Estos servicios implementan embedded wallets que abstraen completamente la gestión de claves criptográficas, permitiendo que usuarios entren mediante email, redes sociales o incluso autenticación biométrica sin necesidad de instalar extensiones de navegador ni custodiar claves privadas con frases semilla.

La arquitectura subyacente típicamente combina Account Abstraction mediante ERC-4337 con custodia delegada: el proveedor genera y custodia la clave privada en tu nombre, cifrada con credenciales que ya posees (contraseña de email, sesión OAuth de Google). Esto elimina la fricción de onboarding que históricamente ha sido la barrera más grande para adopción retail, convirtiendo la experiencia Web3 en algo indistinguible de Web2 desde la perspectiva del usuario.

Sin embargo, esta conveniencia tiene costos filosóficos, técnicos y regulatorios significativos. Aunque muchos proveedores ofrecen caminos de exportación de claves para eventualmente migrar hacia auto-custodia real, la mayoría de usuarios nunca ejecutan esta transición. En la práctica, estos servicios replican el modelo de custodia centralizada de exchanges como Coinbase, solo que integrado directamente en la experiencia de la aplicación. Si el proveedor sufre un hack, experimenta problemas de disponibilidad, o decide cerrar el servicio, los usuarios enfrentan riesgos similares a los de plataformas Web2 tradicionales.

Adicionalmente, existe un trade-off fiscal y regulatorio crítico frecuentemente ignorado: desde la perspectiva de autoridades fiscales como Hacienda en España, una wallet custodiada por un proveedor extranjero constituye una cuenta en el extranjero sujeta a declaración mediante modelo 720 si el saldo supera 50.000 EUR al cierre del año. Sin embargo, en la práctica, estas wallets rara vez alcanzan dicho umbral cuando se utilizan como simple mecanismo de acceso a DApps de consumo generalista como GameFi o redes sociales, quedando la obligación fiscal más como consideración teórica que práctica para el usuario promedio.

Las tensiones arquitectónicas son múltiples. Desde la perspectiva DeSoc, WaaS secuestra tu reputación on-chain en cuentas que técnicamente son propiedad del proveedor: tus SBTs y POAPs viven en una dirección que no controlas, contradiciendo la visión de identidad soberana. Desde la perspectiva DIDs/VCs, estos servicios almacenan credenciales en sus propios servidores, no en una wallet bajo tu control exclusivo como asume eIDAS 2.0 y OpenID4VC. La incertidumbre regulatoria es crítica: si las credenciales viven en infraestructura del proveedor, ¿pueden legalmente actuar como European Digital Identity Wallets? La respuesta técnica es probablemente negativa, pero la mayoría de proveedores no ha clarificado públicamente su estrategia de compliance.

La tensión fundamental es que WaaS resuelve UX inmediata sacrificando simultáneamente ambas visiones de identidad Web3: secuestra reputación on-chain en cuentas propietarias y contradice la custodia soberana que sustenta DIDs/VCs. Para aplicaciones de consumo masivo que priorizan crecimiento sobre coherencia ideológica, este compromiso puede ser aceptable temporalmente. Para aplicaciones que manejan valores significativos, reputación crítica, o donde el cumplimiento con eIDAS 2.0 será obligatorio, depender de wallets custodiadas genera vulnerabilidades técnicas, filosóficas y potencialmente legales que contradicen el propósito mismo de construir en blockchain.

**Infraestructura neutral: EAS y protocolos de attestations**:

Proyectos como [Ethereum Attestation Service (EAS)](https://attest.sh/) y [Sign Protocol](https://sign.global/) adoptan una postura neutral respecto a estas disputas filosóficas. [EAS](https://attest.sh/) despliega contratos inteligentes idénticos en múltiples redes: [Ethereum](https://ethereum.org/) mainnet, [Optimism](https://www.optimism.io/), [Base](https://base.org/), [Arbitrum](https://arbitrum.io/), [Polygon](https://polygon.technology/), [Linea](https://linea.build/), [Scroll](https://scroll.io/) y otras L2s, permitiendo que las attestations vivan donde sea más conveniente según costos y necesidades.

Proveen infraestructura de attestations on-chain que cualquier actor puede usar según sus necesidades: puedes hacer attestations públicas componibles si priorizas transparencia, o attestations off-chain si necesitas privacidad.

No toman partido sobre si la identidad debe ser credenciales formales vs. grafo social, simplemente ofrecen primitivas técnicas que ambos modelos pueden consumir. Esta neutralidad arquitectónica es poderosa pero no resuelve las tensiones fundamentales, solo las hace técnicamente viables en paralelo.

**Proof of Personhood y resistencia Sybil**:

Actores como [Worldcoin](https://worldcoin.org/), [Gitcoin Passport](https://passport.gitcoin.co/), [Proof of Humanity](https://www.proofofhumanity.id/) y [BrightID](https://www.brightid.org/) se enfocan exclusivamente en resolver un problema específico: demostrar que eres un humano único real, resistiendo ataques [Sybil](https://www.microsoft.com/en-us/research/publication/the-sybil-attack/) (creación de múltiples identidades falsas). Sus infraestructuras varían significativamente:

*Worldcoin* opera [World Chain](https://world.org/world-chain), su propia L2 construida sobre [OP Stack](https://stack.optimism.io/), aunque también verifica identidades que pueden usarse en [Ethereum](https://ethereum.org/) mainnet y otras chains mediante bridges.

*Gitcoin Passport* almacena attestations usando [EAS](https://attest.sh/) en múltiples L2s: principalmente [Optimism](https://www.optimism.io/) y [Base](https://base.org/), permitiendo que los scores de humanidad sean verificables on-chain donde sea necesario.

*Proof of Humanity* es un smart contract desplegado únicamente en [Ethereum](https://ethereum.org/) mainnet, creando un registro público y permanente en la L1.

*BrightID* opera su propia red peer-to-peer descentralizada completamente independiente de blockchains, aunque puede anclar verificaciones en [Ethereum](https://ethereum.org/) o [Gnosis Chain](https://www.gnosis.io/) cuando es necesario.

Para estos proyectos, la *wallet* y la dirección siguen siendo la forma de acceso, pero el resto de la información reside en sus propios ecosistemas. La extensión mediante Credenciales Verificables (VC) o la persistencia total *on-chain* son secundarias; su prioridad absoluta es garantizar la unicidad del individuo.

> Si bien su prioridad absoluta es garantizar la unicidad del individuo, estos protocolos mantienen una flexibilidad pragmática para adoptar estándares según lo demande la interoperabilidad de la industria.

Cada solución presenta diferentes compromisos arquitectónicos: Worldcoin prioriza la privacidad mediante pruebas de conocimiento cero (ZK-proofs) pero depende de *hardware* biométrico centralizado; Gitcoin Passport agrega reputación *on-chain* sacrificando cierta privacidad; Proof of Humanity crea registros públicos permanentes en la capa 1 (L1); y BrightID preserva la privacidad del grafo social pero requiere confianza en su red descentralizada. Ninguno pretende ser una solución completa de identidad, sino resolver el problema anti-Sybil para habilitar mecanismos como la votación cuadrática, distribuciones justas de tokens y gobernanza democrática.

## Las diferentes visiones que fragmentan el ecosistema

La fragmentación en identidad Web3 no es accidental ni temporal, refleja tensiones filosóficas irreconciliables entre objetivos que fundamentalmente compiten entre sí. Entender estas tensiones es crucial porque explican por qué no existe "una solución de identidad Web3" unificada, sino un ecosistema de herramientas especializadas que hacen trade-offs incompatibles.

### Privacidad vs. composabilidad: on-chain vs off-chain

La primera tensión fundamental es dónde viven tus datos de identidad y quién puede acceder a ellos.

El modelo **off-chain con credenciales privadas** (DIDs, VCs, VPs) maximiza privacidad mediante control del usuario. Tus credenciales viven en tu wallet bajo tu custodia exclusiva, solo tú decides cuándo y a quién mostrarlas, y puedes usar [Zero-Knowledge Proofs](https://ethereum.org/en/zero-knowledge-proofs/) para revelar el mínimo necesario. Un smart contract no puede simplemente "leer" si tienes un diploma universitario, necesitas activamente presentar una prueba. Esto protege tu privacidad pero destruye la composabilidad automática: los protocolos DeFi no pueden consultar instantáneamente tu historial crediticio, las DAOs no pueden verificar automáticamente membresías, los NFT marketplaces no pueden filtrar automáticamente usuarios por jurisdicción.

El modelo **on-chain público** (SBTs, attestations on-chain, POAPs) maximiza composabilidad sacrificando privacidad. Tus credenciales son tokens en tu dirección que cualquier smart contract puede leer sin permiso. Un protocolo de lending puede verificar instantáneamente que posees un SBT de "buen pagador" emitido por otro protocolo y ajustar tus tasas automáticamente. Una DAO puede requerir posesión de ciertos SBTs para habilitar votación. Este modelo es técnicamente simple y extremadamente poderoso para construir sistemas componibles, pero significa que toda tu identidad es un libro abierto: cualquiera puede ver todos tus SBTs, correlacionar tu actividad, y construir perfiles detallados de tu vida digital.

Más que una imposibilidad técnica insuperable, el verdadero 'punto medio' fracasa hoy por la falta de uniformidad en el acceso. A diferencia de la identidad federada de la Web2 (Login con Google/Apple), que ofrece una entrada fluida y universal, la Web3 obliga al usuario a navegar un ecosistema fragmentado: o te sumerges en la complejidad técnica de las wallets privadas, o dependes de logins tipo Web2 que sacrifican la soberanía. El sacrificio real no es solo entre privacidad y composabilidad, sino en la cordura del usuario, que aún no dispone de un estándar que haga la identidad tan invisible y sencilla como un toque biométrico en el móvil.

### Autoridades formales vs. reputación emergente: credenciales vs grafo social

La segunda tensión es epistemológica: ¿qué constituye identidad verificable?

El modelo de **autoridades y credenciales formales** (gobiernos con eIDAS, universidades emitiendo diplomas, empresas certificando experiencia) asume que la identidad se construye mediante validación de instituciones reconocidas. Tu diploma vale porque Stanford University lo firmó, no porque la comunidad cree que eres inteligente. Este modelo replica estructuras del mundo físico en blockchain: necesitas emisores con autoridad real, mecanismos de revocación cuando las credenciales caducan, y probablemente compliance regulatorio. Funciona bien para integración con sistemas legales y financieros tradicionales, pero centraliza el poder de validación en manos de instituciones que pueden excluir, discriminar o censurar.

El modelo de **grafo social y reputación emergente** (Lens Protocol, Farcaster, sistemas de reputación on-chain) argumenta que la identidad emerge de tus relaciones y acciones verificables. Tu reputación se construye mediante quién te sigue, qué DAOs te aceptan como miembro, qué contribuciones open-source has hecho, qué eventos has atendido (POAPs), cuánto has participado en gobernanza. No necesitas que Stanford certifique tu inteligencia si has contribuido código a protocolos importantes que la comunidad valora. Este modelo es inherentemente descentralizado y resistente a censura porque ninguna autoridad única puede revocar tu reputación social, pero es vulnerable a manipulación (comprar seguidores, crear narrativas falsas) y no satisface requisitos legales en la mayoría de jurisdicciones.

Ambos modelos coexisten en Web3 porque sirven necesidades diferentes. Si necesitas abrir una cuenta bancaria o probar tu edad legalmente, requieres credenciales formales de autoridades reconocidas. Si necesitas demostrar reputación en comunidades descentralizadas para recibir funding de una DAO, tu grafo social y contribuciones on-chain son más relevantes que cualquier diploma. La tensión surge cuando sistemas intentan ser puristas: protocolos que solo aceptan reputación emergente excluyen a newcomers sin historial on-chain, mientras que sistemas que solo aceptan credenciales formales replican barreras de acceso del mundo tradicional.

### Auto-custodia vs. conveniencia: el dilema del onboarding masivo

La tercera tensión fundamental es quién controla realmente tus claves privadas, y por extensión, tu identidad y activos.

El modelo de **auto-custodia pura** (self-custody) es el ideal cypherpunk original: tú generas, almacenas y gestionas tus propias claves privadas mediante wallets no-custodiales como MetaMask, Ledger o Trezor. Nadie más puede acceder a tus fondos ni censurar tus transacciones. Si pierdes tus claves, nadie puede recuperarlas por ti. Esta soberanía absoluta viene con responsabilidad absoluta: debes proteger tu frase semilla de 12 o 24 palabras contra pérdida, robo, y errores de usuario. Para usuarios técnicamente sofisticados que entienden las implicaciones, este modelo ofrece garantías de seguridad y resistencia a censura incomparables.

El problema es que la auto-custodia crea fricción masiva para adoption retail. Los usuarios promedio no están preparados para gestionar secretos criptográficos cuya pérdida resulta en pérdida permanente e irrecuperable de fondos. Las frases semilla son confusas, los usuarios reutilizan contraseñas débiles, comparten capturas de pantalla accidentalmente, caen en phishing. La experiencia de onboarding tradicional (instalar extensión de navegador, anotar 12 palabras, entender conceptos de gas, confirmar transacciones manualmente) genera tasas de abandono superiores al 90% para usuarios no-cripto.

El modelo de **wallets custodiadas y embedded wallets** (WaaS) resuelve este problema de UX trasladando la custodia a un tercero de confianza. Servicios como Privy, Dynamic o Magic custodian tus claves cifradas en su infraestructura, permitiéndote acceder mediante credenciales familiares como email o OAuth social. La experiencia se vuelve indistinguible de Web2: un clic y estás dentro, sin frases semilla ni gestión manual de gas. Para aplicaciones de consumo masivo, esto elimina la barrera de entrada más grande.

Pero este modelo replica exactamente los problemas que blockchain pretendía resolver. Si el proveedor WaaS sufre un hack, experimenta downtime, o decide cerrar el servicio, pierdes acceso a tus activos. Si el proveedor implementa compliance agresivo por presión regulatoria, puede congelar tu cuenta sin aviso. Aunque muchos servicios ofrecen "exportación de claves" para migrar eventualmente a auto-custodia, la mayoría de usuarios nunca ejecutan esta transición, permaneciendo indefinidamente en un modelo centralizado.

Existe un punto medio emergente mediante **custodia programable y social recovery**. Account Abstraction permite implementar lógica de recuperación social donde un conjunto de guardianes (amigos, familiares, otros dispositivos tuyos) pueden colectivamente recuperar tu cuenta si pierdes las claves, sin que ningún guardián individual tenga control unilateral. Servicios como Argent implementan esto, ofreciendo UX simple sin sacrificar completamente la auto-custodia. Sin embargo, este modelo añade complejidad técnica y todavía requiere que usuarios entiendan conceptos de smart contracts y configuren guardianes apropiadamente.

La tensión real no es técnica sino filosófica. Web3 promete soberanía individual sobre identidad y activos, pero la mayoría de humanos prefieren conveniencia sobre soberanía. Los usuarios no quieren gestionar claves criptográficas igual que no quieren gestionar certificados SSL para navegar la web. La pregunta incómoda es: si el 95% de usuarios elige voluntariamente custodia delegada por conveniencia, ¿hemos fallado en la promesa de descentralización, o simplemente hemos descubierto que la mayoría de personas no valora la soberanía lo suficiente como para aceptar su costo?

La realidad pragmática en 2026 es segmentación de mercado. Aplicaciones financieras manejando valores significativos (DeFi protocols, trading avanzado, tesorería de DAOs) asumen auto-custodia porque sus usuarios sofisticados valoran seguridad sobre conveniencia. Aplicaciones de consumo masivo (gaming, social, collectibles casuales) implementan embedded wallets porque priorizan crecimiento de usuario sobre purismo ideológico. La descentralización progresiva, donde usuarios comienzan con wallets custodiadas y gradualmente migran hacia auto-custodia conforme aprenden, es el compromiso más viable, aunque en la práctica la mayoría nunca completa esa migración.

### Account Abstraction: separando identidad de claves criptográficas

En el modelo tradicional de Ethereum, tu wallet no es solo un método de autenticación, sino que actúa directamente como tu credencial de identidad. Las Externally Owned Accounts (EOAs) funcionan así: la clave privada que controla tu wallet es inseparable de tu identidad on-chain. Si pierdes esa clave, pierdes permanentemente todo lo asociado: tus tokens, tu reputación acumulada, tus credenciales, tu historial completo. Si la clave es comprometida, un atacante puede vaciar tu cuenta sin posibilidad de reversión. No existe distinción entre el método de acceso y la identidad misma, creando fragilidades fundamentales para construir identidad persistente a largo plazo.

[Account Abstraction (AA)](https://ethereum.org/en/roadmap/account-abstraction/) rompe esta dependencia al separar tu identidad (la cuenta) del método de acceso (las claves). Con [ERC-4337](https://eips.ethereum.org/EIPS/eip-4337) creas una nueva cuenta de smart contract que soporta social recovery, rotación de claves, múltiples métodos de autenticación simultáneos, lógica personalizada de seguridad y crucialmente, gas sponsorship mediante paymasters (permitiendo que terceros paguen tus transacciones o pagar con tokens distintos a ETH). El problema crítico para identidad es que requiere una dirección nueva: si llevas años acumulando POAPs, SBTs y reputación en tu EOA actual, migrar a ERC-4337 significa empezar de cero o ejecutar un proceso manual complejo de transferir cada token y credencial a la nueva dirección.

[EIP-7702](https://eips.ethereum.org/EIPS/eip-7702) resuelve específicamente este dilema de migración permitiendo que tu EOA existente delegue temporalmente su lógica a un smart contract durante transacciones individuales, sin cambiar permanentemente su estructura. Para identidad esto significa que puedes añadir social recovery, rotación de claves y otras capacidades avanzadas a tu cuenta actual sin perder tu dirección ni tu historial. Sin embargo, estas capacidades solo están activas cuando explícitamente lo solicitas transacción por transacción, no son permanentes como en ERC-4337.

Esta delegación temporal introduce vectores de ataque específicos que Vitalik Buterin ha señalado públicamente: el riesgo principal es que durante el periodo de delegación, un atacante que comprometa tu clave EOA podría delegar hacia un contrato malicioso que drene fondos o ejecute acciones no autorizadas. A diferencia de ERC-4337 donde la lógica de seguridad está siempre activa en el smart contract, EIP-7702 requiere que el usuario autorice explícitamente cada delegación, creando ventanas de vulnerabilidad si la clave EOA es comprometida entre transacciones. Adicionalmente, la naturaleza temporal de la delegación complica la auditoría de seguridad: es más difícil razonar sobre el estado de seguridad de una cuenta que alterna entre comportamiento EOA tradicional y lógica delegada.

Ambos enfoques habilitan las mismas funcionalidades de identidad (social recovery, key rotation), pero la diferencia fundamental está en el modelo de seguridad: EIP-7702 prioriza portabilidad de historial conservando tu dirección EOA a costa de un modelo de seguridad más complejo y potencialmente vulnerable, mientras que ERC-4337 ofrece garantías permanentes de seguridad avanzada mediante una cuenta smart contract nueva con lógica compleja siempre activa, pero requiere migración explícita de tu identidad y reputación acumulada.

El impacto de Account Abstraction sobre las diferentes visiones de identidad es profundo pero asimétrico. Para el modelo de reputación on-chain y grafo social, AA representa una mejora fundamental y casi unánimemente positiva. La reputación puede finalmente vivir en la cuenta (la dirección del smart contract) independientemente de las claves que la controlan. Esto resuelve el problema crítico de *key rotation*: puedes rotar tus claves de firma periódicamente por seguridad, cambiar de dispositivo hardware, migrar de una clave ECDSA a esquemas post-cuánticos cuando sea necesario, todo sin crear una nueva identidad y perder tu historial. Tus POAPs, tus SBTs, tu membresía en DAOs, tu historial de contribuciones en Gitcoin, permanecen asociados a tu cuenta incluso cuando las claves subyacentes cambian completamente.

Para el modelo de credenciales verificables off-chain (DIDs/VCs), la relación con Account Abstraction es más compleja y ambivalente. Por una parte, AA facilita la rotación de claves sin cambiar tu identificador público (tu dirección de cuenta), lo cual alinea perfectamente con el principio de DIDs donde el identificador debe persistir independientemente de las claves de autenticación. El estándar [DID:ethr](https://github.com/decentralized-identity/ethr-did-resolver) puede beneficiarse directamente de AA para implementar key rotation más robusta. Por otra parte, AA añade una capa adicional de complejidad a la verificación de credenciales: ahora un verificador no puede simplemente validar una firma contra una clave pública, debe interactuar con un smart contract que define lógica de autenticación arbitraria.

Esta complejidad tiene implicaciones prácticas. Si tu wallet usa AA con múltiples métodos de autenticación (biometría, hardware key, recovery social simultáneamente), ¿cómo emites una credencial verificable que pueda ser validada off-chain sin consultar el estado on-chain del smart contract? Las soluciones típicamente requieren que la credencial incluya metadata adicional sobre qué método de autenticación específico se usó al momento de emisión, o que los verificadores tengan capacidad de consultar on-chain el estado actual de la cuenta. Esto erosiona parcialmente las garantías de privacidad del modelo off-chain puro, donde idealmente no necesitas tocar blockchain para verificar una credencial.

Respecto a la portabilidad cross-chain, AA no resuelve mágicamente la fragmentación entre redes incompatibles. Tu smart account en Ethereum mainnet es un contrato completamente separado de cualquier cuenta en Solana, Cosmos o incluso otras L2s de Ethereum como Arbitrum u Optimism.

Protocolos como [LayerZero](https://layerzero.network/) o [Across](https://across.to/) experimentan con sincronización cross-chain de estados, permitiendo que acciones en una chain actualicen tu perfil en otras, pero esta coordinación añade complejidad, latencia y costos significativos. La visión a largo plazo de Account Abstraction asume que la mayoría de actividad convergirá en el ecosistema Ethereum (mainnet L1 + L2s compatibles con EVM) donde la composabilidad nativa es posible, aceptando que otras blockchains incompatibles permanecerán fragmentadas.

El impacto más inmediato y visible de AA en 2026 es la proliferación de wallets que abstraen completamente la gestión de claves para nuevos usuarios. Servicios como [Privy](https://www.privy.io/), [Dynamic](https://www.dynamic.xyz/) y [Biconomy](https://www.biconomy.io/) implementan ERC-4337 para ofrecer experiencias donde el usuario entra con email o social login, y la wallet se crea invisible en segundo plano como smart account. Esto facilita dramáticamente el onboarding pero replica paradójicamente muchos problemas de Web2: si pierdes acceso a tu email, pierdes acceso a tu wallet; si el proveedor cierra, potencialmente pierdes acceso a menos que hayas exportado tus claves.

La promesa de Account Abstraction para identidad es poderosa pero todavía incompleta. Resuelve problemas críticos de persistencia y recuperación para reputación on-chain, pero añade complejidad a sistemas que priorizan privacidad off-chain y no elimina fragmentación cross-chain. El futuro más probable es híbrido: AA se convierte en estándar para cuentas on-chain donde la composabilidad es prioritaria, mientras que sistemas que requieren máxima privacidad continúan usando métodos tradicionales de firma off-chain con DIDs y VCs, aceptando la fricción adicional como costo necesario de sus garantías de privacidad.

### Consecuencias prácticas de la fragmentación

Esta fragmentación tiene impactos reales en la experiencia de usuario. Un usuario promedio de Web3 navega múltiples sistemas de identidad incompatibles simultáneamente:

Para comprar crypto en un exchange centralizado, pasas KYC completo entregando tu identidad legal a una empresa privada (modelo centralizado tradicional). Para interactuar con protocolos DeFi, usas tu dirección Ethereum como identificador pseudónimo donde tu reputación es tu historial de transacciones visible públicamente (modelo on-chain transparente). Si participas en gobernanza de DAOs, podrías necesitar POAPs de eventos para probar membresía o Gitcoin Passport para resistencia Sybil (modelo de reputación emergente). Si una dApp requiere verificación de jurisdicción por compliance, podrías presentar una credencial off-chain mediante Privado ID que demuestre "no estoy en país sancionado" sin revelar tu ubicación exacta (modelo off-chain con privacidad).

Ninguno de estos sistemas se comunica con los otros de forma nativa. Tu reputación construida en Ethereum no es visible ni relevante en Solana. Tus credenciales verificables off-chain no ayudan a smart contracts que necesitan leer datos on-chain. Tu grafo social en Lens Protocol no certifica tu edad para compliance legal.

Los desarrolladores de aplicaciones enfrentan decisiones arquitectónicas fundamentales que determinan qué usuarios pueden participar. Si construyes un sistema que requiere credenciales formales off-chain, excluyes a usuarios que solo tienen reputación on-chain. Si construyes asumiendo todo on-chain público, excluyes a usuarios que requieren privacidad. Si priorizas composabilidad nativa con smart contracts, sacrificas privacidad. Si priorizas privacidad mediante VCs off-chain, sacrificas la experiencia de usuario fluida de interacciones automáticas on-chain.

La realidad es que Web3 no ha convergido en un modelo unificado de identidad porque los diferentes casos de uso tienen requisitos genuinamente incompatibles. La solución pragmática no es forzar convergencia prematura, sino reconocer esta diversidad y construir puentes entre sistemas donde sea posible mediante estándares compartidos (como [OpenID4VC](https://openid.net/sg/openid4vc/) permitiendo que wallets Web3 y EUDI coexistan) mientras aceptamos que ciertos trade-offs son fundamentales e irreconciliables.

## La Realidad Práctica en 2026: Fragmentación Persistente

A pesar de los esfuerzos de estandarización técnica mediante OID4VC y mandatos regulatorios como eIDAS 2.0, el usuario en web3 enfrenta una experiencia fragmentada que refleja la falta de coordinación entre actores del ecosistema.

### El Stack de Identidad

En la práctica, un usuario Web3 activo en 2026 gestiona su identidad mediante una fragmentación de aplicaciones que, en el mejor de los casos, se reduce a dos o tres interfaces principales, dependiendo de sus necesidades:

**Wallet principal cripto**: [MetaMask](https://metamask.io/), [Coinbase Wallet](https://www.coinbase.com/wallet/) o [Phantom](https://phantom.app/) funcionan como la interfaz central donde acumulas tokens, firmas transacciones, guardas [SBTs](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763), coleccionas [POAPs](https://poap.xyz/), y gestionas [Gitcoin Passport](https://passport.gitcoin.co/). Esta wallet soporta "Sign-In with Ethereum" y actúa como tu identidad base para la mayoría de dApps. La fragmentación aquí no es conceptual: todo vive en la misma aplicación.

**EUDI Wallet europea**: Para ciudadanos europeos que necesiten interactuar con servicios regulados o ejercer sus derechos digitales bajo [eIDAS 2.0](https://digital-strategy.ec.europa.eu/en/policies/eidas-regulation), esta es una aplicación separada obligatoria que almacena credenciales oficiales gubernamentales. No se integra nativamente con MetaMask. Es una segunda aplicación que debes abrir cuando un servicio Web2 o Web3 regulado lo requiera.

**Emisores VC (KYC, etc)**: [Civic](https://www.civic.com/), [Fractal ID](https://www.fractal.id/), [Holonym](https://holonym.id/), entre otros, son emisores que serían interoperables en un ecosistema mas amplio, ya que sus credenciales se integran directamente en tu wallet principal mediante **MetaMask Snaps** (como [Masca](https://masca.io/)) o en la **EUDI Wallet** (estándar europeo). Esto permite que la identidad y los activos convivan en una sola aplicación, eliminando la fricción de terceros proveedores.

> Cabria pensar que el ecosistema se dirija en esta dirección.

**Ecosistemas cerrados**: World ID** (de [Worldcoin](https://worldcoin.org/)) entre otros, requeririan su propia aplicación usando su propio mecanismo de ZK. A pesar de su evolución hacia el estándar de [Verifiable Credentials](https://www.w3.org/TR/vc-data-model/), seguirian siendo un sistema cerrado que no permite una gestión nativa desde otras wallets como MetaMask con snap Masco o EUDI Wallet, forzando una experiencia de usuario fragmentada. Aunque presumiblemente, el esta

**WaaS Wallets as a Serve: experiencia web2**:

La fragmentación real desde la perspectiva del usuario no es cuántos tipos de tokens o credenciales acumulas, sino cuántas aplicaciones diferentes debes instalar, abrir y gestionar. Un usuario europeo activo en Web3 termina con dos aplicaciones obligatorias (wallet cripto + EUDI Wallet), posiblemente tres si adopta Worldcoin. Los SBTs, POAPs, Gitcoin Passport y credenciales Civic/Fractal viven dentro de tu wallet principal sin añadir complejidad de aplicaciones adicionales.

### Intentos de unificación: MetaMask Snaps y Account Abstraction

[MetaMask Snaps](https://snaps.metamask.io/) representa un intento de crear una "plataforma de identidad" extensible donde implementaciones como [Masca](https://masca.io/) integran la gestión de identificadores descentralizados (DIDs) y credenciales verificables dentro de la *wallet* más popular de Ethereum. Sin embargo, esta aproximación enfrenta limitaciones críticas relacionadas con la experiencia de usuario y la disponibilidad multiplataforma.

La complejidad añadida requiere que los usuarios descubran, instalen y gestionen extensiones de terceros, lo que eleva la barrera de entrada. Además, se produce una fragmentación de estado conceptual entre las claves financieras y las claves de identidad, añadiendo fricción al uso diario. A esto se suma que el soporte en entornos móviles ha sido históricamente limitado en comparación con la experiencia de escritorio, excluyendo a una parte significativa de los usuarios *retail*.

Paralelamente, la [Account Abstraction](https://ethereum.org/en/roadmap/account-abstraction/) (abstracción de cuentas) promete simplificar la experiencia *on-chain* mediante cuentas inteligentes (*smart accounts*) que podrían gestionar automáticamente el gas, los permisos y las credenciales. Sin embargo, esta y estándares como [OID4VC](https://openid.net/sg/openid4vc/) evolucionan como esfuerzos paralelos sin una coordinación clara: uno optimiza la cuenta *on-chain* y el otro estandariza credenciales *off-chain*, pero carecen de puentes nativos efectivos entre ambos modelos.

### ¿Convergencia o coexistencia permanente?

En 2026, la pregunta fundamental es si el ecosistema convergirá hacia una experiencia unificada de identidad o si la fragmentación actual es una característica permanente del diseño descentralizado.

Existen argumentos sólidos para una eventual convergencia. La presión regulatoria podría forzar el cumplimiento de estándares comunes como eIDAS u OID4VC, mientras que los altos costos de fricción actuales motivarán la innovación en capas de agregación. Además, es posible que las generaciones nativas de Web3 normalicen la gestión de múltiples herramientas como una práctica estándar.

Por otro lado, la coexistencia permanente se sustenta en que los compromisos fundamentales —privacidad frente a composabilidad, o autoridad formal frente a reputación emergente— son a menudo irreconciliables. Dado que cada dominio (finanzas, identidad legal, reputación social) tiene requisitos técnicos y regulatorios incompatibles, la especialización funcional puede resultar superior a soluciones monolíticas que intentan resolver todos los casos de uso.

La realidad más probable apunta a una especialización con interoperabilidad selectiva. Veremos múltiples *wallets* y aplicaciones especializadas conectadas mediante protocolos de puente, análogos a [WalletConnect](https://walletconnect.com/) pero para identidad, que permitan flujos entre aplicaciones sin forzar la fusión de funcionalidades incompatibles.

## Guía de decisión para desarrolladores: ¿Qué camino tomar?

Para un desarrollador en 2026, la parálisis por análisis es el mayor riesgo. No existe una solución única que resuelva todos los aspectos de la identidad. La estrategia correcta es definir tu caso de uso principal y seleccionar el *stack* tecnológico que optimice para ese objetivo específico, aceptando los compromisos inherentes.

A continuación presentamos un marco de decisión basado en las necesidades más comunes de las dApps modernas.

### DeFi regulada, RWA o Pagos

Si tu aplicación toca dinero fiat, activos del mundo real (RWA) o valores regulados, tu prioridad es la certeza legal y evitar el lavado de dinero.

El desafío principal radica en la necesidad de verificar que el usuario no se encuentra en listas de sanciones (OFAC) y validar su identidad real (KYC), todo ello sin la carga de custodiar documentos sensibles ni asumir la responsabilidad de gestionar datos personales bajo normativas como GDPR.

La solución recomendada es delegar la verificación en proveedores especializados que emitan credenciales reutilizables. En este stack, servicios como [Fractal ID](https://www.fractal.id/), [Civic](https://www.civic.com/) o [Privado ID](https://www.privado.id/) permiten verificaciones de conocimiento cero (ZK) que preservan la privacidad, utilizando el estándar de Credenciales Verificables (VCs) *off-chain*.

El patrón de desarrollo consiste en que el usuario se verifica una única vez con el proveedor para obtener su credencial en la *wallet*. Posteriormente, tu *smart contract* o interfaz solo necesita verificar la prueba criptográfica de que el KYC ha sido aprobado, sin tocar nunca los datos personales del usuario.

### Gobernanza DAO o Airdrops

Cuando el objetivo es distribuir poder de voto o tokens, el riesgo crítico es el ataque Sybil, donde una sola persona crea múltiples cuentas para manipular resultados o acaparar recursos.

En este escenario, no es necesario conocer la identidad civil del usuario. El requisito fundamental es obtener garantías de que se trata de un humano único y distinto a los demás participantes.

La solución pasa por mecanismos de *Proof of Personhood* (PoP). El stack recomendado incluye agregadores como [Gitcoin Passport](https://passport.gitcoin.co/), que suma puntos por actividad social y *on-chain*, o soluciones de biometría y red de confianza como [World ID](https://worldcoin.org/world-id) y [Proof of Humanity](https://www.proofofhumanity.id/).

El patrón habitual es establecer un "umbral de humanidad" (por ejemplo, una puntuación mínima en Passport) que actúe como compuerta para permitir la acción de votar o reclamar, evitando solicitar un KYC real si no es estrictamente obligatorio por ley.

### Redes Sociales o Comunidades

Si estás construyendo una plataforma social, un juego o un club de miembros, el valor reside en el historial y el contexto del usuario.

Una dirección hexadecimal vacía resulta impersonal y genera el problema del arranque en frío. Para fomentar la interacción, necesitas nombres legibles, avatares y una reputación previa que aporte confianza.

La solución se basa en aprovechar el grafo social *on-chain* y los datos públicos. El stack ideal incorpora [ENS](https://ens.domains/) para nombres legibles, protocolos como [Lens Protocol](https://www.lens.xyz/) o [Farcaster](https://www.farcaster.xyz/) para importar seguidores y contenido, y credenciales como [POAP](https://poap.xyz/) para reflejar el historial de participación.

El patrón de diseño implica que al conectar la *wallet*, la aplicación lea automáticamente el perfil para poblar la biografía y el avatar del usuario, utilizando además la tenencia de ciertos NFTs para desbloquear canales exclusivos o funcionalidades específicas.

### Onboarding masivo para usuarios no nativos

Para aplicaciones de consumo masivo (*Consumer Crypto*) dirigidas a usuarios que no son nativos del ecosistema cripto, la prioridad es minimizar la fricción.

Obligar al usuario a instalar una extensión de navegador, guardar una frase semilla de 12 palabras y comprender el concepto de gas suele resultar en una pérdida drástica de conversión.

La solución tecnológica es la abstracción de cuentas combinada con el inicio de sesión social. Herramientas de infraestructura como [Privy](https://www.privy.io/) o [Dynamic](https://www.dynamic.xyz/) son fundamentales en este stack.

El mecanismo permite la autenticación mediante correo electrónico o redes sociales, generando una *wallet* "invisible" (*embedded wallet*) en segundo plano. El patrón comienza con una experiencia federada similar a la Web2, donde el usuario entra con un clic, permitiendo una transición hacia la auto-custodia real mediante la exportación de claves en una etapa posterior, lo que se conoce como descentralización progresiva.

### Resumen arquitectónico

No intentes reinventar la rueda construyendo tu propio sistema de identidad desde cero. Si construyes *fintech*, utiliza VCs *off-chain* con pruebas ZK. Si diseñas sistemas democráticos, implementa *Proof of Personhood*. Si tu foco es social, aprovecha los datos *on-chain* de ENS y Lens. Y si buscas consumo masivo, opta por *embedded wallets* y *social login*.


---
