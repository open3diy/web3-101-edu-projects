# Cryptography

## Concepto

La criptografía es la ciencia de la transformación de un mensaje para mantenerlo confidencial en base a claves, que pueden ser simétricas o asimétricas. En el contexto de blockchain, es el fundamento que permite transacciones seguras sin intermediarios centralizados.

## Tipos de Criptografía

### Criptografía Simétrica

Utiliza la misma clave para cifrar y descifrar. Ambas partes deben compartir la clave secreta previamente.

Cifrado por Bloques

Divide el mensaje en bloques de tamaño fijo y cifra cada bloque independientemente. Algoritmos comunes incluyen DES (obsoleto), 3DES (lento pero más seguro), y AES (estándar actual con claves de 128, 192 o 256 bits).

AES es el más utilizado actualmente por su balance entre seguridad y rendimiento. Opera en bloques de 128 bits y AES-256 es prácticamente imposible de romper por fuerza bruta.

Cifrado por Flujo

Cifra el mensaje bit a bit o byte a byte usando un flujo de claves pseudo-aleatorio. RC4 fue popular pero ahora es inseguro. ChaCha20 es moderno y eficiente, usado en TLS 1.3 y VPNs modernas.

### Criptografía Asimétrica

La más común por su versatilidad. Distribuye clave pública para funciones unidireccionales: lo que se cifra con una clave solo se puede descifrar con la otra.

Utiliza un par de claves matemáticamente relacionadas: clave pública (compartida abiertamente) y clave privada (mantenida en secreto). Este sistema resuelve el problema de distribución de claves. Puedes publicar tu clave pública libremente, y cualquiera puede usarla para enviarte mensajes cifrados que solo tú puedes descifrar con tu clave privada.

Algoritmos principales:

RSA (Rivest-Shamir-Adleman)

Basado en la dificultad de factorizar números primos grandes. Tamaños de clave típicos son 2048 o 4096 bits. Ampliamente usado para cifrado y firmas digitales en PKI tradicional.

ECDSA (Elliptic Curve Digital Signature Algorithm)

Basado en matemática de curvas elípticas. Una clave ECDSA de 256 bits tiene seguridad equivalente a RSA de 3072 bits. Es determinista en generación de clave pública en base a privada. Usado en Bitcoin, Ethereum, y la mayoría de certificados SSL/TLS modernos.

EdDSA (Edwards-curve Digital Signature Algorithm)

Variante moderna diseñada para evitar vulnerabilidades de implementación. Determinista, resistente a timing attacks. Usado en Solana, Polkadot, Cardano, y SSH moderno (ed25519).

## Certificados Digitales

En criptografía asimétrica se utilizan soportes como X.509 o GPG llamados certificados, con estructura definida que contiene atributos específicos.

### Componentes de un Certificado

Un certificado digital contiene:

Algoritmos

Algoritmo de hash y de firma (típicamente SHA-256 con RSA o ECDSA). Algoritmo y hash de cifrado utilizados para las operaciones criptográficas.

Propósitos (Key Usage)

Define para qué puede usarse el certificado: firma digital, cifrado de datos, firma de certificados (solo CAs), autenticación de servidor/cliente, firma de código.

Identificación

Sujeto: identifica al propietario del certificado (nombre, organización, email). Emisor: identifica a la Autoridad Certificadora que firmó el certificado. Número de serie: identificador único del certificado.

Huella Digital

Hash generado en base a todo el contenido del certificado (incluido firmas de los emisores). SUPER importante para verificar autenticidad.

```bash
# Ejemplo de huella digital SHA-256
59:3A:FB:72:44:49:1C:F7:E3:6E:41:B4:25:9F:87:3D...
```

Validez y Revocación

Caducidad: fechas de inicio y expiración del certificado. Métodos de comprobación de revocación: CRL (Certificate Revocation List) y OCSP (Online Certificate Status Protocol).

Claves

Clave privada: mantenida en secreto por el propietario. Clave pública: distribuida libremente en el certificado.

### Modelo de Confianza

El emisor firma el certificado para darle autenticidad si confiamos en una PKI con CA (Public Key Infrastructure con Certificate Authority).

Si no confiamos en la PKI, debemos confiar en el valor de la huella digital como auténtico, verificándola por un canal secundario confiable (en persona, teléfono, mensaje firmado previamente conocido).

## Operaciones Criptográficas

### Firma Digital

Se genera hash del contenido y se cifra con la clave privada. Como resultado está la cadena cifrada y la parte pública para su descifrado.

Propósito: mantener autenticidad e integridad del mensaje. También no repudio porque solo está en posesión del emisor firmante, siempre que incluya marca de tiempo.

Algoritmo típico: SHA para hash y RSA para cifrado de firma. En blockchain se usa SHA-256 o Keccak-256 con ECDSA.

Proceso:

1. Genera hash del mensaje (ej: SHA-256)
2. Cifra el hash con clave privada, produciendo la firma
3. Distribuye mensaje + firma + clave pública
4. Receptor descifra firma con clave pública y compara hashes

### Cifrado Asimétrico

Se genera una serialización cifrada del contenido usando la clave pública del destinatario, para que el receptor pueda descifrarlo con su clave privada.

Algoritmo típico: SHA para hashing y RSA o ECDH para cifrado. Usado cuando necesitas enviar datos confidenciales a alguien sin haber compartido claves previamente.

## Casos de Uso por Algoritmo

Resumen de cuándo usar cada tipo:

Firma y Cifrado con Simétrica

