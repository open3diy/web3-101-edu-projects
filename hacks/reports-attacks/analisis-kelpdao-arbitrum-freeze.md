# El hack de KelpDAO y el congelamiento de Arbitrum: técnica, tesorerías y la grieta de la descentralización

> Este documento no es un reporte de incidente más. El qué pasó está en cinco titulares. Lo interesante es **qué dejó al descubierto**: cómo se comportan las tesorerías DeFi bajo estrés, por qué los fondos robados acaban en L2s y, sobre todo, qué dice de Arbitrum (y del sector) que su Security Council congelara $71M sin que nadie supiera con precisión cuántas firmas hicieron falta.
>
> Análisis complementario en vídeo: [El robo que acabó con el experimento de cripto](https://www.youtube.com/watch?v=pFJR31YWe-E&t=252s) y cobertura original en [TradingView/NewsBTC](https://es.tradingview.com/news/newsbtc:b1d26fd4f09cd:0/).

---

## 1. Resumen ejecutivo

* **Fecha del exploit**: 18-19 de abril de 2026.
* **Protocolo objetivo**: [KelpDAO](https://kelpdao.xyz/) (LRT, Liquid Restaking Token rsETH) sobre la mensajería de [LayerZero](https://layerzero.network/).
* **Monto robado**: ~116,500 rsETH ≈ **$292M** al momento del ataque.
* **Vector primario**: compromiso de la **DVN (Decentralized Verifier Network)** de LayerZero — un setup `1-of-1` con verificadores internos comprometidos + DDoS a verificadores externos.
* **Acción derivada**: el atacante usó rsETH no respaldado como colateral en **Aave V3** para tomar prestado **WETH y stables reales**.
* **Daño sistémico**: ~25% del TVL de Aave salió en 72h (de ~$45B a ~$30B). Tasas USDT/USDC saltaron de ~3.4% a 14%.
* **Reacción Arbitrum**: el **Security Council** congeló **30,766 ETH (~$71M)** consolidados en una dirección controlada por el atacante.
* **Reacción coalición DeFi**: 25 de abril, **AAVE, KelpDAO, LayerZero, EtherFi y Compound** presentan una **Constitutional AIP** pidiendo liberar los ETH a un Gnosis Safe `2-of-3` co-controlado por Aave, KelpDAO y Certora. Timeline estimado: ~49 días.
* **Atribución**: LayerZero atribuye preliminarmente el ataque a **Lazarus Group / TraderTraitor** (RPDC).

## 2. Análisis técnico: el bridge no fue lo que falló, fueron sus ojos

KelpDAO no perdió fondos por un bug en su contrato. Perdió fondos porque la **capa que verifica que algo pasó al otro lado de la cadena** estaba operativamente centralizada.

### 2.1 Qué es una DVN y por qué importa

LayerZero V2 separa la mensajería en tres roles: **executor**, **DVN** y **endpoint**. La DVN es el oráculo que confirma "este evento ocurrió en la cadena origen". El protocolo permite configurar `N-of-M` DVNs, idealmente independientes y diversas.

**KelpDAO operaba en `1-of-1` con la DVN gestionada por LayerZero Labs**. Una sola fuente de verdad. Un solo punto de fallo.

### 2.2 Lo que comprometió el atacante

Según la [reconstrucción de Chainalysis](https://www.chainalysis.com/blog/kelpdao-bridge-exploit-april-2026/):

1. **Recon**: el atacante obtuvo la lista de RPCs que la DVN consultaba.
2. **Acceso a dos nodos internos** independientes en clusters separados (probable supply chain o credenciales filtradas, consistente con el TTP de Lazarus).
3. **Swap de software**: los nodos comprometidos seguían respondiendo verídicamente a *otros* sistemas (para no levantar alertas), pero a la DVN le reportaban **quemas de rsETH inexistentes** en la cadena origen.
4. **DDoS contra los nodos externos** que podrían haber detectado la divergencia.
5. La DVN aprueba el "mensaje": en la cadena destino se acuñan rsETH **sin colateral** que los respalde.
6. Esos rsETH se depositan como colateral en Aave V3. Se piden prestados WETH y stables reales. Cuando el sistema descubre que el colateral no vale nada, la deuda ya está fuera.

### 2.3 La lectura

* El bug no es de Solidity. El bug es **organizacional**: la idea de "verificador descentralizado" se diseñó como `N-of-M`, pero se desplegó como `1-of-1`. El parámetro era responsabilidad del integrador (KelpDAO), no de LayerZero.
* Es exactamente el patrón que [SlowMist](https://hacked.slowmist.io/) y [CertiK](https://www.certik.com/resources) llevan dos años marcando: la mayor parte de las pérdidas catastróficas no vienen de exploits novedosos, vienen de **configuraciones por defecto inseguras** en infraestructura compartida.
* El reparto de culpas ya empezó: KelpDAO acusa a LayerZero por sus nodos comprometidos; LayerZero responde que la elección `1-of-1` fue de KelpDAO. Ambas tienen parte de razón, y ninguna tendrá toda la culpa cuando llegue la coordinación legal.

## 3. ¿Por qué los fondos terminaron en Arbitrum (y en L2s en general)?

No es accidental. Es la consecuencia directa de tres dinámicas que la industria viene arrastrando:

### 3.1 Liquidez profunda + comisiones bajas = lavadero más eficiente

Para un atacante que necesita **fragmentar, swapear y consolidar** $292M sin slippage destructivo, mainnet es caro y lento. **Arbitrum, Base y Optimism ofrecen pools profundos en USDC/ETH/WBTC con comisiones de céntimos**. Lo que en mainnet costaría seis cifras en gas en una semana, en L2 cuesta tres.

### 3.2 Finalidad y bridge nativo flexible

Los fondos pueden moverse entre L2 y L1 con costes mínimos, esperar el desafío de 7 días si interesa, o salir más rápido vía bridges third-party. Es óptimo para un atacante que *quiere ganar tiempo* mientras el blanqueo se organiza.

### 3.3 Falsa sensación de menor vigilancia

Hasta hace poco, la **infraestructura forense** de los grandes (Chainalysis, TRM, Elliptic) tenía cobertura asimétrica: muy buena en mainnet, irregular en L2s emergentes. Esta brecha se está cerrando, y este caso lo demuestra: la consolidación en Arbitrum fue **rastreada y actuada** en menos de 72h.

### 3.4 La paradoja

El atacante eligió Arbitrum por las mismas tres razones que un usuario legítimo: **es más rápido, más barato y más líquido**. Y por la misma razón por la que el ecosistema lo eligió: **Arbitrum tiene un Security Council**. La eficiencia y el control conviven en la misma infraestructura. Cuando el atacante optimiza, el defensor también puede.

## 4. La reacción de Arbitrum: "freeze" sin botón de freeze

### 4.1 Lo que técnicamente hizo el Security Council

Arbitrum no tiene una función `freezeAddress(addr)`. Lo que hizo el Security Council fue **usar sus poderes privilegiados sobre los contratos del protocolo para mover los 30,766 ETH desde la dirección controlada por el atacante a una "ownerless wallet"** — una dirección sin clave privada conocida, efectivamente un agujero negro hasta que la DAO decida lo contrario.

* No hay una blacklist on-chain como Tether.
* No hay un mecanismo de "censura selectiva" del secuenciador.
* Sí hay **upgradeability administrativa** sobre los contratos del rollup, y el Security Council la ejerció.

Esto importa porque **es un mecanismo distinto de los que normalmente se discuten** en el debate descentralización: no es censura del secuenciador, no es validador rechazando bloques, no es admin del token bloqueando saldos. Es **gobierno de emergencia del protocolo** sustituyendo el estado.

### 4.2 ¿Cuántos firmantes hicieron falta?

El número exacto y el quórum no se publicaron en el momento. Lo que sí se sabe:

* El [Security Council](https://docs.arbitrum.io/how-arbitrum-works/state-transition-function/modified-geth-on-arbitrum) de Arbitrum tiene 12 miembros divididos en 2 cohortes de 6, con quórum de 9-of-12 para acciones de emergencia y 7-of-12 para no emergencia.
* La acción se ejecutó "con input de las autoridades sobre la identidad del atacante".
* No hubo voto previo de la DAO. El Council actuó, y *después* la coalición de protocolos pidió legitimación retroactiva vía Constitutional AIP.

### 4.3 La incomodidad

Esto **funciona**. Es probablemente lo correcto. Y al mismo tiempo es un gobierno on-chain ejecutando una acción de policía sin proceso público previo, con asistencia de fuerzas del orden de jurisdicción no especificada, sobre una cadena que **se vende como descentralizada**. Las dos frases anteriores son simultáneamente verdad.

## 5. Cómo actúan las tesorerías DeFi bajo estrés sistémico

El caso es un manual de cómo los protocolos articulan respuestas cuando el blast radius supera lo que su risk module puede absorber.

### 5.1 Aave: defensa en silencio, contabilidad en público

* Los smart contracts de Aave **no fueron comprometidos**. El daño es deuda mala generada por colateral falso aceptado.
* Aave no detuvo el protocolo, no usó el Safety Module todavía, no socializó pérdidas. Lo que hizo fue **dejar que las tasas de interés hicieran su trabajo**: USDT/USDC subieron a 14% APR, lo que **incentivó depósitos** y **desincentivó nuevos préstamos** durante la crisis aguda.
* En paralelo, su risk team (Chaos Labs, Gauntlet, BGD Labs) coordinó con KelpDAO el cierre de mercados rsETH y la propuesta conjunta a Arbitrum.
* La fuga de TVL ($15B en 3 días) **no es un fallo del protocolo, es un fallo de confianza en el ecosistema circundante**.

### 5.2 KelpDAO: confesión, contención, coordinación

* Comunicación pública casi inmediata. El equipo no negó ni minimizó.
* Pausa de minteo y redenciones en la mayoría de cadenas mientras se reconstruía la verificación.
* Co-firma de la Constitutional AIP: en lugar de pelear unilateralmente por los ETH congelados, **se metió en una estructura compartida** (`2-of-3 Gnosis Safe` con Aave y Certora). Es la jugada políticamente correcta: comparte la legitimidad.

### 5.3 Las tesorerías como "última instancia"

Lo que este caso confirma es que **las tesorerías de los grandes protocolos DeFi están funcionando, de facto, como bancos centrales del subsistema**. Son los únicos balance sheets con el tamaño y la legitimidad necesarios para:

* Coordinar rescates parciales.
* Pagar auditorías y forense post-incidente.
* Servir de contraparte para acuerdos legales y de recuperación.
* Custodiar fondos recuperados durante meses mientras la AIP se ejecuta.

Es un rol que nadie acordó formalmente y que tampoco está bien capitalizado para soportar. Si en lugar de un evento aislado fuesen tres simultáneos, el sistema no cubriría.

## 6. La grieta: descentralización útil vs descentralización predicada

Aquí va lo que no aparece en los reportes técnicos pero define el momento.

### 6.1 La incomodidad estructural

Charles Guillemet (CTO de Ledger) lo dijo sin rodeos: el congelamiento de Arbitrum es un caso de **"claves controladas por humanos sobrescribiendo el comportamiento on-chain"**. Su lectura es que la mayoría de rollups importantes están en **etapas tempranas de descentralización con partes confiables influyentes**, y que el stack DeFi opera con **"grados variables de permisología"** a pesar del discurso.

Tiene razón. Y la respuesta del ecosistema —"sí, pero esta vez era Lazarus, así que está bien"— es exactamente el problema. La excepción justificada es el principio de la regla.

### 6.2 La paradoja Arbitrum

Arbitrum ha hecho del relato de la descentralización una de sus banderas comerciales: stages de Vitalik, gobernanza de DAO, secuenciador descentralizado en roadmap, BoLD para validación. Pero el **Security Council es un poder extraordinario muy real**, con quórum bajo, y con capacidad para **reescribir el estado del rollup** en supuestos de emergencia que ellos mismos definen.

Cuando el Security Council congela $71M de un atacante norcoreano:

* Para el usuario perjudicado, es maravilloso.
* Para el discurso de "no necesitas confiar en nadie", es **una contradicción operativa**.

No es que Arbitrum no crea en la descentralización. Es que **cree en una versión de la descentralización que admite excepciones cuando son convenientes**, y no ha sido del todo honesta marketinizando esa segunda parte. El día que el Council use el mismo mecanismo en un caso *no* tan limpio —digamos, presión regulatoria sobre un mixer, o una decisión política sobre fondos rastreados a un país sancionado pero usados por refugiados— el aplauso será mucho menor.

### 6.3 La comparación con Tether (y por qué no es la misma)

El mismo mes, Tether congeló **$344M USDT** coordinándose con OFAC. Justin Sun aprovechó para anunciar que TRON era "la blockchain más descentralizada", y días después Tether (que opera mayoritariamente en TRON) hizo otro freeze. El propio anuncio se autodesmintió.

Pero **mezclar Tether y Arbitrum es un error analítico**:

* **Tether** es un emisor centralizado de un activo respaldado por reservas off-chain. La capacidad de blacklist está en el contrato, documentada, y su justificación es regulatoria. Es centralización **por diseño y por ley**.
* **Arbitrum** es un rollup que afirma converger hacia "stage 2" de descentralización. Su Security Council es **transitorio en la teoría**, pero indistinguible en la práctica de un poder permanente mientras no haya un mecanismo confiable de retirada.

La diferencia importa porque marca dónde ponemos el listón crítico. Tether nunca prometió no congelar. Arbitrum sí ha prometido (en horizonte) un mundo sin esta clase de poderes. La crítica no es por usar el poder hoy: es por la **distancia entre el roadmap predicado y el comportamiento real**.

### 6.4 Cómo se daña la confianza, exactamente

La confianza no se daña uniformemente. Se fragmenta:

* **Usuario retail individual**: gana confianza. "Si me hackean, hay alguien que puede ayudarme". Es un cambio enorme respecto a la doctrina cypherpunk original.
* **Usuario builder / dev senior**: pierde confianza. Si el rollup puede reescribir estado, mi contrato no es soberano sobre su propio almacenamiento. Mi modelo de seguridad incluye un actor más, no documentado en mi código.
* **Tesorerías y DAOs grandes**: ganan confianza pragmática. Tienen un canal de escalado para emergencias.
* **Inversores institucionales tradfi**: ganan confianza. La existencia de un mecanismo de rescate hace el activo más asegurable y más invertible bajo marcos regulatorios convencionales.
* **Atacantes sofisticados**: ajustan su comportamiento. La próxima vez no consolidan en Arbitrum, fragmentan en 30 cadenas con menos coordinación posible.
* **Actores políticamente molestos para alguien**: pierden confianza. Si el Council puede actuar coordinado con "autoridades", la cuestión es **qué autoridades, en qué jurisdicción, bajo qué proceso**.

La gran pregunta no es "¿está bien o mal el freeze?". Es **"¿quién controla, exactamente, el botón rojo y bajo qué reglas verificables?"**. Hoy, en Arbitrum, no hay una respuesta pública satisfactoria.

## 7. ¿Y si el futuro es CeFi (o "SiFi")?

La tesis más incómoda que se desprende del [vídeo](https://www.youtube.com/watch?v=pFJR31YWe-E&t=252s) es esta: el ecosistema dejará de ser oficialmente DeFi en los próximos meses y años, y se convertirá en **CeFi** —Finanzas Centralizadas— o, más precisamente, en **"SiFi"**: finanzas vigiladas, construidas sobre plataformas custodias como Coinbase y operadas con la participación directa de Morgan Stanley, Goldman Sachs y el resto del establishment bancario.

No es una predicción descabellada. Es lo que ya está pasando, y el caso KelpDAO/Arbitrum lo acelera.

### 7.1 La evidencia que ya está sobre la mesa

* **Custodia institucional**: la mayoría del flujo nuevo de ETH y BTC en 2025 entra vía ETFs (BlackRock, Fidelity) y mesas custodias (Coinbase Prime, Anchorage). El "self-custody" sigue siendo posible, pero deja de ser el camino por defecto.
* **Settlement on-chain, ejecución off-chain**: el patrón emergente —RWAs, tokenized treasuries, repos tokenizados— usa la blockchain como capa de liquidación, pero la lógica financiera, el KYC, el compliance y la última milla de control están en bases de datos centralizadas.
* **L2s como "appchains de instituciones"**: Base (Coinbase) tiene un secuenciador único operado por Coinbase. Es funcionalmente un sidechain con marketing de rollup. Y es enorme. Si el modelo "L2 institucional con secuenciador propio" se generaliza, el destino natural es **una blockchain pública usada como rieles para infraestructura privada**.
* **El propio freeze de Arbitrum**: cada vez que un Security Council coordina con autoridades, el sector demuestra a los reguladores que el control existe. Y los reguladores aprenden que pueden pedirlo.

### 7.2 Por qué KelpDAO es un punto de inflexión narrativo

El argumento DeFi original era: *"no necesitamos confiar en intermediarios porque el código es la ley y la red no puede revertir nada"*. KelpDAO rompe los tres pedazos a la vez:

* **El código no fue la ley**: la verificación off-chain (DVN) se compromete y el contrato acepta minteo no respaldado.
* **Los intermediarios sí eran necesarios**: LayerZero Labs operaba la DVN, KelpDAO la configuró así, y ambos son los puntos de fallo.
* **La red sí pudo revertir**: el Security Council de Arbitrum movió 30,766 ETH a una wallet sin clave.

Cada uno de estos hechos, por separado, ya era discutible en 2024. Los tres juntos, en un único incidente que recorrió portadas durante una semana, **deslegitiman pública y simultáneamente** las tres premisas fundacionales. Es difícil reconstruir un relato "puro" de DeFi después de esto.

### 7.3 El argumento a favor del giro CeFi/SiFi

* **Recuperabilidad**: en el mundo CeFi/SiFi, un hack como el de KelpDAO se trata como un fraude bancario clásico. Hay seguro, hay subrogación legal, hay procesos de recuperación. Hay **a quién demandar**.
* **Adopción**: el 99% del capital institucional del mundo no entrará nunca en un sistema sin compliance, sin audit trails y sin "phone numbers a los que llamar". Si cripto quiere ese capital, tiene que parecerse a lo que ese capital reconoce.
* **Estabilidad sistémica**: bancos centrales y reguladores no van a permitir que la próxima crisis financiera empiece en un protocolo DeFi opaco. La presión regulatoria empuja hacia balance sheets identificables.
* **Usabilidad**: para 99% de los usuarios, "tu llave, tu cripto" es un meme aterrador, no una bandera de libertad. Custodios profesionales son, sociológicamente, lo que la gente quiere.

Visto así, **CeFi/SiFi no es una traición a cripto: es la culminación lógica de una infraestructura de liquidación neutral siendo absorbida por los actores con balance, escala y legitimidad legal**.

### 7.4 El argumento en contra

* **Si todo el stack converge a Coinbase + Goldman, ¿qué problema resolvió cripto exactamente?** La promesa original era *desintermediar*. Si el resultado es **los mismos intermediarios usando rieles más eficientes**, lo que se ha entregado es una mejora de back-office bancario, no un nuevo paradigma. Eso no es nada despreciable —es un trillón de dólares de eficiencia—, pero no es lo que se prometió.
* **La censura selectiva escala**: una vez que existen botones rojos legítimos para Lazarus, existen para todo. Hoy un atacante norcoreano. Mañana un opositor político en una jurisdicción no-democrática que pidió "input" al Security Council. La pendiente no es resbaladiza por accidente, lo es por diseño operativo.
* **Punto único de captura regulatoria**: si la infraestructura crítica vive en 5 entidades (Coinbase, BlackRock, Tether, Circle, una L2 corporativa), capturar regulatoriamente esas 5 entidades captura el sistema. Es exactamente lo que el bitcoin original intentaba imposibilitar.
* **La red de "verdaderos creyentes" no desaparece**: Bitcoin L1, Ethereum self-custody, Monero, Nostr y similares seguirán existiendo como **opt-out cypherpunk para una minoría**. Pero esa minoría dejará de ser la cabeza del sector y pasará a ser una subcultura paralela. Como hoy lo son los partidarios de PGP frente a Gmail.

### 7.5 La síntesis incómoda

Es probable que el sector evolucione en **dos capas simultáneas y permanentes**:

1. **Una capa CeFi/SiFi mainstream** sobre rieles públicos (Ethereum L1 + L2s "stage 1") con custodios regulados, ETFs, RWAs, KYC nativo, y mecanismos de freeze normalizados. Aquí estará el dinero, los usuarios, los titulares, y la regulación. Aquí terminará operando Arbitrum.
2. **Una capa "DeFi pura" residual y autodefensiva** —Bitcoin self-custody, Ethereum no-permissioned, alguna L2 verdaderamente sin Security Council— que funcionará para casos de uso ideológicos, geopolíticamente sensibles o financieramente marginales. Será más pequeña que la mainstream, será más pobre, y será la única que pueda decir honestamente que cumple la promesa original.

La pregunta del vídeo —"¿y si el futuro es de organizaciones centrales?"— probablemente no se responde con sí o no. Se responde con: **el futuro es ambas cosas en paralelo, pero la organización central se queda con el 95% del capital y de la atención mediática**. Cripto no muere; se domestica. Y lo que llamemos "DeFi" en 2030 será, en lo esencial, fintech con liquidación on-chain.

Si esto es una victoria o una derrota depende de qué te llevó a cripto. Si entraste por eficiencia financiera, ganas. Si entraste por soberanía individual frente al Estado, **acabas de perder, y este caso es uno de los actos donde la derrota se hizo pública**.

## 8. Conclusiones operativas

Para builders, operadores y usuarios, lo aprovechable de este episodio:

1. **Auditar la configuración, no solo el código**: si tu protocolo usa LayerZero, Wormhole, Hyperlane o cualquier mensajería con `N-of-M`, **mira el M efectivo, no el M posible**. Un `1-of-1` por defecto es deuda existencial.
2. **Las tesorerías necesitan playbooks de crisis**, no solo políticas de inversión. Coordinar AIPs de emergencia en 5 días requiere relaciones, plantillas legales y firmantes pre-acordados. No se improvisa.
3. **Si dependes de un L2, mapea su Security Council** como mapearías a tu validador favorito: cuántos miembros, qué quórum, cuál es el mecanismo de remoción. No es paranoia, es modelado de amenazas básico (ver [security-principles-and-best-practices.md](../security-principles-and-best-practices.md)).
4. **El usuario debe entender que "L2" no es una marca homogénea**. La distancia entre el modelo de confianza de Arbitrum, Optimism, Base, zkSync y StarkNet es enorme y crece. El [DYOR aplicado a L2s](../web3-project-dyor-evaluation-guide.md) es ya un ejercicio diferenciado.
5. **Para protocolos LRT/LST**: el supuesto de "el colateral subyacente es real" requiere verificación on-chain redundante, no fe en el bridge. La industria lleva un año hablándolo y este caso lo cobra.
6. **La conversación pública sobre descentralización tiene que dejar de ser binaria**. La pregunta ya no es "¿es descentralizado?". Es "¿qué clase de centralización conserva, qué proceso la regula, y cómo se desmonta con el tiempo?".

## 8. Lecturas y referencias

* [Inside the $71M freeze on Arbitrum — CoinDesk](https://www.coindesk.com/tech/2026/04/22/inside-the-usd71-million-freeze-on-arbitrum-that-has-the-crypto-world-questioning-what-decentralization-really-means)
* [Arbitrum freezes $71M in ETH — CoinDesk](https://www.coindesk.com/markets/2026/04/21/arbitrum-freezes-usd71-million-in-ether-tied-to-kelp-dao-exploit)
* [Inside the KelpDAO Bridge Exploit — Chainalysis](https://www.chainalysis.com/blog/kelpdao-bridge-exploit-april-2026/)
* [Ledger CTO sobre el control en L2s — Crypto Times](https://www.cryptotimes.io/2026/04/21/ledger-cto-arbitrum-freeze-exposes-l2-control-after-kelpdao-hack/)
* [Five DeFi Protocols pide liberar 30,765 ETH — news.bitcoin.com](https://news.bitcoin.com/five-major-defi-protocols-ask-arbitrum-dao-to-free-30765-eth-locked-after-rseth-bridge-bug/)
* [Crypto Decentralization Myth — NewsBTC](https://www.newsbtc.com/news/crypto-decentralization-myth/)
* [Tether y Arbitrum congelan activos — Gizmodo](https://gizmodo.com/tether-and-arbitrum-freeze-assets-as-crypto-faces-crisis-of-purpose-2000750571)
* [Cobertura en español — TradingView/NewsBTC](https://es.tradingview.com/news/newsbtc:b1d26fd4f09cd:0/)
* [Vídeo: El robo que acabó con el experimento de cripto](https://www.youtube.com/watch?v=pFJR31YWe-E&t=252s)
* Contexto interno: [overview-attacks-2025.md](./overview-attacks-2025.md), [overview-attacks-2024.md](./overview-attacks-2024.md), [attack-vectors-overview.md](../attack-vectors-overview.md)

---
