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

Según bits de algoritmo, el SHA-256 es de 256 bits o 32 bytes. Cada byte permite dos números hexadecimales, es decir, representación de posición fija de 64 caracteres.

```bash
SHA-256: 256 bits = 32 bytes = 64 caracteres hex
Input: "blockchain"
Output: ef7797e13d3a75526946a3bcf00daec9fc9c9c4d51ddc7cc5df888f74dd434d1
        |<---------------------- 64 caracteres ---------------------->|
```

Input alimenta a función de hash y tiene como resultado digest o digestión (como el hash de la comida). Es una función unidireccional: fácil calcular hash desde mensaje, imposible calcular mensaje desde hash.

Propiedades importantes:

Determinista: mismo input siempre produce mismo output. Resistencia a preimagen: dado hash, imposible encontrar mensaje original. Resistencia a colisiones: imposible encontrar dos mensajes con mismo hash. Efecto avalancha: cambio mínimo en input produce hash completamente diferente.

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

## Herramientas

- [Gadgets de seguridad](https://www.redeszone.net/reportajes/listas/gadgets-mejorar-seguridad/)
- [Check signature tool](http://www.dcmembers.com/skwire/download/sfv-ninja/)

## Recursos Adicionales

- [SHA-256 en Bitcoin](https://academy.bit2me.com/sha256-algoritmo-bitcoin/)
- [Ataques DoS](https://academy.bit2me.com/que-son-ataques-dos/)
- [Firma digital ciega](https://es.wikipedia.org/wiki/Firma_digital_ciega)
- [Web of Trust](https://en.wikipedia.org/wiki/Web_of_trust)
- [Scrypt Function](https://en.wikipedia.org/wiki/Scrypt)
- [Curvas Elípticas Explicadas](https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/)
- [ECDSA Bitcoin Wiki](https://en.bitcoin.it/wiki/Elliptic_Curve_Digital_Signature_Algorithm)

