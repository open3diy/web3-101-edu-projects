# Protocolos de roles y control de acceso en Web3

El control de acceso es uno de los pilares fundamentales de la seguridad en Web3. A diferencia de sistemas centralizados donde un administrador de base de datos gestiona permisos desde un servidor, en Web3 el control de acceso está codificado en smart contracts inmutables, es verificable on-chain, y puede ser auditado públicamente por cualquiera. Cuando un protocolo DeFi gestiona miles de millones de dólares, o una DAO controla un treasury valorado en cientos de millones, no basta con "tener buenas intenciones": necesitas mecanismos criptográficos y económicos que garanticen que solo las personas autorizadas puedan ejecutar acciones críticas.

Este documento explora los protocolos, patrones y estándares que rigen quién puede hacer qué en el ecosistema Web3. Desde contratos simples con un único propietario hasta complejos sistemas multi-firma con delays temporales, cada patrón resuelve problemas específicos de seguridad y descentralización. Comprender estos mecanismos no es opcional si construyes aplicaciones que custodian valor real: la diferencia entre un protocolo robusto y uno explotado suele estar en la correcta implementación del control de acceso.

## El problema del control de acceso en sistemas descentralizados

En Web2, el control de acceso es relativamente simple: existe un servidor central, una base de datos con usuarios y permisos, y un administrador que puede modificarlo todo. Si algo falla, puedes pausar el sistema, revertir cambios en la base de datos y parchear el código. En Web3, este modelo no funciona.

Los smart contracts son inmutables por diseño: una vez desplegados en la blockchain, su código no cambia. No existe un botón de "deshacer" ni un administrador omnipotente que pueda revertir transacciones fraudulentas. Si despliegas un contrato con un bug crítico en el sistema de permisos, un atacante podría drenar todos los fondos y no hay forma de recuperarlos mediante intervención administrativa.

Esta inmutabilidad crea un dilema: necesitas flexibilidad para evolucionar el protocolo (arreglar bugs, añadir funcionalidades, ajustar parámetros económicos), pero también necesitas garantías de que nadie puede abusar de esos privilegios. Si el contrato puede ser pausado, ¿quién tiene ese poder? Si los parámetros pueden cambiar, ¿cómo evitas que un desarrollador malicioso o comprometido destruya el protocolo?

Además, la transparencia de blockchain añade complejidad. Cualquier atacante puede leer el código del contrato, ver quién tiene qué permisos, analizar vulnerabilidades y planear exploits. No existe "seguridad por oscuridad". El sistema de control de acceso debe ser tan robusto que, incluso sabiendo exactamente cómo funciona, nadie pueda comprometer el protocolo.

Los mayores exploits en la historia de DeFi tienen un denominador común: fallos en control de acceso. El hack de The DAO en 2016 ($50M), Ronin Bridge en 2022 ($625M), Poly Network en 2021 ($611M), todos involucraron problemas donde atacantes pudieron ejecutar acciones que no deberían haber estado autorizados a realizar.

## Role-Based Access Control (RBAC)

El patrón más ampliamente adoptado en Web3 es Role-Based Access Control, donde en lugar de asignar permisos individuales a cada dirección, defines roles abstractos (ADMIN, MINTER, PAUSER, BURNER, UPGRADER) y asignas esos roles a direcciones específicas. Cada función crítica del contrato verifica que quien la llama tenga el rol correspondiente.

**OpenZeppelin AccessControl**: el estándar de facto

