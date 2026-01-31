
# Identidad Web3

Una de las promesas fundamentales de web3 es devolver el control de la identidad a los individuos, no solo como cuestión de soberanía personal, sino porque concentrar este control en manos de terceros genera vulnerabilidades de seguridad sistémicas.

> El autor de este artículo, tras superar una crisis nerviosa, ha logrado aclarar todo esto; por favor, valórenlo adecuadamente... Bromas aparte, la identidad sufre una fragmentación motivada por intereses, lo que la hace más compleja de explicar de lo que parece...

El objetivo es que cada persona pueda poseer y gestionar su propia identidad de forma autosoberana. En la práctica, esta visión no difiere radicalmente de lo que ya conocemos en el mundo físico: posees un DNI en España o un pasaporte que te pertenece, del cual eres custodio, y donde acumulas sellos y validaciones que acreditan tus accesos y atributos. La solución descentralizada replica este modelo mediante un pasaporte digital donde tu wallet personal actúa como contenedor de credenciales verificables.

Antes de continuar, es fundamental revisar ciertos conceptos clave:

Un **identificador** es un código único que te representa en el sistema. Tu wallet de [MetaMask](https://metamask.io/) (una de las billeteras digitales más populares para Ethereum) genera una dirección hexadecimal (0x1234...abcd) que funciona como tu identificador en la blockchain, un código que permite a los sistemas localizarte y comunicarse contigo. Este es un ejemplo simple, existen otros identificadores más formales como el DID, que veremos más adelante.

Una **atestación** es una declaración firmada digitalmente por un emisor que da fe o certifica ciertos atributos, afirmaciones o hechos sobre un sujeto. En términos simples, es cuando alguien con autoridad reconocida (una universidad, un empleador, una organización) confirma algo sobre ti de forma verificable. Por ejemplo, una universidad puede atestiguar que completaste un grado académico, o una empresa puede atestiguar que trabajaste para ella durante cierto período.

Una **credencial** es cualquier evidencia o documento firmado que puedes presentar por ti mismo, para demostrar algo o probar que tienes ciertos derechos o atributos. Habrás notado que se parece mucho a una atestación, y es normal: para W3C una atestación es el acto que genera una credencial, es la declaración o certificación en sí, algo más genérico que una credencial. Mientras que de una credencial se habla en contexto de identificación y es capaz de identificar a un sujeto, la atestación existe en un contexto más de validación o acreditación de hechos en el mundo de la seguridad.

Una **identidad** es la representación reconocible y significativa de quién eres en un contexto social. No puedes decirle a alguien "envíame dinero a cero-equis-uno-dos-tres-cuatro...a-be-ce-de" sin que sea confuso y propenso a errores. Necesitas algo que los humanos puedan entender y recordar. Aquí entra en juego tu **marca personal**: un nombre legible y una imagen (foto de perfil) que te distingan. Una identidad se construye y verifica gracias a una o varias credenciales, y preferimos este término en lugar de "atestación" en este contexto porque la identidad es algo que tú posees y gestionas, mientras que la atestación es algo que otros dicen sobre ti.

Con estos conceptos claros, emergen preguntas fundamentales que definen el diseño de sistemas de identidad descentralizada. ¿Es un identificador por sí mismo una identidad? Más específicamente, ¿tu dirección de Ethereum constituye tu identidad, o solo lo es cuando se asocia a un nombre o foto de perfil reconocible que únicamente tú puedes acreditar? ¿O una identidad requiere además que un emisor de confianza lo certifique con atributos verificables? o ¿por qué tiene que ser precisamente una identidad y no es un grafo social?

Igualmente, ¿tiene sentido tu identidad y tus atributos acreditados si no pueden portarse en diferentes redes? Porque, ¿cómo podrás llevar tu reputación si no puedes portar tus acreditaciones a otras redes?

Pero además... ¿acaso importa tanto tu identidad? ¿No deberían valer solo tus atestaciones que te dan reputación on-chain asociada a una dirección? ¿O mucho mejor, algo más simple como un NFT que has ganado y no puedes transferir para conseguir la composabilidad total en smart contracts on-chain? Pero ¿y si no queremos exponer nuestra privacidad más de la necesaria?

Estas preguntas no tienen respuestas únicas y absolutas. Las diferentes implementaciones de identidad descentralizada representan trade-offs entre objetivos y filosofías diferentes aplicadas en Web3 donde convive composabilidad y privacidad. La fragmentación al respecto genera una tensión que complica mucho la experiencia de usuario real, porque mientras discuten qué es lo mejor, los que queremos acceder a una aplicación nos resulta más cómodo hacer login en Google o, si es Web3, usar MetaMask por cuestiones históricas y sobre todo porque es la wallet de facto; mientras nos apañamos con pasar complejos procesos KYC para ciertas DApps. Por lo tanto, se puede decir, que la identidad descentralizada en web3 todavía no está resuelta, por lo tanto, este artículo mas que certezas tendrá que tomarse como una serie de conclusiones y cuestiones todavía abiertas.

## Conociendo la situación actual del resto de actores

La situación actual es complicada, hay varios actores y todos tienen sus intereses claros en lo que afecta al control y centralización.

**Las bigtech en web2**:

Por una parte las big tech, dominadoras de la [Web2](https://ethereum.org/en/developers/docs/web2-vs-web3/) en plataformas centralizadas como redes sociales y servicios cloud, tu identidad digital no te pertenece realmente. Cuando creas una cuenta en Facebook, Google o cualquier plataforma digital, la empresa almacena tu información, controla el acceso a ella y puede modificarla, censurarla o eliminarla sin tu consentimiento previo. Esta fragmentación de identidad entre múltiples plataformas que no se comunican entre sí es lo que técnicamente se conoce como [siloed identity](https://www.w3.org/2012/webcrypto/webcrypto-next-workshop/papers/webcrypto2014_submission_8.pdf), donde cada servicio mantiene tu información aislada en su propio silo.

Este modelo centralizado genera varios problemas fundamentales. Primero, existe un riesgo de seguridad significativo porque todas tus credenciales están almacenadas en servidores centralizados que se convierten en objetivos atractivos para hackers. Segundo, no tienes portabilidad: tu reputación en Amazon no sirve en eBay, tu historial profesional en LinkedIn no se transfiere a otras plataformas. Tercero, dependes completamente de la plataforma: si deciden cerrar tu cuenta, pierdes años de datos, conexiones y reputación acumulada. Esta dependencia crea lo que se denomina [vendor lock-in](https://en.wikipedia.org/wiki/Vendor_lock-in), donde quedas atrapado en el ecosistema de un proveedor específico sin capacidad real de migrar tu identidad y datos a alternativas.

Además, el modelo centralizado crea problemas de privacidad. Para usar la mayoría de servicios digitales, debes revelar más información de la necesaria. Si quieres entrar a un sitio para mayores de edad, tienes que proporcionar tu fecha de nacimiento completa cuando en realidad solo necesitan saber que eres mayor de 18 años.

**Gobiernos y reguladores**:

Por otra parte los gobiernos y reguladores están desarrollando sus propios marcos normativos para la identidad digital. En concreto en Europa como el mayor referente, la regulación [eIDAS 2.0](https://digital-strategy.ec.europa.eu/en/policies/eidas-regulation) y su implementación de European Digital Identity Wallet, ofrece un equilibrio entre el control institucional y la autonomía del usuario. Además, viendo el problema de Web2, a partir de 2026, plataformas de gran tamaño como Meta (Facebook, Instagram), Amazon, Apple, Booking.com, TikTok y Zalando, etc estarán **obligadas por ley a aceptar** la European Digital Identity Wallet (EUDI Wallet) como método válido de autenticación e identificación. Esto significa que estos servicios no pueden rechazar este método de identificación cuando un usuario elija utilizarlo. **Para los ciudadanos**: El uso de la cartera digital europea es **voluntario**. Los ciudadanos pueden elegir si desean obtener y utilizar esta identidad digital, y los Estados miembros deben proporcionar métodos alternativos de identificación tradicionales para aquellos que no deseen adoptarla. No existe obligación legal de que los ciudadanos usen este sistema para su vida cotidiana. Sin embargo, la regulación cubre sectores amplios donde los servicios deben aceptar eIDAS 2.0: banca, transporte, energía, seguridad social, sanidad, suministro de agua, infraestructura postal, infraestructura digital, educación y telecomunicaciones. Aunque usar la cartera digital sea voluntario para ciudadanos, la amplitud de sectores obligados a aceptarla significa que, en la práctica, se convierte en un estándar de facto para identidad digital en Europa.

**Web3 con KYC/AML**:

Adicionalmente nos encontramos con el compliance de plataformas cripto o web3 con KYC/AML  debemos reconocer una realidad incómoda: KYC (Know Your Customer) y AML (Anti-Money Laundering) no son identidad descentralizada, sino identidad centralizada tradicional operando dentro de Web3 por obligación legal. Esta distinción es fundamental para entender correctamente el ecosistema.

Cada exchange donde compras ETH o BTC requiere procesos KYC rigurosos: pasaporte, prueba de domicilio, selfie sosteniendo tu documento, declaraciones de fuente de fondos. Este proceso es completamente centralizado y contradice frontalmente los principios de identidad autosoberana. Entregas tus datos personales más sensibles a una empresa privada que los almacena en sus servidores, exactamente el modelo centralizado que queremos superar.

¿Por qué existe esta contradicción en un ecosistema que promete descentralización? Regulación. Los gobiernos han implementado marcos regulatorios estrictos que obligan a cualquier entidad que facilite conversión entre fiat y criptomonedas a implementar controles KYC/AML. Regulaciones como la [5th Anti-Money Laundering Directive (5AMLD)](https://eur-lex.europa.eu/eli/dir/2018/843/oj) en Europa o el [Bank Secrecy Act](https://www.fincen.gov/resources/statutes-and-regulations/bank-secrecy-act) en Estados Unidos existen para prevenir lavado de dinero, financiamiento del terrorismo y evasión fiscal.

El resultado es que la mayoría de usuarios comprometen su privacidad desde el momento cero. Tu primer contacto con crypto probablemente fue entregar tu identidad legal completa a Coinbase o Binance. Incluso protocolos DeFi descentralizados como Uniswap o Aave enfrentan presión regulatoria para implementar restricciones geográficas y verificación de identidad cuando alcanzan volúmenes significativos.

Protocolos como [Aave Arc](https://aave.com/) experimentaron con "DeFi permisionado" donde solo usuarios KYC-verificados podían participar. [MakerDAO](https://makerdao.com/) discute implementar KYC para activos del mundo real (RWA). DAOs grandes enfrentan dilemas similares: ¿cómo cumplir obligaciones fiscales sin comprometer pseudonimidad de miembros?

La identidad descentralizada teórica choca con las realidades del sistema financiero tradicional. Mientras los estados-nación controlen las rampas de entrada y salida del ecosistema crypto, KYC centralizado será inevitable para la mayoría de participantes. Los puristas argumentan que esto es temporal, que eventualmente viviremos completamente on-chain. Los pragmáticos reconocen que la regulación no desaparecerá, y que sistemas híbridos son el futuro más probable.

**Redes sociales descentralizadas y el grafo social**:

Proyectos como [Lens Protocol](https://www.lens.xyz/), [Farcaster](https://www.farcaster.xyz/) y [CyberConnect](https://cyberconnect.me/) representan una visión radicalmente diferente: para ellos, la identidad no son credenciales formales emitidas por autoridades, sino tu grafo social y las conexiones que construyes. En este modelo, identidad, credenciales y reputación se fusionan en un único constructo social on-chain.

**Lens Protocol** originalmente operaba como smart contracts en [Polygon](https://polygon.technology/), pero a partir de 2026 lanzó [Lens Chain](https://www.lens.xyz/), su propia blockchain soberana específicamente diseñada para redes sociales descentralizadas. Este movimiento hacia infraestructura propia demuestra la madurez del protocolo y su necesidad de optimizar rendimiento para casos de uso sociales de alto volumen. Tu perfil es un NFT (token no fungible) que posees directamente. Este NFT no solo te identifica, sino que contiene tu grafo social completo: cada seguidor es otro NFT vinculado a tu perfil, cada publicación es un NFT asociado, cada interacción queda registrada on-chain. Tu reputación no se certifica mediante diplomas o attestations externas, emerge orgánicamente de tus conexiones y contenido. Si tienes 10,000 seguidores verificables on-chain y produces contenido que genera alta interacción, esa es tu reputación, sin necesidad de que una autoridad central la certifique.

La portabilidad funciona mediante composabilidad del protocolo: cualquier aplicación que integre Lens puede leer instantáneamente tu perfil, seguidores, y actividad. Si una interfaz te censura o cierra, simplemente accedes a otra aplicación que consuma el mismo protocolo social subyacente, conservando intacta tu audiencia porque los datos viven en blockchain, no en servidores de la aplicación.

**Farcaster** adopta una arquitectura híbrida única: tu identidad base (un Farcaster ID numérico) se registra on-chain en [Optimism](https://www.optimism.io/) (una L2 de Ethereum), garantizando propiedad verificable inmutable. Sin embargo, Farcaster opera su propia red descentralizada de servidores llamados "Hubs" para almacenar el contenido social masivo off-chain. Sin embargo, el contenido social masivo vive en una red descentralizada de "Hubs" off-chain que almacenan tus mensajes, likes y interacciones. Cada mensaje está firmado criptográficamente con tu clave privada vinculada a tu FID on-chain, probando autoría sin necesidad de almacenamiento blockchain costoso. La portabilidad de reputación se logra porque cualquier aplicación puede conectarse a los Hubs, leer tu historial completo de actividad firmada, y construir métricas de reputación. Tu influencia en una app Farcaster (medida por seguidores, engagement, longevidad de cuenta) es instantáneamente visible en cualquier otra app del ecosistema.

**CyberConnect** funciona como capa de grafo social multi-chain, desplegando contratos inteligentes en múltiples blockchains existentes simultáneamente: [Ethereum](https://ethereum.org/), [BNB Chain](https://www.bnbchain.org/), [Polygon](https://polygon.technology/), [Optimism](https://www.optimism.io/), [Arbitrum](https://arbitrum.io/), y [Solana](https://solana.com/). No tiene blockchain propia, sino que permite que tu identidad y conexiones en una chain sean reconocidas en las otras mediante su protocolo de indexación cross-chain. Aquí la separación conceptual es más clara: tu identidad es tu dirección blockchain (o múltiples direcciones vinculadas), tus credenciales son las conexiones verificables con otras direcciones (follows, endorsements), y tu reputación emerge de la estructura de tu red. CyberConnect no impone un NFT de perfil único como Lens, sino que agrega conexiones existentes entre direcciones en múltiples ecosistemas. La portabilidad cross-chain significa que si construiste una red de 5,000 seguidores en Ethereum, proyectos en Solana pueden consultar esas mismas conexiones mediante el protocolo CyberConnect sin necesidad de que tus seguidores migren manualmente a otra blockchain.

La visión compartida de estos protocolos es que la portabilidad relevante no es llevar diplomas universitarios entre redes, sino migrar tu capital social completo: tu audiencia, tu historial de contribuciones, tu web de confianza. Para ellos, las credenciales formales (DIDs, VCs con ZK-proofs) añaden complejidad técnica innecesaria cuando la identidad puede simplemente ser tu dirección blockchain más el grafo social públicamente verificable que has construido. No necesitas probar que Stanford te dio un diploma si has publicado investigación técnica que recibió endorsements de developers reconocidos en la comunidad. Tu reputación es tu output verificable, no certificados de autoridades externas.

**Ethereum Foundation y la visión DeSoc**:

La propuesta de Vitalik Buterin y la Ethereum Foundation, cristalizada en el paper ["Decentralized Society: Finding Web3's Soul"](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763), apuesta por los Soulbound Tokens (SBTs) como primitiva fundamental de identidad. Esta visión está diseñada específicamente para el ecosistema [Ethereum](https://ethereum.org/): tanto la mainnet L1 como todas las L2s compatibles con EVM ([Optimism](https://www.optimism.io/), [Arbitrum](https://arbitrum.io/), [Base](https://base.org/), [Polygon](https://polygon.technology/), etc.).

Su visión es que todo debe estar on-chain para máxima composabilidad: smart contracts leyendo directamente tus credenciales públicas no transferibles, sin necesidad de infraestructura off-chain compleja.

La privacidad, desde su perspectiva, se resuelve en capas superiores mediante Zero-Knowledge Proofs, stealth addresses o L2s con privacidad integrada, no es responsabilidad del sistema de identidad base.

Esta filosofía prioriza la simplicidad técnica y la transparencia: si no estás dispuesto a aceptar que blockchain es fundamentalmente pública y transparente, quizás Web3 no es el ecosistema adecuado. La portabilidad cross-chain no es una preocupación central porque asumen que el ecosistema Ethereum (L1 + L2s compatibles) dominará.

**Infraestructura neutral: EAS y protocolos de attestations**:

Proyectos como [Ethereum Attestation Service (EAS)](https://attest.sh/) y [Sign Protocol](https://sign.global/) adoptan una postura neutral respecto a estas disputas filosóficas. [EAS](https://attest.sh/) despliega contratos inteligentes idénticos en múltiples redes: [Ethereum](https://ethereum.org/) mainnet, [Optimism](https://www.optimism.io/), [Base](https://base.org/), [Arbitrum](https://arbitrum.io/), [Polygon](https://polygon.technology/), [Linea](https://linea.build/), [Scroll](https://scroll.io/) y otras L2s, permitiendo que las attestations vivan donde sea más conveniente según costos y necesidades.

Proveen infraestructura de attestations on-chain que cualquier actor puede usar según sus necesidades: puedes hacer attestations públicas componibles si priorizas transparencia, o attestations off-chain si necesitas privacidad.

No toman partido sobre si la identidad debe ser credenciales formales vs. grafo social, simplemente ofrecen primitivas técnicas que ambos modelos pueden consumir. Esta neutralidad arquitectónica es poderosa pero no resuelve las tensiones fundamentales, solo las hace técnicamente viables en paralelo.

**Proof of Personhood y resistencia Sybil**:

Actores como [Worldcoin](https://worldcoin.org/), [Gitcoin Passport](https://passport.gitcoin.co/), [Proof of Humanity](https://www.proofofhumanity.id/) y [BrightID](https://www.brightid.org/) se enfocan exclusivamente en resolver un problema específico: demostrar que eres un humano único real, resistiendo ataques Sybil (creación de múltiples identidades falsas). Sus infraestructuras varían significativamente:

**Worldcoin** opera [World Chain](https://world.org/world-chain), su propia L2 construida sobre [OP Stack](https://stack.optimism.io/), aunque también verifica identidades que pueden usarse en [Ethereum](https://ethereum.org/) mainnet y otras chains mediante bridges.

**Gitcoin Passport** almacena attestations usando [EAS](https://attest.sh/) en múltiples L2s: principalmente [Optimism](https://www.optimism.io/) y [Base](https://base.org/), permitiendo que los scores de humanidad sean verificables on-chain donde sea necesario.

**Proof of Humanity** es un smart contract desplegado únicamente en [Ethereum](https://ethereum.org/) mainnet, creando un registro público y permanente en la L1.

**BrightID** opera su propia red peer-to-peer descentralizada completamente independiente de blockchains, aunque puede anclar verificaciones en [Ethereum](https://ethereum.org/) o [xDai](https://www.xdaichain.com/) cuando es necesario.

Para ellos, la identidad rica es secundaria; lo único que importa es la unicidad. Cada uno sacrifica aspectos diferentes según su arquitectura: Worldcoin prioriza privacidad mediante ZK-proofs pero centraliza hardware biométrico, Gitcoin Passport agrega reputación on-chain sacrificando privacidad, Proof of Humanity crea registros públicos permanentes en L1, BrightID preserva privacidad del grafo social pero requiere confianza en su red descentralizada. Ninguno pretende ser una solución completa de identidad, solo resuelven el problema anti-Sybil que habilita votación cuadrática, distribuciones justas de tokens, y gobernanza democrática.

## Las diferentes visiones que fragmentan el ecosistema

La fragmentación en identidad Web3 no es accidental ni temporal, refleja tensiones filosóficas irreconciliables entre objetivos que fundamentalmente compiten entre sí. Entender estas tensiones es crucial porque explican por qué no existe "una solución de identidad Web3" unificada, sino un ecosistema de herramientas especializadas que hacen trade-offs incompatibles.

### Privacidad vs. composabilidad: on-chain vs off-chain

La primera tensión fundamental es dónde viven tus datos de identidad y quién puede acceder a ellos.

El modelo **off-chain con credenciales privadas** (DIDs, VCs, Verifiable Presentations) maximiza privacidad mediante control del usuario. Tus credenciales viven en tu wallet bajo tu custodia exclusiva, solo tú decides cuándo y a quién mostrarlas, y puedes usar Zero-Knowledge Proofs para revelar el mínimo necesario. Un smart contract no puede simplemente "leer" si tienes un diploma universitario, necesitas activamente presentar una prueba. Esto protege tu privacidad pero destruye la composabilidad automática: los protocolos DeFi no pueden consultar instantáneamente tu historial crediticio, las DAOs no pueden verificar automáticamente membresías, los NFT marketplaces no pueden filtrar automáticamente usuarios por jurisdicción.

El modelo **on-chain público** (SBTs, attestations on-chain, POAPs) maximiza composabilidad sacrificando privacidad. Tus credenciales son tokens en tu dirección que cualquier smart contract puede leer sin permiso. Un protocolo de lending puede verificar instantáneamente que posees un SBT de "buen pagador" emitido por otro protocolo y ajustar tus tasas automáticamente. Una DAO puede requerir posesión de ciertos SBTs para habilitar votación. Este modelo es técnicamente simple y extremadamente poderoso para construir sistemas componibles, pero significa que toda tu identidad es un libro abierto: cualquiera puede ver todos tus SBTs, correlacionar tu actividad, y construir perfiles detallados de tu vida digital.

No existe punto medio técnico que preserve ambas propiedades completamente. Algunas aproximaciones híbridas intentan balancear: attestations off-chain con hash on-chain, ZK-proofs que permiten verificación selectiva manteniendo cierta componibilidad, o sistemas donde publicas attestations públicas básicas pero guardas credenciales sensibles off-chain. Sin embargo, cada compromiso sacrifica algún aspecto de privacidad o composabilidad.

### Autoridades formales vs. reputación emergente: credenciales vs grafo social

La segunda tensión es epistemológica: ¿qué constituye identidad verificable?

El modelo de **autoridades y credenciales formales** (gobiernos con eIDAS, universidades emitiendo diplomas, empresas certificando experiencia) asume que la identidad se construye mediante validación de instituciones reconocidas. Tu diploma vale porque Stanford University lo firmó, no porque la comunidad cree que eres inteligente. Este modelo replica estructuras del mundo físico en blockchain: necesitas emisores con autoridad real, mecanismos de revocación cuando las credenciales caducan, y probablemente compliance regulatorio. Funciona bien para integración con sistemas legales y financieros tradicionales, pero centraliza el poder de validación en manos de instituciones que pueden excluir, discriminar o censurar.

El modelo de **grafo social y reputación emergente** (Lens Protocol, Farcaster, sistemas de reputación on-chain) argumenta que la identidad emerge de tus relaciones y acciones verificables. Tu reputación se construye mediante quién te sigue, qué DAOs te aceptan como miembro, qué contribuciones open-source has hecho, qué eventos has atendido (POAPs), cuánto has participado en gobernanza. No necesitas que Stanford certifique tu inteligencia si has contribuido código a protocolos importantes que la comunidad valora. Este modelo es inherentemente descentralizado y resistente a censura porque ninguna autoridad única puede revocar tu reputación social, pero es vulnerable a manipulación (comprar seguidores, crear narrativas falsas) y no satisface requisitos legales en la mayoría de jurisdicciones.

Ambos modelos coexisten en Web3 porque sirven necesidades diferentes. Si necesitas abrir una cuenta bancaria o probar tu edad legalmente, requieres credenciales formales de autoridades reconocidas. Si necesitas demostrar reputación en comunidades descentralizadas para recibir funding de una DAO, tu grafo social y contribuciones on-chain son más relevantes que cualquier diploma. La tensión surge cuando sistemas intentan ser puristas: protocolos que solo aceptan reputación emergente excluyen a newcomers sin historial on-chain, mientras que sistemas que solo aceptan credenciales formales replican barreras de acceso del mundo tradicional.

### Consecuencias prácticas de la fragmentación

Esta fragmentación tiene impactos reales en la experiencia de usuario. Un usuario promedio de Web3 navega múltiples sistemas de identidad incompatibles simultáneamente:

Para comprar crypto en un exchange centralizado, pasas KYC completo entregando tu identidad legal a una empresa privada (modelo centralizado tradicional). Para interactuar con protocolos DeFi, usas tu dirección Ethereum como identificador pseudónimo donde tu reputación es tu historial de transacciones visible públicamente (modelo on-chain transparente). Si participas en gobernanza de DAOs, podrías necesitar POAPs de eventos para probar membresía o Gitcoin Passport para resistencia Sybil (modelo de reputación emergente). Si una dApp requiere verificación de jurisdicción por compliance, podrías presentar una credencial off-chain mediante Privado ID que demuestre "no estoy en país sancionado" sin revelar tu ubicación exacta (modelo off-chain con privacidad).

Ninguno de estos sistemas se comunica con los otros de forma nativa. Tu reputación construida en Ethereum no es visible ni relevante en Solana. Tus credenciales verificables off-chain no ayudan a smart contracts que necesitan leer datos on-chain. Tu grafo social en Lens Protocol no certifica tu edad para compliance legal.

Los desarrolladores de aplicaciones enfrentan decisiones arquitectónicas fundamentales que determinan qué usuarios pueden participar. Si construyes un sistema que requiere credenciales formales off-chain, excluyes a usuarios que solo tienen reputación on-chain. Si construyes asumiendo todo on-chain público, excluyes a usuarios que requieren privacidad. Si priorizas composabilidad nativa con smart contracts, sacrificas privacidad. Si priorizas privacidad mediante VCs off-chain, sacrificas la experiencia de usuario fluida de interacciones automáticas on-chain.

La realidad es que Web3 no ha convergido en un modelo unificado de identidad porque los diferentes casos de uso tienen requisitos genuinamente incompatibles. La solución pragmática no es forzar convergencia prematura, sino reconocer esta diversidad y construir puentes entre sistemas donde sea posible mediante estándares compartidos (como OpenID4VC permitiendo que wallets Web3 y EUDI coexistan) mientras aceptamos que ciertos trade-offs son fundamentales e irreconciliables.

italik sugiere que la SSI nos da el control individual, pero la DecSoc nos da la capacidad de colaborar
Él ha dicho que para que Web3 no sea solo un casino financiero, necesita una "capa social"

La visión de Vitalik: Él menciona proyectos como Lens porque están construyendo el Grafo Social Descentralizado. Aunque Lens use NFTs (transferibles), Vitalik argumenta que en una sociedad ideal (DecSoc), los elementos que definen quién eres (tus títulos, tu reputación) deberían ser SBTs (no transferibles)

ctualidad: Lens ha ido evolucionando y muchos desarrolladores dentro de su ecosistema están integrando herramientas como Sismo para emitir "badges" o insignias que sí funcionan como SBTs sobre tu perfil de Lens.

Quadratic Funding (QF), popularizado por Gitcoin (y co-creado por Vitalik), no es un token, sino un algoritmo matemático. Sin embargo, necesita desesperadamente de los SBTs o la SSI para funcionar bien

Gitcoin Passport: Una colección de SBTs que demuestran que no eres un bot.

Desde la visión de Vitalik (expuesta en su paper Decentralized Society y en sus ensayos sobre Plurality), la tensión entre la soberanía total (SSI) y el bien común (DecSoc) se resuelve de la siguiente manera:

La tensión que ves existe porque Vitalik está dispuesto a sacrificar un poco de esa "soberanía absoluta" e individualista de la SSI en favor de una identidad colectiva y verificable que permita que la sociedad descentralizada realmente funcione.


## Identidad autosoberana: el nuevo paradigma

[Self-Sovereign Identity (SSI)](https://en.wikipedia.org/wiki/Self-sovereign_identity), o identidad autosoberana. Este principio establece que los individuos deben tener control completo sobre sus credenciales, datos personales y cómo se comparten, sin depender de autoridades centrales para validación o almacenamiento. El término fue popularizado en el artículo [The Path to Self-Sovereign Identity](https://www.lifewithalacrity.com/article/the-path-to-self-sovereign-identity/) de Christopher Allen.

[W3C](https://www.w3.org/) (World Wide Web Consortium), el organismo internacional que desarrolla estándares web abiertos, definió formalmente varios estándares al respecto: la [Decentralized Identifiers (DIDs)](https://www.w3.org/TR/did-core/), [Verifiable Credentials (VCs)](https://www.w3.org/TR/vc-data-model/) y [Verifiable Presentations (VPs)](https://www.w3.org/TR/vc-data-model/#presentations) que sirve de facto como la implementación fundamental SSI como solución técnica. Se puede resumir, aunque lo veremos más adelante, que DID es el identificador, que define el DID:método que es el sistema donde se registra, VC es el documento acreditativo que guardas, y VP es la evidencia que generas para el verificador.

Web3 como solución descentralizada y eIDAS con la EUDI Wallet de alguna forma están abrazando esta idea, cada una con su enfoque diferente, web3 siempre con su enfoque permisionless, mientras que eIDAS domesticando la descentralización de identidad.

En la práctica, ambas admiten que la wallet (billetera digital) actúa como tu identidad base donde viven nuestras VC, como si fuera un pasaporte, en este caso digital, permitiendo, según la implementación, el uso de ZK proofs que eviten dar más información de la necesaria.

### DPKI y DID: Los cimientos de la identidad autosoberana

A diferencia de la infraestructura tradicional de clave pública ([PKI](https://en.wikipedia.org/wiki/Public_key_infrastructure)), donde dependemos de autoridades centrales llamadas Certificate Authorities (CAs) para validar y certificar las claves públicas de otros, surge el concepto de Decentralized Public Key Infrastructure (DPKI). En DPKI, no necesitas que una autoridad central certifique que una clave pública pertenece a alguien específico; en su lugar, por ejemplo en el caso de web3, la blockchain actúa como un registro público e inmutable donde cualquiera puede publicar y verificar asociaciones entre identificadores y claves públicas sin intermediarios.

Como dijimos, la [W3C](https://www.w3.org/) (World Wide Web Consortium), el organismo internacional que desarrolla estándares web abiertos, definió formalmente el estándar de [Decentralized Identifiers (DIDs)](https://www.w3.org/TR/did-core/) que sirve de facto como la implementación fundamental para construir sistemas DPKI. Tenemos que aclarar que W3C define un estándar que es la base de la DPKI, pero no significa que lo definiera con ese fin, de hecho, es también usado en EUDI Wallets.

El estándar contempla desde la sintaxis (DID Syntax), la estructura completa (DID Document), los métodos de implementación (DID Methods) y la resolución (DID Resolution) que explicaremos ahora, pero también se define el modelos de datos y relaciones de verificación para establecer la infraestructura, que puedes revisar en el [estándar W3C DID Core](https://www.w3.org/TR/did-core/).

**DID Syntax**:

DID Syntax es el Formato URI (Identificador Único).

Para que todos hablemos el mismo lenguaje, cada DID sigue una estructura fija: did:metodo:identificador_unico.

El método indica dónde reside el ID (puede ser en la red de Ethereum, como did:ethr:0x123, en Bitcoin o incluso en una base de datos de Google si ellos implementan el estándar).

El identificador suele ser una cadena alfanumérica única que representa al sujeto (tú), pero que no revela quién eres por sí misma.

**DID Methods: la infraestructura que lo implementa**:

Como decíamos, los métodos son la infraestructura concreta que implementa el estándar DID. Por ejemplo, en `did:ethr`, sería la propia red Ethereum L1 que alberga los DID Documents mediante smart contracts.

W3C mantiene un [registro oficial de métodos DID](https://www.w3.org/TR/did-spec-registries/) que forman parte de la implementación. Este registro, gestionado mediante pull requests en GitHub, representa uno de los pocos aspectos centralizados del ecosistema: la documentación formal sobre qué métodos existen y cómo funcionan. Cualquiera puede implementar un método sin necesidad de aprobación para usarlo, aunque es cierto que deberá pasar los requisitos técnicos para ser aceptado su pull request.

Los DIDs pueden implementarse de múltiples formas, cada una con trade-offs entre descentralización, costo y funcionalidad. Existen métodos que usan Ethereum como registro (`did:ethr`), métodos puramente criptográficos sin registro alguno (`did:key`), métodos que aprovechan infraestructura web tradicional (`did:web`), métodos de Capa 2 sobre Bitcoin (`did:ion`), y métodos que convierten direcciones blockchain existentes en DIDs sin infraestructura adicional (`did:pkh` para Public Key Hash).

> Este no es un documento de especificación sobre DID ni lo pretende, asi que disculpen si es tan resumido.

Lo importante es entender que no hay una solución única: algunos priorizan descentralización máxima aunque sea más costosa, otros buscan simplicidad aunque sacrifiquen actualización de claves, otros permiten adopción gradual aprovechando dominios web existentes, otros facilitan la transición permitiendo usar direcciones blockchain ya existentes como identificadores sin necesidad de registros adicionales, y otros maximizan privacidad mediante identificadores efímeros por contexto. Todos siguen el estándar W3C DID Core, permitiendo interoperabilidad básica entre métodos.

**DIDs efímeros para privacidad**:

Un método particularmente relevante para Web3 es `did:peer`, diseñado para relaciones punto a punto sin registro público alguno. A diferencia de otros métodos donde tu DID se publica en blockchain o registros, `did:peer` genera identificadores exclusivos para cada relación específica que se descartan después.

Este concepto de **pairwise DIDs** (DIDs por pares) permite que tu wallet genere un DID diferente para cada dApp o protocolo con el que interactúas. Tu exchange descentralizado ve un DID, tu plataforma de lending otro diferente, tu red social descentralizada otro distinto. Esto previene que servicios correlacionen tu actividad entre contextos: nadie puede rastrear que la misma identidad que comercia en Uniswap también participa en gobernanza de una DAO específica.

Los DIDs efímeros son especialmente útiles en mensajería descentralizada (cada conversación usa DIDs únicos generados para esa interacción), interacciones DeFi sensibles donde no quieres que tu actividad financiera sea correlacionable públicamente, y sistemas de votación anónima en DAOs donde necesitas probar elegibilidad sin revelar tu identidad persistente.

La privacidad que ofrecen los pairwise DIDs contrasta con usar un único DID público para todo: si usas `did:ethr:0x123...` en múltiples servicios, cualquiera puede correlacionar todas tus interacciones consultando la blockchain. Con DIDs efímeros, cada contexto está aislado criptográficamente.

Es importante aclarar que los DIDs efímeros resuelven privacidad de IDENTIDAD en interacciones off-chain, pero no pueden ocultar transacciones financieras on-chain. Cuando ejecutas una transacción en blockchain (enviar tokens, interactuar con un smart contract), tu dirección Ethereum real siempre es visible porque el contrato necesita saber desde dónde debitar fondos y hacia dónde acreditarlos. Los activos viven en direcciones específicas, no en DIDs abstractos. Por esto, los DIDs efímeros son útiles para presentar credenciales, mensajería, y verificaciones de identidad, pero no para privacidad financiera, como en DeFi, donde se requieren soluciones diferentes como ZK-rollups con privacidad, stealth addresses, o protocolos de mixing.

**DID Resolution: de identificador a documento verificable**:

Hasta ahora hemos visto qué es un DID (el identificador) y dónde vive (el método). Pero para que un DID sea útil, necesitas poder obtener su DID Document, el archivo JSON que contiene las claves públicas y metadata necesarias para verificar identidad. Aquí entra la resolución de DIDs.

DID Resolution es el proceso estandarizado de convertir un DID string (como `did:ethr:0x123...`) en su DID Document correspondiente. Un resolver es el software que implementa este proceso, consultando la infraestructura específica del método para recuperar el documento. La belleza del estándar W3C es que todos los resolvers siguen la misma interfaz: le das un DID, te devuelve un DID Document, independientemente del método subyacente.

Cuando tu aplicación necesita verificar una firma de alguien con DID `did:ethr:0xabc...`, el resolver consulta el smart contract de registro en Ethereum L1, recupera el DID Document asociado a esa dirección, y tu aplicación usa las claves públicas de ese documento para validar la firma. Si fuera `did:web:example.com`, el resolver haría una petición HTTPS a `https://example.com/.well-known/did.json` para obtener el documento. Cada método tiene su propia lógica de recuperación, pero la interfaz que ofrece el resolver es uniforme.

La resolución también puede devolver metadata adicional sobre el proceso: si el DID fue desactivado, si el documento ha sido actualizado recientemente, o si existen versiones históricas del mismo. Esto es crucial para sistemas que necesitan auditar cambios de identidad a lo largo del tiempo.

**El DID Document (Metadatos de Verificación)**:

El DID Document es un archivo (normalmente en formato JSON) que contiene los metadatos técnicos necesarios que permiten verificar el ID (la identidad) criptográficamente. Para más detalle leer la [especificación W3C DID Core](https://www.w3.org/TR/did-core/#core-properties). Resumiendo incluye métodos de verificación (claves públicas y algoritmos), métodos de autenticación, endpoints de servicio para comunicación, y mecanismos de gestión y actualización del DID.

Este documento no guarda identidades personales como tu nombre o email, solo la infraestructura criptográfica que permite verificar que tú eres quien dices ser.

### Las Verifiable Credentials (VCs)

W3C define de forma complementaria el estándar de [Verifiable Credentials](https://www.w3.org/TR/vc-data-model/), un modelo de datos para credenciales verificables que los emisores pueden emitir y que otros pueden validar criptográficamente usando los DID Documents de los actores involucrados.

En esencia, las VCs son documentos en formato JSON que contienen afirmaciones o claims sobre un sujeto, emitidos por una entidad y firmados digitalmente. El emisor tiene un DID, el sujeto (persona sobre quien se hace la afirmación) tiene un DID, y el verificador puede usar los DID Documents de ambos para validar la autenticidad de la credencial.

Por ejemplo, una VC puede contener cualquier tipo de información: tu email verificado, tu edad, un diploma universitario, una certificación profesional, o tu membresía en una organización. Lo que las hace "verificables" es que están firmadas criptográficamente por el emisor usando su DID, permitiendo que cualquier verificador pueda comprobar matemáticamente su autenticidad consultando el DID Document del emisor, sin necesidad de contactarlo directamente.

Una aclaración: una VC materializa una attestation como un objeto estándar: cuando el emisor da fe (attests) de ciertos atributos del sujeto, esa attestation se concreta en el documento VC estructurado según el estándar W3C, con la firma criptográfica del emisor y los claims específicos sobre el titular.

Estas credenciales viven en tu wallet bajo tu control exclusivo. Tú decides cuándo y a quién mostrarlas. Si pierdes tu wallet, necesitarás solicitar nuevamente estas credenciales a los emisores originales, aunque existen mecanismos de recuperación social y respaldo que pueden ayudar en estos escenarios.

> Aspectos que podrás ver en el documento de [experiencia de usuario](./8-1-user-experience.md).

Las VCs tienen la capacidad de verificación selectiva. Por ejemplo, puedes tener una credencial que contiene tu fecha de nacimiento completa emitida por el gobierno, pero cuando necesites probar que eres mayor de edad para acceder a un servicio, puedes presentar una prueba derivada que solo revela "es mayor de 18 años" sin exponer tu fecha exacta de nacimiento. Esto se logra mediante técnicas criptográficas como [Zero-Knowledge Proofs](https://ethereum.org/en/zero-knowledge-proofs/).

### Verifiable Presentations: presentando credenciales selectivamente

Cuando posees Verifiable Credentials en tu wallet, raramente las compartes directamente en su forma completa. En su lugar, creas [Verifiable Presentations (VPs)](https://www.w3.org/TR/vc-data-model/#presentations), un estándar W3C complementario a VCs que define cómo presentar una o más credenciales a un verificador de forma controlada.

Una Verifiable Presentation es un contenedor firmado que agrupa las credenciales que decides revelar para un contexto específico. Si un servicio necesita verificar tu edad y tu membresía en una organización, creas una VP que contiene solo esas dos credenciales, no todas las que posees. La VP está firmada por ti usando tu DID, probando que eres el titular legítimo de esas credenciales y que autorizas explícitamente su presentación en este contexto.

La potencia de las VPs se multiplica con Zero-Knowledge Proofs. Puedes crear una VP que demuestre predicados derivados sin revelar datos subyacentes: "soy mayor de 18 años" sin mostrar tu fecha de nacimiento, "vivo en país permitido" sin revelar tu dirección exacta, "tengo saldo suficiente" sin exponer tu balance completo. El verificador recibe prueba matemática de la afirmación sin acceder a información sensible.

Las VPs también incluyen timestamps y pueden limitarse a verificadores específicos mediante encriptación. Esto previene que una presentación creada para el servicio A sea reutilizada fraudulentamente ante el servicio B. Cada presentación es contextual y firmada específicamente para ese propósito, creando trazabilidad auditada de qué credenciales revelaste, a quién, y cuándo.

### Casos de uso y roles

Las VCs operan mediante un triángulo de confianza de actores con diferente rol, donde emisor, titular y verificador son independientes entre sí. Este desacoplamiento contrasta radicalmente con Web2, donde plataformas como Google o Facebook centralizan estos tres roles: ellas mismas validan tu identidad (emisor), almacenan tus datos en sus servidores (custodia), y verifican tu acceso cada vez que inicias sesión (verificador). En Web3, estos roles están separados criptográficamente: una universidad emite tu credencial, tú la custodias en tu wallet, y un empleador la verifica sin contactar a la universidad porque el ancla de confianza es el propio método, como sería el caso de did:ethr.

Los casos de uso fundamentales en el ecosistema de VCs que podemos ver son:

- **Emisor emite credencial verificable a titular**: Una entidad con autoridad certifica atributos del sujeto mediante una credencial firmada digitalmente. Ejemplo: universidad emite diploma académico, gobierno emite certificado de residencia, empresa emite credencial de experiencia laboral
- **Titular custodia credencial en wallet personal**: El sujeto almacena y gestiona sus credenciales bajo control exclusivo sin depender de servidores centralizados. Ejemplo: usuario guarda sus diplomas, certificaciones y credenciales KYC en MetaMask o Privado ID
- **Titular presenta credencial verificable ante verificador**: El titular genera una presentación selectiva de credenciales para demostrar atributos específicos en un contexto determinado. Ejemplo: presentar prueba de edad mayor de 18 sin revelar fecha exacta de nacimiento, demostrar residencia en jurisdicción permitida sin exponer dirección postal completa
- **Verificador valida autenticidad de credencial sin contactar emisor**: Un servicio comprueba criptográficamente la validez de una credencial consultando el DID Document del emisor, sin comunicación directa. Ejemplo: protocolo DeFi verifica credencial KYC para acceso a pool permisionado, plataforma de gobernanza valida membresía DAO para habilitar votación
- **Titular revoca acceso o presenta credencial con restricciones temporales**: El titular controla cuándo y a quién muestra sus credenciales, pudiendo limitar presentaciones por tiempo, contexto o verificador específico. Ejemplo: autorizar acceso a credencial educativa solo durante enero 2026 y únicamente para verificadores universitarios
- **Titular agrega credenciales de múltiples emisores en presentación única**: El sujeto combina credenciales de diferentes fuentes para contextos que requieren validación multidimensional. Ejemplo: presentar simultáneamente reputación de DAO A, certificación de protocolo B e historial profesional de empresa C ante un potencial empleador

**Delegación de identidad y autorización**:

Después de ver varios casos de uso, tenemos que destacar otro importante, habilitado por las VPs: la delegación de identidad y autorización. Si quieres ver en detalle aspectos técnicos puedes acceder a [DID Protocols](../infrastructure/identity/did-protocols.md), pero aquí está el resumen conceptual.

Más allá de presentar tus propias credenciales, frecuentemente necesitas permitir que otros actúen en tu nombre sin entregarles control total. Esto se logra mediante [Authorization Capabilities (ZCAP)](https://w3c-ccg.github.io/zcap-spec/), una especificación del [W3C Credentials Community Group](https://w3c-ccg.github.io/) que define tokens criptográficos firmados que otorgan permisos específicos a un DID delegado. Basándose en el modelo de [Object Capabilities (OCAP)](https://en.wikipedia.org/wiki/Object-capability_model), las capabilities funcionan bajo el principio de "quien posee el token, tiene el permiso" (bearer token): son verificables criptográficamente sin necesidad de coordinación centralizada, a diferencia de sistemas tradicionales donde la autorización se verifica consultando bases de datos centrales de permisos.

Las capabilities permiten permisos descentralizados granulares con restricciones precisas: puedes autorizar que alguien presente tu credencial educativa solo durante enero 2026 y solo a verificadores universitarios, o que un representante vote en tu nombre en una DAO solo para propuestas de categoría "tesorería". Estas autorizaciones son revocables instantáneamente sin cambiar tus credenciales subyacentes.

Además existen las **jerarquías de autoridad descentralizadas** que son fundamentales para identidad corporativa. Una organización posee un DID corporativo raíz que representa la entidad legal, y emite capabilities derivadas a empleados para actuar en representación corporativa dentro de límites específicos. Un empleado de ventas recibe autorización para firmar contratos hasta $50,000, un contador recibe permisos para presentar credenciales financieras corporativas ante auditores. Cada nivel de delegación añade restricciones adicionales creando cadenas de autoridad verificables: empleado X actuó bajo autoridad Y otorgada por ejecutivo Z, todo auditable on-chain sin sistemas centralizados.

### El ecosistema Web3 de VC: Emisores, Titulares y Verificadores

El ecosistema de identity Web3 ha desarrollado varias implementaciones de VCs o credenciales verificables, en muchos casos con privacidad mediante Zero-Knowledge Proofs. Las veremos en [9-1-ecosystem-DApps](9-1-ecosystem-DApps.md), aunque aquí veremos las fundamentales.

**Emisores (Issuers)**:

Entidades que validan y certifican información. Una universidad verifica que completaste tu grado, un gobierno confirma tu ciudadanía, una empresa atestigua tu experiencia laboral. Tras validar, emiten la credencial firmada con su DID. [Fractal ID](https://web.fractal.id/) y [Civic](https://www.civic.com/) operan como emisores KYC especializados: verifican documentos legales o biometría, y emiten VCs que otros servicios pueden consumir sin repetir el proceso.

Como emisores, emergen soluciones híbridas que intentan hacer KYC menos invasivo usando infraestructura descentralizada como herramienta, no como fin. Servicios como [Coinbase Onchain Verifications](https://www.coinbase.com/onchain-verify), o las mencionadas [Fractal ID](https://web.fractal.id/) y [Civic](https://www.civic.com/) operan bajo un modelo de "KYC reutilizable": completas verificación de identidad legal tradicional con ellos (centralizadamente), y luego emiten una credencial verificable que prueba "este usuario pasó KYC nivel X" sin revelar tus datos personales cada vez que interactúas con protocolos.

**Titulares (Holders)**:

El usuario final que recibe y custodia sus credenciales. Las VCs se almacenan en tu dispositivo, no en servidores del emisor ni del verificador. [Privado ID](https://www.privadoid.com/) (anteriormente Polygon ID) ejemplifica la infraestructura del titular: un ecosistema completo de identidad autosoberana que incluye wallet móvil, soporte nativo para ZK-proofs, y herramientas para gestionar credenciales privadamente. El titular decide qué revelar, cuándo y a quién, generando pruebas selectivas según cada contexto.

**Verificadores (Verifiers)**:

Servicios que consumen credenciales sin contactar al emisor. La verificación es puramente criptográfica: consultan el DID Document del emisor para validar la firma, sin comunicación directa. Como ejemplo [Gnosis Safe](https://www.gnosis.io/) implementa verificación mediante módulos que condicionan ejecución de transacciones a posesión de credenciales específicas. Otros verificadores incluyen protocolos DeFi como [Aave Arc](https://aave.com/) que requieren VCs de KYC para acceso a pools permisionados, plataformas de gobernanza como [Snapshot](https://snapshot.org/) que verifican credenciales de membresía para habilitar votación, y marketplaces NFT que verifican credenciales de artista verificado antes de mostrar colecciones destacadas. Igualmente lo podemos ver en protocolos DeFi que verifican cumplimiento regulatorio (sanciones, jurisdicciones prohibidas) antes de permitir operaciones, consumiendo VCs sin acceder a datos personales del usuario.

### Coexistencia centralizado y descentralizado

El modelo eIDAS 2.0 representa domesticar el principio de Self-Sovereign Identity (SSI) que fundamenta Web3. Mientras SSI propone que cada individuo controle completamente sus credenciales sin depender de autoridades centrales, eIDAS 2.0 concentra el control en manos del Estado, creando un sistema donde:

- Emisión y revocación institucional: Los Estados miembros controlan qué entidades pueden emitir credenciales oficiales y bajo qué circunstancias pueden revocarse, manteniendo soberanía gubernamental sobre identidad legal. Esto no es malo en sí mismo, simplemente representa una implementación permisionada de SSI en lugar del modelo permissionless de Web3
- Interoperabilidad regional: Diseñado para funcionar dentro del espacio económico europeo, con portabilidad entre Estados miembros pero sin garantías de reconocimiento fuera de esta jurisdicción.
- Punto único de fallo: a no ser que se diga lo contrario, eIDAS 2.0 no dice que se deba usar [EBSI (European Blockchain Services Infrastructure)](https://ec.europa.eu/digital-building-blocks/wikis/display/EBSI/Home), una blockchain permisionada operada por nodos de múltiples Estados miembros. En ese caso, esta identificación, si está basada en un servicio central, tendrá un SPOF o punto único de fallo, algo crítico en un sistema que tiene que ser resiliente.

Aunque es cierto que cumple con protecciones GDPR integradas, algo que muchos usuarios agradecen: La regulación europea incluye garantías de privacidad (derecho al olvido, portabilidad limitada, consentimiento explícito) que no existen necesariamente en implementaciones Web3 puramente descentralizadas

Este contraste no es meramente técnico sino profundamente político. Como señalan críticos del sistema, la identidad digital obligatoria puede convertirse en un mecanismo de control social donde el Estado puede, en teoría, negar acceso a servicios esenciales basándose en criterios que escapan al control del individuo.

**Interoperabilidad y convergencia: el estándar OpenID4VC**:

A pesar de las diferencias filosóficas (centralizado vs descentralizado), existe un área de convergencia técnica significativa. La industria está adoptando masivamente el estándar [OpenID for Verifiable Credentials (OpenID4VC)](https://openid.net/sg/openid4vc/), que permite utilizar los rieles probados de OpenID Connect (la tecnología detrás de "Log in with Google") para el intercambio de credenciales verificables.

Esto significa que tanto la futura [European Digital Identity Wallet (EUDI)](https://digital-strategy.ec.europa.eu/en/policies/eudi-wallet-implementation) como las wallets Web3 nativas (como MetaMask o Privado ID) están convergiendo hacia los mismos protocolos de transporte. Técnicamente, esto podría permitir que una wallet Web3 almacene una credencial oficial del gobierno (siempre que cumpla con los requisitos de seguridad del nivel de garantía) o que una wallet institucional verifique credenciales emitidas por protocolos descentralizados.

Esta adopción de estándares técnicos comunes facilita

- Interoperabilidad real: credenciales emitidas bajo eIDAS podrían, técnicamente, verificarse en aplicaciones Web3 y viceversa, siempre que se confíe en los emisores.
- Experiencia de usuario unificada: el flujo para recibir una credencial del gobierno o un diploma de una DAO sería idéntico para el usuario (escanear QR o click en link).
- Adopción de mejoras de privacidad: permite integrar técnicas como [Selective Disclosure](https://www.w3.org/TR/vc-data-model/#dfn-selective-disclosure) y [Zero-Knowledge Proofs](https://ethereum.org/en/zero-knowledge-proofs/) sobre infraestructuras existentes.

Sin embargo, es crucial entender que usar los mismos estándares técnicos no elimina la diferencia fundamental de control y gobernanza. Que usen el mismo "lenguaje" técnico no cambia que en el modelo centralizado la raíz de confianza es el Estado (que puede revocarla), mientras que en Web3 la raíz es la criptografía y el consenso descentralizado.

> Es un estándar sin madurar, veremos cómo evoluciona, por lo tanto, tampoco voy a desarrollar mucho este apartado.

**El pragmatismo del usuario de web3**:

El escenario más probable no es que Web3 reemplace completamente los sistemas estatales, sino que ambos coexistan:

- Identidad legal vs. identidad social: los gobiernos continuarán emitiendo documentos oficiales (pasaportes, licencias, títulos académicos), pero los individuos podrán gestionar reputación, participación comunitaria y credenciales no-oficiales en sistemas descentralizados.
- Casos de uso diferenciados: interacciones con el Estado pueden requerir eIDAS, mientras que participación en DAOs, protocolos DeFi, o comunidades Web3 utilizará identidades descentralizadas y en muchos casos con KYC/AML.
- Resistencia a la censura: sistemas descentralizados proporcionan alternativas resilientes cuando sistemas centralizados fallan, son censurados, o excluyen a ciertos grupos.

La clave está en entender que la identidad descentralizada no es principalmente una alternativa técnica a los sistemas estatales, sino una garantía de libertad digital. Incluso en escenarios donde regulaciones obliguen el uso de identidades centralizadas para ciertos servicios, mantener sistemas descentralizados paralelos preserva la capacidad de participación económica, social y política fuera del control estatal directo.

En resumen, para usuarios, la identidad Web3 existe actualmente en tres capas distintas: tu identidad legal KYC en exchanges (completamente centralizada), tu identidad pseudónima on-chain para interacciones generales (direcciones Ethereum), y identidad autosoberana.


### Consideraciones y desafíos


---


----



## Attestation Layer: la capa de verificación on-chain

Más allá de las Verifiable Credentials que vimos como estándar W3C para credenciales off-chain, el ecosistema blockchain ha desarrollado lo que se conoce como Attestation Layer o Capa de Atestación: infraestructura on-chain diseñada específicamente para registrar, verificar y gestionar attestations de forma nativa.

Un attestation, en su concepto más fundamental de seguridad informática, es una declaración firmada digitalmente por un emisor que da fe de ciertos atributos o afirmaciones sobre un sujeto. Este concepto existe desde hace décadas en sistemas de seguridad tradicionales. Se define como capa de atestación en lugar de credenciales porque tiene un enfoque más primitivo, son documentos de verificación no evidencias de un sujeto que utiliza para identificarse.

Al igual que las VCs, las attestations son tecnológicamente neutrales y pueden usarse para múltiples propósitos: identidad autosoberana genuina (diplomas universitarios, membresías en DAOs, contribuciones open source), reputación social (asistencia a eventos, participación comunitaria), o compliance regulatorio (verificación KYC, sanctions screening). La diferencia fundamental con VCs es que las attestations típicamente viven públicamente on-chain donde smart contracts pueden componerlas, mientras que VCs priorizan almacenamiento privado off-chain bajo control del usuario.

Ejemplos reales incluyen universidades como [MIT Digital Credentials](https://digitalcredentials.mit.edu/) que emiten diplomas verificables, certificaciones profesionales que pueden verificarse instantáneamente, sistemas de reputación profesional como LinkedIn pero donde las habilidades son attestations verificables emitidas por organizaciones reconocidas, o proveedores KYC que emiten attestations confirmando "usuario verificado" sin exponer datos sensibles.

**Ethereum Attestation Service (EAS): implementación específica de Attestation Layer**:

[Ethereum Attestation Service (EAS)](https://attest.sh/) es un producto y servicio concreto que se ha establecido como una de las implementaciones líderes de la Attestation Layer en Ethereum y L2s compatibles. EAS no es "la arquitectura" de attestations, sino una implementación específica y popular de esta arquitectura más amplia. La propuesta de valor de EAS radica en su simplicidad: proporciona smart contracts estandarizados y APIs donde cualquiera puede emitir attestations verificables on-chain sin necesidad de desplegar contratos propios ni inventar formatos incompatibles.

El modelo conceptual de EAS gira alrededor de dos elementos: schemas y attestations. Los schemas definen estructuras de datos reutilizables, como plantillas que especifican qué campos debe contener una attestation (por ejemplo, un schema de "asistencia a eventos" incluiría campos como nombre del evento, fecha, y participante). Las attestations son instancias concretas de estos schemas, firmadas por emisores específicos sobre sujetos específicos.

Lo importante del Schema Registry de EAS es que funciona como un catálogo público donde la comunidad puede descubrir y reutilizar schemas existentes en lugar de fragmentar el ecosistema con formatos incompatibles. Si tu DAO necesita atestiguar membresía, probablemente ya existe un schema estándar que múltiples organizaciones usan. Esta estandarización permite que aplicaciones que consumen attestations entiendan datos de múltiples emisores sin integraciones personalizadas para cada uno.

EAS soporta attestations tanto on-chain como off-chain según las necesidades del caso de uso. Las attestations on-chain viven permanentemente en blockchain con verificabilidad máxima y composabilidad directa con smart contracts, pero implican costos de gas. Las attestations off-chain se firman criptográficamente y almacenan fuera de blockchain, con solo un hash registrado on-chain, reduciendo dramáticamente costos pero introduciendo dependencia de disponibilidad externa.

**Más allá de EAS: ecosistema de attestations**:

Aunque EAS domina como infraestructura de attestations, existe un ecosistema más amplio de soluciones de identidad y credenciales. El documento [9-1-ecosystem-DApps](9-1-ecosystem-DApps.md) explora estas implementaciones concretas y sus casos de uso prácticos.

**On-chain vs off-chain attestations: trade-offs críticos**:

EAS soporta dos modos de almacenamiento con implicaciones técnicas y económicas significativas.

Las attestations on-chain se registran directamente en smart contracts desplegados en Ethereum L1 o L2s. Cada attestation se almacena permanentemente en blockchain storage, accesible mediante queries a los contratos EAS. Las ventajas incluyen verificabilidad máxima porque cualquiera puede consultar la blockchain directamente sin confiar en servicios externos, permanencia garantizada porque los datos sobrevivirán mientras exista la blockchain, y composabilidad nativa porque otros smart contracts pueden leer y reaccionar a estas attestations programáticamente.

Los trade-offs incluyen costos de gas significativos. En Ethereum L1, emitir una attestation puede costar $5-50 dependiendo de congestión de red. L2s como Optimism reducen esto a centavos, pero aún existe fricción económica. El storage permanente también significa que attestations sensibles quedan públicamente visibles para siempre, aunque el contenido puede encriptarse antes de registration. Para casos de uso de alto volumen, estos costos se acumulan rápidamente: un sistema de reputation scoring que emite millones de attestations diarias enfrentaría costos prohibitivos on-chain.

Las attestations off-chain se firman criptográficamente por el emisor pero almacenan fuera de blockchain, típicamente en bases de datos tradicionales o storage descentralizado como IPFS. Solo el hash de la attestation y metadata mínima se publican on-chain, reduciendo dramáticamente costos. El contenido completo se sirve mediante APIs de EAS o infraestructura propia del emisor.

Las ventajas incluyen costos órdenes de magnitud menores, adecuados para aplicaciones de alta frecuencia, flexibilidad para actualizar metadata o revocar attestations sin transacciones on-chain adicionales, y privacidad mejorada porque el contenido sensible puede almacenarse con acceso controlado. Los trade-offs son dependencia de disponibilidad de servicios externos porque si el storage off-chain desaparece, solo queda el hash on-chain, y verificación más compleja porque los verificadores deben confiar en que el contenido servido coincide con el hash registrado.

**Composabilidad: attestations como legos de reputación**:

La verdadera potencia de la Attestation Layer emerge cuando múltiples protocolos componen attestations de diversas fuentes para construir sistemas de reputación ricos. Imagina un protocolo de préstamos descentralizado que evalúa solvencia considerando attestations de membresía en DAOs respetadas, attestations de historial de repago en otros lending protocols, attestations de tenencia de tokens específicos, y si el protocolo debe cumplir regulaciones, attestations de verificación KYC de proveedores autorizados.

Cada attestation proviene de un emisor diferente, pero todos son verificables mediante la misma infraestructura on-chain. El lending protocol implementa lógica que pondera estas attestations según su confianza en cada emisor y la relevancia de los claims, generando un credit score componible. Las attestations de reputación social (membresías, contribuciones) construyen confianza descentralizada genuina, mientras que attestations de KYC permiten cumplir requisitos legales sin comprometer privacidad más allá de lo estrictamente necesario. Este modelo híbrido es imposible en sistemas centralizados donde cada plataforma mantiene silos de reputación incompatibles.

Gitcoin Passport ejemplifica perfectamente esta composabilidad. Como sistema de Proof of Personhood anti-Sybil (explicado en detalle en la [sección dedicada a Proof of Personhood](#proof-of-personhood-demostrando-que-eres-humano-único)), Gitcoin Passport agrega attestations de docenas de fuentes diferentes: verificación de Twitter, staking de ETH, participación histórica en Gitcoin Grants, verificación biométrica de BrightID. Cada stamp es una attestation on-chain. El Passport score se calcula ponderando estas attestations según algoritmos anti-Sybil, demostrando cómo múltiples credenciales componibles crean identidad verificable robusta resistente a manipulación.

**Lógica programable en EAS: Resolver Contracts**:

EAS permite opcionalmente asociar resolver contracts a schemas específicos. Estos resolver contracts son smart contracts que actúan como intermediarios programables dentro del ecosistema EAS: cuando alguien intenta emitir, revocar o verificar una attestation usando ese schema, el resolver ejecuta automáticamente código personalizado que puede aprobar, rechazar o modificar la operación.

Es importante no confundir estos resolver contracts de EAS con los DID Resolvers que vimos en secciones anteriores. Un DID Resolver es software que convierte un DID string en su DID Document consultando la infraestructura del método correspondiente. Un EAS Resolver Contract es un smart contract específico que ejecuta lógica de negocio cuando se operan attestations. Son conceptos completamente diferentes que comparten el término "resolver" pero operan en contextos distintos.

Los resolver contracts de EAS permiten agregar lógica de negocio compleja a las attestations. Imagina que quieres emitir attestations de acceso premium solo a miembros verificados de tu DAO. El resolver puede verificar automáticamente que el destinatario posee un token de membresía antes de permitir la emisión. Si no cumple el requisito, la transacción falla directamente en el smart contract.

Los resolvers también pueden desencadenar acciones automáticas. Cuando se emite una attestation específica, el resolver podría acuñar un NFT para el usuario, transferir tokens como recompensa, o notificar a otros contratos del evento. En el caso de revocaciones, el resolver puede implementar reglas de gobernanza que determinen quién tiene autoridad para revocar attestations específicas, protegiendo contra ataques donde actores maliciosos intentan eliminar attestations legítimas.

Sin embargo, los resolvers añaden complejidad técnica y superficie de ataque. Un bug en el código del resolver puede bloquear completamente la emisión de attestations o introducir vulnerabilidades de seguridad. Por esta razón, la mayoría de schemas operan sin resolvers. En lugar de validar condiciones durante la emisión, estos sistemas confían en que los verificadores implementen su propia lógica al momento de consultar las attestations.

## Mejores prácticas en VC y Attestations

### La importancia crítica de confiar en el emisor

Determinar si debes confiar en el emisor de un VC o atestación está es quizás el aspecto más importante y a menudo malentendido de las credenciales verificables.

La criptografía garantiza que la universidad con DID `did:ethr:0x123...` emitió tu diploma, pero no puede decirte si esa entidad realmente es Stanford University o un impostor. La tecnología verifica la firma, pero tú como verificador debes decidir si confías en la reputación y autoridad del emisor para hacer esas afirmaciones. Un diploma firmado por una universidad prestigiosa tiene valor porque confías en su proceso de evaluación académica; el mismo diploma firmado por una entidad desconocida no tiene peso, aunque técnicamente ambas credenciales sean válidas criptográficamente.

En la práctica, la confianza en emisores se construye mediante varios mecanismos que operan en capas superiores. Algunos ecosistemas mantienen registries on-chain de emisores autorizados gobernados por DAOs. Otros confían en la reputación acumulada y el reconocimiento social del emisor. Proyectos empresariales pueden establecer trust frameworks donde organizaciones participantes acuerdan mutuamente reconocer sus credenciales. Plataformas de análisis blockchain pueden construir scores de reputación basados en el historial de emisión.

La descentralización significa que no existe una autoridad central que certifique emisores globalmente, lo cual es intencional por diseño. Cada contexto define sus propios criterios de confianza. Una DAO puede aceptar credenciales de ciertos emisores para membresía, mientras otra DAO rechaza esos mismos emisores pero confía en otros diferentes. Esta flexibilidad contextual es poderosa pero requiere que verificadores hagan su diligencia debida sobre qué emisores aceptan.

### Diseño correcto: semántica temporal de para attestations y VCs

Un aspecto crucial que aplica tanto a Verifiable Credentials como a attestations on-chain es la semántica temporal de las afirmaciones. Muchos malentienden que firmar digitalmente una credencial o registrarla permanentemente en blockchain garantiza su validez perpetua. En realidad, solo certifica que esa afirmación específica fue hecha en un momento determinado por un emisor verificable. Si tu empleador emite una credencial en 2023 que dice "trabaja en la empresa X", esa credencial registra permanentemente esa afirmación. Sin embargo, la afirmación era verdadera en 2023, pero puede dejar de serlo en 2024 si te despiden.

Por esto, el diseño de credenciales debe ser muy cuidadoso con la semántica temporal independientemente de si son VCs off-chain o attestations on-chain. Existen varias aproximaciones correctas que aplican a ambos modelos:

**Credenciales con fecha de expiración explícita**: "trabajó en empresa X desde enero 2023 hasta diciembre 2023", donde la validez temporal está codificada en los datos del claim. Cuando alguien verifica la credencial en 2025, puede ver que ya expiró sin necesidad de consultar mecanismos de revocación. Esto funciona bien para contratos temporales, certificaciones que caducan, o membresías por tiempo limitado.

**Credenciales de estado actual con revocación**: "actualmente emplea a esta persona", que se entiende válida desde la emisión hasta que sea revocada explícitamente. El emisor tiene la responsabilidad de revocarla cuando el estado cambie. Esto es apropiado para relaciones continuas donde la fecha de finalización no se conoce al momento de emisión.

**Credenciales de eventos puntuales**: "completó este curso en marzo 2023" o "asistió a este evento en 2024", donde la afirmación describe un hecho histórico que no cambia con el tiempo y por tanto raramente requiere revocación. Estas son las credenciales más simples porque su validez es intrínsecamente permanente.

El problema surge cuando las credenciales se diseñan ambiguamente sin considerar su semántica temporal. Si un claim dice "es empleado de la empresa X" sin especificar temporalidad ni implementar mecanismos de revocación proactivos, estás creando una afirmación que pretende ser verdad indefinidamente pero no tienes forma de invalidarla cuando deje de ser cierta. Esta es una falla de diseño, no una limitación técnica de la infraestructura.

Para attestations on-chain, la inmutabilidad blockchain es ventajosa para auditoría histórica: puedes demostrar que en 2023 tenías esa afirmación válida sobre ti, incluso si después fue revocada. Para VCs off-chain, el archivo firmado en tu wallet cumple función similar: prueba que en algún momento el emisor hizo esa afirmación sobre ti. En ambos casos, confundir "registro permanente de que se hizo una afirmación" con "la afirmación es verdadera para siempre" es un error conceptual fundamental que debe evitarse mediante diseño correcto de schemas y procesos de gestión de credenciales.

### Revocación: mecanismos para attestations y VCs

La revocación es un aspecto crítico tanto para attestations on-chain como para Verifiable Credentials off-chain, pero los mecanismos son diferentes según el tipo de credencial.

**Revocación de attestations on-chain (EAS y similares)**:

Cuando una attestation se registra en un smart contract como EAS, el mecanismo de revocación está integrado en el protocolo. El emisor original puede llamar a la función de revocación del contrato, que marca esa attestation específica como revocada en el registro on-chain mediante un flag booleano.

El proceso es directo: el smart contract registra quién emitió cada attestation. Solo ese emisor (o direcciones autorizadas según el schema) puede revocarla posteriormente. El titular sigue "poseyendo" la attestation en el sentido de que fue emitida a su dirección, pero ahora tiene estado de revocación marcado. Cuando un verificador consulta la attestation, el smart contract devuelve tanto los datos como el estado de revocación actual. Este proceso es instantáneo porque solo requiere consultar el contrato, sin necesidad de contactar al emisor.

EAS implementa revocación nativa mediante la función `revoke()` documentada en [docs.attest.sh/docs/core--concepts/revocation](https://docs.attest.sh/docs/core--concepts/revocation). Otras implementaciones de Attestation Layer pueden usar mecanismos similares con variaciones en los detalles técnicos.

**Revocación de Verifiable Credentials off-chain**:

Para VCs que siguen el estándar W3C y se almacenan off-chain en la wallet del usuario, el mecanismo es diferente. El emisor mantiene una lista de revocación separada que puede ser un archivo JSON publicado en un servidor, un registro on-chain específico para revocaciones, o un servicio API.

Cuando el emisor decide revocar una VC, agrega el ID único de esa credencial a su lista de revocación. El usuario conserva físicamente el archivo JSON de la VC en su wallet, pero cuando un verificador la comprueba, además de validar la firma criptográfica consultando el DID Document del emisor, debe consultar la lista de revocación para verificar si esa credencial específica ha sido invalidada. Si está en la lista, los verificadores la rechazan aunque técnicamente la firma sea válida.

Esta separación entre posesión y validez es fundamental: el usuario siempre tiene el archivo (posesión), pero el emisor controla si sigue siendo válida (validez). La autoridad del emisor deriva de su DID: como firmó la credencial con su clave privada asociada a ese DID, solo él puede actualizar el registro de revocación de credenciales firmadas por ese DID.

La revocación plantea desafíos de privacidad importantes. Si cada verificación requiere consultar un registro centralizado controlado por el emisor, éste puede rastrear cuándo y dónde usas tus attestations. Cada consulta a la lista de revocación revela que alguien está verificando esa credencial específica en ese momento. Soluciones avanzadas como [accumulator-based revocation](https://eprint.iacr.org/2020/777) permiten verificar que una attestation no ha sido revocada sin revelar cuál attestation específica estás verificando, preservando privacidad del titular. Estos sistemas usan estructuras criptográficas donde puedes probar que tu credencial no está en el conjunto de revocadas sin identificarla explícitamente.

## Soulbound Tokens: credenciales vinculadas permanentemente

Los Soulbound Tokens (SBTs) representan otra aproximación fundamental para implementar atestaciones que son públicas y permanente en Web3, propuesta formalmente por Vitalik Buterin, E. Glen Weyl y Puja Ohlhaver en su paper de 2022 ["Decentralized Society: Finding Web3's Soul"](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763). La visión detrás de los SBTs es crear una infraestructura de identidad y reputación que capture la riqueza de las relaciones sociales y compromisos del mundo real en el ecosistema blockchain.

El concepto toma su nombre del videojuego World of Warcraft, donde los "soulbound items" son objetos que quedan permanentemente vinculados a un personaje y no pueden transferirse ni venderse. En Web3, esta misma lógica se aplica a tokens que representan credenciales, afiliaciones, compromisos o logros que no deberían poder comercializarse porque su valor radica precisamente en su vinculación auténtica con una identidad específica.

**Características fundamentales de los SBTs**:

La no-transferibilidad es la propiedad definitoria de los SBTs. A diferencia de los NFTs tradicionales que pueden venderse o transferirse libremente, un SBT queda vinculado permanentemente a la dirección que lo recibió inicialmente. Esta característica es crucial para credenciales cuyo valor depende de su autenticidad: un diploma universitario no tiene valor si puede comprarse en un mercado secundario; una certificación profesional pierde sentido si quien la posee no es quien completó la formación.

Los SBTs son públicamente verificables y residen on-chain como tokens siguiendo estándares como [ERC-5192](https://eips.ethereum.org/EIPS/eip-5192), que define interfaces para tokens no transferibles. Cualquiera puede consultar la blockchain y ver qué SBTs posee una dirección específica, permitiendo verificación instantánea sin intermediarios. Esta transparencia pública contrasta con las Verifiable Credentials que típicamente se almacenan off-chain bajo control del usuario.

La composabilidad on-chain permite que smart contracts lean y reaccionen a la presencia o ausencia de SBTs específicos. Por ejemplo, un protocolo de gobernanza podría otorgar peso de voto adicional a direcciones que posean SBTs de participación en eventos comunitarios, o un lending protocol podría ofrecer tasas preferenciales a usuarios con SBTs de buen historial crediticio emitidos por otros protocolos.

**El concepto de "Soul" en DeSoc**:

En la visión de Buterin y coautores, las direcciones Ethereum que acumulan SBTs se convierten en "Souls" o almas digitales que representan identidades sociales complejas. Una Soul no es simplemente una dirección con tokens, sino un conjunto verificable de relaciones, afiliaciones, credenciales y compromisos que construyen una identidad social rica y multidimensional.

Las Souls pueden representar tanto personas como instituciones. Tu Soul personal acumula SBTs emitidos por universidades que certifican tu educación, empleadores que confirman tu experiencia laboral, DAOs que reconocen tus contribuciones, y comunidades que validan tu participación. Simultáneamente, las instituciones también tienen Souls: una universidad tiene su propia identidad verificable mediante SBTs emitidos por organismos acreditadores, gobiernos, o asociaciones académicas.

Esta red de Souls interconectadas mediante SBTs crea lo que los autores llaman "Decentralized Society" (DeSoc): un ecosistema donde la confianza emerge de redes verificables de relaciones y afiliaciones, no de autoridades centrales ni de riqueza financiera acumulada. En DeSoc, tu reputación y capacidades se demuestran mediante el grafo de credenciales que otros han emitido sobre ti, creando resistencia natural a ataques Sybil y manipulación.

**Casos de uso donde los SBTs son especialmente apropiados**:

Las credenciales educativas son el caso de uso más directo. Una universidad emite un SBT a tu dirección certificando tu graduación. Este token permanece vinculado a tu identidad para siempre, verificable instantáneamente por empleadores o programas de postgrado sin necesidad de transcripciones físicas ni llamadas de verificación. La imposibilidad de transferir el SBT garantiza que quien lo posee realmente completó los estudios.

Las membresías en organizaciones se benefician de la no-transferibilidad. Un SBT de membresía en una DAO prestigiosa tiene valor precisamente porque demuestra que tú específicamente fuiste aceptado y participaste activamente, no porque lo compraste en un marketplace. Estos SBTs pueden incluir metadata sobre roles específicos, duración de participación, o contribuciones realizadas.

Las certificaciones profesionales y licencias encuentran representación natural como SBTs. Una certificación AWS, una licencia médica, o un certificado de auditor de smart contracts pueden emitirse como SBTs verificables on-chain, creando portabilidad sin depender de bases de datos centralizadas de cada emisor.

**Recuperación y gestión de Souls**:

Un desafío crítico de los SBTs es la recuperación de identidad cuando pierdes acceso a tu wallet. Si tus credenciales más importantes están vinculadas permanentemente a una dirección cuyas claves privadas perdiste, has perdido efectivamente tu identidad digital completa.

El paper de DeSoc propone mecanismos de recuperación social donde un conjunto de "guardianes" (otras Souls de confianza) pueden aprobar colectivamente la migración de tus SBTs a una nueva dirección. Este modelo se asemeja a la recuperación social implementada en Smart Contract Wallets con Account Abstraction, pero aplicado específicamente a la identidad representada por SBTs.

Otra aproximación es que los emisores mantengan capacidad de re-emitir SBTs a direcciones alternativas previa verificación off-chain de identidad, aunque esto introduce elementos de centralización que algunos consideran contrarios al espíritu de DeSoc.

**SBTs y resistencia a ataques Sybil**:

Una aplicación poderosa de los SBTs es prevenir ataques Sybil en gobernanza y distribuciones de tokens. Crear múltiples direcciones Ethereum es trivial, pero acumular SBTs auténticos emitidos por instituciones diversas a lo largo del tiempo es extremadamente difícil para atacantes.

Un sistema de votación podría requerir que participantes posean cierta combinación de SBTs (educación universitaria + participación en DAOs + historial de contribuciones open source) para calificar, estableciendo barreras que identidades falsas no pueden superar fácilmente. Esto es más robusto que simplemente requerir tenencia de tokens, que puede comprarse, o que pruebas biométricas centralizadas como Worldcoin.

Sin embargo, este enfoque introduce riesgos de exclusión: quienes no tienen acceso a educación formal o participación previa en ecosistemas Web3 quedan excluidos, perpetuando desigualdades existentes. El diseño de sistemas de SBTs debe balancear resistencia a Sybil con inclusividad.

**Advertencia crítica sobre privacidad**:

Es fundamental distinguir entre datos intrínsecamente públicos y datos privados. Los SBTs son excelentes para credenciales públicas (haber asistido a una conferencia, haber votado en una DAO), pero nunca deben utilizarse para información personal sensible (títulos médicos, direcciones físicas, historial crediticio) a menos que utilicen envoltorios de privacidad como Zero-Knowledge Proofs. Emitir un SBT plano con datos personales en una blockchain pública equivale a publicar esos datos en la primera plana de un periódico: es irreversible y visible para siempre.

**Sismo y ZK Badges: privacidad para SBTs**:

Uno de los mayores desafíos de los SBTs públicos es la privacidad: si tu wallet acumula todos tus datos médicos, financieros y sociales públicamente, te conviertes en un libro abierto. Proyectos como [Sismo](https://www.sismo.io/) introdujeron el concepto de ZK Badges (insignias basadas en conocimiento cero) para resolver esto.

Sismo permite a los usuarios agregar sus identidades (conectar su cuenta de Twitter, GitHub y varias wallets de Ethereum) en una bóveda segura (Data Vault) y generar pruebas de conocimiento cero. Con estas pruebas, el usuario puede acuñar un SBT (el Badge) en una dirección nueva y limpia que certifica un hecho (ej. "soy contribuidor de Ethereum" o "tengo un Cryptopunk") sin revelar cuál es la dirección de origen ni vincular públicamente ambas identidades. Esto permite disfrutar de los beneficios de reputación de los SBTs manteniendo la privacidad del historial del usuario.

**Estado actual de adopción**:

A diferencia de las Verifiable Credentials que tienen estándares W3C maduros y múltiples implementaciones, los SBTs están en etapas más tempranas de estandarización y adopción. [ERC-5192](https://eips.ethereum.org/EIPS/eip-5192) define la interfaz básica para tokens no transferibles, pero el ecosistema aún está explorando patrones óptimos de emisión, revocación, y recuperación.

Proyectos como [Nouns DAO](https://nouns.wtf/) experimentan con membresías representadas como SBTs, y plataformas educativas Web3 emiten certificaciones de completación como tokens no transferibles. Sin embargo, la adopción mainstream de SBTs como infraestructura de identidad estándar aún no ha ocurrido, en parte debido a que el concepto es más reciente y los tooling son menos maduros que para sistemas de attestations o Verifiable Credentials.

## Proof of Attendance Protocol (POAP): credenciales de participación

Un componente esencial de la identidad en Web3 es nuestro historial: no solo quiénes somos, sino dónde hemos estado. [Proof of Attendance Protocol (POAP)](https://poap.xyz/) captura esta dimensión emitiendo tokens NFT coleccionables que certifican tu asistencia a eventos físicos o virtuales.

Desde una perspectiva técnica estricta, los POAPs son NFTs estándar (ERC-721) y, por tanto, **son transferibles**. Esto los diferencia de los Soulbound Tokens (SBTs) y de las Attestations de EAS. Sin embargo, en la práctica social, la comunidad los trata "como si fueran" intransferibles: comprar un POAP de un evento al que no fuiste se considera socialmente inútil, ya que la credencial vale por demostrar *tu* vivencia, no tu poder adquisitivo.

Esta tensión entre la "posibilidad técnica de transferir" y la "intención social de no hacerlo" fue precisamente una de las inspiraciones para el desarrollo de los SBTs reales (ERC-5192), que fuerzan esta restricción a nivel de código.

Los POAPs siguen siendo muy populares como una capa más ligera y "gamificada" de identidad (veremos más en la sección de [reputación](7-2-reputation.md)), ideal para comunidades que quieren reconocer la participación de sus miembros sin la rigidez de una certificación académica o un documento de identidad oficial.

## Cuándo usar VCs, Attestation Layer o SBTs

Elegir la herramienta correcta depende de dos factores fundamentales: dónde necesitas que vivan los datos y quién debe tener acceso a verlos. Aunque las tres tecnologías pueden parecer similares, cada una resuelve una necesidad arquitectónica distinta.

Las **Verifiable Credentials (W3C)** son la elección obligada cuando manejas datos privados y sensibles. Su principal ventaja es que priorizan la privacidad del usuario manteniendo los datos off-chain en su dispositivo, no en la blockchain pública. Son ideales para casos como verificar la mayoría de edad mediante ZK-proofs sin revelar la fecha de nacimiento, credenciales educativas que no deseas exponer públicamente, o compliance regulatorio donde necesitas probar atributos ("pasé KYC", "no estoy sancionado") sin revelar identidad completa. El trade-off es una mayor complejidad técnica, ya que requieren wallets específicas para su gestión.

Por otro lado, la **Attestation Layer (como EAS)** es ideal para construir reputación pública y suministrar datos que los Smart Contracts deban leer automáticamente. A diferencia de las VCs, aquí se prioriza la eficiencia y la composabilidad sobre la privacidad. Son perfectas para sistemas de "Credit Scoring" en DeFi donde un protocolo necesita consultar tu historial on-chain instantáneamente y sin intermediarios. La contrapartida es que, por defecto, toda la información es pública.

Finalmente, los **Soulbound Tokens (SBTs)** brillan cuando el objetivo es la visibilidad social y el estatus. Al ser NFTs intransferibles, aparecen visualmente en galerías como OpenSea o Rainbow, lo que los hace perfectos para diplomas universitarios, medallas de gobernanza o certificados de asistencia a eventos. Su función es permitir que el usuario "luzca" el logro en su perfil público. Sin embargo, al igual que las attestations, carecen de privacidad y son más difíciles de actualizar o revocar una vez emitidos.

En resumen: usa VCs para proteger secretos personales, Attestations para alimentar lógica de contratos inteligentes, y SBTs para exhibir logros sociales permanentes.

## Proof of Personhood: demostrando que eres humano único

El "Proof of Personhood" (PoP) no es una tecnología diferente, sino uno de los casos de uso más importantes de la infraestructura de identidad que acabamos de ver. Su objetivo es resolver el problema de la unicidad: ¿cómo demuestra un sistema que una dirección de wallet corresponde a un ser humano único y real, sin depender de un pasaporte gubernamental ni revelar la identidad física del usuario?

Técnicamente, los protocolos de PoP funcionan como emisores de credenciales. Verifican a la persona mediante biometría, análisis social o vídeo, y luego emiten el resultado como una Verifiable Credential (VC) si se prioriza privacidad, o una Attestation si es público. Este mecanismo es la base para la resistencia a ataques Sybil y es fundamental para sistemas de votación cuadrática, renta básica universal o distribuciones justas de tokens.

**Worldcoin y biometría descentralizada**:

[Worldcoin](https://worldcoin.org/) utiliza el escaneo de iris para asegurar la unicidad del usuario. Su innovación principal radica en cómo preserva la privacidad mediante el uso de Zero-Knowledge Proofs. El dispositivo "Orb" genera un código único derivado del iris y lo valida contra una base de datos de hashes ya registrados para asegurar que la persona no existe previamente en el sistema.

Lo crucial es que Worldcoin no revela la biometría cuando se utiliza la identidad en aplicaciones. En su lugar, el World ID funciona como una Verifiable Credential privada. Al interactuar con una aplicación, la wallet genera una prueba matemática que certifica la posesión de una credencial válida emitida por un Orb y que es la primera vez que realiza esa acción, sin revelar qué hash de iris pertenece al usuario ni su identidad real.

La tecnología base consiste en una credencial de identidad y el protocolo Semaphore, un circuito ZK para señalización anónima en Ethereum. El modelo se define como Proof of Uniqueness: una vez verificado físicamente, el usuario opera digitalmente con privacidad total.

Más allá de Worldcoin, el ecosistema explora aproximaciones con reconocimiento facial en dispositivos móviles mediante enclaves seguros, huellas dactilares, análisis de patrones de comportamiento, y combinaciones multi-modal. Sin embargo, hacer biometría privacy-preserving enfrenta desafíos significativos: detectar duplicados sin almacenar templates completos, resolver la revocabilidad cuando un hash biométrico se compromete (no puedes cambiar tu iris como cambiarías una contraseña), y evitar ataques de presentación mediante fotos o videos cuando el hardware de captura no está controlado.

El trilema persiste: maximizar precisión anti-Sybil sacrifica privacidad si se centralizan datos, preservar privacidad mediante procesamiento local aumenta vulnerabilidad a ataques de presentación, o descentralizar infraestructura dificulta coordinar verificaciones de unicidad global. Para implementaciones concretas y análisis detallado del ecosistema, consulta [9-1-ecosystem-DApps](9-1-ecosystem-DApps.md).

**Gitcoin Passport**:

[Gitcoin Passport](https://passport.gitcoin.co/) es un sistema agregador de credenciales verificables diseñado específicamente para resistir [ataques Sybil](https://en.wikipedia.org/wiki/Sybil_attack): situaciones donde una persona crea múltiples identidades falsas para manipular votaciones o reclamar [airdrops](https://www.coinbase.com/es-es/learn/crypto-basics/what-is-a-crypto-airdrop) (distribuciones gratuitas de tokens) repetidamente.

El Passport recopila "stamps" o sellos de diferentes fuentes: verificación de cuenta de Twitter, vinculación con GitHub, posesión de ENS, participación en DAOs, [staking](https://ethereum.org/en/staking/) de ETH (bloquear ETH para asegurar la red y ganar recompensas), verificación mediante BrightID, y muchos más. Estos stamps son credenciales verificables que pueden almacenarse tanto on-chain como off-chain. El diseño actual utiliza principalmente attestations on-chain mediante Ethereum Attestation Service (EAS) en redes L2 como Optimism y Base, lo que permite verificación pública mientras mantiene costos bajos. Cada stamp suma puntos a tu "humanity score", un indicador de cuán probable es que seas un humano único real versus un bot o identidad duplicada.

Los protocolos pueden establecer umbrales de Passport score para participar en votaciones, recibir airdrops o acceder a ciertos beneficios. Lo interesante es que los verificadores ven tu score agregado pero no necesariamente qué stamps específicos posees, preservando cierto grado de privacidad mientras demuestras humanidad.

**Proof of Humanity: registro on-chain público**:

[Proof of Humanity](https://www.proofofhumanity.id/) funciona técnicamente como un Token Curated Registry que vive directamente en un smart contract de Ethereum. Es una lista pública de humanos verificados, por lo que la credencial no es un archivo privado en posesión del usuario, sino su presencia activa en este registro on-chain. Esto constituye una atestación pública permanente. Para ser incluido, el usuario debe subir un video público, depositar una garantía económica (stake) y obtener avales de otros miembros ya registrados.

**BrightID: grafo social off-chain y credenciales**:

[BrightID](https://www.brightid.org/) tiene una arquitectura fundamentalmente diferente, ya que no es una blockchain, sino una red de nodos peer-to-peer que mantienen un grafo social. Técnicamente actúa como un oráculo de unicidad descentralizado.

A diferencia de un registro público, BrightID analiza la estructura de las conexiones sociales para detectar bots. Cuando un usuario es verificado tras participar en videollamadas grupales, la red emite una firma criptográfica que funciona técnicamente como una Verifiable Credential (VC). El usuario presenta esta credencial a las aplicaciones para probar que es único sin revelar quiénes son sus amigos ni exponer su grafo social públicamente. Mientras Proof of Humanity es una lista pública on-chain, BrightID es un generador de pruebas de unicidad off-chain que preserva la privacidad del grafo social.

**El trilema de Proof of Personhood**:

Cada sistema de Proof of Personhood enfrenta un trilema fundamental entre descentralización, privacidad y resistencia Sybil. Esta diversidad de implementaciones permite a los desarrolladores elegir la herramienta adecuada. Si necesitas privacidad absoluta para una votación política, Worldcoin con sus pruebas de conocimiento cero es la opción. Si necesitas filtrar bots en una distribución de tokens sin fricción biométrica, Gitcoin Passport y su sistema de reputación agregada es más adecuado. Cada solución hace compromisos diferentes entre estos tres pilares fundamentales.

## Autenticación estandarizada: Sign-In with Ethereum (SIWE)

Mientras que los DIDs y VCs manejan las credenciales, la industria necesitaba un estándar robusto para algo más básico: ¿cómo demuestro que soy el dueño de esta dirección ante un servidor Web2 tradicional sin enviar una transacción en la blockchain?

La respuesta es [Sign-In with Ethereum (EIP-4361)](https://eips.ethereum.org/EIPS/eip-4361). Antes de SIWE, cada dApp implementaba su propio mecanismo ad-hoc para pedirte que firmaras un mensaje aleatorio para loguearte, lo cual era peligroso (nunca sabías qué estabas firmando realmente y podías ser víctima de phishing).

SIWE estandarizó el formato del mensaje que firma la wallet de manera legible. Cuando ves un mensaje que dice *"wants you to sign in with your Ethereum account"* seguido de la dirección, el dominio del sitio, un nonce (código único) y la fecha, estás usando SIWE. Esto proporciona seguridad robusta ya que el dominio está vinculado criptográficamente en la firma, previniendo ataques de replay y phishing.

Es el puente fundamental de autenticación. Permite que uses tu identidad Ethereum para entrar en foros, chats de Discord, o sitios corporativos, reemplazando el "Login con Google" por un "Login con tu Wallet" que es seguro, estándar y auditado.

## Sistemas de nombres descentralizados

Los sistemas de nombres descentralizados transforman direcciones blockchain incomprensibles en nombres legibles por humanos, creando una capa de identidad esencial para la adopción masiva de Web3.

Es importante no confundir un sistema de nombres como ENS con un DID completo. Mientras que un DID es un estándar técnico para identidad verificable que incluye métodos criptográficos de autenticación, un sistema de nombres es principalmente una capa de usabilidad que facilita la interacción humana. La pregunta natural es: ¿cuándo usar uno u otro?

**Usa un sistema de nombres (como ENS) cuando**:

- Necesitas que otros humanos te envíen pagos o interactúen contigo fácilmente
- Quieres una identidad pública reconocible en el ecosistema blockchain
- Buscas asociar múltiples datos públicos (avatar, redes sociales, direcciones) a un nombre memorable
- Priorizas la simplicidad y la adopción sobre la verificabilidad formal

**Usa un DID cuando**:

- Necesitas probar atributos verificables sobre tu identidad (edad, credenciales educativas, licencias profesionales)
- Requieres interoperabilidad formal entre diferentes sistemas y organizaciones
- Trabajas con casos de uso que demandan estándares de verificación rigurosos
- Necesitas privacidad selectiva mediante Zero-Knowledge Proofs

En la práctica, ambos sistemas son complementarios. Tu nombre ENS puede funcionar como tu identidad pública y fácil de recordar, mientras que tu DID actúa como el sustrato técnico que permite verificar credenciales cuando sea necesario. Un profesional podría usar `maria.eth` para recibir pagos y networking, pero presentar credenciales verificables mediante su DID cuando aplica a un trabajo o accede a servicios que requieren verificación formal de identidad.

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

## Identidad social y grafos soberanos

Mientras los PFPs resuelven la identidad "visual", han surgido protocolos que buscan descentralizar la identidad "relacional": tu grafo social (tus conexiones, seguidores y contenido). En Web2, tu identidad en Twitter o Instagram pertenece a la plataforma; si cierran tu cuenta, pierdes años de construcción social.

Esta nueva capa de identidad se centra en la portabilidad de tus relaciones, permitiendo que tu "yo social" viaje contigo entre aplicaciones.

**Lens Protocol: el perfil como activo raíz**:

[Lens Protocol](https://www.lens.xyz/) materializa este concepto convirtiendo tu perfil en un NFT. A diferencia de un PFP estático, este NFT es dinámico y componible.

**Propiedad del perfil**:

Eres dueño de tu perfil como eres dueño de cualquier otro token en tu wallet. No es una entrada en una base de datos corporativa, es un activo en tu posesión.

**Portabilidad de audiencia**:

Tus seguidores y posts están vinculados a tu dirección, no a una aplicación específica. Si una interfaz te censura o deja de funcionar, puedes usar otra conservando instantáneamente todo tu historial e identidad.

**Grafo social on-chain**:

Cada "follow" se registra mediante NFTs, creando un grafo de conexiones público y verificable que ninguna entidad centralizada puede apagar o manipular.

**Farcaster: identidad federada híbrida**:

[Farcaster](https://www.farcaster.xyz/) aborda el problema con un enfoque ligeramente diferente. Tu identidad principal (un ID numérico llamado FID) se registra en un smart contract en Ethereum (Optimism), garantizando propiedad y unicidad global. Sin embargo, los datos sociales masivos (casts, likes) se almacenan en una red descentralizada de "Hubs" off-chain para máxima eficiencia, manteniendo garantías criptográficas de que cada mensaje fue firmado por tu identidad.

> Para profundizar en cómo funcionan estas redes a nivel de protocolo y aplicación, consulta [Redes Sociales Descentralizadas](9-2-decentralized-social-networks.md).

## Desafío: identidad multicadena

Uno de los desafíos más complejos que enfrentan los usuarios de Web3 es la fragmentación de su identidad a través de múltiples blockchains. A diferencia de Web2, donde tu identidad de Google funciona en todos los servicios del ecosistema, en Web3 cada blockchain opera como un universo separado con sus propias reglas, formatos de direcciones y estándares criptográficos.

**El problema de la fragmentación**:

Un usuario típico de Web3 no vive en una sola blockchain. Puede tener una dirección Ethereum (`0x1234...`) donde guarda sus NFTs y participa en gobernanza de DAOs, una dirección Solana (`AbC123...`) donde hace trading de memecoins por sus bajas fees, una dirección Polygon donde interactúa con juegos blockchain, y quizás direcciones adicionales en Arbitrum, Optimism, Base o Bitcoin. Cada una de estas direcciones es técnicamente una identidad separada e inconexta.

Esta fragmentación genera problemas reales para la construcción de identidad del usuario:

**Reputación dividida**: Tu historial de contribuciones en Ethereum no se transfiere automáticamente a Solana. Si has participado activamente en gobernanza de MakerDAO durante años, acumulado POAPs de eventos importantes, y obtenido credenciales verificables en el ecosistema Ethereum, nada de esto es visible ni relevante cuando intentas unirte a una DAO nativa de Solana. Debes construir tu reputación desde cero en cada ecosistema.

**Credenciales no portables**: Las Verifiable Credentials emitidas como VCs específicas de Ethereum no funcionan directamente en otras chains. Si una universidad te emitió un diploma como VC anclada en Ethereum mediante un DID `did:ethr:0x123`, una dApp en Solana no tiene infraestructura nativa para resolver ese DID ni verificar esa credencial.

**Marca personal fragmentada**: Para creadores de contenido, desarrolladores, o cualquier profesional Web3 que construye su identidad pública, esta fragmentación es especialmente problemática. Un desarrollador puede tener contribuciones significativas distribuidas en GitHub (vinculada a su ENS en Ethereum), arte digital publicado como NFTs en Tezos, y participación en gobernanza de protocolos DeFi en Avalanche. No existe forma natural de presentar un "perfil unificado" que agregue toda esta actividad en una identidad coherente.

**Decisión entre unificación y privacidad**: Algunos usuarios quieren explícitamente mantener identidades separadas por privacidad: su wallet de trading no debe conectarse públicamente con su wallet de participación en DAOs. Otros usuarios necesitan lo contrario: vincular todas sus direcciones para demostrar el alcance completo de su participación y reputación. El ecosistema actual no facilita ninguna de estas dos estrategias de forma nativa.

**Soluciones emergentes desde la perspectiva del usuario**:

Los usuarios han desarrollado diversas estrategias para navegar este desafío multicadena, cada una con sus propios trade-offs:

**Agregación selectiva mediante plataformas de reputación**: Servicios como [DegenScore](https://degenscore.com/) y [Phi.land](https://philand.xyz/) permiten a los usuarios conectar manualmente múltiples wallets de diferentes chains para agregar su actividad on-chain en un único perfil visualizable. El usuario decide qué direcciones vincular públicamente, creando una identidad unificada compuesta. El trade-off es que esta vinculación es pública y permanente: una vez que DegenScore sabe que `0xABC` (Ethereum) y `XyZ789` (Solana) pertenecen al mismo usuario, esa conexión queda expuesta para análisis blockchain.

**Identidad basada en nombres cross-chain**: Sistemas de nombres como [Unstoppable Domains](https://unstoppabledomains.com/) permiten registrar un nombre único (como `alice.crypto`) que resuelve a múltiples direcciones simultáneamente: tu dirección Ethereum, Solana, Polygon, etc. El usuario mantiene una marca personal consistente (`alice.crypto`) mientras técnicamente opera direcciones separadas en cada chain. Cuando alguien te envía fondos a `alice.crypto`, el remitente especifica en qué chain quiere operar y el sistema resuelve a la dirección correcta automáticamente.

**Proof of ownership cross-chain mediante firmas**: Para casos donde necesitas demostrar que controlas direcciones en múltiples chains sin vincularlas públicamente on-chain, puedes generar firmas criptográficas desde cada dirección certificando que todas pertenecen a la misma entidad. Por ejemplo, firmas desde tu wallet Ethereum, Solana y Polygon el mismo mensaje único, demostrando control sobre las tres. Estas firmas se presentan off-chain a verificadores específicos (como un empleador o una DAO evaluando tu membresía) sin publicarlas globalmente. Esto preserva privacidad mientras pruebas propiedad cuando es necesario.

**Smart Contract Wallets con Account Abstraction**: Wallets basadas en smart contracts como [Safe](https://safe.global/) (anteriormente Gnosis Safe) permiten desplegar la misma dirección de smart contract en múltiples chains compatibles con EVM mediante [CREATE2](https://eips.ethereum.org/EIPS/eip-1014), resultando en la misma dirección (misma secuencia hexadecimal) funcionando en Ethereum, Polygon, Arbitrum, Optimism, etc. Esto unifica tu identidad técnica a través de chains compatibles: tu reputación, credenciales y actividad asociada a esa dirección específica funciona consistentemente en todos esos ecosistemas. El trade-off es que esto solo funciona entre chains compatibles con EVM; Solana, Bitcoin, y otros ecosistemas no-EVM quedan excluidos.

**Protocolos de identidad cross-chain nativos**: Proyectos como [Ceramic Network](https://ceramic.network/) construyen infraestructura específicamente diseñada para identidad que trascienda blockchains individuales. Ceramic permite crear un DID único (usando el método `did:pkh` que soporta múltiples chains) y almacenar datos de identidad (perfil, credenciales, grafo social) en una red descentralizada independiente de cualquier blockchain específica. Las dApps en cualquier chain pueden consultar esta identidad universal. El usuario firma desde cualquiera de sus wallets para probar control sobre ese DID multicadena.

**La estrategia del "perfil puente"**: Muchos usuarios profesionales mantienen un "perfil puente" público donde declaran explícitamente la conexión entre sus identidades. Por ejemplo, configuran su ENS en Ethereum para incluir metadata que referencia su dirección Solana, mientras simultáneamente su perfil Solana incluye un link a su ENS. Esto es esencialmente documentación social verificable: cualquiera puede verificar ambas direcciones y ver las referencias cruzadas consistentes, construyendo confianza de que pertenecen a la misma persona sin necesidad de infraestructura técnica compleja.

**Realidad pragmática**:

La identidad multicadena permanece como uno de los problemas abiertos más significativos en Web3. No existe una solución estándar que resuelva todos los casos de uso, y los usuarios deben elegir estrategias basadas en sus necesidades específicas de privacidad, portabilidad de reputación, y complejidad técnica que están dispuestos a manejar.

Para usuarios que priorizan privacidad extrema, mantener identidades completamente separadas por blockchain sigue siendo la opción más segura. Para profesionales que construyen marca personal, invertir en agregación pública mediante plataformas de reputación o nombres cross-chain ofrece mayor visibilidad a costa de privacidad. Para desarrolladores de aplicaciones, elegir si construir mono-chain (simplicidad técnica) o multi-chain (mayor alcance de usuarios) sigue siendo un trade-off fundamental.

## Reputación on-chain y verificabilidad

La identidad descentralizada proporciona los cimientos técnicos (DIDs, VCs, attestations), pero es la reputación la que aporta valor y contexto a esa identidad. Mientras que tu DID demuestra que controlas una identidad, tu reputación on-chain evidencia lo que has hecho con ella: cada transacción, voto en gobernanza, contribución a protocolos o evento al que asistes queda registrado de forma permanente en la blockchain como un historial verificable e inmutable.

Esta reputación, construida a partir de acciones verificables, se convierte en capital social que no puede falsificarse ni comprarse fácilmente. Los sistemas de reputación en Web3 emplean mecanismos como POAPs (proof of attendance), Soulbound Tokens (credenciales no transferibles), agregadores de actividad on-chain y algoritmos avanzados que previenen ataques Sybil y manipulación del sistema.

Para un análisis completo sobre cómo se construye, mide y utiliza la reputación en Web3—including infraestructura técnica (EAS, Ceramic, The Graph), modelos de agregación (contextual, basado en grafos, múltiples fuentes), casos de uso en gobernanza DAO y DeFi, y desafíos como la resistencia a Sybil attacks y la privacidad—consulta [Reputación Web3](7-2-reputation.md).

## Wallets y experiencia de usuario

Hablar de identidad Web3 implica comprender la evolución de las wallets blockchain: desde las cuentas simples controladas por claves privadas hasta las sofisticadas Smart Contract Wallets con Account Abstraction, gas sponsorship, firmas flexibles, session keys, límites personalizados e identidad multichain. Sin embargo, estos temas se abordan en detalle en [experiencia de usuario](./8-1-user-experience.md).

Aun así, es importante destacar que el smartphone, que se ha consolidado como el elemento clave de seguridad y nodo central de la identidad soberana (SSI) en el contexto de la seguridad multifactor (MFA), actuando como ancla de la identidad descentralizada bajo el principio de "algo que tengo". Este factor es considerado más seguro que otros como "algo que sé" o "algo que soy".

En su arquitectura, el móvil permite desde biometría local hasta, en algunos casos según la gama del dispositivo, el uso de módulos seguros como TEE o HSM.

En estos casos se usa el estándar de facto para la comunicación peer-to-peer desde la aplicación, ques es [WalletConnect](https://walletconnect.com/), que permite una conexión segura.

### Passkeys (WebAuthn): el fin de la contraseña

La evolución más significativa en la accesibilidad de la identidad Web3 ha sido la adopción masiva de [Passkeys](https://fidoalliance.org/passkeys/), basadas en el estándar [WebAuthn/FIDO2](https://webauthn.io/). Los Passkeys permiten a los usuarios crear y acceder a sus wallets utilizando la biometría nativa de sus dispositivos (FaceID, TouchID, Windows Hello) en lugar de gestionar complejas seed phrases o contraseñas vulnerables.

Esta tecnología elimina el punto de fallo más común en la auto-custodia: el error humano al guardar las claves. Al vincular criptográficamente la identidad a un enclave seguro de hardware en el dispositivo del usuario, se logra un nivel de seguridad phishing-resistant. Los principales proveedores de smart contract wallets ya integran Passkeys como método principal de autenticación, creando una experiencia de usuario indistinguible de las aplicaciones fintech modernas pero manteniendo la soberanía de los fondos.

### El Smartphone como "Identity Hub" Universal

El smartphone se ha convertido en el ancla física de la identidad descentralizada porque resuelve tres problemas simultáneamente: portabilidad (siempre lo llevas), seguridad (hardware especializado como TEE/HSM protege las claves incluso si el sistema se compromete), y usabilidad (biometría y notificaciones push permiten autenticación instantánea).

Esta combinación única permite que el móvil actúe como hub centralizado de tu identidad descentralizada: gestiona múltiples direcciones blockchain desde el mismo entorno seguro, se conecta a aplicaciones de escritorio mediante WalletConnect sin exponer tus claves, almacena credenciales verificables localmente que presentas selectivamente usando ZK-proofs, y delega permisos temporales mediante session keys para aplicaciones que requieren interacción continua sin confirmaciones constantes.

El concepto clave es que el smartphone separa tres responsabilidades: custodia de claves (siempre en el dispositivo), presentación de credenciales (selectiva según contexto), y autorización de acciones (delegable cuando es seguro hacerlo). Esta arquitectura convierte al móvil en el punto de confianza desde el cual interactúas con todo el ecosistema Web3, manteniendo control mientras permites experiencias fluidas.

## Identidad de organizaciones descentralizadas

Mientras que gran parte de la discusión sobre identidad descentralizada se centra en individuos, las organizaciones autónomas descentralizadas también necesitan identidades verificables y estandarizadas. Las DAOs operan mediante smart contracts, pero estos contratos por sí solos no proporcionan información legible sobre qué representa la organización, quiénes son sus miembros, o cómo funciona su gobernanza.

**ERC-4824: metadatos estandarizados para DAOs**:

[ERC-4824](https://eips.ethereum.org/EIPS/eip-4824) es un estándar de Ethereum que define una interfaz común para que las DAOs publiquen sus metadatos de forma estandarizada. El estándar especifica que un contrato de DAO debe implementar una función `daoURI()` que devuelve una URI apuntando a un documento JSON con información estructurada sobre la organización.

Este documento JSON contiene campos como el nombre de la DAO, descripción, enlaces a propuestas de gobernanza, información sobre contratos asociados, y otros metadatos relevantes. El formato estandarizado permite que exploradores de blockchain, interfaces de gobernanza y herramientas de análisis muestren información consistente sobre cualquier DAO sin necesidad de integraciones personalizadas para cada organización.

La importancia de ERC-4824 radica en crear interoperabilidad entre ecosistemas de DAOs. Una plataforma de análisis puede descubrir y presentar información sobre miles de DAOs diferentes simplemente consultando esta interfaz estándar. Los agregadores de gobernanza pueden mostrar propuestas activas de múltiples organizaciones en un solo lugar. Los sistemas de reputación pueden vincular la participación de individuos en diversas DAOs de forma coherente.

**DIDs organizacionales y credenciales colectivas**:

Más allá de los metadatos, las DAOs requieren identidades verificables para interactuar con el mundo legal y digital. Una DAO puede tener un DID organizacional que controla colectivamente mediante su mecanismo de gobernanza. A diferencia de un DID individual controlado por una clave privada, un DID de DAO requiere que las acciones sean aprobadas mediante votación o consenso de sus miembros según las reglas establecidas en sus smart contracts.

Este DID organizacional puede poseer credenciales verificables como registro legal en ciertas jurisdicciones, acuerdos con proveedores, certificaciones de compliance, o membresía en asociaciones industriales. Los smart contracts de la DAO actúan como la "wallet" organizacional: cuando una decisión de gobernanza es aprobada, el contrato puede firmar documentos legales o credenciales en nombre de la organización.

Por ejemplo, una DAO registrada legalmente como entidad en Wyoming puede obtener una credencial verificable emitida por el estado confirmando su existencia legal. Esta credencial permitiría a la DAO abrir cuentas bancarias, firmar contratos, o cumplir requisitos regulatorios mientras mantiene gobernanza descentralizada on-chain. El puente entre identidad digital descentralizada e identidad legal tradicional es crucial para que las DAOs operen efectivamente en contextos que requieren compliance.

**Attestations de membresía y roles**:

Las organizaciones también necesitan emitir credenciales sobre sus miembros. Utilizando servicios de Attestation Layer (explicado anteriormente en la sección de attestations on-chain), las DAOs pueden emitir attestations verificables que confirman membresía, roles específicos, contribuciones realizadas, o permisos delegados.

Estas attestations organizacionales funcionan como credenciales laborales descentralizadas. Si contribuiste significativamente a una DAO conocida, esa organización puede emitir una attestation que otros empleadores o DAOs pueden verificar criptográficamente. Tu reputación profesional se vuelve portátil y verificable sin depender de cartas de recomendación tradicionales o llamadas de verificación de empleo.

Para detalles sobre cómo las organizaciones implementan estos sistemas de attestations como parte de su arquitectura de roles y permisos, consulta [Roles y Control de Acceso](7-5-roles-access-control.md).

## Oráculos de identidad: conectando mundos off-chain y on-chain

Aunque [Chainlink](https://chain.link/) es conocido principalmente por proporcionar feeds de precios y datos del mundo real a smart contracts, también juega un papel emergente en infraestructura de identidad descentralizada mediante oráculos de identidad.

El desafío fundamental es conectar identidades y credenciales del mundo off-chain (licencias de conducir gubernamentales, historiales crediticios, diplomas universitarios físicos) con aplicaciones on-chain que necesitan verificar estos atributos. Los smart contracts no pueden acceder directamente a bases de datos externas ni APIs de verificación, requiriendo oráculos que actúen como puentes confiables.

Los oráculos de Chainlink facilitan verificación de identidad mediante varios mecanismos. Primero, consultan servicios de verificación tradicionales (bureaus de crédito, bases de datos gubernamentales, sistemas universitarios) y reportan resultados verificables on-chain. Un smart contract puede solicitar verificación de que un usuario cumple ciertos criterios (mayor de edad, residente de jurisdicción permitida, sin antecedentes penales) y el oráculo devuelve una attestation firmada.

Segundo, Chainlink permite implementar KYC descentralizado con preservación de privacidad. Un proveedor KYC off-chain verifica la identidad de un usuario según estándares regulatorios, luego el oráculo genera una credencial on-chain que simplemente indica "este usuario pasó KYC nivel X" sin revelar datos personales específicos. El smart contract puede requerir esta credencial para permitir acceso a servicios regulados sin que los datos sensibles toquen blockchain.

Tercero, los oráculos pueden agregar múltiples fuentes de verificación para crear scores de reputación o confianza más robustos. En lugar de depender de una sola fuente de verdad, el oráculo consulta múltiples proveedores de datos de identidad (credit bureaus, verificadores biométricos, registros públicos) y calcula un score agregado, reduciendo el riesgo de dependencia en un punto único de fallo.

Chainlink Labs ha desarrollado [DECO](https://www.deco.works/), un proyecto de investigación experimental que explora protocolos de oráculos con preservación de privacidad. DECO investiga cómo permitir que un oráculo pueda probar criptográficamente que cierta información existe en una fuente externa (como un sitio web HTTPS) sin revelar la información completa ni requerir que la fuente modifique su infraestructura. La visión es que podrías probar atributos como que tu balance bancario excede cierto umbral sin revelar el balance exacto ni permitir que el oráculo vea tus datos bancarios completos. Sin embargo, DECO permanece en fase de investigación y desarrollo, sin implementaciones en producción mainstream. Las soluciones actuales de oráculos de identidad utilizan enfoques más tradicionales de attestations y agregación de datos de múltiples fuentes.

La integración de Chainlink con sistemas de identidad también habilita interoperabilidad entre cadenas. Una credencial verificable emitida en Ethereum puede ser validada y utilizada en Polygon, Avalanche, o cualquier otra cadena mediante Cross-Chain Interoperability Protocol (CCIP) de Chainlink, permitiendo que tu identidad descentralizada sea verdaderamente multi-chain sin necesidad de re-verificación en cada ecosistema.

Los casos de uso incluyen lending protocols que verifican credit scores sin exponerlos públicamente, DEXs que cumplen requisitos de sanctions screening consultando listas off-chain mediante oráculos, insurance protocols que verifican historial de reclamaciones, y gaming platforms que confirman edad sin KYC invasivo.

Sin embargo, el uso de oráculos introduce trade-offs. Aunque Chainlink usa redes descentralizadas de nodos para minimizar confianza, cualquier sistema que depende de datos off-chain inherentemente confía en que esos datos son correctos y que los oráculos reportan honestamente. La descentralización de la red de oráculos mitiga esto, pero no lo elimina completamente. Por eso, los oráculos de identidad son más apropiados para verificación de atributos públicos o semi-públicos donde múltiples fuentes pueden ser consultadas y comparadas, en lugar de secretos críticos que no deben filtrarse bajo ninguna circunstancia.

## zkTLS y Web Proofs: trayendo tu historial de Web2

Una de las limitaciones históricas de la identidad Web3 ha sido la dificultad para importar la reputación que ya has construido en el mundo tradicional. Tienes años de historial en Uber, un saldo bancario que demuestra solvencia, o una cuenta de Steam con miles de horas de juego. Tradicionalmente, la única forma de traer estos datos a la blockchain era mediante oráculos centralizados o APIs corporativas (OAuth) que requerían permiso de las empresas.

La tecnología de zkTLS (Zero-Knowledge Transport Layer Security), también conocida como Web Proofs, ha roto esta barrera permitiendo a los usuarios generar pruebas de sus datos Web2 de forma soberana y sin permiso (permissionless).

El concepto se basa en que casi toda la web segura utiliza el protocolo TLS (el candado verde en tu navegador) para garantizar que los datos vienen realmente del servidor del banco o la red social. zkTLS permite que tu navegador genere una prueba criptográfica de que "recibió una respuesta del servidor X conteniendo el dato Y", sin revelar tu contraseña ni las cookies de sesión al verificador.

Protocolos como [Reclaim Protocol](https://www.reclaimprotocol.org/) o [TLSNotary](https://tlsnotary.org/) implementan esta tecnología. Esto permite casos de uso revolucionarios: una dApp puede verificar que tienes más de 100 seguidores en Twitter o que has completado un curso en una plataforma de e-learning cerrada, simplemente pidiéndote que te loguees en esos sitios en tu propio navegador. Tú generas la prueba localmente y la dApp la verifica, sin que la plataforma Web2 sepa siquiera que está ocurriendo la verificación. Es el puente definitivo para la identidad soberana: tus datos de la Web2 te pertenecen y puedes usarlos donde quieras.

## Ejemplos prácticos

Para asentar todos los conceptos técnicos vistos, veamos cuatro flujos de uso reales que demuestran cómo estas tecnologías (VCs, SBTs, Attestations) resuelven problemas cotidianos en Web3.

**Caso 1: DeFi Institucional y Privacidad (Privado ID)**:

El problema habitual es que un usuario quiere depositar USDC en un pool de "Activos del Mundo Real" (RWA) en protocolos como Aave o Goldfinch. Por normativas legales, el protocolo debe verificar que el usuario no está en una lista de sanciones internacionales (KYC), pero el usuario legítimamente no quiere que su pasaporte, nombre real y dirección física queden expuestos públicamente en la blockchain para siempre.

La solución se implementa mediante Verifiable Credentials (VC) y tecnología Zero-Knowledge. El proceso comienza cuando el usuario completa un KYC tradicional con un proveedor de confianza fuera de la cadena. Este proveedor emite una VC al wallet móvil del usuario (como [Privado ID wallet](https://www.privadoid.com/)) que certifica atributos como "KYC Aprobado" o "Residente en España", sin guardar estos datos en la cadena.

Para realizar el depósito, el usuario conecta su wallet al protocolo DeFi. En lugar de entregar la credencial, su dispositivo genera una Zero-Knowledge Proof, una prueba criptográfica que demuestra matemáticamente que posee la credencial válida de "No sancionado" sin revelar el contenido de la misma. El smart contract verifica esta prueba y permite la transacción. El resultado final es que el protocolo cumple con la regulación estricta mientras la privacidad del usuario permanece intacta, ya que ningún observador de la blockchain puede vincular la dirección con una identidad real.

**Caso 2: Financiación Pública y Resistencia a Sybil (Gitcoin Passport)**:

Las Organizaciones Autónomas Descentralizadas (DAOs) enfrentan constantemente el desafío de distribuir fondos (Grants) de manera justa. Si utilizan mecanismos como votación cuadrática, necesitan evitar que una sola persona cree cientos de cuentas falsas (ataque Sybil) para inflar artificialmente el apoyo a sus propios proyectos y drenar los fondos comunitarios.

[Gitcoin Passport](https://passport.gitcoin.co/) soluciona esto agregando múltiples capas de verificación mediante la Attestation Layer. El usuario conecta su wallet y verifica diversas cuentas y posesiones: conecta su perfil de Twitter y Google, demuestra antigüedad en Ethereum, o prueba la titularidad de un dominio ENS. Cada una de estas verificaciones genera un "stamp" o attestation (gestionada frecuentemente a través de [EAS](https://attest.sh/)) que sirve como evidencia de legitimidad.

El sistema utiliza un algoritmo para agregar todas estas atestaciones y calcular un "Humanity Score" o puntuación de humanidad. Si el score del usuario supera cierto umbral establecido por la DAO, se asume que es un humano único y se permite su voto con el poder de emparejamiento completo. Así, la identidad se construye no por un documento único, sino por la composición de múltiples evidencias verificables difíciles de falsificar en masa.

**Caso 3: Reputación Social sin perder Privacidad (Sismo)**:

Imagina un usuario que es un "whale" (poseedor de grandes capitales) y tiene un CryptoPunk guardado en una hardware wallet de alta seguridad (bóveda fría) que nunca conecta a aplicaciones web por precaución. Este usuario desea ingresar a un grupo exclusivo de Telegram o Discord reservado para holders de Punks, pero hacerlo requeriría firmar con su bóveda fría, exponiendo su dirección y arriesgando su seguridad.

Proyectos como [Sismo](https://www.sismo.io/) resuelven esta paradoja utilizando Soulbound Tokens (SBTs) y privacidad. El usuario utiliza el Data Vault de Sismo para importar su bóveda fría de manera privada. Luego, genera una prueba de conocimiento cero que certifica "El propietario de este Data Vault posee un CryptoPunk", sin revelar cuál es la dirección específica de la bóveda.

Con esta prueba, el usuario puede acuñar un Badge (insignia) en forma de SBT en una wallet diferente, una wallet caliente de uso diario. Finalmente, utiliza esta wallet secundaria con el SBT para autenticarse en el chat exclusivo. De esta forma, demuestra su estatus y reputación portándolos a una identidad nueva y segura, manteniendo sus activos principales completamente aislados del riesgo.

**Caso 4: La experiencia de usuario base (ENS + SIWE)**:

El obstáculo más común para los nuevos usuarios es la complejidad de las direcciones criptográficas (`0x...`) y la inseguridad de gestionar múltiples contraseñas para diferentes servicios. Web3 propone unificar esto en una experiencia fluida donde la identidad viaja con el usuario.

La solución integra [ENS](https://ens.domains/) y [Sign-In With Ethereum](https://login.xyz/). Primero, el usuario registra un nombre legible como `mi-nombre.eth` y configura en él su avatar y perfiles sociales. Luego, al visitar una red social descentralizada o un marketplace, utiliza su wallet para iniciar sesión firmando un mensaje criptográfico.

La aplicación reconoce inmediatamente al usuario, saludándolo como "Mi Nombre" y mostrando su avatar personalizado, sin que haya sido necesario crear una cuenta nueva ni establecer una contraseña. La identidad es propiedad del usuario y se proyecta automáticamente en cualquier aplicación compatible, eliminando la fricción de registros repetitivos y mejorando la seguridad general.

**Caso 5: Historial verificado de eventos (POAP)**:

En el mundo profesional tradicional, demostrar la asistencia a conferencias o la participación en eventos clave depende de diplomas en papel o declaraciones de confianza en un CV que nadie verifica. Esto genera un vacío para demostrar el "estar ahí" o la participación activa en una comunidad.

[POAP (Proof of Attendance Protocol)](https://poap.xyz/) transforma esta experiencia mediante coleccionables digitales. Al asistir a un evento, el usuario escanea un código QR único o reclama un token mediante su wallet. Este token NFT queda registrado en su historial con metadatos verificables del evento (fecha, lugar, diseño).

Con el tiempo, la wallet del usuario se convierte en un pasaporte visual de sus vivencias. Un reclutador o una comunidad pueden verificar instantáneamente que el usuario realmente asistió a los hackathons, cursos o conferencias que afirma, sin necesidad de contactar a los organizadores. La reputación se construye sobre pruebas criptográficas de presencia real.

**Caso 6: Portabilidad de la identidad social (Lens Protocol)**:

El problema central de las redes sociales actuales ("Web2") es el encierro: si un creador de contenido con 100,000 seguidores en una plataforma es baneado o decide mudarse, pierde toda su audiencia y contenido; debe empezar de cero. Su grafo social pertenece a la empresa, no a él.

Protocolos de identidad social como [Lens](https://www.lens.xyz/) invierten este modelo. El perfil del usuario y sus relaciones (a quién sigue) se almacenan como NFTs en la blockchain, bajo su custodia directa. Si el usuario no está satisfecho con la aplicación de interfaz que utiliza, puede cambiar a otra aplicación diferente (por ejemplo, de Hey a Orb) simplemente conectando su wallet.

El resultado es que sus 100,000 seguidores, sus publicaciones y su reputación aparecen instantáneamente en la nueva plataforma. La identidad social es soberana y portable, obligando a las aplicaciones a competir por ofrecer la mejor experiencia de usuario en lugar de monopolizar los datos para retener a la audiencia.

## Almacenamiento de datos de identidad: Ceramic y DWNs

Mientras que las blockchains almacenan el estado financiero global e IPFS almacena archivos estáticos inmutables, la identidad digital requiere algo diferente: datos dinámicos que evolucionan con el tiempo. Nuestra identidad no es estática; cambiamos de trabajo, actualizamos nuestras fotos de perfil y acumulamos nueva reputación constantemente.

Para gestionar estos datos mutables, el ecosistema se apoya en dos tecnologías fundamentales que actúan como la "memoria" descentralizada de la identidad: Ceramic Network y los Decentralized Web Nodes (DWNs).

### Ceramic Network

[Ceramic](https://ceramic.network/) actúa como una red de datos descentralizada para información mutable basada en streams. Su papel es fundamental para dar viabilidad práctica a los sistemas de Verifiable Credentials (VCs).

**Almacenamiento eficiente**: Guardar credenciales complejas directamente en Ethereum es prohibitivamente costoso. Ceramic permite almacenar estos documentos JSON ricos "off-chain" en una red descentralizada, manteniendo la verificabilidad.

**Propiedad por DID**: Los datos se organizan en "streams" donde cada uno es propiedad de un DID. Solo el usuario que controla la clave privada puede firmar actualizaciones.

**Composabilidad**: Los datos en Ceramic son interoperables y públicos por defecto (aunque pueden encriptarse), permitiendo que múltiples dApps lean el mismo perfil o grafo social del usuario, rompiendo los silos de datos.

### Decentralized Web Nodes (DWNs)

El estándar de [Decentralized Web Nodes (DWNs)](https://identity.foundation/decentralized-web-node/spec/), impulsado principalmente por [TBD](https://www.tbd.website/) y la Decentralized Identity Foundation, ofrece una aproximación alternativa enfocada en la privacidad y la soberanía personal total.

Un DWN es un almacén de datos personales que pertenece exclusivamente al usuario (como un "servidor personal" pero estandarizado). A diferencia de una red global pública como Ceramic, los DWNs están diseñados para ser privados por defecto. Un usuario puede tener múltiples réplicas de su DWN (en su teléfono, en su laptop, y en un servicio en la nube encriptado) que se sincronizan automáticamente.

Las aplicaciones piden permiso para escribir o leer datos específicos en el DWN del usuario. Es la arquitectura base de lo que algunos denominan **Web5**: una web donde las aplicaciones no tienen base de datos propia de usuarios, sino que actúan como interfaces que interactúan con el DWN soberano de cada persona.

Ambas tecnologías complementan a la blockchain (notario/juez) y a la wallet (llavero), proporcionando el archivador dinámico necesario para una identidad digital completa.

## Consideraciones y desafíos

A pesar del progreso significativo, la identidad descentralizada enfrenta desafíos importantes que limitan su adopción masiva.

El problema de usabilidad ha mejorado pero persiste. Aunque wallets como MetaMask han introducido mecanismos de recuperación de seed phrase y Account Abstraction está ganando tracción, gestionar claves privadas sigue siendo complejo para usuarios no técnicos. La recuperación social y las smart contract wallets añaden capas de seguridad, pero también introducen nuevos conceptos que los usuarios deben comprender.

La privacidad presenta dilemas fundamentales. La transparencia de blockchain permite reputación verificable, pero toda la actividad financiera on-chain es públicamente visible por diseño. Soluciones como Privado ID permiten probar atributos mediante Zero-Knowledge Proofs sin revelar datos subyacentes, lo cual funciona bien para credenciales verificables off-chain (edad, nacionalidad, titulaciones). Sin embargo, para actividad financiera on-chain no existe privacidad por defecto: cada transacción, balance y participación en protocolos DeFi queda registrada públicamente. Aunque mixing services y privacy coins existen, introducen fricciones de usabilidad y riesgos regulatorios significativos.

La interoperabilidad entre sistemas de identidad sigue siendo limitada pese a los avances. Tu identidad ENS funciona principalmente en Ethereum y algunos L2s, mientras que redes sociales descentralizadas como Lens Protocol o Farcaster, aunque han evolucionado significativamente en 2025-2026 con adopción creciente, operan en sus propios ecosistemas con portabilidad parcial. Diferentes métodos DID usan diferentes mecanismos de resolución. Los estándares W3C proporcionan un marco común, pero la fragmentación práctica persiste porque cada ecosistema optimiza para sus necesidades específicas.

Finalmente, existe una tensión fundamental entre descentralización y conveniencia. Los servicios centralizados como Google SSO son convenientes precisamente porque un solo proveedor maneja todo. La descentralización distribuye control pero también distribuye complejidad. Encontrar el balance correcto es el desafío de diseño central de Web3: suficiente descentralización para preservar autonomía, pero suficiente abstracción de complejidad para permitir adopción masiva.


### Consideraciones y desafíos

A pesar del progreso significativo, la identidad descentralizada enfrenta desafíos importantes que limitan su adopción masiva, con una contradicción filosófica fundamental: ¿debe Web3 abstraer su complejidad hasta parecerse a Web2, o hacerlo traiciona sus principios fundacionales?

**La paradoja de usabilidad: Account Abstraction y Smart Contract Wallets**:

El problema de usabilidad ha mejorado significativamente. Wallets como MetaMask han introducido mecanismos de recuperación de seed phrase, y tecnologías como [Account Abstraction (ERC-4337)](https://eips.ethereum.org/EIPS/eip-4337) y Smart Contract Wallets como [Safe](https://safe.global/) prometen eliminar completamente la gestión manual de claves privadas. Puedes recuperar tu cuenta mediante guardianes sociales, usar autenticación biométrica, o pagar gas fees con tokens arbitrarios. Técnicamente, esto resuelve la usabilidad: tu wallet funciona como cualquier aplicación Web2, con recuperación de contraseña y experiencia familiar.

Pero aquí surge la tensión conceptual profunda: si tu identidad Web3 depende de DIDs y Verifiable Credentials vinculados criptográficamente a claves específicas, y ahora esas claves son gestionadas por smart contracts que pueden modificarse, actualizarse o recuperarse mediante mecanismos sociales, ¿dónde queda la inmutabilidad criptográfica que fundamenta la confianza descentralizada? Un DID vinculado a una dirección EOA (Externally Owned Account) tradicional tiene garantías matemáticas absolutas: solo quien posee la clave privada puede firmar. Un DID vinculado a una Smart Contract Wallet introduce lógica mutable: las reglas de quién puede firmar pueden cambiar según la gobernanza del contrato.

Las implementaciones actuales como [did:ethr con Account Abstraction](https://github.com/decentralized-identity/ethr-did-resolver) permiten asociar DIDs a smart contracts, especificando múltiples métodos de verificación con diferentes niveles de autoridad: claves maestras para operaciones críticas (rotación de claves, actualización de DID Document) y claves delegadas de menor privilegio para operaciones cotidianas que pueden revocarse sin comprometer la identidad raíz. Sin embargo, esto introduce complejidad que el usuario promedio no comprende: ¿qué clave está firmando esta Verifiable Presentation? ¿Puede alguno de mis guardianes sociales revocar mis credenciales? La recuperación social y las smart contract wallets añaden capas de seguridad, pero erosionan las garantías criptográficas puras que fundamentan la confianza descentralizada.

**La custodia distribuida de credenciales**:

Las Verifiable Credentials supuestamente viven en tu dispositivo bajo tu control exclusivo. Pero si pierdes acceso a tu wallet mediante Account Abstraction, ¿quién custodia realmente tus VCs? La recuperación social implica que un conjunto de guardianes puede restaurar acceso, pero las VCs como archivos JSON no están en la blockchain, están en tu storage local. Proyectos como [Ceramic Network](https://ceramic.network/) implementan almacenamiento descentralizado de credenciales donde tus VCs se sincronizan cifradas en una red distribuida, accesibles solo con tus credenciales de recuperación. Esto funciona, pero ahora dependes de infraestructura de red descentralizada persistente, no solo de blockchain.

La pregunta filosófica es: ¿sigue siendo Self-Sovereign Identity si tu recuperación depende de terceros (guardianes sociales) y tu almacenamiento de credenciales depende de redes distribuidas externas? La respuesta técnica es que sí, porque tú controlas los permisos, pero la realidad práctica es más matizada. La soberanía absoluta requiere competencia técnica que la mayoría de usuarios no posee. Las abstracciones necesarias para usabilidad masiva introducen dependencias que erosionan parcialmente esa soberanía.

**Privacidad y transparencia: dilemas irreconciliados**:

La privacidad presenta dilemas fundamentales. La transparencia de blockchain permite reputación verificable, pero toda la actividad financiera on-chain es públicamente visible por diseño. Actualmente conviven dos modelos de identidad Web3 incompatibles: tu identidad financiera on-chain (direcciones Ethereum, actividad DeFi) es pseudónima pero completamente transparente, mientras que tu identidad basada en VCs y DIDs promete privacidad selectiva mediante Zero-Knowledge Proofs.

Soluciones como Privado ID permiten probar atributos mediante Zero-Knowledge Proofs sin revelar datos subyacentes, lo cual funciona bien para credenciales verificables off-chain (edad, nacionalidad, titulaciones). Sin embargo, cuando usas una dApp DeFi, tu wallet firma transacciones con tu dirección pública, exponiendo tu actividad financiera. Aunque presentes una Verifiable Credential que prueba "tengo más de 18 años" sin revelar tu fecha de nacimiento, tu dirección Ethereum sigue siendo rastreable. La privacidad de VCs opera principalmente off-chain para autenticación y autorización, no para actividad financiera on-chain.

Soluciones de privacidad on-chain como [Aztec Network](https://aztec.network/) o [Railgun](https://www.railgun.org/) intentan resolver esto con transacciones privadas mediante ZK-proofs, pero introducen fricciones significativas: pools de liquidez separados, interoperabilidad limitada con protocolos existentes, y escrutinio regulatorio intenso. Aunque mixing services y privacy coins existen, introducen fricciones de usabilidad y riesgos regulatorios significativos. La mayoría de usuarios continúa operando con transparencia total porque la privacidad on-chain sacrifica composabilidad y conveniencia.

**Fragmentación e interoperabilidad limitada**:

La interoperabilidad entre sistemas de identidad sigue siendo limitada pese a los avances. Tu identidad ENS funciona principalmente en Ethereum y algunos L2s, mientras que redes sociales descentralizadas como Lens Protocol o Farcaster, aunque han evolucionado significativamente en 2025-2026 con adopción creciente, operan en sus propios ecosistemas con portabilidad parcial. Diferentes métodos DID usan diferentes mecanismos de resolución. Los estándares W3C proporcionan un marco común, pero la fragmentación práctica persiste porque cada ecosistema optimiza para sus necesidades específicas.

**El trilemma de identidad Web3**:

Web3 enfrenta un trilemma análogo al blockchain trilemma pero aplicado a identidad: usabilidad, privacidad y descentralización son difíciles de maximizar simultáneamente. Puedes tener dos, pero no las tres sin compromisos severos.

Si priorizas descentralización y privacidad (DIDs con pairwise ephemeral identifiers, almacenamiento local de VCs, Zero-Knowledge Proofs para todo), sacrificas usabilidad: usuarios deben gestionar claves, comprender conceptos criptográficos complejos, y aceptar que perder acceso significa perder identidad permanentemente. Si priorizas usabilidad y descentralización (Account Abstraction con recuperación social, UX simplificada), introduces vectores de confianza social que erosionan garantías criptográficas puras. Si priorizas usabilidad y privacidad (servicios custodiales con ZK-proofs), reintroduces centralización donde el custodio tiene poder significativo sobre tu identidad.

**¿Qué busca realmente Web3?**:

Existe una tensión fundamental entre descentralización y conveniencia. Los servicios centralizados como Google SSO son convenientes precisamente porque un solo proveedor maneja todo. La descentralización distribuye control pero también distribuye complejidad. La respuesta sobre qué busca Web3 no es única porque el ecosistema está fragmentado entre puristas que priorizan descentralización sobre todo, pragmáticos que aceptan trade-offs para adopción masiva, y usuarios finales que simplemente quieren que las cosas funcionen sin complejidad técnica.

La identidad descentralizada teórica promete autonomía total, pero la implementación práctica requiere abstracciones que inevitablemente introducen dependencias y puntos de confianza. El desafío real no es técnico sino de diseño de incentivos: ¿cómo construir sistemas que preserven autonomía suficiente para que importen los principios de Web3, pero que sean suficientemente usables para que los usuarios promedio adopten sin entender toda la complejidad subyacente? Encontrar el balance correcto es el desafío de diseño central de Web3: suficiente descentralización para preservar autonomía, pero suficiente abstracción de complejidad para permitir adopción masiva. Hasta ahora, la industria no ha resuelto esta tensión, y la fragmentación actual refleja diferentes apuestas sobre qué lado del trade-off priorizar.



---

ISO 18013-5 (carnet de conducir)?



1. El Choque de Filosofías (Por qué nada encaja)

    Los Puristas de la Identidad (DID/VC): Siguen los estándares del W3C. Creen en el "wallet de identidad" (off-chain). Su biblia es la soberanía total. Aquí están proyectos como Privado ID. Para ellos, el dato nunca debería tocar la blockchain por privacidad.

    Los Maximalistas de Ethereum (SBT/EAS): Es la visión de Vitalik. Dicen: "Si no está en la blockchain, no es composable". Inventaron los Soulbound Tokens (SBT) para que tu identidad sea un "tatuaje" en tu wallet. Es público, es on-chain y es fácil de usar para otros contratos.

    Los "Silos" de Utilidad (Worldcoin/Farcaster/Lens): Estos no quieren crear un estándar mundial; quieren que su protocolo funcione.

        Worldcoin quiere una base de datos de humanos (aunque usen ZK).

        Farcaster es su propia red: tu identidad es tu "Fid" (Farcaster ID).

        Lens es un NFT.

2. El "Tirón de Orejas" técnico: ¿Atributo o Identidad?

Has dado en el clavo con lo de los atributos. El ecosistema confunde Identidad (quién eres) con Reputación (qué has hecho).

    Gitcoin Passport es el mejor ejemplo de este "Frankenstein": Empezó como una base de datos propia, se dio cuenta de que nadie quería eso, intentó ser un agregador de VCs, y ahora corre a EAS (Ethereum Attestation Service) porque se ha dado cuenta de que si no hay una capa de atestación común, sus datos son islas desiertas.

    La guerra de la Composabilidad: Si yo quiero crear una dApp de préstamos, ¿qué miro? ¿Tu WorldID? ¿Tu registro en PoH? ¿Tus stamps de Gitcoin? ¿Tu ENS? Como no hay un estándar único, los desarrolladores terminan implementando 5 SDKs distintos. Es un desastre de eficiencia.

Concepto	¿Dónde vive?	¿Qué es?	Ejemplo
Identidad Base	On-chain	El "contenedor" o nombre.	ENS (.eth), Farcaster ID.
Credencial (VC)	Off-chain	Un carnet en tu bolsillo digital. Privado.	Privado ID, Verax.
Atestación	On-chain	Un post-it pegado en tu frente (wallet). Público.	EAS, Proof of Humanity.
SBT	On-chain	Un NFT que no puedes transferir.	El "badge" de una conferencia.


Vitalik sabe que el modelo VC (off-chain) es técnicamente superior para la privacidad, pero pésimo para la agilidad de Web3. Si todo es off-chain y privado en tu wallet, los contratos inteligentes no pueden "reaccionar" automáticamente a tu identidad sin que tú hagas una acción manual. Por eso el ecosistema está moviéndose hacia EAS, intentando que las "atestaciones" sean el lenguaje universal que una todo.

Gitcoin Passport y Privado ID están intentando ser la capa que traduzca todo este caos en un solo "score" o una sola "prueba".

Silo de Identidad", el problema

1. El problema de la "Gravedad de los Datos"

Las atestaciones on-chain (EAS) tienen masa: se quedan pegadas a la red donde se emitieron. Para que no sea una "m...", el ecosistema está intentando tres soluciones:
A. Atestaciones Cross-Chain (El puente de confianza)

Protocolos como LayerZero o Chainlink CCIP están trabajando con EAS para permitir que tú puedas "probar" en la Red B que tienes una atestación en la Red A.

    Cómo funciona: No mueves el dato, mueves una prueba de su existencia. Es complejo, lento y caro.

B. El modelo "Hub and Spoke" (El modelo Farcaster/Lens)

Vitalik y otros proponen que la identidad viva en una "Capa de Identidad" (como una L2 específica o la Mainnet) y que todas las demás redes consulten ese hub.

    El fallo: Si la red principal está congestionada, tu identidad es "lenta".

C. Las ZK-Proofs (La solución elegante)

Aquí es donde los VCs y el off-chain ganan la partida. Si tú tienes tu reputación en un archivo firmado (VC) en tu wallet:

    Vas a cualquier red (Arbitrum, Polygon, Solana).

    Generas una Zero-Knowledge Proof localmente en tu teléfono.

    La dApp la verifica en milisegundos.

    Resultado: Tu reputación es portátil por naturaleza porque no vive en la red, vive contigo.

2. El Gran Cacao: EAS vs. VCs

Aquí está la pelea actual:

    EAS (Ethereum Attestation Service) es genial para la composabilidad dentro de una red. Si todo ocurre en Optimism, las piezas de LEGO encajan perfecto.

    Los VCs (estilo Privado ID) son geniales para la interoperabilidad cross-chain y la privacidad, pero son más difíciles de "leer" para un Smart Contract básico.

3. ¿Por qué se siente roto?

Se siente roto porque los protocolos (Worldcoin, PoH, Gitcoin) tienen miedo de perder su "foso defensivo".

    Si Worldcoin permite que te lleves tu "humano verificado" a un VC que tú controlas totalmente y que puedes usar sin su SDK, ellos pierden el control sobre el usuario y los datos (aunque digan que son pro-privacidad).

    Hay una lucha de poder por ser el "Emisor Maestro" (el Root of Trust).

El "Pegamento" de EAS es una tirita, no una cura

EAS ayuda porque estandariza cómo se escribe el dato (el esquema), para que al menos todos hablen el mismo idioma. Pero no soluciona dónde vive el dato.

¿Cuál es el final de este camino? Probablemente una solución híbrida:

    Emisores (Worldcoin, PoH) emiten el "hecho".

    EAS lo registra on-chain para que sea público y fácil de usar en esa red.

    Tú lo conviertes en un VC para llevártelo en tu wallet a otras redes y mantener tu soberanía.