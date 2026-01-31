# Attestation Infrastructure: Arquitectura Técnica EAS

Este documento profundiza en la infraestructura de attestations on-chain, con foco principal en [Ethereum Attestation Service (EAS)](https://attest.sh/), el estándar de facto para attestations verificables en Ethereum y L2s. Complementa la introducción conceptual en [7-1-identity.md](../101/7-1-identity.md).

## Arquitectura de EAS

EAS proporciona smart contracts estandarizados que permiten a cualquiera emitir y consumir attestations sin desplegar infraestructura propia. La arquitectura consta de tres componentes principales:

### 1. Schema Registry

El Schema Registry es un contrato que almacena las plantillas (schemas) que definen la estructura de las attestations. Cualquiera puede registrar un schema que otros pueden reutilizar.

**Estructura de un Schema**:

```solidity
struct Schema {
    bytes32 uid;           // Identificador único del schema
    address resolver;      // Contrato resolver opcional
    bool revocable;        // Si las attestations son revocables
    string schema;         // Definición del schema en formato ABI
}
```

**Ejemplo de schema práctico**:

```javascript
// Schema para certificación educativa
"address student, string courseName, uint256 completionDate, uint8 grade"

// Schema para KYC básico
"bool isVerified, uint8 verificationLevel, uint256 expirationDate"

// Schema para reputación DAO
"bytes32 daoId, string role, uint256 contributionScore, bool isActive"
```

El schema define los campos que cada attestation de ese tipo debe incluir. Usar schemas estandarizados permite composabilidad: múltiples emisores pueden emitir attestations del mismo schema que verificadores pueden consumir uniformemente.

### 2. Attestation Contract

El contrato principal donde se registran las attestations. Cada attestation se almacena con metadata completa:

```solidity
struct Attestation {
    bytes32 uid;              // ID único de esta attestation
    bytes32 schema;           // Schema que usa
    uint64 time;              // Timestamp de creación
    uint64 expirationTime;    // Timestamp de expiración (0 = sin expiración)
    uint64 revocationTime;    // Timestamp de revocación (0 = no revocada)
    bytes32 refUID;           // Referencia a otra attestation (para chains)
    address recipient;        // A quién se emite la attestation
    address attester;         // Quién emite la attestation
    bool revocable;           // Si puede ser revocada
    bytes data;               // Datos codificados según el schema
}
```

**Funciones principales**:

```solidity
// Crear attestation on-chain
function attest(AttestationRequest calldata request) 
    external payable returns (bytes32);

// Crear attestation off-chain (solo registra hash)
function attestByDelegation(DelegatedAttestationRequest calldata request) 
    external payable returns (bytes32);

// Revocar attestation
function revoke(RevocationRequest calldata request) 
    external payable returns (bytes32);

// Consultar attestation
function getAttestation(bytes32 uid) 
    external view returns (Attestation memory);
```

### 3. Resolver Contracts (Opcional)

Los resolvers son smart contracts custom que se ejecutan automáticamente cuando se crea o revoca una attestation. Permiten implementar lógica de negocio compleja:

**Ejemplos de uso de resolvers**:

**Verificación de elegibilidad**: Resolver verifica que el recipient cumple requisitos antes de permitir la attestation (ej. debe poseer cierto NFT, debe estar en whitelist)

**Pago condicional**: Transferir tokens automáticamente al recipient cuando recibe attestation (ej. bounty por completar tarea)

**Attestations encadenadas**: Verificar que existe attestation previa necesaria (ej. para emitir diploma de posgrado, debe existir attestation de grado)

**Límites temporales**: Prevenir emisión de múltiples attestations del mismo tipo en periodo corto (anti-spam)

**Esquema de código de resolver básico**:

```solidity
contract EducationResolver is SchemaResolver {
    function onAttest(
        Attestation calldata attestation, 
        uint256 value
    ) internal override returns (bool) {
        // Decodificar datos
        (address student, string memory course, uint256 date, uint8 grade) = 
            abi.decode(attestation.data, (address, string, uint256, uint8));
        
        // Validar que el grade es válido (0-100)
        require(grade <= 100, "Invalid grade");
        
        // Validar que el attester está autorizado (lista de universidades)
        require(authorizedUniversities[attestation.attester], "Not authorized");
        
        return true; // Permitir attestation
    }
    
    function onRevoke(
        Attestation calldata attestation, 
        uint256 value
    ) internal override returns (bool) {
        // Lógica custom para revocación
        return true;
    }
}
```

## On-Chain vs Off-Chain: Trade-offs Técnicos

EAS soporta dos modos de almacenamiento con trade-offs muy diferentes:

### Attestations On-Chain

**Funcionamiento**: Datos completos de la attestation se almacenan en el smart contract de EAS en la blockchain.

**Ventajas**:
- ✅ **Verificabilidad máxima**: Cualquier smart contract puede leer y actuar sobre la attestation directamente
- ✅ **Composabilidad nativa**: Protocolos DeFi pueden condicionar operaciones a posesión de attestations específicas
- ✅ **Inmutabilidad garantizada**: Una vez registrada, la attestation existe permanentemente en la blockchain
- ✅ **Descubrimiento público**: Exploradores blockchain pueden indexar y buscar attestations
- ✅ **Timestamps autoritativos**: El tiempo de creación está garantizado por consenso blockchain

**Desventajas**:
- ❌ **Gas costs significativos**: Cada attestation requiere transacción on-chain. En Ethereum mainnet puede costar $5-50 USD según congestión
- ❌ **Privacidad cero**: Todos los datos son públicos para siempre. Inapropiado para información sensible
- ❌ **Límite de tamaño**: Blockchains tienen límites prácticos de tamaño de datos (gas limits)
- ❌ **Latencia**: Confirmación requiere tiempo de bloque (12s en Ethereum, más en otros chains)

**Análisis de costos (Ethereum mainnet, gas 30 gwei)**:
- Attestation simple (3 campos): ~70,000 gas ≈ $6.30 USD
- Attestation compleja (10 campos): ~120,000 gas ≈ $10.80 USD
- Revocación: ~45,000 gas ≈ $4.05 USD

En L2s como Optimism, Arbitrum, Base, Polygon zkEVM, estos costos se reducen 10-100x:
- Optimism: ~$0.10-0.30 por attestation
- Arbitrum: ~$0.08-0.25 por attestation
- Base: ~$0.05-0.15 por attestation

**Casos de uso ideales**:
- Credenciales que otros smart contracts necesitan leer (membresía DAO, nivel KYC para DeFi)
- Attestations públicas donde privacidad no importa (POAPs, certificados de cursos públicos)
- Contextos donde composabilidad on-chain justifica el costo

### Attestations Off-Chain

**Funcionamiento**: La attestation completa se almacena fuera de blockchain (IPFS, Arweave, Ceramic, base de datos). Solo el hash criptográfico se registra on-chain.

**Ventajas**:
- ✅ **Gas costs mínimos**: Solo registrar hash de 32 bytes cuesta ~30,000 gas ≈ $2.70 (mainnet) o $0.05 (L2)
- ✅ **Privacidad mejorada**: Datos sensibles no tocan blockchain. Solo compartes attestation completa con verificadores específicos
- ✅ **Sin límite de tamaño**: Puedes incluir megabytes de datos (documentos, imágenes) en la attestation
- ✅ **Revocabilidad flexible**: Puedes actualizar el estado off-chain sin transacción on-chain

**Desventajas**:
- ❌ **No componible on-chain**: Smart contracts no pueden leer los datos directamente
- ❌ **Requiere infraestructura adicional**: Necesitas almacenamiento descentralizado (IPFS) o servidor
- ❌ **Verificación multi-paso**: Verificador debe obtener attestation completa, computar hash, comparar con on-chain
- ❌ **Riesgo de disponibilidad**: Si el storage off-chain falla, la attestation se pierde aunque el hash persista

**Estructura técnica**:

```javascript
// 1. Crear attestation off-chain
const attestationData = {
  schema: "0x...",
  recipient: "0xRecipient...",
  attester: "0xAttester...",
  time: 1704067200,
  expirationTime: 0,
  data: encodedData, // Puede ser arbitrariamente grande
  revocable: true
};

// 2. Computar hash
const attestationHash = keccak256(
  abi.encode(attestationData)
);

// 3. Subir attestation completa a IPFS
const ipfsHash = await ipfs.add(JSON.stringify(attestationData));

// 4. Registrar solo el hash on-chain con metadata mínima
await eas.attestOffChain({
  schema: schemaId,
  dataHash: attestationHash,
  recipient: recipientAddress
});

// 5. Para verificar, verificador:
// a) Obtiene attestation completa desde IPFS usando ipfsHash
// b) Recomputa hash de los datos
// c) Compara hash computado con el registrado on-chain
// d) Si coinciden, attestation es auténtica
```

**Casos de uso ideales**:
- Credenciales personales sensibles (datos médicos, historial crediticio, documentos KYC completos)
- Attestations con documentos adjuntos (diplomas con PDF, certificaciones con imágenes)
- Escenarios de alto volumen donde costo on-chain es prohibitivo
- Comunicación bilateral donde composabilidad pública no es necesaria

### Estrategia Híbrida

Muchas aplicaciones usan ambos modos estratégicamente:

**Metadata on-chain, detalles off-chain**: Registra on-chain campos mínimos que smart contracts necesitan (ej. `isVerified: bool, level: uint8`), mantiene detalles completos off-chain (documentos de respaldo, justificaciones)

**Public on-chain, private off-chain**: Attestations públicas (POAPs, certificados de cursos) van on-chain para máxima visibilidad. Attestations sensibles (KYC, salud) van off-chain con hashes on-chain solo para verificabilidad cuando usuario elige revelar

**Agregación periódica**: Acumula múltiples attestations off-chain y periódicamente publica un Merkle root on-chain que compromete a todas ellas, balanceando costo con verificabilidad

## Schemas: Diseño y Best Practices

El diseño de schemas es crítico para lograr interoperabilidad y evitar fragmentación del ecosistema.

### Principios de Diseño

**1. Minimalismo**: Incluye solo campos esenciales. Schemas simples son más reutilizables y baratos de almacenar.

```javascript
// ❌ Schema sobrecargado
"string firstName, string lastName, string middleName, uint256 birthDate, 
 string birthCity, string birthCountry, string nationality, string passportNumber"

// ✅ Schema minimal para mayoría de edad
"bool isOver18, uint256 verifiedDate"
```

**2. Extensibilidad**: Usa schemas base que otros pueden extender.

```javascript
// Schema base reutilizable
bytes32 constant BASE_IDENTITY = "address user, bool isVerified";

// Extensiones específicas referencian el base
"bytes32 baseAttestation, uint8 kycLevel, string jurisdiction"
```

**3. Tipos apropiados**: Usa tipos Solidity correctos para cada campo.

```javascript
// ❌ Todo como string
"string userId, string score, string timestamp"

// ✅ Tipos específicos
"address user, uint256 score, uint64 timestamp"
```

**4. Referencias**: Usa `bytes32 refUID` para crear chains de attestations relacionadas.

```javascript
// Attestation de grado universitario referencia attestation de admisión
{
  schema: DEGREE_SCHEMA,
  data: "string degreeName, uint256 graduationDate",
  refUID: admissionAttestationUID  // Link a attestation previa
}
```

### Schemas Estandarizados Existentes

La comunidad EAS ha desarrollado schemas estandarizados para casos comunes:

**Identity Verification**:
```
Schema UID: 0x...
Fields: bool isVerified, uint8 verificationLevel, uint256 expirationTimestamp
Usar para: KYC básico, proof of personhood
```

**Event Attendance**:
```
Schema UID: 0x...
Fields: bytes32 eventId, string eventName, uint256 attendanceDate
Usar para: Conferencias, hackathons, meetups (alternativa a POAP)
```

**Reputation Score**:
```
Schema UID: 0x...
Fields: bytes32 contextId, uint256 score, string category
Usar para: Reputación en DAOs, marketplaces, lending protocols
```

**Skill Endorsement**:
```
Schema UID: 0x...
Fields: address endorsee, string skillName, uint8 proficiencyLevel
Usar para: Endorsements profesionales, verificación de habilidades
```

Antes de crear schema custom, busca en el [Schema Explorer](https://base.easscan.org/schemas) si existe uno que puedas reutilizar. La interoperabilidad surge de schemas compartidos.

## Composabilidad: Construyendo sobre Attestations

El verdadero poder de EAS emerge cuando múltiples protocolos componen attestations de diferentes fuentes.

### Caso 1: Lending Protocol con Reputación Componible

Un protocolo de lending descentralizado (como Aave, Compound) tradicionalmente solo considera colateral. Con attestations, puede implementar "undercollateralized lending" basado en reputación:

```solidity
contract ReputationBasedLending {
    IEAS public eas;
    
    function checkBorrowEligibility(address borrower) 
        public view returns (uint256 maxLoanAmount) 
    {
        uint256 reputationScore = 0;
        
        // Check 1: ¿Tiene attestation KYC válida?
        Attestation memory kycAttestation = 
            eas.getAttestation(userKycAttestationUID[borrower]);
        if (kycAttestation.revocationTime == 0 && 
            kycAttestation.expirationTime > block.timestamp) {
            reputationScore += 100;
        }
        
        // Check 2: ¿Cuántas attestations de DAOs respetables tiene?
        uint256 daoMemberships = countDaoAttestations(borrower);
        reputationScore += daoMemberships * 50;
        
        // Check 3: ¿Tiene attestation de repago exitoso en otros protocolos?
        if (hasRepaymentHistory(borrower)) {
            reputationScore += 200;
        }
        
        // Check 4: ¿Gitcoin Passport score alto?
        uint256 gitcoinScore = getGitcoinPassportScore(borrower);
        reputationScore += gitcoinScore / 10;
        
        // Score determina loan amount sin colateral
        maxLoanAmount = reputationScore * 1e18; // Score → USDC
    }
}
```

Este contrato compone attestations de múltiples fuentes independientes (KYC provider, DAOs, otros lending protocols, Gitcoin) para tomar decisiones financieras informadas.

### Caso 2: Gobernanza Ponderada por Contribuciones

Una DAO puede ponderar votos según historial de contribuciones verificado mediante attestations:

```solidity
contract ContributionWeightedGovernance {
    function getVotingPower(address member) 
        public view returns (uint256) 
    {
        uint256 power = 1; // Voto base
        
        // +10 por cada PR merged (attestation de GitHub integration)
        power += countAttestations(member, PR_MERGED_SCHEMA) * 10;
        
        // +5 por cada audit realizado
        power += countAttestations(member, AUDIT_SCHEMA) * 5;
        
        // +20 por participación >6 meses (attestation de antigüedad)
        if (hasLongTermAttestation(member, MEMBERSHIP_SCHEMA, 180 days)) {
            power += 20;
        }
        
        // Cap máximo para prevenir centralización
        if (power > 100) power = 100;
        
        return power;
    }
}
```

### Caso 3: Marketplace con Trust Score

Un marketplace descentralizado (como OpenSea o Rarible) puede mostrar trust scores agregando attestations:

```javascript
async function calculateSellerTrustScore(sellerAddress) {
  let score = 0;
  
  // Attestations de compradores previos (5* ratings)
  const reviews = await eas.getAttestations({
    schema: REVIEW_SCHEMA,
    recipient: sellerAddress
  });
  const avgRating = reviews.reduce((sum, r) => 
    sum + decodeRating(r.data), 0) / reviews.length;
  score += avgRating * 20; // Max 100 puntos
  
  // Attestation KYC (bonus por identidad verificada)
  const kycAttestation = await eas.getAttestation(
    await getKycAttestationUID(sellerAddress)
  );
  if (kycAttestation && !kycAttestation.revoked) {
    score += 50;
  }
  
  // Attestations de volume histórico de ventas
  const salesVolume = await calculateSalesVolume(sellerAddress);
  score += Math.min(salesVolume / 1000, 50); // Max 50 puntos
  
  return Math.min(score, 200); // Score máximo: 200
}
```

### Patrones de Composición

**Aggregation**: Combinar múltiples attestations del mismo schema para score acumulativo

**Conditional Logic**: Requerir combinación específica de attestations (KYC AND membership AND reputation > threshold)

**Hierarchical**: Attestations que referencian otras como prerequisitos (diploma requiere admisión attestation)

**Temporal**: Ponderar attestations por edad (attestations recientes valen más)

**Weighted Aggregation**: Diferentes fuentes tienen diferentes pesos según confiabilidad

## Indexación y Consulta

Para aplicaciones que necesitan consultar attestations eficientemente, indexación off-chain es esencial.

### The Graph Protocol

[The Graph](https://thegraph.com/) indexa eventos de smart contracts y proporciona API GraphQL para consultas complejas.

**Subgraph para EAS**:

```graphql
type Attestation @entity {
  id: ID!
  schema: Schema!
  recipient: Bytes!
  attester: Bytes!
  time: BigInt!
  expirationTime: BigInt!
  revocationTime: BigInt!
  refUID: Bytes!
  data: Bytes!
}

type Schema @entity {
  id: ID!
  schema: String!
  resolver: Bytes
  revocable: Boolean!
  attestations: [Attestation!] @derivedFrom(field: "schema")
}
```

**Consultas ejemplo**:

```graphql
# Todas las attestations de un usuario
{
  attestations(where: { recipient: "0x..." }) {
    id
    schema {
      schema
    }
    attester
    time
    data
  }
}

# Attestations de un schema específico no revocadas
{
  attestations(
    where: { 
      schema: "0x...",
      revocationTime: 0
    }
  ) {
    recipient
    attester
    data
  }
}

# Attestations emitidas por emisor confiable
{
  attestations(
    where: { attester: "0xTrustedIssuer..." },
    orderBy: time,
    orderDirection: desc
  ) {
    recipient
    schema {
      schema
    }
    data
  }
}
```

### EASSCAN: Explorer Oficial

[EASSCAN](https://easscan.org/) es el block explorer oficial para EAS, disponible en múltiples chains:
- [Base EASSCAN](https://base.easscan.org/)
- [Optimism EASSCAN](https://optimism.easscan.org/)
- [Arbitrum EASSCAN](https://arbitrum.easscan.org/)

Proporciona:
- Búsqueda de attestations por UID, recipient, attester, schema
- Visualización de schemas con todas las attestations emitidas
- Estadísticas de uso (total attestations, schemas más usados)
- APIs REST para integración programática

## Seguridad y Consideraciones

### Confianza en Emisores

Las attestations son tan confiables como sus emisores. La verificación criptográfica prueba que el `attester` firmó la attestation, pero no prueba que el attester es confiable.

**Estrategias de mitigación**:

**Whitelists de emisores**: Protocolo mantiene lista curada de emisores autorizados
```solidity
mapping(address => bool) public trustedAttesters;
```

**Reputation de emisores**: Construir score basado en historial del emisor (cuántas attestations han emitido, cuántas fueron revocadas, feedback de usuarios)

**Stake requirements**: Emisores deben hacer stake de tokens. Si emiten attestations fraudulentas, stake es slasheado

**Attestations sobre attesters**: Meta-attestations que certifican que un emisor es confiable (emitidas por organizaciones de governance reconocidas)

### Privacidad y Selective Disclosure

Attestations on-chain públicas crean riesgos de privacidad. Si tu attestation KYC está on-chain con tu address Ethereum, cualquiera puede vincular tu identidad real con toda tu actividad blockchain.

**Mejores prácticas**:

**Minimal disclosure**: Solo registra on-chain el mínimo necesario. Para KYC, en lugar de `name, address, SSN`, registra solo `isVerified: true, level: 2`

**Zero-Knowledge Proofs**: Usa sistemas como [Privado ID](https://www.privadoid.com/) o [Sismo](https://www.sismo.io/) que permiten probar "tengo attestation con propiedad X" sin revelar la attestation completa

**Fresh addresses**: Recibe attestations sensibles en addresses dedicadas separadas de tu wallet principal de actividad

**Off-chain by default**: Usa attestations off-chain para datos sensibles, on-chain solo cuando composabilidad es esencial

### Immutability vs Rectification

Las attestations on-chain son permanentes por diseño. Si una attestation contiene error o información desactualizada, no puedes editarla, solo revocarla y emitir una nueva.

**Implicaciones**:

**Dato erróneo**: Si emisor registra información incorrecta, la attestation incorrecta existirá on-chain para siempre aunque sea revocada

**Derecho al olvido**: Conflicto con regulaciones como GDPR que garantizan derecho a eliminar datos personales. Attestations on-chain no pueden borrarse

**Estrategias**:

- Usa attestations off-chain para datos que pueden requerir rectificación
- Diseña schemas que no incluyan PII directamente (usa hashes en lugar de datos reales)
- Implementa sistemas de revocación + re-emisión como flujo estándar de corrección

## Costos y Optimizaciones

### Batching de Attestations

En lugar de emitir attestations individuales, agrupa múltiples en una sola transacción:

```solidity
function multiAttest(
    MultiAttestationRequest[] calldata requests
) external payable returns (bytes32[] memory);
```

**Ahorro**: ~40% gas por attestation cuando batches >10 attestations

### L2s y Rollups

Costos de attestation en diferentes chains (Enero 2026):

| Chain | Costo Attestation Simple | Confirmación |
|-------|------------------------|--------------|
| Ethereum Mainnet | $8-15 | 12 segundos |
| Optimism | $0.08-0.15 | 2 segundos |
| Arbitrum | $0.06-0.12 | 250ms |
| Base | $0.04-0.10 | 2 segundos |
| Polygon zkEVM | $0.05-0.12 | 10 segundos |

**Recomendación**: Para alto volumen de attestations, usa L2s como Base o Arbitrum. Para attestations críticas que requieren máxima seguridad, usa Ethereum mainnet.

### Data Encoding Eficiente

Usa tipos de datos apropiados para minimizar storage:

```solidity
// ❌ Ineficiente: 160 bytes
"string name, string email, string country"

// ✅ Eficiente: 32 bytes
"bytes32 nameHash, bytes32 emailHash, bytes2 countryCode"
```

## Casos de Uso Avanzados

### Credenciales Educativas Verificables

Universidad emite diplomas como attestations on-chain:

```javascript
const DEGREE_SCHEMA = "address student, bytes32 degreeHash, 
                       uint256 graduationDate, uint8 honorsLevel";

await eas.attest({
  schema: DEGREE_SCHEMA,
  data: encodeData([
    studentAddress,
    keccak256("Bachelor of Science in Computer Science"),
    1704067200,  // Graduation date
    3            // Honors: summa cum laude
  ]),
  recipient: studentAddress,
  expirationTime: 0,  // Nunca expira
  revocable: true     // Universidad puede revocar si descubre fraude
});
```

Empleador verifica diploma consultando attestation directamente sin contactar a la universidad.

### Supply Chain Tracking

Cada paso en supply chain recibe attestation:

```javascript
// Manufacturer attesta origen
attest({ schema: ORIGIN_SCHEMA, data: "factory: FactoryA, date: ...", recipient: productNFT })

// Shipper attesta transporte
attest({ schema: SHIPPING_SCHEMA, data: "route: A→B, temperature: 4°C", recipient: productNFT })

// Inspector attesta calidad
attest({ schema: QUALITY_SCHEMA, data: "passed: true, inspector: 0x...", recipient: productNFT })
```

Consumidor final escanea QR del producto y ve historial completo verificable.

### Sybil-Resistant Airdrops

Proyecto ejecuta airdrop solo a usuarios con attestation de humanidad:

```solidity
function claimAirdrop() external {
    // Requiere attestation de Gitcoin Passport o Proof of Humanity
    require(
        hasValidAttestation(msg.sender, GITCOIN_PASSPORT_SCHEMA) ||
        hasValidAttestation(msg.sender, POH_SCHEMA),
        "No humanity attestation"
    );
    
    require(!claimed[msg.sender], "Already claimed");
    claimed[msg.sender] = true;
    
    token.transfer(msg.sender, AIRDROP_AMOUNT);
}
```

Esto previene que bots farmeen airdrop con miles de wallets.

## Integración con Otros Protocolos

### Verifiable Credentials (VCs)

EAS y VCs son complementarios:
- **VCs**: Privadas, off-chain, controladas por usuario
- **EAS Attestations**: Públicas, on-chain, componibles por smart contracts

**Patrón híbrido**: Emisor emite VC al usuario off-chain (privacidad) y registra hash de la VC como attestation on-chain (verificabilidad pública opcional).

### ENS (Ethereum Name Service)

Vincula attestations a nombres ENS para UX mejorada:

```javascript
// En lugar de mostrar "0x1234...abcd tiene 5 attestations"
// Muestra "alice.eth tiene 5 attestations"

const ensName = await provider.lookupAddress(attestation.recipient);
```

### Lens Protocol / Farcaster

Redes sociales descentralizadas pueden integrar attestations como "verificación":

- Usuario con attestation KYC recibe badge de "Verificado"
- Usuario con attestation de contribuidor open-source recibe badge especial
- Contenido de usuarios con alta reputación (medida por attestations) se rankea más alto

## Referencias

- [EAS Documentation](https://docs.attest.sh/)
- [EAS GitHub](https://github.com/ethereum-attestation-service/eas-contracts)
- [EASSCAN Explorer](https://easscan.org/)
- [EAS Schema Registry](https://base.easscan.org/schemas)
- [Attestation Use Cases](https://docs.attest.sh/docs/category/use-cases/)

---

Este documento proporciona la base técnica completa para implementar y consumir attestations on-chain. Para casos de uso prácticos de identidad y reputación, consulta [7-2-reputation.md](../101/7-2-reputation.md) y [9-1-ecosystem-DApps.md](../101/9-1-ecosystem-DApps.md).
