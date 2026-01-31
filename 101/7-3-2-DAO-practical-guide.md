# Guía práctica: Cómo crear una DAO

Crear una DAO no es simplemente desplegar un contrato inteligente. Es diseñar un sistema de incentivos, coordinar humanos, gestionar riesgos técnicos y legales, y construir comunidad. Esta guía cubre el proceso completo desde la concepción hasta el lanzamiento.

## Antes de empezar: Preguntas fundamentales

Antes de escribir una sola línea de código, debes responder honestamente estas preguntas:

**¿Realmente necesitas una DAO?**

No todo proyecto necesita gobernanza descentralizada. Considera alternativas:
- Si eres una startup temprana que necesita moverse rápido: una empresa tradicional con tokens futuros puede ser mejor.
- Si solo necesitas crowdfunding: una ICO/IDO sin gobernanza formal puede ser suficiente.
- Si tu comunidad es pequeña (<50 personas): un multisig con comunicación informal puede funcionar.

Una DAO tiene sentido cuando:
- Gestionas recursos compartidos que requieren coordinación de muchos stakeholders.
- Necesitas legitimidad descentralizada para que usuarios confíen (especialmente en DeFi).
- Tu protocolo generará ingresos que deben distribuirse de forma transparente.
- Quieres alinear incentivos a largo plazo entre fundadores, inversores y comunidad.

**¿Qué tipo de DAO necesitas?**

Diferentes arquetipos tienen diferentes requisitos técnicos:

- **Protocol DAO**: Gobierna un protocolo DeFi (ej. Uniswap, Aave). Necesita integración profunda con smart contracts, timelocks de seguridad, y capacidad de actualizar parámetros técnicos.

- **Investment DAO**: Gestiona fondos para invertir colectivamente (ej. MolochDAO, The LAO). Necesita gestión de tesorería robusta, due diligence descentralizado, y mecanismos de rage quit.

- **Grants DAO**: Distribuye fondos a proyectos de bien público (ej. Gitcoin). Necesita sistemas de evaluación, curación comunitaria, y posiblemente quadratic funding.

- **Collector DAO**: Compra y gestiona NFTs u otros activos (ej. PleasrDAO). Necesita multisigs seguros, sistema de valuación, y posibilidad de fraccionar propiedad.

- **Social DAO**: Coordina comunidad sin fines financieros explícitos (ej. Friends With Benefits). Necesita mecanismos de membresía, reputación, y gobernanza social más que financiera.

**¿Cuánta descentralización realmente quieres?**

Sé honesto sobre el espectro descentralización-eficiencia:

- **Descentralización máxima**: Todo on-chain, cualquiera puede proponer, votos vinculantes. Lento, costoso, riesgo de gridlock. Ideal para protocolos maduros con stakes altos.

- **Descentralización progresiva**: Comienzas con equipo central tomando decisiones operativas, gradualmente transfieres control conforme madura la comunidad. Recomendado para mayoría de proyectos.

- **Híbrido pragmático**: DAO vota decisiones estratégicas (tokenomics, partnerships, uso de tesorería), equipo ejecuta operaciones diarias. Balance común en producción.

- **DAO cosmético**: Token sin poder real, equipo toma decisiones importantes. Evitar: genera desconfianza y potenciales problemas legales.

## Fase 1: Diseño de la gobernanza

Antes de tocar código, diseña el sistema de gobernanza en papel. Este es el paso más crítico y subestimado.

### 1.1. Tokenomics del token de gobernanza

**Suministro total y distribución inicial**

Define claramente cómo se reparte el 100% del supply inicial:

```
Ejemplo - Distribución típica de protocol DAO:

Team & Advisors:        20%  (vesting 4 años, cliff 1 año)
Early Investors:        15%  (vesting 2-3 años)
Community Treasury:     30%  (controlado por DAO)
Liquidity Mining:       25%  (distribuido gradualmente)
Public Sale:           10%  (inmediatamente líquido)
```

**Vesting schedules**

Nunca distribuyas todo el supply de inmediato. Implementa vesting para alinear incentivos a largo plazo:

- **Cliff**: Período inicial donde no se libera nada (típicamente 6-12 meses).
- **Vesting lineal**: Liberación gradual después del cliff (típicamente 2-4 años).
- **Lockups diferentes por categoría**: Team con vesting más largo que community.

