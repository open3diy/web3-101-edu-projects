# Ecosistema de wallets web3

Ante el panorama de wallets que existe en el ecosistema Web3, un desarrollador puede verse superado al intentar comprender todos los mecanismos de validación que el usuario debe completar al interactuar con una DApp. Hay múltiples arquitecturas de claves, modelos de custodia y estándares de transacción en constante evolución. Este documento es una guía de referencia y explicación conceptual sobre cómo funciona la identidad, la custodia y la autenticación, utilizando el ecosistema EVM (Ethereum y redes compatibles) como marco principal para la toma de decisiones arquitectónicas.

Como vimos en el documento de [identidad](../../101/7-1-identity.md), una wallet no es solo un almacén de claves: es también el mecanismo principal de autenticación del usuario en Web3. En ese contexto, las wallets implementan distintos factores de autenticación según su diseño. La forma más básica de crear una wallet es mediante una [SRP (Secret Recovery Phrase)](https://support.metamask.io/start/what-is-a-secret-recovery-phrase-and-how-to-keep-your-crypto-wallet-secure/), una frase de 12 o 24 palabras que deriva de forma determinista todas las claves privadas y sirve como único mecanismo de recuperación. El acceso cotidiano se protege con una contraseña o PIN que descifra localmente la clave almacenada. Algunas wallets como [Privy](https://www.privy.io/) o [MetaMask con Social Login](https://metamask.io/news/introducing-metamask-social-login) permiten usar un login social como método de recuperación de la SRP —no como autenticación directa—. Las [passkeys](https://passkeys.dev/) representan otro factor posible para el acceso cotidiano a la wallet: en lugar de una contraseña o PIN, el usuario se identifica con biometría, que desbloquea localmente la clave sin transmitir ningún secreto. Su adopción varía según la wallet, y es una de las cuestiones que este documento también busca aclarar.

La segunda dimensión relevante es quién custodia las claves privadas, porque quién las controla controla la identidad digital del usuario. Como vimos en identidad, las wallets se clasifican en tres modelos. En una wallet custodial, un tercero —habitualmente un exchange centralizado como [Coinbase](https://www.coinbase.com/) o [Binance](https://www.binance.com/)— guarda las claves en sus propios servidores y el usuario accede con credenciales tradicionales; el control real de la identidad digital recae sobre la plataforma, no sobre el usuario. En una wallet self-custodial el usuario es el único que posee su SRP y, por tanto, sus claves privadas —como ocurre con [MetaMask](https://metamask.io/)—, con la responsabilidad de custodia que eso implica. El modelo non-custodial elimina el único punto de control: mediante técnicas como [MPC (Multi-Party Computation)](https://en.wikipedia.org/wiki/Secure_multi-party_computation) la clave se distribuye entre el usuario y uno o varios proveedores sin que ninguna parte pueda actuar de forma unilateral, o mediante Smart Contract Wallets como [Safe](https://safe.global/), donde la lógica de autorización reside en el propio contrato en cadena y el umbral de firmas necesarias se define en tiempo de despliegue.

La evolución técnica de las wallets ha estado impulsada en gran medida por la presión de la experiencia de usuario. El modelo original de Ethereum son las wallets EOA (Externally Owned Account): una clave privada, una dirección derivada de ella, firma directa de transacciones. Es un modelo simple pero rígido: no admite lógica de autorización compleja, no tiene recuperación nativa y cualquier cambio de firmante implica mover todos los activos a una nueva dirección. El estándar [ERC-4337](https://eips.ethereum.org/EIPS/eip-4337) introdujo [Account Abstraction (AA)](https://eips.ethereum.org/EIPS/eip-4337) sin modificar el protocolo base: en este modelo existe una Smart Contract Wallet (SCW) cuya dirección vive on-chain y cuya lógica es programable, mientras que la EOA pasa a ser el factor de autenticación: firma las `UserOperation` que la SCW valida on-chain, separando así la identidad on-chain de la gestión de claves. Esto abre la puerta a recuperación social, pago de gas en tokens arbitrarios o por terceros (paymasters), firmas en lote y muchas otras capacidades que la EOA simple no puede ofrecer. Sin embargo, el ecosistema arrastra una masa enorme de usuarios con EOAs puras que no pueden migrar directamente a AA sin costes de transición. [EIP-7702](https://eips.ethereum.org/EIPS/eip-7702), incluido en el hard fork Pectra de 2025, resuelve esta tensión permitiendo que una EOA delegue temporalmente su ejecución a la lógica de un contrato inteligente, obteniendo las capacidades de una SCW sin cambiar de dirección y manteniendo compatibilidad total con el ecosistema existente.

Con este contexto, el desarrollador dentro del ecosistema Ethereum tiene que construir una DApp que funcione con cualquier tipo de wallet tal como existe el ecosistema hoy. La regla práctica es clara: como mucho se puede degradar la experiencia —por ejemplo, ofrecer funcionalidades avanzadas de AA solo a usuarios con SCW— pero nunca excluir por completo a quien llega con una EOA tradicional. Ignorar esta heterogeneidad es el origen de buena parte de los problemas de adopción en DApps reales, y entenderla desde el inicio evita rediseños costosos.

Este documento se organiza en dos partes. La primera cubre los escenarios de interacción: los distintos entornos desde los que un usuario puede conectar su wallet a una DApp, desde extensiones de navegador hasta aplicaciones móviles o autenticación mediante passkeys. La segunda aborda la pila de protocolos que permiten la comunicación entre DApp y wallet: el transporte, la autenticación de sesión y las operaciones de firma y ejecución de transacciones. Muchos de estos protocolos dependen de infraestructura en ejecución —como servidores relay o bundlers—, y entender esa distinción es clave para tomar decisiones arquitectónicas informadas.

Finalmente, veremos las bibliotecas que abstraen esta complejidad. Herramientas como [wagmi](https://wagmi.sh/), [viem](https://viem.sh/), [ethers.js](https://docs.ethers.org/) y kits de interfaz como [RainbowKit](https://www.rainbowkit.com/) permiten al desarrollador integrar wallets sin implementar cada protocolo desde cero.

## Conceptos que a menudo se confunden

Antes de entrar en el detalle de cada parte, conviene desambiguar varios términos que el ecosistema usa con frecuencia de forma intercambiable pero que responden a capas distintas del problema.

**Conectar una DApp**:

Es la acción de interfaz que ocurre cuando el usuario hace clic en "Connect Wallet": la wallet muestra un diálogo de permisos y, si el usuario lo aprueba, devuelve su dirección a la DApp. En términos de protocolo, esto es una llamada `eth_requestAccounts` que la DApp envía al proveedor. No es autenticación: la DApp recibe una dirección, pero en ese momento no tiene ninguna prueba criptográfica de que el usuario al otro lado controla esa dirección. Es simplemente un consentimiento de visibilidad.

**Sesión**:

Una sesión es un estado que el servidor mantiene para recordar que un usuario ya demostró que controla una dirección concreta. [SIWE (EIP-4361)](https://eips.ethereum.org/EIPS/eip-4361) es el mecanismo que establece esa sesión: el usuario firma un mensaje estructurado y el servidor verifica la firma off-chain. Una vez establecida, el servidor puede emitir un JWT o cookie de sesión con duración finita. Si la DApp es una SPA sin backend, no existe sesión en este sentido; la EVM verifica cada transacción de forma independiente y no hay estado de autenticación que gestionar.

**Conectividad**:

La conectividad describe el canal físico o lógico a través del cual la DApp puede enviar mensajes a la wallet. [EIP-1193](https://eips.ethereum.org/EIPS/eip-1193) resuelve esta capa cuando la wallet es una extensión del navegador: inyecta `window.ethereum` directamente en el contexto JavaScript de la página. WalletConnect resuelve la misma capa cuando wallet y DApp están en dispositivos distintos: establece un canal cifrado de extremo a extremo, pero lo enruta a través de un servidor relay que actúa como intermediario de transporte — la DApp y la wallet nunca se conectan directamente entre sí. La conectividad precede a cualquier otra interacción: sin canal, no hay posibilidad de enviar una petición de firma.

**Comunicación**:

Sobre el canal de conectividad corre el protocolo de comunicación: los mensajes JSON-RPC que la DApp envía (`eth_requestAccounts`, `eth_signTypedData`, `eth_sendTransaction`…) y las respuestas que la wallet devuelve. Este protocolo es el mismo independientemente del canal subyacente: tanto si la wallet es una extensión local como si está al otro lado de un relay de WalletConnect, los mensajes siguen el mismo formato JSON-RPC. Lo que cambia es cómo se transportan, no qué se transporta.

**Firma de mensaje vs. transacción**:

Firmar un mensaje y enviar una transacción son dos operaciones completamente distintas aunque ambas requieren la clave privada del usuario. Una firma de mensaje —`personal_sign` o `eth_signTypedData`— es una operación off-chain: no cuesta gas, no modifica ningún estado en la blockchain y puede ejecutarse sin conexión a ningún nodo RPC. SIWE funciona completamente sobre firmas de mensaje. Una transacción —`eth_sendTransaction`— sí va on-chain, consume gas, propaga cambios de estado y requiere que alguien la incluya en un bloque. Confundir ambas lleva a errores como pensar que SIWE "cuesta gas" o que verificar una firma requiere hacer una llamada a la blockchain.

**Autenticación vs. autorización**:

La autenticación responde a "¿quién eres?": la DApp verifica que el usuario controla la dirección que declara, mediante una firma de mensaje. La autorización responde a "¿qué puedes hacer?": un contrato inteligente verifica si esa dirección tiene permiso para transferir tokens, llamar a una función protegida o actuar como administrador. El mecanismo de autorización más conocido on-chain es el patrón `approve` de ERC-20, que concede a un contrato tercero permiso para gastar tokens en nombre del owner. Son capas independientes: un usuario puede estar autenticado ante el servidor pero no tener autorización para ejecutar cierta operación on-chain, y viceversa.

**Descubrimiento de wallet vs. conectividad**:

Antes de establecer el canal, la DApp debe saber qué wallets están disponibles en el entorno del usuario. Durante años, esto se resolvió de forma implícita: la primera extensión que se instalaba sobreescribía `window.ethereum` y era la única wallet visible. [EIP-6963](https://eips.ethereum.org/EIPS/eip-6963) introduce un mecanismo de descubrimiento basado en eventos del DOM que permite que múltiples wallets coexistan y se anuncien simultáneamente sin pisarse entre sí. El descubrimiento ocurre antes de la conectividad: primero la DApp sabe qué wallets hay disponibles y luego el usuario elige una y se establece el canal. Mezclar estos dos momentos es lo que genera la clásica confusión de "si el usuario tiene MetaMask y Rabby instalados, ¿cuál aparece?".

**Aprobación on-chain vs. conexión a la DApp**:

Cuando el usuario "conecta" su wallet a una DApp, no está concediendo ningún permiso on-chain: solo está permitiendo que la DApp lea su dirección. La aprobación on-chain es un acto separado y explícito —como un `approve` de ERC-20— que queda registrado en el contrato y persiste indefinidamente hasta que el usuario la revoque, con independencia de si la wallet está "conectada" a esa DApp o no. Esta distinción es crítica desde el punto de vista de seguridad: revocar la conexión desde la interfaz de la wallet no revoca las aprobaciones on-chain previas. Para eso existen herramientas específicas como [Revoke.cash](https://revoke.cash/).

## Escenarios de interacción

Un usuario puede llegar a una DApp desde contextos muy distintos: un navegador de escritorio con una extensión instalada, un móvil sin extensiones, una aplicación que gestiona la wallet internamente, o un dispositivo hardware dedicado. Cada escenario impone restricciones diferentes sobre el canal de conectividad disponible y, por tanto, sobre los protocolos que el desarrollador puede usar.

### Extensión de navegador

Es el escenario más habitual en escritorio. La wallet —MetaMask, Rabby, Coinbase Wallet— se instala como extensión y, al cargar la página, inyecta `window.ethereum` en el contexto JavaScript siguiendo [EIP-1193](https://eips.ethereum.org/EIPS/eip-1193). La DApp detecta su presencia y puede enviar llamadas JSON-RPC directamente sin ningún canal externo.

El problema histórico de este modelo es que la primera extensión instalada sobreescribía `window.ethereum`, haciendo invisible al resto. [EIP-6963](https://eips.ethereum.org/EIPS/eip-6963) resuelve esto: las wallets emiten el evento `eip6963:announceProvider` con su metadata (nombre, icono, UUID) en respuesta al evento `eip6963:requestProvider` que lanza la DApp. Esto permite que MetaMask y Rabby coexistan y que el usuario elija explícitamente cuál usar. Las bibliotecas modernas como wagmi y RainbowKit implementan EIP-6963 de serie.

El flujo completo en este escenario es: carga de página → descubrimiento via EIP-6963 → usuario elige wallet → DApp llama `eth_requestAccounts` → wallet muestra diálogo de consentimiento → usuario aprueba → DApp recibe la dirección.

### Wallet móvil con navegador integrado

Muchas wallets móviles —[MetaMask Mobile](https://metamask.io/download/), [Trust Wallet](https://trustwallet.com/), [Coinbase Wallet](https://www.coinbase.com/wallet)— incluyen un navegador interno que inyecta `window.ethereum` igual que una extensión de escritorio. Si el usuario abre la DApp desde ese navegador interno, el comportamiento es idéntico al escenario de extensión. No hay relay, no hay QR: la wallet y la DApp comparten el mismo proceso.

Este escenario es técnicamente el más simple, pero impone una restricción de UX importante: el usuario tiene que abandonar su navegador habitual para usar el de la wallet.

### Wallet y DApp en dispositivos distintos (WalletConnect)

Cuando la DApp está en un navegador sin extensión instalada —o en una aplicación nativa— y la wallet vive en el móvil del usuario, la conexión se establece mediante [WalletConnect v2](https://docs.walletconnect.com/). El protocolo funciona de la siguiente forma:

1. La DApp genera un URI de emparejamiento (`wc:...`) y lo presenta al usuario como código QR o enlace profundo.
2. El usuario escanea el QR o pulsa el enlace desde su wallet móvil.
3. Ambas partes se conectan al servidor relay de WalletConnect, que actúa como intermediario de transporte.
4. La comunicación se cifra de extremo a extremo usando claves derivadas de X25519, de forma que el relay no puede leer el contenido de los mensajes.
5. La sesión es persistente: el usuario puede cerrar la app y reconectarse sin volver a escanear el QR, siempre que la sesión no haya expirado.

El relay es infraestructura operada por WalletConnect Inc., aunque el protocolo especifica cómo auto-hospedarlo. Esto implica una dependencia externa que el desarrollador debe contemplar: si el relay no está disponible, la conectividad falla aunque la wallet y la DApp funcionen correctamente. Esta dependencia es la principal razón por la que algunas aplicaciones de alto valor prefieren el escenario de extensión cuando es posible.

Las llamadas JSON-RPC que la DApp envía al provider de WalletConnect son exactamente las mismas que en EIP-1193; la diferencia es solo el canal de transporte.

### Wallets embebidas

Las wallets embebidas —[Privy](https://www.privy.io/), [Dynamic](https://www.dynamic.xyz/), [Web3Auth](https://web3auth.io/), [Magic](https://magic.link/)— crean y gestionan la wallet del usuario dentro de la propia experiencia de la DApp, sin requerir ninguna extensión ni aplicación externa. El usuario se autentica con email, Google o Apple ID, y el proveedor genera una clave privada asociada a esa identidad.

El modelo de custodia varía según el proveedor y su implementación, pero se puede decir que son non-custodial. Los modelos más comunes son:

- **MPC (Multi-Party Computation)**: la clave se divide en fragmentos entre el dispositivo del usuario y los servidores del proveedor usando técnicas como [threshold ECDSA](https://eprint.iacr.org/2020/540). Ninguna parte tiene la clave completa; la firma requiere colaboración en tiempo real. El proveedor no puede firmar unilateralmente y el usuario solo no puede firmar. Si el proveedor desaparece, la recuperación depende de los mecanismos de exportación que haya habilitado.
- **Clave en enclave seguro del dispositivo**: la clave reside en el Secure Enclave del dispositivo y se desbloquea con biometría (passkeys). El proveedor facilita la derivación y el acceso social, pero la clave nunca abandona el hardware del usuario.

Este escenario elimina la fricción de onboarding —no hay que instalar nada— a costa de introducir una dependencia de infraestructura del proveedor embebido. Es el modelo preferido para aplicaciones de consumo masivo donde el usuario objetivo no tiene experiencia previa con wallets.

Cabe señalar que en estos modelos el proveedor OAuth —Google, Apple— puede correlacionar la identidad social del usuario con su actividad on-chain, ya que el handle de autenticación y la dirección generada están vinculados en los servidores del proveedor embebido. [zkLogin](https://docs.sui.io/concepts/cryptography/zklogin), disponible actualmente en Sui, representa el extremo opuesto: utiliza OAuth como mecanismo de autenticación pero genera una prueba de conocimiento cero que demuestra al contrato que el usuario posee un JWT válido sin revelar su contenido, de modo que ni el proveedor OAuth ni ningún observador externo puede vincular la identidad social con la dirección on-chain. En el momento de escribir este documento no existe una implementación de zkLogin equivalente y ampliamente adoptada en EVM, aunque hay proyectos activos explorando esa dirección.

### Passkeys como firmante directo

Más allá de usarse como factor de acceso a la wallet, las passkeys pueden ser el propio mecanismo de firma en el contexto de Account Abstraction. [Coinbase Smart Wallet](https://www.coinbase.com/wallet/smart-wallet) es el ejemplo más conocido: la clave del usuario reside en el Secure Enclave del dispositivo y se firma con biometría; esa firma —que sigue el estándar WebAuthn— es verificada on-chain por el contrato de la SCW usando precompilados de curva P-256.

En este escenario el usuario nunca ve una SRP ni gestiona una clave privada en el sentido tradicional. La identidad on-chain está respaldada por hardware del dispositivo, lo que mejora la seguridad pero introduce una dependencia de ese dispositivo concreto para firmar.

### Hardware wallets

Dispositivos como [Ledger](https://www.ledger.com/) o [Trezor](https://trezor.io/) almacenan la clave privada en hardware aislado y la firma ocurre dentro del dispositivo sin que la clave salga nunca al sistema operativo del ordenador. La DApp se comunica con ellos a través de un software bridge: en el caso de Ledger, mediante [Ledger Connect Kit](https://developers.ledger.com/docs/connectivity/ledgerJS) o a través de MetaMask cuando el usuario importa su Ledger en la extensión.

Desde el punto de vista de la DApp, el proveedor expuesto sigue siendo `window.ethereum` o un provider de WalletConnect; la presencia del hardware es transparente para el código de la aplicación. El impacto visible es la latencia: cada firma requiere confirmación física en el dispositivo.

## La pila de protocolos

Una vez que el desarrollador entiende desde qué entorno llega el usuario, necesita comprender los protocolos que operan sobre ese canal. La pila se puede organizar en tres niveles: transporte (cómo se conectan DApp y wallet), autenticación de sesión (cómo el servidor verifica la identidad del usuario) y operaciones (cómo se firman mensajes y se ejecutan transacciones).

### Capa de transporte

**EIP-1193 — Provider estándar**:

[EIP-1193](https://eips.ethereum.org/EIPS/eip-1193) define la interfaz que toda wallet-extensión debe exponer: un objeto con un método `request({ method, params })` que devuelve una promesa y emite eventos `accountsChanged`, `chainChanged` y `disconnect`. Toda llamada JSON-RPC pasa por este único punto de entrada. La biblioteca wagmi abstrae esta interfaz, pero en el fondo todo llega a una llamada `provider.request(...)`.

**EIP-6963 — Descubrimiento multi-wallet**:

Como se mencionó en la sección de conceptos, [EIP-6963](https://eips.ethereum.org/EIPS/eip-6963) resuelve la coexistencia de múltiples extensiones. El ciclo de vida es:

1. La DApp emite `window.dispatchEvent(new Event('eip6963:requestProvider'))`.
2. Cada wallet escucha ese evento y responde con `eip6963:announceProvider`, adjuntando un objeto `EIP6963ProviderDetail` con `info` (uuid, name, icon, rdns) y `provider` (el objeto EIP-1193).
3. La DApp acumula todos los providers recibidos y los presenta al usuario.

El campo `rdns` (reverse DNS, p.ej. `io.metamask`) actúa como identificador estable para persistir la preferencia del usuario entre sesiones.

**WalletConnect v2 — Relay cifrado**:

En WalletConnect v2, la capa de transporte introduce el concepto de **tópico**: cada sesión tiene un identificador aleatorio de 32 bytes. Los mensajes se enrutan en el relay a través de ese tópico y se cifran con una clave simétrica derivada del intercambio ECDH inicial. El relay solo ve tópicos cifrados, no puede leer el contenido.

El protocolo distingue entre **pairing** (el emparejamiento inicial via QR) y **session** (la sesión negociada posteriormente). Un mismo pairing puede usarse para negociar varias sesiones con distintos permisos (namespaces), lo que permite a wallets avanzadas gestionar múltiples conexiones sin requerir escanear el QR repetidamente.

### Autenticación de sesión: SIWE

[Sign-In With Ethereum (EIP-4361)](https://eips.ethereum.org/EIPS/eip-4361) es el protocolo estándar para establecer una sesión autenticada entre el usuario y un servidor. El flujo es:

1. El cliente solicita un **nonce** al servidor. El nonce es de un solo uso y tiene caducidad corta.
2. El servidor devuelve el nonce y el cliente construye el mensaje SIWE con campos obligatorios: `domain`, `address`, `statement`, `uri`, `version`, `chain-id`, `nonce`, `issued-at` y opcionalmente `expiration-time` y `resources`.
3. El usuario firma el mensaje con `personal_sign` desde su wallet.
4. El cliente envía el mensaje y la firma al servidor.
5. El servidor verifica que la firma corresponde a la dirección declarada (recuperación de clave pública de la firma ECDSA), que el dominio coincide con el suyo (prevención de phishing), que el nonce es válido y no ha sido usado, y que el mensaje no ha expirado.
6. Si todo es correcto, el servidor emite una cookie de sesión o JWT con la dirección como identificador de usuario.

El punto crítico para el desarrollador es que la verificación off-chain de la firma no cuesta gas ni requiere ninguna llamada a la blockchain. Solo se necesita `ecrecover` (o su equivalente en la biblioteca del servidor). Para EOAs esto es suficiente. Para Smart Contract Wallets, la verificación sí requiere una llamada de lectura al contrato: [ERC-1271](https://eips.ethereum.org/EIPS/eip-1271) es el estándar que define el método `isValidSignature()` que toda SCW debe implementar para responder si una firma dada es válida según su lógica interna.

### Firma de mensajes

**`personal_sign`**:

Es el método más simple. La wallet añade el prefijo `\x19Ethereum Signed Message:\n{length}` al mensaje antes de firmar, lo que previene que una firma de mensaje pueda usarse como firma de transacción (son formatos distintos). SIWE usa `personal_sign`. La respuesta es una firma de 65 bytes (`r`, `s`, `v`) codificada en hex.

**`eth_signTypedData_v4` (EIP-712)**:

[EIP-712](https://eips.ethereum.org/EIPS/eip-712) permite firmar datos estructurados y tipados. En lugar de un string arbitrario, el usuario ve en su wallet un desglose legible de los campos y sus valores (p.ej., "Token: USDC, Spender: 0x…, Amount: 1000"). El hash firmado incluye un **domain separator** que incorpora el nombre del contrato, versión, chainId y dirección del contrato verificador, lo que hace que una firma válida en un contexto sea inválida en otro.

Los casos de uso más importantes son:

- **Permit (ERC-2612)**: permite al usuario aprobar un `allowance` de ERC-20 sin pagar gas, mediante una firma off-chain que el protocolo receptor puede usar para llamar a `permit()` on-chain en nombre del usuario.
- **Typed orders**: protocolos de trading como [CoW Protocol](https://cow.fi/) o [OpenSea Seaport](https://github.com/ProjectOpenSea/seaport) usan firmas EIP-712 para representar órdenes fuera de la cadena.
- **UserOperations y session keys**: la firma de una `UserOperation` sigue EIP-712 por especificación de ERC-4337. Las session keys —claves temporales con permisos acotados (por ejemplo, autorizar acciones en un juego sin requerir aprobación manual en cada una)— también se autorizan mediante firmas EIP-712 que el contrato de la SCW valida on-chain.

### Transacciones EOA

**`eth_sendTransaction`**:

El método estándar para enviar transacciones. La DApp construye el objeto de transacción (`to`, `value`, `data`, `gas`, `maxFeePerGas`, `maxPriorityFeePerGas`) y lo envía al provider. La wallet muestra un diálogo de confirmación con una estimación de gas y un desglose de la acción si el provider de datos (como [Blockaid](https://www.blockaid.io/) o [Blowfish](https://blowfish.xyz/)) puede interpretar el calldata. Una vez confirmado, la wallet firma la transacción y la propaga al nodo RPC configurado, que la introduce en el mempool.

El desarrollador no controla qué nodo RPC usa la wallet del usuario: MetaMask usa Infura por defecto, Rabby tiene su propia infraestructura. Esto puede generar latencias distintas en la propagación. Para controlar el RPC, la opción es pasar la transacción firmada al nodo del desarrollador mediante `eth_sendRawTransaction`, pero esto requiere que el usuario exporte su clave o que la DApp controle la firma (escenario de embedded wallet).

### Account Abstraction (ERC-4337)

En el modelo ERC-4337, las transacciones de usuario no van directamente al mempool: se empaquetan como **UserOperations** y pasan por una infraestructura alternativa.

**Estructura de una UserOperation**:

Una `UserOperation` es un objeto con campos análogos a una transacción (`sender`, `nonce`, `callData`, `callGasLimit`…) pero también con campos propios de AA: `initCode` (para crear la SCW si aún no existe), `paymasterAndData` (paymaster que patrocinará el gas, si lo hay) y la `signature` que el `EntryPoint` pasará a la SCW para que la valide según su lógica interna.

**Flujo de ejecución**:

1. La DApp construye la `UserOperation`.
2. La firma con la clave del usuario (EOA que actúa como firmante de la SCW) usando `eth_signTypedData_v4`.
3. La envía a un **bundler** mediante la llamada RPC `eth_sendUserOperation`.
4. El bundler simula la `UserOperation` para verificar que es válida y que la SCW tiene fondos suficientes o que el paymaster la cubre.
5. El bundler agrupa varias `UserOperations` en una sola transacción regular y la envía al contrato `EntryPoint` (`0x0000000071727De22E5E9d8BAf0edAc6f37da032` en ERC-4337 v0.7).
6. El `EntryPoint` llama a cada SCW para validar su `UserOperation` y luego para ejecutar el `callData`.

Los bundlers son operadores de infraestructura: [Alchemy](https://www.alchemy.com/), [Pimlico](https://www.pimlico.io/), [Stackup](https://www.stackup.sh/), [Biconomy](https://www.biconomy.io/). Algunos ofrecen también servicios de paymaster. El desarrollador elige el bundler al configurar el cliente de AA y puede cambiar de proveedor sin modificar la lógica de la DApp.

**Paymasters**:

Un paymaster es un contrato que acepta pagar el gas de `UserOperations` ajenas. Los modelos más comunes son:

- **Sponsoring paymaster**: el desarrollador financia el gas de sus usuarios. La UX resultante es gasless desde el punto de vista del usuario.
- **ERC-20 paymaster**: el usuario paga el gas en un token ERC-20 (p.ej., USDC) en lugar de ETH. El paymaster convierte el token al pagar al bundler.

**EIP-7702 — Delegación de código en EOAs**:

[EIP-7702](https://eips.ethereum.org/EIPS/eip-7702), activado en el hard fork Pectra (abril 2025), introduce un nuevo tipo de transacción (tipo 4) que permite a una EOA establecer su código como la delegación a un contrato existente. La EOA firma una autorización que incluye `chain_id`, `address` (del contrato delegado) y `nonce`. Durante la ejecución de esa transacción, y de forma persistente mientras la autorización esté activa, el `EXTCODESIZE` y `EXTCODECOPY` de la EOA devuelven el código del contrato delegado.

El resultado práctico: una EOA existente puede obtener las capacidades de una SCW —batching de llamadas, gas en tokens arbitrarios, recuperación social— sin cambiar de dirección y sin migrar activos. El usuario mantiene su EOA original y el ecosistema no se fragmenta. Para el desarrollador, esto significa que a medio plazo la distinción entre EOA y SCW se difuminará; las bibliotecas como [viem](https://viem.sh/experimental/eip7702) ya exponen utilidades para construir transacciones de tipo 4.

## Bibliotecas y herramientas

Las bibliotecas del ecosistema se organizan en capas: cada capa construye sobre la anterior y no son alternativas entre sí. El stack habitual para una DApp en React es:

```text
RainbowKit  ← capa de UI: botón "Connect Wallet" y modal de selección
    ↑ usa
wagmi       ← capa de hooks React: gestión de estado, conexión, contratos
    ↑ usa
viem        ← capa de bajo nivel: RPC, ABI, firmas, transacciones
```

La alternativa a viem es ethers.js (no a wagmi ni a RainbowKit). La alternativa a RainbowKit es AppKit. Para Account Abstraction se añade permissionless.js, que también se apoya en viem.

### viem — capa de bajo nivel

[viem](https://viem.sh/) es la biblioteca de bajo nivel de referencia para TypeScript. Gestiona directamente las llamadas JSON-RPC, la codificación ABI, la construcción de transacciones y las firmas. No hace suposiciones sobre el framework: funciona en React, Vue o Node.js. wagmi y permissionless.js usan viem internamente; el desarrollador raramente necesita llamar a viem directamente si ya usa wagmi.

Para EIP-7702, el namespace `viem/experimental` expone `walletClient.signAuthorization()` para construir autorizaciones de delegación de código.

### ethers.js — alternativa a viem

[ethers.js v6](https://docs.ethers.org/v6/) es la alternativa clásica a viem. Cubre el mismo nivel —llamadas RPC, contratos, firmas— con una API distinta. Es la opción habitual en proyectos con base de código anterior a la adopción de viem. Para proyectos nuevos, viem es preferible por su tipado estricto, pero ethers.js sigue siendo completamente válido.

### wagmi — hooks React sobre viem

[wagmi](https://wagmi.sh/) es la capa de hooks de React para Ethereum. Usa viem para las llamadas al nodo y TanStack Query para caché y revalidación. No se elige entre viem y wagmi: wagmi envuelve viem y los usa conjuntamente. Los hooks principales son:

- `useAccount()` — dirección conectada, estado de conexión.
- `useConnect()` / `useDisconnect()` — gestión de conexión.
- `useReadContract()` / `useWriteContract()` — lectura y escritura en contratos.
- `useSignMessage()` / `useSignTypedData()` — firma de mensajes.
- `useSendTransaction()` — envío de transacciones.
- `useSwitchChain()` — cambio de red.

wagmi gestiona el descubrimiento EIP-6963 y la integración con WalletConnect mediante conectores. El desarrollador no toca directamente `window.ethereum` ni el relay de WalletConnect.

### RainbowKit — UI sobre wagmi

[RainbowKit](https://www.rainbowkit.com/) añade la capa de interfaz de usuario encima de wagmi: el botón "Connect Wallet", el modal de selección de wallet con soporte EIP-6963, la UI de confirmación de red y los estilos configurables. Requiere wagmi —no es una alternativa a él— y evita que el desarrollador implemente esa UX desde cero.

[ConnectKit](https://docs.family.co/connectkit) de Family es la alternativa con diseño más cuidado y soporte nativo para Safe y Coinbase Smart Wallet. [AppKit](https://reown.com/appkit) (antes Web3Modal), mantenida por el equipo de WalletConnect, tiene mayor énfasis en el flujo de WalletConnect y soporte para ecosistemas adicionales (Solana, Bitcoin). La evaluación independiente de [0xpass sobre RainbowKit](https://blog.0xpass.io/p/exploring-rainbowkit-assessing-its) documenta con detalle las limitaciones de cada librería en cuanto a detección y priorización de wallets.

### Permissionless.js — Account Abstraction sobre viem

[Permissionless.js](https://docs.pimlico.io/permissionless) de Pimlico es la biblioteca de referencia para ERC-4337. Se apoya en viem y expone un `SmartAccountClient` que construye y envía `UserOperations` en lugar de transacciones regulares, manteniendo la misma API que un `WalletClient` de viem. Soporta las SCW más comunes ([Safe](https://safe.global/), [Kernel](https://github.com/zerodevapp/kernel), [Biconomy Nexus](https://docs.biconomy.io/)) e integra paymasters para gas patrocinado o en ERC-20.

### MetaMask Delegation Toolkit — delegation flows

El [MetaMask Delegation Toolkit](https://docs.metamask.io/delegation-toolkit/) implementa los estándares [ERC-7710](https://eips.ethereum.org/EIPS/eip-7710) y [ERC-7715](https://eips.ethereum.org/EIPS/eip-7715) para crear delegaciones on-chain con restricciones (caveated delegations): una cuenta puede delegar capacidades específicas a otra —por ejemplo, autorizar a una DApp a ejecutar cierto tipo de operaciones durante un periodo limitado— sin cederle el control total de la wallet.

No es una biblioteca de UI ni un sustituto de RainbowKit o wagmi. Es una herramienta especializada comparable a permissionless.js: se usa cuando el caso de uso requiere delegation flows explícitos, como session keys avanzadas o permisos delegados entre contratos. Requiere que la SCW del usuario implemente ERC-7710.

## Decisiones arquitectónicas

Con todo el panorama expuesto, las decisiones prácticas que un desarrollador debe tomar al inicio de un proyecto son las siguientes:

### ¿Qué escenarios de usuario debo cubrir?

Si la audiencia es principalmente usuarios avanzados en escritorio, el escenario de extensión de navegador con [EIP-6963](https://eips.ethereum.org/EIPS/eip-6963) es suficiente. Si se apunta a usuarios móviles o sin experiencia previa con wallets, [WalletConnect](https://docs.walletconnect.com/) y/o wallets embebidas son necesarios; los proveedores principales son [Privy](https://www.privy.io/), [Dynamic](https://www.dynamic.xyz/) y [Alchemy Account Kit](https://accountkit.alchemy.com/). Las dos opciones no son excluyentes: [wagmi](https://wagmi.sh/) y [RainbowKit](https://www.rainbowkit.com/) las combinan por defecto.

### ¿Necesita mi DApp autenticación en un servidor?

Si hay un backend que debe conocer quién es el usuario entre solicitudes, [SIWE (EIP-4361)](https://eips.ethereum.org/EIPS/eip-4361) es el estándar: el usuario firma un mensaje estructurado y el servidor verifica la firma off-chain, sin coste de gas. Si la DApp es una SPA puramente on-chain, no hay sesión que gestionar: la EVM verifica cada transacción de forma independiente.

### ¿Debo soportar Account Abstraction?

Para la mayoría de DApps la respuesta hoy es: soportar EOA (cuentas tradicionales de Ethereum) siempre, y ofrecer mejoras de UX —gas patrocinado, batching de operaciones— a usuarios con Smart Contract Wallets si lo requiere el caso de uso. [EIP-7702](https://eips.ethereum.org/EIPS/eip-7702), activado en el hard fork Pectra (2025), permite que una EOA obtenga capacidades de SCW sin cambiar de dirección, lo que reducirá esta distinción con el tiempo. Si el caso de uso requiere delegation flows explícitos —delegar permisos acotados a una DApp o a una session key—, el [MetaMask Delegation Toolkit](https://docs.metamask.io/delegation-toolkit/) implementa los estándares [ERC-7710](https://eips.ethereum.org/EIPS/eip-7710) y [ERC-7715](https://eips.ethereum.org/EIPS/eip-7715) para ese propósito.

### ¿Qué biblioteca usar?

Para proyectos nuevos en React: [viem](https://viem.sh/) como capa de bajo nivel, [wagmi](https://wagmi.sh/) para los hooks de React y [RainbowKit](https://www.rainbowkit.com/) para la UI de conexión. No se elige entre ellas: se usan las tres en capas. [ethers.js](https://docs.ethers.org/v6/) es la alternativa a viem para proyectos existentes. Para Account Abstraction se añade [permissionless.js](https://docs.pimlico.io/permissionless) sobre viem. Para delegation flows con permisos acotados, el [MetaMask Delegation Toolkit](https://docs.metamask.io/delegation-toolkit/).

---
