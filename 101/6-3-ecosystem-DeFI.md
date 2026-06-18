# El ecosistema de aplicaciones para las finanzas: DeFi

## Acerca de

Esta introducción a DeFi tiene como objetivo orientar y guiar hacia otros artículos de interés, priorizando la claridad de los conceptos clave y ofreciendo una visión general. No pretende detallar exhaustivamente cada aspecto, sino aclarar las motivaciones y puntos fundamentales.

DeFi es un campo complejo y extenso, que merece su propio estudio y laboratorio de práctica, así que no te preocupes si quedan temas por profundizar.

Aunque podría parecer que DeFi debería abordarse más adelante, en un anexo o en otra fase del proyecto, lo cierto es que en Web3 la rentabilidad es un aspecto fundamental: cada rol suele ser doble —fundador e inversor, productor e inversor, usuario e inversor—. Por eso es necesario comprender desde el principio los conceptos fundamentales que veremos a continuación, ya que el papel del inversor es la piedra angular de Web3.

## ¿Que es [DeFi](https://ethereum.org/es/defi/)?

<img src="./assets/DeFi.png" alt="ecosystem" width="400">

DeFi constituye la capa económica del ecosistema Web3, orientada a crear y gestionar servicios financieros sin intermediarios. En su forma más básica incluye [préstamos con colateral](https://ethereum.org/es/defi/#lending) —donde se deposita un activo para obtener liquidez sin venderlo, como en [Aave](https://aave.com/) o [Compound](https://compound.finance/)—, ahorro mediante [staking](https://ethereum.org/es/staking/) y [liquid staking](https://www.binance.com/es/academy/glossary/liquid-staking) (que permite mantener liquidez mientras se genera rendimiento), e [intercambio descentralizado](https://ethereum.org/es/defi/#swaps) de tokens a través de [liquidity pools](https://finematics.com/liquidity-pools-explained/) y [AMMs](https://academy.bit2me.com/que-es-automated-market-maker-amm/) habitualmente.

Sobre esa base, DeFi ofrece formas de poner el capital a trabajar de manera más activa. La más popular es el [Yield Farming](https://finematics.com/yield-farming-explained/): el capital deja de estar quieto y se mueve entre protocolos buscando el rendimiento más alto en cada momento.

en yiLo que persigue el farmer es retorno —medido en dólares o en el activo de referencia que le interese—, no un papel concreto dentro del protocolo. Ese rendimiento llega casi siempre como un token que el propio protocolo emite para atraer liquidez, y se complementa a veces con comisiones de trading, puntos pre-token o intereses de préstamo. Cuando ese token además otorga gobernanza —como [UNI](https://uniswap.org/blog/uni) en [Uniswap](https://uniswap.org/) o [COMP](https://compound.finance/governance/comp) en Compound—, la mayoría de los farmers no lo conserva para votar sino que lo vende por el activo que sí perseguía: el derecho a gobernar es, en la práctica, un subproducto. El problema operativo es que perseguir el mejor rendimiento exige saltar entre protocolos, leer condiciones y reequilibrar constantemente, y eso consume tiempo y gas. Para resolver esa carga surgieron las [bóvedas curadas](https://docs.stakedao.org/curated-vaults) (*curated vaults*): contratos inteligentes que agrupan el capital de varios usuarios y ejecutan estrategias de Yield Farming de forma automática, repartiendo las ganancias de forma proporcional.

Para quienes buscan más sofisticación, DeFi también ofrece [activos sintéticos](https://www.bitstamp.net/es/learn/blockchain/what-are-synthetic-assets/) —tokens que replican el precio de un activo real sin necesidad de tenerlo— y futuros perpetuos en exchanges descentralizados como [dYdX](https://dydx.exchange/), que permiten especular sobre precios con apalancamiento.

Otro mecanismo relevante es el [restaking](https://medium.com/@laureengeller0403/restaking-explained-is-shared-security-the-future-of-web3-or-a-systemic-risk-2a83a3dcc543): en lugar de dejar el capital bloqueado en staking sin otro uso, protocolos como [EigenLayer](https://www.eigenlayer.xyz/) permiten reutilizarlo para asegurar otras redes al mismo tiempo, multiplicando su utilidad.

Finalmente, la tokenización de activos del mundo real ([RWA](https://www.coinbase.com/es-es/learn/crypto-basics/what-are-real-world-assets-rwa)) lleva al ecosistema on-chain activos como bonos, inmuebles o deuda privada, abriendo DeFi a capital que antes solo existía en las finanzas tradicionales.

Es un espacio abierto, en lo bueno y en lo malo, porque DeFi es permisionless; es decir, **cualquiera, en cualquier lugar y en cualquier momento**, con una wallet puede participar. No hay que cumplir requisitos previos, ni pedir permiso, y al ser descentralizado, ni siquiera es necesario proporcionar datos personales.

Pero este permisionless tiene otra cara igual de importante: cualquiera puede crear un protocolo financiero, publicarlo en la blockchain y ponerlo a disposición del mundo sin pedir autorización a nadie. Las DApps lo implementan, los usuarios lo adoptan, y muchas veces lo hacen atraídos por la rentabilidad que promete. Confían en el código, confían en la comunidad, pero ese ecosistema abierto no está exento de errores, vulnerabilidades o incluso malas intenciones. La libertad de crear y usar sin permiso es exactamente la misma que hace posible tanto la innovación como el riesgo.

Ya sabemos qué hace DeFi; la siguiente pregunta es sobre qué opera y quién lo hace. El sujeto de DeFi son los activos digitales: ETH, stablecoins, tokens envueltos, sintéticos, LP tokens y activos del mundo real tokenizados. Sin ellos no hay préstamos, no hay swaps ni liquidez. Puedes profundizar en cada tipo y su papel en [los activos digitales en DeFi](../ecosystem/DeFi/defi-assets.md). Y esos activos los mueven actores muy distintos: desde usuarios individuales que aportan liquidez o piden prestado, hasta bots que arbitran y liquidan en milisegundos, DAOs que gestionan capital colectivo y equipos que construyen los protocolos. Conocer sus roles y motivaciones ayuda a leer el ecosistema con mucha más claridad, y puedes hacerlo en [los actores del ecosistema DeFi](../ecosystem/DeFi/defi-actors.md).

El ecosistema DeFi evoluciona rápidamente y hay novedades que merecen un análisis más detallado. Para una visión actualizada de los protocolos, categorías y tendencias relevantes en 2026, puedes consultar [el mapa del ecosistema DeFi](../deep-dive/defi/defi-ecosystem-map-2026.md).

## Evolución de DeFi en capas

<img src="./assets_5/defiStack.png" alt="ecosystem" width="400">

En Web3 todo es modular y en capas, siguiendo el principio de composabilidad, y DeFi no iba a ser la excepción.

Se puede interpretar que DeFi se construye sobre capas, denominadas DeFi 1.0, 2.0, 3.0… que pueden confundirse con versiones, pero en realidad forman un stack de capas tecnológicas, donde cada una resuelve un problema distinto.

La primera capa, [DeFi 1.0](https://web3.bitget.com/en/academy/what-are-DeFi-1-0-2-0-and-3-0) (2017-2020), establece los cimientos del intercambio, los préstamos y la provisión de liquidez sin intermediarios. Ejemplos fundacionales incluyen [MakerDAO](https://makerdao.com/) (stablecoin descentralizada DAI respaldada por colateral), [Uniswap](https://uniswap.org/) (AMM para intercambio de tokens), [Compound](https://compound.finance/) (lending/borrowing algorítmico con tokens cToken) y [Aave](https://aave.com/) (lending con innovaciones como flash loans). Estos protocolos establecieron los patrones fundamentales que el resto del ecosistema adoptó.

Hacia el final de esta etapa surgió el Yield farming, un modelo de incentivos que impulsó la adopción de estos protocolos y marcó la transición hacia DeFi 2.0. La interfaz web de sus DApps ofrece herramientas para que el usuario tesorero gestione manualmente. Su interoperabilidad es básica: sus contratos inteligentes son *composables*, permitiendo que otros protocolos interactuaran directamente con ellos en la blockchain. Su principal desafío es la baja eficiencia de capital y la [fragmentación de la liquidez](https://es.cointelegraph.com/news/liquidity-fragmentation-in-DeFi-a-systemic-problem) entre múltiples plataformas.

Sobre los cimientos de DeFi 1.0 —donde proyectos como Yearn Finance (Finanzas del Anhelo) introdujeron la automatización del rendimiento— surge [DeFi 2.0](https://changelly.com/blog/what-is-DeFi-2-0/) (2021-2022) como una evolución orientada a la sostenibilidad y la **automatización**. Su innovación clave es la liquidez propiedad del protocolo [(Protocol-Owned Liquidity, POL)](https://www.cube.exchange/es/what-is/protocol-owned-liquidity), en lugar del usuario: un modelo que busca independencia frente a los incentivos externos y garantiza una gestión más autónoma y estable del capital.

Ejemplos destacados incluyen [Olympus DAO](https://www.olympusdao.finance/) (bonding y protocol-owned liquidity), [Tokemak](https://www.tokemak.xyz/) (gestión descentralizada de liquidez) y [Convex](https://www.convexfinance.com/) (optimización de rendimientos en Curve). Aunque muchos de estos experimentos fallaron o no cumplieron expectativas, introdujeron conceptos valiosos sobre diseño de incentivos sostenibles.

Un caso emblemático de esta transición fueron las **Curve Wars** (2021-2022): una competencia entre protocolos por acumular poder de voto sobre las emisiones de liquidez de Curve Finance, donde quien controlaba más veCRV dirigía más recompensas hacia sus propias pools. Ilustra perfectamente cómo DeFi 2.0 busca controlar la liquidez mediante gobernanza, aunque también reveló los riesgos de concentración del poder de voto cuando múltiples capas de protocolos compiten por el mismo recurso estratégico.

La interfaz web de las DApps permite al usuario inversor o de gobernanza ajustar parámetros estratégicos de la tesorería, aunque con mayor complejidad operativa y riesgo de seguridad, pero permitiendo difuminar el problema de fragmentación de liquidez mediante protocolos automatizados.

La tercera capa, [DeFi 3.0](https://medium.com/@web3./DeFi-3-0-the-evolution-of-decentralized-finance-and-the-emergence-of-the-crypto-legos-and-ai-775b585bd65) (2023-presente), se centra en eficiencia de capital, interoperabilidad cross-chain, productos más sofisticados (derivados, opciones, structured products), mejor experiencia de usuario y cumplimiento regulatorio opcional.

Su pilar técnico es la agregación y orquestación [cross-chain](https://www.coinbase.com/es-es/learn/crypto-glossary/whats-the-difference-between-cross-chain-and-multichain): reunir diferentes protocolos de DeFi 1.0 y 2.0 para ofrecer las mejores condiciones posibles, incluso entre distintas redes. El patrón de agregar liquidez no es nuevo en DeFi: los primeros agregadores de DEX, como [1inch](https://1inch.io/) a partir de 2019, ya resolvían el problema de la liquidez fragmentada dentro de una sola cadena, consultando múltiples pools simultáneamente y enrutando la orden por el camino más eficiente. DeFi 3.0 extiende esa misma lógica al plano cross-chain: en lugar de agregar pools dentro de una red, se agregan cadenas enteras y los puentes que las conectan. Los [agregadores cross-chain](https://li.fi/knowledge-hub/crypto-aggregators/) como [LI.FI](https://li.fi/) o [Socket](https://socket.tech/) son la expresión directa de esa evolución: permiten que una operación cruce puentes, consolide liquidez de distintas redes y ejecute en la cadena destino en un solo paso. Este servicio se ofrece como infraestructura de abstracción de liquidez multi-chain sobre la que otros protocolos construyen. Además, esta capa integra Activos del Mundo Real (RWA) como vía de escalabilidad, ampliando el alcance más allá del ecosistema puramente cripto, y abre oportunidades como el Farming as a Service (FaaS), donde la orquestación cross-chain optimiza estrategias de yield farming a escala global.

Dentro de esta misma etapa emerge un cambio arquitectónico relevante: las arquitecturas basadas en *intents* (intenciones declarativas). En el modelo de agregación clásico el usuario especifica cómo ejecutar la transacción —ruta, slippage máximo, pool— y el protocolo la encamina por el mejor camino disponible. En el modelo de intents, el usuario solo declara el resultado deseado ("quiero X de este token pagando como máximo Y"), y agentes especializados llamados *solvers* compiten entre sí para ejecutar esa intención de la forma más eficiente. [UniswapX](https://uniswap.org/whitepaper/uniswapX.pdf) y [CoW Protocol](https://cow.fi/) son implementaciones características de este modelo, y algunos de los agregadores clásicos han migrado también su ejecución principal hacia esta arquitectura. La razón es que resuelve un problema que la agregación clásica no eliminaba del todo: el MEV, el valor que bots externos extraen reordenando o interceptando transacciones. Con los solvers compitiendo para ofrecer el mejor precio al usuario, ese valor revierte al usuario en lugar de ser capturado por terceros.

Junto a los agregadores y los intents, existe una tercera aproximación al problema cross-chain que merece distinguirse: las redes de liquidez nativa entre cadenas. Los agregadores como LI.FI dependen de puentes externos para mover activos y, por tanto, del riesgo que esos puentes introduzcan. Los protocolos de esta tercera categoría, en cambio, no enrutan a través de infraestructura ajena sino que crean sus propias pools de liquidez para cada par de cadenas, usando un activo nativo del propio protocolo como capa de liquidación. [THORChain](https://thorchain.org/) es el ejemplo más representativo: cualquier swap entre Bitcoin, Ethereum u otros activos nativos pasa por pools respaldadas por RUNE, sin necesidad de versiones envueltas ni de confiar en un puente externo. El resultado es un intercambio cross-chain donde el protocolo es al mismo tiempo la infraestructura de liquidez y el mecanismo de ejecución.

Mirando al futuro, una posible capa DeFi 4.0 tendría como objetivo la adopción masiva mediante la completa abstracción de la tecnología, transformando la interacción en una experiencia simple e intuitiva para el usuario final. Su interoperabilidad sería perfecta y omnipresente, integrando no solo protocolos DeFi, sino también el sistema financiero tradicional y otras plataformas digitales, haciendo que la blockchain subyacente sea prácticamente invisible.

Sin perder perspectiva en el resto de capas, como fundadores de proyectos sobre todo nos centraremos en la capa 1.0 que es donde crearemos liquidez en un proyecto para el mercado secundario y previsiblemente en la 2.0 para automatizar.

---

🔴 Rojo = Emisión e incentivos

Liquidity mining.
Recompensas.
Inflación del token.
Subsidios.
Bootstrapping de liquidez.

🟢 Verde = Generación de valor

Comisiones de trading.
Intereses de préstamos.
Ingresos del protocolo.
Cash flow real.
Actividad económica.

🟡 Dorado = Especulación

Trading.
Narrativas.
Memecoins.
Apuestas sobre crecimiento.
Valoraciones futuras.

🔵 Azul = Seguridad y confianza

Staking.
Validadores.
Auditorías.
Colateralización.
Gestión de riesgo.
Oráculos.

🟣 Morado = Eficiencia del sistema

Arbitrajistas.
Liquidadores.
MEV "útil".
Market makers.
Solvers.
Routers.