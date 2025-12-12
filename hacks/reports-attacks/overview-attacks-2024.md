# Web3 Attack Landscape 2024

## 1. Introducción

Este informe resume el panorama actual de ataques en Web3, basado en datos consolidados hasta finales de 2024. No existen todavía informes oficiales de 2025, por lo que toda la información pública verificable proviene de análisis anuales y reportes publicados durante 2024 o que resumen el año 2023-2024.

## 2. Por qué las fuentes son de 2024

Las organizaciones que recopilan datos de hacks, exploits y vulnerabilidades publican informes anuales, no continuos. Los reportes más recientes disponibles son:

* [Immunefi Crypto Losses Reports](https://immunefi.com/reports/): Informes detallados sobre pérdidas en el ecosistema cripto.
* [DefiLlama Exploits & Hack Database](https://defillama.com/hacks): Base de datos en tiempo real de hacks en DeFi.
* [Chainalysis Crypto Crime Report](https://www.chainalysis.com/reports/): Análisis forense sobre crimen en blockchain.
* [CertiK Web3 Security Reports](https://www.certik.com/resources): Informes de seguridad y auditoría.
* [SlowMist Hacked Stats](https://hacked.slowmist.io/): Estadísticas y archivo de incidentes de seguridad.

Estas fuentes cubren incidentes hasta finales de 2023 y datos parciales/actualizados de 2024, convirtiéndose en la base más completa disponible actualmente.

Por ello, el panorama general disponible más preciso es el de 2024, y cualquier proyección para 2025 sería hipotética.

## 3. Categorías de ataque predominantes (2024)

### 3.1 Compromiso de claves e identidad

Esta categoría sigue siendo la principal causa de pérdidas financieras. Se refiere a situaciones donde el atacante obtiene acceso ilegítimo a las credenciales de un usuario o protocolo.

* Robo de claves privadas: Acceso directo a la clave que controla los fondos, a menudo por almacenamiento inseguro.
* [Phishing](https://ethereum.org/es/security/#phishing): Técnicas de ingeniería social (webs falsas, correos) para engañar al usuario y que revele sus claves o firme transacciones maliciosas.
* Ice Phishing: Un tipo de phishing donde se engaña al usuario para que firme un permiso ("approve") que permite al atacante gastar sus tokens posteriormente.
* Compromiso de [Multisig](https://ethereum.org/es/developers/docs/smart-contracts/#multisig): Ataques dirigidos a los firmantes de una billetera multifirma, logrando el umbral necesario para ejecutar transacciones maliciosas.

### 3.2 Fallos de control de acceso

Ocurren cuando los contratos inteligentes no restringen adecuadamente quién puede ejecutar funciones sensibles.

* Privilege Escalation: Un usuario normal logra obtener permisos de administrador.
* Falta de validación: Funciones críticas (como `mint` o `withdraw`) públicas sin modificadores de acceso (ej. `onlyOwner`).
* Inicialización incorrecta: Contratos que no se inicializan correctamente, permitiendo que un atacante tome posesión ("front-run the initialization").
* Recurso: [OpenZeppelin Access Control](https://docs.openzeppelin.com/contracts/4.x/access-control).

### 3.3 Ataques económicos y flashloans

Explotan la lógica financiera de los protocolos DeFi en lugar de errores de código puramente técnicos.

* [Flash Loans Attacks](https://chain.link/education/flash-loans): Uso de préstamos instantáneos (sin colateral) para manipular mercados con gran capital en una sola transacción.
* Manipulación de Gobernanza: Uso de flashloans para obtener temporalmente gran poder de voto y aprobar propuestas maliciosas.
* [Reentrancy](https://consensys.github.io/smart-contract-best-practices/attacks/reentrancy/): Un contrato malicioso llama repetidamente a una función de retiro antes de que el contrato víctima actualice su saldo.

### 3.4 Manipulación de oráculos

Los oráculos alimentan a la blockchain con datos externos (precios). Si estos datos se manipulan, el protocolo falla.

* Manipulación de precio spot: Alterar el precio de un activo en un DEX con baja liquidez para que un protocolo de préstamos crea que vale más (o menos) de lo real.
* Falta de validación de datos: Confiar en una sola fuente de datos centralizada o fácilmente manipulable.
* Solución: Uso de oráculos descentralizados como [Chainlink](https://chain.link/) o mecanismos como TWAP (Time-Weighted Average Price).

### 3.5 Fallos criptográficos y verificación

Errores en la implementación de matemáticas complejas o criptografía.

* Fallos en [ZK-proofs](https://ethereum.org/es/developers/docs/scaling/zk-rollups/): Errores en los circuitos de pruebas de conocimiento cero que permiten crear pruebas falsas.
* Signature Replay: Reutilizar una firma digital válida para ejecutar una acción múltiples veces.
* Verificación de firmas débil: Implementaciones incorrectas de `ecrecover` o validación de firmas ECDSA.

### 3.6 Infraestructura y ataques off-chain

Ataques que no ocurren en la blockchain (on-chain), sino en los sistemas tradicionales que la rodean.

* Frontend Hijacking: Hackear el servidor web o DNS de una dApp para mostrar una interfaz falsa que roba fondos (ej. ataque a Curve Finance DNS).
* Compromiso de servidores: Acceso a servidores backend que guardan claves calientes (hot wallets).
* [Bridges](https://ethereum.org/es/developers/docs/bridges/): Los puentes entre cadenas son puntos críticos ("honeypots") con gran liquidez y lógica compleja, frecuentemente atacados.

## 4. Tendencias observadas en 2024

* El compromiso de claves privadas supera el 50% del valor total robado.
* Los ataques de permisos y lógica interna siguen creciendo.
* Los exploits DeFi evolucionan hacia vectores económicos complejos.
* Mayor foco en ZK-proofs y nuevas superficies de ataque.
* Bridges y cross-chain continúan como puntos frágiles.

---
