# Wallet

## Concepto

Un wallet o monedero es una herramienta que permite acceder a tu cuenta en la blockchain, gestionar tus claves privadas y autenticarse para realizar transacciones.

A diferencia de un monedero tradicional que guarda dinero físico, un wallet de criptomonedas no almacena las monedas en sí, sino las claves criptográficas que demuestran la propiedad de los fondos registrados en la blockchain.

### Funciones en el Ecosistema Web3

En el contexto de Ethereum y otras blockchains modernas, las wallets han evolucionado más allá del simple almacenamiento de claves. Funcionan como el punto central de interacción del usuario con todo el ecosistema descentralizado.

Puerta de Acceso a dApps

Las wallets permiten conectarte con aplicaciones descentralizadas sin necesidad de crear cuentas tradicionales. Cuando visitas una dApp como Uniswap para intercambiar tokens, OpenSea para comprar NFTs, o Aave para prestar criptomonedas, tu wallet funciona como tu identidad digital. La dApp detecta tu wallet, solicita conexión, y una vez aprobada puede leer tu dirección y saldos. Esta conexión es similar a "Iniciar sesión con Google" pero sin intermediarios centralizados.

Además, las wallets permiten firmar mensajes criptográficos para probar que controlas una dirección específica, útil para acceder a plataformas, votar en DAOs, o autenticarte en servicios que requieren verificación de propiedad.

Gestión de Aprobaciones

Uno de los aspectos más importantes y delicados es el sistema de aprobaciones de tokens. Para que una dApp como Uniswap pueda mover tus tokens ERC-20 (por ejemplo, USDC o DAI), primero debes aprobar explícitamente que el contrato inteligente de esa dApp tenga permiso para hacerlo. Tu wallet gestiona estas aprobaciones mostrándote exactamente qué contrato quiere acceder a cuáles tokens y en qué cantidad.

Puedes establecer límites específicos (solo 100 USDC) o aprobaciones ilimitadas (práctica común pero riesgosa). Las wallets modernas incluyen herramientas para revisar todas las aprobaciones activas y revocarlas cuando ya no confías en un protocolo o simplemente dejaste de usarlo.

Hub de Ecosistema

Las wallets modernas han integrado acceso directo a múltiples servicios del ecosistema Web3. Desde la misma interfaz de tu wallet puedes intercambiar tokens (swaps), transferir activos entre diferentes blockchains (bridges), explorar y visualizar tus NFTs, participar en staking para generar rendimientos, e incluso acceder a protocolos DeFi complejos con interfaces simplificadas.

Esta integración reduce la fricción: no necesitas visitar múltiples sitios web o gestionar diferentes interfaces. Tu wallet se convierte en tu panel de control personal para todas tus actividades on-chain.

Ejemplos de wallets modernas:

MetaMask es la wallet más utilizada, disponible como extensión de navegador y aplicación móvil. Es el estándar de facto para Ethereum y chains compatibles con EVM. Rainbow destaca por su diseño intuitivo y excelente gestión de NFTs, ideal para nuevos usuarios. Rabby está optimizada para usuarios que operan en múltiples chains simultáneamente, mostrando claramente en qué red estás operando. Coinbase Wallet se integra perfectamente con el exchange Coinbase. Phantom, aunque originalmente diseñada para Solana, ahora soporta múltiples blockchains.

## Tipos de Clientes

### Full Node (Cliente Completo)

Nodo completo que descarga toda la blockchain de forma local.

- Descargas un cliente oficial y creas una cuenta con private key
- Sincronizas toda la blockchain (actualmente ~500 GB para Bitcoin)
- Las private keys están bajo tu control total
- Mayor seguridad y autonomía
- Requiere espacio en disco considerable y tiempo de sincronización

### Web Client

Cliente que opera completamente en remoto a través de un servicio web.

- Las private keys se almacenan en servidores de terceros
- Ejemplos: BitGo, Blockchain.com
- Ventajas: portabilidad, compatibilidad, fácil acceso desde cualquier dispositivo
- Desventajas: expuestas a ataques, dependencia del proveedor, menor control

### Lightweight Client

Cliente ligero que no almacena la blockchain completa pero mantiene las private keys localmente.

- Usa SPV (Simple Payment Verification) para validar transacciones
- Descarga solo las cabeceras de los bloques
- Ejemplo: Electrum para PC
- Balance entre seguridad y recursos necesarios

### Mobile Client

Wallet diseñada para smartphones que puede funcionar como full client, web client o lightweight client.

- Ventaja principal: accesibilidad desde dispositivos móviles
- Generalmente operan como lightweight clients por limitaciones de almacenamiento
- Descargan solo los bloques más recientes
- Ejemplos: Mycelium, Copay, Trust Wallet

