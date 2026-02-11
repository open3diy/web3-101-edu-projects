
# Identidad Web3


## Attestation Layer: la capa de verificación on-chain











**Proof of Humanity: registro on-chain público**:

[Proof of Humanity](https://www.proofofhumanity.id/) funciona técnicamente como un Token Curated Registry que vive directamente en un smart contract de Ethereum. Es una lista pública de humanos verificados, por lo que la credencial no es un archivo privado en posesión del usuario, sino su presencia activa en este registro on-chain. Esto constituye una atestación pública permanente. Para ser incluido, el usuario debe subir un video público, depositar una garantía económica (stake) y obtener avales de otros miembros ya registrados.

**BrightID: grafo social off-chain y credenciales**:

[BrightID](https://www.brightid.org/) tiene una arquitectura fundamentalmente diferente, ya que no es una blockchain, sino una red de nodos peer-to-peer que mantienen un grafo social. Técnicamente actúa como un oráculo de unicidad descentralizado.

A diferencia de un registro público, BrightID analiza la estructura de las conexiones sociales para detectar bots. Cuando un usuario es verificado tras participar en videollamadas grupales, la red emite una firma criptográfica que funciona técnicamente como una Verifiable Credential (VC). El usuario presenta esta credencial a las aplicaciones para probar que es único sin revelar quiénes son sus amigos ni exponer su grafo social públicamente. Mientras Proof of Humanity es una lista pública on-chain, BrightID es un generador de pruebas de unicidad off-chain que preserva la privacidad del grafo social.

**El trilema de Proof of Personhood**:

Cada sistema de Proof of Personhood enfrenta un trilema fundamental entre descentralización, privacidad y resistencia Sybil. Esta diversidad de implementaciones permite a los desarrolladores elegir la herramienta adecuada. Si necesitas privacidad absoluta para una votación política, Worldcoin con sus pruebas de conocimiento cero es la opción. Si necesitas filtrar bots en una distribución de tokens sin fricción biométrica, Gitcoin Passport y su sistema de reputación agregada es más adecuado. Cada solución hace compromisos diferentes entre estos tres pilares fundamentales.


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