**Inflación vs deflación**

Decide si el supply será fijo o inflacionario:

- **Supply fijo** (ej. Bitcoin, Uniswap inicial): Escasez garantizada, pero dificulta incentivos a largo plazo para nuevos contribuidores.

- **Inflación moderada** (ej. 2-5% anual): Permite recompensar participación sostenida sin diluir excesivamente holders existentes.

- **Deflación mediante burn** (ej. fee burning de EIP-1559): Reduce supply usando ingresos del protocolo para recomprar y quemar tokens.

**Utilidad más allá de gobernanza**

Un token solo de gobernanza tiene problema: ¿por qué holdearlo si no genera retornos? Considera utilidades adicionales:

- **Staking con rewards**: Bloquea tokens para ganar yield (ej. Curve's veCRV).
- **Fee sharing**: Distribuye parte de los ingresos del protocolo (ej. GMX).
- **Boosts y privilegios**: Mayor peso en rewards, acceso temprano a features (ej. Convex).
- **Descuentos en fees**: Pagar comisiones con el token obtiene descuento (ej. BNB en Binance).

### 1.2. Mecanismo de votación

**Quórum mínimo**

Establece cuántos tokens deben participar para que un voto sea válido:

- **Quórum bajo (2-5%)**: Fácil aprobar propuestas, riesgo de captura por minoría activa.
- **Quórum medio (10-15%)**: Balance razonable para DAOs medianas.
- **Quórum alto (25%+)**: Difícil alcanzar, puede paralizar gobernanza.

Considera quórum adaptativo: si la participación es consistentemente baja, el quórum se ajusta automáticamente.

**Umbral de aprobación**

Define qué mayoría se necesita para aprobar:

- **Mayoría simple (>50%)**: Estándar para decisiones rutinarias.
- **Supermayoría (66-75%)**: Para cambios importantes (ej. actualizar contratos core).
- **Unanimidad práctica (90%+)**: Solo para decisiones existenciales (ej. migrar a otra blockchain).

**Duración de votación**

- **Corta (3-5 días)**: Agilidad pero riesgo de participación baja.
- **Media (7-10 días)**: Estándar para mayoría de propuestas.
- **Larga (14+ días)**: Decisiones críticas que requieren debate extenso.

**Período de delay (Timelock)**

Crucial para seguridad: separa aprobación de ejecución con un delay:

- **24-48 horas**: Mínimo para detectar propuestas maliciosas obvias.
- **3-7 días**: Estándar de industria, permite reacción comunitaria.
- **14+ días**: Para cambios estructurales profundos.

Durante el timelock, la comunidad puede:
- Analizar técnicamente qué hará exactamente el código.
- Organizar rechazo social si se detecta malicia.
- Rage quit si están en desacuerdo fundamental.

### 1.3. Delegación

Implementa delegación desde el inicio para combatir baja participación:

**Características esenciales**:
- Delegación revocable en cualquier momento.
- Posibilidad de votar directamente incluso si has delegado (override temporal).
- Delegados deben ser transparentes: perfiles públicos, historial de votos visible.

**Incentivos para delegados**:
- Reconocimiento social y reputación.
- Posibles grants de la DAO para delegados activos.
- Dashboards que muestran rendimiento de delegados.

### 1.4. Tipos de propuestas

Define diferentes tipos de propuestas con diferentes requisitos:

**Propuestas de señalización** (no vinculantes):
- Quórum bajo, mayoría simple.
- Off-chain (Snapshot).
- Usadas para gauging sentiment antes de propuestas formales.

**Propuestas operativas** (ajustes de parámetros):
- Quórum medio, mayoría simple.
- Timelock corto (2-3 días).
- Ej: cambiar fee de 0.3% a 0.25%.

**Propuestas de financiamiento** (grants, partnerships):
- Quórum medio, mayoría simple.
- Timelock medio (5-7 días).
- Requieren propuesta estructurada con milestones y presupuesto.

**Propuestas críticas** (actualizar contratos core):
- Quórum alto, supermayoría.
- Timelock largo (14 días).
- Requieren auditoría independiente antes de votación.

**Propuestas de emergencia**:
- Ejecutadas por multisig de emergencia.
- Solo para pausar protocolo ante exploit activo.
- Deben ser ratificadas por DAO después del hecho.

## Fase 2: Desarrollo técnico

Una vez diseñada la gobernanza en papel, implementa los contratos inteligentes.

### 2.1. Selección de blockchain

**Ethereum Mainnet**:
- **Ventajas**: Máxima seguridad, liquidez, ecosistema maduro, tooling completo.
- **Desventajas**: Gas fees muy alto para votación on-chain, limita participación.
- **Cuándo usarlo**: DAOs que gestionan cientos de millones o protocolos DeFi críticos.

**Layer 2s (Arbitrum, Optimism, Base)**:
- **Ventajas**: Fees bajos (~$0.01-0.10 por voto), seguridad heredada de Ethereum, buen tooling.
- **Desventajas**: Menor liquidez que mainnet, bridges añaden complejidad.
- **Cuándo usarlo**: Recomendado para mayoría de DAOs nuevas que necesitan gobernanza on-chain accesible.

**Alt-L1s (Solana, Avalanche, Polygon PoS)**:
- **Ventajas**: Fees extremadamente bajos, transacciones rápidas.
- **Desventajas**: Menor descentralización, riesgo de downtime, ecosistema menos maduro.
- **Cuándo usarlo**: Si tu aplicación ya está en ese ecosistema o necesitas throughput extremo.

**Multi-chain**:
- Algunos proyectos despliegan en múltiples chains con bridges entre ellos.
- Complejidad significativa: ¿cómo agregar votos cross-chain? ¿Dónde vive la tesorería?
- Soluciones emergentes: LayerZero, Axelar para mensajería cross-chain.

### 2.2. Arquitectura de contratos

**Patrón recomendado: Separación de concerns**

No metas todo en un contrato monolítico. Separa responsabilidades:

```
GovernanceToken.sol         → ERC20Votes (token con snapshot de balances)
Governor.sol                → Lógica de propuestas y votación
Timelock.sol                → Delay entre aprobación y ejecución
Treasury.sol                → Gestión de fondos
ProtocolExecutor.sol        → Interfaz para cambiar parámetros del protocolo
```

**Contratos upgradeables vs inmutables**

Gran dilema de diseño:

**Contratos inmutables**:
- Máxima confianza: nadie puede cambiar el código.
- Problema: si hay bug o necesitas nueva funcionalidad, estás atascado.
- Solución: migración social (convencer a usuarios de moverse a nueva versión).

**Contratos upgradeables (proxy pattern)**:
- Flexibilidad: puedes corregir bugs y añadir features.
- Problema: introduce vector de ataque si el admin key es comprometido.
- Solución: admin key controlado por el Governor + Timelock, no por EOA individual.

**Recomendación híbrida**:
- Core logic crítico (ej. manejo de fondos): inmutable o con multiples capas de seguridad.
- Periféricos (ej. UI contracts, helpers): upgradeables para iterar rápido.

### 2.3. Implementación con OpenZeppelin Governor

OpenZeppelin Governor es el estándar de facto. Ejemplo mínimo:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/governance/Governor.sol";
import "@openzeppelin/contracts/governance/extensions/GovernorSettings.sol";
import "@openzeppelin/contracts/governance/extensions/GovernorCountingSimple.sol";
import "@openzeppelin/contracts/governance/extensions/GovernorVotes.sol";
import "@openzeppelin/contracts/governance/extensions/GovernorVotesQuorumFraction.sol";
import "@openzeppelin/contracts/governance/extensions/GovernorTimelockControl.sol";

contract MyGovernor is
    Governor,
    GovernorSettings,
    GovernorCountingSimple,
    GovernorVotes,
    GovernorVotesQuorumFraction,
    GovernorTimelockControl
{
    constructor(
        IVotes _token,
        TimelockController _timelock,
        uint256 _votingDelay,      // bloques antes de que comience votación
        uint256 _votingPeriod,     // bloques que dura votación
        uint256 _proposalThreshold, // tokens mínimos para proponer
        uint256 _quorumPercentage  // % del supply necesario para quórum
    )
        Governor("MyGovernor")
        GovernorSettings(_votingDelay, _votingPeriod, _proposalThreshold)
        GovernorVotes(_token)
        GovernorVotesQuorumFraction(_quorumPercentage)
        GovernorTimelockControl(_timelock)
    {}

    // Overrides requeridos por Solidity cuando usas múltiples herencias
    // ... (implementación de overrides)
}
```

**Parámetros típicos**:
```
Voting Delay:         1 day    (13,000 bloques en Ethereum)
Voting Period:        7 days   (91,000 bloques)
Proposal Threshold:   100,000 tokens
Quorum:              4% del supply total
Timelock Delay:       2 days
```

### 2.4. Token de gobernanza con snapshots

El token debe implementar `ERC20Votes` para habilitar snapshots:

```solidity
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Votes.sol";

contract GovernanceToken is ERC20Votes {
    constructor() ERC20("MyDAO", "MDAO") ERC20Permit("MyDAO") {
        _mint(msg.sender, 100_000_000 * 10**18); // 100M tokens
    }

    // Override _afterTokenTransfer para actualizar delegaciones
    function _afterTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override(ERC20Votes) {
        super._afterTokenTransfer(from, to, amount);
    }
}
```

**Características críticas de ERC20Votes**:
- `delegate(address)`: Delega tu poder de voto.
- `getPastVotes(address, blockNumber)`: Obtiene votos en un bloque específico (evita manipulación flash).
- `getPastTotalSupply(blockNumber)`: Total supply histórico para calcular quórum.

### 2.5. Timelock para seguridad

El Timelock actúa como buffer de seguridad:

```solidity
import "@openzeppelin/contracts/governance/TimelockController.sol";

// Deploy timelock
TimelockController timelock = new TimelockController(
    2 days,        // minDelay
    [],           // proposers (será el Governor)
    [],           // executors (cualquiera puede ejecutar después del delay)
    address(0)    // admin (renunciamos al admin después de setup)
);
```

**Flujo completo de propuesta**:
1. Usuario crea propuesta → Entra en período de votación.
2. Votación termina → Si aprobada, entra en cola del Timelock.
3. Espera el minDelay → Durante este tiempo, la comunidad puede auditar.
4. Cualquiera ejecuta → La propuesta modifica el protocolo.

### 2.6. Gestión de tesorería

La tesorería debe ser controlada por el Timelock, no por el Governor directamente:

```
Treasury (ETH, tokens, NFTs)
    ↓ controlado por
TimelockController
    ↓ controlado por
Governor (votación de la DAO)
```

Para transferir fondos:
```solidity
// Propuesta ejecuta esta llamada después de aprobación + timelock
timelock.execute(
    treasuryAddress,      // target
    transferAmount,       // value (ETH)
    abi.encodeWithSignature("transfer(address,uint256)", recipient, amount),
    bytes32(0),          // predecessor
    bytes32(0)           // salt
);
```

### 2.7. Multisig de emergencia

Incluso con gobernanza on-chain, necesitas un multisig para emergencias:

**Casos de uso legítimos**:
- Pausar contratos si se detecta exploit activo.
- Actualizar frontend comprometido.
- Responder a vulnerabilidades zero-day antes de que sean explotadas.

**Implementación con Safe (Gnosis Safe)**:
```
Multisig 5-of-9:
- 3 fundadores
- 3 miembros de comunidad electos
- 3 asesores técnicos externos
```

**Principios**:
- Multisig NO debe controlar la tesorería principal.
- Solo puede pausar, no modificar parámetros económicos.
- Toda acción debe ser ratificada por DAO en las siguientes 72 horas.

## Fase 3: Testing y auditoría

No lances a mainnet sin testing exhaustivo. El costo de un bug es catastrófico.

### 3.1. Testing local

**Hardhat/Foundry tests**:

Escribe tests para cada escenario:
- Propuesta y votación exitosa.
- Propuesta rechazada.
- Quórum no alcanzado.
- Delegación y voto por proxy.
- Timelock correctamente enforced.
- Propuesta maliciosa bloqueada.
- Edge cases: qué pasa si supply cambia durante votación, etc.

```javascript
// Ejemplo test con Hardhat
describe("Governor", function() {
    it("Should execute proposal after quorum and timelock", async function() {
        // 1. Crear propuesta
        const proposal = await governor.propose(targets, values, calldatas, description);
        
        // 2. Avanzar a voting period
        await ethers.provider.send("evm_mine", []);
        
        // 3. Votar (usando múltiples cuentas para superar quórum)
        await governor.connect(voter1).castVote(proposalId, 1); // For
        await governor.connect(voter2).castVote(proposalId, 1);
        
        // 4. Avanzar hasta fin de votación
        await ethers.provider.send("evm_increaseTime", [7 * 24 * 60 * 60]);
        
        // 5. Queue en timelock
        await governor.queue(targets, values, calldatas, descriptionHash);
        
        // 6. Avanzar timelock delay
        await ethers.provider.send("evm_increaseTime", [2 * 24 * 60 * 60]);
        
        // 7. Ejecutar
        await governor.execute(targets, values, calldatas, descriptionHash);
        
        // 8. Verificar estado cambió
        expect(await protocol.someParameter()).to.equal(newValue);
    });
});
```

### 3.2. Testnet deployment

Despliega en testnet pública (Goerli, Sepolia) y:
- Ejecuta propuestas de prueba.
- Invita a la comunidad a interactuar.
- Prueba integración con frontend.
- Simula ataques: flash loans, griefing, spam de propuestas.

### 3.3. Auditoría profesional

**NO lances sin auditoría** si gestionarás fondos significativos.

**Firmas de auditoría respetadas**:
- **OpenZeppelin**: Gold standard, costoso (~$50k-200k).
- **Trail of Bits**: Expertise en seguridad sistémica.
- **Consensys Diligence**: Especializado en DeFi.
- **Certora**: Verificación formal matemática.
- **Code4rena/Sherlock**: Auditorías competitivas crowdsourced, más económicas (~$20k-50k).

**Qué auditar**:
- Contratos de gobernanza (Governor, Timelock).
- Token y sus extensiones (vesting, staking).
- Integración con protocolo (cómo la DAO cambia parámetros).
- Treasury management (cómo se mueven fondos).

**Después de auditoría**:
- Publica el informe completo (transparencia).
- Implementa todas las recomendaciones críticas y de alta severidad.
- Considera bug bounty program para incentivos continuos.

### 3.4. Bug bounty

Lanza bug bounty antes del mainnet launch:

**Plataformas**:
- **Immunefi**: Especializada en Web3, bounties de millones de USD.
- **HackerOne**: Tradicional pero creciente en crypto.

**Estructura de recompensas típica**:
```
Critical (drain de fondos, manipulación de votos):  $100k - $1M
High (bypass de timelock, manipulación de quórum):  $25k - $100k
Medium (griefing, DOS temporal):                    $5k - $25k
Low (informational):                                $500 - $5k
```

## Fase 4: Distribución de tokens

Cómo distribuyes inicialmente el token define la salud a largo plazo de la DAO.

### 4.1. Métodos de distribución

**Fair Launch (lanzamiento justo)**:
- No hay pre-sale, no hay VC allocation.
- Tokens se ganan mediante participación (mining, liquidity provision).
- Ejemplo: Yearn Finance (YFI), Uniswap (airdrop retroactivo).
- **Ventaja**: Máxima descentralización percibida, buena narrativa.
- **Desventaja**: Sin runway financiero para desarrollo, founders no capturan upside inicial.

**Airdrop retroactivo**:
- Distribuir tokens gratis a usuarios que ya usaron el protocolo antes de su existencia.
- Ejemplo: Uniswap ($UNI), ENS, Optimism.
- **Ventaja**: Recompensa early adopters, genera loyalty.
- **Desventaja**: Muchos recipients venden inmediatamente (airdrop farmers).

**Public sale (IDO/ICO)**:
- Venta pública en DEX o plataforma de launchpad.
- **Ventaja**: Recauda capital, crea precio inicial de mercado.
- **Desventaja**: Riesgo regulatorio (tokens como securities), puede ser capturado por bots.

**Private sale + vesting**:
- Venta a inversores estratégicos con lockup largo.
- **Ventaja**: Capital significativo para desarrollo, advisors valiosos.
- **Desventaja**: Concentración de ownership, presión de VCs para liquidez.

**Liquidity mining**:
- Distribuir tokens como rewards por proveer liquidez o usar el protocolo.
- **Ventaja**: Bootstrapping de liquidez, alineación con usuarios activos.
- **Desventaja**: Atraer mercenarios que farm y dump, insostenible a largo plazo.

### 4.2. Contratos de vesting

Implementa vesting on-chain, no confíes en promesas:

```solidity
import "@openzeppelin/contracts/finance/VestingWallet.sol";

// Deploy vesting wallet para team member
VestingWallet teamVesting = new VestingWallet(
    teamMemberAddress,
    block.timestamp + 365 days,  // cliff de 1 año
    4 * 365 days                 // vesting lineal por 4 años después
);

// Transfer tokens al vesting contract
token.transfer(address(teamVesting), teamAllocation);
```

**Best practices**:
- Cliff mínimo de 6-12 meses para team e inversores.
- Vesting más largo para team (4 años) que para community (1-2 años).
- Community treasury sin vesting pero controlado por DAO.

### 4.3. Merkle airdrop para eficiencia

Si haces airdrop a miles de addresses, usa Merkle tree para eficiencia de gas:

```solidity
contract MerkleAirdrop {
    bytes32 public merkleRoot;
    mapping(address => bool) public hasClaimed;

    function claim(uint256 amount, bytes32[] calldata proof) external {
        require(!hasClaimed[msg.sender], "Already claimed");
        
        // Verificar proof
        bytes32 leaf = keccak256(abi.encodePacked(msg.sender, amount));
        require(MerkleProof.verify(proof, merkleRoot, leaf), "Invalid proof");
        
        hasClaimed[msg.sender] = true;
        token.transfer(msg.sender, amount);
    }
}
```

Users reclaman individualmente, solo pagan gas por su claim.

## Fase 5: Bootstrapping de liquidez

Tu token necesita liquidez para que sea tradeable.

### 5.1. DEX pools

**Uniswap V2/V3 pool**:
```
Pair: MDAO/ETH o MDAO/USDC
Initial ratio: Define precio inicial
Profundidad: Al menos $100k para reducir slippage
```

**Decisión**: ¿Pool V2 (automática) o V3 (concentrada)?
- V2: Más simple, liquidez distribuida en todo el rango de precio.
- V3: Capital-efficient, pero necesitas gestionar rangos activamente.

### 5.2. Liquidity mining incentives

Incentiva a proveedores de liquidez para bootstrapping:

```solidity
// Simple staking contract para LP tokens
contract LPStaking {
    IERC20 public lpToken;
    IERC20 public rewardToken;
    
    mapping(address => uint256) public stakes;
    mapping(address => uint256) public rewardDebt;
    
    uint256 public rewardPerBlock;
    
    function stake(uint256 amount) external {
        lpToken.transferFrom(msg.sender, address(this), amount);
        stakes[msg.sender] += amount;
        // Actualizar rewards...
    }
    
    function withdraw() external {
        uint256 pending = calculatePendingRewards(msg.sender);
        rewardToken.transfer(msg.sender, pending);
        // ...
    }
}
```

**Consideraciones**:
- ¿Cuántos tokens destinar a liquidity mining?
- ¿Cuánto tiempo mantener incentivos? (típicamente 3-12 meses).
- ¿Cómo evitar mercenarios que farm y huyen?

**Solución: vesting de rewards**:
- Rewards se liberan gradualmente (ej. 20% inmediato, 80% vesting 6 meses).
- Incentiva commitment a largo plazo.

### 5.3. Protocolo-owned liquidity

Alternativa a mercenarios: la DAO posee su propia liquidez.

**Bonding (modelo Olympus)**:
```
Usuario vende ETH/USDC a la DAO con descuento
    ↓
Recibe tokens MDAO con vesting
    ↓
DAO usa ETH/USDC para crear LP permanente
```

**Ventaja**: Liquidez permanente, no dependes de mercenarios.
**Desventaja**: Complejidad adicional, requiere diseño tokenómico sofisticado.

## Fase 6: Lanzamiento y descentralización progresiva

### 6.1. Pre-launch checklist

Antes de lanzar, verifica:

**Técnico**:
- [ ] Contratos auditados por al menos una firma respetada.
- [ ] Bug bounty activo.
- [ ] Testnet completamente funcional con propuestas de prueba ejecutadas.
- [ ] Documentación técnica completa (cómo proponer, votar, delegar).
- [ ] Frontend auditado (riesgo de frontend malicioso que draina fondos).

**Legal**:
- [ ] Consulta con abogado crypto sobre riesgo regulatorio en tu jurisdicción.
- [ ] Considera wrapper legal (Wyoming LLC, Cayman Foundation).
- [ ] Terms of service claros (especialmente disclaimers sobre riesgo).

**Operativo**:
- [ ] Comunidad existente en Discord/Telegram/Twitter.
- [ ] Documentación clara para usuarios (guías paso a paso).
- [ ] Multisig configurado con signers de confianza.
- [ ] Liquidez initial en DEX suficiente.

**Comunicación**:
- [ ] Anuncio público con todos los detalles (tokenomics, contratos, auditoría).
- [ ] Transparency report: quién controla qué porcentaje de tokens.
- [ ] Roadmap claro de descentralización progresiva.

### 6.2. Estrategia de descentralización progresiva

No entregues control completo el día 1. Fase gradual:

**Fase 1: Lanzamiento controlado (Meses 0-3)**:
- DAO existe pero con poderes limitados.
- Multisig puede vetar propuestas maliciosas.
- Team ejecuta desarrollo según roadmap pre-aprobado.
- Comunidad se familiariza con proceso de gobernanza mediante propuestas de señalización.

**Fase 2: Descentralización parcial (Meses 3-12)**:
- DAO controla tesorería y grants.
- DAO puede cambiar parámetros del protocolo dentro de rangos seguros.
- Team mantiene control de contratos críticos pero debe justificar decisiones públicamente.
- Emergen delegados profesionales activos.

**Fase 3: Descentralización sustancial (Año 1-2)**:
- DAO controla todo excepto pausas de emergencia.
- Multisig solo puede pausar ante exploit, no vetar propuestas.
- Team es un contributor más, no tiene control especial.
- Todas las decisiones importantes requieren voto on-chain.

**Fase 4: Descentralización completa (Año 2+)**:
- Multisig se disuelve o se reemplaza por multisig comunitario.
- Team original puede salir sin colapsar el proyecto.
- DAO es autosuficiente: financia su propio desarrollo, marketing, operaciones.

### 6.3. Métricas de salud de DAO

Monitorea constantemente:

**Participación**:
- % de tokens que votan regularmente.
- Número de delegados activos.
- Diversidad de voting power (Gini coefficient).

**Actividad**:
- Propuestas por mes.
- % de propuestas que alcanzan quórum.
- % de propuestas aprobadas.

**Financiero**:
- Runway de tesorería (cuántos meses puede operar la DAO).
- Retorno de grants (cuántos proyectos financiados generaron valor).
- Diversificación de tesorería (% en stablecoins vs tokens volátiles).

**Social**:
- Actividad en Discord/Forum.
- Nuevos miembros activos por mes.
- Retención de contribuidores.

## Fase 7: Operaciones a largo plazo

Una DAO lanzada no es el fin, es el principio.

### 7.1. Gestión de tesorería profesional

Conforme crece la tesorería, necesitas estrategia sofisticada:

**Diversificación**:
```
Ejemplo - DAO con $10M en tesorería:

Stablecoins (USDC/DAI):        40%  → Runway operativo
Native token:                  30%  → Alineación con protocolo
Blue chips (ETH, BTC):        20%  → Store of value
DeFi yield:                   10%  → Ingresos pasivos
```

**Yield generation**:
- Depositar stablecoins en Aave/Compound para interés.
- Proveer liquidez en pools estables (USDC/DAI) con bajo riesgo.
- Staking de ETH en protocolos como Lido.

**Risk management**:
- No más del 10% de tesorería en un solo protocolo (riesgo de exploit).
- Auditar todos los protocolos donde depositas.
- Mantener suficiente liquidez inmediata (20-30%) para emergencias.

### 7.2. Grants program sostenible

Si financias proyectos, hazlo estructurado:

**Proceso típico**:
1. **Application**: Proyecto presenta propuesta con milestones.
2. **Review**: Grants council evalúa técnicamente.
3. **Voting**: DAO vota si aprobar.
4. **Milestones**: Fondos se liberan en tranches al completar objetivos.
5. **Retrospective**: Evaluación pública de resultados.

**Herramientas**:
- **Questbook**: Plataforma para gestionar grants con milestones on-chain.
- **Gitcoin Grants**: Quadratic funding rounds.
- **Coordinape**: Círculos de contributors se pagan entre sí based on contribution.

### 7.3. Evolución de la gobernanza

La gobernanza no es estática. Mejora continuamente:

**Ejemplos de mejoras comunes**:
- Migrar de off-chain (Snapshot) a on-chain conforme crece la tesorería.
- Implementar quadratic voting para decisiones de grants.
- Crear sub-DAOs especializados (Marketing DAO, Dev DAO).
- Añadir reputation system complementario a tokens.

## Recursos y herramientas

### Frameworks de desarrollo
- **OpenZeppelin Contracts**: Librería estándar para Governor pattern.
- **Aragon OSx**: Framework modular completo.
- **DAOhaus**: Moloch DAOs with UI out of the box.
- **Colony**: Reputación y jerarquías on-chain.

### Tooling operativo
- **Snapshot**: Votación off-chain gasless.
- **Tally**: Frontend universal para interactuar con Governor contracts.
- **Safe (Gnosis Safe)**: Multisig para tesorería y emergencias.
- **Zodiac**: Módulos para extender Safe con gobernanza.

### Analytics y dashboards
- **Dune Analytics**: Queries SQL sobre datos on-chain de tu DAO.
- **DeepDAO**: Directorio y analytics de DAOs cross-chain.
- **Boardroom**: Agregador de propuestas y votaciones.

### Gestión de comunidad
- **Discord + Collab.Land**: Verificación de token holders para acceso a canales.
- **Discourse**: Forums para discusión de propuestas.
- **Commonwealth**: Plataforma all-in-one para discusión y votación.

## Errores comunes a evitar

**Error 1: Lanzar DAO prematuramente**
- No lances gobernanza antes de product-market fit.
- Primero construye producto valioso, luego descentraliza el control.

**Error 2: Token solo de gobernanza sin utilidad**
- Nadie quiere holdear token que solo sirve para votar.
- Añade staking, fee sharing, boosts, o algo que genere valor.

**Error 3: Quórum demasiado bajo**
- Quórum de 1% significa que 99% no participa y una minoría controla.
- Aumenta engagement antes de bajar quórum.

**Error 4: Concentración de tokens en pocas wallets**
- Top 10 holders con >50% del supply = plutocracia.
- Distribuye ampliamente desde el inicio.

**Error 5: No auditar smart contracts**
- Un bug en gobernanza puede drenar toda la tesorería.
- Auditoría es inversión, no gasto.

**Error 6: Complejidad excesiva**
- No necesitas quadratic voting + conviction voting + holographic consensus el día 1.
- Empieza simple, itera después.

**Error 7: Ignorar aspectos legales**
- "Code is law" no te protege de la SEC.
- Consulta abogados especializados en crypto.

**Error 8: Prometer descentralización sin entregarla**
- Si el equipo mantiene control real, no lo llames DAO.
- Sea honesto sobre el nivel de descentralización.

## Conclusión

Crear una DAO exitosa es mucho más que desplegar un Governor contract. Requiere:
- **Diseño cuidadoso**: Incentivos alineados, tokenomics sostenible, gobernanza práctica.
- **Excelencia técnica**: Contratos auditados, arquitectura segura, testing exhaustivo.
- **Comunidad activa**: Usuarios comprometidos que realmente participan.
- **Descentralización gradual**: No apresures el proceso, gana trust primero.
- **Iteración continua**: La gobernanza evoluciona, aprende de la práctica.

Las DAOs no son una solución universal. Son herramientas para contextos específicos donde transparencia, resistencia a censura y coordinación global sin confianza centralizada son más valiosas que velocidad de ejecución y privacidad estratégica.

Si después de leer esta guía decides que realmente necesitas una DAO, bienvenido al experimento de coordinación humana más ambicioso de nuestra generación. Si decides que no la necesitas, también es una decisión sabia. No toda organización debería ser descentralizada.
