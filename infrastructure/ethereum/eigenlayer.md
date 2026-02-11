# EigenLayer: Restaking y Seguridad Compartida

EigenLayer es un protocolo de middleware construido sobre Ethereum que introduce el concepto de **restaking**, permitiendo que validadores de Ethereum reutilicen su ETH ya en stake para asegurar servicios adicionales (llamados AVS - Actively Validated Services) más allá del consenso de Ethereum. Esta innovación extiende la seguridad criptoeconómica de Ethereum a todo un ecosistema de aplicaciones y protocolos que necesitan validación descentralizada, creando un mercado de seguridad compartida donde desarrolladores pueden aprovechar la base de validadores de Ethereum sin construir su propio conjunto de validadores desde cero.

El protocolo fue fundado por Sreeram Kannan (Universidad de Washington) y lanzado en mainnet en 2024. EigenLayer representa uno de los desarrollos más significativos en la arquitectura de seguridad de blockchain desde la introducción de Proof of Stake, fundamentalmente porque desacopla la provisión de seguridad económica (staking de ETH) de servicios específicos de validación, permitiendo que un pool compartido de validadores asegure múltiples protocolos simultáneamente.

## El Problema que Resuelve EigenLayer

### Fragmentación de Seguridad en el Ecosistema Blockchain

Cada protocolo que requiere validación descentralizada tradicionalmente debe construir su propio conjunto de validadores desde cero, enfrentando desafíos fundamentales:

**Bootstrapping de Seguridad:**

Proyectos nuevos carecen de reputación y liquidez inicial. Atraer validadores suficientes para alcanzar niveles de seguridad comparables a redes maduras requiere años de desarrollo de comunidad, incentivos económicos atractivos, y superar el problema del huevo y la gallina: los usuarios no confían en protocolos con poca seguridad, pero atraer validadores requiere usuarios y volumen.

**Costo de Capital:**

Validadores deben adquirir y bloquear tokens nativos del protocolo, fragmentando capital entre múltiples redes. Un validador que participa en 10 protocolos diferentes necesita capital bloqueado en 10 tokens diferentes, cada uno con volatilidad y riesgo de liquidez. Esto crea ineficiencias masivas de capital: el mismo capital no puede asegurar múltiples protocolos simultáneamente.

**Centralización en Protocolos Pequeños:**

Proyectos con pocos validadores o bajo valor total en stake son vulnerables a ataques económicos. Si el costo de corromper 2/3 de los validadores es menor que el valor que pueden robar, el protocolo es fundamentalmente inseguro. Muchos protocolos pequeños operan con security budgets de millones de dólares asegurando aplicaciones que custodian decenas o cientos de millones, invirtiendo la ecuación económica de seguridad.

**Ejemplos de Servicios que Necesitan Validación:**

- **Oráculos descentralizados:** Chainlink, Pyth, UMA necesitan redes de nodos que reportan datos del mundo real de forma confiable.
- **Bridges cross-chain:** Puentes entre blockchains requieren validadores que certifiquen estado en ambas cadenas y ejecuten transferencias de activos de forma segura.
- **Data Availability Layers:** Servicios como Celestia o EigenDA que garantizan disponibilidad de datos para rollups.
- **Keeper networks:** Redes de bots que ejecutan tareas automatizadas (liquidaciones en DeFi, rebalanceo de pools, ejecución de órdenes).
- **Coprocessors:** Servicios que realizan cómputo complejo off-chain y retornan resultados verificables on-chain.
- **Sequencers descentralizados:** Rollups que buscan descentralizar sus sequencers para resistencia a censura.

Cada uno tradicionalmente requeriría su propio token de seguridad, conjunto de validadores, y mecanismos de slashing, fragmentando seguridad y capital.

### La Propuesta de Valor de EigenLayer

EigenLayer permite que estos servicios "alquilen" seguridad de la base de validadores de Ethereum, heredando las garantías criptoeconómicas del pool de ~30M+ ETH en stake (valor de decenas de miles de millones de dólares). Los validadores de Ethereum pueden optar voluntariamente por extender su participación (restake) para validar AVS adicionales, ganando recompensas extra pero asumiendo condiciones de slashing adicionales.

Esto crea un **mercado libre de seguridad compartida** donde:

- **Desarrolladores de AVS** pueden lanzar servicios con seguridad instantánea sin bootstrapping, pagando comisiones a operadores basadas en demanda.
- **Operadores** (validadores de Ethereum) pueden diversificar ingresos asegurando múltiples AVS con el mismo capital en stake.
- **Stakers** (usuarios que delegan ETH a operadores) reciben rendimientos mejorados sin fragmentar capital entre múltiples tokens.

## Arquitectura Técnica de EigenLayer

EigenLayer opera como un conjunto de smart contracts en Ethereum mainnet que coordinan el restaking, registro de operadores, delegación, y slashing. La arquitectura modular permite extensibilidad y composabilidad con el resto del ecosistema DeFi de Ethereum.

### Componentes Core del Protocolo

**1. StrategyManager Contract**

Gestiona todas las estrategias de inversión disponibles para restaking. Una "estrategia" es un smart contract que define cómo los activos restaked generan yield adicional o cómo se integran con protocolos DeFi:

- **Funciones principales:** `depositIntoStrategy()`, `withdrawFromStrategy()`, `addStrategiesToDepositWhitelist()`
- **Estrategias soportadas:** Native ETH (validator credentials), stETH (Lido), rETH (Rocket Pool), cbETH (Coinbase), y potencialmente cualquier LST (Liquid Staking Token) whitelisted
- **Accounting:** Mantiene registro on-chain del balance de cada staker en cada estrategia, actualizando cuando se deposita, retira, o sufre slashing

