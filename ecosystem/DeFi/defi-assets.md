# Los activos digitales en DeFi

## Acerca de

DeFi opera sobre activos digitales. Sin ellos no hay préstamos, no hay swaps, no hay liquidez ni rendimiento. Entender qué tipos de activos existen dentro del ecosistema DeFi, cómo funcionan y qué papel cumplen es una condición previa para comprender cualquier protocolo financiero descentralizado.

Este documento recorre los principales tipos de activos que circulan en DeFi: desde los activos nativos de las blockchains hasta los tokens sintéticos, pasando por stablecoins, tokens envueltos, tokens de liquidez y activos del mundo real tokenizados.

## Activos nativos

Los activos nativos son los tokens propios de cada red blockchain. El más relevante para DeFi es [ETH](https://ethereum.org/es/eth/), el activo nativo de Ethereum, que sirve simultáneamente como combustible para ejecutar transacciones (gas) y como colateral fundamental en multitud de protocolos. Otros ejemplos son SOL en Solana, AVAX en Avalanche o MATIC en Polygon.

Estos activos son la base sobre la que se construye todo lo demás. Su valor no depende de ningún emisor central ni de un contrato inteligente externo: están definidos directamente en el protocolo de la red. Por esta razón son considerados el activo más "puro" dentro del ecosistema, aunque su volatilidad los convierte en activos complejos para ciertos usos financieros como los pagos cotidianos o los préstamos estables.

Dentro del ecosistema DeFi, los activos nativos suelen actuar como colateral primario en protocolos de préstamo como [Aave](https://aave.com/) o [Compound](https://compound.finance/), y como par base en pools de liquidez de exchanges descentralizados como [Uniswap](https://uniswap.org/).

## Activos envueltos

Los activos envueltos ([wrapped tokens](https://www.binance.com/es/square/post/227457)) son representaciones de un activo en una blockchain distinta a la suya. El ejemplo canónico es [WBTC](https://academy.bit2me.com/que-es-wrapped-bitcoin-wbtc/) (Wrapped Bitcoin): Bitcoin envuelto en un contrato inteligente de Ethereum que emite un token ERC-20 con paridad 1:1 respecto al BTC original, permitiendo que el activo más capitalizado del mercado participe en el ecosistema DeFi de Ethereum.

El mecanismo funciona mediante custodia del activo original por parte de un custodio o de un contrato de bloqueo en la cadena origen, mientras se acuña el equivalente en la cadena destino. Este proceso introduce una dependencia del custodio o del puente que gestiona el respaldo, lo que convierte al token envuelto en un activo con riesgo de contraparte añadido respecto al original.

Los activos envueltos amplían significativamente el alcance de DeFi al incorporar liquidez de redes que no tienen capacidad nativa de smart contracts (como Bitcoin), y también facilitan la interoperabilidad entre cadenas compatibles con EVM.

## Tokens emitidos por protocolos

Cualquier equipo puede desplegar un contrato inteligente en Ethereum o en cualquier EVM compatible y emitir un token siguiendo el estándar [ERC-20](https://ethereum.org/es/developers/docs/standards/tokens/erc-20/). No hace falta permiso, no hace falta respaldo, no hace falta colateral. El token existe desde el momento en que se despliega el contrato, y desde ese momento puede intercambiarse en cualquier DEX, depositarse en pools de liquidez o usarse como colateral en protocolos que lo admitan.

Esta categoría agrupa todo lo que no encaja en las demás: tokens de utilidad que dan acceso a servicios de un protocolo, tokens de proyecto que representan una apuesta sobre el éxito de un equipo, memecoins sin utilidad declarada cuyo valor depende enteramente de la narrativa y el momentum social, y cualquier otro token que un equipo haya decidido emitir. LINK de Chainlink, MATIC de Polygon, o cualquier token de un proyecto recién lanzado en Pump.fun son ejemplos del mismo tipo de activo con perfiles de riesgo radicalmente distintos.

En DeFi estos tokens son el material de trabajo más común. La mayoría de los pares de liquidez en un DEX consisten en un token de este tipo enfrentado a una stablecoin o a un activo nativo. Su riesgo es directo: el valor depende exclusivamente de lo que el mercado esté dispuesto a pagar en cada momento, sin ningún mecanismo de respaldo que actúe como suelo. Un token puede ir a cero si el proyecto fracasa, si el equipo abandona o simplemente si el interés del mercado desaparece.

## Activos sintéticos

Los [activos sintéticos](https://www.bitstamp.net/es/learn/blockchain/what-are-synthetic-assets/) son representaciones on-chain de activos del mundo real o de otros activos digitales, creadas mediante colateralización y oráculos de precios, sin que el protocolo tenga que poseer ni custodiar el activo subyacente real.

Protocolos como [Synthetix](https://synthetix.io/) permiten emitir sintéticos que replican acciones, materias primas, divisas o índices. El mecanismo de Synthetix utiliza un pool de deuda compartido: cuando un usuario emite un sintético, asume una porción proporcional de la deuda colectiva del protocolo. Esto permite exposición a activos tradicionales sin necesidad de intermediarios ni custodios, pero introduce dos dependencias críticas: la fiabilidad de los oráculos que alimentan los precios de referencia y el riesgo de desacople entre el precio sintético y el activo real en condiciones de estrés del mercado.

Los sintéticos expanden el universo de activos accesibles en DeFi más allá del ecosistema cripto, pero su estabilidad depende de una gestión cuidadosa del colateral y de una infraestructura de oráculos robusta.

## Stablecoins: el anclaje al mundo real

<img src="./assets/stablecoins.png" alt="ecosystem" width="400">

Las stablecoins son criptoactivos diseñados para mantener una paridad estable con una moneda fiduciaria, normalmente el dólar estadounidense o el euro, funcionando como un anclaje entre el mundo digital y el mundo real. Su valor se mantiene en una relación 1:1 mediante [distintos tipos de respaldo](https://academy.binance.com/en/articles/what-is-a-stablecoin): colateral fiduciario, colateral cripto, o mecanismos algorítmicos.

Son el activo más utilizado en DeFi. Permiten realizar coberturas frente a la volatilidad del mercado, transferencias de valor estables y son el componente fundamental en las pools de liquidez. En una pool siempre hay dos tokens: uno base y otro cotizado. El token cotizado, que suele ser una stablecoin, actúa como la puerta de entrada al token base, representa el valor con el que los usuarios acceden o intercambian, y es la referencia del mercado para valorar el activo dentro de la pool.

Las principales stablecoins del mercado son [USDT](https://academy.bit2me.com/que-es-usdt-theter-criptomoneda/) y [USDC](https://academy.bit2me.com/que-es-usdc/). USDT es la más utilizada y con mayor capitalización, aunque presenta menor transparencia sobre sus reservas. USDC, emitida por Circle, es la más regulada y auditada, lo que la hace más segura desde el punto de vista institucional.

Además de las grandes stablecoins, varios ecosistemas han intentado crear sus propias monedas estables nativas para mantener la liquidez dentro de su red y reducir la dependencia del dólar. La mayoría han enfrentado problemas de estabilidad o de confianza en momentos de tensión del mercado. El caso más sonado es el de [Terra y Luna](https://www.binance.com/es/square/post/19013579135442), donde el colapso del mecanismo algorítmico de UST en 2022 destruyó decenas de miles de millones de dólares en valor en pocos días.

### El panorama regulatorio de las stablecoins

El marco regulatorio de las stablecoins está en construcción activa en las principales jurisdicciones. En EE.UU., la [GENIUS Act de 2025](https://www.fundssociety.com/es/noticias/normativa/genius-act-asi-innova-ee-uu-para-innovar-en-el-ambito-de-las-stablecoins/) ha despejado el camino regulatorio para las stablecoins de pago, exigiendo que el respaldo 1:1 esté compuesto exclusivamente por activos ultra-seguros y líquidos como Bonos del Tesoro a corto plazo. Sin embargo, el marco completo para exchanges, brokers y buena parte de la actividad DeFi sigue dependiendo de la evolución de la [CLARITY Act (H.R. 3633)](https://www.congress.gov/bill/119th-congress/house-bill/3633).

En Europa, bajo la normativa [MiCA](https://academy.bit2me.com/cuales-son-las-stablecoins-ancladas-al-euro-y-adaptadas-a-mica/), las stablecoins deben ser emitidas por entidades reguladas dentro del Espacio Económico Europeo. MiCA clasifica las stablecoins en dos categorías: los **E-Money Tokens (EMT)**:

los EMT mantienen paridad 1:1 con una moneda fiat específica (USDC, [EURD](https://academy.bit2me.com/que-es-eurod/)), y los **Asset-Reference Tokens (ART)**:

los ART están referenciados a una cesta diversificada de activos como divisas, commodities o bonos, con mayor complejidad de gestión y mayores requisitos regulatorios. La tendencia europea apunta claramente hacia las [CBDC](https://www.bde.es/wbe/es/areas-actuacion/politica-monetaria/preguntas-frecuentes/definicion-funciones-del-dinero/que-son-las-cbdc.html).

China impulsa el yuan digital o [e-CNY](https://www.binance.com/es-LA/square/post/16796254015674) como moneda digital soberana emitida por el Banco Popular. Paralelamente, Pekín utiliza a Hong Kong como laboratorio regulatorio para [experimentar con stablecoins privadas](https://es.cointelegraph.com/news/first-chinese-stablecoin-debut-race-heats-up) bajo supervisión, sin comprometer la estabilidad financiera dentro del continente.

### DAI: la stablecoin alineada con los ideales Web3

<img src="./assets_5/dai.png" alt="ecosystem" width="400">

[DAI](https://crypto.com/es/university/what-is-maker-dao-dai) es la stablecoin nativa de Web3 porque representa el ideal de descentralización funcional dentro del ecosistema DeFi: no depende de bancos, gobiernos ni empresas emisoras, sino de contratos inteligentes y gobernanza on-chain. Se emite de forma abierta mediante colateral cripto (ETH, wBTC, LSDs, etc.) y su política monetaria la define la comunidad a través de [MakerDAO](https://makerdao.com/es/).

Aunque no es una [stablecoin algorítmica](https://es.cointelegraph.com/learn/articles/stablecoins-101-what-are-crypto-stablecoins-and-how-do-they-work) pura, ya que está respaldada por activos reales bloqueados en contratos inteligentes, parte de su colateral incluye activos centralizados como USDC, lo que introduce un punto de dependencia respecto al mundo TradFi. En escenarios de fuerte caída del mercado puede sufrir presiones de liquidación. Aun así, en términos de filosofía Web3, DAI sigue siendo la referencia por su descentralización, autocustodia y transparencia total en cadena.

### Riesgos sistémicos en las stablecoins

Las stablecoins, aunque aportan estabilidad y liquidez, también introducen riesgos sistémicos que pueden afectar tanto a protocolos individuales como a todo el mercado. Su aparente solidez depende de la transparencia de las reservas, la robustez del mecanismo de paridad y la confianza de los usuarios.

El riesgo de colateral y transparencia surge del desconocimiento real sobre dónde están las reservas, qué cantidad está invertida en instrumentos de riesgo variable y cuánta está realmente disponible de forma líquida. En stablecoins centralizadas como USDT o USDC, un problema en las reservas o una congelación regulatoria puede provocar una pérdida de paridad inmediata, como ocurrió con USDC en marzo de 2023 tras la quiebra de Silicon Valley Bank. En las descentralizadas como DAI, una caída brusca del valor del colateral puede generar liquidaciones masivas que presionen la estabilidad del sistema.

El riesgo tecnológico y de gobernanza es también relevante: un fallo en el contrato inteligente, una mala parametrización o un ataque de gobernanza pueden desestabilizar la paridad. Las stablecoins algorítmicas han demostrado ser especialmente frágiles ante eventos de pánico, como ocurrió con UST de Terra en 2022.

Finalmente, el riesgo de concentración y dependencia del dólar convierte a DeFi en un ecosistema vulnerable a la política monetaria de EE.UU. Un colapso o bloqueo de una gran stablecoin como USDC o USDT afectaría simultáneamente a miles de protocolos y pools de liquidez, generando contagio inmediato. En definitiva, las stablecoins son el pilar de DeFi, pero también su mayor punto de fragilidad.

## LP tokens y receipt tokens

Cuando un usuario deposita activos en una pool de liquidez o en un protocolo de préstamo, recibe a cambio un token que representa su posición. Estos tokens, conocidos como LP tokens (Liquidity Provider tokens) o receipt tokens, son activos DeFi de segunda capa que circulan dentro del ecosistema y pueden ser utilizados como colateral en otros protocolos, componiéndose en capas.

En [Uniswap](https://uniswap.org/) v2, al depositar un par de activos en una pool se recibe un LP token que acredita la proporción del fondo aportada. En [Aave](https://aave.com/), al depositar un activo de préstamo se reciben aTokens (como aUSDC o aETH) que acumulan automáticamente los intereses generados. En [Compound](https://compound.finance/), el equivalente son los cTokens. En [Curve Finance](https://curve.fi/), los LP tokens de sus pools de stablecoins son especialmente apreciados porque pueden depositarse en protocolos como [Convex](https://www.convexfinance.com/) para amplificar el rendimiento.

Estos tokens son fundamentales para entender la composabilidad de DeFi: el capital no queda inmovilizado en un único protocolo sino que puede circular y seguir generando rendimiento en capas sucesivas, aunque esto también multiplica el riesgo de liquidación en cascada cuando el mercado cae.

## Tokens de gobernanza

Los tokens de gobernanza están en este documento porque son activos financieros reales dentro de DeFi: se intercambian en DEX, se usan como colateral en protocolos de préstamo, generan rendimiento al bloquearse y distribuyen comisiones del protocolo a sus poseedores. El voto es solo una de sus funciones; desde la perspectiva del inversor DeFi, son una forma directa de exposición al crecimiento del protocolo.

CRV de [Curve Finance](https://curve.fi/), UNI de [Uniswap](https://uniswap.org/), COMP de [Compound](https://compound.finance/) o AAVE de [Aave](https://aave.com/) son ejemplos habituales. Muchos de ellos implementan el modelo ve-token (vote-escrowed): el usuario bloquea el token durante un período determinado y, a cambio, recibe mayor poder de voto y una porción mayor de las comisiones generadas por el protocolo. Cuanto más tiempo se bloquea, mayor es el beneficio obtenido, lo que alinea los incentivos del poseedor con la salud a largo plazo del protocolo.

En la práctica, estos tokens son también la recompensa que reciben los proveedores de liquidez en Yield Farming. Cuando depositas activos en una pool, parte del rendimiento llega en forma de tokens de gobernanza del protocolo, convirtiendo al proveedor de liquidez automáticamente en copropietario con voz en las decisiones del sistema.

## Activos del mundo real tokenizados (RWA)

Los [activos del mundo real tokenizados](https://www.coinbase.com/es-es/learn/crypto-basics/what-are-real-world-assets-rwa) (Real World Assets, RWA) representan el puente entre DeFi y las finanzas tradicionales. Bonos del Tesoro de EE.UU., deuda privada, inmuebles, materias primas o acciones pueden ser tokenizados como activos on-chain y participar en protocolos DeFi: depositarse como colateral, incluirse en pools de liquidez o usarse como base para estrategias de rendimiento.

El atractivo de los RWA es su capacidad de aportar rendimiento estable y activos con menor volatilidad al ecosistema DeFi, diversificando las fuentes de colateral más allá de los activos cripto puros. Protocolos como [MakerDAO](https://makerdao.com/es/) ya incorporan deuda del Tesoro de EE.UU. como parte del respaldo de DAI. [Centrifuge](https://centrifuge.io/) y [Goldfinch](https://goldfinch.finance/) son ejemplos de protocolos especializados en llevar deuda privada on-chain.

El desafío de los RWA reside en la brecha entre el mundo on-chain y el off-chain: la tokenización no elimina el riesgo legal ni la necesidad de confiar en custodios y mecanismos de ejecución fuera de la blockchain. La transparencia y las auditorías que respaldan realmente el valor de los activos son condición indispensable para que los RWA mantengan la confianza del ecosistema.

## Liquid Staking Tokens (LST)

Cuando un usuario hace staking de ETH en la red de Ethereum, ese capital queda bloqueado y no puede utilizarse en otros protocolos. Los Liquid Staking Tokens resuelven ese problema: al depositar ETH en un protocolo de liquid staking, el usuario recibe a cambio un token que representa su posición de staking y que puede circular libremente en el ecosistema DeFi.

[Lido](https://lido.fi/) emite stETH (staked ETH), el LST más utilizado del mercado. [Rocket Pool](https://rocketpool.net/) emite rETH con un enfoque más descentralizado. [Frax Finance](https://frax.finance/) emite frxETH. Todos ellos acumulan automáticamente las recompensas de staking y pueden usarse como colateral en préstamos, como par en pools de liquidez o como base para estrategias de rendimiento adicional mediante restaking.

Los LST son uno de los activos con mayor presencia en DeFi porque combinan dos fuentes de rendimiento en un solo activo: el rendimiento base del staking de la red y el rendimiento adicional que genera su uso dentro de los protocolos. Sin embargo, introducen un riesgo específico conocido como slashing: si el validador que gestiona el staking incumple las reglas del protocolo, parte del colateral puede ser penalizado, afectando al valor del LST.

## Liquid Restaking Tokens (LRT)

Los Liquid Restaking Tokens son una capa construida encima de los LST. La idea detrás del restaking, introducida por [EigenLayer](https://www.eigenlayer.xyz/), es que el ETH ya comprometido para asegurar Ethereum puede comprometerse adicionalmente para asegurar otros servicios descentralizados —oráculos, capas de disponibilidad de datos, secuenciadores— y generar rendimiento extra a cambio. Un LRT es el token líquido que representa esa posición de restaking, de la misma forma que un LST representa la posición de staking.

[ether.fi](https://ether.fi/) emite eETH, [Renzo](https://www.renzoprotocol.com/) emite ezETH, [KelpDAO](https://kelpdao.xyz/) emite rsETH y [Puffer](https://www.puffer.fi/) emite pufETH. Todos ellos pueden usarse como colateral en protocolos de préstamo o depositarse en pools de liquidez, igual que cualquier otro activo del ecosistema.

El riesgo de los LRT es cualitativamente distinto al de los LST. Cada LRT está comprometido simultáneamente con varios servicios externos —los AVS—, y un evento de slashing en cualquiera de ellos afecta al valor del token. Entre 2024 y 2026 los LRTs se han convertido en el colateral más usado en estrategias de apalancamiento en cadena, donde el usuario deposita el LRT, pide prestadas stablecoins, compra más LRT y repite el ciclo varias veces. Esa concentración multiplica la exposición: si el LRT pierde valor de golpe, todas las posiciones apalancadas encima de él se liquidan en cascada.

## Yield-bearing stablecoins

Las yield-bearing stablecoins son stablecoins que acumulan rendimiento de forma nativa, sin necesidad de depositarlas en ningún protocolo adicional. Son la respuesta a un problema concreto: tener USDC o USDT en una wallet significa tener capital aparcado que no genera nada. Una yield-bearing stablecoin vale siempre un dólar, pero mientras la mantienes va acumulando interés automáticamente.

sDAI y sUSDS, emitidas por [Sky (MakerDAO)](https://sky.money/), acumulan los intereses que el protocolo cobra sobre las deudas activas en DAI y USDS, más el rendimiento de las treasuries tokenizadas que tiene en reserva. sUSDe, emitida por [Ethena](https://www.ethena.fi/), acumula el rendimiento del staking del ETH subyacente y el funding rate de la posición corta que mantiene el protocolo. [sFRAX](https://frax.finance/), de Frax Finance, funciona con un mecanismo similar.

La distinción importante respecto a una stablecoin normal es que son activos que trabajan solos: el rendimiento se acumula en el propio token sin que el usuario tenga que hacer nada. Eso las hace especialmente útiles para tesorerías de DAOs o para capital que va a permanecer en dólares durante semanas o meses. La contrapartida es que cada una hereda el riesgo del mecanismo que genera ese rendimiento: si el funding rate de Ethena se vuelve negativo de forma sostenida, el respaldo de sUSDe se erosiona; si el colateral de Sky falla, sDAI pierde el suelo.

---
