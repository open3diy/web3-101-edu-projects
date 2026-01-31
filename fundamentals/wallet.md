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

## Modelos de Custodia

### Custodial Wallets (Custodia por Terceros)

Wallets donde una entidad externa controla las claves privadas.

**Características:**

- El proveedor gestiona y almacena las claves
- Usuario accede mediante credenciales (email/password)
- Equivalente a una cuenta bancaria tradicional
- Ejemplos: exchanges (Coinbase, Binance, Kraken)

**Ventajas:**

- Recuperación de cuenta mediante email/2FA
- Sin responsabilidad de gestionar claves privadas
- Interfaz familiar para usuarios nuevos
- Soporte al cliente disponible
- Transacciones internas instantáneas y sin fees

**Desventajas:**

- No controlas tus fondos realmente ("Not your keys, not your coins")
- Riesgo de hackeo del exchange
- Riesgo de quiebra o congelación de fondos
- Requiere KYC/AML (identidad verificada)
- Sujeto a regulación y censura
- Posible pérdida total si el proveedor desaparece

**Casos de Uso:**

- Trading activo en exchanges
- Usuarios nuevos aprendiendo
- Cantidades pequeñas para uso frecuente

### Non-Custodial Wallets (Auto-Custodia)

Wallets donde el usuario controla completamente sus claves privadas.

**Características:**

- Usuario tiene control exclusivo de las claves
- Nadie más puede acceder a los fondos
- Responsabilidad total de seguridad
- Ejemplos: MetaMask, Ledger, Trust Wallet, Electrum

**Ventajas:**

- Control total sobre tus fondos
- Resistente a censura
- Sin riesgo de quiebra de terceros
- Privacidad (no requiere KYC para crear)
- Acceso a DeFi y dApps
- Propiedad verdadera de activos

**Desventajas:**

- Si pierdes seed phrase, pierdes fondos (sin recuperación)
- Usuario responsable de seguridad
- Posible pérdida por errores (dirección incorrecta, phishing)
- Requiere conocimiento técnico básico
- Sin soporte al cliente

**Casos de Uso:**

- Almacenamiento a largo plazo
- Uso de DeFi y dApps
- Valoración de privacidad y soberanía
- Cantidades significativas

### Servicios de Custodia Profesional

**Prosegur Crypto:**

- Custodia institucional de claves privadas
- Bóvedas de seguridad física certificadas
- Seguros contra robo y pérdida
- Multi-firma y controles de gobernanza
- Auditorías regulares
- Dirigido a: instituciones, family offices, grandes patrimonios
- Cumplimiento regulatorio completo

**Otros Custodios Institucionales:**

- Coinbase Custody
- BitGo Trust
- Fireblocks
- Copper

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

### MPC Wallet (Multi-Party Computation)

Wallet que utiliza criptografía avanzada para fragmentar la clave privada en múltiples partes distribuidas entre diferentes participantes, sin que la clave completa exista nunca en un solo lugar.

**¿Qué es Multi-Party Computation?**

MPC es una técnica criptográfica que permite a múltiples partes realizar cálculos colaborativos sobre datos privados sin revelar esos datos entre sí. En el contexto de wallets, esto significa que la clave privada se fragmenta matemáticamente en "shares" (fragmentos) distribuidos entre diferentes dispositivos o servicios, y estos fragmentos colaboran criptográficamente para firmar transacciones sin reconstruir la clave completa.

**Diferencia con Multisig:**

- **Multisig:** Múltiples direcciones independientes con claves completas separadas aprueban transacciones on-chain. Cada firmante tiene una clave privada completa y funcional. La lógica de aprobación está en el smart contract.

- **MPC:** Una única dirección cuya clave privada está fragmentada. Los fragmentos por sí solos son inútiles y no pueden firmar. La firma se genera mediante computación criptográfica distribuida off-chain, resultando en una firma estándar indistinguible de una wallet normal.

**Arquitectura Threshold (t-of-n):**

Los esquemas MPC utilizan umbrales configurables donde necesitas t fragmentos de un total de n para firmar transacciones:

- **2-of-3:** Necesitas 2 de 3 fragmentos. Tolera pérdida de 1 fragmento.
  - Ejemplo: Fragmento en tu teléfono + fragmento en servidor del proveedor + fragmento en laptop. Cualquier combinación de 2 puede firmar.

- **3-of-5:** Necesitas 3 de 5 fragmentos. Mayor seguridad contra colusión, tolera pérdida de 2 fragmentos.
  - Ejemplo: Dispositivo móvil + laptop + tablet + servidor proveedor + dispositivo de familiar. Cualquier combinación de 3 puede firmar.

- **5-of-7:** Común en organizaciones que requieren consenso amplio.
  - Ejemplo: Tesorería corporativa donde 5 de 7 ejecutivos deben aprobar transacciones grandes.

La elección del umbral balancea:

- **Seguridad contra ataques:** Umbrales altos dificultan colusión maliciosa (necesitas comprometer más fragmentos).
- **Resiliencia contra pérdida:** Umbrales bajos permiten recuperación incluso si pierdes varios dispositivos.
- **Conveniencia operacional:** Umbrales muy altos pueden bloquear operaciones si múltiples participantes no están disponibles.

**Proceso de Firma MPC:**

1. **Generación Distribuida de Clave (DKG):**
   - Múltiples partes colaboran criptográficamente para generar fragmentos de clave.
   - Ninguna parte conoce la clave privada completa en ningún momento.
   - Se deriva la clave pública correspondiente (visible on-chain como dirección normal).

2. **Firma de Transacción:**
   - Usuario inicia transacción desde su dispositivo.
   - El fragmento local inicia protocolo MPC solicitando colaboración de otros fragmentos.
   - Los fragmentos participantes realizan cálculos criptográficos colaborativos (múltiples rondas de comunicación).
   - Se genera firma ECDSA válida sin reconstruir la clave privada completa.
   - La firma resultante es idéntica a una firma tradicional (indistinguible on-chain).

3. **Verificación:**
   - La blockchain verifica la firma como cualquier transacción normal.
   - Ninguna diferencia visible on-chain con wallets tradicionales (mismas fees, mismo formato).

**Protocolos MPC Principales:**

- **GG20 (Gennaro-Goldfeder 2020):** Protocolo threshold ECDSA sin trusted dealer. Ampliamente usado, múltiples rondas de comunicación.