**2. DelegationManager Contract**

Maneja la relación entre stakers y operadores. Los stakers (usuarios con ETH restaked) delegan su stake a operadores (entidades que ejecutan infraestructura de validación para AVS):

- **Funciones principales:** `delegateTo()`, `undelegate()`, `registerAsOperator()`
- **Operator metadata:** Cada operador publica metadata on-chain incluyendo comisión cobrada, servicios AVS que valida, y detalles de contacto
- **Withdrawal delays:** Implementa períodos de retiro (típicamente 7 días) para prevenir que operadores maliciosos salgan instantáneamente antes de ser slasheados

**3. Slasher Contract**

Coordina las condiciones de slashing cross-service y ejecuta penalizaciones cuando operadores actúan maliciosamente:

- **Funciones principales:** `freezeOperator()`, `slashShares()`, `resetFrozenStatus()`
- **Opt-in slashing:** Cada AVS define sus propias condiciones de slashing (reglas específicas de qué comportamientos son penalizables). Los operadores optan explícitamente por estas condiciones al registrarse en un AVS.
- **Veto mechanisms:** Incluye períodos de disputa donde slashing propuesto puede ser desafiado antes de ejecución final, protegiendo contra falsos positivos.

**4. AVS Directory & Registry**

Registro on-chain de todos los AVS activos, sus requisitos de seguridad, y los operadores registrados en cada uno:

- **AVS metadata:** Descripción del servicio, endpoints de infraestructura, parámetros económicos (comisiones, recompensas), y condiciones de slashing
- **Operator sets:** Lista de operadores activos validando cada AVS con su stake delegado correspondiente
- **Performance tracking:** Algunos AVS publican métricas de performance on-chain para transparencia y reputación

### Flujo de Fondos y Lifecycle de Restaking

**Fase 1: Depósito y Restaking**

1. **Native Restaking (Validadores):**
   - Validador de Ethereum modifica sus withdrawal credentials apuntándolos a contratos de EigenLayer (`EigenPod`)
   - El ETH en stake del validador ahora puede ser slasheado por EigenLayer además de Ethereum
   - Cuando el validador sale de Ethereum, los fondos se retiran a través de EigenLayer

2. **LST Restaking (Usuarios):**
   - Usuario posee Liquid Staking Tokens (stETH, rETH, cbETH, etc.)
   - Deposita LSTs en el contrato `StrategyManager` de EigenLayer
   - Recibe "shares" representando su posición restaked
   - Continúa ganando rewards de staking del LST subyacente + rewards de AVS

**Fase 2: Delegación a Operadores**

- Staker elige un operador basándose en reputación, comisiones, y AVS que valida
- Llama a `delegateTo()` en DelegationManager, asignando su stake al operador
- El stake delegado aumenta el poder de validación del operador en los AVS donde está registrado
- Staker puede cambiar de operador (proceso de "redelegation") con períodos de espera

**Fase 3: Operador Valida AVS**

- Operador ejecuta infraestructura off-chain para los AVS donde está registrado (nodos de oráculo, validadores de bridge, sequencers, etc.)
- Participa en protocolos de consenso o validación específicos de cada AVS
- Firma attestations, propone bloques, ejecuta computación, según requerimientos del AVS
- Sus acciones están respaldadas por el stake delegado; comportamiento malicioso resulta en slashing

**Fase 4: Distribución de Recompensas**

- AVS pagan recompensas a operadores (típicamente en tokens nativos del AVS o ETH)
- Operadores retienen su comisión (configurada en DelegationManager, típicamente 5-20%)
- Recompensas netas se distribuyen proporcionalmente a stakers delegados
- Distribución puede ser on-chain (gas costoso) o mediante Merkle proofs off-chain con claims on-chain

**Fase 5: Retiro y Unstaking**

- Staker inicia proceso de retiro llamando a `queueWithdrawal()` en StrategyManager
- Entra en período de espera (típicamente 7 días) durante el cual puede ser slasheado si su operador actúa maliciosamente
- Después del período, completa retiro con `completeQueuedWithdrawal()`
- Recibe sus LSTs de vuelta (o puede reclamar ETH nativo si hizo native restaking)

## Restaking: Native vs LST

EigenLayer soporta dos modelos fundamentalmente diferentes de restaking, cada uno con trade-offs distintos en riesgo, rendimiento, y complejidad operacional.

### Native Restaking

**Mecánica Técnica:**

Los validadores de Ethereum ejecutan nodos beacon chain con 32 ETH en stake. Normalmente, sus withdrawal credentials apuntan a una dirección que controlan directamente. Con native restaking, modifican estas credentials para apuntar a un smart contract de EigenLayer llamado **EigenPod**, que actúa como intermediario:

- **EigenPod deployment:** Cada validador crea su propio EigenPod (contrato proxy individual) mediante `EigenPodManager.createPod()`
- **Cambio de credentials:** Llama a la función de Ethereum beacon chain para actualizar `0x01` withdrawal credentials al address del EigenPod
- **Proof submission:** Periódicamente, debe probar on-chain mediante Beacon Chain state proofs que su(s) validador(es) siguen activos y con balance correcto
- **Slashing exposure:** El ETH en stake puede ser slasheado tanto por Ethereum (por violaciones de consenso) como por EigenLayer (por violaciones de AVS)

