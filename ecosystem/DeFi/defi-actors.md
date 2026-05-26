# Los actores del ecosistema DeFi

## Acerca de

DeFi no es solo tecnología: es un ecosistema habitado por personas, organizaciones y agentes automatizados con roles distintos y a veces complementarios. Comprender quiénes participan, qué hacen y cómo interactúan es tan importante como entender los protocolos que los sostienen.

A diferencia del sistema financiero tradicional, donde los roles están definidos por regulación y jerarquía institucional, en DeFi los roles son fluidos. Una misma persona puede ser proveedor de liquidez, trader, prestamista y votante de gobernanza al mismo tiempo. Esta flexibilidad es una de las características más poderosas del ecosistema, pero también una de las más complejas de entender al principio.

Este documento describe los principales actores del ecosistema DeFi: sus motivaciones, sus herramientas y el papel que juegan en el flujo de capital.

## Los usuarios del ecosistema

La base del ecosistema DeFi son sus usuarios directos: personas que interactúan con protocolos financieros a través de sus wallets, sin necesidad de intermediarios ni de verificación de identidad.

### Los proveedores de liquidez

Los [proveedores de liquidez](https://academy.binance.com/en/articles/what-are-liquidity-pools-in-defi) (LP, del inglés *liquidity providers*) son usuarios que depositan activos en pools de liquidez de exchanges descentralizados como [Uniswap](https://uniswap.org/) o [Curve](https://curve.fi/). A cambio de bloquear su capital, reciben una comisión proporcional cada vez que alguien usa esa liquidez para intercambiar tokens.

Su rol es fundamental porque sin liquidez no hay mercado. Son quienes hacen posible que otros puedan intercambiar activos de forma instantánea y sin contrapartida directa. El LP recibe un [LP token](https://academy.binance.com/en/articles/what-are-liquidity-pool-lp-tokens) que representa su participación en el pool y que puede usar en otros protocolos, siguiendo el principio de composabilidad de DeFi.

El principal riesgo al que se enfrentan es la [pérdida impermanente](https://finematics.com/impermanent-loss-explained/) (*impermanent loss*): cuando el precio relativo de los activos depositados cambia, el LP puede terminar con menos valor que si simplemente los hubiera mantenido en su wallet. Este riesgo aumenta con la volatilidad del par.

### Los traders e intercambiadores

Los traders son quienes realizan intercambios de tokens a través de DEXes. Pueden ser usuarios individuales que quieren convertir sus activos, o entidades más sofisticadas que operan con estrategias activas.

En el modelo AMM (*Automated Market Maker*), el trader no necesita encontrar una contrapartida: el precio lo determina una fórmula matemática aplicada a las reservas del pool. Esto permite operar en cualquier momento y con cualquier par que tenga liquidez suficiente.

Los traders más activos utilizan agregadores como [1inch](https://1inch.io/) o [Paraswap](https://paraswap.io/) para encontrar la mejor ruta de ejecución entre múltiples pools y DEXes, minimizando el slippage y maximizando el valor obtenido.

### Los prestatarios y prestamistas

Los [protocolos de préstamo](https://ethereum.org/es/defi/#lending) como [Aave](https://aave.com/) o [Compound](https://compound.finance/) permiten dos roles complementarios dentro del mismo protocolo.

Los prestamistas depositan activos en el protocolo y reciben a cambio un token de recibo (aToken en Aave, cToken en Compound) que acumula intereses automáticamente. No necesitan encontrar a alguien a quien prestarle: el protocolo agrega la liquidez de todos los depositantes y la pone a disposición del mercado.

Los prestatarios depositan colateral por encima del valor del préstamo y obtienen liquidez sin necesidad de vender sus activos. Este modelo de [préstamo sobrecolateralizado](https://www.coinbase.com/es-es/learn/crypto-basics/what-is-defi) permite acceder a capital manteniendo la exposición al activo base. La lógica es que si el colateral cae por debajo de un umbral, el protocolo lo liquida automáticamente para proteger a los prestamistas.

Este esquema, que puede parecer paradójico (¿para qué pedir prestado si tienes más de lo que pides?), tiene sentido en contextos donde se quiere mantener la exposición a un activo que se espera que suba, obtener liquidez para operar, o aprovechar oportunidades en otros protocolos sin cerrar posiciones existentes.

### Los yield farmers

Los [yield farmers](https://finematics.com/yield-farming-explained/) son usuarios que mueven activamente su capital entre protocolos para maximizar el rendimiento. No tienen lealtad a un protocolo concreto: van donde los incentivos son más altos.

El yield farming surgió como mecanismo de distribución de tokens de gobernanza. Los protocolos recompensaban con sus propios tokens a quienes aportaban liquidez, creando un círculo de incentivos que disparó el crecimiento del ecosistema en 2020. Con el tiempo, los farmers desarrollaron estrategias cada vez más complejas: depositar en un protocolo, usar el token recibido como colateral en otro, usar esa liquidez para entrar en un tercero, y así sucesivamente.

Esta composabilidad es poderosa pero también concentra riesgos. Un fallo en cualquier protocolo de la cadena puede desencadenar pérdidas en cascada. Los yield farmers sofisticados gestionan activamente la exposición, diversifican entre estrategias y monitorean constantemente las métricas de riesgo como el APY real (descontando la depreciación de los tokens de recompensa) y el [TVL](https://www.coinbase.com/es-es/learn/crypto-glossary/what-is-tvl-in-defi) de los protocolos donde operan.

## Los agentes automatizados

DeFi no solo es habitado por personas. Una parte sustancial de la actividad on-chain la generan agentes automatizados: bots y contratos inteligentes que ejecutan operaciones en milisegundos, a menudo sin intervención humana directa.

### Los arbitrajistas y buscadores de MEV

Los arbitrajistas son agentes (normalmente bots) que explotan diferencias de precio del mismo activo entre distintos pools o redes. Su actividad es económicamente beneficiosa para el ecosistema: al comprar donde está barato y vender donde está caro, empujan los precios hacia el equilibrio y mantienen la coherencia del mercado.

Ligado al arbitraje existe el concepto de [MEV](https://ethereum.org/es/developers/docs/mev/) (*Maximal Extractable Value*): el valor que puede extraerse manipulando el orden de las transacciones dentro de un bloque. Los *searchers* o buscadores de MEV son agentes especializados que monitorizan el mempool de transacciones pendientes, identifican oportunidades y pagan altas comisiones a los validadores para que incluyan sus transacciones en posiciones estratégicas.

Las formas más comunes de extracción de MEV son el *front-running* (insertar una transacción antes que la de un usuario para beneficiarse del movimiento de precio que esa transacción causará), el *sandwich attack* (rodear una transacción con dos propias para explotar el slippage) y el arbitraje puro entre pools.

La aparición de arquitecturas basadas en *intents* como [UniswapX](https://uniswap.org/whitepaper/uniswapX.pdf) o [CoW Protocol](https://cow.fi/) busca precisamente revertir este valor hacia el usuario en lugar de dejarlo en manos de searchers externos.

### Los liquidadores

Los liquidadores son agentes (personas o bots) que ejecutan las liquidaciones forzosas cuando una posición de préstamo cae por debajo del umbral de colateralización mínimo requerido.

En protocolos como Aave o Compound, cuando el valor del colateral de un prestatario cae demasiado, cualquier agente externo puede activar la liquidación: paga la deuda del prestatario y recibe a cambio el colateral con un descuento (el *liquidation bonus*). Esto crea un incentivo económico para que agentes externos monitoreen el protocolo y mantengan su solvencia.

La rapidez es esencial. Los liquidadores compiten entre sí para ser los primeros en detectar y ejecutar liquidaciones, lo que ha generado un mercado de bots altamente optimizados que operan en tiempo real.

### Los solvers

Los [solvers](https://docs.cow.fi/cow-protocol/reference/core/auctions/the-solver-competition) son un tipo de agente que emerge con las arquitecturas de *intents*. En este modelo, el usuario no especifica cómo ejecutar una operación sino qué resultado quiere obtener ("quiero X tokens pagando como máximo Y"), y los solvers compiten entre sí para encontrar la ejecución más eficiente.

Un solver puede enrutar la orden por múltiples pools, usar liquidez off-chain, combinar órdenes de distintos usuarios para hacer coincidencias directas (batch auctions en CoW Protocol) o cualquier otra estrategia que le permita ofrecer el mejor precio. El solver que gana la competición ejecuta la transacción y retiene parte del margen.

Este modelo descentraliza la búsqueda de la mejor ejecución y, en la práctica, reduce el MEV que los usuarios sufren porque el incentivo de los solvers está alineado con dar el mejor precio posible al usuario.

## Los participantes colectivos e institucionales

A medida que DeFi madura, aparecen participantes de mayor escala que operan con estrategias más sofisticadas y con capital colectivo.

### Las DAO de inversión

<img src="./assets_5/investmentDAO.png" alt="ecosystem" width="400">

Las [DAO de inversión](https://es.cointelegraph.com/news/what-are-investment-daos-and-how-do-they-work) son organizaciones descentralizadas orientadas a gestionar capital de forma colectiva y programable. Operan como fondos de inversión nativos de la Web3, donde las decisiones de asignación se ejecutan mediante contratos inteligentes y se gobiernan de manera transparente por los poseedores de [tokens de gobernanza](https://www.coinbase.com/es-es/learn/crypto-basics/what-is-a-governance-token).

El capital de una DAO se organiza normalmente en una [tesorería](https://www.ledger.com/academy/glossary/bitcoin-treasury) on-chain, un conjunto de contratos que custodian los fondos de manera autónoma. Esta tesorería actúa como el balance general del protocolo y puede distribuir recursos hacia distintas estrategias de inversión, liquidez o incentivos. Su transparencia permite auditar en tiempo real las posiciones, los rendimientos y los gastos, algo imposible en los fondos tradicionales.

Dentro de la tesorería, muchas DAO utilizan [bóvedas](https://cointelegraph.com/explained/what-is-a-crypto-vault-and-how-does-it-work) (vaults), que funcionan como bots de inversión automatizados. Cada bóveda ejecuta estrategias definidas por la comunidad o los desarrolladores: yield farming, staking, provisión de liquidez o [arbitraje](https://www.coinbase.com/es-es/learn/advanced-trading/what-is-crypto-arbitrage-trading) entre protocolos. Los usuarios depositan capital en la bóveda y reciben un token representativo de su participación, cuyo valor aumenta a medida que la estrategia genera beneficios.

Protocolos como [Yearn Finance](https://yearn.finance/) perfeccionaron este modelo, donde el código reemplaza al gestor de inversión. Las estrategias se automatizan, los riesgos se diversifican y las recompensas se distribuyen proporcionalmente, todo de forma on-chain. Otros ejemplos incluyen [Badger DAO](https://badger.com/) (enfocado en Bitcoin en DeFi), [Harvest Finance](https://harvest.finance/) (optimización de yield farming) y [Beefy Finance](https://beefy.finance/) (optimizador multi-chain con estrategias auto-compounding).

La gestión eficiente de una tesorería es crítica. Un exceso de exposición a un único activo o protocolo puede comprometer la estabilidad de la DAO. Por eso, muchas implementan políticas de gobernanza automatizada, límites de riesgo, reservas en stablecoins o diversificación entre bóvedas.

**Gestión de tesorería**:

La gestión de tesorería en una DAO de inversión o en una DAO emisora de tokens es un proceso estratégico y dinámico que busca equilibrar seguridad, rentabilidad y sostenibilidad. Todo parte de definir objetivos claros: preservar el valor de los fondos, generar rendimientos, garantizar liquidez operativa y sostener la estabilidad del protocolo. Al estar en blockchain, cada movimiento de la tesorería es transparente y auditable, lo que impone una disciplina colectiva y decisiones basadas en consenso.

En la práctica, la gestión consiste en asignar el capital entre diferentes estrategias y riesgos. Parte se mantiene en stablecoins o activos líquidos para cubrir pagos, incentivos y gastos operativos. Otra parte se destina a posiciones de mayor rendimiento: staking, participación en pools de liquidez, inversiones en tokens estratégicos o préstamos descentralizados. El reto está en lograr diversificación sin fragmentación: demasiada exposición a un solo activo compromete la estabilidad; un enfoque excesivamente conservador limita el crecimiento.

Las decisiones sobre la tesorería suelen pasar por votaciones de gobernanza, donde los poseedores del token proponen y aprueban cambios en la distribución, la política de inversión o los mecanismos de cobertura. Este proceso puede ser abierto o delegado a comités especializados, pero siempre bajo reglas verificables y controles on-chain que minimicen riesgos operativos o abusos.

En una DAO emisora de tokens, la tesorería asume un rol adicional: sostener el valor y la utilidad del token. Puede intervenir en el mercado secundario (compras o quema), proveer liquidez en DEX, financiar incentivos o apoyar integraciones estratégicas. Además, sirve como respaldo económico para el desarrollo, la expansión del protocolo y la remuneración del equipo o colaboradores.

Con la madurez del ecosistema, la gestión de tesorería evoluciona hacia la automatización inteligente: contratos que ajustan posiciones según el mercado, estrategias de cobertura automatizadas y paneles de análisis que monitorizan rendimiento y exposición en tiempo real. La transparencia, trazabilidad y gobernanza activa fortalecen la confianza comunitaria y hacen de la tesorería el núcleo de resiliencia y sostenibilidad del proyecto.

En definitiva, la gestión de tesorería en una DAO es el arte de gobernar el capital colectivo con visión estratégica, flexibilidad y responsabilidad, combinando tecnología, incentivos y gestión del riesgo para maximizar el valor del ecosistema.

### Los fondos e inversores institucionales

A medida que DeFi ha ganado legitimidad, han entrado al ecosistema actores de mayor escala: fondos de capital riesgo cripto, family offices, fondos de cobertura (*hedge funds*) especializados y, más recientemente, tesorerías corporativas.

Estos actores operan con estrategias distintas a las del usuario individual. Sus posiciones son más grandes, su horizonte temporal más largo y su exposición al riesgo más calculada. Utilizan protocolos DeFi para generar rendimiento sobre activos que de otro modo estarían ociosos, para obtener liquidez sin liquidar posiciones, o para ejecutar estrategias de arbitraje y cobertura a escala.

Fondos como [Paradigm](https://www.paradigm.xyz/), [a16z crypto](https://a16zcrypto.com/) o [Multicoin Capital](https://multicoin.capital/) no solo invierten capital sino que actúan como actores de gobernanza con peso significativo en los votos de los protocolos donde tienen participación, lo que introduce dinámicas de poder que merecen ser tenidas en cuenta al analizar la descentralización real de cualquier protocolo.

Los market makers profesionales, como [Wintermute](https://www.wintermute.com/) o [Jump Crypto](https://jumpcrypto.com/), proporcionan liquidez profunda en DEXes y CEXes, estrechando los spreads y mejorando la experiencia de trading para todos los participantes.

## Los constructores y mantenedores

### Los equipos de protocolo y desarrolladores

Los equipos que construyen y mantienen los protocolos DeFi son actores centrales aunque a veces invisibles para el usuario final. Definen las reglas del sistema, escriben y auditan el código de los contratos inteligentes, diseñan los mecanismos de incentivos y gestionan las actualizaciones y respuestas a incidentes de seguridad.

En los primeros años de un protocolo, el equipo fundador suele tener control considerable sobre el desarrollo y las decisiones, incluso cuando el protocolo se presenta como descentralizado. Con el tiempo, y si el diseño lo permite, ese control se transfiere gradualmente a la comunidad mediante gobernanza on-chain.

La transparencia del código es una característica esencial: los contratos inteligentes son públicamente verificables, lo que permite que cualquier desarrollador audite el protocolo. Plataformas como [OpenZeppelin](https://openzeppelin.com/) facilitan este trabajo ofreciendo contratos estándar auditados que los equipos pueden reutilizar como base.

### Las comunidades de gobernanza

Los [poseedores de tokens de gobernanza](https://ethereum.org/es/dao/) son quienes toman las decisiones colectivas sobre el futuro de un protocolo: qué activos admitir como colateral, qué parámetros de riesgo ajustar, cómo distribuir los ingresos del protocolo o qué desarrollos priorizar.

La gobernanza on-chain funciona mediante propuestas y votaciones directamente en la blockchain. Cualquier poseedor del token puede proponer cambios o votar en los ya existentes, y si la propuesta supera el quórum necesario, el contrato la ejecuta automáticamente sin intervención de ningún equipo central.

En la práctica, la participación en gobernanza suele ser baja. Las decisiones acaban concentradas en grandes holders, fondos de inversión y el equipo fundador. Protocolos como [Compound](https://compound.finance/governance) o [MakerDAO](https://vote.makerdao.com/) han experimentado con delegación de voto y subcomités especializados para aumentar la calidad de las decisiones sin sacrificar la descentralización formal.

## La infraestructura de soporte

### Los oráculos

Los [oráculos](https://chain.link/education/blockchain-oracles) son el puente entre la blockchain y el mundo exterior. Los contratos inteligentes no pueden acceder por sí mismos a datos externos (precios de activos, tasas de interés, resultados de eventos), y los oráculos son la infraestructura que los provee de manera confiable.

En DeFi, los oráculos de precios son críticos para los protocolos de préstamo (para saber cuándo liquidar), para los activos sintéticos (para mantener el peg) y para los derivados (para calcular el valor de las posiciones). [Chainlink](https://chain.link/) es el oracle más utilizado, con una red descentralizada de nodos que agregan datos de múltiples fuentes y los publican on-chain. [Pyth Network](https://pyth.network/) ofrece una alternativa de mayor velocidad orientada a datos financieros de alta frecuencia, aportada directamente por las propias instituciones financieras que generan esos datos.

Un oracle comprometido o manipulado puede desestabilizar un protocolo entero. Los ataques de manipulación de precios a través de flash loans han sido una de las vulnerabilidades más explotadas en DeFi, lo que hace de la calidad y robustez de los oráculos una consideración de seguridad fundamental.

### Los agregadores y enrutadores

Los [agregadores](https://li.fi/knowledge-hub/crypto-aggregators/) son protocolos que no tienen liquidez propia sino que la consultan de múltiples fuentes simultáneamente para encontrar la mejor ejecución posible para el usuario.

[1inch](https://1inch.io/) fue el primer agregador de DEX relevante, resolviendo el problema de la fragmentación de liquidez dentro de una misma red. Con la expansión multi-chain, surgieron agregadores cross-chain como [LI.FI](https://li.fi/) o [Socket](https://socket.tech/) que extienden esa lógica a operaciones que atraviesan múltiples redes y puentes.

Estos agregadores actúan como infraestructura invisible para el usuario: muchas DApps los integran internamente sin que el usuario final sepa que su swap atraviesa cinco protocolos distintos antes de completarse. Su rol en el ecosistema es análogo al de los buscadores de vuelos en el mundo real: no operan el avión, pero optimizan qué combinación de vuelos conviene tomar.
