# Identidad Web3

Una de las promesas fundamentales de web3 es devolver el control de la identidad a los individuos, no solo como cuestión de soberanía personal, sino porque concentrar este control en manos de terceros genera vulnerabilidades de seguridad sistémicas.

El objetivo es que cada persona pueda poseer y gestionar su propia identidad de forma autosoberana. En la práctica, esta visión no difiere radicalmente de lo que ya conocemos en el mundo físico: posees un DNI en España o un pasaporte que te pertenece, del cual eres custodio, y donde acumulas sellos y validaciones que acreditan tus accesos y atributos. La solución descentralizada replica este modelo mediante un pasaporte digital donde tu wallet personal actúa como contenedor de credenciales.

Esta aspiración se ha materializado como [Self-Sovereign Identity (SSI)](https://en.wikipedia.org/wiki/Self-sovereign_identity), o identidad autosoberana. Este principio establece que los individuos deben tener control completo sobre sus credenciales, datos personales y respecto a cómo se comparte, sin depender de autoridades centrales para validación o almacenamiento. El término fue popularizado en el artículo [The Path to Self-Sovereign Identity](https://www.lifewithalacrity.com/article/the-path-to-self-sovereign-identity/) de Christopher Allen.

Aunque esta visión es clara, existen diferentes perspectivas sobre cómo implementarla en una web3 que necesita saber de tí, porque la validación descentralizada y la composabildiad asi lo requiere. Antes de profundizar en las tensiones y modelos existentes, es fundamental establecer ciertos conceptos clave:

Un **identificador** es un código único que te representa en el sistema. Tu wallet de [MetaMask](https://metamask.io/), como [EOA](https://www.binance.com/es/academy/glossary/externally-owned-account-eoa), o un [SCW como CA](https://www.binance.com/en/academy/glossary/smart-contract-wallet), tiene una dirección hexadecimal (0x1234...abcd) que funciona como tu identificador en la blockchain, un código que permite a los sistemas localizarte y comunicarse contigo. Este es un ejemplo simple, existen otros identificadores más formales como el [DID (Decentralized Identifier)](https://www.w3.org/TR/did-core/), que veremos más adelante. Lo importante es que un identificador no es una identidad, lo es según las relaciones que establecemos con él.

Una **atestación** es una declaración firmada digitalmente por un emisor que da fe o certifica ciertos atributos, afirmaciones o hechos sobre un sujeto. En términos simples, es cuando alguien con autoridad reconocida (una universidad, un empleador, una organización) confirma algo sobre ti de forma verificable. Por ejemplo, una universidad puede atestiguar que completaste un grado académico, o una empresa puede atestiguar que trabajaste para ella durante cierto período.

Una **credencial** es cualquier evidencia o documento firmado que puedes presentar por ti mismo, para demostrar algo o probar que tienes ciertos derechos o atributos. Habrás notado que se parece mucho a una atestación, y es normal: para [W3C](https://www.w3.org/) una atestación es el acto que genera una credencial, es la declaración o certificación en sí, algo más genérico que una credencial. Mientras una credencial se usa en el contexto de la identificación en posesión de un **sujeto**, la atestación existe en un contexto más de validación o acreditación de **hechos** en el mundo de la seguridad.

Una **identidad** es la representación reconocible y significativa de quién eres en un contexto social. No puedes decirle a alguien "envíame dinero a cero-equis-uno-dos-tres-cuatro...a-be-ce-de" sin que sea confuso y propenso a errores. Necesitas algo que los humanos puedan entender y recordar. Aquí entra en juego tu **marca personal**: un nombre legible y una imagen (foto de perfil) que te distingan. Una identidad se construye y verifica gracias a una o varias credenciales, y preferimos este término en lugar de "atestación" en este contexto porque la identidad es algo que tú posees y gestionas como sujeto, mientras que la atestación es algo, un hecho, que otros dicen.

## Conociendo la situación actual del los actores

La situación actual es complicada, hay varios actores y todos tienen sus intereses claros y su visión:

**Las bigtech en web2: Siloed/Traditional**:

Por una parte, las grandes tecnológicas (*Big Tech*), dominadoras de la [Web2](https://ethereum.org/en/developers/docs/web2-vs-web3/) en plataformas centralizadas como redes sociales y servicios cloud, gestionan una identidad digital que no te pertenece realmente. Cuando creas una cuenta en Facebook, Google o cualquier plataforma digital, la empresa almacena tu información, controla el acceso a ella y puede modificarla, censurarla o eliminarla sin tu consentimiento previo. Esta fragmentación de identidad entre múltiples plataformas que no se comunican entre sí es lo que técnicamente se conoce como [siloed identity](hhttps://medium.com/evernym/the-three-models-of-digital-identity-relationships-ca0727cb5186), donde cada servicio mantiene tu información aislada en su propio silo.

Este modelo centralizado genera varios problemas fundamentales. Primero, existe un riesgo de seguridad significativo porque todas tus credenciales están almacenadas en servidores centralizados que se convierten en objetivos atractivos para hackers. Segundo, no tienes portabilidad: tu reputación en Amazon no sirve en eBay, tu historial profesional en LinkedIn no se transfiere a otras plataformas. Tercero, dependes completamente de la plataforma: si deciden cerrar tu cuenta, pierdes años de datos, conexiones y reputación acumulada. Esta dependencia crea lo que se denomina [vendor lock-in](https://en.wikipedia.org/wiki/Vendor_lock-in), donde quedas atrapado en el ecosistema de un proveedor específico sin capacidad real de migrar tu identidad y datos a alternativas.

Además, el modelo centralizado crea problemas de privacidad. Para usar la mayoría de servicios digitales, debes revelar más información de la necesaria. Si quieres entrar a un sitio para mayores de edad, tienes que proporcionar tu fecha de nacimiento completa cuando en realidad solo necesitan saber que eres mayor de 18 años.

**Gobiernos y reguladores**:

Por otra parte los gobiernos y reguladores están desarrollando sus propios marcos normativos para la identidad digital. En concreto en Europa como el mayor referente, la regulación [eIDAS 2.0](https://digital-strategy.ec.europa.eu/en/policies/eidas-regulation) y su implementación de European Digital Identity Wallet, ofrece un equilibrio entre el control institucional y la autonomía del usuario.

Además, viendo el problema de Web2, a partir de 2026, plataformas de gran tamaño como Meta (Facebook, Instagram), Amazon, Apple, Booking.com, TikTok y Zalando, etc estarán obligadas por ley a aceptar la European Digital Identity Wallet (EUDI Wallet) como método válido de autenticación e identificación.

Esto significa que estos servicios no pueden rechazar este método de identificación cuando un usuario elija utilizarlo. Para los ciudadanos: El uso de la cartera digital europea es voluntario. Los ciudadanos pueden elegir si desean obtener y utilizar esta identidad digital, y los Estados miembros deben proporcionar métodos alternativos de identificación tradicionales para aquellos que no deseen adoptarla. No existe obligación legal de que los ciudadanos usen este sistema para su vida cotidiana. Sin embargo, la regulación cubre sectores amplios donde los servicios deben aceptar eIDAS 2.0: banca, transporte, energía, seguridad social, sanidad, suministro de agua, infraestructura postal, infraestructura digital, educación y telecomunicaciones. Aunque usar la cartera digital sea voluntario para ciudadanos, la amplitud de sectores obligados a aceptarla significa que, en la práctica, se convierte en un estándar de facto para identidad digital en Europa.

**Identidad federada: cuando BigTech se convierte en el intermediario**:

La industria reconoció tempranamente que obligar a usuarios a crear cuentas separadas en cada sitio web era insostenible. La solución que emergió fue el modelo de identidad federada: permite que un proveedor de identidad externo actúe como intermediario de confianza. Cuando hoy encuentras botones de "Sign in with Google", "Sign in with Apple" o "Sign in with Facebook" en prácticamente cualquier aplicación o servicio digital, estás usando este modelo basado principalmente en [OpenID Connect (OIDC)](https://openid.net/connect/), una capa de identidad construida sobre [OAuth 2.0](https://oauth.net/2/) que extiende su framework de autorización con capacidades de autenticación. [SAML](https://en.wikipedia.org/wiki/Security_Assertion_Markup_Language) es un protocolo alternativo más antiguo que todavía se usa en contextos empresariales.

Este enfoque resolvió problemas prácticos significativos: ya no necesitas recordar docenas de contraseñas diferentes, ni repetir procesos de registro tediosos en cada sitio. Sin embargo, simplemente trasladó la centralización a un nivel superior. En lugar de tener tu identidad fragmentada en múltiples silos, ahora depende de un puñado de gigantes tecnológicos que actúan como guardianes. Google, Apple, Facebook y Microsoft se han convertido en los IDPs (Identity Providers) dominantes, intermediando la mayoría de relaciones digitales en Internet. Si una de estas compañías cierra tu cuenta o decide que no cumples sus términos de servicio, pierdes acceso simultáneamente a docenas o cientos de servicios que dependen de esa identidad federada.

En 2026, este modelo no solo persiste sino que se ha convertido en el método de autenticación más usado globalmente en aplicaciones Web2. Su relevancia para Web3 es doble y aparentemente contradictoria. Por una parte, muchas dApps pragmáticamente implementan autenticación híbrida: ofrecen "Sign-In with Ethereum" para usuarios nativos crypto, pero también "Sign-In with Google" para facilitar onboarding gradual desde Web2 sin la fricción de gestionar claves privadas desde el primer momento.

**OpenID4VC: cuando los IDPs se transforman en emisores de credenciales**:

Por otra parte, el estándar [OpenID4VC (OpenID for Verifiable Credentials)](https://openid.net/sg/openid4vc/) está transformando el panorama al convertir IDPs tradicionales en emisores de credenciales verificables. Esto significa que Google o Apple pueden emitir VCs que el usuario guarda en su wallet Web3 o [EUDI Wallet europeo](https://digital-strategy.ec.europa.eu/es/factpages/european-digital-identity-wallet), creando un puente entre la identidad federada Web2 y las credenciales autosoberanas.

La diferencia fundamental con la federación tradicional es arquitectónica: en lugar de que Google intermedie cada login manteniendo control perpetuo, ahora Google puede emitir una credencial verificable una vez que tú guardas en tu wallet y presentas donde quieras sin su participación posterior. El IDP sigue siendo el emisor inicial, pero pierde el rol de intermediario permanente que caracteriza a la federación clásica.

Paralelamente, emisores especializados como [Fractal ID](https://www.fractal.id/) o [Civic](https://www.civic.com/) operan como emisores nativos de VCs para KYC, realizando verificación una vez y emitiendo una credencial que tú custodias y presentas donde necesites, sin intermediación posterior. Estos proveedores nunca fueron IDPs en el sentido federado, desde su diseño inicial operan bajo el paradigma de credenciales verificables autosoberanas.

La distinción crucial es que eIDAS 2.0 establece dos niveles de confianza: **credenciales cualificadas**, emitidas por Qualified Trust Service Providers (QTSPs) certificados bajo eIDAS con reconocimiento legal pleno en toda la UE, y **credenciales no cualificadas**, emitidas por proveedores privados como Fractal ID o Civic, técnicamente compatibles con EUDI Wallet pero sin el mismo peso legal que las gubernamentales. Para casos críticos como identidad oficial o edad legal, predominarán las credenciales cualificadas; para casos de uso menos regulados como membresías o reputación, las credenciales privadas seguirán siendo válidas y útiles.

**Web3 con KYC/AML**:

Adicionalmente, en lo referente al cumplimiento normativo (*compliance*) de plataformas cripto o Web3 con KYC/AML, debemos reconocer una realidad incómoda: [KYC](https://en.wikipedia.org/wiki/Know_your_customer) (*Know Your Customer*) y [AML](https://en.wikipedia.org/wiki/Money_laundering#Anti-money_laundering) (*Anti-Money Laundering*) no representan identidad descentralizada, sino identidad centralizada tradicional operando dentro de Web3 por obligación legal. Esta distinción es fundamental para entender correctamente el ecosistema.

Cada exchange donde compras ETH o BTC requiere procesos KYC rigurosos: pasaporte, prueba de domicilio, selfie sosteniendo tu documento, declaraciones de fuente de fondos. Este proceso es completamente centralizado y contradice frontalmente los principios de identidad autosoberana. Entregas tus datos personales más sensibles a una empresa privada que los almacena en sus servidores, exactamente el modelo centralizado que queremos superar.

¿Por qué existe esta contradicción en un ecosistema que promete descentralización? Regulación. Los gobiernos han implementado marcos regulatorios estrictos que obligan a cualquier entidad que facilite conversión entre fiat y criptomonedas a implementar controles KYC/AML. Regulaciones como la [5th Anti-Money Laundering Directive (5AMLD)](https://eur-lex.europa.eu/eli/dir/2018/843/oj) en Europa o el [Bank Secrecy Act](https://www.fincen.gov/resources/statutes-and-regulations/bank-secrecy-act) en Estados Unidos existen para prevenir lavado de dinero, financiamiento del terrorismo y evasión fiscal.

El resultado es que la mayoría de usuarios comprometen su privacidad desde el momento cero. Tu primer contacto con crypto probablemente fue entregar tu identidad legal completa a Coinbase o Binance. Incluso protocolos [DeFi](https://ethereum.org/en/defi/) descentralizados como [Uniswap](https://uniswap.org/) o Aave enfrentan presión regulatoria para implementar restricciones geográficas y verificación de identidad cuando alcanzan volúmenes significativos.

Protocolos como [Aave Arc](https://aave.com/) experimentaron con "DeFi permisionado" donde solo usuarios KYC-verificados podían participar. [MakerDAO](https://makerdao.com/) discute implementar KYC para activos del mundo real (RWA). DAOs grandes enfrentan dilemas similares: ¿cómo cumplir obligaciones fiscales sin comprometer pseudonimidad de miembros?

La identidad descentralizada teórica choca con las realidades del sistema financiero tradicional. Mientras los estados-nación controlen las rampas de entrada y salida del ecosistema crypto, KYC centralizado será inevitable para la mayoría de participantes. Los puristas argumentan que esto es temporal, que eventualmente viviremos completamente on-chain. Los pragmáticos reconocen que la regulación no desaparecerá, y que sistemas híbridos son el futuro más probable.

**Identidad y privacidad off-chain**:

El modelo off-chain con credenciales privadas basado en [Decentralized Identifiers (DIDs)](https://www.w3.org/TR/did-core/), [Verifiable Credentials (VCs)](https://www.w3.org/TR/vc-data-model/) y [Verifiable Presentations](https://www.w3.org/TR/vc-data-model/#presentations) maximiza privacidad mediante control del usuario. Tus credenciales viven en tu wallet bajo tu custodia exclusiva, solo tú decides cuándo y a quién mostrarlas, y puedes usar [Zero-Knowledge Proofs](https://ethereum.org/en/zero-knowledge-proofs/) para revelar el mínimo necesario. Un smart contract no puede simplemente "leer" si tienes un diploma universitario, necesitas activamente presentar una prueba. Esto protege tu privacidad pero destruye la composabilidad automática: los protocolos DeFi no pueden consultar instantáneamente tu historial crediticio, las DAOs no pueden verificar automáticamente membresías, los NFT marketplaces no pueden filtrar automáticamente usuarios por jurisdicción.

Proyectos como [Privado ID](https://www.privado.id/) (anteriormente Polygon ID) representan esta visión de identidad SSI más purista, priorizando la privacidad aunque afectando la composabilidad en Web3. Existen además emisores como [Fractal ID](https://www.fractal.id/) o [Civic](https://www.civic.com/) que facilitan el cumplimiento de KYC necesario para ciertas dApps, actuando como puentes entre la identidad legal y el ecosistema descentralizado.

> Puedes conocer más sobre este protocolo en [Protocolo DID](../infrastructure/identity/did-protocol.md)

**Identidad, reputación on-chain y grafo social**:

La propuesta de Vitalik Buterin y la Ethereum Foundation, cristalizada en el paper ["Decentralized Society: Finding Web3's Soul"](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763), apuesta por los Soulbound Tokens (SBTs) como primitiva fundamental de identidad basada en la reputación. Esta visión está diseñada específicamente para el ecosistema [Ethereum](https://ethereum.org/): tanto la mainnet L1 como todas las L2s compatibles con EVM ([Optimism](https://www.optimism.io/), [Arbitrum](https://arbitrum.io/), [Base](https://base.org/), [Polygon](https://polygon.technology/), etc.).

Su visión es que todo debe estar on-chain para máxima composabilidad: smart contracts leyendo directamente tus credenciales públicas no transferibles, sin necesidad de infraestructura off-chain compleja. La privacidad, desde su perspectiva, se resuelve en capas superiores mediante Zero-Knowledge Proofs, [stealth addresses](https://vitalik.eth.limo/general/2023/01/20/stealth.html) o L2s con privacidad integrada, no es responsabilidad del sistema de identidad base.

Esta filosofía prioriza la simplicidad técnica y la transparencia: si no estás dispuesto a aceptar que blockchain es fundamentalmente pública y transparente, quizás Web3 no es el ecosistema adecuado, visión que ya explicamos en [privacidad web3](4-3-challenges-privacy.md). La portabilidad cross-chain no es una preocupación central porque asumen que el ecosistema Ethereum (L1 + L2s compatibles) dominará.

Aquí es donde [Account Abstraction](https://ethereum.org/en/roadmap/account-abstraction/) transforma arquitectónicamente el concepto de identidad on-chain. En el modelo tradicional de [EOA](https://www.binance.com/es/academy/glossary/externally-owned-account-eoa), tu identidad y tu método de autenticación son inseparables: la clave privada que controla tu wallet es tu identidad. Con Account Abstraction mediante [ERC-4337](https://eips.ethereum.org/EIPS/eip-4337), tu identidad migra completamente on-chain al vivir en un [Smart Contract Wallet (SCW)](https://www.binance.com/en/academy/glossary/smart-contract-wallet). Este smart contract se convierte en tu contenedor de identidad persistente: almacena tus SBTs, acumula tu reputación, posee tus [POAPs](https://blog.bit2me.com/es/poap-proof-of-attendance-protocol/), mantiene tu historial de gobernanza. La EOA, que antes era tu identidad misma, se convierte simplemente en una credencial de acceso, una entre muchas formas ante tu identidad real que vive en el contrato.

Esta separación es fundamental porque desacopla tu identidad (la cuenta smart contract con su dirección pública) de tus métodos de autenticación (las claves que usas para controlarla). Puedes rotar tus EOAs periódicamente por seguridad, añadir autenticación biométrica, implementar recuperación social mediante guardianes, delegar permisos específicos a otras cuentas para operaciones limitadas sin ceder control total, todo sin cambiar tu identidad pública ni perder tu historial acumulado. Si tu EOA actual es comprometida, simplemente revocas su permiso en el smart contract y añades una nueva, pero tu identidad on-chain permanece intacta en la misma dirección del contrato. La delegación resulta especialmente valiosa para casos de uso como permitir que una aplicación específica ejecute transacciones predefinidas en tu nombre sin acceso completo a tu cuenta, o autorizar a un gestor de tesorería de una DAO a mover fondos dentro de límites establecidos. Sin embargo, esta flexibilidad tiene un precio: intercambias la simplicidad y superficie de ataque mínima de las EOAs por la complejidad y riesgos de bugs en smart contracts, tema que exploraremos en detalle más adelante.

Esta arquitectura materializa completamente la visión de identidad on-chain: tu reputación emerge de tus relaciones y acciones verificables que quedan registradas en la blockchain. Tu reputación se construye mediante quién te sigue, qué DAOs te aceptan como miembro, qué contribuciones open-source has hecho, qué eventos has atendido ([POAPs](https://poap.xyz/)), cuánto has participado en gobernanza. No necesitas que Stanford certifique tu inteligencia, solo si has contribuido código a protocolos importantes que la comunidad valora. Este modelo es inherentemente descentralizado y resistente a censura porque ninguna autoridad única puede revocar tu reputación social, pero es vulnerable a manipulación (comprar seguidores, crear narrativas falsas) y no satisface requisitos legales en la mayoría de jurisdicciones.

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

> Puedes conocer más sobre esta infraestructura en [Capa de Atestación](../infrastructure/identity/attestation-infrastructure.md).

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

La fragmentación no es técnica sino filosófica. Web3 promete soberanía individual sobre identidad y activos, pero la mayoría de humanos prefieren conveniencia sobre soberanía. Los usuarios no quieren gestionar claves criptográficas de igual forma que no quieren gestionar certificados SSL para navegar la web. La pregunta incómoda es: si el 95% de usuarios elige voluntariamente custodia delegada por conveniencia, ¿hemos fallado en la promesa de descentralización, o simplemente hemos descubierto que la mayoría de personas no valora la soberanía lo suficiente como para aceptar su costo?

Esta cuestión tiene otra cara de la moneda, frente a la demagógica frase de gestionar certificados SSL, vale preguntarse: en un mundo digital donde tu identidad puede significar la pérdida de derechos fundamentales, ¿no es el robo de tu identidad ante el banco o la administración algo crítico? Web2 ha creado una facilidad que en realidad es fragilidad. Todos llevamos nuestro DNI o pasaporte físico en la cartera de nuestro bolsillo, custodiando personalmente credenciales que acreditan nuestra identidad legal. Este modelo tradicional ya es identidad autosoberana descentralizada: tú custodias el documento, nadie más puede presentarlo por ti, y las instituciones solo validan su autenticidad cuando lo presentas voluntariamente. El debate no es si la auto-custodia es viable, es si la conveniencia digital justifica renunciar a un principio que funciona desde hace siglos. No casualmente, incluso regulaciones como eIDAS 2.0 reconocen esta realidad adoptando wallets basadas en DIDs: frente a problemas sociales y económicos en la era digital, la auto-custodia deja de ser opcional para convertirse en necesaria.

Dentro de las visiones que sí comparten el principio de descentralización y auto-soberanía de identidad, encontramos dos aproximaciones fundamentales. Por un lado, el modelo basado en autoridades formales que emiten credenciales verificables, con clasificaciones cualificadas o no cualificadas según marcos como eIDAS. Por otro, el modelo que construye identidad mediante reputación emergente en la red, donde tu valor reside en tus acciones verificables y el reconocimiento de la comunidad, los valores DeSoc que veremos más adelante.

La realidad pragmática en 2026 es segmentación de mercado. Aplicaciones financieras manejando valores significativos (DeFi protocols, trading avanzado, tesorería de DAOs) asumen auto-custodia porque sus usuarios sofisticados valoran seguridad sobre conveniencia. Aplicaciones de consumo masivo (gaming, social, collectibles casuales) implementan embedded wallets porque priorizan crecimiento de usuario sobre purismo ideológico. La descentralización progresiva, donde usuarios comienzan con wallets custodiadas y gradualmente migran hacia auto-custodia conforme aprenden, es el compromiso más viable, aunque en la práctica la mayoría nunca completa esa migración.

### Privacidad vs. composabilidad: on-chain vs off-chain

La primera tensión fundamental es dónde viven tus datos de identidad y quién puede acceder a ellos.

El modelo **off-chain con credenciales privadas** (DIDs, VCs, VPs) maximiza privacidad mediante control del usuario. Tus credenciales viven en tu wallet bajo tu custodia exclusiva, solo tú decides cuándo y a quién mostrarlas, y puedes usar [Zero-Knowledge Proofs](https://ethereum.org/en/zero-knowledge-proofs/) para revelar el mínimo necesario. Un smart contract no puede simplemente "leer" si tienes un diploma universitario, necesitas activamente presentar una prueba. Esto protege tu privacidad pero destruye la composabilidad automática: los protocolos DeFi no pueden consultar instantáneamente tu historial crediticio, las DAOs no pueden verificar automáticamente membresías.

El modelo **on-chain público** (SBTs, attestations on-chain, POAPs) maximiza composabilidad sacrificando privacidad. Tus credenciales son tokens en tu dirección que cualquier smart contract puede leer sin permiso. Un protocolo de lending puede verificar instantáneamente que posees un SBT de "buen pagador" emitido por otro protocolo y ajustar tus tasas automáticamente. Una DAO puede requerir posesión de ciertos SBTs para habilitar votación. Este modelo es técnicamente simple y extremadamente poderoso para construir sistemas componibles, pero significa que toda tu identidad es un libro abierto: cualquiera puede ver todos tus SBTs, correlacionar tu actividad, y construir perfiles detallados de tu vida digital.

Más que una imposibilidad técnica insuperable, el verdadero 'punto medio' fracasa hoy por la falta de uniformidad en el acceso. A diferencia de la identidad federada de la Web2 (Login con Google/Apple), que ofrece una entrada fluida y universal, la Web3 obliga al usuario a navegar un ecosistema fragmentado: o te sumerges en la complejidad técnica de las wallets privadas, o dependes de logins tipo Web2 que sacrifican la soberanía. El sacrificio real no es solo entre privacidad y composabilidad, sino en la cordura del usuario, que aún no dispone de un estándar que haga la identidad tan invisible y sencilla como un toque biométrico en el móvil.

### Autoridades formales vs. reputación emergente: credenciales vs grafo social

La segunda tensión es epistemológica: ¿qué constituye identidad verificable?

El modelo de **autoridades y credenciales formales** (gobiernos con eIDAS, universidades emitiendo diplomas, empresas certificando experiencia) asume que la identidad se construye mediante validación de instituciones reconocidas. Tu diploma vale porque Stanford University lo firmó, no porque la comunidad cree que eres inteligente. Este modelo replica estructuras del mundo físico en blockchain: necesitas emisores con autoridad real, mecanismos de revocación cuando las credenciales caducan, y probablemente compliance regulatorio. Funciona bien para integración con sistemas legales y financieros tradicionales, pero centraliza el poder de validación en manos de instituciones que pueden excluir, discriminar o censurar.

El modelo de **grafo social y reputación emergente** (Lens Protocol, Farcaster, sistemas de reputación on-chain) argumenta que la identidad emerge de tus relaciones y acciones verificables. Tu reputación se construye mediante quién te sigue, qué DAOs te aceptan como miembro, qué contribuciones open-source has hecho, qué eventos has atendido (POAPs), cuánto has participado en gobernanza. No necesitas que Stanford certifique tu inteligencia si has contribuido código a protocolos importantes que la comunidad valora. Este modelo es inherentemente descentralizado y resistente a censura porque ninguna autoridad única puede revocar tu reputación social, pero es vulnerable a manipulación (comprar seguidores, crear narrativas falsas) y no satisface requisitos legales en la mayoría de jurisdicciones.

Ambos modelos coexisten en Web3 porque sirven necesidades diferentes. Si necesitas abrir una cuenta bancaria o probar tu edad legalmente, requieres credenciales formales de autoridades reconocidas. Si necesitas demostrar reputación en comunidades descentralizadas para recibir funding de una DAO, tu grafo social y contribuciones on-chain son más relevantes que cualquier diploma. La tensión surge cuando los sistemas adoptan posturas extremas y puristas. Los protocolos que solo aceptan reputación emergente crean una paradoja excluyente: si acabas de llegar al ecosistema y no tienes historial on-chain acumulado, POAPs de eventos previos, ni membresías en DAOs establecidas, simplemente no puedes participar porque te falta la reputación que solo se obtiene participando. Por otro lado, los sistemas que únicamente reconocen credenciales formales emitidas por instituciones tradicionales reproducen exactamente las mismas barreras de acceso, burocracia y centralización del poder que Web3 prometía superar.

### Auto-custodia vs. conveniencia: el dilema del onboarding masivo

La tercera tensión fundamental es quién controla realmente tus claves privadas, y por extensión, tu identidad y activos.

El modelo de **auto-custodia pura** (self-custody) es el ideal cypherpunk original: tú generas, almacenas y gestionas tus propias claves privadas mediante wallets no-custodiales como MetaMask, Ledger o Trezor. Nadie más puede acceder a tus fondos ni censurar tus transacciones. Si pierdes tus claves, nadie puede recuperarlas por ti. Esta soberanía absoluta viene con responsabilidad absoluta: debes proteger tu frase semilla de 12 o 24 palabras contra pérdida, robo, y errores de usuario. Para usuarios técnicamente sofisticados que entienden las implicaciones, este modelo ofrece garantías de seguridad y resistencia a censura incomparables.

El problema es que la auto-custodia crea fricción masiva para adoption retail. Los usuarios promedio no están preparados para gestionar secretos criptográficos cuya pérdida resulta en pérdida permanente e irrecuperable de fondos. Las frases semilla son confusas, los usuarios reutilizan contraseñas débiles, comparten capturas de pantalla accidentalmente, caen en phishing. La experiencia de onboarding tradicional (instalar extensión de navegador, anotar 12 palabras, entender conceptos de gas, confirmar transacciones manualmente) genera tasas de abandono superiores al 90% para usuarios no-cripto.

El modelo de **wallets custodiadas y embedded wallets** (WaaS) resuelve este problema de UX trasladando la custodia a un tercero de confianza. Servicios como Privy, Dynamic o Magic custodian tus claves cifradas en su infraestructura, permitiéndote acceder mediante credenciales familiares como email o OAuth social. La experiencia se vuelve indistinguible de Web2: un clic y estás dentro, sin frases semilla ni gestión manual de gas. Para aplicaciones de consumo masivo, esto elimina la barrera de entrada más grande.

Pero este modelo replica exactamente los problemas que blockchain pretendía resolver. Si el proveedor WaaS sufre un hack, experimenta downtime, o decide cerrar el servicio, pierdes acceso a tus activos. Si el proveedor implementa compliance agresivo por presión regulatoria, puede congelar tu cuenta sin aviso. Aunque muchos servicios ofrecen "exportación de claves" para migrar eventualmente a auto-custodia, la mayoría de usuarios nunca ejecutan esta transición, permaneciendo indefinidamente en un modelo centralizado.

Existe un punto medio emergente mediante **custodia programable y social recovery** que combina conveniencia con auto-custodia genuina. Account Abstraction permite implementar lógica de recuperación social donde un conjunto de guardianes (amigos, familiares, otros dispositivos tuyos) pueden colectivamente recuperar tu cuenta si pierdes las claves, sin que ningún guardián individual tenga control unilateral. Servicios como Argent implementan esto, ofreciendo UX simple sin sacrificar completamente la auto-custodia.

La wallet más adoptada globalmente, [MetaMask](https://metamask.io/), ha evolucionado significativamente en 2024-2025 para cerrar esta brecha entre conveniencia y auto-custodia. Su [Social Login](https://support.metamask.io/configure/wallet/social-login/) permite crear wallets mediante autenticación con Google o Apple ID. Adicionalmente, el [Smart Accounts Kit](https://docs.metamask.io/smart-accounts-kit/) implementa smart contract wallets con delegaciones granulares, permisos específicos mediante ERC-7715, gas abstraction (permitiendo que aplicaciones paguen el gas de los usuarios), y cuentas multichain coordinadas. Este enfoque representa la materialización práctica de Account Abstraction en la wallet con mayor adopción del ecosistema, democratizando capacidades avanzadas que antes requerían implementaciones especializadas. Para explorar en profundidad estas tecnologías y su impacto en la experiencia de usuario, consulta [experiencia de usuario en Web3](8-1-user-experience.md).

### Account Abstraction: separando identidad de claves criptográficas

Como ya vimos anteriormente, [Account Abstraction (AA)](https://ethereum.org/en/roadmap/account-abstraction/) mediante [ERC-4337](https://eips.ethereum.org/EIPS/eip-4337) separa fundamentalmente tu identidad (la cuenta smart contract) de tus métodos de autenticación (las claves que la controlan), habilitando nuevos casos de uso que exploramos en detalle en [experiencia de usuario en Web3](8-1-user-experience.md).

El impacto de Account Abstraction sobre las diferentes visiones de identidad es profundo pero asimétrico. Para el modelo de reputación on-chain y grafo social, AA representa una mejora fundamental. La reputación puede finalmente vivir en la cuenta (la dirección del smart contract) independientemente de las claves que la controlan. Esto resuelve el problema crítico de key rotation: puedes rotar tus claves de firma periódicamente por seguridad, cambiar de dispositivo hardware, migrar de una clave ECDSA a esquemas post-cuánticos cuando sea necesario, todo sin crear una nueva identidad y perder tu historial. Tus POAPs, tus SBTs, tu membresía en DAOs, tu historial de contribuciones en Gitcoin, permanecen asociados a tu cuenta incluso cuando las claves subyacentes cambian completamente.

Para el modelo de credenciales verificables off-chain (DIDs/VCs), Account Abstraction introduce una tensión potencial. Hoy los emisores usan claves estáticas (EOAs) para firmar credenciales, permitiendo verificación completamente offline: tu wallet presenta la credencial y cualquiera puede validar la firma sin consultar la blockchain. Pero si en el futuro los emisores migraran a smart contract wallets con rotación de claves, la verificación requeriría consultas on-chain para confirmar que la clave de firma sigue siendo válida, sacrificando la autonomía offline que caracteriza a las VCs. Este dilema entre seguridad mediante key rotation versus portabilidad offline probablemente se resolverá con soluciones híbridas donde emisores mantengan claves dedicadas para credenciales.

Respecto a portabilidad cross-chain, AA no resuelve la fragmentación entre redes incompatibles. Tu smart account en Ethereum mainnet es un contrato completamente separado de cualquier cuenta en Solana, Cosmos o incluso otras L2s de Ethereum como Arbitrum u Optimism.

Protocolos como [LayerZero](https://layerzero.network/) o [Across](https://across.to/) experimentan con sincronización cross-chain de estados, permitiendo que acciones en una chain actualicen tu perfil en otras, pero esta coordinación añade complejidad, latencia y costos significativos. La visión a largo plazo de Account Abstraction asume que la mayoría de actividad convergirá en el ecosistema Ethereum (mainnet L1 + L2s compatibles con EVM) donde la composabilidad nativa es posible, aceptando que otras blockchains incompatibles permanecerán fragmentadas.

## Cuándo usar VCs, Attestation Layer o SBTs

Elegir la herramienta correcta depende de dos factores fundamentales: dónde necesitas que vivan los datos y quién debe tener acceso a verlos. Aunque las tres tecnologías pueden parecer similares, cada una resuelve una necesidad arquitectónica distinta.

Las **Verifiable Credentials (W3C)** son la elección obligada cuando manejas datos privados y sensibles. Su principal ventaja es que priorizan la privacidad del usuario manteniendo los datos off-chain en su dispositivo, no en la blockchain pública. Son ideales para casos como verificar la mayoría de edad mediante ZK-proofs sin revelar la fecha de nacimiento, credenciales educativas que no deseas exponer públicamente, o compliance regulatorio donde necesitas probar atributos ("pasé KYC", "no estoy sancionado") sin revelar identidad completa. El trade-off es una mayor complejidad técnica, ya que requieren wallets específicas para su gestión.

Por otro lado, la **Attestation Layer (como EAS)** es ideal para construir reputación pública y suministrar datos que los Smart Contracts deban leer automáticamente. A diferencia de las VCs, aquí se prioriza la eficiencia y la composabilidad sobre la privacidad. Son perfectas para sistemas de "Credit Scoring" en DeFi donde un protocolo necesita consultar tu historial on-chain instantáneamente y sin intermediarios. La contrapartida es que, por defecto, toda la información es pública.

Finalmente, los **Soulbound Tokens (SBTs)** brillan cuando el objetivo es la visibilidad social y el estatus. Al ser NFTs intransferibles, aparecen visualmente en galerías como OpenSea o Rainbow, lo que los hace perfectos para diplomas universitarios, medallas de gobernanza o certificados de asistencia a eventos. Su función es permitir que el usuario "luzca" el logro en su perfil público. Sin embargo, al igual que las attestations, carecen de privacidad y son más difíciles de actualizar o revocar una vez emitidos.

En resumen: usa VCs para proteger secretos personales, Attestations para alimentar lógica de contratos inteligentes, y SBTs para exhibir logros sociales permanentes.

## Sistemas de nombres descentralizados

Los sistemas de nombres descentralizados transforman direcciones blockchain incomprensibles en nombres legibles por humanos, creando una capa de identidad esencial para la adopción masiva de Web3.

**Usa un sistema de nombres (como ENS) cuando**:

- Necesitas que otros humanos te envíen pagos o interactúen contigo fácilmente
- Quieres una identidad pública reconocible en el ecosistema blockchain
- Buscas asociar múltiples datos públicos (avatar, redes sociales, direcciones) a un nombre memorable
- Priorizas la simplicidad y la adopción sobre la verificabilidad formal

**ENS: tu nombre en Ethereum**:

[Ethereum Name Service](https://ens.domains/) se ha convertido en el estándar de facto para identidad humana en el ecosistema Ethereum. Funciona de manera similar al [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) tradicional de internet (el sistema que convierte nombres como google.com en direcciones IP), pero completamente descentralizado. En lugar de que una organización como ICANN controle el registro de nombres, ENS utiliza [smart contracts](https://ethereum.org/en/smart-contracts/) (programas autoejecutables en blockchain) en Ethereum que cualquiera puede consultar y usar.

Cuando registras un nombre ENS como `tuNombre.eth`, estás creando un registro en blockchain que puede resolver a múltiples tipos de información. Lo más básico es asociar el nombre con tu dirección Ethereum, permitiendo que alguien te envíe ETH a `tuNombre.eth` en lugar de tener que copiar y pegar una dirección hexadecimal de 42 caracteres que es fácil de confundir.

Pero ENS va mucho más allá de simplemente resolver nombres a direcciones. Puedes asociar tu nombre con direcciones de múltiples blockchains (Bitcoin, Dogecoin, Litecoin), con tu avatar [NFT](https://ethereum.org/en/nft/) (token no fungible que representa propiedad digital única), con tu sitio web descentralizado almacenado en [IPFS](https://ipfs.tech/) (sistema de archivos distribuido peer-to-peer), con tus handles de redes sociales, con tu email, o con cualquier dato de texto arbitrario que quieras hacer público.

El registro de nombres ENS funciona mediante un modelo de renovación anual. No compras el nombre permanentemente, sino que pagas una cuota anual que va a un contrato del DAO de ENS. Los nombres de 4 o más caracteres siguen un sistema first-come-first-served con precio anual fijo basado en la longitud del nombre. Los nombres muy cortos de 3 caracteres utilizan un sistema de subastas holandesas. Este modelo previene la especulación extrema y el acaparamiento de nombres, aunque ciertamente existe un mercado secundario activo donde nombres populares se venden por precios significativos.

Un aspecto poderoso de ENS es que funciona bidireccionalmente. La resolución más obvia es cuando escribes un nombre: si quieres enviar fondos y escribes `maria.eth`, el sistema busca a qué dirección (`0x123...abc`) corresponde ese nombre para ejecutar la transacción. Esto es resolución directa: nombre → dirección.

Pero ENS también permite el camino inverso, y aquí está la verdadera magia. Imagina que ves una transacción en Etherscan que proviene de la dirección `0x123...abc`. Normalmente verías solo ese código hexadecimal incomprensible. Sin embargo, si esa dirección tiene configurada la resolución inversa en ENS, Etherscan consultará "¿qué nombre ENS está asociado con `0x123...abc`?" y te mostrará `maria.eth` en su lugar. Esto es resolución inversa: dirección → nombre. Lo mismo ocurre en wallets, aplicaciones DeFi, marketplaces de NFTs: en lugar de códigos hexadecimales, ves nombres legibles. Esto ha convertido a ENS en la identidad visual por defecto del ecosistema Ethereum: tu nombre .eth te representa en todas partes, haciendo la experiencia mucho más humana y menos técnica.

**Unstoppable Domains: identidad multi-chain**:

[Unstoppable Domains](https://unstoppabledomains.com/) ofrece una alternativa a ENS con un modelo diferente: compras el dominio una vez sin renovaciones anuales. Ofrece múltiples extensiones (.crypto, .nft, .blockchain, .bitcoin, .wallet, .dao, .x) y se enfoca en la compatibilidad multi-chain desde el principio.

A diferencia de ENS que está anclado principalmente en Ethereum, Unstoppable Domains resuelve direcciones para docenas de blockchains diferentes desde un solo nombre. Tu dominio `nombre.crypto` puede apuntar simultáneamente a tu dirección de Ethereum, Bitcoin, Polygon, Solana y muchas otras cadenas, simplificando la recepción de pagos cross-chain. Desde 2024, Unstoppable ha continuado expandiendo su soporte a blockchains adicionales y ecosistemas emergentes, reforzando su posición como solución multi-chain.

Unstoppable también integra funcionalidad de sitios web descentralizados. Puedes alojar un sitio web en IPFS y configurar tu dominio para que los navegadores compatibles (Brave, Opera) lo resuelvan directamente, creando una web realmente descentralizada y resistente a censura.

La principal diferencia filosófica es el modelo de propiedad: ENS favorece las renovaciones anuales para prevenir acaparamiento y mantener el espacio de nombres activo, mientras que Unstoppable favorece la propiedad perpetua como un activo digital permanente. Ambos enfoques tienen ventajas y el mercado está decidiendo qué modelo prevalece.

**Namecoin: el pionero de identidad descentralizada**:

Aunque hoy ENS domina el espacio de nombres descentralizados, [Namecoin](https://www.namecoin.org/) fue el proyecto pionero que demostró la viabilidad del concepto. Lanzado en 2011 como un fork de Bitcoin, Namecoin fue la primera blockchain alternativa (altcoin) y el primer sistema de nombres descentralizado.

Namecoin permite registrar dominios `.bit` que no pueden ser censurados ni confiscados por autoridades porque el registro está en blockchain. Originalmente diseñado como DNS alternativo resistente a censura, también permitía registro de identidades descentralizadas mediante el espacio de nombres `id/`. Un usuario podía registrar `id/alice` y asociar información de perfil, claves públicas, o cualquier dato arbitrario.

El sistema funciona mediante transacciones especiales que registran o actualizan nombres en la blockchain Namecoin. Como fork de Bitcoin, hereda su modelo de seguridad mediante minería Proof-of-Work, específicamente mediante merge-mining con Bitcoin (los mineros de Bitcoin pueden minar Namecoin simultáneamente sin costo adicional).

Aunque Namecoin demostró el concepto fundamental, su adopción fue limitada por varios factores. Primero, requería software especializado y configuración compleja para resolver dominios `.bit`, a diferencia del DNS tradicional integrado en todos los navegadores. Segundo, la experiencia de usuario era pobre comparada con sistemas centralizados. Tercero, la comunidad de desarrollo era pequeña y el proyecto carecía del momentum y financiamiento de proyectos más recientes.

Sin embargo, el legado de Namecoin es invaluable. Probó que los sistemas de nombres descentralizados son técnicamente viables, inspiró directamente a proyectos como ENS, y estableció principios que hoy consideramos fundamentales: control total del usuario sobre su identidad, resistencia a censura, y ausencia de autoridades centrales. ENS y otros sistemas modernos son evoluciones naturales del trabajo pionero de Namecoin, aprovechando las lecciones aprendidas y el ecosistema maduro de Ethereum.

## NFT Profile Pictures: identidad social visual

Más allá de nombres legibles, una de las formas más visibles y culturalmente significativas de identidad en Web3 son los NFT Profile Pictures o PFPs. Aunque técnicamente son simplemente tokens no fungibles que representan arte digital coleccionable, socialmente han evolucionado en un fenómeno de identidad mucho más profundo.

Cuando alguien en Twitter/X usa un [Bored Ape Yacht Club](https://boredapeyachtclub.com/) como avatar, no solo está mostrando una imagen, está señalizando membresía en una comunidad específica, status económico (los Bored Apes se vendieron por cientos de miles de dólares en su pico), y afinidad cultural con ciertos valores del ecosistema crypto. Lo mismo aplica para [CryptoPunks](https://www.larvalabs.com/cryptopunks) (los OG del espacio, con algunos vendiéndose por millones), [Azuki](https://www.azuki.com/), [Doodles](https://doodles.app/), o cualquiera de los miles de proyectos PFP que surgieron durante el boom NFT de 2021-2022.

Lo interesante es que estos NFTs funcionan como señales de identidad verificables on-chain. Cuando usas un Bored Ape como tu PFP, cualquiera puede verificar en blockchain que realmente posees ese token específico, no solo una copia de la imagen. Twitter/X implementó verificación de NFTs mediante [Twitter Blue](https://help.twitter.com/en/using-twitter/twitter-blue-labs#nft) (ahora X Premium) donde avatares verificados se muestran con forma hexagonal en lugar de circular, señalizando visualmente propiedad auténtica. Aunque esta feature ha tenido adopción variable, demuestra que incluso plataformas Web2 reconocen el valor de identidad verificable on-chain.

Los PFPs crean lo que algunos llaman "identity as a service": compras entrada a una comunidad, una estética, y una red social. Proyectos exitosos como Bored Apes construyeron clubes exclusivos con eventos presenciales, merchandise, y derechos comerciales sobre tu NFT específico. Poseer el NFT te da acceso a canales privados de Discord, eventos exclusivos, y airdrops de tokens relacionados. Tu PFP se convierte en tu identidad reconocible a través de múltiples plataformas: el mismo Ape que usas en Twitter aparece en tu perfil de Discord, en tu wallet conectada a dApps, en foros Web3.

Sin embargo, los PFPs también revelan limitaciones y problemas del modelo. Primero, el valor de identidad está completamente atado a valor financiero especulativo: cuando el precio de tu Ape cae 90%, tu señal de status también colapsa. Segundo, este modelo de identidad es inherentemente exclusionario: solo quienes pueden pagar precios floor de miles o decenas de miles de dólares pueden participar en ciertas comunidades. Tercero, la cultura PFP ha sido criticada por reducir identidad a consumo conspicuo: "eres lo que compras" llevado al extremo on-chain.

La evolución de PFPs también muestra la tensión entre identidad persistente y privacidad. Cuando tu Ape es tu identidad reconocible en todas partes, pierdes pseudonimidad: cualquiera puede rastrear todas tus interacciones on-chain asociadas a esa dirección. Algunos usuarios mantienen múltiples identidades: un PFP público para networking social, direcciones separadas para actividad financiera DeFi, wallets completamente anónimas para participación en DAOs sensibles.

Lo que los PFPs demuestran inequívocamente es que identidad en Web3 no es solo infraestructura técnica (DIDs, credenciales verificables), sino performance social y cultural. La forma más exitosa de identidad Web3 hasta la fecha no fue un protocolo DID elegante, fue gente pagando fortunas por monos pixelados para usarlos como avatares. Esta realidad pragmática debe informar cómo diseñamos sistemas de identidad futuros: la tecnología debe servir a necesidades sociales reales, no al revés.

## El reto arquitectónico: identidad fragmentada entre blockchains

Antes de explorar soluciones específicas de identidad, debemos entender un problema fundamental que define toda la arquitectura de Web3: **elegir una wallet no es elegir una herramienta, es elegir un ecosistema completo**. A diferencia de Web2, donde tu identidad de Google funciona universalmente, en Web3 no existe interoperabilidad real. Cada blockchain opera como un universo tribal separado con sus propios formatos de direcciones, estándares criptográficos, comunidades de desarrolladores, y lo más importante: infraestructura de identidad incompatible.

### Ecosistemas como bandos irreconciliables

La fragmentación de Web3 no es un bug temporal que se resolverá con mejores bridges o protocolos de interoperabilidad. Es una característica arquitectónica fundamental que refleja visiones filosóficas incompatibles sobre cómo debe funcionar blockchain.

**Team Ethereum/EVM**: Cuando un usuario instala MetaMask o cuando un developer implementa Privy/Dynamic para onboarding, no está haciendo una elección neutral de infraestructura. Está comprando entrada al ecosistema Ethereum: mainnet L1, todas las L2s compatibles con EVM (Arbitrum, Optimism, Base, Polygon, zkSync), y el universo de aplicaciones construidas sobre estos estándares. Tu identidad es una dirección 0x..., tus NFTs siguen ERC-721, tu reputación vive en contratos EVM, y tu grafo social probablemente usa Lens Protocol o Farcaster. Account Abstraction mediante ERC-4337, nombres mediante ENS, attestations mediante EAS: todo está diseñado para este mundo.

**Team Solana**: Phantom wallet y el ecosistema Solana operan en un universo paralelo. Las direcciones usan formato base58, los NFTs siguen el Token Program de Solana (no ERC-721), la finalidad es sub-segundo versus minutos en Ethereum, y las aplicaciones priorizan throughput masivo sobre descentralización máxima. Jupiter para DEX aggregation, Magic Eden para NFTs, Dialect para messaging: infraestructura completamente separada. Un usuario nativo de Solana no "visita" Ethereum mainnet, son mundos diferentes.

**Team Cosmos**: El ecosistema Cosmos con su Inter-Blockchain Communication (IBC) representa una tercera visión: soberanía de aplicaciones específicas mediante app-chains interconectadas. Wallets como Keplr, identidades basadas en direcciones cosmos..., y aplicaciones que pueden ser blockchains completas dedicadas. Osmosis para DEX, Juno para smart contracts, Celestia para data availability: arquitectura modular que Ethereum rechaza filosóficamente.

**Otros ecosistemas**: Polkadot con parachains, Avalanche con subnets, Near Protocol, Tezos, Algorand: cada uno con sus propias wallets nativas, estándares de tokens, comunidades de developers, y visiones incompatibles. No es que estos ecosistemas no puedan comunicarse técnicamente mediante bridges, es que sus comunidades, herramientas de desarrollo, y filosofías operan en paralelo sin convergencia real.

### La decisión que define tu producto

Esta realidad tribal significa que **antes de diseñar tu sistema de identidad, debes responder una pregunta estratégica fundamental: ¿en qué ecosistema vivirá tu aplicación?** Y esta decisión no es reversible fácilmente.

Si construyes una DAO de gobernanza usando Snapshot, Safe multisig, y voting power basado en tokens ERC-20, has elegido Team Ethereum. Tu aplicación simplemente no funcionará en Solana sin reescribirla completamente. Las credenciales verificables que emites usando EAS en Base no se pueden verificar nativamente en Cosmos. Tu grafo social en Lens Protocol no existe para usuarios de Solana.

Si construyes un juego NFT de alta frecuencia que requiere transacciones instantáneas y fees de centavos, probablemente necesitas Solana o Polygon. Pero entonces sacrificas acceso a la liquidez DeFi de Ethereum mainnet, integración con herramientas enterprise construidas sobre EVM, y composabilidad con la mayoría de protocolos DeFi establecidos.

Si construyes infraestructura crítica que requiere neutralidad máxima y resistencia a censura (por ejemplo, un oráculo descentralizado), quizás necesitas una app-chain en Cosmos con validadores propios. Pero entonces tu base de usuarios inicial es microscópica comparada con Ethereum o Solana, y necesitas convencer a usuarios de instalar otra wallet más.

**Las soluciones de abstracción son parches, no soluciones**: Herramientas como [OneBalance](https://www.onebalance.io/), [Socket](https://socket.tech/), o [Li.Fi](https://li.fi/) intentan abstraer esta complejidad mediante agregación cross-chain y routing inteligente de transacciones. Permiten que un usuario con fondos en Arbitrum ejecute una acción en Base sin bridges manuales, o que una aplicación acepte pagos en cualquier chain sin gestionar la complejidad. Son valiosas para reducir fricción operativa, pero no resuelven el problema fundamental: tu identidad, reputación y grafo social siguen fragmentados. Puedes mover valor entre chains, pero no puedes unificar tu historial de participación en governance de Ethereum con tus logros en gaming de Solana. La abstracción de liquidez no es equivalente a la portabilidad de identidad.

### La realidad multicadena del usuario

Un participante típico de Web3 no tiene una identidad: tiene múltiples identidades técnicamente desconectadas viviendo en universos paralelos. Una dirección Ethereum para NFTs y gobernanza, una dirección Solana para trading de alta frecuencia, quizás direcciones en Cosmos para participar en app-chains especializadas. Cada identidad es una persona digital completamente separada.

Tu reputación no es portable entre ecosistemas, y nunca lo será de forma nativa. Años de participación en governance de Ethereum mediante Snapshot y votaciones on-chain no se reconocen automáticamente en Solana porque Solana ni siquiera tiene los mismos primitivos de gobernanza. Las credenciales verificables que emites ancladas en Ethereum no funcionan nativamente en otras chains porque otras chains no ejecutan smart contracts EVM ni soportan el mismo formato de firmas criptográficas.

Para profesionales Web3, esto significa perfiles fragmentados irreconciliables. Tus contribuciones open-source a protocolos Ethereum viven en tu dirección 0x... Tus logros en gaming de Solana viven en una dirección base58 completamente separada. Tus participaciones en DAOs de Cosmos están en direcciones cosmos... No existe agregación natural porque no existe interoperabilidad técnica real.

### Estrategias de unificación: parches insuficientes

Los usuarios y desarrolladores han intentado diversas aproximaciones para navegar esta fragmentación, pero todas son soluciones parciales que confirman el problema fundamental en lugar de resolverlo:

**Agregación mediante plataformas de reputación**: Servicios como [DegenScore](https://degenscore.com/) o [DeBank](https://debank.com/) permiten vincular manualmente múltiples wallets para crear perfiles unificados que muestren tus posiciones DeFi en Ethereum, tus NFTs en Solana, y tus stakes en Cosmos simultáneamente. El trade-off es triple: primero, esta vinculación es pública y permanente, destruyendo cualquier separación intencional entre identidades. Segundo, la agregación es solo visual, no funcional: un smart contract en Ethereum no puede leer tu reputación en Solana mediante DeBank. Tercero, dependes de un servicio centralizado para mantener esta agregación; si DeBank cierra, tu perfil unificado desaparece.

**Nombres cross-chain**: [Unstoppable Domains](https://unstoppabledomains.com/) permite que un nombre único como `alice.crypto` resuelva a múltiples direcciones simultáneamente, manteniendo marca personal consistente mientras operas direcciones separadas por chain. Pero esto solo resuelve legibilidad humana, no portabilidad de reputación. Tu nombre es consistente, pero tu historial on-chain sigue fragmentado. ENS en Ethereum no tiene equivalente nativo reconocido en Solana; cada ecosistema tiene sus propios sistemas de nombres (ENS para Ethereum, Bonfida para Solana, Starname para Cosmos) que no se comunican.

**Account Abstraction con direcciones deterministas**: Smart contract wallets como [Safe](https://safe.global/) pueden deployarse en la misma dirección a través de múltiples chains EVM-compatibles mediante CREATE2, unificando identidad técnica dentro del universo EVM. Esto funciona perfectamente entre Ethereum mainnet, Arbitrum, Optimism, Base, Polygon: todas reconocen la misma dirección y pueden compartir reputación mediante registros cross-L2. Pero esta solución refuerza la tribalización en dos niveles: primero, solo funciona dentro de Team Ethereum (Safe en Ethereum y una wallet en Solana no pueden coordinarse de ninguna manera técnicamente viable). Segundo, incluso dentro de Team Ethereum existe fragmentación competitiva: Safe domina el espacio enterprise/DAO con su ecosistema maduro de módulos y guards, mientras MetaMask con su Delegation Toolkit y Smart Accounts Kit apuesta por democratizar AA para usuarios retail mediante integración nativa en la wallet más adoptada globalmente. Estas dos visiones no son totalmente compatibles: Safe tiene su propio sistema de módulos y gestión de permisos, MetaMask implementa ERC-7715 para delegaciones granulares. Un developer debe elegir hacia qué ecosistema de AA optimizar su integración, fragmentando incluso dentro del mismo Team Ethereum. La ironía es que ambos operan sobre el mismo estándar ERC-4337, pero sus SDKs, patrones de uso, y comunidades de developers operan en paralelo con interoperabilidad limitada.

**Protocolos de identidad cross-chain**: [Ceramic Network](https://ceramic.network/) construye infraestructura específicamente para identidad que trascienda blockchains individuales mediante DIDs multicadena y streams de datos descentralizados. La visión es elegante: tu DID ancla en Ceramic puede referenciar credenciales de múltiples chains, creando una identidad portable. La realidad es que Ceramic añade una capa de complejidad significativa, requiere que todas las aplicaciones que consultan tu identidad integren el SDK de Ceramic (fragmentando el ecosistema en "apps que soportan Ceramic" vs "apps que no lo hacen"), y no resuelve el problema fundamental: los smart contracts en Ethereum mainnet no pueden consultar nativamente datos de Ceramic sin oráculos costosos. Ceramic es identidad off-chain que intenta coordinarse con múltiples on-chains, heredando todos los trade-offs del modelo DIDs/VCs (privacidad pero sin composabilidad nativa).

**Bridges de identidad mediante LayerZero u Omnichain**: Protocolos como [LayerZero](https://layerzero.network/) permiten que mensajes cross-chain transporten información de identidad, teóricamente habilitando que una attestation emitida en Ethereum se verifique en Avalanche. Pero esto requiere que ambas chains ejecuten contratos LayerZero, introduce latencia y costos de mensajería, y crea dependencia en la seguridad de un bridge adicional. Además, solo funciona entre chains que LayerZero soporte explícitamente; ecosistemas como Solana con arquitectura fundamentalmente incompatible no pueden participar en este modelo.

### El dilema privacidad vs. unificación vs. tribalización

La fragmentación no es solo técnica sino filosófica, y las tensiones son múltiples:

**Privacidad intencional**: Algunos usuarios prefieren mantener identidades completamente separadas. Su wallet de trading especulativo con apalancamiento 50x no debe conectarse con su reputación profesional en DAOs de gobernanza. Su participación en comunidades pseudónimas controversiales debe estar aislada de su identidad pública verificada con KYC. Esta separación es una feature, no un bug: la fragmentación protege compartimentalización intencional de tu vida digital.

**Portabilidad de reputación**: Otros usuarios necesitan lo contrario: demostrar el alcance completo de su reputación agregada cross-chain. Un desarrollador que contribuyó a protocolos tanto en Ethereum como en Solana quiere que ambas comunidades reconozcan su expertise total. Un inversor con historial impecable de liquidaciones cero en lending protocols de múltiples chains quiere que ese track record se reconozca universalmente para acceder a mejores tasas.

**Tribalización inevitable**: La realidad pragmática es que los ecosistemas no convergen, divergen. Ethereum duplica su apuesta en rollups y Account Abstraction, Solana duplica su apuesta en throughput extremo sacrificando descentralización, Cosmos construye soberanía de app-chains. Cada comunidad desarrolla herramientas, lenguajes, y culturas más especializadas y menos compatibles. La identidad fragmentada refleja esta realidad: tu identidad social en Farcaster (Ethereum-native) no tiene equivalente en Solana porque Solana no prioriza social graphs on-chain del mismo modo.

**Implicaciones arquitectónicas**: El ecosistema actual no facilita ninguna estrategia de forma nativa. Puedes tener privacidad mediante separación total de identidades, pero entonces no puedes agregar reputación. Puedes intentar unificación mediante servicios como DeBank, pero sacrificas privacidad y introduces dependencia centralizada. Puedes construir exclusivamente dentro de un ecosistema (EVM) para maximizar composabilidad, pero entonces excluyes usuarios de otros mundos.

Esta realidad arquitectónica irreconciliable explica por qué las recomendaciones de este repositorio son tan específicas: asumimos Team Ethereum/EVM, priorizamos identidad on-chain componible mediante EAS y ENS, y aceptamos que usuarios nativos de Solana o Cosmos simplemente no son nuestra audiencia target. No porque no sean valiosos, sino porque construir para todos los ecosistemas simultáneamente es técnicamente inviable sin comprometer profundamente la experiencia en cada uno. Web3 no es "one internet, many applications" como Web2. Es "many internets incompatibles, cada uno con su propio conjunto de aplicaciones nativas".

## Autenticación estandarizada: Sign-In with Ethereum (SIWE)

Mientras que los DIDs y VCs manejan las credenciales, la industria necesitaba un estándar robusto para algo más básico: ¿cómo demuestro que soy el dueño de esta dirección ante un servidor Web2 tradicional sin enviar una transacción en la blockchain?

La respuesta es [Sign-In with Ethereum (EIP-4361)](https://eips.ethereum.org/EIPS/eip-4361). Antes de SIWE, cada dApp implementaba su propio mecanismo ad-hoc para pedirte que firmaras un mensaje aleatorio para loguearte, lo cual era peligroso (nunca sabías qué estabas firmando realmente y podías ser víctima de phishing).

SIWE estandarizó el formato del mensaje que firma la wallet de manera legible. Cuando ves un mensaje que dice *"wants you to sign in with your Ethereum account"* seguido de la dirección, el dominio del sitio, un nonce (código único) y la fecha, estás usando SIWE. Esto proporciona seguridad robusta ya que el dominio está vinculado criptográficamente en la firma, previniendo ataques de replay y phishing.

Es el puente fundamental de autenticación. Permite que uses tu identidad Ethereum para entrar en foros, chats de Discord, o sitios corporativos, reemplazando el "Login con Google" por un "Login con tu Wallet" que es seguro, estándar y auditado.

## La posición de este repositorio y decisiones arquitectónicas

Existen tres grandes caminos en identidad Web3, cada uno con sus compromisos y audiencias.

La vía formal regulatoria, prioriza el cumplimiento legal y el reconocimiento gubernamental (EUDI Wallet, DIDs/VCs bajo eIDAS 2.0). Es obligatoria para aplicaciones que manejan identidad legal estricta, activos regulados o interoperabilidad bancaria. Confía en proveedores de servicios de confianza cualificados.

La vía de adopción masiva retail, prioriza eliminar la fricción mediante custodia delegada o compartida (WaaS con embedded wallets como Privy, Dynamic o Magic). Ofrece una experiencia similar a la Web2, sacrificando principios de soberanía a cambio de tasas de conversión más altas en aplicaciones de consumo.

La vía de identidad on-chain componible, prioriza la composabilidad nativa, la transparencia y la resistencia a la censura (SBTs, ENS, EAS, [SIWE](https://docs.login.xyz/)). Asume la auto-custodia y construye la identidad mediante la interacción verificable y pública entre protocolos, sin depender de la existencia de un proveedor centralizado de wallets.

Este repositorio que enfrente este trilema (web3 plagados de trilemas como no...) se enfoca deliberadamente en el tercer camino. Asumimos que construyes tokens de utilidad y herramientas de coordinación, no valores regulados. Asumimos una audiencia inicial B2B o usuarios técnicamente capaces que valoran el control total. Creemos que la combinación de MetaMask junto con estándares abiertos representa el equilibrio óptimo para este segmento.

### Implicaciones técnicas y regulatorias

Esta decisión no es solo filosófica, tiene impactos operativos y legales críticos.

Evitamos la incertidumbre de la custodia porque las soluciones WaaS introducen dependencias críticas. Si el proveedor cierra o es censurado, la recuperación de la cuenta puede comprometerse. Además, desde una perspectiva fiscal, una wallet cuyas claves custodia o gestiona un proveedor extranjero podría interpretarse como una cuenta en el extranjero, disparando obligaciones de reporte y complicaciones legales que no existen con la auto-custodia pura en software local.

Reconocemos que el compliance es inevitable para rampas fiat, pero apostamos por el cumplimiento bajo demanda. La arquitectura propuesta sugiere integración modular donde el usuario mantiene su wallet personal y solo se conecta con proveedores de identidad para generar una prueba específica cuando la regulación lo exija, sin convertir toda la cuenta en una identidad permisionada.

Favorecemos modelos públicos para la reputación y el grafo social. Aceptamos que en Web3 la historia on-chain es pública. Intentar ocultar toda la actividad bajo capas de privacidad complejas a menudo destruye la composabilidad, limitando la capacidad de que otros contratos interactúen contigo automáticamente.

### Stack tecnológico recomendado

Para implementar esta visión de identidad descentralizada y componible recomendamos las siguientes piezas.

**Wallet y Conexión**:

Utilizamos MetaMask como referencia de auto-custodia. Para la integración, recomendamos AppKit o RainbowKit para soportar el protocolo WalletConnect. Esto permite a los usuarios conectar cualquier wallet móvil manteniendo sus claves en su dispositivo, sin depender de un login social custodiado.

**Autenticación**:

Implementamos Sign-In with Ethereum ([SIWE](https://docs.login.xyz/) - EIP-4361). Es fundamental reemplazar el login tradicional para autenticar que el usuario controla una dirección mediante una firma de mensaje estandarizada, creando una sesión segura con el backend sin requerir contraseñas ni depender de terceros.

**Identidad Legible**:

Integramos ENS (Ethereum Name Service). La interfaz debe resolver automáticamente las direcciones. Mostrar un nombre legible en lugar de una dirección hexadecimal reduce errores y humaniza la experiencia.

**Reputación y Credenciales**:

Usamos **EAS (Ethereum Attestation Service)** porque se ha convertido en el estándar de interoperabilidad en ecosistemas como Optimism y Base. Mientras que los SBTs suelen requerir contratos personalizados difíciles de integrar por terceros, EAS permite que cualquier dApp lea y verifique la reputación de un usuario (ej. "usuario verificado", "participante en gobernanza") utilizando un esquema universal.

```solidity
// Ejemplo simplificado de verificación en Solidity
function verifyUserAttestation(bytes32 attestationUID) public view {
    // Verificamos la atestación directamente en el registro global de EAS
    Attestation memory attestation = eas.getAttestation(attestationUID);

    require(attestation.recipient == msg.sender, "No pertenece al usuario");
    require(attestation.schema == REQUIRED_SCHEMA_UID, "Schema incorrecto");
    require(attestation.revocationTime == 0, "Credencial revocada");
}
```

**Grafo Social**:

Sugerimos integrar **Farcaster** o **Lens Protocol** para enriquecer el perfil sin crear silos. En lugar de gestionar tu propia base de datos de avatares y biografías, consulta estos protocolos abiertos. Esto permite que el usuario traiga su reputación social y sus conexiones desde el primer día, evitando el problema del "arranque en frío" y respetando la portabilidad de sus datos.

**Resistencia Sybil**:

Integramos Gitcoin Passport para agregar múltiples señales de identidad y calcular un puntaje de humanidad sin exponer datos biométricos directamente a la dApp.

```javascript
// Ejemplo conceptual en frontend
const score = await passportScorer.getScore(address);
if (score > 20) {
   allowVoting();
}
```

El Passport recopila "stamps" o sellos de diferentes fuentes: verificación de cuenta de Twitter, vinculación con GitHub, posesión de ENS, participación en DAOs, [staking](https://ethereum.org/en/staking/) de ETH, verificación mediante [BrightID](https://www.brightid.org/), y muchos más. Estos stamps son credenciales verificables que pueden almacenarse tanto on-chain como off-chain. El diseño actual utiliza principalmente attestations on-chain mediante Ethereum Attestation Service (EAS) en redes L2 como Optimism y Base, lo que permite verificación pública mientras mantiene costos bajos. Cada stamp suma puntos a tu "humanity score", un indicador de cuán probable es que seas un humano único real versus un bot o identidad duplicada.

Los protocolos pueden establecer umbrales de Passport score para participar en votaciones, recibir airdrops o acceder a ciertos beneficios. Lo interesante es que los verificadores ven tu score agregado pero no necesariamente qué stamps específicos posees, preservando cierto grado de privacidad mientras demuestras humanidad.

**Account Abstraction**:

Aquí enfrentamos una **tensión estratégica real dentro de Team Ethereum** que no tiene respuesta única correcta. Existen dos caminos principales, ambos válidos pero con trade-offs significativos:

**Opción A - Safe (Gnosis Safe)**: El estándar histórico y batalla-probado de smart contract wallets en Ethereum. Domina tesorerías DAO, multisig enterprise, y gestión de activos institucionales con años de uso en producción sin incidentes mayores. Su ecosistema de módulos, guards y plugins es el más maduro del espacio. Soporta ERC-4337 nativamente y permite arquitecturas complejas de permisos, recovery, y automatización. El trade-off es que requiere que usuarios operen explícitamente con una Safe wallet, añadiendo fricción de onboarding comparado con la MetaMask que probablemente ya tienen instalada. Integrar Safe significa comprometerse con su SDK, patrones de desarrollo, y ecosistema específico.

**Opción B - MetaMask Delegation Toolkit & Smart Accounts Kit**: La apuesta de ConsenSys para democratizar Account Abstraction mediante integración nativa en la wallet con >30M usuarios. Implementa ERC-7715 para delegaciones granulares, gas abstraction, y cuentas multichain coordinadas sin requerir que usuarios instalen software adicional. El trade-off es que es tecnología más reciente (2024-2025) comparada con Safe (operando desde 2018), con menos battle-testing en escenarios edge case complejos. Además, el modelo de delegaciones de MetaMask es filosóficamente diferente: prioriza UX retail sobre arquitecturas enterprise complejas.

**Nuestra recomendación pragmática para este repositorio**:

Para **tesorerías, multisig y gestión de activos críticos** (>$100K en valor, múltiples firmantes, requerimientos de compliance enterprise): **Safe es innegociable**. Su madurez, auditorías, y adopción institucional lo convierten en el único estándar aceptable para estos casos. No existe alternativa creíble en 2026.

Para **UX de usuario final, onboarding masivo, y aplicaciones consumer** (gaming, social, NFTs, gobernanza comunitaria): **MetaMask Delegation Toolkit es más coherente** con el resto del stack que recomendamos. Si ya asumimos MetaMask como wallet base, implementamos SIWE para autenticación, y priorizamos reducción de fricción, introducir Safe como requerimiento adicional contradice la estrategia. Los usuarios ya tienen MetaMask; aprovechar su AA nativa elimina pasos de configuración y reduce abandono.

**La tensión no resuelta**: Esta fragmentación dentro de Team Ethereum es sintomática del problema más amplio de falta de convergencia en Web3. Ambas soluciones operan sobre ERC-4337, pero sus SDKs, patrones de integración, y filosofías de diseño no convergen naturalmente. Un protocolo que optimiza para Safe no necesariamente funciona óptimamente con MetaMask AA, y viceversa. Developers terminan eligiendo un camino y excluyendo parcialmente al otro, replicando el problema de tribalización incluso dentro del mismo ecosistema.

Proyectos ambiciosos pueden intentar soportar ambos mediante abstracción de la capa de wallet, pero esto añade complejidad significativa. Nuestra posición es pragmática: si tu caso de uso es retail/consumer, MetaMask AA es el camino de menor fricción. Si es enterprise/tesorería, Safe es obligatorio. Si necesitas ambos segmentos, prepárate para implementar dos integraciones paralelas con sus respectivos costos de mantenimiento.

### Lo que conscientemente rechazamos

No usamos WaaS como primera opción. Si tu modelo de negocio depende de convertir usuarios masivos que aún no saben gestionar claves, este stack no es el adecuado. Aunque reconocemos la fricción inicial, defendemos que la verdadera soberanía requiere que el usuario custodie sus claves. Esta filosofía se alinea con la dirección de la EUDI Wallet (custodia local en dispositivo) y se ve respaldada por las mejoras masivas en UX que MetaMask y el ecosistema de Account Abstraction están implementando para democratizar la auto-custodia sin comprometer la seguridad.

No priorizamos eIDAS como requisito de diseño. No estamos construyendo aplicaciones de administración pública. Si se necesitan credenciales gubernamentales cualificadas, este no es el repositorio de referencia.

Rechazamos crear sistemas de identidad propietarios. Si no es un estándar o un protocolo público neutral, no lo integramos.

### Para quién es esta aproximación

Esta arquitectura es para desarrolladores que construyen la próxima generación de herramientas de coordinación y utilidad descentralizada. Es para quienes creen que la identidad no debe ser un servicio alquilado a una corporación, sino un activo en manos del usuario, aunque esto requiera una curva de aprendizaje inicial.

---