**Ventajas:**

- **Capital efficiency máxima:** El mismo 32 ETH asegura Ethereum + múltiples AVS simultáneamente, maximizando utilización de capital
- **Sin intermediarios:** No depende de protocolos de liquid staking, eliminando riesgos de smart contracts de terceros
- **Rewards compuestos:** Gana rewards de Ethereum + rewards de AVS sin diluir posición

**Desventajas:**

- **Complejidad técnica:** Requiere ejecutar nodo validador completo (clientes de ejecución + consenso), mantener >99% uptime, monitorear múltiples AVS
- **Liquidez cero:** Los 32 ETH quedan completamente ilíquidos hasta que el validador sale de Ethereum (proceso de varios días/semanas)
- **Riesgo de slashing amplificado:** Expuesto a condiciones de slashing de Ethereum + todos los AVS donde participa; error en un AVS puede resultar en pérdida de todo el stake
- **Requisito de capital alto:** Necesitas exactamente 32 ETH (no más, no menos) para cada validador

### LST Restaking (Liquid Staking Token Restaking)

**Mecánica Técnica:**

Usuarios que poseen tokens de liquid staking (representaciones tokenizadas de ETH en stake) pueden depositarlos en EigenLayer para restaking:

- **Tokens soportados:** stETH (Lido), rETH (Rocket Pool), cbETH (Coinbase Wrapped Staked ETH), ankrETH, osETH, entre otros whitelisted
- **Depósito simple:** Llama a `StrategyManager.depositIntoStrategy(strategy, token, amount)` desde cualquier wallet
- **Shares accounting:** Recibe "shares" de EigenLayer que representan su posición restaked, similar a LP tokens en DeFi
- **Composabilidad:** Los LSTs continúan generando staking rewards del protocolo base mientras están restaked en EigenLayer

**Ventajas:**

- **Accesibilidad:** Cualquiera con cualquier cantidad de LSTs puede participar (no requiere 32 ETH completos)
- **Liquidez preservada:** Los LSTs son tradeable en DEXs; si necesitas liquidez urgente, puedes vender aunque haya delays de retiro en EigenLayer
- **Sin infraestructura:** No necesitas ejecutar validadores; solo depositar tokens en smart contract
- **Diversificación de riesgo:** Si usas múltiples LSTs de diferentes proveedores, diversificas riesgo de implementación

**Desventajas:**

- **Capas de riesgo apiladas:** Expuesto a riesgos de smart contract de EigenLayer + protocolo de liquid staking subyacente + Ethereum
- **Comisiones adicionales:** Protocolos de liquid staking cobran comisión (típicamente 10% de rewards); EigenLayer operadores cobran otra comisión (5-20%)
- **Menor capital efficiency:** El LST debe mantener liquidity premium para ser tradeable, lo que comprime rendimientos vs native staking
- **Dependencia de oráculos:** Algunos LSTs (especialmente rebasing como stETH) requieren oráculos para tracking de balance, introduciendo vectores de ataque

### Comparación de Rendimientos Esperados

Ejemplo numérico (valores aproximados, enero 2026):

**Native Restaking:**

- Ethereum PoS base: ~3.5% APR en ETH
- EigenLayer AVS rewards: ~2-6% APR adicional (varía según AVS)
- **Total: ~5.5-9.5% APR**
- Riesgo: Slashing de Ethereum + slashing de AVS

**LST Restaking (ejemplo con stETH):**

- Lido staking rewards: ~3.2% APR (3.5% menos 10% comisión)
- EigenLayer AVS rewards: ~2-6% APR
- Menos comisión operador EigenLayer: ~-0.3% APR (asumiendo 15% comisión sobre AVS rewards)
- **Total: ~4.9-8.9% APR**
- Riesgo: Slashing de Ethereum + slashing de Lido + slashing de EigenLayer AVS + riesgo de smart contract de Lido

La diferencia de ~0.6-0.7% refleja las comisiones adicionales del liquid staking, pero viene con ventaja de liquidez y menor barrera de entrada.

## AVS: Actively Validated Services

Los AVS son servicios descentralizados que requieren validación activa por operadores y utilizan EigenLayer para seguridad económica. Cada AVS define su propia lógica de negocio, protocolo de validación, y condiciones de slashing.

### Arquitectura de un AVS

Un AVS típico consta de varios componentes interconectados:

**1. Smart Contracts On-Chain (Ethereum Mainnet)**

- **AVS Service Manager:** Contrato principal que se registra en el EigenLayer AVS Directory
- **Slashing conditions:** Define qué comportamientos de operadores son penalizables y con qué severidad
- **Task definitions:** Especifica qué trabajo deben realizar los operadores (attestations, computación, relay de mensajes, etc.)
- **Reward distribution:** Implementa lógica de cómo se distribuyen pagos a operadores basado en performance

**2. Infraestructura Off-Chain**

- **Validador nodes:** Software que operadores ejecutan para participar en el protocolo del AVS
- **Peer-to-peer network:** Red de comunicación entre operadores para consenso o coordinación
- **APIs/Oracles:** Servicios que proveen datos del mundo exterior al AVS si es necesario
- **Monitoring dashboards:** Herramientas para que operadores monitoreen su performance y status

**3. Protocolo de Consenso/Validación**

Cada AVS implementa su propia lógica de cómo múltiples operadores alcanzan consenso o validan información:

