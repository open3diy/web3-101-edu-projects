# Transactions

## Concepto

Una transacción es una instrucción firmada criptográficamente que modifica el estado de la blockchain. Es el mecanismo fundamental mediante el cual los usuarios interactúan con la red, ya sea transfiriendo valor, ejecutando smart contracts, o realizando cualquier operación on-chain.

Cada transacción es atómica: se ejecuta completamente o no se ejecuta en absoluto. No existen estados intermedios. Una vez incluida en un bloque y confirmada por la red, la transacción se vuelve inmutable y permanece en la blockchain para siempre.

## Anatomía de una Transacción

### Componentes Básicos

Una transacción en Ethereum contiene los siguientes campos:

Nonce

Número secuencial que indica cuántas transacciones ha enviado una dirección. Previene ataques de replay (re-envío de la misma transacción) y garantiza que las transacciones se procesen en orden. Cada transacción incrementa el nonce en 1.

From

Dirección del remitente que firma la transacción. Se deriva de la clave pública usada para firmar.

To

Dirección del destinatario. Puede ser una dirección de usuario (EOA) o un contrato inteligente. Si está vacío (null), indica que es una transacción de creación de contrato.

Value

Cantidad de ETH (en wei) que se transfiere. 1 ETH = 10^18 wei. Puede ser 0 si la transacción solo ejecuta código sin transferir valor.

Data

Campo de datos arbitrarios. Para transferencias simples de ETH está vacío. Para interacciones con contratos contiene la llamada a función codificada (function signature + parámetros).

Gas Limit

Cantidad máxima de gas que el remitente está dispuesto a gastar en la transacción. Si la ejecución requiere más gas, la transacción falla pero igual consume el gas.

Gas Price / Max Fee

Precio que el usuario está dispuesto a pagar por unidad de gas. Desde EIP-1559, se divide en:

- Base Fee: tarifa base que se quema (burn)
- Priority Fee (tip): propina para el validador

Signature (v, r, s)

Firma criptográfica ECDSA que prueba que el propietario de la clave privada autorizó la transacción. Consta de tres valores: v (recovery id), r y s (componentes de la firma).

### Ejemplo de Transacción

```json
{
  "from": "0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb",
  "to": "0x5aAeb6053F3E94C9b9A09f33669435E7Ef1BeAed",
  "value": "1000000000000000000",
  "gas": "21000",
  "maxFeePerGas": "20000000000",
  "maxPriorityFeePerGas": "1000000000",
  "nonce": "5",
  "data": "0x",
  "chainId": "1"
}
```

Esta transacción transfiere 1 ETH con un límite de gas de 21,000 unidades (mínimo para transferencias simples).

## Tipos de Transacciones

### Transfer de ETH

Transacción más simple que transfiere ether de una dirección a otra.

- Gas usado: 21,000 unidades (fijo)
- Campo data: vacío (0x)
- To: dirección del destinatario

### Contract Interaction

Transacción que llama a una función de un smart contract.

- Gas usado: variable según complejidad del código
- Campo data: contiene la función codificada y parámetros
- To: dirección del contrato

Ejemplo de data para llamar a `transfer(address,uint256)`:

```solidity
0xa9059cbb
0000000000000000000000005aAeb6053F3E94C9b9A09f33669435E7Ef1BeAed
0000000000000000000000000000000000000000000000000de0b6b3a7640000
```

- `a9059cbb`: function selector (primeros 4 bytes del hash de la firma)
- Siguientes 32 bytes: dirección del destinatario
- Últimos 32 bytes: cantidad (1 ETH en este caso)

### Contract Creation

Transacción que despliega un nuevo smart contract.

- To: campo vacío (null o 0x)
- Data: contiene el bytecode del contrato
- Gas usado: depende del tamaño y complejidad del contrato
- Dirección resultante: calculada determinísticamente desde sender y nonce

Cálculo de dirección del contrato:

```javascript
contract_address = keccak256(rlp([sender_address, nonce]))[12:]
```

### Internal Transactions

No son transacciones reales en el sentido técnico, sino llamadas entre contratos que ocurren durante la ejecución de una transacción. No están firmadas y no aparecen directamente en la blockchain, pero los exploradores las muestran para mayor claridad.