- **CGGMP (Canetti-Gennaro-Goldfeder-Makriyannis-Peled):** Evolución de GG20, más eficiente y resistente a ataques de identificación.

- **Lindell17:** Esquema 2-of-2 optimizado, usado en implementaciones donde solo hay dos partes (usuario + servidor).

- **TSS (Threshold Signature Scheme):** Término genérico para esquemas threshold que incluyen ECDSA-TSS y EdDSA-TSS.

**Implementaciones y Proveedores:**

- **Fireblocks:** MPC institucional para exchanges, fondos, custodios. Fragmentos en múltiples HSMs geográficamente distribuidos.

- **Coinbase Wallet (MPC feature):** 2-of-2 con fragmento en dispositivo del usuario y fragmento en servidores Coinbase cifrados con contraseña del usuario.

- **ZenGo:** Wallet mobile sin seed phrase. 2-of-2 con fragmento en teléfono (cifrado con biometría) y fragmento en servidores ZenGo.

- **Web3Auth:** Infraestructura MPC para desarrolladores. Fragmentos distribuidos entre dispositivo usuario, servidor Web3Auth, y método de recuperación elegido.

- **Torus (ahora Web3Auth):** Social login con MPC. Fragmentos ligados a OAuth providers (Google, Facebook) sin custodio central.

- **Sepior:** Solución empresarial con cumplimiento FIPS 140-2. Usada por instituciones reguladas.

- **Qredo:** Network descentralizada de MPC validators que custodian fragmentos, con consensus bizantino.

**Ventajas:**

- **Eliminación de seed phrases:** No existe frase semilla que memorizar o almacenar físicamente. Esto elimina el mayor punto de falla de seguridad para usuarios promedio.

- **Recuperación sin single point of failure:** Si pierdes un dispositivo, recuperas acceso con los fragmentos restantes sin necesidad de reconstruir una clave completa.

- **Seguridad distribuida:** Atacante necesita comprometer múltiples fragmentos simultáneamente (según umbral). Un solo fragmento robado es matemáticamente inútil.

- **Firmas indistinguibles:** On-chain, transacciones MPC son idénticas a transacciones normales. Mismos fees, mismo formato, sin smart contracts adicionales.

- **Flexibilidad de configuración:** Puedes cambiar umbrales, añadir/remover fragmentos, implementar políticas complejas (fragmentos con diferentes pesos de voto).

- **Compatible con hardware existente:** No requiere hardware especializado como Ledger. Funciona en smartphones, servidores, HSMs estándar.

**Desventajas:**

- **Complejidad criptográfica:** Implementaciones incorrectas pueden ser catastróficamente inseguras. Requiere auditorías exhaustivas.

- **Latencia de firma:** Múltiples rondas de comunicación entre fragmentos aumentan tiempo de firma (1-3 segundos vs instantáneo en wallets locales).

- **Dependencias de red:** Necesitas conectividad entre fragmentos para firmar. Si los servidores del proveedor caen, no puedes firmar.

- **Confianza distribuida:** Aunque mejor que custodia central, sigues dependiendo de que proveedores de fragmentos no colusionen maliciosamente.

- **Recuperación compleja:** Si pierdes fragmentos por debajo del umbral, recuperación puede requerir procesos complejos (social recovery, backup encriptado, etc.).

- **Costo computacional:** Generación de firmas MPC consume más CPU que firmas tradicionales, aunque la diferencia es imperceptible para usuarios.

**Casos de Uso Principales:**

- **Wallets consumer sin seed phrases:** Onboarding masivo de usuarios Web2 que no pueden gestionar claves privadas de forma segura.

- **Custodia institucional:** Fondos de inversión, exchanges, tesorerías corporativas que requieren controles multifirma sin smart contracts.

- **Infraestructura cripto de empresas:** Pagos automatizados, gestión de liquidez, operaciones DeFi de gran volumen donde seguridad es crítica.

- **Social recovery avanzado:** Fragmentos distribuidos entre familiares y dispositivos del usuario, permitiendo recuperación colaborativa.

- **Carteras de alta seguridad para individuos:** Patrimonios significativos donde el riesgo de perder seed phrase o robo de hardware wallet es inaceptable.

**Consideraciones de Seguridad:**

- **Auditorías del protocolo MPC:** Verifica que el proveedor use protocolos auditados (GG20, CGGMP) y que la implementación haya sido revisada por criptógrafos independientes.

- **Distribución geográfica:** Fragmentos deben estar en jurisdicciones y infraestructuras diferentes para evitar puntos únicos de falla.

- **Cifrado de fragmentos en reposo:** Cada fragmento debe estar cifrado con claves derivadas de credenciales del usuario, no solo del proveedor.

- **Resistencia a ataques de canal lateral:** Implementaciones deben proteger contra timing attacks, side-channel attacks durante computación MPC.

- **Plan de recuperación documentado:** Debe existir procedimiento claro para recuperar acceso si pierdes fragmentos, sin centralización excesiva.

**Comparación con Alternativas:**

| Característica | EOA tradicional | Multisig | Smart Contract Wallet | MPC Wallet |
|----------------|-----------------|----------|----------------------|------------|
| Seed phrase requerida | Sí | Sí (por firmante) | Sí (inicialmente) | No |
| Single point of failure | Sí | No | Depende | No |
| Costo on-chain adicional | No | Sí (gas por firmante) | Sí (gas del contrato) | No |
| Indistinguible on-chain | N/A | No (múltiples firmas) | No (contrato visible) | Sí |
| Cambio de protocolo Ethereum | No | No | No | No |
| Recuperación social | No | Difícil | Sí (programable) | Sí (threshold) |
| Adopción institucional | Baja | Media | Media | Alta |

**Recursos Adicionales:**

