
# Identidad Web3




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


----

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