Si quieres firmar y cifrar es típico 3DES en simétrica, aunque AES-256 es preferible actualmente por rendimiento.

Cifrar y Firmar con Asimétrica

Si es cifrar y firmar con asimétrica: RSA o ECDSA. ECDSA es determinista en generación de clave pública en base a privada, lo que lo hace ideal para blockchain.

Solo Cifrado Simétrico

Si es cifrar y descifrar solo: AES con clave simétrica. AES-256-GCM es el estándar recomendado actualmente.

## Conceptos Fundamentales

### Checksum

Valor calculado a partir de datos para detectar errores de transmisión o corrupción accidental. No es criptográficamente seguro, solo detecta errores aleatorios.

En blockchain, las direcciones incluyen checksum para prevenir errores de tipeo. Bitcoin usa Base58Check con 4 bytes de doble SHA-256. Ethereum usa EIP-55 con capitalización como checksum.

Más información: [Suma de verificación](https://es.wikipedia.org/wiki/Suma_de_verificaci%C3%B3n)

### Nonce Criptográfico

Number that can be only used once (número que solo puede usarse una vez).

Número aleatorio y a poder ser único, usado una sola vez destinado en un protocolo de autenticación para que autenticaciones antiguas no puedan re-usarse en replay attacks. Básicamente es una semilla o valor único que comunica el servidor al cliente para que sea usado en una autenticación.

Usos en blockchain:

Autenticación: el servidor envía nonce al cliente, quien debe incluirlo en respuesta firmada para prevenir replay attacks.

Firma ECDSA: el nonce k debe ser único por cada firma. Si se reutiliza, la clave privada puede ser extraída. Crítico para seguridad.

Proof of Work: en minería Bitcoin, el nonce es el valor que mineros incrementan buscando un hash válido que cumpla el target de dificultad.

Transacciones: en Ethereum, el nonce de cuenta es contador secuencial que previene replay de transacciones.

Más información: [Cryptographic nonce](https://en.wikipedia.org/wiki/Cryptographic_nonce)

### Hash

Una función hash es un algoritmo matemático que transforma cualquier cantidad de datos en una cadena de longitud fija. Según los bits del algoritmo, el SHA-256 es de 256 bits o 32 bytes. Cada byte permite dos números hexadecimales, es decir, representación de posición fija de 64 caracteres.

```bash
SHA-256: 256 bits = 32 bytes = 64 caracteres hex
Input: "blockchain"
Output: ef7797e13d3a75526946a3bcf00daec9fc9c9c4d51ddc7cc5df888f74dd434d1
        |<---------------------- 64 caracteres ---------------------->|
```

El input alimenta a la función de hash y tiene como resultado el **digest** o digestión (como el hash de la comida). Es una **función unidireccional**: fácil calcular hash desde mensaje, imposible calcular mensaje desde hash.

#### Historia y Evolución de las Funciones Hash

Las funciones hash criptográficas han evolucionado significativamente desde sus orígenes:

**Década de 1970 - Fundamentos Teóricos:**

El trabajo seminal de **Merkle-Damgård** en la década de 1970 sentó las bases para la construcción de funciones hash criptográficas. La construcción Merkle-Damgård divide el mensaje en bloques y los procesa iterativamente, creando una cadena de dependencias que garantiza que cualquier cambio en el input afecte al output final.

**Década de 1990 - MD5 y SHA-1:**

- **MD5 (Message Digest Algorithm 5)**: Diseñado por Ronald Rivest en 1991, produce hashes de 128 bits. Ampliamente utilizado durante años, pero en 2004 se demostraron **ataques de colisión prácticos**: dos mensajes diferentes pueden producir el mismo hash. **Actualmente obsoleto y no debe usarse**.

- **SHA-1 (Secure Hash Algorithm 1)**: Desarrollado por la NSA en 1995, produce hashes de 160 bits. En 2017, Google demostró el primer ataque de colisión práctico (SHAttered attack). **Deprecado para usos criptográficos**.

**2001 - SHA-2:**

Lanzado por la NSA, incluye variantes de diferentes longitudes:
- SHA-224 (224 bits)
- **SHA-256** (256 bits) - el más usado en blockchain
- SHA-384 (384 bits)
- SHA-512 (512 bits)

SHA-256 es el estándar actual en Bitcoin y la mayoría de blockchains. No se conocen vulnerabilidades prácticas.

**2012 - SHA-3 (Keccak):**

Ganador de la competencia de hash organizada por NIST. Diseño completamente diferente basado en el principio de **esponjas criptográficas**, ofreciendo una alternativa robusta a SHA-2. Ethereum utiliza una variante llamada **Keccak-256** (ligeramente diferente de SHA-3 estándar).

**2020 - BLAKE3:**

Algoritmo moderno extremadamente rápido, basado en BLAKE2 pero optimizado para paralelización. Diseñado para ser resistente a ataques cuánticos y mucho más eficiente que SHA-2.

#### Propiedades Fundamentales

Una función hash criptográfica debe cumplir:

**1. Determinismo:**

Mismo input siempre produce mismo output. Esto es fundamental para verificación.

```bash
SHA-256("bitcoin") = 6b88c087247aa2f07ee1c5956b8e1a9f4c7f892a70e324f1bb3d161e05ca107b
# Siempre, en cualquier computadora, en cualquier momento
```

**2. Resistencia a Preimagen (Unidireccionalidad):**

Dado un hash H, es computacionalmente imposible encontrar un mensaje M tal que hash(M) = H. Esto protege contra ingeniería inversa.

**3. Resistencia a Segunda Preimagen:**

Dado un mensaje M1, es imposible encontrar otro mensaje M2 diferente tal que hash(M1) = hash(M2). Esto previene suplantación.

**4. Resistencia a Colisiones:**

Es computacionalmente imposible encontrar dos mensajes diferentes M1 y M2 tal que hash(M1) = hash(M2). Esta propiedad fue vulnerada en MD5 y SHA-1, por eso se consideran inseguros.

**5. Efecto Avalancha:**

Un cambio mínimo en el input produce un hash completamente diferente. Esto es crucial para detectar modificaciones.

```bash
# Ejemplos del efecto avalancha con SHA-256:

Input: "blockchain"
Hash:  ef7797e13d3a75526946a3bcf00daec9fc9c9c4d51ddc7cc5df888f74dd434d1

Input: "Blockchain"  # Solo la 'B' mayúscula
Hash:  625da44e4eaf58d61cf048d168aa6f5e492dea166d8bb54ec06c30de07db57e1
       ^  Completamente diferente

Input: "blockchain "  # Un espacio al final
Hash:  8cc0f1f8c7c3c20ab7c8e5fa52d81f3c5a8d2b8a9c8f2e5c1f3c6a7b8c9d0e1f2
       ^  Totalmente distinto

Input: "blockchaio"   # Cambio de 'n' por 'o'
Hash:  3f9c4a8e6d2f1b5a7c8e9d0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b
       ^  Hash radicalmente diferente
```

Este efecto avalancha garantiza que incluso la modificación más pequeña en un bloque de blockchain sea inmediatamente detectable.

#### Aplicaciones en Blockchain

**1. Encadenamiento de Bloques:**

Cada bloque contiene el hash del bloque anterior, creando una cadena inmutable:

```
Bloque 1:
- Datos: "Transacción A"
- Hash anterior: 0000000000000000
- Hash propio: abc123...

Bloque 2:
- Datos: "Transacción B"
- Hash anterior: abc123...  ← Hash del Bloque 1
- Hash propio: def456...

Bloque 3:
- Datos: "Transacción C"
- Hash anterior: def456...  ← Hash del Bloque 2
- Hash propio: ghi789...
```

Si alguien intenta modificar el Bloque 1:
1. Su hash cambiaría de `abc123...` a algo diferente
2. El Bloque 2 seguiría apuntando al hash antiguo `abc123...`
3. La cadena estaría rota y sería detectable inmediatamente
4. Para ocultar el cambio, el atacante debería recalcular todos los bloques posteriores
5. En una red descentralizada con miles de nodos, esto es prácticamente imposible

**2. Proof of Work (Minería):**

Los mineros buscan un nonce que produzca un hash que cumpla cierto objetivo (target). Por ejemplo, en Bitcoin el hash debe comenzar con cierto número de ceros:

```bash
# Target: hash debe comenzar con 4 ceros
Hash("Bloque + nonce=1")    = 8a3f2c...  ✗ No válido
Hash("Bloque + nonce=2")    = 7b2e1d...  ✗ No válido
Hash("Bloque + nonce=3")    = 9c4f3e...  ✗ No válido
...
Hash("Bloque + nonce=42857") = 0000a1b2...  ✓ Válido!
```

**3. Direcciones de Wallets:**

Las direcciones criptográficas se derivan aplicando funciones hash a claves públicas:

- Bitcoin: RIPEMD-160(SHA-256(clave_pública))
- Ethereum: Keccak-256(clave_pública), tomando últimos 20 bytes

**4. Verificación de Integridad:**

Los hashes permiten verificar que archivos, transacciones o bloques no han sido alterados sin necesidad de comparar todo el contenido, solo el hash.

### Árboles de Merkle

Una aplicación fundamental de las funciones hash en blockchain son los **Árboles de Merkle** (Merkle Trees), inventados por Ralph Merkle en 1979.

#### Estructura

Un árbol de Merkle es una estructura de datos jerárquica donde:

1. Las **hojas** contienen hashes de datos individuales (transacciones)
2. Los **nodos intermedios** contienen hashes de sus hijos concatenados
3. La **raíz de Merkle** (Merkle Root) es el hash en la cima del árbol

```
                    Raíz de Merkle
                    Hash(ABCD)
                   /          \
              Hash(AB)        Hash(CD)
             /      \        /      \
         Hash(A)  Hash(B)  Hash(C)  Hash(D)
           |        |        |        |
         Tx A     Tx B     Tx C     Tx D
```

#### Proceso de Construcción

```bash
# Ejemplo con 4 transacciones:
Tx A = "Alice paga 1 BTC a Bob"
Tx B = "Bob paga 0.5 BTC a Carol"
Tx C = "Carol paga 2 BTC a Dave"
Tx D = "Dave paga 0.3 BTC a Eve"

# Nivel 1 (hojas):
Hash(A) = SHA-256("Alice paga 1 BTC a Bob")     = a1b2c3...
Hash(B) = SHA-256("Bob paga 0.5 BTC a Carol")   = d4e5f6...
Hash(C) = SHA-256("Carol paga 2 BTC a Dave")    = g7h8i9...
Hash(D) = SHA-256("Dave paga 0.3 BTC a Eve")    = j0k1l2...

# Nivel 2 (nodos intermedios):
Hash(AB) = SHA-256(a1b2c3... + d4e5f6...) = m3n4o5...
Hash(CD) = SHA-256(g7h8i9... + j0k1l2...) = p6q7r8...

# Nivel 3 (raíz):
Merkle Root = SHA-256(m3n4o5... + p6q7r8...) = s9t0u1v2...
```

#### Ventajas en Blockchain

**1. Verificación Eficiente (SPV - Simple Payment Verification):**

Puedes verificar que una transacción está incluida en un bloque sin descargar todo el bloque, solo la **prueba de Merkle** (Merkle Proof):

```bash
# Para verificar Tx A, solo necesitas:
- Hash(A)
- Hash(B)     # Para reconstruir Hash(AB)
- Hash(CD)    # Para reconstruir Merkle Root

# En lugar de descargar las 4 transacciones completas
```

Con un árbol de 1,000 transacciones, solo necesitas ~10 hashes (log₂ 1000) en lugar de 1,000 transacciones completas. **Reducción exponencial de datos**.

**2. Integridad del Bloque:**

La raíz de Merkle se incluye en el encabezado del bloque. Si cualquier transacción cambia:
- Su hash cambia
- Los hashes de todos sus ancestros cambian
- La raíz de Merkle cambia
- El hash del bloque completo cambia
- La cadena se rompe

**3. Eficiencia en Nodos Ligeros:**

Wallets móviles y SPV clients pueden verificar transacciones sin almacenar toda la blockchain, solo los encabezados de bloques (que contienen las raíces de Merkle).

#### Uso en Diferentes Blockchains

- **Bitcoin**: Utiliza árboles de Merkle estándar con SHA-256
- **Ethereum**: Usa **árboles de Merkle Patricia** (variante optimizada) con Keccak-256 para almacenar estado, transacciones y recibos
- **IPFS**: Usa **Merkle DAGs** (Directed Acyclic Graphs) para estructurar contenido descentralizado

### Hash

## ECDSA en Blockchain

Algoritmo de firma de curva elíptica (ECDSA). La clave pública se crea a partir de la clave privada: ECDSA es el algoritmo de curva elíptica que se utiliza en el protocolo Bitcoin para crear un par de claves privada y pública. La clave pública ECDSA se deriva de la clave privada, pero no se puede hacer el proceso inverso de derivar la clave privada a partir de la clave pública.

### Características Únicas

Este algoritmo es diferente a otros: permite generar (solo en esta dirección) en base a la private key el public key, y en base al public key la address.

Con la private key solo, es posible obtener los 2 elementos restantes (public key y addresses), varias de ellas. La generación es estrictamente unidireccional y determinista.

### Relación entre Claves y Direcciones

Relación 1:1 entre private key, public key y address en uso normal.

Pero en firma múltiple (multisig): una misma address tiene varias public keys asociadas. Sin embargo, para tu firma específica solo tienes una private key.

### Proceso de Generación

1. Private key: número aleatorio de 256 bits (debe generarse con fuente segura de entropía)
2. Public key: punto en curva elíptica = private_key × G (G es punto generador de la curva)
3. Address: hash de la public key

En Bitcoin: RIPEMD-160(SHA-256(public_key)) + prefijos + checksum, codificado en Base58Check.

En Ethereum: Keccak-256(public_key), tomando últimos 20 bytes, codificado en hexadecimal con EIP-55 checksum.

### Firma y Verificación

Para firmar transacción:

1. Hash del mensaje (transacción)
2. Generar nonce k único y aleatorio (CRÍTICO: debe ser único)
3. Calcular punto R = k × G en la curva
4. Calcular firma (r, s) usando matemática de curva elíptica

El nonce k DEBE ser único para cada firma. Reutilizarlo permite a un atacante extraer la clave privada matemáticamente. Esto causó el hack de PlayStation 3 y pérdidas de Bitcoin.

Para verificar:

Cualquiera puede verificar la firma con mensaje, firma (r, s) y clave pública. No necesitas clave privada para verificar, solo la pública. Esto es fundamental en blockchain: todos los nodos pueden verificar transacciones sin conocer claves privadas.

## Hashes en Contratos Inteligentes

Las funciones hash juegan un papel crítico en los contratos inteligentes, permitiendo automatización segura y verificación de condiciones sin revelar información sensible.

### Casos de Uso Prácticos

#### 1. Commit-Reveal Schemes (Esquemas de Compromiso y Revelación)

Permiten hacer compromisos públicos sin revelar la información inmediatamente:

```solidity
// Fase 1: Commit (Compromiso)
// Usuario envía hash de su elección + secreto
function commit(bytes32 hashedChoice) public {
    commitments[msg.sender] = hashedChoice;
}

// Fase 2: Reveal (Revelación)
// Usuario revela su elección y secreto
function reveal(string memory choice, string memory secret) public {
    bytes32 hash = keccak256(abi.encodePacked(choice, secret));
    require(hash == commitments[msg.sender], "No coincide");
    // Procesar elección...
}
```

**Aplicaciones:**
- Votaciones on-chain donde no quieres que otros vean tu voto hasta que todos hayan votado
- Subastas ciegas donde las ofertas se revelan simultáneamente
- Juegos de azar descentralizados (piedra-papel-tijera, loterías)

#### 2. Verificación de Identidad Sin Revelar Datos

```solidity
// Almacenar hash de credenciales en lugar de datos reales
mapping(address => bytes32) public credentialHashes;

function registerCredential(string memory credential) public {
    // Solo se almacena el hash, no la credencial real
    credentialHashes[msg.sender] = keccak256(abi.encodePacked(credential));
}

function verifyCredential(address user, string memory credential) public view returns (bool) {
    return keccak256(abi.encodePacked(credential)) == credentialHashes[user];
}
```

**Ventaja:** La información sensible (documento de identidad, certificado, etc.) nunca se almacena en la blockchain, solo su hash.

#### 3. Gestión de Cadena de Suministro

```solidity
struct Product {
    bytes32 detailsHash;  // Hash de origen, fecha, certificaciones
    uint256 timestamp;
    address supplier;
}

mapping(uint256 => Product) public products;

function registerProduct(uint256 productId, bytes32 detailsHash) public {
    products[productId] = Product({
        detailsHash: detailsHash,
        timestamp: block.timestamp,
        supplier: msg.sender
    });
}

function verifyProduct(uint256 productId, string memory details) public view returns (bool) {
    return keccak256(abi.encodePacked(details)) == products[productId].detailsHash;
}
```

**Aplicaciones:**
- Trazabilidad de alimentos (origen, fecha de producción)
- Autenticidad de productos de lujo
- Certificaciones y cumplimiento normativo

#### 4. Sistemas de Pago Condicional

```solidity
// Pago que se libera solo si se conoce la preimagen de un hash
struct HashedTimeLock {
    bytes32 hashLock;     // Hash del secreto
    uint256 timelock;     // Fecha límite
    uint256 amount;       // Cantidad bloqueada
    address recipient;
    bool claimed;
}

function createHTLC(bytes32 hashLock, address recipient, uint256 lockTime) 
    public payable returns (uint256) 
{
    uint256 id = nextId++;
    htlcs[id] = HashedTimeLock({
        hashLock: hashLock,
        timelock: block.timestamp + lockTime,
        amount: msg.value,
        recipient: recipient,
        claimed: false
    });
    return id;
}

function claim(uint256 id, string memory secret) public {
    HashedTimeLock storage htlc = htlcs[id];
    require(!htlc.claimed, "Ya reclamado");
    require(keccak256(abi.encodePacked(secret)) == htlc.hashLock, "Secreto incorrecto");
    require(block.timestamp <= htlc.timelock, "Expirado");
    
    htlc.claimed = true;
    payable(htlc.recipient).transfer(htlc.amount);
}
```

**Aplicación:** Atomic Swaps (intercambios atómicos entre blockchains diferentes) usando Hash Time Locked Contracts (HTLCs).

#### 5. Almacenamiento Eficiente de Datos Grandes

En lugar de almacenar documentos completos on-chain (muy costoso), se almacena solo el hash:

```solidity
mapping(bytes32 => bool) public documentHashes;

function notarizeDocument(bytes32 documentHash) public {
    documentHashes[documentHash] = true;
    emit DocumentNotarized(documentHash, msg.sender, block.timestamp);
}

function verifyDocument(bytes32 documentHash) public view returns (bool) {
    return documentHashes[documentHash];
}
```

**Casos de uso:**
- Notarización de documentos legales
- Proof of existence (prueba de que un archivo existía en cierto momento)
- Registros médicos (almacenar hash, documento real off-chain)

### Diferencias entre Funciones Hash en Ethereum

Ethereum ofrece varias opciones:

```solidity
// Keccak-256 (SHA-3 variante) - Más usado en Ethereum
bytes32 hash1 = keccak256(abi.encodePacked("data"));

// SHA-256 (Bitcoin standard) - Disponible pero más caro en gas
bytes32 hash2 = sha256(abi.encodePacked("data"));

// RIPEMD-160 - Usado en generación de direcciones Bitcoin
bytes20 hash3 = ripemd160(abi.encodePacked("data"));
```

**Costos de Gas (aproximados):**
- `keccak256`: ~30 gas + 6 gas por palabra
- `sha256`: ~60 gas + 12 gas por palabra
- `ripemd160`: ~600 gas + 120 gas por palabra

**Recomendación:** Usar `keccak256` en Ethereum por ser más eficiente y nativo del protocolo.

## Herramientas

- [Gadgets de seguridad](https://www.redeszone.net/reportajes/listas/gadgets-mejorar-seguridad/)
- [Check signature tool](http://www.dcmembers.com/skwire/download/sfv-ninja/)

## Criptografía Avanzada en Blockchain

### BLS Signatures (Boneh-Lynn-Shacham)

Esquema de firma criptográfica basado en emparejamientos bilineales (bilinear pairings) sobre curvas elípticas que permite agregación eficiente de firmas, crítico para escalabilidad y eficiencia en sistemas blockchain modernos.

**Fundamentos Matemáticos:**

A diferencia de ECDSA que opera sobre curvas elípticas estándar (secp256k1, secp256r1), BLS utiliza curvas con propiedades de emparejamiento como BLS12-381. Un emparejamiento bilineal es una función matemática e: G₁ × G₂ → Gₜ que satisface:

- Bilinealidad: e(aP, bQ) = e(P, Q)^(ab)
- No-degeneración: e(G₁, G₂) ≠ 1
- Computabilidad eficiente

Estas propiedades permiten verificar firmas agregadas sin necesidad de verificar cada firma individual.

**Proceso de Firma:**

1. **Generación de Claves:**
   - Clave privada: x ∈ Zₚ (número aleatorio)
   - Clave pública: PK = x·G₂ (punto en curva G₂)

2. **Firma de Mensaje:**
   - Hash del mensaje a punto de curva: H(m) ∈ G₁
   - Firma: σ = x·H(m)

3. **Verificación:**
   - Comprobar: e(σ, G₂) = e(H(m), PK)
   - Si la ecuación se cumple, la firma es válida

**Agregación de Firmas:**

La propiedad más poderosa de BLS es la agregación:

- Dadas n firmas σ₁, σ₂, ..., σₙ sobre mensajes m₁, m₂, ..., mₙ
- Firma agregada: σₐgg = σ₁ + σ₂ + ... + σₙ (suma de puntos en la curva)
- Claves públicas agregadas: PKₐgg = PK₁ + PK₂ + ... + PKₙ
- Verificación agregada: e(σₐgg, G₂) = ∏ e(H(mᵢ), PKᵢ)

Crucialmente, **el tamaño de σₐgg es idéntico al de una firma individual** (48 bytes en BLS12-381), sin importar cuántas firmas se agreguen.

**Aplicaciones en Blockchain:**

**Ethereum Beacon Chain (Consenso PoS):**

Ethereum 2.0 utiliza BLS signatures como componente fundamental del consenso:

- **Agregación de attestations:** En cada época, miles de validadores firman attestations (votos sobre bloques válidos). Agregar estas firmas reduce drásticamente el ancho de banda:
  - Sin agregación: 10,000 validadores × 96 bytes/firma = 960 KB
  - Con BLS agregado: 1 firma = 96 bytes (reducción >99%)

- **Sync committees:** Comités de 512 validadores que firman headers de bloques para light clients. Una firma agregada representa el consenso de todo el comité.

- **Slashing proofs:** Evidencia de comportamiento malicioso puede incluir múltiples firmas agregadas de forma compacta.

Ethereum usa la curva BLS12-381 con firmas de 96 bytes y claves públicas de 48 bytes. [EIP-2537](https://eips.ethereum.org/EIPS/eip-2537) añadió precompiles para operaciones BLS eficientes en contratos inteligentes.

**Optimistic Rollups y ZK-Rollups:**

L2 solutions utilizan BLS para agregar firmas de múltiples transacciones en un batch:

- **Arbitrum:** Validadores firman bloques. Firmas agregadas reducen costo de verificación on-chain.
- **zkSync y StarkNet:** Aunque usan ZK-proofs como método principal, BLS complementa para firmas de operadores en data availability.

**Multisig Eficiente:**

Tradicional multisig en Ethereum (Safe/Gnosis) requiere incluir todas las firmas ECDSA individuales en la transacción, incrementando linealmente el gas:

- 3-of-5 multisig con ECDSA: ~5 firmas × 65 bytes = 325 bytes + lógica verificación
- Mismo esquema con BLS: 1 firma agregada = 96 bytes

Ahorro de gas significativo en organizaciones con múltiples firmantes.

**Ventajas:**

- **Agregación de firmas:** Múltiples firmas → una firma del mismo tamaño. Reducción dramática de ancho de banda y storage.
- **Verificación batch eficiente:** Verificar n firmas agregadas es más rápido que verificar n firmas individuales.
- **Umbral nativo:** Esquemas threshold (t-of-n) son naturalmente implementables sin complejidad adicional.
- **Determinismo:** Como ECDSA, la generación de firma es determinista (no requiere nonce aleatorio).

**Desventajas:**

- **Emparejamientos costosos:** Operaciones de pairing son computacionalmente más caras que multiplicación escalar de ECDSA (aunque el ahorro en agregación compensa en casos de múltiples firmas).
- **Claves públicas más grandes:** 48 bytes en BLS12-381 vs 33 bytes en ECDSA comprimido.
- **Rogue key attacks:** Sin medidas de protección, un atacante puede elegir clave pública maliciosa PK* = PK - PKₘₐₗ para cancelar la firma honesta en agregación. Solución: proof-of-possession (PoP) donde cada firmante demuestra conocimiento de su clave privada.
- **Implementación compleja:** Requiere aritmética de curvas con pairing, bibliotecas especializadas, superficie de ataque mayor.

**Implementaciones y Herramientas:**

- **py_ecc:** Implementación Python de BLS12-381 usada en especificación de Ethereum beacon chain.
- **blst:** Biblioteca C/C++ de alta performance usada por clientes Ethereum (Prysm, Lighthouse).
- **noble-curves:** Implementación JavaScript/TypeScript auditable de BLS12-381.
- **Apache Milagro:** Suite criptográfica multi-lenguaje con soporte BLS.

**Seguridad:**

- **Nivel de seguridad:** BLS12-381 ofrece ~128 bits de seguridad, equivalente a AES-128 o RSA-3072.
- **Resistencia cuántica:** Como ECDSA, BLS es vulnerable a algoritmo de Shor en computadoras cuánticas. No es post-cuántico.
- **Auditorías:** Implementaciones deben ser exhaustivamente auditadas. Bugs en aritmética de pairing pueden ser catastróficos.

**Recursos Adicionales:**

- [BLS Signatures for Beginners](https://ethresear.ch/t/pragmatic-signature-aggregation-with-bls/2105) - Ethereum Research
- [BLS12-381 For The Rest Of Us](https://hackmd.io/@benjaminion/bls12-381) - Ben Edgington
- [Pairing-Based Cryptography](https://www.iacr.org/archive/asiacrypt2008/53500001/53500001.pdf) - Paper académico fundacional
- [EIP-2537 Specification](https://eips.ethereum.org/EIPS/eip-2537) - BLS precompiles en Ethereum

### Schnorr Signatures y MuSig

Esquema de firma digital basado en el problema del logaritmo discreto, conocido por su simplicidad matemática, eficiencia y propiedades de agregación. Schnorr fue patentado hasta 2008, lo que retrasó su adopción. Bitcoin lo integró en 2021 mediante Taproot (BIP-340).

**Fundamentos de Schnorr:**

A diferencia de ECDSA que requiere aritmética modular compleja y nonces críticos, Schnorr tiene estructura matemática más elegante:

**Generación de Claves:**

- Clave privada: x ∈ Zₙ (escalar aleatorio)
- Clave pública: P = x·G (punto en curva elíptica)

**Proceso de Firma:**

1. Generar nonce aleatorio: k ∈ Zₙ
2. Calcular R = k·G
3. Calcular challenge: e = H(R || P || m) donde m es el mensaje
4. Calcular s = k + e·x
5. Firma: (R, s)

**Verificación:**

1. Recalcular: e = H(R || P || m)
2. Verificar: s·G = R + e·P
3. Si la ecuación se cumple, la firma es válida

**Linealidad y Agregación:**

La propiedad fundamental de Schnorr es la linealidad:

- Si σ₁ = (R₁, s₁) firma mensaje m con clave x₁
- Y σ₂ = (R₂, s₂) firma el mismo mensaje m con clave x₂
- Entonces σₐgg = (R₁ + R₂, s₁ + s₂) es firma válida para clave agregada x₁ + x₂

Esto habilita **signature aggregation** y **multisig nativo** sin smart contracts.

**MuSig: Multisignatures con Schnorr:**

MuSig (Multi-Signature) es un protocolo que permite a múltiples partes colaborar para producir una única firma Schnorr indistinguible de una firma individual.

**Variantes de MuSig:**

**MuSig1 (Original):**

- Requiere tres rondas de comunicación
- Vulnerable a rogue-key attacks sin medidas de protección
- Implementación inicial, no recomendado para producción

**MuSig2 (Actual estándar):**

- Dos rondas de comunicación
- Resistente a rogue-key attacks mediante key aggregation coefficient
- Usado en Bitcoin Taproot
- Proceso:

1. **Ronda 1 (Compromiso de nonce):**
   - Cada participante genera nonce rᵢ y comparte compromiso H(Rᵢ)

2. **Ronda 2 (Revelación de nonce):**
   - Cada participante revela Rᵢ
   - Todos verifican compromisos y calculan R = ∑Rᵢ

3. **Firma:**
   - Calcular clave pública agregada: P̃ = ∑aᵢ·Pᵢ donde aᵢ = H(L || Pᵢ) y L es lista de todas las claves
   - Cada participante calcula sᵢ = rᵢ + H(R || P̃ || m)·aᵢ·xᵢ
   - Firma final: s = ∑sᵢ

**MuSig-DN (Deterministic Nonces):**

- Elimina requisito de generación de nonces aleatorios
- Nonces derivados determinísticamente de clave privada y mensaje
- Previene ataques de reutilización de nonce

**FROST (Flexible Round-Optimized Schnorr Threshold):**

- Extensión de MuSig para firmas threshold (t-of-n)
- Permite que subconjunto de participantes firme sin revelar quiénes específicamente
- Mejor privacidad que MuSig simple

**Implementación en Bitcoin Taproot (BIP-340, BIP-341, BIP-342):**

Taproot, activado en Bitcoin en noviembre 2021, introdujo Schnorr signatures como método de firma estándar:

**Ventajas para Bitcoin:**

- **Indistinguibilidad:** Transacciones multisig son idénticas a transacciones single-sig on-chain. Mejor privacidad.
- **Eficiencia:** Una firma Schnorr agregada (64 bytes) vs múltiples firmas ECDSA (65 bytes × n firmantes).
- **Menor costo:** Transacciones multisig usan menos block space → fees más bajos.
- **Script paths ocultos:** Taproot permite condiciones de gasto complejas (timelocks, hashlocks) que solo se revelan si se usan, no por defecto.

**Ejemplo Comparativo:**

- **Pre-Taproot multisig 3-of-5:** Transacción incluye script explícito con 5 claves públicas (33 bytes cada una) y 3 firmas ECDSA (65 bytes cada una). Total visible on-chain: ~360 bytes.

- **Post-Taproot MuSig 3-of-5:** Transacción incluye 1 clave pública agregada (32 bytes) y 1 firma Schnorr (64 bytes). Total: 96 bytes. **Reducción ~73%**.

Además, observadores externos no pueden determinar que es multisig, mejorando privacidad.

**Threshold Signatures con Schnorr:**

Esquemas t-of-n donde cualquier subconjunto de t participantes puede generar firma válida:

- **FROST:** Protocolo threshold optimizado, 2 rondas, sin trusted dealer
- **Uso en custodia institucional:** Fondos que requieren aprobación de, por ejemplo, 5 de 9 ejecutivos
- **Privacidad mejorada:** No se revela on-chain cuántos firmantes participaron ni quiénes específicamente

**Ventajas de Schnorr sobre ECDSA:**

- **Linealidad matemática:** Agregación de firmas y claves es trivial (suma de puntos).
- **Simplicidad de implementación:** Menos propenso a bugs que ECDSA.
- **Seguridad demostrable:** Prueba de seguridad en modelo random oracle, asumiendo dureza del logaritmo discreto.
- **Batch verification:** Verificar múltiples firmas Schnorr simultáneamente es más eficiente que verificarlas individualmente.
- **No-maleabilidad nativa:** ECDSA sufre de transaction malleability (firma puede modificarse sin invalidarla), Schnorr no.

**Desventajas:**

- **Adopción limitada:** Solo Bitcoin Taproot y algunos proyectos (Polkadot, Cardano usan Ed25519 que es variante de Schnorr). Ethereum sigue usando ECDSA.
- **Requerimiento de coordinación:** MuSig requiere interacción entre firmantes (múltiples rondas), mientras ECDSA multisig puede ser asíncrono.
- **Rogue-key attacks:** Sin protección adecuada (key aggregation coefficients), atacante puede manipular clave agregada.

**Aplicaciones Más Allá de Bitcoin:**

**Lightning Network:**

- Canales de pago aprovechan Schnorr para transacciones multisig eficientes
- Schnorr/Taproot permite channel factories y splice-in/out más eficientes

**Monero (RandomX):**

- Usa ring signatures basadas en Schnorr para privacidad
- Permite ofuscar quién específicamente firmó entre múltiples posibles firmantes

**Zcash Orchard:**

- Usa RedDSA (variante de Schnorr sobre curva Jubjub) en shielded transactions

**Comparación BLS vs Schnorr:**

| Característica | BLS | Schnorr |
|----------------|-----|----------|
| Base matemática | Emparejamientos bilineales | Logaritmo discreto |
| Agregación | Nativa, cualquier combinación | Requiere coordinación (MuSig) |
| Tamaño firma | 96 bytes (BLS12-381) | 64 bytes (secp256k1) |
| Tamaño clave pública | 48 bytes | 32 bytes |
| Verificación agregada | Eficiente via pairings | Batch verification disponible |
| Adopción blockchain | Ethereum PoS, L2s | Bitcoin Taproot, Polkadot |
| Complejidad implementación | Alta (pairings) | Media (aritmética curva) |
| Rondas de comunicación multisig | 0 (no interactivo) | 2 (MuSig2) |
| Threshold nativo | Sí | Sí (FROST) |
| Privacidad multisig | Firmas indistinguibles | Firmas indistinguibles |

**Recursos Adicionales:**

- [BIP-340: Schnorr Signatures for secp256k1](https://github.com/bitcoin/bips/blob/master/bip-0340.mediawiki)
- [BIP-341: Taproot](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki)
- [MuSig2 Paper](https://eprint.iacr.org/2020/1261.pdf) - Especificación académica
- [FROST Paper](https://eprint.iacr.org/2020/852.pdf) - Threshold signatures
- [Taproot Workshop](https://bitcoinops.org/en/schorr-taproot-workshop/) - Bitcoin Optech
- [Schnorr Signatures Overview](https://github.com/sipa/bips/blob/bip-schnorr/bip-schnorr.mediawiki) - Pieter Wuille

## Commit-Reveal Schemes

Los esquemas commit-reveal son primitivas criptográficas que permiten comprometerse a un valor sin revelarlo inmediatamente, previniendo manipulación retroactiva. Son fundamentales para garantizar fairness en escenarios donde el orden de revelación podría ser explotado.

**Funcionamiento básico:**

1. **Commit phase:** Usuario calcula hash de su valor secreto: `commitment = hash(secret + salt)`. Publica commitment on-chain
2. **Waiting period:** Otros participantes publican sus commitments sin conocer valores de otros
3. **Reveal phase:** Cada participante publica su valor original + salt. Smart contract verifica `hash(revealed_value + salt) == commitment`
4. **Execution:** Solo valores válidos (cuyo hash coincide con commitment) se aceptan. Valores no revelados son descartados

**Por qué funciona:** Hash unidireccional imposibilita calcular `secret` desde `commitment`. Salt previene ataques de diccionario contra valores predecibles (ej. números 1-100). Una vez publicado commitment, usuario no puede cambiar su valor porque cualquier modificación produciría hash diferente.

**Casos de uso en blockchain:**

- **NFT Fair Mints:** Previene sniping. Usuarios commit durante mint window, reveal después. El contrato asigna NFTs basándose en reveals, no en velocidad de transacción
- **Voting privado:** DAOs permiten votar sin revelar opción hasta que periodo de votación termine. Previene bandwagoning donde votos tardíos copian mayoría
- **Generación aleatoria descentralizada:** Múltiples participantes commiten entropía, revelan, y XOR de todos los valores genera semilla aleatoria que nadie pudo predecir
- **Time-locked secrets:** Subastas ciegas donde bids se commitean durante periodo, revelan después. Ganador es mayor bid, pero nadie conoció bids de otros durante subasta
- **Multiplayer gaming:** Commits aseguran que movimientos simultáneos no puedan reaccionar a acciones de oponente (piedra-papel-tijera on-chain)

**Limitaciones:** Requiere dos transacciones on-chain (commit + reveal), duplicando costos de gas. Si usuario no revela, su participación es invalidada pero commitment consume espacio. Esquemas deben manejar non-revelation mediante timeouts o penalizaciones de stake.

## Recursos Adicionales

- [SHA-256 en Bitcoin](https://academy.bit2me.com/sha256-algoritmo-bitcoin/)
- [Ataques DoS](https://academy.bit2me.com/que-son-ataques-dos/)
- [Firma digital ciega](https://es.wikipedia.org/wiki/Firma_digital_ciega)
- [Web of Trust](https://en.wikipedia.org/wiki/Web_of_trust)
- [Scrypt Function](https://en.wikipedia.org/wiki/Scrypt)
- [Curvas Elípticas Explicadas](https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/)
- [ECDSA Bitcoin Wiki](https://en.bitcoin.it/wiki/Elliptic_Curve_Digital_Signature_Algorithm)
- [Commit-Reveal Schemes](https://en.wikipedia.org/wiki/Commitment_scheme) - Wikipedia

