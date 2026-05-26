# Web3 Attack Landscape 2025

## 1. Introducción

Este informe resume el panorama de ataques en Web3 durante 2025, basado en los reportes anuales y agregados públicos disponibles a fecha de cierre del año. La diferencia clave frente a [2024](./overview-attacks-2024.md) es de patrón: menos incidentes, pero significativamente más graves. El sector pasó de un goteo constante de exploits pequeños a un puñado de eventos catastróficos liderados por actores profesionales con capacidades casi estatales.

## 2. Cifras agregadas

* **~200 incidentes registrados** (caída del ~50% interanual respecto a 2024).
* **~$3.4 mil millones robados** (subida del ~55% interanual).
* **Concentración de pérdidas**: los 4 mayores incidentes representaron más del **65%** del total robado.
* **Atribución a actores estatales**: por primera vez, un único grupo (Lazarus / TraderTraitor) representa más del 45% de las pérdidas confirmadas en el año.

Fuentes principales del consolidado:

* [Chainalysis 2025 Crypto Crime Report](https://www.chainalysis.com/reports/) — datos forenses on-chain.
* [Immunefi Crypto Losses Reports](https://immunefi.com/reports/) — pérdidas DeFi.
* [SlowMist Hacked Stats](https://hacked.slowmist.io/) — archivo histórico.
* [DefiLlama Hacks](https://defillama.com/hacks) — base en tiempo real.
* [CertiK Web3 Security Reports](https://www.certik.com/resources) — auditoría y análisis.

## 3. Los grandes incidentes del año

### 3.1 Bybit — $1.5B (febrero 2025)

El mayor robo confirmado de la historia del sector cripto. Atribuido a **Lazarus Group** vía un ataque de **supply chain a Safe{Wallet}**: meses de ingeniería social a un desarrollador, inyección de JavaScript malicioso en el frontend de firma, y sustitución silenciosa de las direcciones de destino mientras los firmantes ejecutivos firmaban lo que creían que era una transacción rutinaria.

Lecciones clave:

* La cadena de confianza no termina en el contrato: el frontend de la wallet **es** parte de la superficie de ataque.
* La verificación blind-signing en multisig institucionales sigue siendo un punto ciego dramático.
* Recurso: revisar [security-principles-and-best-practices.md](../security-principles-and-best-practices.md) y [endpoint-security.md](../endpoint-security.md).

### 3.2 OG Bitcoin Whale — $330M (abril 2025)

Pérdida de 3,520 BTC mediante **deepfakes de voz** y **call center fraudulento** desde Reino Unido. El atacante no rompió ninguna criptografía: rompió la confianza humana del titular suplantando a sus asesores y dirigiéndolo a un portal falso de "verificación de cartera".

Es el primer caso público a esta escala donde el vector es enteramente IA generativa aplicada a ingeniería social.

### 3.3 Cetus Protocol (Sui) — $223M (mayo 2025)

Bug aritmético en el AMM más grande de [Sui](https://sui.io/). Un **flashloan** disparó un **overflow** en el cálculo de liquidez, permitiendo retirar mucho más de lo aportado. Los validadores de Sui **congelaron $162M** antes de que cruzaran un puente, lo que abrió por primera vez en Sui el mismo debate que años antes tuvo Ethereum con The DAO: ¿es legítimo que validadores actúen como freno de emergencia?

### 3.4 Balancer V2 — $128M (noviembre 2025)

Exploit cross-chain (Ethereum, Arbitrum, Base) basado en **errores de redondeo de precisión**. El atacante ejecutó 65+ micro-swaps para componer la deriva de redondeo, distorsionar la contabilidad de los pools y mintear LP tokens infravalorados. Es un ejemplo paradigmático de cómo los exploits económicos puros, sin "bug" tradicional, ya son una categoría madura.

### 3.5 KelpDAO / rsETH — $292M (abril 2026, listado por proximidad)

Aunque cae fuera del año fiscal 2025, el incidente de KelpDAO en abril de 2026 es la culminación de las tendencias observadas durante todo 2025: **infraestructura off-chain comprometida** (verificadores DVN de [LayerZero](https://layerzero.network/)), **acuñación no respaldada** de tokens, depósito como colateral en Aave para sacar activos reales, y consolidación de fondos en L2.

Análisis detallado en [analisis-kelpdao-arbitrum-freeze.md](./analisis-kelpdao-arbitrum-freeze.md).

## 4. Categorías de ataque en 2025

### 4.1 Compromiso de infraestructura off-chain

Categoría dominante. Bybit (Safe{Wallet}), KelpDAO (DVN de LayerZero), y varios más demuestran que **la blockchain es la parte segura del sistema**. El eslabón débil son los nodos RPC, los pipelines de despliegue, los SDK de wallets, y los servidores de los verificadores.

* Compromiso de claves privadas y seed phrases vía supply chain.
* Hijack de DNS/frontend de dApps.
* Compromiso de oráculos centralizados o de un único [DVN](https://docs.layerzero.network/v2/concepts/modular-security/security-stack-dvns).

### 4.2 Ingeniería social asistida por IA

Crecimiento explosivo. Deepfakes de voz, vídeo en llamadas Zoom, clonación de identidad de fundadores y empleados. La superficie ya no es solo "el usuario novato": son CFOs, firmantes de multisig y devs senior.

### 4.3 Exploits económicos sofisticados

Reentrancy y oracle manipulation clásicos siguen presentes, pero la frontera está en:

* **Errores de precisión y redondeo** componibles (Balancer V2).
* **Manipulación de modelos de tasa de interés** durante eventos de estrés.
* **Manipulación de tokens LRT/LST** y sus oráculos derivados.

### 4.4 Bridges y mensajería cross-chain

[Los bridges siguen siendo el honeypot estructural](https://ethereum.org/es/developers/docs/bridges/). En 2025 el patrón nuevo es atacar la **capa de verificación** del bridge (DVNs, validadores, relayers) en vez del contrato del puente en sí. KelpDAO/LayerZero es el caso de manual.

### 4.5 Fallos de control de acceso e inicialización

Persisten, sobre todo en proyectos jóvenes en L2s emergentes. Una porción no menor de los 200 incidentes son contratos sin `onlyOwner`, funciones `initialize()` reentradas, o roles de admin filtrados.

## 5. Tendencias y lecturas

* **Profesionalización del atacante**: Lazarus + grupos con presupuesto multi-mes para ingeniería social superan ampliamente al "hacker oportunista".
* **Concentración**: pocos eventos enormes, no muchos pequeños. Esto distorsiona métricas — un buen año en número de incidentes puede ser un año récord en pérdidas.
* **L2s como destino preferido del atacante**: liquidez profunda + finalidad rápida + infraestructura todavía con `Security Councils` activos. Esto ha activado un debate público sobre la **descentralización real** de los rollups (ver KelpDAO/Arbitrum).
* **Restaking y LRTs como nueva superficie crítica**: rsETH, ezETH, weETH y derivados acumulan TVL muy superior a la madurez de su infraestructura de verificación.
* **Tesorerías de protocolos como pagadores de última instancia**: Aave, Compound y otros han tenido que articular respuestas formales (propuestas constitucionales, swaps de deuda, planes de recompensas) cada vez con más frecuencia.
* **El debate "freeze vs descentralización"** se ha vuelto un tema central, no anecdótico. La industria todavía no tiene una doctrina clara.

## 6. Cómo encaja con otros materiales de este repo

* Vector técnico → [attack-vectors-overview.md](../attack-vectors-overview.md), [smart-contract-attacks.md](../smart-contract-attacks.md).
* Forense post-incidente → [blockchain-forensics-and-analysis.md](../blockchain-forensics-and-analysis.md).
* Defensa operacional → [security-operations-center-web3.md](../security-operations-center-web3.md), [secure-development-frameworks.md](../secure-development-frameworks.md).
* Evaluación previa de proyectos → [web3-project-dyor-evaluation-guide.md](../web3-project-dyor-evaluation-guide.md).

---