Más información: [Carteras móviles Bitcoin](https://academy.bit2me.com/carteras-moviles-bitcoins/)

## Tipos de Wallet por Almacenamiento

### Hardware Wallet

Dispositivos físicos especializados en almacenar claves privadas de forma segura.

- Ejemplos: Trezor, Ledger Nano
- Las claves nunca salen del dispositivo
- Protección contra malware
- Ideal para almacenamiento a largo plazo

### Paper Wallet

Documento físico que contiene las claves privadas y públicas impresas.

- Generalmente en formato QR para facilitar el escaneo
- Completamente offline
- Vulnerable a daños físicos y pérdida

Práctica: [Monedero de papel Bitcoin](https://academy.bit2me.com/monedero-papel-bitcoin-paper-wallet/)

### Software Wallet

Aplicaciones para ordenador o smartphone que gestionan las claves.

Para PC:

- Electrum
- Bitcoin Core (monedero oficial Bitcoin)

Para smartphone:

- Electrum
- Mycelium
- Copay

Más información: [Monedero Bitcoin Core](https://academy.bit2me.com/monedero-bitcoin-core/)

### Cloud Wallet

Wallet alojada en servicios en la nube gestionados por terceros.

- Accesible desde cualquier dispositivo con internet
- Las claves están en servidores del proveedor
- Mayor riesgo de seguridad

### Smart Contract Wallet

Wallet cuya lógica está implementada en un smart contract en la blockchain.

A diferencia de las wallets tradicionales (EOA - Externally Owned Accounts) que dependen directamente de claves privadas, estas wallets son contratos inteligentes que permiten funcionalidades avanzadas:

- Recuperación social (social recovery) sin seed phrases
- Límites de gasto programables
- Transacciones por lotes (batch transactions)
- Pago de gas con tokens (no solo ETH)
- Permisos granulares y roles
- Actualizables (upgradeable)
- Gestión automática de aprobaciones
- Sesiones con permisos temporales para dApps

Ejemplos:

- Safe (anteriormente Gnosis Safe): gestión multi-firma para equipos y DAOs
- Argent: recuperación social y staking integrado
- Ambire: enfocada en DeFi con yield optimizado
- ZeroDev: SDK para desarrolladores de wallets AA

Ventajas para interactuar con dApps:

- Aprobaciones batch: aprobar múltiples tokens en una transacción
- Límites automáticos: las dApps no pueden gastar más de lo permitido
- Revocación programada: permisos que expiran automáticamente
- Delegación segura: permitir que apps operen en tu nombre con restricciones

Más información: [ERC-4337 Account Abstraction](https://eips.ethereum.org/EIPS/eip-4337)

## Estrategias de Almacenamiento

### Hot Wallet

Wallet conectada a internet para uso cotidiano.

- Ideal para cantidades pequeñas de uso frecuente
- Mayor conveniencia pero menor seguridad
- Vulnerable a ataques remotos

### Cold Wallet

Wallet mantenida offline para almacenamiento seguro de grandes cantidades.

Tipos de cold storage:

**True Cold Storage:**

- Las claves nunca han estado en un dispositivo conectado a la red
- Requiere dos wallets: una online para crear transacciones sin firmar y otra offline para firmarlas
- Máxima seguridad

**Cold Storage:**

- El dispositivo solo se conecta a la red para firmar transacciones
- Permanece offline el resto del tiempo
- Balance entre seguridad y usabilidad

**Hardware Wallet:**

- Dispositivos como Trezor o Ledger Nano
- Especializados en mantener las claves offline
- Conexión segura cuando se necesita firmar

## Gestión de Claves

### Import vs Sweep

**Import (Importar):**

- Agrega una clave privada existente a tu wallet
- La clave puede ser usada desde múltiples wallets
- Riesgo: si una wallet está comprometida, los fondos están en peligro

**Sweep (Barrer):**

- Transfiere todos los fondos asociados a una clave privada a una nueva dirección
- La clave original queda vacía
- Más seguro cuando recibes una clave de terceros

## Cómo Funcionan las Direcciones Bitcoin

### Proceso de Creación

Una dirección Bitcoin (ejemplo: `16UwLL9Risc3QfPqBUvKofHmBQ7wMtjvM`) se genera siguiendo estos pasos:

1. Generación de clave privada (256 bits aleatorios)

Ejemplo: `18E14A7B6A307F426A94F8114701E7C8E774E7F9A47E2C2035DB29A206321725`

2. Derivación de clave pública usando ECDSA (Elliptic Curve Digital Signature Algorithm)

La clave pública se deriva matemáticamente de la privada, pero no es posible el proceso inverso

3. Hash SHA-256 de la clave pública

4. Hash RIPEMD-160 del resultado anterior

Esto reduce el tamaño y aumenta la seguridad

5. Agregar byte de versión (network byte)

Identifica la red (mainnet, testnet, etc.)

6. Calcular checksum

- Aplicar doble SHA-256 al hash extendido
- Tomar los primeros 4 bytes como checksum

7. Concatenar hash extendido + checksum

8. Codificar en Base58Check

Formato final legible que evita caracteres confusos (0, O, I, l)

Más información: [Cómo se crea una dirección Bitcoin](https://www.oroyfinanzas.com/2014/01/como-crea-direccion-clave-publica-bitcoin/)

### Validación de Propiedad

Cuando realizas una transacción, demuestras la propiedad mediante firma digital:

1. Creas una firma usando tu clave privada
2. Envías la transacción con: firma + clave pública
3. La red valida que:

- La firma fue creada por el propietario de la clave privada
- La clave pública corresponde a la dirección origen
- Solo el propietario de la clave privada puede generar esa firma válida

Este proceso prueba matemáticamente la propiedad sin revelar la clave privada.

## Características Avanzadas

### Seed Phrase (Frase Semilla)

Secuencia de 12 o 24 palabras que permite recuperar todas las claves de una wallet.

- Generada al crear una wallet HD (Hierarchical Deterministic)
- Permite respaldo y recuperación completa
- Debe guardarse de forma segura y offline
- Si alguien obtiene tu seed, tiene acceso total a tus fondos

### HD Wallets (Hierarchical Deterministic)

Wallets que generan múltiples direcciones a partir de una única seed.

- Estándar BIP32/BIP44
- Genera direcciones determinísticamente
- Master Public Key (MPK) permite generar direcciones de solo lectura
- Útil para auditorías sin exponer capacidad de firma

Más información: [Deterministic Wallet](https://en.bitcoin.it/wiki/Deterministic_wallet)

### Direcciones Multifirma (Multisig)

Requieren múltiples claves privadas para autorizar una transacción.

Configuraciones comunes:

- 2-de-3: necesitas 2 firmas de 3 claves posibles
- 1-de-2: cualquiera de 2 claves puede firmar
- 3-de-5: necesitas 3 firmas de 5 claves posibles

Casos de uso:

- Seguridad distribuida (keys en diferentes dispositivos)
- Control corporativo compartido
- Protección contra pérdida de una clave

El primer carácter de la dirección indica el tipo (multisig suele empezar con '3').

Recursos:

- [Direcciones multifirma](https://academy.bit2me.com/direcciones-bitcoin-multifirma/)
- [Multisig en Electrum](https://electrum.readthedocs.io/en/latest/multisig.html)
- [Multisig técnico](https://www.soroushjp.com/2014/12/20/bitcoin-multisig-the-hard-way-understanding-raw-multisignature-bitcoin-transactions/)

## Account Abstraction (AA)

Account Abstraction es un concepto que permite que las cuentas de usuario funcionen como smart contracts en lugar de depender exclusivamente de claves privadas (EOA).

### EOA vs Smart Contract Accounts

**EOA (Externally Owned Account):**

- Controlada por una clave privada única
- Si pierdes la clave privada, pierdes acceso permanente
- Solo puede iniciar transacciones
- Lógica de firma fija (ECDSA)
- Debe pagar gas en ETH

**Smart Contract Account:**

- Controlada por código programable
- Lógica de autorización flexible
- Puede ser actualizada
- Permite recuperación y múltiples métodos de autenticación
- Puede abstraer el pago de gas

### Ventajas de Account Abstraction

**Seguridad Mejorada:**

- Recuperación social: designa guardianes para recuperar acceso
- Límites de transacción diarios
- Autenticación multi-factor
- Sesiones con permisos limitados

**Mejor Experiencia de Usuario:**

- Transacciones patrocinadas (paymaster paga el gas)
- Pago de gas con cualquier token
- Transacciones por lote en una sola operación
- Actualizaciones de lógica sin cambiar dirección

**Flexibilidad:**

- Lógica de firma customizable
- Soporte para diferentes algoritmos criptográficos
- Integración con hardware biométrico
- Automatización de operaciones

### ERC-4337

Estándar que implementa Account Abstraction sin cambios en el protocolo de Ethereum.

Componentes principales:

- UserOperation: transacción de usuario empaquetada
- Bundler: nodo que agrupa UserOperations
- EntryPoint: contrato único que procesa operaciones
- Paymaster: contrato opcional que patrocina gas
- Wallet Contract: el smart contract de la wallet

Flujo de transacción:

1. Usuario crea UserOperation
2. Bundler recopila múltiples UserOperations
3. Bundler envía lote al EntryPoint
4. EntryPoint valida y ejecuta cada operación
5. Paymaster (opcional) paga el gas

Más información: [Account Abstraction ERC-4337](https://www.alchemy.com/blog/account-abstraction)

## Interacción con dApps

### Conexión Web3

Las wallets modernas se integran con aplicaciones descentralizadas mediante protocolos estandarizados:

**Extensión de Navegador:**

- Inyecta objeto `window.ethereum` en páginas web
- Las dApps detectan la wallet automáticamente
- Usuario aprueba conexión explícitamente
- Soporte para múltiples redes (mainnet, testnets, L2s)

**WalletConnect:**

- Protocolo para conectar wallets móviles con dApps
- Escaneo de código QR para establecer conexión
- Comunicación cifrada end-to-end
- Soporte multi-chain

### Aprobaciones de Tokens (ERC-20)

Para que una dApp mueva tus tokens ERC-20, necesita tu aprobación:

```solidity
// Ejemplo de aprobación en Ethereum
approve(spenderAddress, amount)
```

Proceso:

1. dApp solicita aprobación para gastar tus tokens
2. Wallet muestra diálogo con detalles: token, cantidad, contrato destino
3. Usuario firma aprobación
4. dApp puede ahora mover hasta la cantidad aprobada

Buenas prácticas:

- Aprobar solo la cantidad necesaria, no "unlimited"
- Revisar aprobaciones activas regularmente
- Usar herramientas como Revoke.cash para auditar permisos
- Revocar aprobaciones de dApps que ya no usas

### Gestión de Permisos

Herramientas para auditar y revocar aprobaciones:

- [Revoke.cash](https://revoke.cash): revocación de aprobaciones en múltiples chains
- [Etherscan Token Approvals](https://etherscan.io/tokenapprovalchecker): verificación en Ethereum
- Configuración nativa en wallets modernas (MetaMask, Rainbow)

Riesgos de aprobaciones:

- Contrato comprometido puede drenar fondos aprobados
- Aprobaciones ilimitadas persisten indefinidamente
- Phishing sites pueden solicitar aprobaciones maliciosas
- Contratos no auditados representan mayor riesgo

### Ecosistema de dApps Integradas

Muchas wallets modernas incluyen acceso directo a:

**DeFi:**

- Swaps descentralizados (Uniswap, 1inch)
- Lending protocols (Aave, Compound)
- Yield farming y staking
- Bridges entre chains

**NFTs:**

- Marketplaces (OpenSea, Blur)
- Galerías personales
- Mint directo de colecciones

**Utilidades:**

- ENS (Ethereum Name Service) para dominios .eth
- Exploradores de blockchain integrados
- Historial de transacciones
- Calculadoras de portfolio

### WIF (Wallet Import Format)

Formato estándar para codificar claves privadas ECDSA.

- Facilita la copia y transferencia entre wallets
- Codificado en Base58Check
- Incluye checksum para detectar errores
- Formato compacto y legible

## Formatos de Direcciones

### Legacy (BASE58)

Formato original de direcciones Bitcoin.

**P2PKH (Pay To Public Key Hash):**

- Empieza con '1'
- Ejemplo: `1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa`

**P2SH (Pay To Script Hash):**

- Empieza con '3'
- Soporta multisig y smart contracts
- Ejemplo: `3J98t1WpEZ73CNmYviecrnyiWrnqRhWNLy`

Más información: [P2PK, P2PKH, P2SH](https://bitcoin.stackexchange.com/questions/64733/what-is-p2pk-p2pkh-p2sh-p2wpkh-eli5)

### SegWit (BECH32)

Formato moderno introducido con Segregated Witness.

**P2WPKH (Pay To Witness Public Key Hash):**

- Versión SegWit de P2PKH
- Empieza con 'bc1q'
- Fees más bajos
- Ejemplo: `bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq`

**P2WSH (Pay To Witness Script Hash):**

- Versión SegWit de P2SH
- Soporta multisig
- Empieza con 'bc1q' (más largo que P2WPKH)

Ventajas de SegWit:

- Comisiones más bajas
- Mayor capacidad de transacciones por bloque
- Direcciones más largas pero más eficientes
- Protección contra maleabilidad de transacciones

Más información: [Bitcoin SegWit vs Legacy](https://blog.mercury.cash/es/2019/06/14/que-es-bitcoin-segwit-y-bitcoin-legacy/)

## Recursos Adicionales

- [Electrum Documentation](https://electrum.readthedocs.io/en/latest/index.html)
- [Base58Check Encoding](https://en.bitcoin.it/wiki/Base58Check_encoding)
- [Bit2Me Academy](https://academy.bit2me.com/)

---
