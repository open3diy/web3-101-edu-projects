# Identidad Web3

**Desambiguación de términos**:

Antes de continuar, debemos aclarar los términos técnicos que la identidad maneja para que no exista ambigüedad sobre lo que hablamos, porque solemos confundirlos o, sobre todo, tratarlos como si fueran lo mismo:

Un **identificador** es un código único que te representa en el sistema. Tu wallet de [MetaMask](https://metamask.io/), como [EOA](https://www.binance.com/es/academy/glossary/externally-owned-account-eoa) o dirección de [SCW](https://ethereum.org/developers/docs/smart-contracts/), tiene una dirección hexadecimal (0x1234...abcd) que funciona como tu identificador en la blockchain, un código que permite a los sistemas localizarte y comunicarse contigo. Este es un ejemplo simple, existen otros identificadores más formales como el [DID (Decentralized Identifier)](https://www.w3.org/TR/did-core/), que veremos más adelante. Lo importante es que un identificador no es una identidad, lo es según las relaciones que establecemos con él.

Una **atestación** es una declaración firmada digitalmente por un emisor que da fe o certifica ciertos atributos, afirmaciones o hechos sobre un sujeto. En términos simples, es cuando un emisor (una universidad, un empleador, una organización, una red) confirma algo sobre ti de forma verificable. Por ejemplo, una universidad puede atestiguar que completaste un grado académico, o una empresa puede atestiguar que trabajaste para ella durante cierto período.

Un **certificado** es el documento formal que materializa el resultado de una atestación. Cuando esa universidad atestigua que completaste un grado, el certificado es el documento —físico o digital— que puedes conservar y presentar como prueba. Implica un emisor con autoridad reconocido.

Una **credencial** es cualquier evidencia o documento firmado que puede presentar el propio sujeto para demostrar algo o probar que tiene ciertos derechos o atributos. Habrás notado que se parece a una atestación y a un certificado, y es normal porque los tres conceptos están relacionados: la atestación es el acto del emisor, el certificado es el documento que lo materializa, y la credencial es ese mismo documento visto desde la perspectiva de quien lo porta y lo usa. Para [W3C](https://www.w3.org/), la especificación [Verifiable Credential (VC)](https://www.w3.org/TR/vc-data-model/) es el estándar técnico concreto que define cómo representar una credencial de forma verificable y portable en entornos digitales descentralizados.

Una **identidad** es la representación reconocible y significativa de quién eres en un contexto social. Conviene subrayarlo porque la identidad siempre depende del marco en el que se interpreta: en el ámbito legal, un identificador como el DNI puede operar como identidad por decisión institucional; en Web3, una dirección puede bastar como identificador técnico. Sin embargo, la identidad rara vez se agota en ese dato. También intervienen elementos de *marca personal*, como un nombre legible en [ENS](https://docs.ens.domains/learn/protocol/) o una imagen [PFP (foto de perfil)](https://tangem.com/es/glossary/pfp/), junto con las credenciales y la reputación que los demás asocian contigo. En muchos contextos no eres solo una persona, sino "la doctora X" o "el auditor Y". Por eso decimos que la identidad se construye y se verifica a partir de una o varias credenciales y preferimos llamarlo "credencial" porque en este contexto es algo que tú presentas y gestionas, mientras que la atestación es algo que otros afirman sobre ti.

**Los tres factores de autenticación**:

La autenticación es el proceso de demostrar que controlas una credencial. Los factores son los métodos disponibles para hacerlo, y se clasifican en tres: algo que sabes, algo que tienes y algo que eres.

El primer factor, **algo que sabes**, son secretos como password, PINs o la frase semilla de una wallet. El password no es la credencial en sí, es el método de autenticación: el servidor verifica que conoces el secreto asociado a tu cuenta. Protocolos como [OAuth 2.0](https://oauth.net/2/) y [OpenID Connect](https://openid.net/connect/) construyen sobre este factor para federación de identidad ("Sign in with Google"). Su debilidad estructural es que el secreto puede robarse, filtrarse o adivinarse —sin importar cuánto se haga hash en el servidor—.

El segundo factor, **algo que tienes**, es el objeto físico o criptográfico que custodias. En Web3 el ejemplo más representativo son las cold wallets, es decir, hardware wallets como Ledger o Trezor. Aunque el ejemplo más ilustrativo de este factor es la evolución directa del password: las [passkeys](https://fidoalliance.org/passkeys/). Las wallets en general se clasifican también como algo que tienes, aunque, como veremos más adelante, no siempre eres el custodio de sus claves.

El tercer factor, **algo que eres**, son rasgos biométricos como huella dactilar, reconocimiento facial o iris. Es el factor más difícil de delegar, pero también el más difícil de revocar si se compromete: una contraseña se cambia, los dedos no. En la práctica su papel habitual es desbloquear localmente el segundo factor —la huella que libera la passkey en el smartphone, el reconocimiento facial que da acceso a la hardware wallet—, no actuar como credencial directa.

**La wallet**:

Dentro de los factores, la wallet es el más relevante. Si quieres saber más sobre ellas puedes acceder al [concepto fundamental de wallet](../fundamentals/wallet.md).

Respecto a la identidad, lo esencial es entender que la wallet no almacena criptomonedas: almacena la clave privada que demuestra que eres quien tiene derecho a actuar desde una dirección. Es esa clave la que convierte una dirección en una identidad. Sin usuario, sin email, sin registro central: quien firma, existe. La misma dirección te identifica en un exchange descentralizado, en una DAO, en un marketplace de NFTs y en cualquier protocolo que se despliegue en el futuro. Nadie puede revocarla.

De ahí el punto crítico: tu identidad en Web3 es tuya exactamente en la medida en que lo sea tu clave privada. Si la custodias tú, eres soberano. Si la custodia otra persona, eres un usuario con derechos contractuales frente a una empresa. Sobre esta base se construyen todos los sistemas de identidad más avanzados —DIDs, ENS, credenciales verificables, reputación on-chain—, pero todos comparten la misma raíz: quien controla la clave, controla la identidad.

**Custodia de claves en Wallet**:

Hemos visto el concepto de *[wallet](https://ethereum.org/wallets/)* (cartera), ahora conviene aclarar qué implica respecto quién controla las claves privadas:

Una **wallet custodial** delega la custodia de las claves privadas a un tercero. Tú accedes con usuario y contraseña, pero las claves que firman tus transacciones las guarda la plataforma. Ejemplos típicos son los exchanges centralizados como [Coinbase](https://www.coinbase.com/) o [Binance](https://www.binance.com/). Si la plataforma cierra, te bloquea la cuenta o es hackeada, pierdes el acceso a tu identidad y fondos porque nunca tuviste las claves. Es el modelo más próximo a la banca tradicional.

Una **wallet self-custodial** (o *autocustodial*) es aquella en la que tú —y solo tú— controlas las claves privadas. La frase canónica del ecosistema es "not your keys, not your coins", y aplica igual a tu identidad: si no controlas las claves, no controlas el identificador. La [EUDI Wallet](https://digital-strategy.ec.europa.eu/es/factpages/european-digital-identity-wallet) que veremos luego es un ejemplo, pero en Web3 [MetaMask](https://metamask.io/) es el ejemplo más representativo: al instalarlo, generas una [SRP (*Secret Recovery Phrase*)](https://support.metamask.io/start/what-is-a-secret-recovery-phrase-and-how-to-keep-your-crypto-wallet-secure/) —una frase de 12 o 24 palabras que deriva todas tus claves privadas y es la única forma de recuperar el acceso a tu wallet. Nadie más la conoce. Es importante aclarar que añadir recuperación social **no convierte la wallet en custodial**: por ejemplo, [MetaMask Social Login](https://metamask.io/es/news/introducing-metamask-social-login) permite recuperar la SRP usando tu cuenta de Google o Apple más una contraseña propia, pero ninguna entidad —ni MetaMask— tiene acceso a todas las piezas necesarias para reconstruirla sin ti. Si pierdes esa contraseña, nadie puede recuperar la wallet por ti.

Una **wallet non-custodial** es aquella en la que ninguna entidad única posee ni puede acceder unilateralmente a la clave privada completa. La propiedad que la define no es cómo se implementa técnicamente, sino ese resultado: el proveedor del servicio no puede mover tus fondos solo, aunque esté involucrado en la custodia. Esto se consigue de varias formas: la más habitual es [MPC (*Multi-Party Computation*)](https://en.wikipedia.org/wiki/Secure_multi-party_computation), una técnica criptográfica donde la clave se divide en fragmentos distribuidos entre el usuario y uno o varios proveedores, de forma que ninguna parte puede firmar transacciones ni reconstruir la clave sin la colaboración del resto. Pero hay otras aproximaciones que cumplen la misma propiedad: una [SCW (*Smart Contract Wallet*)](https://ethereum.org/developers/docs/smart-contracts/) controlada mediante [passkeys](https://fidoalliance.org/passkeys/) delega la autorización a lógica on-chain donde ningún tercero tiene acceso unilateral; un [multisig](https://ethereum.org/en/developers/docs/smart-contracts/) como [Safe](https://safe.global/) requiere la firma de varios firmantes independientes antes de ejecutar cualquier transacción. Lo que comparten todos estos modelos es la ausencia de un único punto de control.

El modelo non-custodial no surge solo de una motivación técnica o de seguridad: tiene también una dimensión legal deliberada. Al distribuir el control entre varias partes sin que ninguna lo posea completamente, se elimina la figura del custodio —una entidad jurídicamente responsable a la que un regulador pueda señalar, reclamar o sancionar—. Esto facilita el acceso a web3 sin la fricción de la self-custody, pero sin que ningún legislador pueda argumentar que existe un tercero que "tiene" los fondos del usuario, lo que complica, por ejemplo, que Hacienda "no los pueda" considerar activos depositados en el extranjero o exija responsabilidades a un intermediario identificable. (PD: decimos que "no los pueda", pero en realidad Hacienda hace un poco lo que quiere, tanga o no razón, lo interpretará a su favor, pero en este caso, lo tiene difícil para demostrar lo contrario).

**Identidad descentralizada**:

Una de las promesas fundamentales de web3 es devolver el control de la identidad a los individuos, no solo por soberanía personal, sino porque concentrar este control en manos de terceros genera vulnerabilidades sistémicas de seguridad.

El objetivo es que cada persona pueda poseer y gestionar su propia identidad de forma autosoberana, a la que puedas relacionar certificados de terceros que acrediten tu identidad, y que interesados puedan validarlo. En la práctica, esta visión no difiere radicalmente de lo que ya conocemos en el mundo físico: posees un DNI en España o un pasaporte que te pertenece, del cual eres custodio, y donde acumulas sellos y validaciones que acreditan tus accesos.

Esta aspiración se ha materializado como [Self-Sovereign Identity (SSI)](https://en.wikipedia.org/wiki/Self-sovereign_identity), o identidad autosoberana. Este principio establece que los individuos deben tener control completo sobre sus credenciales, datos personales y decidir cómo se comparten, sin depender de autoridades centrales para validación o almacenamiento. El término fue popularizado en el artículo [The Path to Self-Sovereign Identity](https://www.lifewithalacrity.com/article/the-path-to-self-sovereign-identity/) de Christopher Allen.

Tanto legisladores como la comunidad web3 han convergido en la [identidad descentralizada](https://www.entrust.com/blog/2023/06/decentralized-identity) como marco técnico de referencia, aunque desde posiciones opuestas: web3 la adopta para lograr validación y almacenamiento genuinamente descentralizados, mientras que los legisladores la adoptan como infraestructura técnica manteniendo emisores cualificados y validación bajo control institucional. No es un consenso sobre el modelo, sino una convergencia en el estándar técnico con visiones irreconciliables sobre quién tiene el control.

Ese estándar técnico fue definido por [W3C](https://www.w3.org/) (World Wide Web Consortium), el organismo internacional que desarrolla estándares web abiertos, mediante tres especificaciones complementarias: los [Decentralized Identifiers (DIDs)](https://www.w3.org/TR/did-core/) definen cómo se componen y resuelven los identificadores descentralizados, las [Verifiable Credentials (VCs)](https://www.w3.org/TR/vc-data-model/) establecen cómo estructurar credenciales que acrediten atributos de la identidad, y las [Verifiable Presentations (VPs)](https://www.w3.org/TR/vc-data-model/#presentations) definen cómo presentarlas selectivamente ante un verificador. Esta tecnología maximiza privacidad mediante control del usuario. Tus credenciales viven en tu wallet bajo tu custodia exclusiva, solo tú decides cuándo y a quién mostrarlas, y puedes usar [Zero-Knowledge Proofs](https://ethereum.org/en/zero-knowledge-proofs/) para revelar el mínimo necesario.

> Si quieres saber más al respecto, puedes acceder al documento del [protocolo DID](../infrastructure/identity/did-protocol.md).

Web3 los reconoce como marco conceptual, pero en la práctica el ecosistema tomó un camino propio: como veremos en el documento más adelante, ninguna [SCW (Smart Contract Wallet)](https://ethereum.org/en/smart-contracts/) ni [EOA (Externally Owned Account)](https://www.binance.com/es/academy/glossary/externally-owned-account-eoa) mainstream usa DIDs en producción, y las atestaciones on-chain como [EAS (Ethereum Attestation Service)](https://attest.org) o [Gitcoin Passport](https://passport.gitcoin.co) reemplazaron a las [VCs (Verifiable Credentials)](https://www.w3.org/TR/vc-data-model/) off-chain porque la composabilidad on-chain era incompatible con el modelo de credenciales del W3C.

> El análisis que sigue se centra en el ecosistema Ethereum. No es una elección arbitraria: es donde se ha concentrado la mayor densidad de investigación e implementación real sobre identidad descentralizada, aparte de ser la elección declarada de referencia de este repositorio y autor.

## Contexto actual del ecosistema de identidad

Con el marco conceptual establecido —qué es la identidad, por qué debe ser autosoberana y qué dos caminos ha tomado la descentralización— podemos ahora ver quién está construyendo en este espacio y desde qué posición.

**Las BigTech en web2: Siloed/Traditional**:

Por una parte, las grandes tecnológicas (*Big Tech*), dominadoras de la [Web2](https://ethereum.org/en/developers/docs/web2-vs-web3/) en plataformas centralizadas como redes sociales y servicios cloud, gestionan una identidad digital que no te pertenece realmente. Cuando creas una cuenta en Facebook, Google o cualquier plataforma digital, la empresa almacena tu información, controla el acceso a ella y puede modificarla, censurarla o eliminarla sin tu consentimiento previo. Esta fragmentación de identidad entre múltiples plataformas que no se comunican entre sí es lo que técnicamente se conoce como [siloed identity](hhttps://medium.com/evernym/the-three-models-of-digital-identity-relationships-ca0727cb5186), donde cada servicio mantiene tu información aislada en su propio silo.

Este modelo centralizado genera varios problemas fundamentales. Primero, existe un riesgo de seguridad significativo porque todas tus credenciales están almacenadas en servidores centralizados que se convierten en objetivos atractivos para cyber criminales. Segundo, no tienes portabilidad: tu reputación en Amazon no sirve en eBay, tu historial profesional en LinkedIn no se transfiere a otras plataformas. Tercero, dependes completamente de la plataforma: si deciden cerrar tu cuenta, pierdes años de datos, conexiones y reputación acumulada. Esta dependencia crea lo que se denomina [vendor lock-in](https://en.wikipedia.org/wiki/Vendor_lock-in), donde quedas atrapado en el ecosistema de un proveedor específico sin capacidad real de migrar tu identidad y datos a alternativas.

Además, el modelo centralizado crea problemas de privacidad. Para usar la mayoría de servicios digitales, debes revelar más información de la necesaria. Si quieres entrar a un sitio para mayores de edad, tienes que proporcionar tu fecha de nacimiento completa cuando en realidad solo necesitan saber que eres mayor de 18 años.

**Identidad federada: cuando BigTech se convierte en el intermediario**:

La industria reconoció tempranamente que obligar a usuarios a crear cuentas separadas en cada sitio web era insostenible. La solución que emergió fue el modelo de identidad federada: permite que un proveedor de identidad externo actúe como intermediario de confianza. Cuando hoy encuentras botones de "Sign in with Google", "Sign in with Apple" o "Sign in with Facebook" en prácticamente cualquier aplicación o servicio digital, estás usando este modelo basado principalmente en [OpenID Connect (OIDC)](https://openid.net/connect/), una capa de identidad construida sobre [OAuth 2.0](https://oauth.net/2/) que extiende su framework de autorización con capacidades de autenticación. [SAML](https://en.wikipedia.org/wiki/Security_Assertion_Markup_Language) es un protocolo alternativo más antiguo que todavía se usa en contextos empresariales.

Este enfoque resolvió problemas prácticos significativos: ya no necesitas recordar docenas de contraseñas diferentes, ni repetir procesos de registro tediosos en cada sitio. Sin embargo, simplemente trasladó la centralización a un nivel superior. En lugar de tener tu identidad fragmentada en múltiples silos, ahora depende de un puñado de gigantes tecnológicos que actúan como guardianes. Google, Apple, Facebook y Microsoft se han convertido en los IDPs dominantes, intermediando la mayoría de relaciones digitales en Internet. Si una de estas compañías cierra tu cuenta o decide que no cumples sus términos de servicio, pierdes acceso simultáneamente a docenas o cientos de servicios que dependen de esa identidad federada.

En 2026, este modelo no solo persiste sino que se ha convertido en el método de autenticación más usado globalmente en aplicaciones Web2. Su relevancia para Web3 es doble y aparentemente contradictoria. Por una parte, muchas dApps pragmáticamente implementan autenticación híbrida: ofrecen "Sign-In with Ethereum" para usuarios nativos crypto, pero también "Sign-In with Google" para facilitar onboarding gradual desde Web2 sin la fricción de gestionar claves privadas desde el primer momento.

**DID en Gobiernos y reguladores**:

La identidad descentralizada ha sido la opción adoptada por reguladores y gobiernos como marco normativo. La regulación [eIDAS 2.0](https://digital-strategy.ec.europa.eu/en/policies/eidas-regulation) y su implementación mediante la European Digital Identity Wallet (EUDI Wallet) ofrecen un equilibrio entre el control institucional y la autonomía del usuario, materializando las tecnologías Decentralized Identifiers (DIDs) y Verifiable Presentations en un sistema con respaldo legal.

Respondiendo a las carencias del modelo Web2, desde 2026 las plataformas de gran tamaño —Meta (Facebook, Instagram), Amazon, Apple, Booking.com, TikTok, Zalando y otras— están obligadas por ley a aceptar la EUDI Wallet como método válido de autenticación e identificación.

El uso de la cartera digital europea es voluntario para los ciudadanos: los Estados miembros deben ofrecer métodos alternativos de identificación para quienes no deseen adoptarla. Sin embargo, la regulación cubre sectores tan amplios —banca, transporte, energía, seguridad social, sanidad, suministro de agua, infraestructura postal, infraestructura digital, educación y telecomunicaciones— que en la práctica se convierte en un estándar de facto para la identidad digital en Europa.

**DID soberano fuera de Europa: Bután y Buenos Aires**:

El modelo DID/VC no es exclusivo de Europa ni requiere el paraguas regulatorio de eIDAS para funcionar. Dos casos reales demuestran que gobiernos pueden adoptar identidad descentralizada con una filosofía más cercana a la visión SSI original, donde el protocolo es abierto y el Estado actúa como emisor de credenciales pero sin ser propietario ni intermediario permanente.

El [Sistema de Identidad Digital Nacional de Bután (NDI)](https://www.bhutanndi.com/) migró en octubre de 2025 desde Polygon a Ethereum mainnet, convirtiéndose en uno de los primeros sistemas de identidad nacional anclados directamente en la L1 de Ethereum. El sistema emite credenciales de ciudadanía, pasaporte e identidad oficial como Verifiable Credentials firmadas digitalmente en la wallet personal del ciudadano. La privacidad se implementa mediante Zero-Knowledge Proofs: un ciudadano puede demostrar que es mayor de edad o que es residente sin revelar su fecha de nacimiento exacta ni su número de identificación. Al anclar las pruebas criptográficas en Ethereum, cualquier parte puede verificar la autenticidad de las credenciales sin consultar a ninguna autoridad central butanesa, algo que eIDAS no permite porque mantiene listas de confianza gubernamentales como requisito de verificación.

[QuarkID](https://www.digitalpublicgoods.net/r/quarkid), desarrollado por la Secretaría de Innovación de la Ciudad de Buenos Aires, introduce un matiz arquitectónico especialmente relevante: el gobierno no es propietario del protocolo, sino un usuario más de él. Cuando el Gobierno de la Ciudad de Buenos Aires integró QuarkID en su aplicación oficial `miBA` en 2024, los más de 3,6 millones de usuarios recibieron identidades digitales descentralizadas para gestionar documentos civiles —certificados de nacimiento, matrimonio, defunción, registros fiscales, vacunación— como VCs en ZKSync Era, la L2 de Ethereum basada en ZK-proofs. La consecuencia de que el GCBA sea "usuario del protocolo" y no su propietario es que ningún tercero, ni siquiera el propio gobierno, puede rastrear cuándo o para qué usa un ciudadano sus credenciales. QuarkID es open source y ha sido reconocido como [Bien Público Digital](https://www.digitalpublicgoods.net/) en el marco de los Objetivos de Desarrollo Sostenible de la ONU, lo que lo convierte en infraestructura reutilizable por cualquier gobierno sin licencias ni dependencia de un proveedor.

La diferencia estructural con eIDAS es precisamente esa: eIDAS impone un anillo de control institucional alrededor de la tecnología DID/VC mediante listas de emisores cualificados y certificación de wallets, lo que garantiza reconocimiento legal pero a costa de recentralizar la confianza en los estados. Bután y Buenos Aires demuestran que es posible emitir credenciales con validez real sin ese anillo, dejando la verificación criptográfica en manos del protocolo abierto.

**OpenID4VC: cuando los IDPs se transforman en emisores de credenciales**:

Por otra parte, el estándar [OpenID4VC (OpenID for Verifiable Credentials)](https://openid.net/sg/openid4vc/) está transformando el panorama al convertir IDPs (proveedores de identidad) tradicionales en VC (emisores de credenciales verificables). Esto significa que Google o Apple pueden emitir VCs que el usuario guarda en su wallet Web3 o [EUDI Wallet europeo](https://digital-strategy.ec.europa.eu/es/factpages/european-digital-identity-wallet), creando un puente entre la identidad federada Web2 y las credenciales autosoberanas.

La diferencia fundamental con la federación tradicional es arquitectónica: en lugar de que Google intermedie cada login manteniendo control perpetuo, ahora Google puede emitir una credencial verificable una vez que tú guardas en tu wallet y presentas donde quieras sin su participación posterior. El IDP sigue siendo el emisor inicial, pero pierde el rol de intermediario permanente que caracteriza a la federación clásica.

Paralelamente, emisores especializados como [Fractal ID](https://www.fractal.id/) o [Civic](https://www.civic.com/) operan como emisores nativos de VCs para KYC, realizando verificación una vez y emitiendo una credencial que tú custodias y presentas donde necesites, sin intermediación posterior. Estos proveedores nunca fueron IDPs en el sentido federado, desde su diseño inicial operan bajo el paradigma de credenciales verificables autosoberanas.

La distinción crucial es que eIDAS 2.0 establece dos niveles de confianza: **credenciales cualificadas**, emitidas por Qualified Trust Service Providers (QTSPs) certificados bajo eIDAS con reconocimiento legal pleno en toda la UE, y **credenciales no cualificadas**, emitidas por proveedores privados como Fractal ID o Civic, técnicamente compatibles con EUDI Wallet pero sin el mismo peso legal que las gubernamentales. Para casos críticos como identidad oficial o edad legal, predominarán las credenciales cualificadas; para casos de uso menos regulados como membresías o reputación, las credenciales privadas seguirán siendo válidas y útiles.

**Web3 con KYC/AML**:

En Web3 en lo referente al cumplimiento normativo (*compliance*) debemos reconocer una realidad incómoda: [KYC](https://en.wikipedia.org/wiki/Know_your_customer) (*Know Your Customer*) y [AML](https://en.wikipedia.org/wiki/Money_laundering#Anti-money_laundering) (*Anti-Money Laundering*) no representan identidad descentralizada, sino identidad centralizada tradicional operando dentro de Web3 por obligación legal. Esta distinción es fundamental para entender correctamente el ecosistema.

Cada exchange donde compras ETH o BTC requiere procesos KYC rigurosos: pasaporte, prueba de domicilio, selfie sosteniendo tu documento, declaraciones de fuente de fondos. Este proceso es completamente centralizado y contradice frontalmente los principios de identidad autosoberana. Entregas tus datos personales más sensibles a una empresa privada que los almacena en sus servidores, exactamente el modelo centralizado que queremos superar.

¿Por qué existe esta contradicción en un ecosistema que promete descentralización? Regulación. Los gobiernos han implementado marcos regulatorios estrictos que obligan a cualquier entidad que facilite conversión entre fiat y criptomonedas a implementar controles KYC/AML. Regulaciones como la [5th Anti-Money Laundering Directive (5AMLD)](https://eur-lex.europa.eu/eli/dir/2018/843/oj) en Europa o el [Bank Secrecy Act](https://www.fincen.gov/resources/statutes-and-regulations/bank-secrecy-act) en Estados Unidos existen para prevenir lavado de dinero, financiamiento del terrorismo y evasión fiscal.

El resultado es que la mayoría de usuarios comprometen su privacidad desde el momento cero. Tu primer contacto con crypto probablemente fue entregar tu identidad legal completa a Coinbase o Binance. Incluso protocolos [DeFi](https://ethereum.org/en/defi/) descentralizados como [Uniswap](https://uniswap.org/) o Aave enfrentan presión regulatoria para implementar restricciones geográficas y verificación de identidad cuando alcanzan volúmenes significativos.

Protocolos como [Aave Arc](https://aave.com/) experimentaron con "DeFi permisionado" donde solo usuarios KYC-verificados podían participar. [MakerDAO](https://makerdao.com/) discute implementar KYC para activos del mundo real (RWA). DAOs grandes enfrentan dilemas similares: ¿cómo cumplir obligaciones fiscales sin comprometer pseudonimidad de miembros?

La identidad descentralizada teórica choca con las realidades del sistema financiero tradicional. Mientras los estados-nación controlen las rampas de entrada y salida del ecosistema crypto, KYC centralizado será inevitable para la mayoría de participantes. Los puristas argumentan que esto es temporal, que eventualmente viviremos completamente on-chain. Los pragmáticos reconocen que la regulación no desaparecerá, y que sistemas híbridos son el futuro más probable.

**Web3 con privacidad off-chain**:

En este modelo DID, se basa en Verifiable Credentials (VCs) que viven fuera de la cadena, bajo la custodia exclusiva del usuario. Tú decides cuándo y a quién presentarlas, y puedes usar [Zero-Knowledge Proofs](https://ethereum.org/en/zero-knowledge-proofs/) para revelar únicamente lo necesario. Un smart contract no puede simplemente "leer" si tienes un diploma universitario: necesitas presentar activamente una prueba. Esto protege tu privacidad, pero introduce fricción en la composabilidad: los protocolos DeFi no pueden consultar tu historial crediticio automáticamente, las DAOs no pueden verificar membresías sin tu intervención, y los NFT marketplaces no pueden filtrar usuarios por jurisdicción sin que tú lo permitas.

Para Ethereum, proyectos como [Privado ID](https://www.privado.id/) (anteriormente Polygon ID) representan la visión SSI más purista, priorizando la privacidad aunque a costa de la composabilidad on-chain. Además, emisores especializados como [Fractal ID](https://www.fractal.id/) o [Civic](https://www.civic.com/) facilitan el cumplimiento de KYC necesario para ciertas dApps, actuando como puentes entre la identidad legal y el ecosistema descentralizado.

Esta visión puede entenderse como una mejora en conveniencia y cumplimiento normativo, destacando el caso de Polygon, donde el marco regulatorio y la protección de datos son relevantes. Permite que reputación on-chain y privacidad coexistan, lo cual es aceptable si es necesario, aunque no representa la visión DeSoc que veremos más adelante. Es una solución pragmática que las instituciones requieren: facilita el acceso a KYC, AML y otras credenciales verificables (VC), sean cualificadas o no. Aunque no elimina la centralización, al menos mejora la experiencia de usuario.

**Web3 con identidad basada en reputación on-chain y grafo social**:

Este es el modelo básico de [wallet Web3](https://ethereum.org/wallets/find-wallet/) que este repositorio comprende como el relevante para una web descentralizada permisionless.

Lo que distingue a este modelo de todos los anteriores es que la identidad no se emite: se acumula en base a la [reputación](7-2-reputation.md). No hay una autoridad que te certifique quién eres; lo que define tu identidad es el rastro verificable que has dejado on-chain —a qué DAOs perteneces, qué eventos has atendido, en qué gobernanzas has votado, qué protocolos usas—. [DeSoc (Decentralized Society)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763), el paper de 2022 de Vitalik Buterin, E. Glen Weyl y Puja Ohlhaver, articuló este marco teórico. La identidad, en este modelo, es pública por diseño y no requiere ningún emisor; su contrapartida es que carece de reconocimiento legal y es vulnerable a la fabricación de señales.

Las primitivas técnicas que lo materializan —[Soulbound Tokens (SBTs)](https://www.binance.com/en/academy/articles/what-are-soulbound-tokens-sbt), [POAPs](https://poap.xyz/), [atestaciones EAS](https://attest.org/), protocolos sociales como [Lens](https://www.lens.xyz/) o [Farcaster](https://www.farcaster.xyz/)— son las mismas que usa la reputación on-chain. No es casualidad: identidad y reputación comparten capa técnica pero responden a preguntas distintas. Lo que separa un uso del otro lo desarrollamos en la sección siguiente y en detalle en [reputación en Web3](7-2-reputation.md).

Todo lo construido hasta aquí —atestaciones, SBTs, nombre ENS, reputación— queda vinculado a una dirección: la de tu wallet. Esta dependencia ha pasado por tres momentos que conviene distinguir para no confundir términos.

En el modelo original, la wallet es una [EOA (Externally Owned Account)](https://www.binance.com/es/academy/glossary/externally-owned-account-eoa): clave privada y dirección son la misma entidad. Identidad y acceso coinciden en un único punto de fallo —perder la clave significa perder todo lo acumulado, sin posibilidad de recuperación.

El modelo de [Account Abstraction (EIP-4337)](https://eips.ethereum.org/EIPS/eip-4337) separó ambos roles: la identidad pasa a vivir en una [Smart Contract Wallet (SCW)](https://ethereum.org/en/smart-contracts/), un contrato persistente en la cadena, mientras que la EOA queda relegada a ser la llave de entrada —reemplazable sin perder la identidad acumulada. La dirección relevante deja de ser la de la EOA y pasa a ser la del contrato.

[EIP-7702](https://eips.ethereum.org/EIPS/eip-7702) volvió a mover las piezas: permite que una EOA adopte temporalmente el comportamiento de un smart contract sin desplegar uno separado, recuperando capacidades que antes requerían una SCW y difuminando la separación nítida que Account Abstraction había establecido. La EOA no desapareció —volvió a ser relevante. Las implicaciones prácticas de esta evolución para la experiencia de usuario las desarrollamos en [experiencia de usuario Web3](8-1-user-experience.md).

> El ecosistema de wallets, su tecnología e implementación lo analizamos en el [ecosistema de wallets web3](../infrastructure/identity/web3-wallet-ecosystem.md).

**Web3 onboarding**:

La adopción masiva de Web3 choca con una barrera estructural: gestionar claves privadas, entender gas o instalar una extensión de navegador son fricciones que la mayoría de usuarios no supera como veremos en [experiencia de usuario](8-1-user-experience.md). La respuesta pragmática del ecosistema fue llevar Web3 al usuario en lugar de al revés.

Este modelo combina dos avances técnicos. Por un lado, [Account Abstraction (ERC-4337)](https://eips.ethereum.org/EIPS/eip-4337) permite que alguien use una dApp sin tener ETH ni comprender el gas: un [Paymaster](https://www.alchemy.com/blog/account-abstraction) patrocina las transacciones en nombre del usuario. Por otro, las redes de capa 2 como [Base](https://base.org/) u [Optimism](https://www.optimism.io/) hacen que esas operaciones sean baratas y casi instantáneas. El resultado desde la perspectiva del usuario es una aplicación web normal: registro en segundos, sin seed phrase visible, con recuperación por email o huella dactilar.

La pieza de identidad que lo hace posible son las *embedded wallets*: plataformas como [Privy](https://www.privy.io/), [Dynamic](https://www.dynamic.xyz/) o [Web3Auth](https://web3auth.io/) generan una wallet derivada del login social del usuario — Google, Apple, email — usando [MPC](https://en.wikipedia.org/wiki/Secure_multi-party_computation) para que ninguna parte controle la clave completa. La wallet existe, la dirección existe, las transacciones se anclan en cadena; pero el usuario nunca ve una seed phrase ni toca las claves.

La diferencia de identidad respecto al modelo de reputación on-chain es, sin embargo, estructural. El identificador del usuario nace atado al OAuth del proveedor externo y a la plataforma que lo genera. Si el proveedor cierra, si el usuario migra de dApp, o si quiere usar esa dirección en un contexto diferente, la portabilidad real no está garantizada. Es cierto que cuando varias dApps comparten el mismo proveedor de onboarding el usuario puede reaparecer con la misma dirección, y en ese sentido existe cierta continuidad de identidad entre aplicaciones. Pero eso no es composabilidad abierta: es federación. Ningún contrato externo puede leer automáticamente el historial de ese usuario sin integrar al mismo proveedor, ni ninguna dApp independiente puede construir sobre esa reputación sin pasar por él.

En términos de identidad, blockchain actúa aquí como capa de consolidación y seguridad —las transacciones quedan ancladas, son auditables e inmutables—, pero la capa de acceso e identificación permanece en el silo del proveedor. No es un modelo malo: resuelve onboarding con eficacia demostrada. Pero responde a una pregunta diferente a la de la identidad abierta y permisionless. La distinción que importa no es técnica sino de soberanía: en este modelo el usuario usa una cuenta; en el modelo de reputación on-chain, el usuario posee una dirección.

**Proof of Personhood**:

Algunos actores del ecosistema se centran exclusivamente en responder una pregunta de identidad muy concreta: ¿eres un humano único real? No se trata de certificar atributos ni de acumular reputación, sino de emitir una credencial que pruebe unicidad biológica resistiendo ataques [Sybil](https://www.microsoft.com/en-us/research/publication/the-sybil-attack/) —la creación de múltiples identidades falsas—. Este mecanismo es fundamental para habilitar votación cuadrática, distribuciones justas de tokens o renta básica universal on-chain.

*[Worldcoin](https://worldcoin.org/)* emite [World ID](https://world.org/world-id) tras el escaneo del iris mediante su dispositivo *Orb*. El dispositivo genera un hash único derivado del iris y lo valida contra la base de datos de hashes ya registrados para asegurar que la persona no existe previamente en el sistema. Una vez verificado, la prueba se convierte en un ZK-proof basado en el protocolo [Semaphore](https://semaphore.appliedzkp.org/): al interactuar con una aplicación, la wallet certifica que posees una credencial válida emitida por un Orb y que es la primera vez que realizas esa acción, sin revelar qué hash de iris ni identidad real. Verificado físicamente una vez, el usuario opera digitalmente con privacidad total. Los World IDs pueden verificarse en [Ethereum](https://ethereum.org/) mainnet y otras chains, y para su gestión opera [World Chain](https://world.org/world-chain), su propia L2 sobre [OP Stack](https://stack.optimism.io/). Sus limitaciones son estructurales: no puedes cambiar tu iris si el hash se compromete, y depende de hardware biométrico centralizado para la emisión.

*[Proof of Humanity](https://www.proofofhumanity.id/)* es un registro público de humanos verificados desplegado como smart contract en Ethereum mainnet. Tu credencial es simplemente estar en esa lista: para entrar debes subir un vídeo público, depositar una garantía económica y obtener avales de miembros ya registrados. Es transparente y sin hardware propio, pero sin privacidad: el vídeo y el registro son públicos.

*[Idena](https://idena.io/)* resuelve el problema sin biometría ni vídeo público. Su mecanismo es una ceremonia de validación sincronizada: en un momento fijo conocido de antemano, todos los participantes resuelven simultáneamente una serie de captchas visuales diseñados para ser fáciles para humanos y difíciles para IA. La clave es la sincronización global: si intentas validar dos identidades a la vez, necesitarías estar físicamente en dos lugares resolviendo captchas en paralelo, lo que hace el ataque costoso en proporción al número de identidades falsas que quieras mantener. La credencial resultante no expone biometría ni vídeo, y el protocolo es completamente descentralizado. Su limitación es la fricción de participación: hay que estar disponible en un momento concreto, y si te lo pierdes, no hay segunda oportunidad hasta la siguiente ceremonia.

Nótese que actores como [Gitcoin Passport](https://passport.gitcoin.co/) o [BrightID](https://www.brightid.org/) suelen citarse en este contexto, pero responden a una lógica distinta: no prueban unicidad biológica sino que agregan señales de actividad y conexiones sociales para inferir que no eres un bot. Son herramientas de resistencia Sybil por reputación, y como tales se desarrollan en [reputación en Web3](7-2-reputation.md).

## La fragmentación de acceso y la autenticación

Web2 resolvió la fragmentación de acceso con identidad federada: un único proveedor —Google, Apple— autentica al usuario en miles de servicios diferentes. Web3 no tiene ese equivalente universal. Los distintos modelos de identidad del ecosistema conviven sin una capa de acceso unificada, y el usuario lo nota: según la plataforma que use encontrará experiencias completamente distintas.

En el ecosistema nativo de dApps, la fragmentación de conexión y autenticación está en gran medida resuelta: existen estándares consolidados tanto para detectar y conectar wallets como para autenticar sesiones mediante firma de mensaje. Los detalles técnicos de cómo funciona esa capa los desarrollamos en el [ecosistema de wallets Web3](../infrastructure/identity/web3-wallet-ecosystem.md).

Donde persiste la fragmentación es fuera del ecosistema nativo. Las plataformas orientadas a adopción masiva sustituyen la wallet por un login social o de email, más cómodo pero con custodia delegada. Las aplicaciones con obligaciones legales —exchanges, protocolos DeFi regulados, servicios financieros— exigen un proceso KYC donde el usuario presenta su DNI, un selfie y prueba de domicilio antes de poder operar. Los servicios que necesitan garantizar unicidad de persona añaden prueba biométrica de humanidad. Y desde 2026, la regulación europea obliga a grandes plataformas a aceptar la EUDI Wallet como método de identificación oficial, añadiendo una modalidad más.

Ninguno de estos métodos es intercambiable con otro, y el usuario se los va encontrando sin aviso. Eso tiene un nombre en experiencia de usuario: "muro de autenticación". Cada método desconocido aumenta la probabilidad de abandono.

Incluso dentro del ecosistema nativo existe un problema de legado. Las dApps desplegadas antes de que el ecosistema convergiera en estándares de detección de wallets se construyeron sobre bibliotecas sesgadas hacia MetaMask, y ese código permanece. Una [investigación de campo publicada en 2023](https://www.reddit.com/r/web3/comments/17bgv90/the_great_wall_in_web3_research/) documentó el alcance del problema analizando las 100 dApps más utilizadas con tres wallets distintas: el 32% directamente no funciona si el usuario no tiene MetaMask instalada; el 43% tiene opciones de login prefijadas en código, incapaces de detectar otras wallets aunque el usuario las tenga; solo el 13% funciona como debería, reconociendo automáticamente cualquier wallet inyectada; el 14% restante muestra diez o más opciones simultáneas generando parálisis por decisión. Nueve de cada diez aplicaciones fallaban en algún punto del flujo.

La raíz de este legado está en la propia naturaleza de Web3. En una aplicación Web2 centralizada, corregir una librería de autenticación obsoleta es una operación de backend que se despliega en horas. En Web3, la lógica que controla accesos puede estar en contratos inmutables, el frontend puede estar anclado en IPFS sin administrador, y la dApp puede no tener ya ningún equipo activo que la mantenga. La descentralización que garantiza que nadie puede censurar la aplicación es la misma propiedad que garantiza que nadie puede actualizarla. [CAIP-122](https://github.com/ChainAgnostic/CAIPs/blob/main/CAIPs/caip-122.md) y los estándares modernos de detección multi-wallet resuelven el problema para las dApps nuevas, pero el ecosistema heredado solo evoluciona por presión económica: cuando el coste de perder usuarios supera el coste de refactorizar, se refactoriza.

Con esta fragmentación, es necesaria una elección y para los propósitos de este repositorio la referencia es clara: la wallet con soberanía real sobre las claves —self-custodial o non-custodial— usada en el modelo de identidad basado en reputación on-chain. Es el único modelo donde la identidad no depende de ningún proveedor externo, donde lo acumulado en cadena pertenece al usuario sin intermediarios, y donde la dirección puede construir historial composable con cualquier protocolo del ecosistema. Los demás modelos tienen su lugar en contextos específicos, pero no son el objetivo aquí. Sin embargo, la tensión entre ese acceso permissionless y los modelos institucionales basados en KYC o federación es estructural y no desaparecerá; cualquier proyecto que aspire a operar más cerca del mundo real deberá navegar esa frontera.

## Sistemas de nombres descentralizados

Una dirección Ethereum es un código hexadecimal de 42 caracteres: fácil de confundir, imposible de recordar. Los sistemas de nombres descentralizados resuelven esto asociando esa dirección a un nombre legible como `maria.eth`, convirtiendo algo técnico en algo humano. Más allá de recibir pagos, ese nombre puede convertirse en el punto de entrada a toda tu identidad pública: tu avatar, tus redes sociales, tus direcciones en otras blockchains o tu sitio web descentralizado, todo accesible desde un solo identificador que tú controlas.

**ENS: tu nombre en Ethereum**:

[Ethereum Name Service](https://ens.domains/) es el estándar principal de identidad humana en el ecosistema Ethereum. Actúa como el equivalente descentralizado del [sistema DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) tradicional, reemplazando el control de entidades centralizadas como ICANN por contratos inteligentes públicos. Su función fundamental es traducir las complejas direcciones hexadecimales de 42 caracteres en nombres legibles terminados en `.eth`, facilitando enormemente la interacción del usuario con la red.

Lejos de limitarse a una simple libreta de direcciones para recibir fondos, un dominio ENS funciona como un perfil de identidad digital completo y extensible. Al registrar un nombre, el usuario obtiene un registro en la cadena de bloques capaz de almacenar y vincular una amplia variedad de metadatos. Esto incluye direcciones de otras redes como Bitcoin o Solana, enlaces a sitios web descentralizados alojados en [IPFS](https://ipfs.tech/), e información de contacto tradicional como correos electrónicos o perfiles de redes sociales. Un caso de uso especialmente popular es la configuración del campo de avatar, que representa la implementación técnica y práctica del concepto de [PFP (Profile Picture)](https://tangem.com/es/glossary/pfp/) en Web3. En este campo, el usuario puede enlazar una imagen o un token no fungible que posea; al hacerlo, esta foto de perfil se propaga automáticamente por todas las aplicaciones descentralizadas compatibles, funcionando como un inicio de sesión universal donde la imagen acompaña al usuario sin necesidad de subirla en cada plataforma. De esta forma, el nombre se convierte en un punto de anclaje único para toda la presencia digital del usuario en la Web3.

La utilidad de este sistema se maximiza gracias a su capacidad de resolución inversa. Mientras que la resolución directa permite enviar activos escribiendo un nombre en lugar de una dirección, la resolución inversa permite que las aplicaciones descentralizadas, billeteras y exploradores de bloques muestren automáticamente el nombre `.eth` del usuario en lugar de su dirección criptográfica. Esta característica transforma el identificador en una identidad visual persistente que acompaña al usuario a través de todo el ecosistema, humanizando la experiencia de navegación y reduciendo la fricción técnica.

Para mantener la disponibilidad del espacio de nombres y evitar el acaparamiento especulativo, el protocolo implementa un modelo económico basado en renovaciones anuales gestionado por su propia organización autónoma descentralizada. Los costos varían según la longitud del dominio, estableciendo precios fijos para nombres comunes y mecanismos de subasta para identificadores más cortos y demandados, asegurando así un acceso equitativo y un mantenimiento continuo del sistema.

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

## NFT Profile Pictures (PFP): identidad social visual

Como vimos al hablar de ENS, la foto de perfil es un componente central de la identidad en Web3. Más allá de la infraestructura técnica, los [NFT Profile Pictures o PFPs](https://tangem.com/es/glossary/pfp/) se convirtieron en el fenómeno cultural dominante de identidad entre 2021 y 2022. Colecciones como [Bored Ape Yacht Club](https://boredapeyachtclub.com/) o [CryptoPunks](https://www.larvalabs.com/cryptopunks) dejaron de ser simplemente arte digital para convertirse en señales de pertenencia: usar uno de estos NFTs como avatar significaba declarar membresía en una comunidad, afinidad con ciertos valores del ecosistema y, de forma implícita, una capacidad económica significativa dado el precio que alcanzaron.

Lo que diferencia un PFP de una foto de perfil corriente es que la propiedad es verificable públicamente. Cualquiera puede comprobar que quien lo usa es efectivamente el dueño del token, no alguien que simplemente copió la imagen. Esto creó una nueva forma de credencial social: la membresía no se declara, se demuestra. Twitter/X llegó a marcar estos avatares con un hexágono en lugar del círculo habitual como señal de verificación, reconociendo que incluso las plataformas Web2 veían valor en este tipo de identidad verificable.

Sin embargo, el modelo tiene limitaciones evidentes. El valor identitario quedó atado al valor especulativo: cuando los precios colapsaron, la señal de estatus colapsó con ellos. Además, construir identidad sobre activos que cuestan miles o decenas de miles de dólares resultó inherentemente exclusionario, lo que limitó su alcance como sistema de identidad general.

Lo que los PFPs demuestran es que la identidad en Web3 no es solo infraestructura técnica, sino también un fenómeno social y cultural. La tecnología de nombres y avatares que ofrece ENS tiene sentido precisamente porque responde a esta necesidad humana real de tener una cara reconocible en el ecosistema.

## Identidad de organizaciones descentralizadas

Una DAO es fundamentalmente un conjunto de smart contracts desplegados en una blockchain. Su dirección de contrato la identifica de forma inequívoca en la red, pero esa dirección por sí sola no dice nada legible sobre qué es la organización, qué gobierna, ni cómo se relaciona con el mundo exterior. La pregunta de identidad para una DAO difiere de la de un individuo: no se trata de demostrar quién eres, sino de declarar qué eres de forma verificable y estandarizada.

El primer nivel de identidad legible es un nombre ENS. Una DAO puede registrar `nombredao.eth` y asociarlo a sus contratos de la misma manera que un individuo registra su nombre personal. Esto permite que exploradores de blockchain y herramientas de gobernanza muestren un nombre comprensible en lugar de una dirección hexadecimal.

Pero un nombre no describe una organización. Para eso existe [ERC-4824](https://eips.ethereum.org/EIPS/eip-4824), un estándar que permite a cualquier contrato de DAO publicar sus propios metadatos de forma que cualquier herramienta pueda leerlos sin necesitar integraciones a medida. El mecanismo es simple: el contrato implementa una función `daoURI()` que devuelve una URI apuntando a un documento JSON con el nombre de la DAO, descripción, enlace a sus propuestas de gobernanza y los contratos que forman parte de la organización. Gracias a esta interfaz común, plataformas como [Tally](https://www.tally.xyz/) o [Snapshot](https://snapshot.org/) pueden descubrir y presentar cualquier DAO que implemente el estándar sin acuerdos individuales con cada organización.

El tercer nivel es el puente con el mundo real. Aquí la palabra "identidad" se refiere a **personalidad jurídica**.

En el derecho, tener "identidad" significa ser reconocido como alguien que puede tener propiedades, firmar contratos y asumir responsabilidades. Tú tienes identidad jurídica (tu DNI), por eso el banco te abre una cuenta. Tu perro no tiene identidad jurídica, por eso no puede firmar una hipoteca.

Una DAO, por defecto, está en la situación legal de tu perro: existe, pero para la ley no es "alguien". Si la DAO quiere alquilar una oficina, el dueño del edificio no puede firmar un contrato con "un código en la blockchain". Necesita firmar con *alguien* que tenga identidad legal.

Por eso la DAO crea una empresa (LLC o Fundación). No para hacer negocio, sino simplemente para **adquirir esa identidad jurídica** que le falta. La empresa es el "representante legal" autómata: existe solo para prestarle su cara legal (su identidad) a la DAO, permitiéndole interactuar con impuestos, bancos y jueces. Sin esta empresa, la DAO es un fantasma legalmente invisible; con la empresa, adquiere una identidad válida ante la ley.

> Este repositorio no aborda este tipo de relación legal, se centra en DAO descentralizadas para aplicaciones de utilidad, por lo tanto, aparte de esta mención, no se hablará mucho más al respecto.

## Almacenamiento de datos de identidad: Ceramic y DWNs

Cuando construyes una dApp que va más allá de simples transacciones y necesitas gestionar perfiles de usuario, historial de credenciales o grafos sociales, te encuentras con un problema concreto: la blockchain es cara para almacenar datos ricos y mutables, e IPFS almacena archivos estáticos inmutables. Ninguno de los dos está diseñado para la identidad dinámica —el perfil de un usuario que cambia, las VCs que se revocan, el historial que crece—.

Esto es relevante principalmente si estás construyendo una dApp social (un protocolo tipo Lens propio, un sistema de reputación con perfiles enriquecidos) o si necesitas dar soporte a credenciales verificables (VCs) con almacenamiento descentralizado. Para la mayoría de dApps DeFi o de gobernanza, EAS resuelve el problema sin necesitar esta capa. Para aplicaciones que sí lo necesitan, el ecosistema ofrece dos aproximaciones con filosofías distintas: Ceramic Network y los Decentralized Web Nodes (DWNs).

### Ceramic Network

[Ceramic](https://ceramic.network/) actúa como una red de datos descentralizada para información mutable basada en streams. Su papel es fundamental para dar viabilidad práctica a los sistemas de Verifiable Credentials (VCs).

**Almacenamiento eficiente**: Guardar credenciales complejas directamente en Ethereum es prohibitivamente costoso. Ceramic permite almacenar estos documentos JSON ricos "off-chain" en una red descentralizada, manteniendo la verificabilidad.

**Propiedad por DID**: Los datos se organizan en "streams" donde cada uno es propiedad de un DID. Solo el usuario que controla la clave privada puede firmar actualizaciones.

**Composabilidad**: Los datos en Ceramic son interoperables y públicos por defecto (aunque pueden encriptarse), permitiendo que múltiples dApps lean el mismo perfil o grafo social del usuario, rompiendo los silos de datos.

### Decentralized Web Nodes (DWNs)

El estándar de [Decentralized Web Nodes (DWNs)](https://identity.foundation/decentralized-web-node/spec/), impulsado principalmente por [TBD](https://www.tbd.website/) y la Decentralized Identity Foundation, ofrece una aproximación alternativa enfocada en la privacidad y la soberanía personal total.

Un DWN es un almacén de datos personales que pertenece exclusivamente al usuario (como un "servidor personal" pero estandarizado). A diferencia de una red global pública como Ceramic, los DWNs están diseñados para ser privados por defecto. Un usuario puede tener múltiples réplicas de su DWN (en su teléfono, en su laptop, y en un servicio en la nube encriptado) que se sincronizan automáticamente.

Las aplicaciones piden permiso para escribir o leer datos específicos en el DWN del usuario. Es la arquitectura base de lo que algunos denominan **[Web5](https://blog.hausera.io/web5-que-es-y-como-transformara-la-tecnologia-iac/)**: una web donde las aplicaciones no tienen base de datos propia de usuarios, sino que actúan como interfaces que interactúan con el DWN soberano de cada persona.

En la práctica, Ceramic es la opción productiva hoy para dApps que necesitan esta capa de almacenamiento mutable descentralizado. Los DWNs son una apuesta de arquitectura a más largo plazo, con adopción aún emergente; conviene conocerlos para entender hacia dónde apunta la soberanía de datos, pero no son una dependencia que debas evaluar para la mayoría de proyectos en 2026.

## Cuándo usar VCs, Attestation Layer, SBTs o POAPs

La elección entre estas primitivas no responde a una jerarquía de superioridad técnica, sino a tres preguntas concretas que deben plantearse siempre en el contexto del problema que se quiere resolver: ¿quién necesita ver los datos?, ¿dónde debe residir la fuente de verdad?, y ¿qué experiencia espera quien porta la credencial?

**Verifiable Credentials (W3C)**:

Las VCs son la elección natural cuando los datos son sensibles y el control debe permanecer exclusivamente en manos del usuario. Su ventaja fundamental es que los datos viajan con la persona, no están expuestos en la blockchain: el titular guarda la credencial en su wallet compatible con el estándar W3C —o en un Decentralized Web Node (DWN), el almacén de datos personal soberano descrito en la sección anterior— y la presenta de forma selectiva a quien necesita verificarla. Esta arquitectura es la adecuada para probar la mayoría de edad sin revelar la fecha exacta de nacimiento mediante ZK-proofs selectivos, acreditar títulos educativos sin exponer el expediente completo, o cumplir requisitos de compliance demostrando atributos como "pasé KYC" o "no estoy en lista de sanciones" sin revelar la identidad de fondo. El coste de esta privacidad es complejidad técnica: requieren una wallet que entienda el estándar W3C (no cualquier wallet Ethereum), flujos de emisión y presentación más elaborados, e infraestructura de emisor que firme las credenciales de forma verificable.

**Attestation Layer (EAS)**:

EAS es el instrumento adecuado cuando necesitas reputación que otros protocolos o contratos inteligentes puedan consumir directamente, sin intermediarios ni acuerdos previos. A diferencia de lo que a veces se simplifica, EAS no es exclusivamente público: tiene dos modalidades complementarias. Las atestaciones on-chain quedan registradas públicamente en el contrato de la red correspondiente y son perfectas para alimentar lógica de contratos —un protocolo DeFi que pondera votos según historial de gobernanza, una dApp que desbloquea funcionalidades según nivel de reputación—; la composabilidad es máxima porque cualquier contrato puede leerlas sin coste adicional de integración. Las atestaciones off-chain son payloads JSON firmados por el emisor que el usuario porta y presenta al frontend —o incluye como dato en una transacción cuando la verificación debe ocurrir on-chain—, con la misma portabilidad práctica que una VC pero sin el ecosistema de gestión que el estándar W3C requiere. Esta modalidad off-chain resuelve casos donde la privacidad importa pero donde tampoco se necesita la infraestructura completa de credenciales verificables. Dado que EAS está desplegado con contratos idénticos en Mainnet, Optimism, Base y Arbitrum, funciona como el idioma común de la reputación interoperable: cualquier emisor puede escribir en el registro y cualquier contrato puede leer sin negociación previa.

**Soulbound Tokens (SBTs)**:

Los SBTs tienen sentido cuando el objetivo es la visibilidad social permanente de un logro significativo. Al ser NFTs intransferibles, aparecen en wallets con soporte de NFTs como Rainbow y en herramientas de gobernanza, lo que los hace adecuados para diplomas universitarios, medallas de gobernanza o acreditaciones de membresía activa que el usuario quiere mostrar como parte de su identidad pública. Su valor reside en esa dimensión exhibitiva: no son credenciales para presentar selectivamente ante un verificador, sino insignias persistentes que forman la identidad visible de una dirección. La contrapartida es que son difíciles de revocar o actualizar una vez emitidos —el soporte de revocación existe en algunas implementaciones pero no está estandarizado— y, al vivir on-chain, toda la información que contienen es pública sin excepciones.

**POAPs**:

Los [POAPs](https://poap.xyz/) son técnicamente NFTs transferibles, pero en la práctica el ecosistema los trata como SBTs de facto: nadie los transfiere porque hacerlo destruiría su significado como prueba de presencia o participación en un momento concreto. La distinción práctica respecto a los SBTs es de granularidad y temporalidad: mientras un SBT tiende a representar un logro duradero y de peso —un título, una membresía activa en una DAO—, un POAP documenta un evento específico en el tiempo: haber asistido a una conferencia, participado en una sesión de gobernanza, completado un tutorial en una fecha determinada. Esta granularidad los convierte en la primitiva más natural para construir historial de participación acumulativo, que sistemas como Gitcoin Passport ya consumen como señal de reputación entre sus stamps.

**Resumen**:

La forma más directa de elegir es partir del consumidor final. Si la consume un humano que debe acceder a un dato privado, las VCs son la herramienta correcta. Si la consume un smart contract que necesita actuar automáticamente, las atestaciones EAS on-chain son la elección obvia. Si nadie la consume activamente sino que existe para ser vista en el perfil del usuario, los SBTs son adecuados para logros de peso y los POAPs para momentos concretos de participación. Y cuando el usuario necesita portar datos off-chain con portabilidad y sin coste de gas, las atestaciones EAS off-chain cubren ese espacio intermedio entre la complejidad del estándar W3C y la permanencia de los registros on-chain.

## Referencias

### Estándares W3C e identidad autosoberana

- [Self-Sovereign Identity — Wikipedia](https://en.wikipedia.org/wiki/Self-sovereign_identity)
- [The Path to Self-Sovereign Identity — Christopher Allen](https://www.lifewithalacrity.com/article/the-path-to-self-sovereign-identity/)
- [Identidad descentralizada — Ethereum Foundation](https://ethereum.org/es/decentralized-identity/)
- [Decentralized Society: Finding Web3's Soul — Buterin, Weyl, Ohlhaver (SSRN)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763)
- [eIDAS 2.0 — Comisión Europea](https://digital-strategy.ec.europa.eu/en/policies/eidas-regulation)
- [European Digital Identity Wallet (EUDI Wallet)](https://digital-strategy.ec.europa.eu/es/factpages/european-digital-identity-wallet)
- [5th Anti-Money Laundering Directive (5AMLD) — EUR-Lex](https://eur-lex.europa.eu/eli/dir/2018/843/oj)
- [Bank Secrecy Act — FinCEN](https://www.fincen.gov/resources/statutes-and-regulations/bank-secrecy-act)
- [Know Your Customer (KYC) — Wikipedia](https://en.wikipedia.org/wiki/Know_your_customer)

### Casos de identidad descentralizada gubernamental

- [National Digital Identity (NDI) — Bután](https://www.bhutanndi.com/)
- [QuarkID — Buenos Aires](https://www.digitalpublicgoods.net/r/quarkid)

### Autenticación y acceso

- [Sign-In with Ethereum (SIWE) — especificación oficial](https://login.xyz/)
- [EIP-1271: Standard Signature Validation for Contracts](https://eips.ethereum.org/EIPS/eip-1271)
- [CAIP-122: Sign-In with X — Chain Agnostic](https://github.com/ChainAgnostic/CAIPs/blob/main/CAIPs/caip-122.md)
- [OpenID Connect (OIDC)](https://openid.net/connect/)
- [OpenID4VC — OpenID for Verifiable Credentials](https://openid.net/sg/openid4vc/)
- [OAuth 2.0](https://oauth.net/2/)
- [SAML — Wikipedia](https://en.wikipedia.org/wiki/Security_Assertion_Markup_Language)
- [Siloed identity — modelos de identidad digital](https://medium.com/evernym/the-three-models-of-digital-identity-relationships-ca0727cb5186)

### Modelos de identidad en Ethereum

- [EOA (Externally Owned Account) — Binance Academy](https://www.binance.com/es/academy/glossary/externally-owned-account-eoa)
- [Ethereum Attestation Service (EAS)](https://attest.org/)
- [Privado ID (anteriormente Polygon ID)](https://www.privado.id/)
- [Fractal ID — emisor de VCs para KYC](https://www.fractal.id/)
- [Civic — verificación de identidad](https://www.civic.com/)

### Proof of Personhood

- [Worldcoin / World ID](https://world.org/world-id)
- [World Chain — L2 de Worldcoin](https://world.org/world-chain)
- [Semaphore — protocolo ZK de Worldcoin](https://semaphore.appliedzkp.org/)
- [Proof of Humanity](https://www.proofofhumanity.id/)
- [Gitcoin Passport](https://passport.gitcoin.co/)
- [BrightID](https://www.brightid.org/)
- [The Sybil Attack — Microsoft Research](https://www.microsoft.com/en-us/research/publication/the-sybil-attack/)

### Nombres descentralizados

- [Ethereum Name Service (ENS)](https://ens.domains/)
- [ENS — documentación del protocolo](https://docs.ens.domains/learn/protocol/)
- [Unstoppable Domains](https://unstoppabledomains.com/)
- [Namecoin](https://www.namecoin.org/)
- [DNS — Cloudflare](https://www.cloudflare.com/learning/dns/what-is-dns/)
- [NFT Profile Pictures (PFP) — Tangem Glossary](https://tangem.com/es/glossary/pfp/)

### Almacenamiento descentralizado de identidad

- [Ceramic Network](https://ceramic.network/)
- [Decentralized Web Nodes (DWNs) — DIF](https://identity.foundation/decentralized-web-node/spec/)
- [IPFS](https://ipfs.tech/)

### Protocolos sociales y reputación

- [Lens Protocol](https://www.lens.xyz/)
- [Farcaster](https://www.farcaster.xyz/)
- [Sismo — ZK-proofs de identidad agregada](https://sismo.io/)
- [Zero-Knowledge Proofs — Ethereum Foundation](https://ethereum.org/en/zero-knowledge-proofs/)

---