- **Threshold signatures:** Algunos AVS requieren que mayoría de operadores (ponderados por stake) firmen attestations
- **Optimistic validation:** Otros asumen validez y solo penalizan si se detecta fraude (similar a Optimistic Rollups)
- **BFT consensus:** AVS más complejos pueden implementar consenso Byzantine Fault Tolerant completo
- **Economic finality:** Usan el stake agregado de operadores como garantía económica de correctitud

### Casos de Uso y Ejemplos de AVS

**EigenDA (Data Availability)**

EigenDA es el primer AVS desarrollado por el equipo de EigenLayer, diseñado como capa de disponibilidad de datos de alta performance para Ethereum rollups:

- **Problema que resuelve:** Rollups necesitan publicar datos de transacciones en Ethereum para que cualquiera pueda reconstruir estado. Ethereum mainnet es costoso (~$0.01-$0.10 por KB según congestión). Proto-Danksharding (EIP-4844) mejoró esto con blobs, pero sigue limitado.
- **Solución:** EigenDA permite rollups publicar datos off-chain a una red de operadores EigenLayer que garantizan disponibilidad mediante compromisos criptográficos (KZG) y erasure coding.
- **Arquitectura:**
  - Rollup sequencer publica bloque a EigenDA network
  - Operadores reciben datos, generan erasure coded chunks, almacenan localmente
  - Quorum de operadores (ponderados por stake) firma certificate de disponibilidad
  - Certificate se publica on-chain en Ethereum como proof de que datos están disponibles
  - Rollup puede usar este certificate para finalizar bloques
- **Economía:** Rollups pagan comisiones a operadores basadas en throughput de datos. Operadores ganan ~5-15% APR adicional según volumen.
- **Security model:** Si >2/3 del stake certifican datos falsamente no-disponibles, todos son slasheados. Cost of corruption excede valor de atacar porque stake > potencial ganancia de censura de rollup.

**Cross-Chain Bridges**

Varios proyectos están desarrollando bridges cross-chain asegurados por EigenLayer:

- **Hyperlane + EigenLayer:** Hyperlane es protocolo de mensajería cross-chain interoperable. Integrando EigenLayer, los relayers que pasan mensajes entre cadenas están respaldados por stake de operadores EigenLayer. Si un relayer miente sobre estado de una cadena, es slasheado.
- **Omni Network:** Blockchain específicamente diseñada como universal interoperability layer. Usa EigenLayer para asegurar sus validadores, permitiendo que hereden seguridad de Ethereum.
- **Arquitectura típica:**
  - Operadores ejecutan light clients o full nodes de ambas cadenas (origen y destino)
  - Atestiguan estado de cadena origen (ej: "transacción X fue incluida en bloque Y")
  - Quorum de attestations activa unlock de fondos en cadena destino
  - Si operadores atestiguan estado falso, son slasheados por cantidad proporcional al valor en riesgo

**Sequencers Descentralizados para Rollups**

Rollups como Arbitrum y Optimism actualmente operan sequencers centralizados que ordenan transacciones. Esto introduce riesgo de censura y punto único de falla:

- **Propuesta:** Operadores EigenLayer actúan como sequencers distribuidos, rotando responsabilidad de proponer bloques
- **Resistencia a censura:** Usuario puede pagar a cualquier operador del conjunto para incluir transacción; si un operador censura, otro la incluirá
- **Protocolo:**
  - Operadores compiten por derecho a secuenciar próximo lote de transacciones
  - Ganador propone bloque candidato
  - Otros operadores validan y atestiguan
  - Bloque finalizado se publica a L1
- **Slashing:** Sequencer que propone bloque inválido o intenta doble-spend es slasheado

**Oráculos Descentralizados**

Aunque Chainlink es el líder establecido, múltiples proyectos exploran usar EigenLayer para oráculos:

- **eOracle:** Oracle de precios asegurado por EigenLayer. Operadores reportan precios de múltiples fuentes, se agrega mediana, quorum firma resultado.
- **Ventaja sobre oráculos tradicionales:** No requiere token nativo para seguridad; hereda pool de ETH en stake. Ataque requiere corromper stake mucho mayor que valor de manipulación de precio posible.
- **Slashing conditions:** Reportar precio >X% desviado de mediana o no reportar dentro de deadline resulta en slashing proporcional.

**Coprocessors (ZK y Optimistic)**

Servicios de computación off-chain verificable:

- **Brevis:** ZK coprocessor que permite smart contracts leer datos históricos de Ethereum o state de otras blockchains mediante ZK proofs. Operadores EigenLayer generan y validan proofs.
- **RISC Zero + EigenLayer:** Permite ejecutar programas arbitrarios off-chain (código en Rust/C++) y probar correctitud on-chain mediante ZK proofs. Operadores EigenLayer generan y validan.
- **Use case:** Smart contract quiere verificar que un usuario tiene historial on-chain específico sin iterar toda la historia (gas prohibitivo). Coprocessor genera proof, operadores validan, contract acepta resultado.

**MEV Management y Fair Ordering**

Proyectos que buscan mitigar MEV (Maximal Extractable Value) usando EigenLayer:

- **Flashbots SUAVE (Single Unified Auction for Value Expression):** Propuesta para mempool descentralizado donde operadores EigenLayer ejecutan subasta de MEV de forma transparente y justa
- **Shutter Network:** Threshold encryption para transactions; operadores EigenLayer mantienen shards de clave de descifrado y solo revelan después de que orden de transacciones está committed

### Lifecycle y Economía de un AVS

**Lanzamiento:**

