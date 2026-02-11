# Protocolos DID: Arquitectura Técnica de Identidad Descentralizada

> 🚧 Este material está en construcción, se deja como referencia pero todavía no ha sido completamente validado en este repositorio de open3diy.

Este documento profundiza en la arquitectura técnica de los Decentralized Identifiers (DIDs) según el estándar [W3C DID Core](https://www.w3.org/TR/did-core/). Aquí encontrarás los detalles de implementación, comparativas entre métodos, y patrones arquitectónicos que complementan la introducción conceptual en [7-1-identity.md](../../101/7-1-identity.md).

## DPKI y DID: Los cimientos de la identidad autosoberana

A diferencia de la infraestructura tradicional de clave pública ([PKI](https://en.wikipedia.org/wiki/Public_key_infrastructure)), donde dependemos de autoridades centrales llamadas Certificate Authorities (CAs) para validar y certificar las claves públicas de otros, surge el concepto de Decentralized Public Key Infrastructure (DPKI). En DPKI, no necesitas que una autoridad central certifique que una clave pública pertenece a alguien específico; en su lugar, por ejemplo en el caso de web3, la blockchain actúa como un registro público e inmutable donde cualquiera puede publicar y verificar asociaciones entre identificadores y claves públicas sin intermediarios.

Como dijimos, la [W3C](https://www.w3.org/) (World Wide Web Consortium), el organismo internacional que desarrolla estándares web abiertos, definió formalmente el estándar de [Decentralized Identifiers (DIDs)](https://www.w3.org/TR/did-core/) que sirve de facto como la implementación fundamental para construir sistemas DPKI. Tenemos que aclarar que W3C define un estándar que es la base de la DPKI, pero no significa que lo definiera con ese fin, de hecho, es también usado en EUDI Wallets.

El estándar contempla desde la sintaxis (DID Syntax), la estructura completa (DID Document), los métodos de implementación (DID Methods) y la resolución (DID Resolution) que explicaremos ahora, pero también se define el modelo de datos y relaciones de verificación para establecer la infraestructura, que puedes revisar en el [estándar W3C DID Core](https://www.w3.org/TR/did-core/).

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

> Aspectos que podrás ver en el documento de [experiencia de usuario](../../101/8-1-user-experience.md).

Las VCs tienen la capacidad de verificación selectiva. Por ejemplo, puedes tener una credencial que contiene tu fecha de nacimiento completa emitida por el gobierno, pero cuando necesites probar que eres mayor de edad para acceder a un servicio, puedes presentar una prueba derivada que solo revela "es mayor de 18 años" sin exponer tu fecha exacta de nacimiento. Esto se logra mediante técnicas criptográficas como [Zero-Knowledge Proofs](https://ethereum.org/en/zero-knowledge-proofs/).

## Verifiable Presentations: presentando credenciales selectivamente

Cuando posees Verifiable Credentials en tu wallet, raramente las compartes directamente en su forma completa. En su lugar, creas [Verifiable Presentations (VPs)](https://www.w3.org/TR/vc-data-model/#presentations), un estándar W3C complementario a VCs que define cómo presentar una o más credenciales a un verificador de forma controlada.

Una Verifiable Presentation es un contenedor firmado que agrupa las credenciales que decides revelar para un contexto específico. Si un servicio necesita verificar tu edad y tu membresía en una organización, creas una VP que contiene solo esas dos credenciales, no todas las que posees. La VP está firmada por ti usando tu DID, probando que eres el titular legítimo de esas credenciales y que autorizas explícitamente su presentación en este contexto.

La potencia de las VPs se multiplica con Zero-Knowledge Proofs. Puedes crear una VP que demuestre predicados derivados sin revelar datos subyacentes: "soy mayor de 18 años" sin mostrar tu fecha de nacimiento, "vivo en país permitido" sin revelar tu dirección exacta, "tengo saldo suficiente" sin exponer tu balance completo. El verificador recibe prueba matemática de la afirmación sin acceder a información sensible.

Las VPs también incluyen timestamps y pueden limitarse a verificadores específicos mediante encriptación. Esto previene que una presentación creada para el servicio A sea reutilizada fraudulentamente ante el servicio B. Cada presentación es contextual y firmada específicamente para ese propósito, creando trazabilidad auditada de qué credenciales revelaste, a quién, y cuándo.

## Casos de uso y roles

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

## El ecosistema Web3 de VC: Emisores, Titulares y Verificadores

El ecosistema de identity Web3 ha desarrollado varias implementaciones de VCs o credenciales verificables, en muchos casos con privacidad mediante Zero-Knowledge Proofs. Las veremos en [9-1-ecosystem-DApps](../../101/9-1-ecosystem-DApps.md), aunque aquí veremos las fundamentales.

**Emisores (Issuers)**:

Entidades que validan y certifican información. Una universidad verifica que completaste tu grado, un gobierno confirma tu ciudadanía, una empresa atestigua tu experiencia laboral. Tras validar, emiten la credencial firmada con su DID. [Fractal ID](https://web.fractal.id/) y [Civic](https://www.civic.com/) operan como emisores KYC especializados: verifican documentos legales o biometría, y emiten VCs que otros servicios pueden consumir sin repetir el proceso.

Como emisores, emergen soluciones híbridas que intentan hacer KYC menos invasivo usando infraestructura descentralizada como herramienta, no como fin. Servicios como [Coinbase Onchain Verifications](https://www.coinbase.com/onchain-verify), o las mencionadas [Fractal ID](https://web.fractal.id/) y [Civic](https://www.civic.com/) operan bajo un modelo de "KYC reutilizable": completas verificación de identidad legal tradicional con ellos (centralizadamente), y luego emiten una credencial verificable que prueba "este usuario pasó KYC nivel X" sin revelar tus datos personales cada vez que interactúas con protocolos.

**Titulares (Holders)**:

El usuario final que recibe y custodia sus credenciales. Las VCs se almacenan en tu dispositivo, no en servidores del emisor ni del verificador. [Privado ID](https://www.privadoid.com/) (anteriormente Polygon ID) ejemplifica la infraestructura del titular: un ecosistema completo de identidad autosoberana que incluye wallet móvil, soporte nativo para ZK-proofs, y herramientas para gestionar credenciales privadamente. El titular decide qué revelar, cuándo y a quién, generando pruebas selectivas según cada contexto.

**Verificadores (Verifiers)**:

Servicios que consumen credenciales sin contactar al emisor. La verificación es puramente criptográfica: consultan el DID Document del emisor para validar la firma, sin comunicación directa. Como ejemplo [Gnosis Safe](https://www.gnosis.io/) implementa verificación mediante módulos que condicionan ejecución de transacciones a posesión de credenciales específicas. Otros verificadores incluyen protocolos DeFi como [Aave Arc](https://aave.com/) que requieren VCs de KYC para acceso a pools permisionados, plataformas de gobernanza como [Snapshot](https://snapshot.org/) que verifican credenciales de membresía para habilitar votación, y marketplaces NFT que verifican credenciales de artista verificado antes de mostrar colecciones destacadas. Igualmente lo podemos ver en protocolos DeFi que verifican cumplimiento regulatorio (sanciones, jurisdicciones prohibidas) antes de permitir operaciones, consumiendo VCs sin acceder a datos personales del usuario.

## Anatomía de un DID

Un DID sigue una sintaxis estándar que consta de tres partes:

```plaintest
did:method:method-specific-id
```

Por ejemplo:

- `did:ethr:0x1234...` - DID en Ethereum
- `did:key:z6MkpT...` - DID criptográfico puro
- `did:web:example.com` - DID usando infraestructura web

**Esquema DID**: Identifica que esto es un DID (como `http:` en URLs)

**Método**: Define dónde y cómo se almacena la información del DID (blockchain, servidor web, solo criptográfico)

**Identificador específico**: El identificador único dentro de ese método

## Tipos principales de métodos DID

Los diferentes métodos DID representan distintas filosofías sobre cómo equilibrar descentralización, costo y privacidad.

**DIDs en blockchain** (`did:ethr`, `did:ion`): Máxima descentralización pero con costos de transacción. Ideales para identidades organizacionales o casos donde la inmutabilidad es crítica.

**DIDs criptográficos** (`did:key`): Completamente offline y privados, pero inmutables. Perfectos para identidades temporales o casos simples de verificación.

**DIDs web** (`did:web`): Aprovechan infraestructura existente (dominios), familiares pero centralizados. Buenos para adopción gradual en organizaciones tradicionales.

**DIDs peer-to-peer** (`did:peer`): Máxima privacidad, cada relación usa identificadores únicos. Ideales para comunicación privada donde no necesitas identidad pública.

## El DID Document: tu tarjeta de presentación criptográfica

Cada DID apunta a un DID Document, un archivo JSON que contiene la información técnica necesaria para interactuar contigo de forma segura:

**Claves de verificación**: Las claves públicas que permiten a otros verificar tu identidad

**Métodos de autenticación**: Qué claves puedes usar para demostrar que eres tú

**Endpoints de servicio**: Dónde pueden contactarte (messaging, storage, etc.)

**Control y delegación**: Quién puede actualizar este documento

Importante: el DID Document no contiene información personal como tu nombre o email, solo la infraestructura criptográfica.

## Rotación de claves: seguridad evolutiva

Una ventaja clave de los DIDs es que puedes cambiar tus claves criptográficas manteniendo el mismo identificador. Si sospechas que tu clave fue comprometida, puedes generar una nueva y actualizar tu DID Document. Esto contrasta con direcciones blockchain tradicionales donde perder la clave significa perder la identidad.

## Mensajería segura entre DIDs

DIDComm es el protocolo estándar para enviar mensajes encriptados entre DIDs. Cuando necesitas enviar una credencial o autorización a alguien, DIDComm cifra el mensaje usando las claves públicas del destinatario.

Esto habilita comunicación privada end-to-end donde cada mensaje está firmado por el remitente y cifrado para el destinatario específico. Funciona sobre cualquier transporte: HTTP, WebSocket, QR codes, o incluso email.

## Patrones organizacionales

**Jerarquías corporativas**: Las empresas pueden estructurar DIDs en árbol, donde el DID corporativo raíz delega autoridad a ejecutivos, quienes a su vez delegan a empleados. Cada nivel añade restricciones adicionales pero nunca puede expandir permisos.

**Multi-firma para alta seguridad**: Para cuentas críticas (tesorería de DAO), múltiples DIDs deben firmar cualquier cambio. Esto previene que una sola clave comprometida cause problemas.

**DIDs efímeros**: Para máxima privacidad, puedes generar nuevos DIDs para cada sesión o interacción, previniendo que adversarios correlacionen tu actividad.

## Delegación de autoridad descentralizada

Uno de los aspectos más poderosos de los DIDs es la capacidad de delegar autoridad específica sin entregar control total. Esto se logra mediante [Authorization Capabilities (ZCAP)](https://w3c-ccg.github.io/zcap-spec/), tokens criptográficos que otorgan permisos específicos.

**Concepto fundamental**: En lugar de dar tu clave privada a alguien para que actúe en tu nombre, emites una "capability" firmada que autoriza acciones específicas. Es como dar una llave que solo abre ciertas puertas.

### Casos de uso

**Gobernanza de DAOs**: Delegas tu derecho de voto a un representante solo para propuestas de tesorería, manteniendo tu voto personal para decisiones técnicas.

**Gestión empresarial**: Un CEO autoriza a empleados a firmar contratos hasta cierto monto o presentar credenciales corporativas ante auditores.

**DeFi automatizado**: Autorizas a una aplicación a ejecutar operaciones en protocolos específicos con límites de monto y tiempo.

**Recuperación social**: Designas guardianes con permisos para aprobar recuperación de cuenta solo bajo condiciones específicas.

**Ventaja de revocación**: A diferencia de compartir claves privadas, las capabilities pueden revocarse instantáneamente. Si un empleado deja la empresa o una capability es comprometida, se invalida inmediatamente sin afectar otras autorizaciones.

**Jerarquías organizacionales**: Las organizaciones pueden crear cadenas de autoridad donde el DID corporativo raíz delega a ejecutivos, quienes sub-delegan a equipos. Cada nivel añade restricciones adicionales pero nunca puede expandir permisos más allá de lo autorizado.

## Referencias y especificaciones

- [W3C DID Core 1.0](https://www.w3.org/TR/did-core/) - Especificación fundamental
- [DID Method Registry](https://www.w3.org/TR/did-spec-registries/) - Lista oficial de métodos
- [DIDComm Messaging](https://identity.foundation/didcomm-messaging/spec/) - Protocolo de mensajería
- [Decentralized Identity Foundation](https://identity.foundation/) - Comunidad y grupos de trabajo
- [Authorization Capabilities](https://w3c-ccg.github.io/zcap-spec/) - Especificación de delegación

---