## Gas y Fees

### Qué es Gas

Gas es la unidad que mide el costo computacional de ejecutar operaciones en Ethereum. Cada operación del EVM (suma, almacenamiento, transferencia) consume una cantidad específica de gas.

Ejemplos de costos:

- ADD (suma): 3 gas
- MUL (multiplicación): 5 gas
- SSTORE (escribir en storage): 20,000 gas (primera vez) o 5,000 gas (actualización)
- SLOAD (leer storage): 200 gas
- LOG: 375 gas + data

### Cálculo de Fees (Pre EIP-1559)

```text
Transaction Fee = Gas Used × Gas Price
```

Si usas 50,000 gas a 20 gwei/gas:

```text
Fee = 50,000 × 20 = 1,000,000 gwei = 0.001 ETH
```

### EIP-1559: Nuevo Modelo de Fees

Introducido en agosto 2021, cambia cómo se calculan las comisiones:

```text
Total Fee = Gas Used × (Base Fee + Priority Fee)
```

Base Fee

- Establecida por el protocolo según demanda de bloques
- Se ajusta automáticamente: +12.5% si bloque lleno, -12.5% si vacío
- Se quema (burn), no va a los validadores
- Predecible para los usuarios

Priority Fee (Tip)

- Propina opcional para el validador
- Incentivo para incluir tu transacción primero
- Va directamente al validador del bloque

Max Fee

- Máximo total que estás dispuesto a pagar por gas
- Si Base Fee + Priority Fee < Max Fee, se reembolsa la diferencia
- Protege contra picos repentinos de base fee

Ejemplo:

```text
Gas Used: 50,000
Base Fee: 30 gwei
Priority Fee: 2 gwei
Max Fee: 50 gwei

Actual Fee = 50,000 × (30 + 2) = 1,600,000 gwei = 0.0016 ETH
Max Possible Fee = 50,000 × 50 = 2,500,000 gwei = 0.0025 ETH
Refund = 0.0025 - 0.0016 = 0.0009 ETH
```

### Estimación de Gas

Las wallets estiman automáticamente el gas necesario usando `eth_estimateGas`. Esta función simula la transacción y calcula cuánto gas consumiría.

Factores que afectan el gas:

- Complejidad del código ejecutado
- Cantidad de datos escritos en storage
- Número de operaciones realizadas
- Estado actual del contrato (escribir en slot vacío vs actualizar)

Buenas prácticas:

- Agregar 10-20% de buffer a la estimación
- Revisar estimaciones en momentos de alta congestión
- Usar herramientas como ETH Gas Station para precios actuales

## Ciclo de Vida de una Transacción

### 1. Creación y Firma

Usuario crea la transacción con wallet, firma con clave privada. La firma demuestra autorización sin revelar la clave.

### 2. Broadcast

Transacción se envía a nodos de la red que la propagan mediante protocolo gossip. En segundos llega a miles de nodos.

### 3. Mempool

Transacciones pendientes esperan en el mempool (memory pool) de cada nodo. Ordenadas por priority fee, las más altas tienen prioridad.

### 4. Inclusión en Bloque

Validador selecciona transacciones del mempool para incluir en el siguiente bloque. Prioriza por fees y considera límite de gas del bloque (30M gas en Ethereum).

### 5. Ejecución

EVM ejecuta la transacción. Si falla (out of gas, revert, error), se revierte pero el gas se consume igual.

### 6. Confirmación

Bloque se propone y valida por la red. Después de 1 confirmación la transacción está incluida, pero se considera segura después de múltiples confirmaciones (típicamente 12-30 bloques para Ethereum).

### 7. Finalidad

En Ethereum post-Merge con Proof of Stake, la finalidad económica se alcanza después de 2 epochs (~12-15 minutos). Después de esto, revertir la transacción requeriría quemar millones de ETH en stakes.

## Estados de Transacción

### Pending

Transacción en mempool esperando ser incluida. Puede permanecer aquí si el gas price es muy bajo.

### Mined/Included

Incluida en un bloque pero aún puede ser reorganizada si hay fork temporal.

### Confirmed

Suficientes bloques después (típicamente 12+) que es prácticamente irreversible.

### Failed