1. Desarrollador crea smart contracts del AVS en Ethereum
2. Registra AVS en EigenLayer AVS Directory con metadata
3. Define slashing conditions y parámetros económicos
4. Lanza infraestructura off-chain (software de operador, documentación)
5. Recluta primeros operadores (típicamente mediante partnerships o grants)

**Bootstrapping:**

- AVS típicamente ofrece incentivos altos iniciales para atraer operadores (subsidios en token nativo, airdrops, etc.)
- Necesita alcanzar quorum mínimo de stake para seguridad creíble (típicamente $10M+ en valor de stake respaldado)
- Construye reputación mediante operación libre de incidentes y auditorías de seguridad

**Operación Estable:**

- AVS cobra a usuarios/aplicaciones que consumen sus servicios (comisiones de transacción, subscripciones, comisiones por computación)
- Distribución: ~50-70% a operadores, ~10-20% al tesoro del protocolo AVS, ~10-20% a stakers pasivos
- Operadores compiten por inclusión basándose en performance (uptime, latency) y comisiones cobradas

**Riesgos y Mitigación:**

- **Underpricing de riesgo:** Si recompensas del AVS son muy bajas comparadas con riesgo de slashing, operadores no participan o capital insuficiente
- **Slashing cascades:** Bug en condiciones de slashing podría slashear injustamente a operadores honestos, causando mass exit
- **Centralización de operadores:** Si operar AVS requiere hardware especializado caro, solo operadores grandes participan

## Slashing: Condiciones y Ejecución

El slashing es el mecanismo de seguridad económica central de EigenLayer. Define cómo se penalizan operadores que actúan maliciosamente o fallan en cumplir obligaciones.

### Principios de Diseño de Slashing

**Atribución de Responsabilidad:**

Para que slashing sea efectivo, debe ser posible probar criptográficamente que un operador específico actuó maliciosamente. Esto requiere:

- **Firmas digitales:** Toda acción del operador (attestation, propuesta de bloque, reporte de datos) debe estar firmada con su clave privada
- **Commits on-chain:** Acciones críticas deben tener footprint on-chain (aunque sea hash commitment) para inmutabilidad temporal
- **Pruebas verificables:** Evidencia de mal comportamiento debe ser verificable on-chain por smart contracts de forma determinista

**Proporcionalidad:**

Severidad del slashing debe corresponder a severidad de la falta y valor en riesgo:

- **Faltas menores:** Downtime, latencia alta → penalización pequeña (~0.1-1% del stake)
- **Faltas moderadas:** Attestations incorrectas sin impacto significativo → ~1-5% del stake
- **Faltas mayores:** Doble-firma, fraude probado, certificación de datos falsos → ~10-50% del stake o expulsión completa

**Correlation Penalties:**

Si múltiples operadores son slasheados simultáneamente por el mismo evento, la penalización de cada uno aumenta. Esto previene colusión:

- Fórmula típica: `slashing_amount = base_slash * (1 + correlation_factor * num_slashed / total_operators)`
- Ejemplo: Si 1 operador es slasheado solo, pierde 10%. Si 30% de operadores son slasheados juntos por mismo evento, cada uno pierde 10% * (1 + 0.5 * 0.3) = 11.5%. Si 90% son slasheados juntos, cada uno pierde 10% * (1 + 0.5 * 0.9) = 14.5%.

Este mecanismo hace que ataques coordinados sean exponencialmente más caros que ataques individuales.

**Períodos de Disputa:**

Para prevenir slashing falso por bugs o manipulación maliciosa:

- Cuando slashing es propuesto, entra en período de disputa (~7-14 días)
- Durante este tiempo, operador o comunidad pueden presentar evidencia contraria
- Comité de gobernanza (inicialmente multisig, eventualmente DAO) puede vetar slashing injusto
- Después del período sin disputa exitosa, slashing se ejecuta

### Ejemplos de Condiciones de Slashing por AVS

**EigenDA:**

- **Falso certificate de disponibilidad:** Operador firma que datos están disponibles cuando no lo están → slashing 30% del stake asignado a EigenDA
- **No responder a challenges:** Si alguien desafía disponibilidad y operador no provee datos en tiempo límite → slashing 10%
- **Downtime prolongado:** >24 horas sin responder a requests de disponibilidad → reducción gradual de rewards, eventualmente remoción del conjunto activo

**Bridge AVS:**

- **Certificar estado falso:** Operador atestigua que transacción ocurrió en cadena origen cuando no ocurrió → slashing 50% de stake (proporcional a valor en riesgo del bridge)
- **Doble-firma:** Firmar dos estados contradictorios para misma altura de bloque → slashing completo + expulsión permanente
- **Censura probada:** Si operador consistentemente ignora transacciones válidas y se puede probar que las recibió → penalización gradual escalando a remoción

**Oracle AVS:**

- **Reportar precio outlier:** Precio reportado >20% desviado de mediana sin justificación externa verificable → slashing 5% de stake
- **No reportar en deadline:** Fallar en enviar reporte dentro de ventana de tiempo → pérdida de rewards del período + penalización menor (~1%) si es recurrente
- **Manipulación coordinada:** Si múltiples operadores reportan precio manipulado en coordinación → correlation penalty amplifica slashing a ~20-40%

### Proceso Técnico de Slashing

**1. Detección y Prueba:**

- **Watchers:** Terceros que monitorean AVS e identifican mal comportamiento (incentivados con bounties, típicamente 5-10% del monto slasheado)
- **Proof generation:** Watcher construye prueba criptográfica de mal comportamiento:
  - Firma del operador malicioso
  - Estado on-chain contradictorio
  - Evidencia de timestamps (para probar que operador tenía información en momento de firmar)

