# Wallet

## La propiedad digital

En el mundo físico, poseer algo significa tenerlo en tus manos o tener un documento legal que lo certifica. Un billete de veinte euros no puede copiarse. Una escritura de propiedad existe en un registro notarial. Hay instituciones, leyes y fuerzas físicas que hacen cumplir esa propiedad.

En el mundo digital, nada de eso existe de forma natural. Un archivo se puede copiar infinitas veces sin que el original desaparezca. No hay escasez natural en los bits. Por eso, antes de Bitcoin, era imposible crear dinero digital genuino: cualquier sistema que alguien construyera podía duplicar monedas arbitrariamente.

Bitcoin resolvió esto en 2009 con un truco matemático: en lugar de que la propiedad la garanticen instituciones, la garantiza la criptografía. Cada unidad de bitcoin está asociada a una dirección en la blockchain. Quien tenga la clave privada de esa dirección puede matemáticamente demostrar que es quien tiene derecho a mover esos fondos. No hay banco ni notario que lo certifique: lo certifica la matemática, ejecutada por miles de nodos independientes en todo el mundo.

Una wallet es la herramienta que guarda esa clave privada y te permite usarla. Técnicamente no almacena criptomonedas, que existen como registros en la blockchain. Almacena la prueba de que eres tú quien puede moverlas. La diferencia importa: si tu banco desaparece, tu dinero desaparece con él. Si perdieras acceso a la blockchain pero conservaras tu clave privada, tus fondos seguirían ahí. Y al revés: si pierdes la clave privada, nadie en el mundo puede ayudarte a recuperar lo que había en esa dirección.

## Centro de operaciones en Web3

Con Ethereum y la proliferación de smart contracts, las wallets dejaron de ser simples custodios de claves. Cada acción que realizas en Web3 requiere tu firma: enviar fondos, autorizar que un protocolo DeFi mueva tus tokens, conectarte a una dApp, votar en una DAO, delegar permisos temporales a una sesión, agrupar múltiples operaciones en un batch. La wallet verifica, aprueba o rechaza cada solicitud antes de que llegue a la blockchain. Sin tu firma, ningún contrato puede tocar nada que te pertenezca. Eso convierte a la wallet en el gatekeeper de todo lo que haces on-chain.

Tu dirección es también, en cierto sentido, tu identidad. No creas cuentas con email y contraseña en cada servicio: la misma dirección te identifica en un exchange descentralizado, en un juego on-chain, en un marketplace de NFTs y en cualquier protocolo que se despliegue en el futuro. Nadie puede revocarla.