- [Threshold Signatures Explained](https://www.fireblocks.com/what-is-mpc/) por Fireblocks
- [MPC vs Multisig](https://www.zengo.com/mpc-vs-multisig/) por ZenGo
- [GG20 Protocol Paper](https://eprint.iacr.org/2020/540.pdf) - Academic paper del protocolo
- [CGGMP Paper](https://eprint.iacr.org/2021/060.pdf) - Protocolo mejorado
- [Practical Threshold Signatures](https://eprint.iacr.org/2019/114.pdf) - Survey académico

## Seguridad en Wallets Móviles

Las wallets móviles modernas implementan capas de seguridad avanzadas que protegen tus claves privadas sin sacrificar la conveniencia de uso diario. Entender estas tecnologías te ayuda a elegir wallets que equilibren seguridad y experiencia de usuario.

### TEE (Trusted Execution Environment)

Los Trusted Execution Environments crean una "bóveda blindada" dentro del procesador de tu smartphone mediante hardware especializado que aísla operaciones criptográficas críticas del sistema operativo principal. Esto significa que incluso si tu teléfono está comprometido con malware, las claves privadas permanecen inaccesibles.

**¿Cómo Funciona un TEE?**

Tu smartphone contiene esencialmente dos sistemas operativos funcionando simultáneamente:

El sistema operativo principal (Android o iOS) donde corren tus aplicaciones normales, accesible por software y potencialmente vulnerable a malware. Este sistema puede ser hackeado, puede tener bugs de seguridad, y las aplicaciones maliciosas pueden intentar leer memoria de otras aplicaciones.

El TEE es un sistema operativo aislado que corre en una partición segura del procesador, completamente separado. Solo operaciones específicas pueden ejecutarse aquí: generación de claves criptográficas, firma de transacciones, autenticación biométrica. Este entorno está protegido por hardware: incluso si obtienes acceso root al sistema operativo principal, no puedes leer o modificar lo que sucede dentro del TEE.

Cuando tu wallet móvil necesita firmar una transacción, en lugar de realizar la operación criptográfica en el sistema operativo normal (donde podría ser interceptada), la wallet envía la transacción al TEE. Dentro de esta bóveda segura, la clave privada nunca sale del enclave protegido. El TEE firma la transacción internamente y devuelve únicamente la firma resultante, manteniendo la clave privada completamente oculta.

**Implementaciones Específicas**:

**Secure Enclave de Apple (iPhone, iPad, Mac)**:

Presente en todos los dispositivos Apple desde el iPhone 5S en adelante, el Secure Enclave es un coprocesador dedicado separado físicamente del CPU principal. Tiene su propia memoria cifrada y sistema operativo microkernel. Cuando creas una wallet en un iPhone, la clave privada se genera directamente dentro del Secure Enclave usando su generador de números aleatorios certificado (True Random Number Generator basado en ruido térmico del hardware).

La clave privada nunca sale del Secure Enclave, ni siquiera el sistema operativo iOS puede accederla. Cuando necesitas firmar una transacción, la wallet envía los datos a firmar al Secure Enclave mediante una API controlada. El Secure Enclave verifica tu identidad mediante Touch ID o Face ID (los datos biométricos también están almacenados únicamente dentro del Secure Enclave), y solo entonces realiza la firma criptográfica, devolviendo el resultado firmado sin exponer la clave.

Este diseño significa que incluso si un atacante obtiene acceso completo a tu iPhone mediante jailbreak o exploit del sistema operativo, no puede extraer la clave privada del Secure Enclave. La única forma de comprometer la clave requeriría acceso físico al dispositivo, desoldadura del chip, y ataques de canal lateral extremadamente sofisticados que cuestan millones de dólares (nivel de agencias de inteligencia).

**ARM TrustZone (Android)**:

La mayoría de smartphones Android modernos implementan seguridad mediante ARM TrustZone, una extensión de hardware presente en procesadores ARM Cortex-A desde 2004 pero popularizada masivamente en la última década. TrustZone crea dos "mundos" virtuales en el mismo chip:

El mundo normal (Normal World) donde corre Android y todas tus aplicaciones. El mundo seguro (Secure World) donde corre un sistema operativo minimalista llamado Trusted OS que gestiona operaciones criptográficas, autenticación biométrica, y almacenamiento seguro.

El procesador puede cambiar entre estos mundos mediante instrucciones especiales, pero el código corriendo en Normal World no puede acceder a memoria o recursos del Secure World. Cuando una wallet Android utiliza TrustZone, genera y almacena la clave privada en el Secure World. Firmar transacciones requiere transición al Secure World mediante APIs del sistema operativo (Android KeyStore), autenticación biométrica o PIN, y ejecución de la operación criptográfica aislada.

La efectividad de TrustZone depende críticamente de la implementación del fabricante del dispositivo. Dispositivos premium de Samsung (Knox), Google (Titan M en Pixels), y otros fabricantes de gama alta implementan TrustZone robustamente con chips de seguridad dedicados adicionales. Dispositivos Android de gama baja pueden tener implementaciones más débiles o directamente no utilizar TrustZone adecuadamente, reduciendo la seguridad significativamente.

**TEE en Hardware Wallets**:

Aunque hardware wallets como Ledger se comercializan como dispositivos seguros, históricamente no todos usaban TEE. Trezor, por ejemplo, usa microcontroladores de propósito general sin TEE, dependiendo de firmware y diseño físico para seguridad. Ledger sí implementa Secure Element (equivalente a TEE en hardware dedicado), almacenando claves privadas en chips certificados Common Criteria EAL5+.

**Limitaciones y Ataques Conocidos**:

Ninguna tecnología es invulnerable. Intel SGX, una implementación TEE anteriormente popular en computadoras, sufrió múltiples vulnerabilidades críticas:

[Spectre](https://spectreattack.com/) y [Meltdown](https://meltdownattack.com/) demostraron que bugs en ejecución especulativa de CPUs modernas permiten leer memoria de procesos aislados, incluyendo TEEs. Ataques posteriores como [Foreshadow](https://foreshadowattack.eu/) comprometieron específicamente SGX. Intel discontinuó SGX en procesadores consumer en 2021, reconociendo que las mitigaciones degradaban rendimiento inaceptablemente.

ARM TrustZone ha sufrido vulnerabilidades donde bugs en implementaciones de fabricantes permitieron escalada de privilegios desde Normal World a Secure World. Secure Enclave de Apple ha sido más resistente, pero en 2019 el exploit checkm8 demostró vulnerabilidad en chips A5-A11, permitiendo jailbreak permanente. Apple mitigó esto en chips A12 y posteriores.

Ataques de canal lateral (side-channel attacks) pueden comprometer TEEs midiendo consumo de energía, emisiones electromagnéticas, o timing de operaciones criptográficas. Estos ataques requieren acceso físico y equipamiento especializado, pero son teóricamente viables.

La lección crítica: TEE es una capa de seguridad poderosa pero no mágica. Reduce dramáticamente la superficie de ataque, pero debe combinarse con otras prácticas de seguridad (actualizaciones de firmware, autenticación fuerte, detección de anomalías).

**Ventajas de TEE en Wallets**:

- Claves privadas nunca expuestas al sistema operativo potencialmente comprometido
- Protección contra malware, keyloggers, y screenreaders
- Firma de transacciones sin revelar material criptográfico
- Integración con autenticación biométrica segura
- Sin necesidad de hardware adicional (hardware wallet)

**Desventajas y Consideraciones**:

- Dependes de la seguridad del hardware del fabricante
- Vulnerabilidades en implementación del TEE comprometen todo
- Actualizaciones de firmware críticas para parchear bugs
- Dispositivos antiguos pueden tener TEEs vulnerables conocidas
- Pérdida del dispositivo = pérdida potencial de acceso (requiere backup)

### Autenticación Biométrica

La autenticación biométrica transforma la experiencia de uso de wallets móviles, reemplazando contraseñas memorables por reconocimiento facial o huella digital. Sin embargo, la implementación técnica determina si esta conveniencia compromete seguridad o la fortalece.

**Biometría Almacenada en TEE**:

Las implementaciones seguras de autenticación biométrica nunca almacenan tu huella digital o mapa facial como imagen o datos reconocibles. En lugar de eso, capturan tu biometría, la procesan mediante algoritmos que generan una representación matemática única (template biométrico), y almacenan este template exclusivamente dentro del TEE.

Cuando desbloqueas tu wallet con Face ID en un iPhone, el proceso funciona así:

La cámara TrueDepth captura un mapa de profundidad de tu rostro usando luz infraestructura estructurada. Estos datos crudos se envían directamente al Secure Enclave (nunca al sistema operativo). Dentro del Secure Enclave, algoritmos de machine learning locales comparan el mapa capturado con el template biométrico almacenado internamente. Si la similitud supera un umbral estadístico, el Secure Enclave autoriza la operación solicitada (desbloquear wallet, firmar transacción). Los datos biométricos capturados y el template almacenado nunca salen del Secure Enclave, ni siquiera Apple puede accederlos.

Esta arquitectura significa que incluso si un atacante extrae una copia completa del almacenamiento del iPhone, obtiene únicamente el template biométrico cifrado, matemáticamente inútil sin la clave de descifrado que vive exclusivamente dentro del Secure Enclave y no puede extraerse sin destruir el chip.

**Touch ID y Fingerprint Sensors**:

Los sensores de huella digital modernos funcionan de manera similar. El sensor captura la imagen de tu huella (ya sea óptico, capacitivo, o ultrasónico), la convierte en un template mediante extracción de minucias (puntos característicos únicos de tu huella), y almacena este template en el TEE. Comparaciones posteriores suceden completamente dentro del entorno seguro.

Dispositivos Android de gama alta (Samsung Galaxy con Knox, Google Pixel con Titan M) implementan esta arquitectura correctamente. Dispositivos de gama baja pueden almacenar templates en almacenamiento normal cifrado, reduciendo significativamente la seguridad porque malware con privilegios elevados podría potencialmente extraer y descifrar los templates.

**Passkeys y WebAuthn**:

La evolución más reciente de autenticación biométrica son los passkeys, estandarizados bajo la especificación [WebAuthn](https://webauthn.io/). En lugar de usar biometría para desbloquear una clave privada que luego firma transacciones, passkeys generan un par de claves criptográficas único para cada servicio.

Cuando creas una wallet usando passkeys, tu dispositivo genera un keypair dentro del TEE. La clave privada nunca sale del TEE y está protegida por autenticación biométrica. La clave pública se registra con la wallet o servicio Web3. Cuando necesitas firmar una transacción, el servicio envía un desafío criptográfico. Tu dispositivo presenta la solicitud de firma, solicita autenticación biométrica (Face ID/Touch ID), y si se aprueba, el TEE firma el desafío con la clave privada almacenada internamente, devolviendo la firma.

Lo poderoso de passkeys es que son phishing-resistant: cada clave privada está vinculada criptográficamente al dominio específico donde se creó. Si un sitio de phishing intenta hacerte firmar algo, tu dispositivo detecta que el dominio no coincide y rechaza la operación, incluso si el sitio falso se ve idéntico al legítimo.

Servicios como [Turnkey](https://www.turnkey.com/), [Dynamic](https://www.dynamic.xyz/), y [Privy](https://www.privy.io/) permiten crear wallets Ethereum controladas por passkeys. Tu iPhone o dispositivo Android actúa como tu hardware wallet, eliminando necesidad de Ledger o Trezor para la mayoría de usuarios.

**Riesgos y Limitaciones Biométricas**:

La biometría no es perfecta. Face ID tiene una tasa de falso positivo de aproximadamente 1 en 1,000,000 (menos seguro que un PIN de 6 dígitos bien elegido, pero mucho más conveniente). Touch ID tiene tasa de 1 en 50,000. Gemelos idénticos y familiares cercanos pueden ocasionalmente engañar sistemas biométricos.

Más preocupante es la coerción: alguien puede forzarte físicamente a desbloquear tu dispositivo con tu rostro o dedo. Los PINs pueden olvidarse convincentemente, las biometrías no. iPhone ofrece mitigación mediante el atajo de bloqueo de emergencia (presionar simultáneamente botón lateral + volumen), que desactiva Face ID temporalmente requiriendo contraseña, útil si anticipas coerción.

Finalmente, biometría no es recuperable: si un servicio pierde tu template biométrico o este se compromete, no puedes cambiarlo como una contraseña. Por eso es crítico que templates vivan únicamente en TEEs locales, nunca se transmitan a servidores, y se protejan con cifrado de hardware.

### Autenticación Multifactorial (2FA/MFA)

La autenticación multifactorial añade capas defensivas requiriendo múltiples pruebas de identidad antes de autorizar operaciones sensibles en tu wallet. Diferentes factores proporcionan diferentes niveles de seguridad.

**Factores de Autenticación**:

**Algo que sabes**: Contraseña, PIN, seed phrase, passphrase. Vulnerable a phishing, keyloggers, y olvido.

**Algo que tienes**: Smartphone, hardware wallet, token físico, app autenticadora (Google Authenticator, Authy). Vulnerable a robo o pérdida del dispositivo.

**Algo que eres**: Huella digital, reconocimiento facial, patrones de voz, comportamiento de tipeo. Vulnerable a suplantación sofisticada y coerción física.

Seguridad robusta combina múltiples factores: comprometer uno no es suficiente para el atacante.

**Implementaciones en Wallets**:

**Custodial Wallets (Exchanges)**:

Exchanges como Coinbase, Binance y Kraken implementan 2FA tradicionalmente mediante:

Time-based One-Time Passwords (TOTP) generados por apps como Google Authenticator. Abres la app, obtienes un código de 6 dígitos que expira en 30 segundos, ingresas el código al iniciar sesión. El código se genera localmente mediante un secreto compartido durante setup inicial y timestamp sincronizado. Incluso si un atacante roba tu contraseña, no puede acceder sin el código TOTP de tu dispositivo físico.

SMS-based 2FA envía código a tu teléfono vía mensaje de texto. Más conveniente pero significativamente menos seguro: ataques de SIM swapping permiten a atacantes convencer a operadores telefónicos de transferir tu número a su tarjeta SIM, interceptando tus códigos 2FA. Múltiples casos documentados de robo de criptomonedas mediante SIM swapping hacen que SMS-based 2FA sea desaconsejable para cantidades significativas.

Hardware keys como YubiKey, Titan Security Key, o Ledger funcionando como segundo factor mediante estándar FIDO U2P. Insertas la llave física en tu computadora o la acercas a tu smartphone, presionas un botón, y la llave firma criptográficamente la solicitud de autenticación. Phishing-resistant porque la llave verifica el dominio del sitio antes de firmar.

**Non-Custodial Wallets Modernas**:

Smart Contract Wallets con Account Abstraction pueden implementar 2FA programáticamente:

Requieres aprobación desde dos dispositivos para transacciones sobre cierto monto. Tu smartphone genera la transacción, pero antes de ejecutarse on-chain, debes aprobarla también desde tu laptop o tablet. Esto protege contra compromiso de un solo dispositivo: un atacante que robe tu teléfono no puede drenar fondos sin acceder también a tu laptop.

Wallets como [Argent](https://www.argent.xyz/) implementan guardianes como segundo factor: transacciones sobre umbrales configurables requieren aprobación de uno o más guardianes (familiares, otros dispositivos tuyos, servicios especializados). Si alguien compromete tu dispositivo principal, los guardianes reciben notificación de transacciones sospechosas y pueden bloquearlas.

[Safe](https://safe.global/) (anteriormente Gnosis Safe) permite multisig on-chain como forma de MFA: configuras tu wallet para requerir 2-de-3 firmas para transacciones grandes. Las tres claves viven en dispositivos separados (smartphone, laptop, hardware wallet). Incluso si un atacante compromete tu smartphone, no puede mover fondos sin acceder también a otro dispositivo.

**MFA en Wallets MPC**:

Wallets MPC como ZenGo implementan inherentemente autenticación multifactorial mediante su arquitectura de fragmentos distribuidos. Un fragmento vive en tu dispositivo móvil protegido por biometría (algo que tienes + algo que eres), otro fragmento en servidores del proveedor. Firmar transacciones requiere colaboración criptográfica de ambos fragmentos, proporcionando efectivamente 2FA automático sin fricción adicional para el usuario.

Si alguien roba tu teléfono, el fragmento local está cifrado con tu biometría (requiere tu rostro o huella). Si alguien hackea los servidores del proveedor, el fragmento remoto es inútil sin el fragmento local. Comprometer ambos simultáneamente requiere ataque coordinado significativamente más sofisticado.

**Consideraciones de Recuperación**:

El mayor desafío de MFA es equilibrar seguridad con recuperación. Si pierdes tu segundo factor (teléfono robado, hardware wallet perdido), ¿cómo recuperas acceso?

Custodial wallets ofrecen procesos de recuperación centralizados: contactas soporte, verificas identidad mediante documentos, y restablecen tus factores de autenticación. Esto introduce riesgo de censura y dependencia en terceros.

Non-custodial wallets con smart contracts pueden implementar recuperación social: si pierdes tus factores de autenticación, múltiples guardianes pueden colaborar para restaurar acceso después de período de espera (48-72 horas), permitiendo cancelación si el propietario legítimo detecta actividad no autorizada.

MPC wallets dependen de que retengas suficientes fragmentos para superar el umbral. Configuraciones 2-de-3 toleran pérdida de un fragmento, pero perder dos significa pérdida permanente de fondos a menos que implementes backup de fragmentos (introduciendo nuevamente el problema de gestionar secretos que intentabas evitar).

**Recomendaciones Prácticas**:

Para holdings significativos (>$10,000): combina múltiples factores:

- Hardware wallet (Ledger, Trezor) como factor primario de firma
- Smartphone con app autenticadora como segundo factor para servicios custodial
- Backup de seed phrase en ubicaciones físicas separadas (casa, caja fuerte bancaria)
- Considera multisig 2-de-3 para montos muy grandes

Para uso diario (<$10,000):

- Wallet móvil moderna con biometría y TEE (Rainbow, MetaMask, Coinbase Wallet)
- Habilita todos los factores de autenticación disponibles
- Mantén backups cifrados de seed phrase
- Usa passkeys cuando estén disponibles para evitar gestionar seed phrases

Para servicios custodial:

- Nunca uses SMS-based 2FA si puedes evitarlo
- Prefiere hardware keys (YubiKey) o TOTP (Google Authenticator)
- Habilita whitelisting de direcciones de retiro
- Configura alertas para todas las transacciones

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

La clave pública se deriva matemáticamente de la privada usando la curva elíptica **secp256k1**.

**¿Por qué secp256k1?**

Bitcoin y Ethereum usan la curva secp256k1 por razones específicas:

- **Eficiencia computacional:** Optimizada para operaciones rápidas
- **Seguridad probada:** 256 bits de seguridad, equivalente a RSA-3072
- **Estructura especial:** Coeficientes elegidos para maximizar velocidad
- **Propiedades matemáticas:** Permite recuperación de clave pública desde firma (feature usado en Ethereum)
- **No-NIST:** Evita curvas potencialmente backdoored por agencias gubernamentales

La derivación es unidireccional: clave privada → clave pública posible, pero no al revés (problema del logaritmo discreto)

3. Hash SHA-256 de la clave pública

4. Hash RIPEMD-160 del resultado anterior

Esto reduce el tamaño y aumenta la seguridad

5. Agregar byte de versión (network byte)

Identifica la red y el tipo de dirección:

- **Mainnet Bitcoin:** Direcciones empiezan con `1` (P2PKH) o `3` (P2SH)
- **Testnet Bitcoin:** Direcciones empiezan con `m`, `n` o `2`
- **Ethereum:** Sin prefijo numérico, formato hexadecimal con `0x`
- **SegWit:** Direcciones empiezan con `bc1q` (mainnet) o `tb1q` (testnet)

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

Secuencia de 12, 18 o 24 palabras que permite recuperar todas las claves de una wallet.

- Generada al crear una wallet HD (Hierarchical Deterministic)
- Permite respaldo y recuperación completa
- Debe guardarse de forma segura y offline
- Si alguien obtiene tu seed, tiene acceso total a tus fondos

#### Generación de Seed Phrase (BIP-39)

El estándar BIP-39 define cómo se genera una seed phrase a partir de entropía:

**1. Generación de Entropía:**

- Se genera entropía aleatoria criptográficamente segura
- Longitudes estándar: 128, 160, 192, 224 o 256 bits
- La entropía determina el número de palabras resultante

**2. Cálculo de Checksum:**

- Se aplica SHA-256 a la entropía
- Se toman los primeros N bits del hash como checksum
- N = longitud de entropía / 32
- Ejemplo: 128 bits de entropía → 4 bits de checksum

**3. Concatenación:**

- Se concatena entropía + checksum
- Ejemplo: 128 bits + 4 bits = 132 bits totales

**4. División en Grupos:**

- Se divide el resultado en grupos de 11 bits
- Cada grupo representa un número de 0 a 2047
- 132 bits / 11 = 12 palabras

**5. Mapeo a Palabras:**

- Cada número se mapea a una palabra de la lista BIP-39
- La lista contiene 2048 palabras en diferentes idiomas
- Palabras diseñadas para ser inequívocas (primeros 4 caracteres únicos)

**Relación Entropía-Palabras:**

- 128 bits → 12 palabras (4 bits checksum)
- 160 bits → 15 palabras (5 bits checksum)
- 192 bits → 18 palabras (6 bits checksum)
- 224 bits → 21 palabras (7 bits checksum)
- 256 bits → 24 palabras (8 bits checksum)

Mayor número de palabras = mayor seguridad, pero 12 palabras ya ofrece seguridad criptográfica robusta (128 bits).

**Passphrase Opcional:**

- BIP-39 permite añadir una passphrase adicional
- Funciona como "palabra 13/25"
- Diferentes passphrases generan wallets completamente diferentes
- Útil para negar plausiblemente (wallets señuelo con passphrase vacía)

### HD Wallets (Hierarchical Deterministic)

Wallets que generan múltiples direcciones a partir de una única seed, organizadas en estructura jerárquica.

#### BIP-32: Derivación Jerárquica

BIP-32 define el proceso de derivación de claves en estructura de árbol:

**Clave Maestra:**

1. La seed phrase se convierte en seed de 512 bits usando PBKDF2-HMAC-SHA512
2. Salt: "mnemonic" + passphrase opcional
3. Iteraciones: 2048
4. Los 512 bits se dividen en:
   - Primeros 256 bits: Clave privada maestra
   - Últimos 256 bits: Chain code maestra

**Derivación de Claves Hijas:**

Para derivar una clave hija desde una clave padre:

1. Se concatena: clave pública padre + índice + chain code padre
2. Se aplica HMAC-SHA512
3. Resultado de 512 bits:
   - Primeros 256 bits: se suman a la clave privada padre (mod n) → clave privada hija
   - Últimos 256 bits: chain code de la clave hija

**Derivación Hardened vs Normal:**

- **Normal (unhardened):** usa clave pública padre
  - Índices: 0 a 2³¹-1
  - Permite derivación de claves públicas sin acceso a claves privadas
  - Útil para generar direcciones de recepción sin exponer capacidad de firma

- **Hardened (reforzada):** usa clave privada padre
  - Índices: 2³¹ a 2³²-1 (notación: número con apóstrofe, ej: 44')
  - Requiere clave privada para derivar
  - Mayor seguridad: compromiso de clave hija no compromete claves hermanas
  - Usada para niveles superiores (propósito, coin type, account)

**Chain Codes:**

- Valor de 256 bits que acompaña a cada clave
- Proporciona 256 bits adicionales de entropía en la derivación
- Previene que compromiso de una clave privada comprometa toda la jerarquía
- Funciona como "sal" criptográfica en el proceso HMAC

#### BIP-44: Estructura de Rutas

BIP-44 define la estructura estándar de derivación:

```
m / purpose' / coin_type' / account' / change / address_index
```

**Componentes:**

1. **m**: Master key (clave maestra)

2. **purpose'**: Propósito (hardened)
   - 44' = BIP-44 (legacy P2PKH)
   - 49' = BIP-49 (SegWit P2SH)
   - 84' = BIP-84 (Native SegWit Bech32)

3. **coin_type'**: Tipo de criptomoneda (hardened)
   - 0' = Bitcoin
   - 1' = Bitcoin Testnet
   - 60' = Ethereum
   - 501' = Solana
   - Lista completa: [SLIP-44](https://github.com/satoshilabs/slips/blob/master/slip-0044.md)

4. **account'**: Número de cuenta (hardened)
   - Permite múltiples identidades separadas
   - 0' = primera cuenta
   - 1' = segunda cuenta, etc.

5. **change**: Cadena externa/interna (normal)
   - 0 = direcciones externas (recibir)
   - 1 = direcciones de cambio (internas)

6. **address_index**: Índice de dirección (normal)
   - 0, 1, 2, 3... generación secuencial de direcciones

**Ejemplos de Rutas:**

- `m/44'/0'/0'/0/0`: Primera dirección Bitcoin (legacy)
- `m/44'/60'/0'/0/0`: Primera dirección Ethereum
- `m/84'/0'/0'/0/5`: Sexta dirección Bitcoin SegWit native
- `m/44'/0'/1'/0/0`: Primera dirección de segunda cuenta Bitcoin
- `m/44'/0'/0'/1/0`: Primera dirección de cambio Bitcoin

#### Ventajas de HD Wallets

**Respaldo Único:**

- Una seed phrase protege infinitas claves
- No necesitas hacer backup de cada dirección nueva
- Recuperación completa desde la seed

**Privacidad:**

- Genera direcciones nuevas para cada transacción
- Dificulta el rastreo de balance total
- Previene análisis de patrones de gasto

**Organización:**

- Estructura jerárquica clara
- Separación por propósito, moneda, cuenta
- Fácil gestión de múltiples identidades

**Master Public Key (xPub):**

- Permite generar direcciones de solo lectura
- Útil para comercios: generar direcciones de pago sin exponer claves privadas
- Auditorías sin riesgo de firma
- No permite acceso a direcciones de cambio hardened

#### Wallets Antiguas vs HD Wallets

Antes de BIP-32 (2012), las wallets generaban claves aleatorias independientes:

**Wallets No-Determinísticas (Antiguas):**

- Cada dirección tiene clave privada generada aleatoriamente
- Requieren backup de cada clave nueva
- Bitcoin Core anterior a v0.13 usaba este modelo
- Pool de claves pre-generadas (keypool)
- Si pierdes wallet.dat, pierdes todas las claves
- Difícil restauración en otra wallet

**HD Wallets (Modernas):**

- Una seed genera todas las claves determinísticamente
- Backup único protege todas las direcciones futuras
- Portabilidad entre diferentes implementaciones
- Estándar desde ~2013
- Todas las wallets modernas son HD

**Migración:**

Bitcoin Core añadió soporte HD en v0.13 (2016), pero mantuvo retrocompatibilidad con wallets antiguas. Electrum fue pionero en implementar HD desde sus inicios.

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

## Wallets Populares

### MetaMask

MetaMask es la wallet más utilizada para Ethereum y chains compatibles con EVM.

**Tipo de Wallet:**

- Wallet HD (implementa BIP-39, BIP-32, BIP-44)
- Non-custodial: usuario controla las claves
- Disponible como extensión de navegador y app móvil
- Usa seed phrase de 12 palabras para recuperación

**Integración Técnica:**

**Web3.js:**

- Inyecta objeto `window.ethereum` en páginas web
- Web3.js es la librería oficial de Ethereum para JavaScript
- Las dApps usan Web3.js para interactuar con MetaMask
- Permite enviar transacciones, firmar mensajes, leer blockchain

**Proveedores de Nodo:**

MetaMask no ejecuta nodos propios, se conecta a proveedores:

- **Infura:** Proveedor principal por defecto
  - Infraestructura de nodos Ethereum as-a-service
  - Propiedad de Consensys (también dueño de MetaMask)
- **Alternativas configurables:**
  - Alchemy
  - QuickNode
  - Nodos propios
  - Las dApps pueden especificar su proveedor preferido

**Características de Seguridad:**

**EIP-1102 (Modo Privado):**

- Protocolo que requiere aprobación explícita para conectar dApps
- Las dApps deben solicitar permiso antes de acceder a direcciones
- Usuario controla qué sitios pueden ver su wallet
- Previene acceso no autorizado automático

**Verificación de Transacciones:**

- Muestra simulación de transacción antes de firmar
- Advierte sobre aprobaciones ilimitadas
- Detecta contratos maliciosos conocidos

**Herramientas y Ecosistema:**

**Chainlist (chainlist.org):**

- Directorio de redes EVM
- Añadir redes custom con un click
- Información RPC, Chain ID, exploradores
- Previene errores de configuración manual

**Ganache:**

- Blockchain local para desarrollo
- Simula Ethereum para testing
- Integración con MetaMask para desarrollo
- Permite probar dApps sin gastar gas real

**Desventajas y Riesgos de MetaMask:**

**Rastreo del Navegador:**

- Al ser extensión de navegador, está expuesta a:
  - Rastreo de actividad por el navegador
  - Chrome especialmente problemático: Google recopila datos de usuarios
  - Historial de navegación vinculado a actividad cripto
- Menor privacidad comparado con wallets standalone

**Vulnerabilidades de Hot Wallet:**

- Siempre conectada a internet
- Superficie de ataque mayor:
  - Malware en el navegador
  - Extensiones maliciosas
  - Phishing sites que imitan dApps legítimas
- Compromiso del navegador = compromiso de la wallet

**Dependencia de Proveedores:**

- Infura/proveedores pueden:
  - Rastrear direcciones IP y actividad
  - Censurar transacciones (han bloqueado regiones geográficas)
  - Sufrir downtime (MetaMask queda inutilizable)
  - Ser hackeados, comprometiendo privacidad
- Single point of failure en la arquitectura

**Recomendaciones de Uso Seguro:**

- No mantener cantidades grandes en MetaMask
- Usar hardware wallet para holdings significativos
- Verificar siempre URLs antes de conectar
- Revisar y revocar aprobaciones regularmente (Revoke.cash)
- Nunca compartir seed phrase
- Usar wallet separada para interacciones arriesgadas (testing, NFTs nuevos)
- Considerar usar Brave o Firefox en lugar de Chrome

### Lightning Network Wallets

Wallets especializadas para pagos instantáneos en Lightning Network (capa 2 de Bitcoin).

**Zap Wallet:**

- Wallet no custodio para Bitcoin y Lightning
- Desktop (Windows, Mac, Linux) y móvil (iOS, Android)
- Control total de claves privadas
- Gestión manual de canales Lightning
- Interfaz amigable para usuarios técnicos
- Open source
- URL: zaphq.io

**Phoenix:**

- Wallet móvil no custodio (iOS, Android)
- Gestión automática de canales
- ACINQ (empresa francesa) maneja infraestructura
- Sin configuración técnica requerida
- Fees por apertura/cierre de canales
- Ideal para usuarios no técnicos

**Breez:**

- Wallet móvil con nodo Lightning integrado
- No custodio
- Podcasts integrados con pagos Lightning
- POS (point of sale) para comercios
- Open source

**Blue Wallet:**

- Wallet móvil Bitcoin y Lightning
- Opción custodio (Lightning) o no custodio (on-chain)
- Interfaz elegante
- Watch-only wallets
- Integración con hardware wallets

**Muun:**

- Wallet híbrida on-chain/Lightning
- No requiere gestión de canales
- Transacciones Lightning sin liquidez previa
- Multi-firma 2-de-2 para seguridad
- Recovery code en papel

**Consideraciones Lightning Wallets:**

- **Liquidez:** Requieren fondos bloqueados en canales
- **Gestión de canales:**
  - Manual: control total, requiere conocimiento técnico
  - Automática: conveniente, fees más altos
- **Fees:**
  - Pagos Lightning: mínimos (satoshis)
  - Apertura/cierre canales: fees on-chain normales
- **Conectividad:** Dispositivo debe estar online para recibir pagos
- **Balance:** Capacidad entrante vs saliente en canales

## Servicios de Exchanges y Utilidades

### Bit2Me

Exchange y ecosistema español de servicios cripto.

**Servicios Principales:**

**Bit2Me Earn:**

- Genera intereses con tus criptomonedas
- Staking de diferentes tokens
- APY variable según activo
- Sin lock-up periods en algunos productos

**Bit2Me Launchpad:**

- Acceso temprano a nuevos proyectos
- Airdrops exclusivos para holders de token B2M
- Modelo similar a Syrup Pools de PancakeSwap
- Oportunidad de obtener tokens antes de listado público

**Bit2Me OTC:**

- Over-The-Counter trading
- Intercambio de grandes volúmenes
- Precios negociados directamente
- Menor slippage para órdenes grandes
- Atención personalizada

**Bit2Me Premium:**

- Soporte dedicado prioritario
- Fees reducidos
- Límites más altos
- Acceso a analistas

**Bit2Me Custody:**

- Custodia profesional de claves
- Seguros y seguridad institucional
- Auditorías regulares
- Para patrimonios significativos

**Bit2Me Commerce:**

- Pasarela de pagos cripto para e-commerce
- Plugins para tiendas online
- Conversión automática a fiat
- Integración con principales CMS

**Bit2Me Loan:**

- Préstamos con garantía cripto
- Mantén tus holdings mientras obtienes liquidez
- Sin venta de activos
- Tasas competitivas

**Bit2Me Pay:**

- Envía cripto usando solo email
- No requiere dirección blockchain
- Destinatario reclama con su email
- Simplifica onboarding de nuevos usuarios

**Token B2M:**

- Token nativo del ecosistema Bit2Me
- Beneficios y descuentos:
  - Fees reducidos en trading
  - Acceso prioritario a Launchpad
  - Mejores tasas en Earn
  - Cashback en servicios
- Staking para recompensas adicionales

### KYC y AML (Anti-Money Laundering)

**Verificación de Origen de Fondos:**

Los exchanges centralizados están obligados por regulación a:

**Límites sin KYC:**

- Típicamente: €1,000 - €10,000 según jurisdicción
- Solo operaciones básicas
- Retiros limitados

**KYC Completo Requerido Para:**

- Depósitos/retiros superiores al límite
- Trading de volúmenes significativos
- Conversión a fiat
- Servicios premium

**Documentación Requerida:**

- Documento de identidad (DNI/Pasaporte)
- Comprobante de domicilio
- Selfie con documento (prueba de vida)
- Fuente de fondos (para cantidades muy altas)

**Análisis de Transacciones:**

- Exchanges monitorean patrones sospechosos:
  - Estructuración (smurfing): dividir transacciones para evitar límites
  - Mezclado de fondos
  - Direcciones asociadas a actividades ilícitas
  - Transacciones desde mixers/tumblers

**Cumplimiento Regulatorio:**

- GAFI (Grupo de Acción Financiera Internacional)
- Directivas europeas (5AMLD, 6AMLD)
- Regulaciones locales (ley de prevención de blanqueo)

**Implicaciones:**

- **Privacidad reducida:** Exchange conoce tu identidad y actividad
- **Posible congelación:** Fondos pueden ser bloqueados durante investigaciones
- **Reportes automáticos:** Transacciones sospechosas reportadas a autoridades
- **Riesgo de censura:** Pueden negar servicio basándose en origen de fondos

**Alternativas:**

- DEX (exchanges descentralizados): sin KYC pero con menor liquidez
- P2P: mayor privacidad pero mayor riesgo de fraude
- Bitcoin ATMs: límites bajos sin KYC

## API JSON-RPC

Interfaz estándar para comunicación entre wallets y nodos blockchain.

**¿Qué es JSON-RPC?**

- Protocolo de llamada a procedimientos remotos
- Usa JSON para serialización de datos
- Generalmente sobre HTTP/HTTPS o WebSocket
- Estándar en Ethereum, Bitcoin y la mayoría de blockchains

**Uso en Wallets:**

Las wallets usan JSON-RPC para:

- Consultar balances: `eth_getBalance`, `getbalance`
- Enviar transacciones: `eth_sendTransaction`, `sendtoaddress`
- Obtener información de bloques: `eth_getBlockByNumber`, `getblock`
- Estimar fees: `eth_estimateGas`, `estimatesmartfee`
- Subscribirse a eventos: `eth_subscribe`

**Ejemplo Llamada Ethereum:**

```json
{
  "jsonrpc": "2.0",
  "method": "eth_getBalance",
  "params": ["0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb", "latest"],
  "id": 1
}
```

**Respuesta:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x7c2562030800"
}
```

**Proveedores JSON-RPC:**

- **Locales:** Nodo propio (Bitcoin Core, Geth, etc.)
- **Remotos:** Infura, Alchemy, QuickNode
- **Públicos:** Menos confiables, rate-limited

**Endpoints:**

- Bitcoin: `http://localhost:8332` (RPC), puerto 8333 (P2P)
- Ethereum: `http://localhost:8545` (HTTP), `ws://localhost:8546` (WebSocket)
- Endpoints remotos varían según proveedor

## Recursos Adicionales

- [Electrum Documentation](https://electrum.readthedocs.io/en/latest/index.html)
- [Base58Check Encoding](https://en.bitcoin.it/wiki/Base58Check_encoding)
- [Bit2Me Academy](https://academy.bit2me.com/)
- [BIP-39 Specification](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki)
- [BIP-32 Specification](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki)
- [BIP-44 Specification](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki)
- [MetaMask Documentation](https://docs.metamask.io/)
- [Ethereum JSON-RPC Specification](https://ethereum.org/en/developers/docs/apis/json-rpc/)

---