**2. Submission On-Chain:**

- Watcher llama a `Slasher.freezeOperator(operator, avsAddress, proof)` en contrato de EigenLayer
- Operador es inmediatamente "frozen": no puede participar en más validaciones, no puede retirar stake
- Se publica toda evidencia on-chain públicamente para transparencia

**3. Período de Disputa:**

- Comunidad, operador afectado, o auditores independientes revisan evidencia
- Si encuentran error en la prueba, pueden presentar contra-prueba
- Multisig de gobernanza (actualmente ~7 miembros, incluyendo Vitalik Buterin, representantes de liquid staking protocols, investigadores) puede vetar
- En futuro, esto migrará a DAO governance con votación token-weighted

**4. Ejecución de Slashing:**

- Si período de disputa expira sin veto, `Slasher.slashShares(operator, strategies[], slashAmounts[])` ejecuta penalización
- Shares correspondientes del operador en cada estrategia se reducen
- Stake subyacente (ETH o LSTs) se transfiere:
  - Porción al watcher que reportó (bounty)
  - Porción quemada (burned) para aumentar escasez
  - Porción al tesoro del AVS para compensar daños

**5. Recuperación Post-Slashing:**

- Operador puede reiniciar operaciones después de pagar penalización
- Si slashing fue parcial (<50%), puede continuar con stake reducido
- Si fue severo (>50%) o expulsión, debe re-registrarse y reconstruir reputación
- Stakers delegados al operador pueden elegir re-delegar a otro operador

### Desafíos y Limitaciones del Slashing

**Atribución Compleja en Sistemas Distribuidos:**

En protocolos donde múltiples operadores colaboran, determinar responsabilidad individual es difícil:

- ¿Quién es culpable si threshold signature tiene firmas suficientes pero resultado es incorrecto?
- Si operador relay mensaje corrupto pero firmó basándose en información de otro operador upstream, ¿quién se slashea?

Soluciones propuestas incluyen slashing proporcional donde todos los participantes en acción maliciosa comparten penalización, o protocolos de atestación en capas donde cada etapa es atribuible individualmente.

**False Positives:**

Bugs en condiciones de slashing podrían slashear operadores honestos:

- Bug de software hace que operador honesto envíe firma malformada interpretada como maliciosa
- Sincronización de red causa que operador vea estado diferente temporalmente y actúe en base a ello
- Reorganización de blockchain hace que acción previamente válida se vuelva inválida retrospectivamente

Mitigaciones incluyen testing exhaustivo, auditorías de condiciones de slashing, períodos de disputa amplios, y insurance protocols donde operadores pueden comprar seguro contra slashing injusto.

**Slashing Insuficiente:**

Si stake respaldando AVS es menor que valor en riesgo, atacar es racionalmente rentable:

- AVS custodia $100M en assets, pero solo tiene $50M en stake respaldándolo
- Atacante puede corromper operadores por $50M, robar $100M, net profit $50M

Solución requiere que AVS calibren parámetros económicos conservadoramente: `stake_required >= k * value_at_risk` donde k > 1 (típicamente 2-3x para margen de seguridad).

## Seguridad y Riesgos

### Modelos de Seguridad

**Seguridad Económica vs Seguridad Criptográfica:**

EigenLayer proporciona seguridad económica, no seguridad criptográfica absoluta:

- **Seguridad criptográfica:** Romper criptografía (ECDSA, SHA-256, etc.) es computacionalmente imposible con tecnología actual
- **Seguridad económica:** Atacar es económicamente irracional porque costo > beneficio potencial

Esto significa que ataques con suficiente capital son teóricamente posibles si beneficio excede stake en riesgo. La defensa depende de alinear incentivos económicos correctamente.

**Supuestos de Honest Majority:**

La mayoría de AVS asumen que >2/3 del stake es controlado por operadores honestos. Si esto se viola, seguridad colapsa:

- **Attack vector:** Cartelización donde operadores grandes colusionan para certificar datos falsos y compartir ganancias
- **Mitigación:** Diversidad geográfica, reputacional y jurisdiccional de operadores; mecanismos de slashing con correlation penalties; gobernanza que puede intervenir en emergencias

### Riesgos Específicos de EigenLayer

**1. Slashing Cascades**

Si bug o exploit causa slashing masivo de operadores, puede desencadenar efectos dominó:

- Operadores slasheados salen del sistema
- Stake total respaldando AVS cae por debajo de niveles seguros
- Usuarios pierden confianza y retiran, acelerando espiral descendente
- AVS se vuelven inseguros o colapsan completamente

**Mitigaciones:**

- Límites de slashing por epoch (no más de X% del stake total puede ser slasheado en período Y)
- Insurance funds que cubren primeras pérdidas en caso de slashing injusto masivo
- Auditorías rigurosas de condiciones de slashing antes de mainnet

**2. Centralización de Operadores**

Si operar en EigenLayer + múltiples AVS requiere hardware sofisticado, ancho de banda alto y expertise técnico profundo, solo operadores institucionales participan:

- Pocos operadores grandes controlan mayoría del stake
- Riesgo de colusión aumenta
- Single point of failure si operador grande falla simultáneamente en múltiples AVS

**Mitigaciones:**

- Diseñar AVS con requisitos técnicos accesibles
- Programas de grants para operadores pequeños/medianos
- Métricas de descentralización públicas que incentiven diversidad