[OpenZeppelin AccessControl](https://docs.openzeppelin.com/contracts/4.x/access-control) es la implementación más utilizada de RBAC en Ethereum. Proporciona un sistema flexible de roles donde:

- Cualquier número de roles puede ser creado
- Cada rol tiene un rol de administrador (admin role) que puede otorgar/revocar ese rol
- Múltiples direcciones pueden tener el mismo rol
- Una dirección puede tener múltiples roles
- Todos los cambios de roles emiten eventos auditables on-chain

Ejemplo básico de uso:

```solidity
import "@openzeppelin/contracts/access/AccessControl.sol";

contract MyToken is AccessControl {
    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");
    bytes32 public constant PAUSER_ROLE = keccak256("PAUSER_ROLE");
    
    constructor() {
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(MINTER_ROLE, msg.sender);
    }
    
    function mint(address to, uint256 amount) public onlyRole(MINTER_ROLE) {
        _mint(to, amount);
    }
    
    function pause() public onlyRole(PAUSER_ROLE) {
        _pause();
    }
}
```

El modificador `onlyRole(ROLE)` verifica que `msg.sender` tenga el rol especificado antes de ejecutar la función. Si no lo tiene, la transacción revierte.

**Jerarquías de roles**

AccessControl permite crear jerarquías: un rol puede tener un "admin role" que controla quién puede otorgar/revocar ese rol. Por defecto, `DEFAULT_ADMIN_ROLE` es el admin de todos los roles, pero puedes configurar estructuras más complejas:

```solidity
// SECURITY_ADMIN puede otorgar/revocar PAUSER_ROLE
_setRoleAdmin(PAUSER_ROLE, SECURITY_ADMIN);
```

Esto permite descentralización progresiva: el fundador inicial tiene DEFAULT_ADMIN_ROLE, luego transfiere control de roles específicos a multisigs o DAOs especializadas, reduciendo puntos centralizados de fallo.

**Casos de uso comunes**

En tokens ERC-20:
- `MINTER_ROLE`: puede crear nuevos tokens (necesario para recompensas, staking, liquidity mining)
- `PAUSER_ROLE`: puede pausar transferencias en emergencias
- `SNAPSHOT_ROLE`: puede crear snapshots del estado del token para votaciones

En DAOs:
- `PROPOSAL_CREATOR`: puede crear propuestas de gobernanza
- `EXECUTOR`: puede ejecutar propuestas aprobadas
- `GUARDIAN`: puede pausar el sistema en emergencias
- `TIMELOCK_ADMIN`: puede gestionar delays en ejecuciones críticas

En protocolos DeFi:
- `POOL_ADMIN`: puede modificar parámetros de pools de liquidez
- `FEE_MANAGER`: puede ajustar fees del protocolo
- `ORACLE_UPDATER`: puede actualizar fuentes de precios

## Ownable: simplicidad con centralización

Para proyectos en fase temprana donde la descentralización completa no es inmediata, [OpenZeppelin Ownable](https://docs.openzeppelin.com/contracts/4.x/api/access#Ownable) ofrece un patrón más simple: un único dueño que controla funciones administrativas.

```solidity
import "@openzeppelin/contracts/access/Ownable.sol";

contract SimpleVault is Ownable {
    function withdrawFees() public onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
    
    function updateConfig(uint256 newParam) public onlyOwner {
        config = newParam;
    }
}
```

El modificador `onlyOwner` verifica que solo el propietario actual pueda ejecutar funciones críticas. Ownership puede transferirse a otra dirección mediante `transferOwnership(newOwner)`.

**Riesgos de Ownable**

Este patrón es extremadamente centralizado: una única clave privada controla todo. Si esa clave se compromete (hackeo, pérdida, coacción), el atacante controla el protocolo completamente. Por eso Ownable solo es aceptable en:

- Contratos en testnet o experimentos
- Proyectos muy tempranos donde governance no está lista
- Como paso transitorio hacia modelos más descentralizados

**Ownable2Step: mitigación de riesgos**

[Ownable2Step](https://docs.openzeppelin.com/contracts/4.x/api/access#Ownable2Step) mejora Ownable requiriendo confirmación del nuevo owner antes de transferir control:

```solidity
// Owner actual propone nuevo owner
transferOwnership(newOwner);

// Nuevo owner debe aceptar
// (desde la dirección newOwner)
acceptOwnership();
```

Esto previene errores fatales como transferir ownership a una dirección incorrecta o a un contrato que no puede llamar `acceptOwnership()`, lo que causaría pérdida permanente de control.

## Multi-signature wallets (multisig)

Los multisigs resuelven el problema del single point of failure: en lugar de una clave privada que controla todo, requieren M-de-N firmas para ejecutar transacciones. Por ejemplo, un multisig 3-de-5 requiere que 3 de 5 claves autorizadas firmen una transacción antes de ejecutarse.

**Safe (anteriormente Gnosis Safe)**

[Safe](https://safe.global/) es el estándar de la industria para multisigs en Ethereum y chains compatibles con EVM. No es solo una wallet multi-firma, sino una infraestructura completa para gestión de activos descentralizada.

Características clave:
- **Threshold signatures**: configura cuántas firmas necesitas (M-de-N)
- **Módulos extensibles**: añade funcionalidades como limits diarios, whitelists, integración con protocolos DeFi
- **Transaction batching**: agrupa múltiples operaciones en una sola transacción
- **Guardians**: direcciones que pueden pausar o bloquear operaciones peligrosas
- **Interoperabilidad**: soportado por prácticamente todos los protocolos DeFi y DAOs

Safe es usado por:
- DAOs para custodiar treasuries (Uniswap, Aave, MakerDAO)
- Protocolos DeFi para control de parámetros críticos
- Equipos de desarrollo para ownership de contratos en producción

**Casos de uso típicos**

Un protocolo DeFi podría tener:
- Multisig 4-de-7 controlando ownership de contratos core (founders + advisors + community representatives)
- Multisig 2-de-3 para operaciones rutinarias (ajustes de fees, actualizaciones de oráculos)
- Multisig 3-de-5 para emergency pause (guardians de seguridad)

Una DAO podría:
- Usar Safe para custodiar treasury principal
- Configurar módulos que permitan ciertos gastos pre-aprobados sin multisig
- Implementar spending limits: gastos menores de 10 ETH requieren 2 firmas, mayores requieren 4

**Limitaciones**

Los multisigs no son perfectos:
- **Coordinación off-chain**: las N partes deben comunicarse externamente para coordinar firmas
- **Disponibilidad**: si M signatarios pierden claves o desaparecen, el multisig queda bloqueado
- **Collusion**: si M signatarios se coludieron, pueden drenar fondos
- **Complejidad UX**: cada operación requiere múltiples pasos, ralentizando decisiones urgentes

Por eso los protocolos serios combinan multisigs con otros mecanismos (timelocks, guardians, parámetros inmutables).

## Timelock controllers: delays para transparencia

Un timelock introduce un delay obligatorio entre la aprobación de una acción y su ejecución. Esto da tiempo a la comunidad para revisar cambios propuestos y, si detectan algo malicioso, retirar fondos antes de que se ejecute.

**OpenZeppelin TimelockController**

[TimelockController](https://docs.openzeppelin.com/contracts/4.x/api/governance#TimelockController) es la implementación estándar. Funciona así:

1. Una dirección autorizada (proposer) programa una operación (por ejemplo, "actualizar parámetro X a valor Y")
2. La operación entra en cola con un timestamp de ejecución mínima (ej: now + 48 horas)
3. Después del delay, otra dirección autorizada (executor) puede ejecutar la operación
4. Opcionalmente, un canceller puede cancelar operaciones pendientes si se detectan problemas

```solidity
import "@openzeppelin/contracts/governance/TimelockController.sol";

// Crear timelock con 48h delay
TimelockController timelock = new TimelockController(
    2 days,           // minimum delay
    proposers,        // addresses que pueden proponer
    executors,        // addresses que pueden ejecutar
    admin             // admin opcional que puede gestionar roles
);

// Transferir ownership del contrato al timelock
myContract.transferOwnership(address(timelock));

// Ahora cualquier cambio crítico requiere:
// 1. Proposer programa cambio
// 2. Esperar 48 horas
// 3. Executor ejecuta cambio
```

**Por qué importan los timelocks**

Compound Finance sufrió en 2021 un bug donde por error distribuyó $80M en tokens COMP extra. Si hubieran tenido un timelock robusto, la comunidad habría detectado el cambio antes de ejecutarse.

Inversamente, protocolos sin timelocks han sufrido rug pulls donde developers cambiaron parámetros críticos (fees al 100%, pausaron withdrawals) drenando fondos antes de que nadie pudiera reaccionar.

El delay típico varía:
- Cambios de parámetros menores: 24-48 horas
- Upgrades de contratos: 7-14 días
- Cambios en governance: 14-30 días

**Trade-offs**

Delays largos aumentan seguridad pero reducen agilidad. En mercados cripto volátiles, no poder ajustar parámetros rápidamente puede ser fatal. Por eso muchos protocolos implementan timelocks escalonados:
- Cambios rutinarios: 24h delay
- Cambios significativos: 7d delay
- Cambios críticos: 14d delay
- Emergency pause: sin delay (ejecutable inmediatamente por guardians)

## Access Control Lists (ACL): permisos granulares

Mientras RBAC asigna roles que pueden ejecutar funciones completas, Access Control Lists permiten permisos ultra-granulares: "dirección X puede ejecutar función Y en contrato Z con parámetros dentro de rango W".

**Aragon ACL**

[Aragon](https://aragon.org/) implementa uno de los sistemas ACL más sofisticados:

```solidity
// Permitir que dao.agent transfiera hasta 100 ETH del vault
acl.grantPermissionP(
    dao.agent,                    // who
    dao.vault,                    // where
    vault.TRANSFER_ROLE(),        // what
    [lessThan(100 ether)]         // under what conditions
);
```

Esto permite crear governance extremadamente flexible:
- Role TREASURER puede transferir hasta 50 ETH sin aprobación, más requiere votación
- Role PARAMETER_MANAGER puede ajustar fees entre 0.1% y 2%, fuera de ese rango requiere DAO
- Role GUARDIAN puede pausar el protocolo, pero solo puede activarlo de nuevo mediante votación

**Parámetros condicionales**

ACLs avanzadas pueden incluir lógica:
- "Solo entre 9am-5pm UTC"
- "Solo si precio de X > $100"
- "Solo si han pasado 7 días desde último cambio"
- "Solo si totalSupply < 1M tokens"

Esto crea "governance programática" donde el contrato mismo aplica reglas de negocio sin intervención humana.

## Delegación de permisos y capabilities

Más allá de asignar roles permanentes, algunos protocolos necesitan permisos temporales o delegables.

**EIP-2612: Permit (meta-transactions para ERC-20)**

[EIP-2612](https://eips.ethereum.org/EIPS/eip-2612) permite que usuarios firmen off-chain una aprobación para que un contrato gaste sus tokens, sin necesidad de una transacción on-chain previa:

```solidity
// Usuario firma mensaje off-chain dando permiso
// Contrato puede usar esa firma para ejecutar transferFrom
token.permit(owner, spender, value, deadline, v, r, s);
token.transferFrom(owner, recipient, value);
```

Esto mejora UX (menos transacciones) y habilita meta-transactions (terceros pagan gas por el usuario).

**ERC-4337: Account Abstraction**

[ERC-4337](https://eips.ethereum.org/EIPS/eip-4337) lleva delegación más allá: wallets pueden programar lógica de autorización arbitraria:
- Multi-firma nativa en la wallet
- Spending limits por categoría
- Whitelist/blacklist de contratos
- Recuperación social de claves
- Gas sponsorship por terceros (paymasters)

Ejemplo: una wallet puede configurar "cualquier transacción DeFi requiere confirmación biométrica, pero transferencias menores de 10 USDC se aprueban automáticamente".

**Capability-based security**

Algunos protocolos emiten NFTs o tokens que otorgan permisos. Por ejemplo:
- Poseer "Admin Badge NFT" otorga derechos de administración transferibles
- Staking X tokens otorga VOTING_POWER proporcional
- Completar quest on-chain otorga credential que desbloquea funcionalidades

Esto permite mercados de permisos: si ya no quieres ser admin, vendes el badge NFT a quien quiera asumir ese rol.

## Control de acceso off-chain: token-gating

El control de acceso no se limita a smart contracts. Comunidades Web3 usan ownership de tokens/NFTs para gestionar permisos en plataformas off-chain.

**Collab.Land y Guild.xyz**

[Collab.Land](https://collab.land/) y [Guild.xyz](https://guild.xyz/) integran Discord/Telegram con blockchain para verificar ownership:
- Poseer 100+ tokens del proyecto otorga rol "Holder" en Discord
- Poseer NFT de la colección otorga acceso a canal exclusivo
- Staking en protocolo otorga rol "Contributor" con permisos especiales

Esto alinea incentivos: quienes tienen skin in the game (poseen tokens) participan en decisiones.

**Snapshot: votación off-chain con ownership on-chain**

[Snapshot](https://snapshot.org/) permite DAOs votar sin pagar gas:
1. DAO configura estrategia de votación (ej: 1 token = 1 voto)
2. Miembros firman votos off-chain
3. Resultado se calcula verificando balances on-chain en snapshot específico
4. Si pasa, multisig o contrato on-chain ejecuta la decisión

Esto combina eficiencia (sin gas para votar) con seguridad (ownership verificable on-chain).

## Mejores prácticas y patrones de seguridad

**Separación de roles**

Nunca uses un único role para todo. Separa:
- **Governance**: quien decide cambios (DAO, multisig)
- **Execution**: quien ejecuta decisiones aprobadas (timelock, executor role)
- **Guardianship**: quien puede pausar emergencias (guardians, security multisig)
- **Operations**: quien gestiona tareas rutinarias (parámetros menores, oracles)

**Principio de mínimo privilegio**

Cada rol debe tener exactamente los permisos que necesita, nada más. Si un rol solo necesita pausar el protocolo, no le des capacidad de cambiar parámetros económicos.

**Descentralización progresiva**

Proyectos suelen empezar centralizados y descentralizar gradualmente:
1. **Fase 1**: Founders con Ownable (desarrollo rápido, iterar sin fricción)
2. **Fase 2**: Transferir ownership a multisig 3-de-5 (founders + advisors)
3. **Fase 3**: Añadir timelock 48h para cambios críticos
4. **Fase 4**: Delegar algunos roles a DAO on-chain con votación
5. **Fase 5**: Ownership final a DAO con timelock 14d + emergency multisig

**Inmutabilidad selectiva**

Algunos parámetros deben ser inmutables desde deployment:
- Fees máximos (hard cap para prevenir extracción)
- Direcciones de contratos core (prevenir redirección maliciosa)
- Supply caps de tokens

Si algo no debe cambiar nunca, codifícalo como `constant` o `immutable` en Solidity, eliminando vectores de ataque.

**Auditoría de eventos**

Cada cambio de permisos debe emitir eventos:
```solidity
event RoleGranted(bytes32 indexed role, address indexed account, address indexed sender);
event RoleRevoked(bytes32 indexed role, address indexed account, address indexed sender);
```

Herramientas como Tenderly o block explorers pueden alertar cuando roles cambian, permitiendo respuesta rápida ante compromisos.

**Testing exhaustivo**

Roles incorrectos son bugs críticos. Tests deben verificar:
- Solo roles autorizados pueden ejecutar funciones protegidas
- Otros roles/direcciones no pueden ejecutarlas
- Transferencias de roles funcionan correctamente
- Revocaciones funcionan correctamente
- Jerarquías de admin roles se respetan

## Casos de estudio: aprendiendo de exploits

**The DAO (2016): reentrancy + falta de circuit breakers**

The DAO perdió $50M porque no tenía mecanismos de pausa de emergencia. Un simple GUARDIAN role con capacidad de pausar transferencias habría limitado el daño.

**Ronin Bridge (2022): multisig comprometido**

Ronin requería 5-de-9 firmas, pero atacantes comprometieron 5 claves (mediante ingeniería social y spear phishing). Lesson: multisig no es suficiente si las claves se almacenan inseguramente. Solución: combinar multisig + hardware wallets + geolocalización distribuida de signers.

**Poly Network (2021): fallo en verificación de roles**

Contrato permitía que cualquiera llamara función privilegiada cambiando ownership. Lesson: auditar exhaustivamente que `onlyRole` / `onlyOwner` están en TODAS las funciones críticas.

**Compound COMP distribution bug (2021): falta de timelock**

Deploy de nueva versión con bug distribuyó $80M extra. Si hubiera habido timelock 48h, comunidad habría detectado el error antes de ejecución.

## Herramientas y recursos

**Librerías estándar**:
- [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts/): AccessControl, Ownable, TimelockController
- [Safe contracts](https://github.com/safe-global/safe-contracts): Multisig battle-tested
- [Aragon](https://aragon.org/): Framework completo de governance y ACL

**Auditoría y monitoreo**:
- [Tenderly](https://tenderly.co/): Monitoring de eventos de roles, simulación de transacciones
- [OpenZeppelin Defender](https://www.openzeppelin.com/defender): Automated monitoring y respuesta a cambios de permisos
- [Forta](https://forta.org/): Detection de cambios sospechosos en ownership/roles

**Testing**:
- [Hardhat](https://hardhat.org/) / [Foundry](https://getfoundry.sh/): Frameworks para testing exhaustivo de permisos
- [Slither](https://github.com/crytic/slither): Static analysis que detecta problemas comunes de access control

## Conclusión: seguridad como proceso, no como estado

El control de acceso en Web3 no es un checkbox que marcas al deployment, sino un proceso continuo de evaluación y mejora. Los protocolos exitosos:

1. Empiezan simples y evolucionan progresivamente hacia descentralización
2. Separan roles con principio de mínimo privilegio
3. Combinan múltiples capas (multisig + timelock + guardians + parámetros inmutables)
4. Monitorizan cambios de permisos en tiempo real
5. Auditan código y procesos antes de manejar valor significativo
6. Aprenden de exploits históricos y ajustan defensas

Recuerda: en Web3, el código es ley. Si tu contrato tiene un bug en access control, no hay customer support que pueda revertir la transacción. La única defensa es diseño cuidadoso, implementación correcta, testing exhaustivo y auditoría profesional.

Los mejores protocolos no nacen perfectamente descentralizados, sino que transicionan gradualmente desde control centralizado (velocidad de iteración) hacia governance descentralizada (seguridad y legitimidad). El arte está en balancear estos trade-offs según la etapa de madurez de tu proyecto.

---

**Para profundizar**:
- Sobre identidad y verificación: [Identidad Web3](7-1-identity-web3.md)
- Sobre governance en DAOs: [DAO](7-3-DAO.md)
- Sobre reputación on-chain: [Reputación Web3](7-2-web3-reputation.md)