Sobre esta identidad se construyen sistemas más avanzados. Los [DIDs (Decentralized Identifiers)](https://www.w3.org/TR/did-core/), estándar del W3C, permiten crear identidades verificables sin registros centralizados: un identificador como `did:ethr:0xABCD...` está anclado en la blockchain y controlado por quien tenga esa clave privada. Proyectos como [Ethereum Name Service (ENS)](https://ens.domains/) añaden legibilidad humana: en lugar de `0xABCD...`, tu identidad puede ser `tu-nombre.eth`. Esta infraestructura abre la puerta a credenciales verificables, diplomas, certificaciones, reputación on-chain que el usuario controla y puede presentar selectivamente.

## Quién controla las claves

La pregunta más importante sobre cualquier wallet es quién tiene acceso real a las claves privadas. La respuesta define cuánta soberanía real tienes.

En un extremo están las **custodial wallets**: un exchange como Coinbase, Binance o Kraken guarda tus claves. Accedes con email y contraseña. Si olvidas la contraseña, la recuperas por email. Hay soporte al cliente e interfaz familiar. El precio es que técnicamente no posees nada: posees un derecho contractual frente a una empresa. Si esa empresa quiebra, es hackeada, congela cuentas o está en una jurisdicción que bloquea tu país, tus fondos pueden desaparecer. El colapso de Mt. Gox en 2014 (850.000 bitcoins) y el de FTX en 2022 (miles de millones de usuarios) son los referentes de lo que significa confiar las claves a terceros.

En el otro extremo están las **self-custodial wallets**: tú controlas exclusivamente tus claves mediante una seed phrase, una secuencia de 12 o 24 palabras que es el único respaldo de todo. Nadie más puede acceder a tus fondos. MetaMask, Ledger, Electrum son ejemplos. La soberanía es total: nadie puede congelar tu cuenta, censurarte ni pedirte identificación. El precio es responsabilidad absoluta: si pierdes la seed phrase no hay recuperación posible. No hay "olvide mi contraseña". Los fondos quedan matemáticamente inaccesibles para siempre.

Entre ambos extremos está la **custodia no-custodial distribuida**: el control se fragmenta entre múltiples partes de forma que ninguna por sí sola puede mover los fondos ni robártelos. No existe seed phrase que perder, pero hay confianza distribuida en terceros. Las MPC wallets y las smart contract wallets con recuperación social viven aquí. Para grandes patrimonios institucionales existe además la custodia profesional (Fireblocks, BitGo Trust, Coinbase Custody) con HSMs certificados, seguros y cumplimiento regulatorio.

## Hot wallet, cold wallet

Independientemente de quién controla las claves, hay una segunda dimensión relevante: si la wallet está conectada a internet.

Una **hot wallet** siempre está online. Es necesaria para uso cotidiano: firmar transacciones, interactuar con dApps, gestionar portfolios activos. Al estar permanentemente conectada, es una superficie de ataque: malware, extensiones de navegador maliciosas y phishing son amenazas reales. MetaMask, Rainbow, Phantom, cualquier app móvil.

Una **cold wallet** mantiene las claves offline. Los dispositivos hardware como Ledger o Trezor son el ejemplo más común: las claves nunca salen del dispositivo, y cuando necesitas firmar algo, conectas el hardware físicamente, verificas en su pantalla y apruebas con un botón. Paper wallets (claves impresas) y setups airgapped (ordenadores sin ninguna conectividad dedicados solo a firmar) son variantes más extremas.

La estrategia habitual combina ambas: hot wallet con cantidades pequeñas para uso diario, como la cartera que llevas en el bolsillo; cold wallet para ahorros significativos, como una caja fuerte. Cuánto en cada una depende del perfil de riesgo.

## Cómo evolucionaron las wallets

Las primeras wallets de Bitcoin generaban claves privadas aleatorias e independientes para cada dirección. Cada clave era única, sin relación matemática con las demás. Si generabas diez direcciones, necesitabas backup de las diez claves por separado. Perder el archivo `wallet.dat` significaba perder acceso a todo permanentemente.

En 2012, el estándar [BIP-32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki) introdujo las **HD wallets** (Hierarchical Deterministic): en lugar de claves aleatorias, una HD wallet deriva todas sus claves desde una única semilla mediante una función matemática determinista. Con una sola seed phrase de 12 o 24 palabras ([BIP-39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki)) puedes restaurar todas las direcciones que hayas generado, en cualquier wallet compatible. El estándar [BIP-44](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki) organizó la jerarquía por moneda, cuenta y propósito: `m / purpose' / coin_type' / account' / change / address_index`. Todas las wallets modernas son HD.

El campo `coin_type` también determina el formato de dirección. En Bitcoin hay dos familias: Legacy (Base58), donde P2PKH empieza con `1` y P2SH con `3`, y SegWit (Bech32), donde las direcciones empiezan con `bc1q` y ofrecen comisiones un 30-40% más bajas con mayor eficiencia de bloque. Las wallets modernas usan SegWit por defecto. [Más sobre los formatos](https://bitcoin.stackexchange.com/questions/64733/what-is-p2pk-p2pkh-p2sh-p2wpkh-eli5).

La seed phrase es el único respaldo. No hay segundo factor, no hay recuperación por email. Si alguien la obtiene, accede a todos tus fondos presentes y futuros derivados de ella. Debe guardarse offline: papel resistente, metal grabado (Cryptosteel y similares), en ubicaciones físicamente separadas. Nunca fotografiada, nunca en servicios cloud, nunca en mensajería. La práctica recomendada es restaurar la wallet en un dispositivo separado para verificar que el backup funciona antes de enviar fondos.

## Bitcoin y Ethereum gestionan los fondos de forma distinta

Bitcoin usa el modelo **UTXO** (Unspent Transaction Outputs): tu saldo no es un número almacenado en ningún sitio, sino la suma de las "monedas no gastadas" que te pertenecen dispersas por la blockchain. Cuando envías bitcoin, la wallet selecciona UTXOs como entrada, construye la salida hacia el destinatario y devuelve el cambio a una dirección tuya nueva. Por eso las wallets Bitcoin HD generan una dirección nueva por transacción: cada cambio va a dirección fresca, mejorando la privacidad.

Ethereum usa un modelo de **cuenta**: hay un saldo numérico directamente asociado a tu dirección, que sube o baja con cada transacción. Es más simple: las wallets Ethereum suelen mostrar una sola dirección activa.

Esta diferencia importa cuando recibes una clave privada de terceros, por ejemplo una paper wallet o un regalo. Tienes dos opciones: **importar**, que agrega la clave a tu wallet pero deja que siga existiendo en su origen, con todos los riesgos que eso conlleva si el dispositivo donde se generó estaba comprometido o si alguien más la conoce; o **barrer** (sweep), que transfiere todos los fondos a una dirección nueva que solo tú controlas, vaciando la original e invalidando cualquier riesgo anterior. Barrer es la opción correcta en casi todos los casos. Importar solo tiene sentido si necesitas mantener la dirección original activa, por ejemplo si es una EOA Ethereum con contratos asociados.

## La evolución de las cuentas Ethereum: EOA → SCW → EIP-7702

Desde los primeros años de Ethereum, las cuentas de usuario son EOAs (Externally Owned Accounts): una dirección controlada por una clave privada única, con lógica de firma fija en ECDSA. Si pierdes la clave, pierdes la cuenta para siempre. No hay forma de cambiar el algoritmo de firma. Cada operación requiere ETH para el gas. Esta rigidez funcionó durante años, pero a medida que Ethereum se volvió infraestructura financiera global, sus limitaciones se hicieron obstáculos reales para la adopción masiva.

Account Abstraction surgió para resolver esto: en lugar de que la lógica de validación esté cableada en el protocolo, cada cuenta puede definir su propia lógica en código. Las **smart contract wallets** (SCW) son contratos inteligentes que actúan como cuentas: programan quién puede autorizar qué, bajo qué condiciones. Recuperación social mediante guardianes, límites de gasto diarios, aprobación multifirma para transacciones grandes, pago de gas con cualquier token, sesiones de permisos temporales, soporte para algoritmos de firma como los usados por passkeys o biometría.

El estándar [ERC-4337](https://eips.ethereum.org/EIPS/eip-4337), desplegado en 2023, implementó esto sin modificar el protocolo: el usuario genera una UserOperation, un Bundler la agrupa con otras y la envía al contrato EntryPoint. Un Paymaster puede patrocinar el gas, permitiendo que el usuario ni siquiera necesite tener ETH para su primera transacción. El onboarding se vuelve tan simple como crear una cuenta web2.

El problema de ERC-4337 es la migración: los usuarios con EOAs existentes tendrían que mover fondos a una SCW nueva. [EIP-7702](https://eips.ethereum.org/EIPS/eip-7702), incluido en el hard fork Pectra de 2025, resolvió esto: permite que una EOA delegue temporalmente su comportamiento a un contrato durante una transacción, actuando como SCW sin dejar de ser EOA. MetaMask o cualquier wallet EOA puede acceder a funcionalidades de SCW sin migrar fondos ni cambiar de dirección.

La evolución: EOA → SCW con lógica programable (ERC-4337) → EOA con capacidades de SCW temporales (EIP-7702). Ejemplos: [Safe](https://safe.global/) para multi-firma en DAOs y tesorerías, [Argent](https://www.argent.xyz/) para recuperación social, ZeroDev como SDK para desarrolladores.

Más información: [Account Abstraction explicado](https://www.alchemy.com/blog/account-abstraction)

## MPC wallets: distribuir la clave sin seed phrase

Las MPC wallets resuelven el problema de la seed phrase desde un ángulo diferente: fragmentar matemáticamente la clave privada en múltiples shares distribuidos entre participantes distintos. La clave completa nunca existe en ningún lugar, ni durante la generación ni durante la firma.

Cuando firmas una transacción, los fragmentos colaboran mediante computación distribuida para generar una firma ECDSA válida sin reconstruir la clave. El resultado on-chain es indistinguible de una EOA normal: mismos fees, mismo formato, sin contratos adicionales. Esto contrasta con el multisig on-chain, donde la coordinación entre firmantes es visible en la blockchain y tiene coste de gas adicional.

Los esquemas usan umbrales configurables (threshold signatures). En 2-de-3, necesitas 2 de 3 fragmentos para firmar, tolerando la pérdida de uno. ZenGo implementa 2-de-2 entre el dispositivo del usuario y sus servidores: ninguno puede mover fondos solo, pero ninguno puede robártelos solo. Si pierdes el dispositivo, recuperas tu fragmento mediante biometría e identidad.

La ventaja es eliminar la seed phrase como punto único de fallo. El precio es que sigues dependiendo de la disponibilidad y honestidad del proveedor del otro fragmento. Adicionalmente, implementaciones incorrectas de los protocolos subyacentes (GG20, CGGMP) pueden ser catastróficamente inseguras.

Comparando los cuatro modelos: una EOA requiere seed phrase y tiene un único punto de fallo, pero sus firmas son indistinguibles on-chain sin coste adicional. El multisig on-chain distribuye claves completas eliminando el punto único de fallo, pero la coordinación es visible y tiene coste de gas. La SCW tiene lógica completamente programable y recuperación social, pero implica coste on-chain. La MPC elimina seed phrase y es indistinguible on-chain sin gas adicional, pero depende de proveedores de fragmentos y no tiene lógica customizable.

Ejemplos: [Fireblocks](https://www.fireblocks.com/) para uso institucional con HSMs distribuidos, [ZenGo](https://zengo.com/) para consumidores, [Web3Auth](https://web3auth.io/) como infraestructura para desarrolladores con social login.

Más información: [Threshold Signatures Explained](https://www.fireblocks.com/what-is-mpc/), [MPC vs Multisig](https://www.zengo.com/mpc-vs-multisig/)

## Autenticación: TEE, passkeys y MFA

La seguridad de una wallet no depende solo de dónde está la clave sino de quién puede activarla.

Los dispositivos móviles modernos incluyen un **TEE** (Trusted Execution Environment): una zona aislada del procesador donde se generan y almacenan claves sin que el sistema operativo principal pueda acceder a ellas. En iPhone es el Secure Enclave, en Android es ARM TrustZone. Incluso con malware o root instalado, las claves dentro del TEE permanecen protegidas por hardware. La autenticación biométrica se integra directamente: los templates de Face ID o huella dactilar se almacenan y comparan dentro del entorno seguro, sin que el sistema operativo vea nunca esos datos.

Los **passkeys**, basados en el estándar [WebAuthn](https://www.w3.org/TR/webauthn/), llevan esto más lejos. Cuando creas una wallet con passkeys, tu dispositivo genera un keypair dentro del TEE vinculado criptográficamente al dominio del servicio. Para firmar, el servicio envía un desafío, tu biometría lo aprueba y el TEE firma internamente devolviendo solo la firma. Lo decisivo es que son phishing-resistant: la clave está vinculada al dominio específico donde se creó, así que si un sitio falso intenta hacerte firmar algo, el dispositivo detecta que el dominio no coincide y rechaza la operación aunque el sitio sea visualmente idéntico al legítimo. Tu iPhone o Android se convierte en hardware wallet. Servicios como [Turnkey](https://www.turnkey.com/), [Dynamic](https://www.dynamic.xyz/) y [Privy](https://www.privy.io/) construyen wallets Ethereum sobre passkeys.

Para exchanges custodiales, la autenticación multifactor es crítica. La recomendación es TOTP (Google Authenticator, Authy) o hardware keys ([YubiKey](https://www.yubico.com/)) en lugar de SMS, que es vulnerable a SIM swapping: el atacante convence al operador de transferir tu número a su SIM e intercepta los códigos 2FA.

## Seguridad: multisig y backup

**Multisig** requiere varias claves privadas independientes para autorizar una transacción. En 2-de-3, necesitas 2 de 3 claves posibles, tolerando la pérdida de una. En 3-de-5, necesitas 3 de 5. Los usos son concretos: distribuir claves entre dispositivos distintos para que un solo compromiso no sea suficiente; requerir aprobación de múltiples ejecutivos para mover una tesorería corporativa; controlar fondos conjuntos entre socios sin una clave maestra. A diferencia de MPC, multisig es visible on-chain y tiene coste adicional de gas.

Más información: [Multisig en Bitcoin](https://academy.bit2me.com/direcciones-bitcoin-multifirma/), [Multisig en Electrum](https://electrum.readthedocs.io/en/latest/multisig.html)

Para el **backup de seed phrases**: papel resistente o metal grabado (Cryptosteel y similares), en ubicaciones físicamente separadas, nunca digital. BIP-39 permite añadir una passphrase adicional que actúa como palabra extra y genera una wallet completamente diferente, útil para wallets señuelo donde la passphrase vacía da una wallet vacía visible y la passphrase memorizada da acceso a los fondos reales. Para holdings grandes, multisig 2-de-3 o 3-de-5 con claves en ubicaciones geográficas distintas. Para herencia, documentar el plan de acceso con suficiente información para que herederos puedan acceder sin revelar las claves a tiempo real.

## Ejemplo: MetaMask

[MetaMask](https://metamask.io/) es la wallet más utilizada para Ethereum y chains EVM-compatibles, y un buen ejemplo de cómo funciona una wallet moderna en la práctica.

Es una HD wallet self-custodial (BIP-39/32/44) con seed phrase de 12 palabras, disponible como extensión de navegador y app móvil. Se conecta a la blockchain a través de proveedores RPC como [Infura](https://www.infura.io/) por defecto, configurable a Alchemy, QuickNode o nodo propio. Inyecta `window.ethereum` en las páginas web; las dApps deben pedir permiso explícito antes de acceder a tu dirección (EIP-1102). Las versiones modernas simulan transacciones antes de presentarlas y advierten sobre aprobaciones ilimitadas de tokens.

Como hot wallet siempre está conectada a internet: malware, extensiones maliciosas y phishing son amenazas reales. Sus proveedores RPC pueden rastrear la IP y actividad, y han bloqueado regiones geográficas en el pasado. Lo razonable: no mantener cantidades grandes, verificar siempre URLs, auditar y revocar aprobaciones con [Revoke.cash](https://revoke.cash), usar una wallet separada para interacciones de riesgo alto, y considerar firmar las transacciones con Ledger o Trezor conectados como capa adicional.

Más información: [Documentación de MetaMask](https://docs.metamask.io/)

## Recursos adicionales

- [BIP-32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), [BIP-39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki), [BIP-44](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki) — Estándares HD wallets
- [ERC-4337](https://eips.ethereum.org/EIPS/eip-4337) — Account Abstraction
- [EIP-7702](https://eips.ethereum.org/EIPS/eip-7702) — EOA como smart contract temporal
- [W3C DID Core](https://www.w3.org/TR/did-core/) — Identidad descentralizada
- [WebAuthn](https://www.w3.org/TR/webauthn/) — Passkeys
- [Electrum Documentation](https://electrum.readthedocs.io/en/latest/index.html)
- [MetaMask Documentation](https://docs.metamask.io/)

---