**3. Riesgos de Composabilidad**

EigenLayer introduce composabilidad compleja entre múltiples capas:

- Ethereum PoS → EigenLayer → múltiples AVS → aplicaciones consumidoras
- Vulnerabilidad en cualquier capa puede propagar a través del stack
- Exploit en un AVS pequeño podría afectar operadores que validan muchos otros AVS

**Mitigaciones:**

- Isolación de riesgo: stakers pueden elegir qué AVS respaldar con su stake
- Validación de AVS por comités de seguridad antes de listing oficial
- Límites de apalancamiento: un operador no puede restakear mismo capital en infinitos AVS, solo hasta multiplicador configurado (ej. 3-5x)

**4. Governance Attacks**

Actualmente, EigenLayer tiene multisig centralizado para decisiones críticas (veto de slashing, upgrades de contratos, aprobación de AVS):

- 7-of-13 multisig con miembros de alta reputación
- Riesgo: captura por entidad maliciosa, coerción de firmantes, o decisiones mal intencionadas

**Roadmap de mitigación:**

- Transición gradual a gobernanza descentralizada mediante token de governance (aún no lanzado, pero planeado)
- Timelock contracts que dan tiempo a comunidad para reaccionar ante cambios
- Separación de poderes: diferentes comités para diferentes decisiones (slashing vs upgrades vs listing de AVS)

### Security Audits y Bug Bounties

EigenLayer ha sido auditado múltiples veces por firmas de seguridad top-tier:

- **Sigma Prime:** Audit de core contracts (2023)
- **Quantstamp:** Audit de EigenDA (2024)
- **Consensys Diligence:** Audit de slashing mechanisms (2024)

Bug bounty programa activo con recompensas de hasta $1M para vulnerabilidades críticas. Historial hasta la fecha (enero 2026) no incluye hacks significativos de fondos en mainnet, aunque testnet ha experimentado múltiples exploits que llevaron a mejoras.

## Operadores y Delegación

### Perfil de un Operador EigenLayer

Operar en EigenLayer requiere capacidad técnica, capital, y gestión de riesgo sofisticada:

**Requisitos Técnicos:**

- Ejecutar validador de Ethereum (si hacen native restaking)
- Infraestructura para cada AVS donde participan (nodos, APIs, monitoring)
- Conectividad de red confiable (>99.9% uptime)
- Seguridad operacional robusta (key management, access controls, incident response)

**Requisitos de Capital:**

- Stake inicial propio o capital delegado suficiente para alcanzar quorum de AVS
- Colateral para cubrir potencial slashing (~10-30% del stake operado)
- Liquidez para cubrir costos operacionales antes de primera distribución de rewards

**Expertise:**

- DevOps para deploy y mantenimiento de infraestructura distribuida
- Conocimiento de protocolos específicos de cada AVS
- Monitoreo de condiciones de slashing y mitigación de riesgos

**Operadores Principales (enero 2026):**

- **Figment:** Operador institucional validando Ethereum + 20+ AVS, ~$500M delegado
- **Coinbase Cloud:** Brazo de infraestructura de Coinbase, enfoque en compliance y seguridad
- **P2P.org:** Operador especializado con reputación en múltiples PoS networks
- **InfStones:** Proveedor de infraestructura con presencia global
- **Operadores community-run:** Cientos de operadores pequeños/medianos validando subconjunto de AVS

### Delegación de Stake

**Por qué delegar:**

La mayoría de holders de ETH no tienen expertise técnico o recursos para operar infraestructura. Delegación permite participar en EigenLayer sin esfuerzo operacional:

- Depositas ETH o LSTs en EigenLayer
- Eliges operador(es) confiable(s)
- Ganas rewards pasivamente (menos comisión del operador)
- No necesitas ejecutar nada técnico

**Criterios de Selección de Operador:**

- **Track record:** Historial de uptime, incidentes de slashing previos, años operando
- **Comisión:** Típicamente 5-20%; más baja no siempre es mejor si implica menor calidad
- **AVS portfolio:** Qué AVS valida el operador (diversificación de riesgo)
- **Transparencia:** Operadores top publican métricas de performance, reportes de incidentes, comunicación con delegators
- **Stake propio:** ¿Cuánto stake propio tiene el operador (skin in the game)? Mínimo ~5-10% del total es buena señal

**Proceso Técnico de Delegación:**

1. Depositar ETH/LSTs en EigenLayer StrategyManager
2. Llamar a `DelegationManager.delegateTo(operatorAddress, approverSignature, salt, expiry)`
3. Tu stake ahora contribuye al poder de validación del operador en sus AVS
4. Rewards se acumulan automáticamente
5. Para cambiar operador: `undelegate()` (con 7-day delay) → `delegateTo(newOperator)`

**Redelegation y Switching Costs:**

Cambiar de operador no es instantáneo:

- Undelegate → período de espera ~7 días → completa withdrawal → re-delegate a nuevo operador
- Durante período de espera, no ganas rewards de AVS (solo rewards base de staking)
- Esto crea "stickiness" que favorece operadores con reputación establecida vs nuevos entrantes

**Liquid Delegation Tokens (Futuro):**

Protocolos están desarrollando LST-like tokens que representan posiciones delegadas:

- Depositas en vault que delega a operador
- Recibes token líquido (ej. "eLSTETH")
- Puedes vender este token sin esperar período de undelegate
- Comprador hereda tu posición delegada

Esto mejora capital efficiency pero añade capa adicional de riesgo de smart contract.