Ejecución falló por error en el código, out of gas, o revert. El gas se consume pero el estado no cambia.

### Dropped

Removida del mempool por:

- Nonce reemplazado por otra transacción con mismo nonce y mayor fee
- Tiempo excesivo en mempool sin ser minada
- Gas price demasiado bajo

## Nonce y Gestión

### Importancia del Nonce

El nonce garantiza orden y previene ataques de replay. Cada transacción de una dirección debe usar el nonce correcto o será rechazada.

### Problemas Comunes

Nonce Gap

Si envías nonce 5 pero nonce 4 aún no se minó, la transacción 5 quedará pendiente hasta que 4 se procese.

Stuck Transaction

Transacción con gas price muy bajo que nunca se mina. Soluciones:

- Speed up: reenviar con mismo nonce y mayor fee
- Cancel: enviar transacción vacía a ti mismo con mismo nonce y mayor fee

### Múltiples Transacciones

Puedes enviar múltiples transacciones con nonces consecutivos. Se procesarán en orden si todas se minan.

## Optimización de Costos

### Timing

- Transaccionar en horarios de baja actividad (fines de semana, madrugadas UTC)
- Evitar lanzamientos populares de NFTs o eventos importantes
- Usar layer 2 solutions para operaciones frecuentes

### Gas Tokens (Histórico)

Antes de EIP-1559 existían tokens que aprovechaban reembolsos de gas. Ya no son efectivos.

### Batch Transactions

Smart contract wallets permiten agrupar múltiples operaciones en una transacción, ahorrando overhead.

### Layer 2

- Arbitrum, Optimism: fees 10-100x menores
- zkSync, Starknet: fees aún menores con zk-proofs
- Polygon: fees casi nulos pero menor seguridad

## Seguridad y Mejores Prácticas

### Verificación Antes de Firmar

- Revisar dirección de destino cuidadosamente
- Verificar cantidad y decimales del token
- Comprobar que el contrato está verificado en Etherscan
- Simular transacción con herramientas como Tenderly

### Aprobaciones

- Aprobar solo cantidades necesarias, no unlimited
- Revocar aprobaciones no usadas con Revoke.cash
- Cuidado con phishing que solicita aprobaciones maliciosas

### Gas Settings

- No establecer gas limit demasiado bajo (transacción fallará)
- Max fee razonable para evitar sobrepagos en picos
- Priority fee suficiente para inclusión oportuna

### Reemplazos

Para cancelar o acelerar transacción pendiente, usa mismo nonce con mayor fee. Algunas wallets tienen "Cancel" y "Speed Up" integrados.

## Herramientas y Recursos

### Exploradores de Blockchain

- [Etherscan](https://etherscan.io): explorador principal de Ethereum
- [Blockscout](https://blockscout.com): open source, múltiples chains
- Permite ver detalles completos de transacciones, contratos, direcciones

### Estimadores de Gas

- [ETH Gas Station](https://ethgasstation.info): recomendaciones de gas price
- [Blocknative Gas Estimator](https://www.blocknative.com/gas-estimator): predicciones en tiempo real
- Integrado en wallets modernas

### Simuladores

- [Tenderly](https://tenderly.co): simular y debuggear transacciones
- [Phalcon](https://phalcon.blocksec.com): análisis de transacciones complejas

### APIs

```javascript
// Obtener nonce con Web3.js
const nonce = await web3.eth.getTransactionCount(address);

// Estimar gas
const gasEstimate = await contract.methods.transfer(to, amount).estimateGas();

// Obtener precio de gas actual
const gasPrice = await web3.eth.getGasPrice();

// Enviar transacción
const tx = await web3.eth.sendTransaction({
  from: sender,
  to: recipient,
  value: web3.utils.toWei('1', 'ether'),
  gas: 21000
});
```

## Recursos Adicionales

- [Ethereum Yellow Paper](https://ethereum.github.io/yellowpaper/paper.pdf): especificación técnica completa
- [EIP-1559 Explicado](https://eips.ethereum.org/EIPS/eip-1559): nuevo modelo de fees
- [Etherscan Gas Tracker](https://etherscan.io/gastracker): monitoreo de gas en vivo
- [EVM Opcodes](https://www.evm.codes/): costos de gas por operación
