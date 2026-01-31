# Protocolos DID: Arquitectura Técnica de Identidad Descentralizada

Este documento profundiza en la arquitectura técnica de los Decentralized Identifiers (DIDs) según el estándar [W3C DID Core](https://www.w3.org/TR/did-core/). Aquí encontrarás los detalles de implementación, comparativas entre métodos, y patrones arquitectónicos que complementan la introducción conceptual en [7-1-identity.md](../101/7-1-identity.md).

## Anatomía de un DID

Un DID sigue la sintaxis URI estándar:

```
did:method:method-specific-id
```

Por ejemplo:
- `did:ethr:0x1234567890abcdef1234567890abcdef12345678` - DID en Ethereum
- `did:key:z6MkpTHR8VNsBxYAAWHut2Geadd9jSwuBV8xRoAnwWsdvktH` - DID criptográfico puro
- `did:web:example.com` - DID usando infraestructura web tradicional

Cada componente tiene propósito específico:

**`did:`** - Esquema URI que identifica esto como DID, análogo a `http:` o `mailto:`

**`method:`** - Define la infraestructura subyacente (blockchain, base de datos, archivo) y las reglas para crear, resolver y actualizar el DID

**`method-specific-id:`** - Identificador único dentro del namespace del método, frecuentemente derivado criptográficamente de una clave pública

## DID Methods: Comparativa Técnica

Los DID Methods difieren fundamentalmente en sus trade-offs entre descentralización, costo, privacidad, y funcionalidad. Entender estas diferencias es crucial para elegir el método apropiado según el caso de uso.

### did:ethr - Ethereum Registry

**Infraestructura**: Ethereum mainnet mediante smart contract registry ([ERC-1056](https://eips.ethereum.org/EIPS/eip-1056))

**Creación**: No requiere transacción on-chain inicialmente. El DID se deriva de una dirección Ethereum existente como `did:ethr:0xABC...`. Solo necesitas transacción cuando quieres actualizar el DID Document registrando metadata adicional.

**DID Document**: Almacenado on-chain mediante el registry contract. Contiene claves públicas de autenticación, claves de delegación, y endpoints de servicio.

**Resolución**: Consulta al smart contract registry en Ethereum para obtener el DID Document actualizado.

**Actualización**: Firma una transacción desde la dirección controladora para modificar el DID Document en el registry.

**Revocación**: Puede transferir control a la dirección `0x0` o revocar delegaciones específicas.

**Trade-offs**:
- ✅ Descentralización completa: no hay intermediarios ni coordinadores
- ✅ Interoperabilidad nativa con ecosistema Ethereum (smart contracts pueden verificar DIDs directamente)
- ✅ Seguridad probada: respaldado por consenso de Ethereum
- ❌ Gas costs: cada actualización del DID Document requiere transacción on-chain con fees
- ❌ Latencia: resolución requiere consulta a nodo Ethereum (segundos, no milisegundos)
- ❌ Privacidad limitada: metadatos del DID Document son públicos on-chain

**Casos de uso ideales**: Identidades organizacionales que interactúan con smart contracts DeFi, DAOs, aplicaciones que requieren máxima descentralización y pueden absorber gas costs.

### did:key - Cryptographic Only

**Infraestructura**: Ninguna. Puramente criptográfico.

**Creación**: Genera par de claves, deriva el DID directamente de la clave pública codificándola en formato multibase. Ejemplo: `did:key:z6MkpTHR8VNsBxYAAWHut2Geadd9jSwuBV8xRoAnwWsdvktH`

**DID Document**: No se almacena en ningún lugar. Se genera dinámicamente cada vez que se resuelve, decodificando la clave pública del DID string.

**Resolución**: Puramente local. Un resolver `did:key` parsea el DID, extrae la clave pública, y construye un DID Document minimal que contiene esa clave.

**Actualización**: Imposible. Los `did:key` son inmutables por diseño. Para "actualizar", debes generar un nuevo DID completamente.

**Revocación**: No existe mecanismo de revocación. Si comprometes la clave, debes comunicar fuera de banda que ese DID ya no es confiable.

**Trade-offs**:
- ✅ Zero infrastructure: no requiere blockchain, base de datos, ni ningún servicio
- ✅ Resolución instantánea: completamente offline, latencia de microsegundos
- ✅ Zero cost: crear y resolver DIDs no tiene costo económico
- ✅ Máxima privacidad: no hay registro público de existencia del DID hasta que lo compartes
- ❌ No soporta rotación de claves: si pierdes o comprometes la clave, pierdes la identidad
- ❌ No soporta metadata dinámica: no puedes agregar endpoints de servicio o delegar permisos
- ❌ Funcionalidad limitada: solo sirve para verificación criptográfica básica

**Casos de uso ideales**: Identidades efímeras para sesiones temporales, comunicación peer-to-peer donde las partes intercambian DIDs directamente, casos donde simplicidad y zero-infrastructure son prioritarios.

### did:web - Web-Based DIDs

**Infraestructura**: Servidores web tradicionales con HTTPS.

**Creación**: Elige un dominio que controlas (ej. `example.com`) y crea un archivo `did.json` en la ruta `.well-known/did.json`. El DID resulta en `did:web:example.com`.

**DID Document**: Almacenado como archivo JSON estático en tu servidor web accesible públicamente.

**Resolución**: Resolver realiza petición HTTPS a `https://example.com/.well-known/did.json` para obtener el DID Document.

**Actualización**: Editas el archivo `did.json` en tu servidor. Los cambios son efectivos inmediatamente para próximas resoluciones.

**Revocación**: Eliminas el archivo o devuelves HTTP 404/410.

**Trade-offs**:
- ✅ Familiaridad: usa infraestructura web que ya conoces (DNS, HTTPS, hosting)
- ✅ Sin costos de blockchain: no pagas gas fees
- ✅ Flexibilidad: actualizas instantáneamente sin límites de frecuencia
- ✅ Human-readable: `did:web:acme.com` es más comprensible que hashes criptográficos
- ❌ Centralización: dependes del proveedor DNS y hosting (pueden censurar o perder control del dominio)
- ❌ Seguridad menor: vulnerable a ataques contra infraestructura DNS/HTTPS tradicional
- ❌ Requiere confianza: resolver debe confiar en que el servidor no fue comprometido

**Casos de uso ideales**: Organizaciones corporativas que ya gestionan dominios web, casos donde familiaridad tecnológica reduce barreras de adopción, identidades semi-públicas donde centralización es aceptable.

### did:ion - Layer 2 sobre Bitcoin

**Infraestructura**: [ION](https://identity.foundation/) es una red Layer 2 Sidetree que ancla hashes de operaciones en Bitcoin mainnet mediante transacciones OP_RETURN.

**Creación**: Generas DID Document localmente, computas su hash, y lo publicas a la red ION. Los nodos ION agrupan múltiples operaciones en un batch que anclan en Bitcoin.

**DID Document**: El documento completo se propaga en la red peer-to-peer de nodos ION. Solo el hash se registra en Bitcoin.

**Resolución**: Consulta a nodos ION que mantienen la base de datos completa de DIDs. Los nodos verifican que los hashes de operaciones coincidan con los registrados en Bitcoin.

**Actualización**: Firmas una operación de actualización con la clave de actualización, la publicas a ION, y eventualmente se ancla en Bitcoin en el siguiente batch.

**Revocación**: Operación de desactivación permanente que también se ancla en Bitcoin.

**Trade-offs**:
- ✅ Descentralización fuerte: respaldado por seguridad de Bitcoin
- ✅ Escalabilidad: batching permite cientos de operaciones por una sola transacción Bitcoin
- ✅ Costos reducidos: compartes costo de transacción Bitcoin entre múltiples usuarios
- ✅ Rotación de claves: soporta actualización del DID Document completo
- ❌ Complejidad: requiere ejecutar nodos ION para resolución confiable
- ❌ Latencia de confirmación: operaciones tardan ~10 minutos (tiempo de bloque Bitcoin) en confirmar
- ❌ Eventual consistency: diferentes nodos ION pueden tener estados ligeramente desincronizados temporalmente

**Casos de uso ideales**: Identidades que requieren descentralización de Bitcoin pero con costo razonable, aplicaciones que toleran latencia de confirmación, usuarios que valoran la inmutabilidad y auditabilidad de Bitcoin.

### did:peer - Ephemeral P2P

**Infraestructura**: Ninguna pública. Puramente peer-to-peer.

**Creación**: Dos partes (Alice y Bob) generan DIDs específicamente para su relación bilateral. Alice crea `did:peer:abc` solo para comunicarse con Bob, y Bob crea `did:peer:xyz` solo para Alice.

**DID Document**: Compartido directamente entre las partes mediante el canal de comunicación inicial (QR code, mensaje cifrado). No se publica globalmente.

**Resolución**: Solo las partes involucradas pueden resolver los DIDs porque solo ellas tienen los documentos. No hay resolución pública.

**Actualización**: Comunicas nueva versión del DID Document directamente a tu peer mediante mensaje firmado.

**Revocación**: Simplemente dejas de responder o envías mensaje de revocación directamente.

**Trade-offs**:
- ✅ Privacidad máxima: nadie fuera de la relación sabe que estos DIDs existen
- ✅ Zero infrastructure: no requiere blockchain, servidores, ni registros públicos
- ✅ Minimal correlation: cada relación usa DIDs únicos, previniendo tracking entre contextos
- ❌ No transferible: si Alice introduce Bob a Carol, Carol no puede verificar el DID de Alice sin interacción directa
- ❌ Scope limitado: solo funciona para comunicación bilateral, no para identidad pública

**Casos de uso ideales**: Mensajería privada end-to-end, relaciones bilaterales donde privacidad es máxima prioridad, comunicación que no requiere verificabilidad por terceros.

### did:pkh - Multi-Chain Unification

**Infraestructura**: [CAIP-10](https://github.com/ChainAgnostic/CAIPs/blob/master/CAIPs/caip-10.md) Chain Agnostic Improvement Proposal para representar cuentas blockchain.

**Creación**: Tomas una dirección existente en cualquier blockchain (Ethereum, Bitcoin, Solana, etc.) y la conviertes en DID usando formato `did:pkh:namespace:chain_id:address`. Ejemplo: `did:pkh:eip155:1:0xABC...` para Ethereum mainnet.

**DID Document**: Construido dinámicamente mediante resolvers que conocen la blockchain específica. El documento básico contiene la clave pública derivable de la dirección.

**Resolución**: Resolver consulta la blockchain correspondiente para verificar que la dirección existe y extraer información pública disponible (como ENS reverse records en Ethereum).

**Actualización**: Depende de la blockchain subyacente. En blockchains con smart contracts puedes registrar metadata adicional.

**Revocación**: Generalmente no soportado, ya que las direcciones blockchain son permanentes.

**Trade-offs**:
- ✅ Interoperabilidad multi-chain: unifica identidad a través de Ethereum, Bitcoin, Solana, Cosmos, etc.
- ✅ Reutiliza infraestructura existente: cualquier dirección blockchain es automáticamente un DID
- ✅ Familiaridad: los usuarios ya entienden direcciones blockchain
- ❌ Heterogeneidad: diferentes blockchains tienen capacidades muy diferentes (Bitcoin no tiene smart contracts)
- ❌ Resolución compleja: resolver debe entender protocolos de múltiples blockchains
- ❌ Privacidad variable: depende totalmente de la privacidad de la blockchain subyacente

**Casos de uso ideales**: Aplicaciones multi-chain que necesitan identidad unificada, protocolos como Ceramic que deben funcionar en múltiples ecosistemas blockchain, usuarios que quieren reutilizar sus wallets existentes como identidad.

## DID Resolution: Proceso Técnico

La resolución de DID es el proceso de convertir un DID string en su DID Document correspondiente. Este proceso es crítico porque permite verificación sin necesidad de contactar al propietario del DID directamente.

### Flujo de Resolución

1. **Parsing**: Resolver parsea el DID string para extraer el método y el method-specific-id
2. **Method Selection**: Carga el driver de resolución específico para ese método
3. **Resolution**: Ejecuta la lógica específica del método para obtener el DID Document
4. **Verification**: Valida que el documento cumple con el estándar W3C DID Core
5. **Return**: Devuelve el DID Document junto con metadata de resolución

### Metadata de Resolución

Además del DID Document, el resolver devuelve metadata como:

```json
{
  "contentType": "application/did+json",
  "created": "2024-01-15T10:30:00Z",
  "updated": "2025-01-10T14:20:00Z",
  "versionId": "3",
  "nextUpdate": "2025-02-01T00:00:00Z"
}
```

Esta metadata permite a verificadores entender frescura y validez del documento.

### Universal Resolver

[Universal Resolver](https://dev.uniresolver.io/) es una implementación de referencia que soporta múltiples métodos DID mediante arquitectura de drivers pluggables. Funciona como gateway: recibe un DID de cualquier método, delega al driver apropiado, y devuelve el DID Document estandarizado.

Ventajas:
- Simplifica integración: una API para todos los métodos
- Mantenido por la comunidad: drivers actualizados para métodos populares
- Hosting público: puedes usar instancia pública o desplegar la tuya

Trade-off: Introducir resolver centralizado crea punto de fallo. Para producción crítica, ejecuta tu propia instancia de Universal Resolver o implementa resolvers específicos para los métodos que necesitas.

## DID Document: Estructura Completa

Un DID Document es un objeto JSON que describe cómo interactuar criptográficamente con el sujeto del DID. Veamos un ejemplo completo:

```json
{
  "@context": [
    "https://www.w3.org/ns/did/v1",
    "https://w3id.org/security/suites/ed25519-2020/v1"
  ],
  "id": "did:example:123456789abcdefghi",
  "controller": "did:example:123456789abcdefghi",
  "verificationMethod": [
    {
      "id": "did:example:123456789abcdefghi#key-1",
      "type": "Ed25519VerificationKey2020",
      "controller": "did:example:123456789abcdefghi",
      "publicKeyMultibase": "zH3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV"
    },
    {
      "id": "did:example:123456789abcdefghi#key-2",
      "type": "EcdsaSecp256k1VerificationKey2019",
      "controller": "did:example:123456789abcdefghi",
      "publicKeyJwk": {
        "kty": "EC",
        "crv": "secp256k1",
        "x": "w...",
        "y": "v..."
      }
    }
  ],
  "authentication": [
    "did:example:123456789abcdefghi#key-1"
  ],
  "assertionMethod": [
    "did:example:123456789abcdefghi#key-1",
    "did:example:123456789abcdefghi#key-2"
  ],
  "keyAgreement": [
    {
      "id": "did:example:123456789abcdefghi#key-3",
      "type": "X25519KeyAgreementKey2020",
      "controller": "did:example:123456789abcdefghi",
      "publicKeyMultibase": "z9hFgmPVfmBZwRvFEyniQDBkz9LmV7gDEqytWyGZLmDXE"
    }
  ],
  "capabilityInvocation": [
    "did:example:123456789abcdefghi#key-1"
  ],
  "capabilityDelegation": [
    "did:example:123456789abcdefghi#key-1"
  ],
  "service": [
    {
      "id": "did:example:123456789abcdefghi#messaging",
      "type": "MessagingService",
      "serviceEndpoint": "https://example.com/messaging"
    },
    {
      "id": "did:example:123456789abcdefghi#storage",
      "type": "DecentralizedWebNode",
      "serviceEndpoint": "https://dwn.example.com"
    }
  ]
}
```

### Campos Clave

**`@context`**: Define vocabulario JSON-LD para interpretar el documento

**`id`**: El DID mismo

**`controller`**: DID(s) que controlan este DID Document. Puede ser el mismo DID (auto-controlado) o DIDs externos (control delegado)

**`verificationMethod`**: Array de claves públicas disponibles. Cada método tiene:
- `id`: URI único del método (típicamente `{DID}#key-{n}`)
- `type`: Algoritmo criptográfico (Ed25519, ECDSA secp256k1, RSA)
- `controller`: Quién controla esta clave
- `publicKey*`: La clave pública en formato multibase, JWK, o hex

**Relaciones de Verificación** (authentication, assertionMethod, etc.): Especifican qué claves pueden usarse para qué propósitos:
- `authentication`: Claves para autenticar al sujeto del DID (login)
- `assertionMethod`: Claves para firmar credenciales verificables o mensajes
- `keyAgreement`: Claves para establecer canales cifrados (Diffie-Hellman)
- `capabilityInvocation`: Claves para invocar capabilities autorizadas
- `capabilityDelegation`: Claves para delegar capabilities a otros

**`service`**: Endpoints donde el sujeto ofrece servicios:
- Messaging: URLs para comunicación DIDComm
- Storage: Decentralized Web Nodes para datos de usuario
- Credential Store: Servicios para emitir/verificar credenciales
- Cualquier endpoint custom que definas

### Rotación de Claves

Uno de los beneficios principales de DIDs sobre direcciones blockchain desnudas es la capacidad de rotar claves sin cambiar el identificador.

**Flujo típico**:
1. Generas nuevo par de claves (key-new)
2. Firmas actualización del DID Document con clave actual (key-old) agregando key-new a verificationMethod
3. Publicas actualización según método DID (transacción on-chain, actualización de archivo, etc.)
4. Opcional: mantienes ambas claves activas temporalmente para transición suave
5. Después de periodo de gracia, firmas nueva actualización con key-new removiendo key-old
6. Destruyes key-old de forma segura

Este mecanismo permite:
- Recuperación ante compromiso: rotas a nueva clave si sospechas que la actual fue comprometida
- Actualizaciones de seguridad: migras a algoritmos criptográficos más fuertes
- Gestión de dispositivos: rotas cuando cambias de dispositivo

No todos los métodos DID soportan rotación de claves. `did:key` es inherentemente inmutable. `did:ethr`, `did:ion`, y `did:web` soportan actualizaciones completas.

## DIDComm: Protocolo de Mensajería

[DIDComm](https://identity.foundation/didcomm-messaging/spec/) es un protocolo de mensajería segura entre DIDs que utiliza los endpoints y claves públicas del DID Document.

Cuando creas una capability o presentación verificable, frecuentemente necesitas transmitirla al delegado o verificador. DIDComm proporciona el canal seguro: los mensajes se encriptan usando las claves públicas del DID Document del destinatario, se firman con tu clave privada para autenticación, y se transmiten mediante transporte agnóstico (HTTP, WebSocket, IPFS, o incluso email).

DIDComm soporta patrones de mensajería complejos: request-response para negociación de credenciales, mensajes asíncronos para notificaciones, y protocolos multi-paso para workflows de autorización. Por ejemplo, un verificador puede solicitar una presentación específica, tu wallet responde con la VP solicitada, y el verificador confirma aceptación, todo mediante mensajes DIDComm encriptados end-to-end.

### Características Principales

**Cifrado end-to-end**: Mensajes cifrados usando claves de `keyAgreement` del destinatario

**Autenticación**: Cada mensaje incluye firma del remitente, verificable contra su `assertionMethod`

**Routing**: Soporta mediadores que forwardean mensajes sin descifrarlos (útil para dispositivos móviles intermitentemente conectados)

**Transport-agnostic**: Funciona sobre HTTP, WebSocket, Bluetooth, QR codes, o cualquier canal de bytes

### Estructura de Mensaje

```json
{
  "type": "https://didcomm.org/basicmessage/2.0/message",
  "id": "unique-message-id",
  "from": "did:example:alice",
  "to": ["did:example:bob"],
  "created_time": 1640000000,
  "body": {
    "content": "Hello Bob!"
  }
}
```

El mensaje se cifra mediante ECDH usando la clave pública de Bob, resultando en JWE (JSON Web Encryption).

### Casos de Uso

**Credential Issuance**: Emisor usa DIDComm para enviar Verifiable Credential al titular de forma privada

**Negotiation**: Dos partes negocian términos de intercambio (precio, datos compartidos) mediante mensajes firmados

**Delegated Authorization**: Principal envía a agente autorización firmada para actuar en su nombre

**Social Recovery**: Guardianes coordinan mediante DIDComm para recuperación de wallet comprometida

DIDComm complementa protocolos como [OIDC4VC](https://openid.net/sg/openid4vc/) proporcionando capa de transporte seguro y privado.

## Patrones Avanzados

### DIDs Jerárquicos para Organizaciones

Una corporación puede estructurar DIDs en jerarquía:

```
did:ethr:0xCORP... (root corporativo)
  ├─ did:ethr:0xCEO... (ejecutivo con delegación completa)
  ├─ did:ethr:0xCFO... (ejecutivo financiero con permisos acotados)
  │   ├─ did:ethr:0xACCT1... (contador con límites transaccionales)
  │   └─ did:ethr:0xACCT2... (auditor con permisos solo-lectura)
  └─ did:ethr:0xENG... (departamento ingeniería)
      ├─ did:ethr:0xDEV1... (desarrollador con acceso a repos)
      └─ did:ethr:0xDEV2... (desarrollador con acceso a staging)
```

Cada DID hijo incluye en su `controller` field el DID padre, creando cadena de confianza verificable. Para revocar permisos de un empleado, la organización actualiza el DID Document del empleado removiendo la delegación desde el DID corporativo.

### DIDs Multi-Sig

Para identidades de alta seguridad (tesorería de DAO, cuentas corporativas), el `controller` puede ser un array de DIDs que requieren firma conjunta:

```json
{
  "id": "did:ethr:0xTREASURY...",
  "controller": [
    "did:ethr:0xGUARDIAN1...",
    "did:ethr:0xGUARDIAN2...",
    "did:ethr:0xGUARDIAN3..."
  ],
  "proof": {
    "type": "multisig",
    "threshold": 2,
    "signatures": [...]
  }
}
```

Cualquier actualización del DID Document requiere firmas de al menos 2 de los 3 guardianes. Esto previene compromiso por un solo punto de fallo.

### DIDs Efímeros con Rotación Automática

Para aplicaciones de alta privacidad, puedes generar nuevos DIDs regularmente:

1. Aplicación genera `did:peer` único por sesión
2. Comparte DID mediante canal inicial (QR code)
3. Después de interacción (ej. 24 horas), ambas partes descartan ese DID
4. Próxima interacción usa nuevos DIDs

Esto previene correlation attacks donde adversarios intentan rastrear al usuario vinculando múltiples interacciones al mismo DID persistente.

## Delegación de identidad y autorización

En sistemas de identidad descentralizada, frecuentemente necesitas permitir que otros actúen en tu nombre sin entregarles control total sobre tu identidad. Imagina que tu DAO necesita que un tesorero ejecute transacciones, o que tu empresa quiere que un empleado firme documentos oficialmente, o que deseas autorizar a una aplicación para presentar ciertas credenciales tuyas sin darle acceso a todas. Aquí entran los mecanismos de delegación y autorización descentralizada.

**Authorization Capabilities: permisos descentralizados granulares**:

Más allá de presentar credenciales propias, frecuentemente necesitas delegar autoridad para que otros actúen en tu nombre. Aquí emergen los [Object Capabilities (OCAPs)](https://en.wikipedia.org/wiki/Object-capability_model) aplicados a identidad descentralizada, formalizados en estándares como [Authorization Capabilities (ZCAP)](https://w3c-ccg.github.io/zcap-spec/) del W3C Community Group.

Una authorization capability es un token criptográfico firmado por ti que otorga permisos específicos a un DID delegado. A diferencia de sistemas tradicionales donde la autorización se verifica consultando una base de datos central de permisos (Access Control Lists), las capabilities son bearer tokens: quien posee el token tiene el permiso, verificable criptográficamente sin coordinación centralizada.

El modelo funciona mediante cadenas de delegación. Tienes un root capability asociado a tu DID que representa autoridad total sobre tu identidad. Puedes firmar una capability derivada que otorga a `did:example:bob` el permiso de "presentar mi credencial educativa", con restricciones adicionales como validez temporal (solo durante enero 2026) o alcance limitado (solo a verificadores universitarios). Bob puede usar esta capability para actuar en tu nombre dentro de esos límites, presentando el token firmado que demuestra tu autorización explícita.

Las capabilities soportan cadenas de delegación transitiva donde Bob podría sub-delegar a `did:example:charlie` permisos aún más restringidos, siempre que la capability original lo permita. Cada nivel de delegación añade restricciones adicionales pero nunca puede expandir permisos. Esto crea jerarquías de confianza descentralizadas donde la autoridad fluye desde el titular original mediante cadenas criptográficas verificables.

**Casos de uso prácticos de delegación**:

En gobernanza de DAOs, los miembros principales pueden delegar su derecho de voto a representantes mediante capabilities con restricciones temáticas. Tu capability podría autorizar que `did:dao:representative` vote en tu nombre solo en propuestas de categoría "tesorería", manteniendo tu voto personal para decisiones técnicas o de protocolo.

Para gestión empresarial, el CEO de una organización puede emitir capabilities que autorizan a empleados específicos a firmar contratos hasta cierto monto, presentar credenciales corporativas ante auditores, o actuar como representantes oficiales en contextos definidos. Estas capabilities son revocables instantáneamente sin necesidad de cambiar credenciales subyacentes.

En DeFi, podrías autorizar a una aplicación de gestión de portfolio a ejecutar ciertas operaciones en tu nombre mediante capabilities que especifican protocolos permitidos, límites de monto, y ventanas temporales. La aplicación presenta tu capability junto con sus transacciones, demostrando autorización verificable sin necesidad de que entregues tus claves privadas.

Las carteras de recuperación social se benefician de capabilities donde designas a guardianes con permisos restringidos para aprobar recuperación de cuenta solo bajo condiciones específicas, sin otorgarles acceso general a tu identidad o activos durante operación normal.

**Revocación de delegaciones**:

Un aspecto crítico de las capabilities es la revocabilidad. A diferencia de entregar claves privadas (irrevocable sin cambiar toda tu identidad), las capabilities pueden invalidarse unilateralmente por el emisor original.

El modelo de revocación funciona similar a VCs: el emisor mantiene un registro de capabilities revocadas (on-chain o mediante servicio accesible). Cuando un verificador valida una capability presentada por un delegado, además de verificar la firma criptográfica, debe consultar si esa capability específica ha sido revocada. Si aparece en el registro, se rechaza automáticamente incluso si la firma es técnicamente válida.

Esto permite gestión dinámica de confianza: si un empleado deja la empresa, revocas instantáneamente todas sus capabilities sin necesidad de cambiar credenciales corporativas o reconfigurar sistemas. Si descubres que una capability fue comprometida, la revocas inmediatamente limitando ventana de abuso.

**Identidad corporativa e institucional: jerarquías de autoridad descentralizadas**:

Las organizaciones enfrentan un desafío único en Web3: necesitan operar como entidades legales reconocibles mientras permiten que empleados individuales actúen en su nombre mediante identidades descentralizadas. Aquí la delegación de identidad se vuelve fundamental para construir jerarquías de autoridad verificables sin sacrificar los beneficios de la descentralización.

Una organización típicamente posee un DID corporativo raíz (`did:example:acmecorp`) que representa a la entidad legal completa. Este DID está controlado por la alta dirección mediante multisig u otros mecanismos de control compartido. Las credenciales más importantes de la organización se emiten a este DID: certificaciones regulatorias, registros comerciales, licencias de operación, membresías en consorcios industriales.

Los empleados mantienen sus propios DIDs personales, pero la organización les emite capabilities derivadas que los autorizan a actuar en representación corporativa dentro de límites específicos. Un empleado de ventas podría recibir una capability que le permite firmar contratos de hasta $50,000, válida solo durante su período de empleo. Un contador recibe capabilities para presentar las credenciales financieras corporativas ante auditores. Un ingeniero obtiene permisos para desplegar código en repositorios corporativos.

La arquitectura típica se estructura en múltiples niveles. El DID corporativo raíz emite capabilities de primer nivel a ejecutivos (CEO, CFO, CTO), quienes a su vez pueden sub-delegar capabilities más restringidas a sus equipos. Un CFO puede recibir autoridad financiera amplia del DID corporativo, y luego emitir capabilities específicas a su equipo de contabilidad para tareas operativas. Cada nivel añade restricciones adicionales: el contador no puede autorizar gastos que el CFO no pueda, y el CFO no puede exceder los límites establecidos por el board.

La trazabilidad es crítica para cumplimiento regulatorio y auditoría. Cuando un empleado firma un contrato en nombre de la empresa, la firma no solo demuestra criptográficamente su autoridad mediante la cadena de capabilities, sino que crea un registro auditable: empleado X actuó bajo autoridad Y otorgada por ejecutivo Z en fecha D, todo verificable on-chain sin necesidad de sistemas centralizados de gestión de permisos.

Las Verifiable Presentations corporativas permiten que empleados presenten credenciales organizacionales selectivamente. Un representante de ventas puede generar una VP que demuestra "represento a Acme Corp verificada como empresa legítima con certificación ISO 9001" sin revelar información financiera sensible de la organización. La VP incluye la cadena de autorización desde el DID corporativo hasta el DID del empleado, probando legitimidad sin exponer estructura organizacional completa.

La separación entre identidad personal y rol corporativo protege tanto a empleados como a organizaciones. Cuando un empleado deja la empresa, la organización revoca sus capabilities corporativas pero el empleado mantiene su DID personal con su historial profesional intacto. Si posteriormente trabaja para otra organización, su nuevo empleador puede verificar su experiencia previa mediante VCs emitidas por el empleador anterior a su DID personal, mientras que su autoridad actual deriva de capabilities emitidas por el nuevo empleador.

Los casos de uso de compliance son particularmente relevantes. Regulaciones financieras requieren que instituciones demuestren quién autorizó qué operaciones. Con DIDs corporativos y capabilities, cada transacción incluye prueba criptográfica de autorización: el tesorero que ejecutó el pago tenía capability válida emitida por el CFO, quien tenía autoridad del board, todo verificable mediante cadena de firmas digitales que satisface requisitos de auditoría sin necesidad de bases de datos centralizadas de permisos.

La gobernanza multi-firma complementa este modelo. Decisiones críticas requieren múltiples firmas del DID corporativo: el board debe aprobar colectivamente presupuestos anuales, fusiones, o cambios estatutarios. Estas firmas múltiples se implementan mediante smart contracts que validan que suficientes ejecutivos autorizados firmaron la decisión antes de emitir capabilities downstream o ejecutar acciones corporativas.

Las organizaciones descentralizadas (DAOs) implementan variaciones de estos patrones. En lugar de jerarquías tradicionales, las DAOs distribuyen autoridad mediante gobernanza tokenizada, pero igualmente necesitan mecanismos donde contributors actúen en nombre de la organización. Un contributor con rol de "community manager" recibe capabilities para presentar credenciales oficiales de la DAO, publicar anuncios oficiales, o moderar espacios comunitarios. La diferencia fundamental es que estas capabilities se otorgan mediante procesos de votación descentralizada en lugar de designación ejecutiva tradicional.

Los desafíos técnicos incluyen gestión de lifecycle de capabilities a escala: una corporación con miles de empleados genera millones de capabilities delegadas que deben mantenerse, renovarse, y revocarse dinámicamente. Soluciones emergentes como [Hats Protocol](https://www.hatsprotocol.xyz/) proporcionan infraestructura específica para gestión de roles y permisos organizacionales, integrando capabilities con sistemas de gestión de identidad empresarial tradicionales mediante APIs y protocolos de sincronización.

## Referencias y Especificaciones

- [W3C DID Core 1.0](https://www.w3.org/TR/did-core/) - Especificación fundamental
- [DID Method Registry](https://www.w3.org/TR/did-spec-registries/) - Lista oficial de métodos
- [DIDComm Messaging](https://identity.foundation/didcomm-messaging/spec/) - Protocolo de mensajería
- [Universal Resolver](https://github.com/decentralized-identity/universal-resolver) - Implementación de referencia
- [DIF (Decentralized Identity Foundation)](https://identity.foundation/) - Comunidad y grupos de trabajo

---

Este documento proporciona la base técnica para implementar sistemas de identidad descentralizada. Para casos de uso prácticos y integración con aplicaciones Web3, consulta [9-1-ecosystem-DApps.md](../101/9-1-ecosystem-DApps.md).