## Ecosistema y Adopción

### Métricas Actuales (enero 2026)

- **TVL (Total Value Locked):** ~$12-15B en ETH y LSTs restaked
- **Número de operadores:** ~800-1000 operadores registrados
- **AVS activos:** ~30-40 AVS en mainnet, ~100+ en testnet o desarrollo
- **Distribución de stake:**
  - Lido stETH: ~45% del TVL
  - Rocket Pool rETH: ~15%
  - Native restaking: ~20%
  - Otros LSTs (cbETH, ankrETH, etc.): ~20%

### Competidores y Alternativas

**Symbiotic:**

Protocolo alternativo de restaking lanzado por Paradigm con diseño similar pero más flexible:

- Soporta cualquier collateral (no solo ETH), incluyendo stablecoins y tokens de protocolos
- Modelos de seguridad más customizables por AVS
- Menor adopción inicial que EigenLayer pero crecimiento rápido

**Cosmos Interchain Security (ICS):**

Permite que chains en ecosistema Cosmos alquilen seguridad del Cosmos Hub:

- Modelo más antiguo (pre-EigenLayer) específico de Cosmos
- Validadores del Hub automáticamente validan consumer chains
- No tan flexible como EigenLayer; más acoplado a arquitectura de Cosmos

**Polkadot Shared Security:**

Parachains en Polkadot heredan seguridad del Relay Chain:

- Built-in en arquitectura de Polkadot, no opt-in como EigenLayer
- Todas las parachains comparten mismo conjunto de validadores
- Menos flexible pero más integrado

**Diferencias clave de EigenLayer:**

- Construido sobre Ethereum, hereda base de validadores más grande ($30B+ en stake)
- Opt-in voluntario permite experimentación y diversidad de AVS
- Mercado libre de seguridad vs modelo centralizado de otros ecosistemas

## Futuro y Roadmap

### Desarrollos Técnicos Planificados

**1. Programmable Slashing**

Actualmente, condiciones de slashing son relativamente estáticas, definidas en smart contracts. Visión futura incluye:

- AVS pueden actualizar condiciones dinámicamente basándose en evolución del protocolo
- Slashing condicional: penalización depende de contexto (ej. mayor slashing durante periodos de alta actividad)
- Insurance mechanisms integrados donde operadores pueden comprar cobertura contra slashing falso positivo

**2. Eigenlayer Token y Governance Descentralizada**

Token de governance (ticker probablemente EIGEN) planeado para:

- Voting on-chain sobre decisiones críticas (veto de slashing, upgrades de protocolo, aprobación de AVS)
- Staking adicional: holders pueden stakear token para participar en governance y ganar rewards
- Reemplazo gradual del multisig actual con DAO completamente descentralizada

**3. Cross-Chain EigenLayer**

Expansión más allá de Ethereum mainnet:

- EigenLayer en L2s (Arbitrum, Optimism, Base) para fees más bajos y mayor throughput
- Integración con otras blockchains compatibles (BNB Chain, Avalanche) para restaking cross-chain
- Desafío: mantener garantías de seguridad cuando stake está fragmentado entre múltiples chains

**4. Mejoras de Capital Efficiency**

- Superfluid staking: mismo capital genera rewards de staking + rewards de EigenLayer + yield de DeFi simultáneamente
- Leverage restaking: protocolos de lending donde puedes usar posición restaked como collateral para pedir prestado y re-restakear
- Riesgo: apalancamiento excesivo puede amplificar pérdidas en caso de slashing

### Visión a Largo Plazo

EigenLayer aspira a convertirse en la **capa de seguridad universal de Web3**, donde cualquier servicio descentralizado puede conectarse instantáneamente a mercado de seguridad líquida:

- **Fragmentation to unification:** En lugar de cada protocolo bootstrapping seguridad independiente, todos comparten pool de Ethereum
- **Security as a service:** AVS pagan por seguridad como utility, similar a cómo cloud computing funciona para cómputo
- **Commoditization de validación:** Operadores se vuelven proveedores comoditizados de validación; AVS compiten en diseño de protocolo y experiencia de usuario, no en atraer validadores

Esta visión tiene paralelos con cómo AWS/Azure commoditizaron infraestructura de servidores: antes cada startup necesitaba comprar servidores propios, ahora alquilan compute de clouds. EigenLayer busca hacer lo mismo con seguridad criptoeconómica.

## Recursos y Referencias

- **Sitio oficial:** [eigenlayer.xyz](https://www.eigenlayer.xyz/)
- **Documentación técnica:** [docs.eigenlayer.xyz](https://docs.eigenlayer.xyz/)
- **Whitepaper:** "EigenLayer: The Restaking Collective" - Sreeram Kannan et al.
- **GitHub:** [github.com/Layr-Labs/eigenlayer-contracts](https://github.com/Layr-Labs/eigenlayer-contracts)
- **Forum de investigación:** [research.eigenlayer.xyz](https://research.eigenlayer.xyz/)
- **Dashboard de métricas:** [app.eigenlayer.xyz](https://app.eigenlayer.xyz/)
- **Lista de AVS:** [eigenlayer.xyz/ecosystem](https://www.eigenlayer.xyz/ecosystem)

### Papers Académicos Relacionados

- "The Limits of Shared Security" - Vitalik Buterin (2023)
- "Restaking Economics: Security Amplification or Risk Concentration?" - Paradigm Research (2024)
- "Cross-Layer MEV in Restaking Protocols" - Flashbots Research (2024)

---
