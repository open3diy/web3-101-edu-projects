# Protocolos DID: Arquitectura Técnica de Identidad Descentralizada

> 🚧 Documento en construcción...

Este documento profundiza en la arquitectura de identidad descentralizada: los estándares [W3C DID Core](https://www.w3.org/TR/did-core/), Verifiable Credentials y Verifiable Presentations, los modelos de delegación, y la coexistencia con marcos regulados como eIDAS 2.0. Complementa la introducción conceptual de [7-1-identity.md](../../101/7-1-identity.md).

## Identidad autosoberana: el nuevo paradigma

[Self-Sovereign Identity (SSI)](https://en.wikipedia.org/wiki/Self-sovereign_identity), o identidad autosoberana. Este principio establece que los individuos deben tener control completo sobre sus credenciales, datos personales y cómo se comparten, sin depender de autoridades centrales para validación o almacenamiento. El término fue popularizado en el artículo [The Path to Self-Sovereign Identity](https://www.lifewithalacrity.com/article/the-path-to-self-sovereign-identity/) de Christopher Allen.

[W3C](https://www.w3.org/) (World Wide Web Consortium), el organismo internacional que desarrolla estándares web abiertos, definió formalmente los estándares que materializan SSI como solución técnica: [Decentralized Identifiers (DIDs)](https://www.w3.org/TR/did-core/), [Verifiable Credentials (VCs)](https://www.w3.org/TR/vc-data-model/) y [Verifiable Presentations (VPs)](https://www.w3.org/TR/vc-data-model/#presentations). Resumiendo: el DID es el identificador, el método define dónde se registra, la VC es el documento acreditativo que custodias y la VP es la evidencia que presentas ante un verificador.

Tanto Web3 como eIDAS con la EUDI Wallet están abrazando esta idea, cada uno desde su filosofía: Web3 con su enfoque permissionless donde la confianza es criptográfica y emergente, y eIDAS domesticando la descentralización bajo soberanía estatal. En la práctica, ambos reconocen que la wallet actúa como tu identidad base donde viven las VCs, y ambos admiten el uso de Zero-Knowledge Proofs para evitar revelar más información de la necesaria.

### DPKI y DID: Los cimientos de la identidad autosoberana

A diferencia de la infraestructura tradicional de clave pública ([PKI](https://en.wikipedia.org/wiki/Public_key_infrastructure)), donde dependemos de autoridades centrales llamadas Certificate Authorities (CAs) para validar y certificar las claves públicas de otros, surge el concepto de Decentralized Public Key Infrastructure (DPKI). En DPKI, no necesitas que una autoridad central certifique que una clave pública pertenece a alguien específico; en su lugar, por ejemplo en el caso de web3, la blockchain actúa como un registro público e inmutable donde cualquiera puede publicar y verificar asociaciones entre identificadores y claves públicas sin intermediarios.

El estándar DID de W3C es la implementación fundamental para construir sistemas DPKI, aunque conviene aclarar que W3C no lo definió exclusivamente con ese fin: también es la base técnica de las EUDI Wallets de eIDAS. El estándar contempla la sintaxis (DID Syntax), la estructura del documento de identidad (DID Document), los métodos de implementación (DID Methods) y el proceso de resolución (DID Resolution), además del modelo de datos y las relaciones de verificación que puedes consultar en detalle en el [estándar W3C DID Core](https://www.w3.org/TR/did-core/).

**DID Syntax**:

DID Syntax es el Formato URI (Identificador Único).

Para que todos hablemos el mismo lenguaje, cada DID sigue una estructura fija: `did:metodo:identificador_unico`.

El método indica dónde reside el ID (puede ser en la red de Ethereum, como `did:ethr:0x123`, en Bitcoin o incluso en una base de datos de Google si ellos implementan el estándar).

El identificador suele ser una cadena alfanumérica única que representa al sujeto (tú), pero que no revela quién eres por sí misma.

**DID Methods: la infraestructura que lo implementa**:

Los métodos son la infraestructura concreta que implementa el estándar DID. Por ejemplo, `did:ethr` utiliza la propia red Ethereum L1 para alojar los DID Documents mediante smart contracts.

W3C mantiene un [registro oficial de métodos DID](https://www.w3.org/TR/did-spec-registries/) que forman parte de la implementación. Este registro, gestionado mediante pull requests en GitHub, representa uno de los pocos aspectos centralizados del ecosistema: la documentación formal sobre qué métodos existen y cómo funcionan. Cualquiera puede implementar un método sin necesidad de aprobación para usarlo, aunque es cierto que deberá pasar los requisitos técnicos para ser aceptado su pull request.

Los DIDs pueden implementarse de múltiples formas, cada una con trade-offs entre descentralización, costo y funcionalidad. Existen métodos que usan Ethereum como registro (`did:ethr`), métodos puramente criptográficos sin registro alguno (`did:key`), métodos que aprovechan infraestructura web tradicional (`did:web`), métodos de Capa 2 sobre Bitcoin (`did:ion`), y métodos que convierten direcciones blockchain existentes en DIDs sin infraestructura adicional (`did:pkh` para Public Key Hash).

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

Este documento no guarda identidades personales como tu nombre o email, solo la infraestructura criptográfica que permite verificar que tú eres quien dices ser. Una ventaja importante de esta separación es la rotación de claves: si una clave privada se ve comprometida, actualizas el DID Document con una nueva y tu identidad —con toda su reputación e historial— permanece intacta, algo imposible en sistemas tradicionales donde comprometer una credencial obliga a reconstruirla desde cero.

### Las Verifiable Credentials (VCs)

W3C define de forma complementaria el estándar de [Verifiable Credentials](https://www.w3.org/TR/vc-data-model/), un modelo de datos para credenciales verificables que los emisores pueden emitir y que otros pueden validar criptográficamente usando los DID Documents de los actores involucrados.

En esencia, las VCs son documentos en formato JSON que contienen afirmaciones o claims sobre un sujeto, emitidos por una entidad y firmados digitalmente. El emisor tiene un DID, el sujeto (persona sobre quien se hace la afirmación) tiene un DID, y el verificador puede usar los DID Documents de ambos para validar la autenticidad de la credencial.

Por ejemplo, una VC puede contener cualquier tipo de información: tu email verificado, tu edad, un diploma universitario, una certificación profesional, o tu membresía en una organización. Lo que las hace "verificables" es que están firmadas criptográficamente por el emisor usando su DID, permitiendo que cualquier verificador pueda comprobar matemáticamente su autenticidad consultando el DID Document del emisor, sin necesidad de contactarlo directamente.

Una aclaración: una VC materializa una attestation como un objeto estándar: cuando el emisor da fe (attests) de ciertos atributos del sujeto, esa attestation se concreta en el documento VC estructurado según el estándar W3C, con la firma criptográfica del emisor y los claims específicos sobre el titular.

Estas credenciales viven en tu wallet bajo tu control exclusivo. Tú decides cuándo y a quién mostrarlas. Si pierdes tu wallet, necesitarás solicitar nuevamente estas credenciales a los emisores originales, aunque existen mecanismos de recuperación social y respaldo que pueden ayudar en estos escenarios.

> Aspectos que podrás ver en el documento de [experiencia de usuario](../../101/8-1-user-experience.md).

Las VCs tienen la capacidad de verificación selectiva. Por ejemplo, puedes tener una credencial que contiene tu fecha de nacimiento completa emitida por el gobierno, pero cuando necesites probar que eres mayor de edad para acceder a un servicio, puedes presentar una prueba derivada que solo revela "es mayor de 18 años" sin exponer tu fecha exacta de nacimiento. Esto se logra mediante técnicas criptográficas como [Zero-Knowledge Proofs](https://ethereum.org/en/zero-knowledge-proofs/).

Para las prácticas de diseño que aplican a VCs —confianza en el emisor, semántica temporal de las afirmaciones y mecanismos de revocación en comparación con attestations on-chain— ver [vc-attestation-best-practices.md](vc-attestation-best-practices.md).

### Verifiable Presentations: presentando credenciales selectivamente

Cuando posees Verifiable Credentials en tu wallet, raramente las compartes directamente en su forma completa. En su lugar, creas [Verifiable Presentations (VPs)](https://www.w3.org/TR/vc-data-model/#presentations), un estándar W3C complementario a VCs que define cómo presentar una o más credenciales a un verificador de forma controlada.

Una Verifiable Presentation es un contenedor firmado que agrupa las credenciales que decides revelar para un contexto específico. Si un servicio necesita verificar tu edad y tu membresía en una organización, creas una VP que contiene solo esas dos credenciales, no todas las que posees. La VP está firmada por ti usando tu DID, probando que eres el titular legítimo de esas credenciales y que autorizas explícitamente su presentación en este contexto.

La potencia de las VPs se multiplica con Zero-Knowledge Proofs. Puedes crear una VP que demuestre predicados derivados sin revelar datos subyacentes: "soy mayor de 18 años" sin mostrar tu fecha de nacimiento, "vivo en país permitido" sin revelar tu dirección exacta, "tengo saldo suficiente" sin exponer tu balance completo. El verificador recibe prueba matemática de la afirmación sin acceder a información sensible.

Las VPs también incluyen timestamps y pueden limitarse a verificadores específicos mediante encriptación. Esto previene que una presentación creada para el servicio A sea reutilizada fraudulentamente ante el servicio B. Cada presentación es contextual y firmada específicamente para ese propósito, creando trazabilidad auditada de qué credenciales revelaste, a quién, y cuándo.

### Casos de uso y roles

Las VCs operan mediante un triángulo de confianza de actores con diferente rol, donde emisor, titular y verificador son independientes entre sí. Este desacoplamiento contrasta radicalmente con Web2, donde plataformas como Google o Facebook centralizan estos tres roles: ellas mismas validan tu identidad (emisor), almacenan tus datos en sus servidores (custodia), y verifican tu acceso cada vez que inicias sesión (verificador). En Web3, estos roles están separados criptográficamente: una universidad emite tu credencial, tú la custodias en tu wallet, y un empleador la verifica sin contactar a la universidad porque el ancla de confianza es el propio método, como sería el caso de `did:ethr`.

Los casos de uso fundamentales en el ecosistema de VCs que podemos ver son:

- **Emisor emite credencial verificable a titular**: Una entidad con autoridad certifica atributos del sujeto mediante una credencial firmada digitalmente. Ejemplo: universidad emite diploma académico, gobierno emite certificado de residencia, empresa emite credencial de experiencia laboral
- **Titular custodia credencial en wallet personal**: El sujeto almacena y gestiona sus credenciales bajo control exclusivo sin depender de servidores centralizados. Ejemplo: usuario guarda sus diplomas, certificaciones y credenciales KYC en MetaMask o Privado ID
- **Titular presenta credencial verificable ante verificador**: El titular genera una presentación selectiva de credenciales para demostrar atributos específicos en un contexto determinado. Ejemplo: presentar prueba de edad mayor de 18 sin revelar fecha exacta de nacimiento, demostrar residencia en jurisdicción permitida sin exponer dirección postal completa
- **Verificador valida autenticidad de credencial sin contactar emisor**: Un servicio comprueba criptográficamente la validez de una credencial consultando el DID Document del emisor, sin comunicación directa. Ejemplo: protocolo DeFi verifica credencial KYC para acceso a pool permisionado, plataforma de gobernanza valida membresía DAO para habilitar votación
- **Titular revoca acceso o presenta credencial con restricciones temporales**: El titular controla cuándo y a quién muestra sus credenciales, pudiendo limitar presentaciones por tiempo, contexto o verificador específico. Ejemplo: autorizar acceso a credencial educativa solo durante enero 2026 y únicamente para verificadores universitarios
- **Titular agrega credenciales de múltiples emisores en presentación única**: El sujeto combina credenciales de diferentes fuentes para contextos que requieren validación multidimensional. Ejemplo: presentar simultáneamente reputación de DAO A, certificación de protocolo B e historial profesional de empresa C ante un potencial empleador

**Delegación de identidad y autorización**:

Después de ver varios casos de uso, tenemos que destacar otro importante, habilitado por las VPs: la delegación de identidad y autorización.

Más allá de presentar tus propias credenciales, frecuentemente necesitas permitir que otros actúen en tu nombre sin entregarles control total. Esto se logra mediante [Authorization Capabilities (ZCAP)](https://w3c-ccg.github.io/zcap-spec/), una especificación del [W3C Credentials Community Group](https://w3c-ccg.github.io/) que define tokens criptográficos firmados que otorgan permisos específicos a un DID delegado. Basándose en el modelo de [Object Capabilities (OCAP)](https://en.wikipedia.org/wiki/Object-capability_model), las capabilities funcionan bajo el principio de "quien posee el token, tiene el permiso" (bearer token): son verificables criptográficamente sin necesidad de coordinación centralizada, a diferencia de sistemas tradicionales donde la autorización se verifica consultando bases de datos centrales de permisos.

Las capabilities permiten permisos descentralizados granulares con restricciones precisas: puedes autorizar que alguien presente tu credencial educativa solo durante enero 2026 y solo a verificadores universitarios, o que un representante vote en tu nombre en una DAO solo para propuestas de categoría "tesorería". Estas autorizaciones son revocables instantáneamente sin cambiar tus credenciales subyacentes.

Además existen las **jerarquías de autoridad descentralizadas** que son fundamentales para identidad corporativa. Una organización posee un DID corporativo raíz que representa la entidad legal, y emite capabilities derivadas a empleados para actuar en representación corporativa dentro de límites específicos. Un empleado de ventas recibe autorización para firmar contratos hasta $50,000, un contador recibe permisos para presentar credenciales financieras corporativas ante auditores. Cada nivel de delegación añade restricciones adicionales creando cadenas de autoridad verificables: empleado X actuó bajo autoridad Y otorgada por ejecutivo Z, todo auditable on-chain sin sistemas centralizados.

### DIDs corporativas: identidad organizacional on-chain

Mientras que los DIDs personales representan individuos con control soberano sobre sus credenciales, los DIDs corporativas modelan entidades colectivas donde la autoridad debe distribuirse entre múltiples actores según roles y jerarquías organizacionales. Este problema no es trivial: una organización no es una persona con una clave privada única, sino una estructura legal que requiere mecanismos de gobernanza para decisiones críticas, procesos de actualización de autoridades cuando cambia el personal, y trazabilidad auditable de quién actuó en nombre de la organización en cada momento.

La importancia de este tema radica en que Web3 está presenciando una convergencia entre estructuras organizacionales tradicionales y nativas digitales. Las empresas tradicionales necesitan operar on-chain para interactuar con protocolos DeFi, emitir credenciales verificables a empleados, y representarse ante reguladores. Paralelamente, las DAOs nativas de Web3 necesitan interfaces con el mundo legal tradicional para abrir cuentas bancarias, firmar contratos con proveedores, y establecer responsabilidad legal ante terceros. Los DIDs corporativas son el puente técnico que permite a ambos tipos de entidades operar en el ecosistema de identidad descentralizada.

**Gobernanza de DIDs organizacionales**:

La diferencia fundamental entre un DID personal y uno corporativo reside en el modelo de control de claves. Un individuo custodia su clave privada y tiene autoridad exclusiva para firmar en su propio nombre. Una organización, en cambio, debe distribuir la autoridad entre múltiples firmantes cuya composición cambia con el tiempo, sin que la identidad persistente de la organización se vea comprometida cuando alguien abandona su rol.

El modelo técnico más extendido para implementar esta gobernanza es el [multisig](https://ethereum.org/en/developers/docs/smart-contracts/security/#use-multisig-wallets), donde el DID Document de la organización especifica un threshold scheme: se requieren M de N firmas válidas para ejecutar acciones en nombre de la entidad. Por ejemplo, el DID corporativo de una startup puede configurarse como 2-de-3, requiriendo que dos de sus tres fundadores firmen cualquier credencial emitida por la empresa o autorización delegada a empleados. Esta configuración se registra en el DID Document mediante el campo `authentication`, que lista las claves públicas autorizadas y el umbral requerido.

Cuando la composición del equipo ejecutivo cambia, la organización actualiza su DID Document sin cambiar el identificador raíz. Si uno de los fundadores abandona la empresa, se publica una actualización que elimina su clave pública del conjunto de firmantes autorizados y añade la del nuevo ejecutivo. El DID `did:ethr:0x789corporate` permanece constante mientras su DID Document evoluciona, preservando la identidad corporativa y su reputación acumulada. Este proceso de rotación es crítico: sin él, un empleado despedido mantendría capacidad técnica de firmar en nombre de la organización indefinidamente.

Las organizaciones más sofisticadas implementan gobernanza graduada mediante roles con diferentes umbrales de autoridad. Las decisiones operacionales rutinarias pueden requerir solo la firma del director ejecutivo (1-de-1), mientras que acciones críticas como modificar el propio DID Document corporativo o emitir credenciales financieras auditadas requieren consenso del consejo completo (3-de-5). Esta jerarquía se codifica en el DID Document mediante múltiples entradas en `verificationMethod`, cada una asociada a contextos específicos de uso.

**Arquitectura técnica: delegación en cascada**:

La infraestructura de DIDs corporativas opera mediante un modelo de delegación en cascada donde la autoridad fluye desde el DID raíz organizacional hacia DIDs individuales de empleados, cada uno con permisos acotados que expiran automáticamente o pueden revocarse instantáneamente. Este diseño permite escalar la operación sin requerir que el multisig corporativo firme cada acción individual.

Consideremos el caso concreto de una empresa de auditoría blockchain. La entidad posee el DID raíz `did:ethr:0xAuditCorp`, controlado mediante un multisig 3-de-5 de sus socios. Cuando contratan a un auditor junior, no le entregan acceso directo a las claves del multisig corporativo (eso sería inseguro), sino que el multisig emite una [Authorization Capability (ZCAP)](https://w3c-ccg.github.io/zcap-spec/) firmada que delega al DID personal del empleado `did:ethr:0xAuditorJunior` permisos específicos: puede emitir credenciales de tipo "informe preliminar de auditoría" con validez máxima de 90 días, pero no puede emitir el dictamen final de auditoría (que requiere firma de un socio senior).

Esta capability es un documento JSON firmado criptográficamente que incluye restricciones temporales, de alcance y de contexto. Cuando el auditor junior presenta un informe a un cliente, entrega tanto su credencial (firmada con su DID personal) como la cadena de autorización que prueba su mandato: el informe está firmado por `did:ethr:0xAuditorJunior`, que actúa bajo capability emitida por `did:ethr:0xAuditCorp`, cuyo DID Document contiene las claves públicas del multisig que firmó originalmente la delegación. El verificador valida toda la cadena criptográficamente sin contactar a la empresa.

Si el empleado es despedido o su rol cambia, la empresa revoca la capability publicando su hash en una lista de revocación on-chain asociada al DID corporativo. A partir de ese momento, cualquier verificador que consulte la lista detecta que esa autorización ya no es válida, sin necesidad de contactar a la empresa directamente. El DID personal del exempleado sigue existiendo (es su identidad soberana), pero ya no puede actuar en representación corporativa.

**Interoperabilidad legal: el puente entre Web3 y estructuras tradicionales**:

Una de las tensiones más interesantes en el ecosistema de DIDs corporativas es la necesidad de establecer vínculos verificables entre identidades on-chain y entidades legales off-chain. Una DAO puede tener un DID `did:ethr:0xDAO123` controlado por su tesorería multisig, pero para abrir una cuenta bancaria en el mundo tradicional, necesita demostrar que ese DID representa legalmente a la entidad XYZ LLC registrada en Delaware.

La solución técnica emergente implica servicios de "ancla legal" (legal anchoring) donde proveedores especializados actúan como puentes verificables entre registros corporativos tradicionales y DIDs on-chain. [GLEIF (Global Legal Entity Identifier Foundation)](https://www.gleif.org/), la organización que administra el sistema global de identificadores de entidades legales (LEI), está desarrollando [vLEI (verifiable LEI)](https://www.gleif.org/en/lei-solutions/gleifs-vision-for-digital-trust-the-vlei), una credencial verificable que asocia un DID con un LEI oficial. Una empresa que posee el LEI 5493001KJTIIGC8Y1R12 puede solicitar un vLEI que certifica criptográficamente: "el DID did:ethr:0xCompany está legalmente controlado por la entidad con LEI 5493001KJTIIGC8Y1R12".

Este vLEI actúa como credencial verificable emitida por GLEIF (una autoridad reconocida globalmente) que el DID corporativo puede presentar cuando opera en contextos que requieren validación legal. Un banco que recibe una solicitud firmada con `did:ethr:0xCompany` puede verificar el vLEI y confirmar ante su departamento de compliance que ese DID representa legalmente a una LLC registrada, sin requerir documentación en papel ni procesos centralizados de verificación. Esta interoperabilidad es fundamental para la adopción empresarial: las organizaciones no abandonarán estructuras legales tradicionales, pero necesitan poder operar on-chain manteniendo su identidad legal reconocible.

**Casos de uso en Web3: DAOs, tesorerías y compliance**:

Las aplicaciones prácticas de DIDs corporativas en el ecosistema Web3 abarcan desde gobernanza organizacional hasta cumplimiento regulatorio en protocolos financieros.

Un caso paradigmático son las tesorerías de DAOs implementadas mediante [Gnosis Safe](https://safe.global/), el estándar de facto para multisig en Ethereum. Una DAO puede asociar su tesorería multisig con un DID corporativo que representa la organización completa, permitiendo que la tesorería no solo controle fondos sino también emita credenciales verificables. La DAO podría emitir credenciales de membresía activa a sus contribuidores, credenciales de rol específico (desarrollador core, moderador de gobernanza, tesorero), o credenciales temporales de delegación de voto. Todas estas credenciales están firmadas por el DID corporativo de la DAO, cuyas claves son controladas por el multisig de la tesorería, creando un sistema de reputación e identidad verificable sin servidores centralizados.

En el ámbito DeFi, los protocolos que operan bajo regulación AML/CTF deben verificar que sus usuarios no son entidades sancionadas ni residen en jurisdicciones prohibidas. Tradicionalmente esto requiere procesos KYC centralizados que recolectan datos personales. Con DIDs corporativas, emergen modelos alternativos: empresas especializadas en verificación (como [Fractal ID](https://web.fractal.id/) o [Coinbase Onchain Verifications](https://www.coinbase.com/onchain-verify)) emiten credenciales corporativas que certifican "esta entidad completó verificación AML nivel X" sin revelar los datos subyacentes. Un protocolo puede requerir que solo DIDs con credenciales válidas de proveedores reconocidos accedan a pools específicos, delegando la verificación legal a emisores especializados mientras mantiene decisiones de acceso on-chain.

Otro caso relevante es la emisión de credenciales educativas o profesionales por instituciones que mantienen identidad legal tradicional pero operan en Web3. Una universidad puede registrar un DID corporativo vinculado a su LEI oficial (verificable mediante vLEI), y emitir diplomas como credenciales verificables firmadas con ese DID. Los empleadores que reciben estas credenciales verifican criptográficamente tanto la autenticidad del diploma (firma válida) como la legitimidad del emisor (el DID está ancladolegalmente a la universidad X mediante vLEI emitido por GLEIF). Esta infraestructura elimina fraudes de credenciales falsas: no puedes forjar el diploma de una universidad sin poseer las claves privadas de su DID corporativo multisig.

**DAOs vs empresas tradicionales: convergencia y divergencia**:

Aunque tanto las DAOs nativas de Web3 como las empresas tradicionales que operan on-chain utilizan DIDs corporativas, existen diferencias filosóficas y técnicas importantes en cómo implementan gobernanza e identidad.

Las DAOs típicamente implementan gobernanza mediante lógica programática verificable on-chain: los token holders votan propuestas, y la ejecución ocurre automáticamente si se alcanza el quorum. El DID de la DAO puede estar controlado por un contrato de gobernanza donde el multisig no tiene discrecionalidad absoluta, sino que debe actuar según lo que dictaminen las votaciones on-chain. Esta gobernanza es transparente y auditable: cualquiera puede verificar qué propuestas se aprobaron y cómo votó cada participante. El DID corporativo de la DAO materializa esta autoridad colectiva emergente en un identificador que puede operar en sistemas de identidad descentralizada.

Las empresas tradicionales, en cambio, suelen mantener estructuras de autoridad jerárquicas off-chain (consejo de administración, CEO, directores) que operan bajo marcos legales nacionales. Su DID corporativo está controlado por un multisig, pero las decisiones sobre qué firmar con ese multisig se toman mediante procesos internos que no están codificados on-chain. La transparencia es limitada: solo los firmantes autorizados conocen las deliberaciones internas que llevaron a emitir determinada credencial corporativa. Sin embargo, esto también otorga flexibilidad: la empresa puede adaptar sus procesos internos sin actualizar contratos on-chain.

Una zona de convergencia interesante son las empresas que están adoptando prácticas de governance descentralizada, no por ideología sino por eficiencia operacional. Cuando una corporación multinacional necesita coordinar autorizaciones entre equipos distribuidos globalmente, implementar un sistema de DIDs corporativas con delegación en cascada simplifica dramáticamente la burocracia: los gerentes regionales reciben capabilities temporales para emitir credenciales de empleado válidas en su jurisdicción, sin requerir aprobación del headquarters para cada contratación. La trazabilidad on-chain además facilita auditorías de compliance, porque puedes demostrar criptográficamente qué autoridad específica emitió cada credencial, cuándo, y bajo qué mandato.

Finalmente, existe un espacio emergente de **entidades híbridas**: DAOs que establecen vehículos legales tradicionales (LLC, fundaciones suizas) para interactuar con el mundo regulado, pero mantienen gobernanza on-chain. El DID corporativo de estas entidades puede tener un componente dual: el DID legal vinculado al LEI de la fundación para interacciones reguladas, y un DID operacional controlado por la gobernanza on-chain de la DAO para operaciones dentro del ecosistema Web3. Estas estructuras están explorando cómo mantener soberanía descentralizada mientras cumplen con obligaciones legales en jurisdicciones específicas.

### El ecosistema Web3 de VC: Emisores, Titulares y Verificadores

El ecosistema de identity Web3 ha desarrollado varias implementaciones de VCs o credenciales verificables, en muchos casos con privacidad mediante Zero-Knowledge Proofs. Las veremos en [9-1-ecosystem-DApps](../../101/9-1-ecosystem-DApps.md), aunque aquí veremos las fundamentales.

**Emisores (Issuers)**:

Entidades que validan y certifican información. Una universidad verifica que completaste tu grado, un gobierno confirma tu ciudadanía, una empresa atestigua tu experiencia laboral. Tras validar, emiten la credencial firmada con su DID.

La pregunta de fondo es: ¿quién puede ser emisor y qué nivel de confianza merece esa credencial? Aquí es donde Web3 y eIDAS 2.0 divergen radicalmente en su filosofía.

En el modelo permissionless de Web3, cualquier entidad puede emitir credenciales sin necesitar autorización de nadie. La confianza es emergente y reputacional: confías en una credencial porque confías en quien la firmó, no porque el Estado haya acreditado a ese emisor. Un protocolo DeFi puede decidir aceptar credenciales KYC de [Fractal ID](https://web.fractal.id/) o [Civic](https://www.civic.com/) porque la industria se ha puesto de acuerdo en considerar esas fuentes fiables, no porque ningún gobierno lo haya impuesto. Del mismo modo, una DAO puede emitir credenciales de membresía que otros protocolos reconocen voluntariamente.

eIDAS 2.0 adopta el enfoque contrario: establece una jerarquía formal de emisores regulada por el Estado. En la cúspide se sitúan los [Qualified Trust Service Providers (QTSPs)](https://digital-strategy.ec.europa.eu/en/policies/eudi-wallet-implementation), entidades acreditadas oficialmente por los Estados miembros y supervisadas por organismos nacionales de supervisión. Solo los QTSPs pueden emitir los dos tipos de credenciales de mayor peso legal: los PID (Person Identification Data, como el DNI digital) los emiten exclusivamente los Estados, mientras que las QEAA (Qualified Electronic Attestations of Attributes, como un título universitario oficial) pueden emitirlas QTSPs acreditados. Por debajo de este nivel existen los emisores no cualificados, que pueden emitir EAA (Electronic Attestations of Attributes) sin acreditación formal: una empresa privada, una asociación o una plataforma digital puede emitir credenciales válidas técnicamente, pero sin el respaldo legal que otorga la acreditación de QTSP.

Esta distinción tiene consecuencias prácticas importantes. Una credencial QEAA tiene validez legal directa en toda la Unión Europea y puede usarse en procedimientos administrativos con la misma fuerza que el documento físico original. Una EAA no cualificada puede ser útil para servicios privados, pero no tiene ese reconocimiento legal automático. En Web3 esta jerarquía no existe formalmente: la "cualificación" de un emisor es un acuerdo entre protocolos, no un certificado del Estado.

Una zona de convergencia interesante son los emisores híbridos de KYC reutilizable como [Coinbase Onchain Verifications](https://www.coinbase.com/onchain-verify), [Fractal ID](https://web.fractal.id/) o [Civic](https://www.civic.com/). Completas la verificación de identidad legal con ellos (centralizadamente, bajo regulación AML/KYC tradicional), y emiten una VC que prueba "este usuario pasó KYC nivel X" sin revelar tus datos personales en cada interacción. Actúan como emisores de facto reconocidos por la industria web3, aunque sin la acreditación formal QTSP que eIDAS requeriría para considerarlos cualificados.

**Titulares (Holders)**:

El usuario final que recibe y custodia sus credenciales. Las VCs se almacenan en tu dispositivo, no en servidores del emisor ni del verificador. [Privado ID](https://www.privadoid.com/) (anteriormente Polygon ID) ejemplifica la infraestructura del titular: un ecosistema completo de identidad autosoberana que incluye wallet móvil, soporte nativo para ZK-proofs, y herramientas para gestionar credenciales privadamente. El titular decide qué revelar, cuándo y a quién, generando pruebas selectivas según cada contexto.

**Verificadores (Verifiers)**:

Servicios que consumen credenciales sin contactar al emisor. La verificación es puramente criptográfica: consultan el DID Document del emisor para validar la firma, sin comunicación directa. Como ejemplo [Gnosis Safe](https://www.gnosis.io/) implementa verificación mediante módulos que condicionan ejecución de transacciones a posesión de credenciales específicas. Otros verificadores incluyen protocolos DeFi como [Aave Arc](https://aave.com/) que requieren VCs de KYC para acceso a pools permisionados, plataformas de gobernanza como [Snapshot](https://snapshot.org/) que verifican credenciales de membresía para habilitar votación, y marketplaces NFT que verifican credenciales de artista verificado antes de mostrar colecciones destacadas. Igualmente lo podemos ver en protocolos DeFi que verifican cumplimiento regulatorio (sanciones, jurisdicciones prohibidas) antes de permitir operaciones, consumiendo VCs sin acceder a datos personales del usuario.

### Coexistencia centralizado y descentralizado

Más allá de la jerarquía de emisores ya descrita, la convivencia entre Web3 y eIDAS 2.0 presenta otras diferencias estructurales relevantes.

En cuanto a resiliencia, eIDAS 2.0 no impone el uso de ninguna infraestructura concreta: no exige [EBSI (European Blockchain Services Infrastructure)](https://ec.europa.eu/digital-building-blocks/wikis/display/EBSI/Home), la blockchain permisionada europea, ni ninguna otra. Esto significa que los Estados miembros pueden implementar la EUDI Wallet sobre servicios centralizados propios, lo que introduce potenciales puntos únicos de fallo (SPOF) que un sistema de identidad crítico debería evitar. En Web3, la resiliencia es una propiedad de diseño: la ausencia de servidores centrales es estructural, no opcional.

En cuanto a privacidad, eIDAS 2.0 integra las garantías del GDPR (derecho al olvido, consentimiento explícito, portabilidad) que no existen por defecto en implementaciones Web3 puramente descentralizadas. Sin embargo, la privacidad en eIDAS es un derecho regulatorio que el Estado concede y puede modificar; en Web3, la privacidad es una propiedad matemática que nadie puede revocar.

Este contraste no es meramente técnico sino profundamente político. La identidad digital bajo control estatal puede convertirse en un mecanismo donde el acceso a servicios esenciales quede condicionado a criterios que escapan al control del individuo.

**Interoperabilidad y convergencia: el estándar OpenID4VC**:

A pesar de las diferencias filosóficas (centralizado vs descentralizado), existe un área de convergencia técnica significativa. La industria está adoptando masivamente el estándar [OpenID for Verifiable Credentials (OpenID4VC)](https://openid.net/sg/openid4vc/), que permite utilizar los rieles probados de OpenID Connect (la tecnología detrás de "Log in with Google") para el intercambio de credenciales verificables.

Esto significa que tanto la futura [European Digital Identity Wallet (EUDI)](https://digital-strategy.ec.europa.eu/en/policies/eudi-wallet-implementation) como las wallets Web3 nativas (como MetaMask o Privado ID) están convergiendo hacia los mismos protocolos de transporte. Técnicamente, esto podría permitir que una wallet Web3 almacene una credencial oficial del gobierno (siempre que cumpla con los requisitos de seguridad del nivel de garantía) o que una wallet institucional verifique credenciales emitidas por protocolos descentralizados.

Esta adopción de estándares técnicos comunes facilita:

- Interoperabilidad real: credenciales emitidas bajo eIDAS podrían, técnicamente, verificarse en aplicaciones Web3 y viceversa, siempre que se confíe en los emisores.
- Experiencia de usuario unificada: el flujo para recibir una credencial del gobierno o un diploma de una DAO sería idéntico para el usuario (escanear QR o click en link).
- Adopción de mejoras de privacidad: permite integrar técnicas como [Selective Disclosure](https://www.w3.org/TR/vc-data-model/#dfn-selective-disclosure) y [Zero-Knowledge Proofs](https://ethereum.org/en/zero-knowledge-proofs/) sobre infraestructuras existentes.

Sin embargo, es crucial entender que usar los mismos estándares técnicos no elimina la diferencia fundamental de control y gobernanza. Que usen el mismo "lenguaje" técnico no cambia que en el modelo centralizado la raíz de confianza es el Estado (que puede revocarla), mientras que en Web3 la raíz es la criptografía y el consenso descentralizado.

> Es un estándar sin madurar, veremos cómo evoluciona, por lo tanto, tampoco voy a desarrollar mucho este apartado.

## Comunicación y patrones avanzados

Una vez que dos identidades pueden descubrirse y verificarse, necesitan comunicarse. [DIDComm](https://identity.foundation/didcomm-messaging/spec/) es el protocolo estándar para mensajería cifrada de extremo a extremo entre DIDs: garantiza que el mensaje proviene de quien dice ser y que solo el destinatario previsto puede leerlo. Es la base sobre la que se construyen flujos como la presentación de credenciales o la negociación de autorizaciones.

La flexibilidad del sistema permite también modelar estructuras organizativas complejas. Un DID corporativo raíz puede delegar permisos limitados a departamentos o empleados, y las identidades de alto valor —como la tesorería de una DAO— pueden configurarse para requerir múltiples firmas, eliminando puntos únicos de fallo y distribuyendo la confianza entre varias partes.

## Tooling: frameworks para implementar DID/VC

Si quieres construir infraestructura DID/VC sin partir desde cero, el ecosistema dispone de tres frameworks de referencia que abstraen la complejidad de los estándares W3C:

[**Veramo**](https://veramo.io/) es un framework JavaScript/TypeScript con arquitectura de plugins. Permite añadir emisión, verificación y gestión de VCs a cualquier aplicación Node.js o React Native. Su diseño modular permite intercambiar métodos DID, esquemas de credenciales o almacenes de claves sin reescribir la lógica de negocio. Es la opción más flexible para developers que quieren control fino sobre cada capa.

[**walt.id**](https://walt.id/) está orientado a organizaciones que necesitan desplegar infraestructura DID/VC como servicio. Provee tres kits independientes con API REST: Issuer Kit para emitir VCs, Verifier Kit para verificarlas y Wallet Kit para custodiarlas. Es especialmente relevante en el contexto eIDAS/EBSI: gran parte de los proyectos piloto de la Comisión Europea sobre identidad digital lo usan como base de implementación. No es código para integrar en una app, sino infraestructura para desplegar como servicio.

[**SpruceID**](https://www.spruceid.com/) se centra en interoperabilidad de estándares. Su librería `DIDKit`, escrita en Rust con bindings a JavaScript, Python y otros lenguajes, es la implementación de referencia más portable para trabajar con DIDs y VCs en cualquier plataforma. Además, son los autores de la especificación y el paquete [`siwe`](https://www.npmjs.com/package/siwe) (Sign-In with Ethereum), lo que los convierte en un actor central tanto en el mundo DID/VC como en el ecosistema de autenticación Ethereum.

Los tres son agnósticos respecto al stack de aplicación: puedes construir sobre ellos una wallet como PrivadoID, un servicio de KYC como Fractal ID, o la infraestructura de credenciales de un gobierno como QuarkID —que en su caso optó por construir un stack propio sobre ZKSync Era siguiendo los estándares W3C directamente, sin usar ninguno de estos frameworks.

## Referencias y Especificaciones

- [W3C DID Core 1.0](https://www.w3.org/TR/did-core/) - Especificación fundamental
- [DID Method Registry](https://www.w3.org/TR/did-spec-registries/) - Lista oficial de métodos
- [DIDComm Messaging](https://identity.foundation/didcomm-messaging/spec/) - Protocolo de mensajería
- [Universal Resolver](https://github.com/decentralized-identity/universal-resolver) - Implementación de referencia
- [DIF (Decentralized Identity Foundation)](https://identity.foundation/) - Comunidad y grupos de trabajo
- [Mejores prácticas en VC y Attestations](vc-attestation-best-practices.md) - Confianza en emisores, semántica temporal y revocación

---
