# Experiencia de usuario

La complejidad técnica de Web3 (gestionar claves privadas, pagar gas en ETH, firmar transacciones manualmente, seed phrases de 12-24 palabras) crea barreras de entrada enormes para usuarios acostumbrados a la simplicidad de Web2. Los protocolos de UX y abstracción de cuentas eliminan esta fricción sin comprometer seguridad o descentralización, haciendo Web3 accesible para millones de usuarios que nunca aprenderán qué es una clave privada.

Nuestro criterio al crear un proyecto para Web3 debe centrarse en comprender estos conceptos para poder elegir la mejor solución tecnológica a utilizar.

**Account Abstraction (ERC-4337)**:

La abstracción de cuentas representa un cambio paradigmático en las wallets de Ethereum. Tradicionalmente existen dos tipos de cuentas: EOAs (controladas por claves privadas, limitadas a transacciones con ETH para gas) y Contract Accounts (contratos inteligentes que no pueden iniciar transacciones por sí mismos).

[ERC-4337](https://eips.ethereum.org/EIPS/eip-4337) introduce las Smart Contract Wallets que combinan lo mejor de ambos mundos, habilitando funcionalidades avanzadas:

* Recuperación social mediante guardianes (amigos, familiares, dispositivos) en lugar de seed phrases
* Paymasters: terceros pagan el gas o se paga con el token que se mueve, eliminando la necesidad de tener ETH
* Batching: combinar múltiples operaciones en una sola transacción (aprobar + swap)
* Límites de gasto y permisos granulares como tarjetas de crédito
* Session keys: delegar permisos para acciones específicas sin aprobar cada transacción
* Firma con cualquier método criptográfico (BLS, biométrica), no solo ECDSA

**Implementaciones principales**:

* MetaMask: la wallet más adoptada evolucionó en 2024-2025 con Social Login (creación mediante Google/Apple + contraseña manteniendo auto-custodia), Smart Accounts Kit (smart contract wallets con delegaciones, permisos granulares ERC-7715, gas abstraction), y multichain accounts. Más en [metamask.io](https://metamask.io/) y [Smart Accounts Kit](https://docs.metamask.io/smart-accounts-kit/).

* Safe (antes Gnosis Safe): smart contract wallet más usada por DAOs. Multi-sig, módulos personalizables, batching. [safe.global](https://safe.global/)

* Argent: mobile-first con recuperación social, límites de gasto, transacciones sin gas. [argent.xyz](https://www.argent.xyz/)

* Biconomy, ZeroDev, Stackup: infraestructura AA como servicio (paymasters, bundlers, social recovery, passkeys)

**Social Login y onboarding Web2**:

Soluciones que permiten crear wallets usando métodos familiares:

* MetaMask Social Login: Google/Apple ID + contraseña única. Auto-custodia mediante SRP generado automáticamente, recuperable solo con credenciales del usuario.

* Magic, Web3Auth: email o social login con claves gestionadas mediante MPC/threshold cryptography. El usuario no sabe que interactúa con blockchain.

* Privy: combina social login con progressive self-custody (migración gradual a control total).

**Passkeys y autenticación biométrica**:

Usar passkeys (Face ID, huella digital) como método de firma. Las claves se almacenan en hardware seguro del dispositivo (Secure Enclave, TEE) con recuperación mediante iCloud Keychain o Google Password Manager. Proyectos: Turnkey, Capsule, Dynamic.

**Experiencias sin firma visible**:

* Session keys: juegos blockchain ejecutan movimientos sin confirmación por cada acción
* Pre-autorizaciones: aplicaciones ejecutan operaciones predefinidas dentro de límites
* Intents: usuarios expresan intenciones ("comprar NFT X por máximo Y ETH") y solvers las ejecutan óptimamente
* Meta-transacciones (EIP-2771): usuario firma mensaje, relayer paga gas y envía transacción

**Desafíos y trade-offs**:

* Mayor complejidad de contratos incrementa superficie de ataque
* Transacciones más costosas en gas por lógica adicional
* Fragmentación entre implementaciones incompatibles
* Dependencias en infraestructura centralizada (paymasters, bundlers, relayers)
* Recuperación social riesgosa si guardianes son comprometidos

**Estrategia recomendada**:

Para proyectos que aspiran a adopción masiva:

* MVP con EOAs (MetaMask, WalletConnect) para validar product-market fit
* Integrar AA progresivamente (MetaMask Smart Accounts Kit, Biconomy, Dynamic) tras validación
* Ofrecer ambas opciones: EOAs para usuarios avanzados, AA/social login para nuevos usuarios

## Identidad descentralizada y experiencia de usuario

La experiencia de usuario en Web3 mejora dramáticamente cuando los usuarios pueden gestionar identidades legibles y portables en lugar de recordar direcciones hexadecimales incomprensibles. Los protocolos de identidad descentralizada transforman la interacción con blockchain de algo técnico y críptico a algo intuitivo y humano.

Los naming services como [ENS](https://ens.domains/) permiten usar `nombre.eth` en lugar de `0x742d35...`, facilitando transacciones y creando identidades memorables. Los Decentralized Identifiers (DIDs) siguiendo el estándar [W3C DID](https://www.w3.org/TR/did-core/) proporcionan identificadores únicos sin autoridad central, mientras que las Verifiable Credentials habilitan verificación selectiva de atributos sin revelar más información de la necesaria mediante zero-knowledge proofs.

Para organizaciones descentralizadas, [ERC-4824](https://eips.ethereum.org/EIPS/eip-4824) estandariza cómo las DAOs publican metadatos mediante `daoURI()`, permitiendo que exploradores y herramientas muestren información organizacional de forma interoperable. Esto facilita participación informada en gobernanza sin depender de bases de datos centralizadas.

La integración de estos protocolos en aplicaciones permite experiencias como autenticación mediante wallet (Sign-In with Ethereum), presentación de credenciales académicas o profesionales sin contactar al emisor original, y portabilidad completa de reputación entre plataformas. Un usuario puede construir su identidad social en una aplicación y llevarla instantáneamente a otra, rompiendo el lock-in tradicional de Web2.

Sin embargo, la fragmentación entre estándares y la complejidad de implementación siguen siendo barreras. Los desarrolladores deben elegir cuidadosamente qué protocolos integrar según su caso de uso específico, balanceando interoperabilidad, privacidad y facilidad de adopción.

Para un análisis completo de identidad descentralizada, incluyendo DIDs, Verifiable Credentials, naming services, Proof of Personhood, reputación on-chain y protocolos de autenticación, consulta el documento [Identidad Web3](8-1-identity-web3.md).

> Los proyectos que logren experiencias comparables a Web2 manteniendo los beneficios de descentralización capturarán la mayor parte de la adopción masiva en los próximos años.

---
