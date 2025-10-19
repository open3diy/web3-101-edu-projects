# El ecosistema de aplicaciones: DeFi

## Acerca de

Esta introducción a DeFi busca orientar y guiar hacia otros artículos de interés, priorizando la claridad de los conceptos clave y ofreciendo una visión general, más que detallar exhaustivamente cada aspecto, pero sí intentando aclarar las motivaciones y aspectos clave.

DeFi es un campo complejo y extenso, que merece su propio estudio y laboratorio de práctica, así que no te preocupes si quedan temas por profundizar.

Aunque podría parecer que DeFi debería abordarse más adelante, en un anexo o en otra fase del proyecto, lo cierto es que en Web3 la rentabilidad es un aspecto fundamental: cada rol suele ser doble —fundador e inversor, productor e inversor, usuario e inversor—. Por eso es necesario comprender desde el principio los conceptos fundamentales que veremos a continuación, ya que el papel del inversor es la piedra angular de Web3.

Como todo en Web3, los términos se consolidan y evolucionan con el tiempo, y siempre existen diferentes visiones e inexactitudes. Disculpa de antemano si encuentras errores; este documento, al igual que DeFi, es un ecosistema vivo que sigue evolucionando y mejorando.

Lo que no se encontrará aquí es una visión simplista y de “mundo feliz”, donde se omiten explicaciones de conceptos complejos y, sobre todo, no se aclaran sus motivaciones.

## ¿Que es [DeFi](https://ethereum.org/es/defi/)?

Como su nombre indica, son finanzas descentralizadas, y con eso ya hemos terminado toda la explicación... gracias por estar aquí, ¡saludos!

Bromas aparte... DeFi constituye la capa financiera del ecosistema Web3, orientada a crear y gestionar servicios como [préstamos](https://ethereum.org/es/defi/#lending), ahorro (mediante staking), emisión de activos, [intercambio](https://ethereum.org/es/defi/#swaps) o provisión de liquidez sin intermediarios (mediante [liquidity pools](https://finematics.com/liquidity-pools-explained/) usando un [AMM](https://academy.bit2me.com/que-es-automated-market-maker-amm/)). Aunque a menudo se asocia con la búsqueda de beneficios ([Yield Farming](https://finematics.com/yield-farming-explained/) y su agregador [Yearn Finance](https://www.bitstamp.net/es/learn/cryptocurrency-guide/what-is-yearn-finance-yfi/)), su función principal es facilitar la financiación y el flujo de capital dentro del ecosistema. En este sentido, suele confundirse con el trading o la inversión especulativa, cuando en realidad persigue objetivos más amplios, relacionados con la sostenibilidad y la economía de un proyecto. Muchas veces se olvida que detrás de muchos proyectos no solo hay memes, sino infraestructuras, salarios e incentivos que proporcionar; una relación muy directa que se debe considerar frente a un simple juego de casino.

Es un espacio abierto, en lo bueno y en lo malo, porque DeFi es permisionless; es decir, **cualquiera, en cualquier lugar y en cualquier momento**, con una wallet puede participar. No hay que cumplir requisitos previos, ni pedir permiso, y al ser descentralizado, ni siquiera es necesario proporcionar datos personales.

El verdadero poder de DeFi no está solo en replicar servicios financieros, sino en tres pilares fundamentales: la economía de tokens, que define cómo el protocolo captura y reparte valor; la tokenización de activos, como WBTC y sobre todo las stablecoins, que conectan con la economía real y proporciona liquidez; y las DAOs, que son en este contexto como las SICAV del mundo cripto, que gestionan tesorerías y deciden cómo fluye el dinero.

Vamos desglosar estos conceptos para que estén mas claros.

### La economía del token

Sin entrar en detalles sobre qué es un token, criptoactivo o criptomoneda, en el ejemplo más básico de un token ERC-20 usado como medio de intercambio para una utilidad concreta, el token permite **capturar y distribuir el valor generado por la red**. Debemos entender el contexto de Web3, donde los fundadores, proveedores y los usuarios, es decir, la red, pueden ser también inversores o holders. Este doble rol es fundamental para la rentabilidad y sostenibilidad del ecosistema Web3.

Cuando un proyecto cuenta con su propio token, es posible construir una economía y una política monetaria alrededor de él, descrito en un documento llamado tokenomic, permitiendo **capturar valor futuro** de la red, en lo que se conoce como el efecto red. Así se logran cosas notables: los proveedores también se benefician directamente de su trabajo porque son, a la vez, inversores. Dicho de forma simple, si hacen un buen trabajo, pueden verse recompensados por la subida del precio de su propio token.

Claro está, todo esto no está exento de riesgos y problemas: la especulación, la concentración de tokens o una mala gestión económica pueden comprometer la sostenibilidad del proyecto.

Aparte de capturar valor, un token propio tiene más ventajas: pueden servir como herramienta de gobernanza, permitir el acceso a servicios exclusivos o incentivar comportamientos dentro del protocolo.

Por lo tanto, ahora que entiendes el propósito de un token, entenderás lo fundamental que resulta DeFi: es la infraestructura descentralizada que gestiona toda su economía.

En el ciclo de vida de un token, durante su fase inicial o startup, el mercado primario es donde se decide cómo y a quién se distribuye la emisión inicial. En este punto, DeFi no siempre está plenamente presente: lo habitual es realizar una oferta inicial (ICO, Initial Coin Offering), estructurada en distintas fases —privada, anticipada o pública— que funcionan como rondas de financiación temprana.

Estas ofertas suelen basarse en un preminado, es decir, una creación previa de tokens asignados antes de su lanzamiento público. Parte de ese preminado se vende en preventas y se gestiona mediante whitelists, listas de direcciones autorizadas a participar en cada fase, limitando el acceso o aplicando requisitos específicos (comunidad, KYC, aportación previa, etc.). Todo esto ocurre dentro del mercado primario, antes de que el token entre en circulación libre en DEX o CEX.

Con el tiempo, y ante los desafíos regulatorios, dado que las ICO podían clasificarse como valores (securities), el proceso evolucionó hacia una estructura más robusta con la aparición de [launchpads](https://es.cointelegraph.com/news/launchpads-funding-ideas-not-products). Estas plataformas centralizan o coordinan las ventas iniciales de tokens, incorporando mecanismos de cumplimiento y transparencia. El auge de DeFi llevó este modelo un paso más allá con variantes descentralizadas como las IDO (Initial DEX Offerings) y las IFO (Initial Farm Offerings), donde la distribución se ejecuta directamente mediante contratos inteligentes en DEX o pools de liquidez, eliminando intermediarios, fortaleciendo la seguridad y optimizando la transparencia.

En contraste, el modelo fair launch propone un enfoque radicalmente abierto: sin preminado, sin whitelists y sin fases privadas. Todos los participantes tienen acceso simultáneo desde el primer bloque, normalmente mediante minería, staking o liquidity mining. Este tipo de lanzamiento busca equidad total en la distribución, aunque sacrifica parte de la eficiencia en la recaudación inicial.

El papel clave de DeFi llega cuando el token entra en el mercado secundario, en el que el token obtiene liquidez real a través de los denominados liquidity pools o piscinas de liquidez. En ellos entran en juego los *Automated Market Makers* (AMM), mecanismos algorítmicos que fijan los precios de intercambio utilizando los fondos aportados por los usuarios. Gracias a este modelo, los tokens pueden negociarse de forma completamente descentralizada y sin intermediarios.

Dentro de esta economía también existen mecanismos de ajuste y distribución del valor, como las recompras de tokens (buybacks) para sostener el precio, las quemas (burn) para controlar la inflación, los airdrops, que funcionan como campañas de marketing de distribución gratuita de tokens para atraer nuevos usuarios, premiar a quienes ya usaban el protocolo y repartir la propiedad entre más participantes para hacer el proyecto más descentralizado y las reservas de incentivos, que premian a los holders o mantenedores del token a bloquear y asegurar el precio (por eso se habla tanto del TVL o Total Valor Bloqueado como una métrica fundamental). Todo esto se gestiona mediante mecanismos como las tesorerías, que son contratos inteligentes que acumulan tokens propios o ajenos; o las bóvedas, que actúan como bots automatizados que ejecutan operaciones concretas definidas para alcanzar ciertos objetivos de rentabilidad.

Con el tiempo, si el proyecto crece, el token puede evolucionar hacia nuevos usos: gobernanza, staking o incluso integración con productos financieros más amplios dentro del ecosistema DeFi.

Como vemos, la envergadura y complejidad de todo esto es enorme. Pero no es necesario aplicarlo todo de golpe. A medida que el proyecto crezca, podremos contar con especialistas en el ecosistema DeFi o como decíamos, también contamos con la ayuda de launchpads o lanzadores de proyectos, porque DeFi es una herramienta, el token es solo el mecanismo de captura de valor, el verdadero valor proviene del modelo de negocio y la comunidad.

### Tokenización de activos

Sin la tokenización, DeFi quedaría limitado a su propio ecosistema: solo se podrían intercambiar activos nativos como ETH o tokens internos. Al tokenizar —ya sean BTC, bonos, acciones, materias primas o monedas fiduciarias (a través de stablecoins)— DeFi gana profundidad, liquidez y una conexión directa con la economía real.

El reto de la tokenización está en garantizar el colateral, la transparencia y las auditorías que respalden realmente el valor de los activos.

A cambio, la tokenización proporciona liquidez y acceso abierto, sin permisos, a una economía verdaderamente global. Desde WBTC, que “envuelve” a Bitcoin, hasta cualquier otro activo tokenizado, todo puede recibir liquidez; pero sin duda son las stablecoins las que ofrecen el anclaje más sólido al mundo real.

#### Las stablecoins: anclaje al mundo real

Las stablecoins son criptoactivos diseñados para mantener una paridad estable con una moneda fiduciaria, normalmente el dólar estadounidense o el euro, funcionando como un anclaje entre el mundo digital y el mundo real. Su valor se mantiene en una relación 1:1 mediante [distintos tipos de respaldo:](https://academy.binance.com/en/articles/what-is-a-stablecoin) colateral fiduciario, colateral cripto, o mecanismos algorítmicos.

Las principales stablecoins del mercado son USDT y USDC. USDT es la más usada y con mayor capitalización, aunque con menor transparencia sobre sus reservas. USDC, emitida por Circle, es la más regulada y auditada, lo que la hace más segura desde el punto de vista institucional. En Europa, bajo la normativa MiCA, las stablecoins deberán ser emitidas por entidades reguladas dentro del Espacio Económico Europeo, por lo que el uso de versiones como EURC o monedas estables respaldadas por bancos europeos será el camino natural. China impulsa el e-CNY como una moneda digital soberana emitida por el Banco Popular, concebida para mantener el control directo sobre la oferta monetaria y la trazabilidad del sistema financiero. A diferencia de una stablecoin respaldada en yuanes, que depende de reservas existentes y puede operar en redes públicas como Ethereum, el e-CNY forma parte de la base monetaria y permite al Estado ajustar liquidez o deuda según sus políticas económicas. Paralelamente, Pekín utiliza a Hong Kong como un laboratorio regulatorio para experimentar con stablecoins privadas bajo supervisión, observando su adopción y efectos en los mercados internacionales sin comprometer la estabilidad ni el control financiero dentro del continente.

En el ámbito Web3, la stablecoin DAI de MakerDAO es una referencia porque es descentralizada y mantiene su valor mediante sobrecolateralización con criptoactivos. Aunque usa algoritmos para ajustar su paridad, no es una stablecoin algorítmica pura, ya que está respaldada por activos reales bloqueados en contratos inteligentes.

Las stablecoins son imprescindibles en DeFi porque aportan estabilidad y liquidez. Permiten realizar coberturas frente a la volatilidad del mercado, transferencias de valor estables y, sobre todo, son el componente fundamental en las pools de liquidez. En una pool siempre hay dos tokens: uno base y otro cotizado. El token cotizado, que suele ser una stablecoin, actúa como la puerta de entrada al token base, representa el valor con el que los usuarios acceden o intercambian, y es la referencia del mercado para valorar el activo dentro de la pool.

Además de las grandes stablecoins como DAI o USDC, varios ecosistemas han intentado crear sus propias monedas estables nativas para mantener la liquidez dentro de su red y reducir la dependencia del dólar. Ejemplos de ello son UST de Terra (colapsada en 2022), USDN de Waves, sUSD en Synthetix, MIM de Abracadabra o FRAX de Frax Finance, que combina respaldo parcial con un mecanismo algorítmico híbrido. Estos intentos muestran el interés de muchos protocolos en emitir una stablecoin propia que funcione como unidad de cuenta interna, aunque la mayoría han enfrentado problemas de estabilidad o de confianza en momentos de tensión del mercado.

A día de hoy, el desafío sigue siendo lograr una stablecoin realmente descentralizada, estable y desvinculada del dólar sin comprometer la seguridad ni la adopción global, algo que el ecosistema DeFi aún busca equilibrar.

**Riesgos sistémicos en las stablecoins**:

Las stablecoins, aunque aportan estabilidad y liquidez al ecosistema DeFi, también introducen riesgos sistémicos que pueden afectar tanto a protocolos individuales como a todo el mercado. Su aparente solidez depende de la transparencia de las reservas, la robustez del mecanismo de paridad y la confianza de los usuarios.

El primer riesgo es el colateral, es decir, la calidad y liquidez de los activos que respaldan la stablecoin. En stablecoins centralizadas como USDT o USDC, un problema en las reservas o una congelación regulatoria puede provocar una pérdida de paridad inmediata. En las descentralizadas como DAI, la caída del valor del colateral (por ejemplo ETH o wBTC) puede generar liquidaciones masivas que presionan la estabilidad del sistema.

El segundo riesgo es el regulatorio. Las stablecoins se sitúan en el punto intermedio entre las criptomonedas y las finanzas tradicionales, lo que las convierte en objetivo directo de los reguladores. Cambios normativos, como los impuestos por MiCA en Europa o la regulación de stablecoins en EE.UU., pueden limitar su circulación, exigir licencias bancarias o restringir su emisión.

El tercer riesgo es el tecnológico y de gobernanza. Un fallo en el contrato inteligente, una mala configuración de parámetros o un ataque de gobernanza pueden desestabilizar la paridad. En las algorítmicas, la dependencia de incentivos automáticos ha demostrado ser extremadamente frágil ante eventos de pánico o volatilidad extrema, como ocurrió con UST de Terra.

También existe un riesgo macroeconómico y de concentración, ya que la mayoría de stablecoins están vinculadas al dólar. Esto convierte al ecosistema DeFi en dependiente de la política monetaria de EE.UU. y limita la soberanía financiera descentralizada. Un colapso o bloqueo de una gran stablecoin, como USDC o USDT, afectaría simultáneamente a miles de protocolos y pools de liquidez, generando contagio inmediato.

En definitiva, las stablecoins son el pilar de DeFi, pero también su mayor punto de fragilidad. La descentralización total y la diversificación de colaterales son los dos factores que determinarán si en el futuro el sistema puede resistir sin depender del dólar ni de entidades centralizadas.

**DAI la stablecoin alineada con los ideales Web3**:

DAI es considerada por muchos la stablecoin nativa de la Web3 porque representa el ideal de descentralización funcional dentro del ecosistema DeFi: no depende de bancos, gobiernos ni empresas emisoras, sino de contratos inteligentes y gobernanza on-chain.

Su legitimidad viene de tres pilares:

- Se emite de forma abierta mediante colateral cripto (ETH, wBTC, LSDs, etc.).
- La política monetaria la define la comunidad a través de MakerDAO.
- Su operativa es completamente transparente y auditable en cadena.

Ahora bien, no está exenta de riesgos. Parte de su colateral hoy incluye activos centralizados como USDC, lo que introduce un punto de dependencia. Además, en escenarios de fuerte caída del mercado, puede sufrir presiones de liquidación.

Aun así, en términos de filosofía Web3, DAI sigue siendo la stablecoin más alineada con la descentralización, la autocustodia y la transparencia, por eso se la considera la referencia “orgánica” de la Web3, incluso si en la práctica su estabilidad se apoya parcialmente en activos del mundo tradicional TradFi.

### Las DAO de inversión

Las DAO de inversión son organizaciones descentralizadas orientadas a gestionar capital de forma colectiva y programable. Operan como fondos de inversión nativos de la Web3, donde las decisiones de asignación se ejecutan mediante contratos inteligentes y se gobiernan de manera transparente por los poseedores de tokens de gobernanza.

El capital de una DAO se organiza normalmente en una tesorería on-chain, un conjunto de contratos que custodian los fondos de manera autónoma. Esta tesorería actúa como el balance general del protocolo y puede distribuir recursos hacia distintas estrategias de inversión, liquidez o incentivos. Su transparencia permite auditar en tiempo real las posiciones, los rendimientos y los gastos, algo imposible en los fondos tradicionales.

Dentro de la tesorería, muchas DAO utilizan bóvedas (vaults), que funcionan como bots de inversión automatizados. Cada bóveda ejecuta estrategias definidas por la comunidad o los desarrolladores: yield farming, staking, provisión de liquidez o arbitraje entre protocolos. Los usuarios depositan capital en la bóveda y reciben un token representativo de su participación, cuyo valor aumenta a medida que la estrategia genera beneficios.

Protocolos como Yearn Finance, Badger DAO o Harvest Finance perfeccionaron este modelo, donde el código reemplaza al gestor de inversión. Las estrategias se automatizan, los riesgos se diversifican y las recompensas se distribuyen proporcionalmente, todo de forma on-chain.

La gestión eficiente de una tesorería es crítica. Un exceso de exposición a un único activo o protocolo puede comprometer la estabilidad de la DAO. Por eso, muchas implementan políticas de gobernanza automatizada, límites de riesgo, reservas en stablecoins o diversificación entre bóvedas.

En conjunto, las tesorerías y bóvedas son el sistema circulatorio financiero de una DAO de inversión: almacenan, asignan y multiplican el capital de la comunidad bajo reglas de código y consenso. Representan la evolución del concepto de “gestor de fondos” hacia un modelo completamente descentralizado, auditable y sin intermediarios.

**Gestión de tesorería**:

La gestión de tesorería en una DAO de inversión o en una DAO emisora de tokens es un proceso estratégico y dinámico que busca equilibrar seguridad, rentabilidad y sostenibilidad. Todo parte de definir objetivos claros: preservar el valor de los fondos, generar rendimientos, garantizar liquidez operativa y sostener la estabilidad del protocolo.
Al estar en blockchain, cada movimiento de la tesorería es transparente y auditable, lo que impone una disciplina colectiva y decisiones basadas en consenso.

En la práctica, la gestión consiste en asignar el capital entre diferentes estrategias y riesgos. Parte se mantiene en stablecoins o activos líquidos para cubrir pagos, incentivos y gastos operativos. Otra parte se destina a posiciones de mayor rendimiento: staking, participación en pools de liquidez, inversiones en tokens estratégicos o préstamos descentralizados.
El reto está en lograr diversificación sin fragmentación: demasiada exposición a un solo activo compromete la estabilidad; un enfoque excesivamente conservador limita el crecimiento.

Las decisiones sobre la tesorería suelen pasar por votaciones de gobernanza, donde los poseedores del token proponen y aprueban cambios en la distribución, la política de inversión o los mecanismos de cobertura. Este proceso puede ser abierto o delegado a comités especializados, pero siempre bajo reglas verificables y controles on-chain que minimicen riesgos operativos o abusos.

En una DAO emisora de tokens, la tesorería asume un rol adicional: sostener el valor y la utilidad del token. Puede intervenir en el mercado secundario (compras o quema), proveer liquidez en DEX, financiar incentivos o apoyar integraciones estratégicas. Además, sirve como respaldo económico para el desarrollo, la expansión del protocolo y la remuneración del equipo o colaboradores.

Con la madurez del ecosistema, la gestión de tesorería evoluciona hacia la automatización inteligente: contratos que ajustan posiciones según el mercado, estrategias de cobertura automatizadas y paneles de análisis que monitorizan rendimiento y exposición en tiempo real.
La transparencia, trazabilidad y gobernanza activa fortalecen la confianza comunitaria y hacen de la tesorería el núcleo de resiliencia y sostenibilidad del proyecto.

En definitiva, la gestión de tesorería en una DAO es el **arte** de gobernar el capital colectivo con visión estratégica, flexibilidad y responsabilidad, combinando tecnología, incentivos y gestión del riesgo para maximizar el valor del ecosistema.

## Evolución de DeFi en capas

En Web3 todo es modular y en capas, siguiendo el principio de composabilidad, y DeFi no iba a ser la excepción.

Se puede interpretar que DeFi se construye sobre capas, denominadas DeFi 1.0, 2.0, 3.0… que pueden confundirse con versiones, pero en realidad forman un stack de capas tecnológicas, donde cada una resuelve un problema distinto.

La primera capa, [DeFi 1.0](https://web3.bitget.com/en/academy/what-are-DeFi-1-0-2-0-and-3-0), establece los cimientos del intercambio, los préstamos y la provisión de liquidez sin intermediarios, principalmente a través de [DEX (Decentralized Exchanges)](https://academy.binance.com/es/articles/what-is-a-decentralized-exchange-dex) y protocolos de lending como Compound o Aave. Hacia el final de esta etapa surgió el Yield farming, un modelo de incentivos que impulsó la adopción de estos protocolos y marcó la transición hacia DeFi 2.0. La interfaz web de sus DApps ofrece herramientas para que el usuario tesorero gestione manualmente. Su interoperabilidad es básica: sus contratos inteligentes son *composables*, permitiendo que otros protocolos interactuaran directamente con ellos en la blockchain. Su principal desafío es la baja eficiencia de capital y la [fragmentación de la liquidez](https://es.cointelegraph.com/news/liquidity-fragmentation-in-DeFi-a-systemic-problem) entre múltiples plataformas.

Sobre los cimientos de DeFi 1.0 —donde proyectos como Yearn Finance (Finanzas del Anhelo) introdujeron la automatización del rendimiento— surge [DeFi 2.0](https://changelly.com/blog/what-is-DeFi-2-0/) como una evolución orientada a la sostenibilidad y la **automatización**. Su innovación clave es la liquidez propiedad del protocolo [(Protocol-Owned Liquidity, POL)](https://www.cube.exchange/es/what-is/protocol-owned-liquidity), en lugar del usuario: un modelo que busca independencia frente a los incentivos externos y garantiza una gestión más autónoma y estable del capital, basada únicamente en el protocolo predefinido, aunque con mayor complejidad operativa y riesgo de seguridad, pero permitiendo difuminar el problema de fragmentación de liquidez mediante protocolos automatizados. La interfaz web de las DApps permite al usuario inversor o de gobernanza ajustar parámetros estratégicos de la tesorería.

La tercera capa, [DeFi 3.0](https://medium.com/@web3./DeFi-3-0-the-evolution-of-decentralized-finance-and-the-emergence-of-the-crypto-legos-and-ai-775b585bd65), acerca DeFi 2.0 a un usuario final menos especializado, y se centra en ofrecer servicios de agregación y orquestación cross-chain, es decir, reunir diferentes protocolos de DeFi 1.0 y 2.0 para ofrecer las mejores opciones, incluso entre distintas cadenas. Esto no ocurre únicamente dentro de una DApp, sino que también puede ofrecerse como servicio, a través de modelos de Farming as a Service (FaaS). Por lo tanto, su interoperabilidad es su razón de ser: orquesta y agrega protocolos de las capas 1.0 y 2.0, moviendo capital dinámicamente entre diferentes redes para maximizar la eficiencia. Además, esta capa marca el inicio de la integración de Activos del Mundo Real (RWA) como vía de escalabilidad, ampliando el alcance más allá del ecosistema puramente cripto.

Mirando al futuro, una posible capa DeFi 4.0 tendría como objetivo la adopción masiva mediante la completa abstracción de la tecnología, transformando la interacción en una experiencia simple e intuitiva para el usuario final. Su interoperabilidad sería perfecta y omnipresente, integrando no solo protocolos DeFi, sino también el sistema financiero tradicional y otras plataformas digitales, haciendo que la blockchain subyacente sea prácticamente invisible.

Sin perder perspectiva en el resto de capas, como fundadores de proyectos sobre todo nos centraremos en la capa 1.0 que es donde crearemos liquidez en un proyecto para el mercado secundario y previsiblemente en la 2.0 para automatizar.

## La economía: un entramado complejo y difícil de digerir

La economía, en sí, ya es compleja; pero con los conceptos DeFi lo es aún más.

La composabilidad, ese juego de legos característico de Web3 donde todo encaja, está muy presente en DeFi. Esto la hace extremadamente versátil y con gran capacidad de escalar, pero también la vuelve compleja de entender al principio.

Se intentará simplificar, resumir y enfocar en los conceptos económicos que cualquier emprendedor que inicia un proyecto debería comprender.

Debemos tener claro que se trata de un ecosistema financiero tan sofisticado como las finanzas tradicionales, pero construido sobre tecnología descentralizada.

Como explicamos, en este ecosistema existe una evolución natural: desde los servicios básicos de intercambio de tokens, préstamos, provisión de liquidez y generación de rendimiento en la etapa 1.0, hasta su automatización en la 2.0, la mejora de rentabilidad e interoperabilidad en la 3.0, y finalmente su escalado al mundo real en la 4.0. Todo esto resume, en esencia, la visión general de DeFi.

Por supuesto, cada DApp o protocolo DeFi puede combinar distintas capas o enfoques. Por ejemplo, PancakeSwap integra elementos de DeFi 1.0 y 2.0 para ofrecer servicios financieros descentralizados —como intercambio, provisión de liquidez y generación de rendimiento— a cambio de comisiones. En la práctica, cada protocolo evoluciona según sus propios objetivos: unos buscan reducir costes o mejorar la rentabilidad, otros aumentar la liquidez o atraer nuevos usuarios. La idea general es sencilla: ofrecer servicios financieros dentro del ecosistema cripto sin intermediarios, de forma automatizada y abierta, a cambio de una ganancia en comisiones que sostiene su propio modelo económico.

Y en la práctica, muchas DApps y protocolos ya comprenden el ecosistema Web3 y son capaces de integrar conceptos DeFi complejos de forma más simplificada y accesible, permitiendo que los proyectos Web3 se creen, crezcan y se mantengan. Aun así, no todo es perfecto: DeFi sigue en crecimiento, la mala experiencia de usuario (UX) continúa siendo un reto, muchos protocolos siguen siendo experimentales, los ataques, tanto a la lógica económica que los hace rentables como a su seguridad básica (por ejemplo, el robo de tokens), siguen siendo una realidad. Pero incluso un token mal gestionado o con poco capital puede ser manipulado (pump /dump) a voluntad con fines especulativos, por actores ajenos al proyecto.

Estas DApps son conocidas como DEX (Decentralized Exchanges), en contraposición a las CEX (Centralized Exchanges). En la práctica como hemos visto, no se limitan al intercambio de tokens unicamente. La mayoría integran los servicios DeFi que mencionamos como préstamos, provisión de liquidez o yield farming. Por tanto, el término “DEX” es más bien una categoría formal o histórica dentro de DeFi, ya que muchas de estas plataformas funcionan hoy como ecosistemas financieros completos.

### El mercado en web3

El mercado, entendido como el espacio donde se realiza la actividad económica, es el núcleo de la Web3. En él se cruzan la oferta y la demanda de activos digitales, se forman los precios y se genera la liquidez que sostiene el ecosistema. La diferencia fundamental frente al mercado tradicional es que en Web3 las reglas no las dicta una institución central, sino el propio código desplegado en contratos inteligentes.

Podemos hablar en primer lugar de los mercados entre pares (P2P), donde los usuarios intercambian directamente activos sin intermediarios. Son la forma más simple de comercio descentralizado y se basan en la confianza o en sistemas de reputación. Cuando se añade un servicio escrow, un contrato que retiene temporalmente los fondos hasta que ambas partes cumplen las condiciones del intercambio, el sistema gana seguridad y transparencia.

A partir de esa evolución nace el modelo user-to-contract (U2C), en el que el usuario ya no negocia con otra persona, sino con un contrato inteligente que actúa como contraparte automatizada. Este modelo es el estándar en DeFi: el código define las reglas del intercambio, elimina el riesgo de contraparte y permite la ejecución automática de órdenes.

En Web3 también distinguimos el mercado primario y el mercado secundario. El primario es donde los proyectos emiten y distribuyen sus tokens iniciales, normalmente mediante preventas, whitelists, IDO o airdrops. Aquí es donde entra el capital que financia al protocolo. El mercado secundario, en cambio, es donde esos tokens ya emitidos se compran y venden entre usuarios, generando liquidez, ajustando el valor de los activos y permitiendo el descubrimiento de precios, es decir, el proceso mediante el cual la interacción entre oferta y demanda determina de forma transparente y dinámica el valor real de un token en el mercado.

Los mercados pueden clasificarse según su mecanismo de funcionamiento. El mercado de libro de órdenes (order book), típico de los exchanges centralizados y algunos DEX híbridos, organiza las órdenes de compra y venta para determinar el precio. El mercado OTC (Over The Counter) permite acuerdos directos entre partes, ideal para grandes operaciones fuera del mercado público. Finalmente, el modelo más característico de DeFi es el AMM (Automated Market Maker), donde los intercambios se realizan contra pools de liquidez gestionados por algoritmos. Estos AMM —como Uniswap, Curve o Balancer— permiten operar sin intermediarios, de forma continua y abierta, a cambio de comisiones que se reparten entre los proveedores de liquidez.

Además, en Web3 surgen nuevos tipos de mercado especializados, como los mercados de préstamos, donde se negocia la liquidez mediante garantías colateralizadas; los mercados de derivados, con futuros y opciones on-chain; y los mercados de activos tokenizados, que conectan finanzas tradicionales y blockchain.

En conjunto, el mercado en Web3 es un entorno dinámico, sin fronteras y sin custodios, donde los contratos inteligentes sustituyen a los intermediarios y la confianza se distribuye entre los participantes. Es la base de toda la economía descentralizada, y entender su estructura es esencial para comprender cómo fluye el valor en DeFi.

**Formación de precios y arbitraje entre mercados DeFi y CEX**:

La formación de precios en Web3 depende de la interacción constante entre los mercados centralizados (CEX) y los descentralizados (DeFi). Ambos operan con los mismos activos, pero bajo reglas distintas: los CEX usan libros de órdenes tradicionales, mientras que los DEX y AMM ajustan sus precios de forma algorítmica mediante la liquidez aportada por los usuarios.

El precio de un token nunca es completamente fijo, sino el resultado del equilibrio dinámico entre oferta y demanda en cada tipo de mercado. En los CEX, los precios reflejan la suma de todas las órdenes activas de compra y venta; en los AMM, el precio se determina automáticamente según la proporción entre los tokens en el pool (x·y = k). Cuando un activo se compra masivamente en un AMM, su precio sube dentro del pool, y si se vende, baja.

Este desajuste temporal entre el precio en los CEX y el precio en los DEX crea oportunidades de arbitraje. Los arbitrajistas son agentes que detectan diferencias de valor entre mercados y realizan operaciones simultáneas para obtener beneficio y equilibrar los precios. Por ejemplo, si un token vale 1,02 USD en un DEX y 1,00 USD en un CEX, los arbitrajistas comprarán en el CEX y venderán en el DEX hasta que los precios se igualen.

El arbitraje no solo genera beneficio individual, sino que cumple una función económica esencial: mantiene la coherencia de precios entre los distintos mercados, evita distorsiones y mejora la eficiencia del sistema. En DeFi, muchas de estas operaciones se ejecutan de forma automática mediante bots on-chain, que monitorizan los precios y actúan en cuestión de segundos, aprovechando la transparencia total de los datos en la blockchain.

En periodos de alta volatilidad o congestión de red, pueden producirse desacoples temporales entre CEX y DEX, ya que las comisiones o la lentitud de las transacciones dificultan el arbitraje. Estas diferencias pueden ser amplificadas si los pools de liquidez tienen poco volumen o si los oráculos tardan en actualizar precios.

En definitiva, la formación de precios en Web3 es un proceso continuo, descentralizado y autorregulado, donde el arbitraje actúa como fuerza de equilibrio entre los mercados. La interacción entre CEX y DeFi es, en última instancia, lo que garantiza que los precios reflejen el valor real de los activos y que la economía digital mantenga coherencia y liquidez global.

**Los oráculos de precios**:

Los oráculos son sistemas que conectan la blockchain con información del mundo exterior. En el contexto DeFi, su función principal es proveer precios fiables y actualizados de los activos negociados, permitiendo que los contratos inteligentes tomen decisiones correctas en función del valor real del mercado.

Como la blockchain no puede acceder por sí misma a datos externos, los oráculos actúan como fuente de verdad para operaciones críticas: liquidaciones, préstamos, emisión de stablecoins o cálculo de recompensas.

Los oráculos pueden ser manipulados, sufrir retrasos o depender de fuentes únicas, lo que genera riesgos como precios falsos, liquidaciones indebidas y pérdidas por ataques (flash loans, front-running, sandwich). La diversificación y actualización rápida son clave para mitigar estos problemas.

**DEX Aggregators**:

Los DEX aggregators son plataformas que permiten a los usuarios encontrar el mejor precio y la mayor eficiencia al intercambiar tokens en DeFi. Estos agregadores representan una evolución hacia DeFi 3.0, ya que conectan múltiples exchanges descentralizados y rutas de liquidez, analizando en tiempo real dónde se puede ejecutar una operación con el menor coste y el menor deslizamiento posible, incluso entre distintas blockchains. El usuario solo interactúa con el agregador, que se encarga de dividir la orden entre diferentes pools o protocolos si es necesario, optimizando el resultado final.

### Pools de liquidez

Las piscinas de liquidez o liquidity pools son la base de la economía DeFi. Su función es permitir que exista liquidez constante en el mercado: que cualquier usuario pueda comprar o vender un activo en cualquier momento, sin necesitar una contraparte directa. Este mecanismo automatizado es lo que da origen al modelo AMM (Automated Market Maker).

Se les llama “piscinas” porque funcionan de forma análoga a un depósito común. Los usuarios aportan pares de tokens que quedan bloqueados en un contrato inteligente, formando una reserva sobre la que otros pueden operar. Generalmente, una pool se compone de dos tokens: uno base y otro cotizado. Este par es el binomio mínimo necesario para el intercambio.

En muchos casos, el token cotizado suele ser una stablecoin, que actúa como nexo común de valor (por ejemplo, DAI, USDC o USDT). En otros, el token cotizado es ETH u otro activo del protocolo con el que se relaciona el token base. Lo importante es que entre ambos tokens exista afinidad de mercado, es decir, que haya una relación económica real o una demanda sostenida. Si un par carece de interés o uso, simplemente no genera volumen ni liquidez.

El precio dentro de una pool se mantiene mediante una fórmula matemática de equilibrio, normalmente x·y = k, donde x y y representan las cantidades de cada token y k es una constante. Si un activo se compra mucho, su cantidad en la pool disminuye y su precio sube automáticamente; si se vende, ocurre lo contrario. Este mecanismo reemplaza el libro de órdenes tradicional, garantizando que siempre haya ambos token disponibles.

Sin embargo, las pools no son sistemas perfectos. En teoría son cerradas y autorreguladas, pero en la práctica dependen del comportamiento externo del mercado. Si el token base puede emitirse libremente fuera de la pool, su exceso de oferta diluye el valor del otro token, generando un efecto similar a la inflación: los proveedores de liquidez pierden poder adquisitivo dentro del pool.

Existen también riesgos de manipulación del precio, como los ataques pump and dump, en los que grandes operadores mueven bruscamente los precios para obtener beneficios especulativos.

Finalmente, uno de los fenómenos más característicos de este modelo es la pérdida impermanente, que ocurre cuando el precio relativo de los tokens del pool cambia respecto al mercado externo.

Se llama "impermanente" porque la pérdida solo se materializa (se hace permanente) si retiras tus activos del pool mientras la diferencia de precios persiste, si luego se ajusta al precio de la pool, ya no hay perdida.

**Ejemplo simple**:

Supongamos una pool con 1 ETH y 3500 DAI (precio inicial 1 ETH = 3500 DAI):

- **Inicio:**  
  - 1 ETH + 3500 DAI → valor total = **7000 DAI**

- **Si el precio sube** a 4000 DAI:  
  - El pool vende parte de tu ETH → terminas con ~0.935 ETH + 3740 DAI  
  - Valor total ≈ **7470 DAI**  
  - Si hubieras holdeado (1 ETH + 3500 DAI), tendrías **7500 DAI**  
  - → **Pérdida impermanente ≈ 30 DAI**

- **Si el precio baja** a 2500 DAI:  
  - El pool compra ETH → terminas con ~1.183 ETH + 2958 DAI  
  - Valor total ≈ **5933 DAI**  
  - Si hubieras holdeado, tendrías **6000 DAI**  
  - → **Pérdida impermanente ≈ 67 DAI**

En ambos casos, **pierdes respecto a haber holdeado**, porque el mecanismo del pool te mantiene equilibrado entre ambos activos.  
La pérdida solo se compensa si las comisiones o incentivos superan esa diferencia.

#### Evolución de las fórmulas de los pools de liquidez

El funcionamiento de los AMM se basa en una función matemática constante que mantiene el equilibrio entre los tokens del pool. A lo largo del tiempo, estos modelos han evolucionado para mejorar la eficiencia del capital y adaptarse a distintos tipos de activos.

**Modelo clásico — x·y = k**:

El modelo original de Uniswap v2 y muchos AMM iniciales.
La fórmula establece que el producto de las cantidades de los dos tokens debe mantenerse constante. Si un usuario compra un token, su cantidad en el pool baja y la del otro sube, ajustando automáticamente el precio.
Este modelo es robusto y simple, pero reparte la liquidez de forma uniforme en todo el rango de precios posibles (de 0 a ∞), lo que significa que gran parte del capital permanece inactivo fuera del rango donde realmente se comercia.

Ejemplo simple:

Supongamos un pool con 10 ETH y 35 000 DAI (precio inicial: 1 ETH = 3.500 DAI).  

El valor total del pool es 70.000 DAI.  

Si un usuario compra 1 ETH, el pool debe mantener constante el producto x·y=k.  

Para ello, la cantidad de ETH baja a 9 y el DAI sube, por ejemplo, a 38.888.  

El nuevo precio resultante será 38 888 / 9 ≈ 4320 DAI por ETH.  

Así, el precio aumenta automáticamente conforme se reduce la cantidad de ETH disponible.

**Liquidez concentrada — Uniswap v3**:

Para mejorar la eficiencia, Uniswap v3 introdujo el concepto de liquidez concentrada, donde los proveedores eligen un rango de precios específico en el que su capital estará activo.
Cada posición se comporta como un pequeño x·y=k dentro de su rango.
Esto permite usar el capital de forma mucho más eficiente y aumentar los rendimientos por comisión, pero también incrementa el riesgo: si el precio sale del rango elegido, la posición se “desactiva” y el proveedor queda expuesto solo a uno de los tokens.

Ejemplo:

Si un proveedor coloca liquidez en el rango 3.000–4.000 DAI por ETH y el precio del ETH sube a 4.100 DAI, toda su liquidez se convierte en DAI, quedando fuera de actividad.

En ese momento ya no genera comisiones ni mantiene equilibrio entre ambos tokens: solo conserva DAI.

De forma inversa, si el precio cae por debajo de 3000, el proveedor mantiene únicamente ETH.

Este comportamiento introduce un riesgo crítico: el proveedor puede quedar atrapado con solo uno de los tokens, perdiendo completamente la exposición al otro.  
Cuando el precio sale del rango, el contrato habrá intercambiado casi todo un activo por el otro, de modo que el saldo de uno de ellos se reduce prácticamente a cero.  
Si el precio no regresa al rango, la posición permanece inactiva y el LP mantiene indefinidamente solo el token restante, sin generar comisiones.  
Por eso, en rangos estrechos, aunque la rentabilidad potencial sea alta, el riesgo de quedar totalmente fuera del mercado o de sufrir pérdidas permanentes aumenta de forma considerable.

**Modelos híbridos o especializados**:

Otros protocolos han diseñado fórmulas adaptadas a diferentes tipos de activos:

Constant sum (x + y = k): usada para stablecoins con precios similares, donde se busca baja volatilidad y mínimo deslizamiento.

Weighted product: usada por Balancer, donde cada token puede tener un peso distinto, permitiendo pools con múltiples activos y proporciones personalizadas.

Hybrid (Curve, Ellipsis): combinan las funciones anteriores, ajustando la curva para ofrecer alta eficiencia cuando los precios son estables (como stablecoins) y mayor elasticidad cuando se alejan del equilibrio.

Ejemplo:

En una pool de Curve entre DAI, USDC y USDT, si un usuario intercambia 1 millón de DAI por USDC, el precio apenas se mueve, porque la curva híbrida suaviza el deslizamiento en torno a 1:1.
Sin embargo, si se intenta intercambiar una cantidad enorme o un token pierde su paridad, la función se comporta más como un AMM tradicional, permitiendo que el precio se desplace para absorber el desequilibrio.

**Modelos dinámicos y estrategias adaptativas**:

Actualmente surgen enfoques donde la liquidez se reajusta de forma automática según la volatilidad o el comportamiento del mercado.
Algunos protocolos experimentales aplican estrategias dinámicas (τ-reset, auto-rebalancing) que modifican el rango de precios o redistribuyen liquidez sin intervención manual.
Estas técnicas buscan mantener la eficiencia de la liquidez concentrada sin exigir al usuario reposicionar constantemente sus fondos, reduciendo costes y riesgo de pérdida impermanente.

En conjunto, la evolución de las fórmulas en los AMM refleja la transición desde un modelo simple y universal a sistemas más inteligentes, adaptativos y orientados a la eficiencia del capital, que ajustan la curva de precios al comportamiento real del mercado.

#### Estrategias de provisión de liquidez

La provisión de liquidez en DeFi no es estática: cada proveedor elige cómo y dónde aportar capital según su tolerancia al riesgo, horizonte temporal y conocimientos técnicos. Con la evolución de los AMM, han surgido tres enfoques principales: estrategias pasivas, activas y automatizadas.

**Estrategias pasivas**:

Son las más simples y tradicionales. El proveedor deposita sus tokens en una pool y mantiene su posición sin realizar ajustes, confiando en las comisiones generadas por las operaciones del mercado.  
Este método funciona bien en modelos clásicos como Uniswap v2 o Balancer, pero resulta menos eficiente en entornos de liquidez concentrada, donde el rango de precios puede quedar rápidamente fuera de actividad.  
El riesgo principal es la pérdida impermanente, que puede superar los beneficios si el mercado se mueve bruscamente. Por ello, se recomienda usar pares de tokens estables o pools especializadas (por ejemplo, Curve para stablecoins), ya que minimizan la divergencia de precios.  
En el caso de proyectos que controlan la emisión o disponen de una tesorería, esta puede emplearse para mantener la liquidez o estabilizar el precio del token, pero no elimina la pérdida impermanente, solo ayuda a reducir la volatilidad y mitigar los efectos de movimientos especulativos en el mercado.

**Estrategias activas**:

El proveedor gestiona su posición de forma dinámica, reajustando los rangos de precio o migrando la liquidez según las condiciones del mercado.
En AMM modernos como Uniswap v3, esta estrategia permite mantener el capital en los tramos donde hay mayor volumen de operaciones, maximizando el rendimiento.
Sin embargo, requiere seguimiento constante, experiencia en análisis de precios y un equilibrio entre comisiones obtenidas y costes de reposicionamiento. En la práctica, solo usuarios avanzados o entidades profesionales logran hacerlo de manera rentable.

**Estrategias automatizadas o gestionadas**:

Para simplificar la gestión, han surgido protocolos que automatizan las decisiones de provisión de liquidez. Plataformas como Arrakis, Gamma, Charm o Automata redistribuyen los fondos dentro de los AMM en función de algoritmos de optimización o modelos de volatilidad.
Estas estrategias convierten la liquidez concentrada en una experiencia más pasiva, similar a un fondo indexado, donde el usuario delega la gestión a un contrato inteligente.
Aun así, implican confiar en el algoritmo y en la seguridad del protocolo gestor, lo que añade una capa de riesgo técnico.

En resumen, la provisión de liquidez ha evolucionado desde una actividad puramente pasiva a una disciplina estratégica que combina análisis, gestión de riesgo y automatización. El objetivo final es el mismo: maximizar el rendimiento sin comprometer el capital, manteniendo la eficiencia del mercado y la estabilidad del sistema DeFi.

### Haz que el dinero trabaje para ti 💪: yield farming

La agricultura de rendimiento tiene esa idea, a veces de marketing, de cultivar el dinero y hacer que trabaje para ti. En el ecosistema DeFi consiste en que, si dispones de un activo, bloquearlo durante un tiempo va a proporcionar un servicio y eso te va a recompensar a modo de comisiones o de nuevos tokens. Puede ser en préstamos, en la seguridad de un protocolo mediante staking, pero sobre todo se asocia el yield farming a las pools de liquidez, los AMM, donde encontramos tipos de yield farming como la minería de liquidez (liquidity mining) y otros derivados.

La liquidity mining, como tipo de agricultura, en realidad, tiene poco de minería y mucho de termino de marketing. DeFi adopta el término “minería” del proof of work (PoW) para darle legitimidad, cuando en realidad se trata premiar la provisión de liquidez, asegurando que los protocolos tengan los fondos necesarios. El objetivo es simple: asegurar que alguien mantenga liquidez mientras los incentivos duren.

En economía, tanto en TradFi como en DeFi, la seguridad del protocolo, la estabilidad de precios y la disponibilidad de liquidez son lo fundamental. La confianza en que los proveedores de liquidez permanezcan es esencial. Todo esto va, en el fondo, de asegurar que mantengas tu posición durante un tiempo y que no abandones la pool de liquidez. El “juego” consiste en eso: en incentivarte para que no retires tus fondos.

Los incentivos provienen tanto del propio emisor del token, que puede reservar parte de su tesorería para repartir recompensas a los holders, como de la plataforma DeFi, que actúa como intermediaria y busca fortalecer su posición de mercado siendo percibida como la más segura o la de mayor liquidez. Ahí entra en juego la métrica TVL (Total Value Locked), usada como indicador de confianza y como herramienta de marketing imprescindible. Pero no pensemos siempre en las plataformas como ángeles de la guarda: tienen sus propios intereses y moverán la liquidez allí donde obtengan más rendimiento. DeFi puede llegar a ser un juego peligroso.

En la mecánica de incentivos —y es eso, mecánica— existen diferentes variantes. Cada protocolo ofrece sus soluciones, pero lo común, dentro de la composabilidad de Web3, es cuando participas en una pool recibes y recibes un token fungible denominado LP (liquidity provider). Ese token representa tu participación y puedes usarlo para retirar los activos, como colateral en préstamos, venderlo como token fungible o, sobre todo, bloquearlo durante un tiempo para asegurar que la liquidez permanezca estable a medio o largo plazo.

Es un bucle de incentivos: bloqueas capital para obtener un token que puedes volver a bloquear para seguir participando en la rueda, por eso, a cambio de ese LP token, la plataforma DeFi puede darte otro token VE (vote-escrowed), es decir, un token bloqueado que otorga poder de voto en la gobernanza del protocolo. Pero no pienses que esa gobernanza significa decidir sobre el futuro del proyecto: eso es una fantasía. En la práctica, ese “voto” se usa para participar en un metajuego interno, donde se decide qué pools recibirán más incentivos. En lo personal, opino que aporta poco y que muchas veces es solo una coreografía donde no estás gobernando nada, solo moviendo la zanahoria de un lugar a otro..

Con DeFi 2.0 y la automatización mediante bóvedas y DAO, la dinámica se acelera. Las bóvedas buscan rentabilidad sin lealtad, los algoritmos mueven liquidez entre protocolos según el rendimiento del momento y los DAO votan estrategias que priorizan el beneficio colectivo sobre la estabilidad individual del token. Los stablecoins facilitan este juego: son el lubricante perfecto para entrar y salir sin fricción. Muchas pools usan como base el token del emisor y una stablecoin, lo que facilita el acceso, pero también la fuga. En cambio, pares como TOKEN-ETH amarran más al ecosistema y reducen el riesgo de una salida masiva… aunque nadie se queda mucho tiempo cuando el APR cae.

Este “juego” constante afecta a la economía interna de las pools y del propio token, que termina siendo tratado más como un activo especulativo que como un servicio o utilidad. En ese mercado secundario, el valor ya no proviene de la función del token, sino del intento de inflar o derrumbar su precio (el clásico pump and dump). Por eso, bloquear el token y asegurar su precio mediante mecanismos de vesting o vote-escrow se vuelve esencial para mantener la estabilidad del ecosistema.

Este ciclo constante acaba transformando el propósito original: el token deja de ser una utilidad y se convierte en una ficha de casino. En el mercado secundario, el precio ya no responde al valor del proyecto, sino a la pura especulación: inflar, drenar y repetir. Por eso el bloqueo del token, los mecanismos vote-escrow o el vesting son esenciales para mantener la estabilidad del ecosistema.

### Curva matemática que relaciona precio y emisión

Como alternativa a pools de liquidez, existen mecanismos en los que la compraventa de tokens no depende de la interacción entre usuarios ni de la provisión de liquidez por terceros.

Una bonding curve (curva de vinculación, en este contexto de emisión) es una función matemática que define cómo varía el precio de un token según su cantidad emitida o en circulación.

El contrato inteligente actúa como un mercado automatizado que vende y recompra el token directamente, sin necesidad de un order book ni de proveedores de liquidez.

El precio se calcula mediante una fórmula predefinida, de modo que cada compra o venta ajusta automáticamente el valor del token en función de la oferta.

**Tipos de bonding curves**:

- **Lineal:** el precio aumenta de forma proporcional al suministro.

  Ejemplo: `p(x) = a·x + b`  
  Adecuada para ventas o emisiones progresivas con crecimiento estable del precio.

- **Exponencial o cuadrática:** el precio crece más rápido a medida que aumenta el suministro.

  Ejemplo: `p(x) = a·x² + b`  
  Útil para limitar la entrada temprana y reforzar el valor de los primeros participantes.

- **Sigmoidal:** combina una fase inicial plana, una parte media empinada y una meseta final.

  Ejemplo: `p(x) = 1 / (1 + e^(-k(x - x₀)))`  
  Se usa para limitar el precio máximo y crear una distribución equilibrada.

- **Inversa:** el precio disminuye con el suministro o con el tiempo.

  Aplicada en modelos deflacionarios, recompensas o subsidios decrecientes.

**Ejemplos de uso en Web3**:

- **Financiación continua de DAOs:** los miembros compran y venden participaciones directamente en la curva, que mantiene liquidez constante.  

  Ejemplo: *Commons Stack*, *Giveth*.  

- **Mercados de NFT dinámicos:** el precio de cada NFT aumenta con cada compra y baja con cada reventa.

  Ejemplo: *Zora Protocol*, *Sound.xyz*.  

- **Tokens sociales o de acceso:** el precio sube a medida que crece la comunidad o el número de holders, reflejando la demanda real.

  Ejemplo: *Rally*, *Friend.tech*.  

- **Emisión o quema programada de tokens:** contratos que usan curvas para ajustar el precio de mint o burn de activos sintéticos o stablecoins.  

**Ventajas frente a una pool de liquidez**:

- Sin pérdida impermanente: solo interviene un activo colateral y un token emitido, por lo que no existen reequilibrios entre dos precios variables.  
- Liquidez garantizada: el contrato siempre compra y vende según la fórmula, sin depender de proveedores de liquidez ni de volumen en el mercado.  
- Gestión pasiva total: no requiere ajustar rangos, mover posiciones ni usar tesorerías para mantener estabilidad.  
- Precio determinista: el valor depende exclusivamente de la curva definida, eliminando arbitraje y manipulaciones externas.  
- Previsibilidad económica: se puede calcular de antemano el impacto exacto de cada compra o venta sobre el precio.  

**Inconvenientes frente a una pool de liquidez**:

- Liquidez limitada al colateral disponible: si el contrato se queda sin reserva, no puede recomprar tokens ni sostener el precio.  
- Ausencia de mercado libre: el precio no se ajusta por oferta y demanda entre usuarios, sino solo por la fórmula.  
- Riesgo de diseño: una curva mal parametrizada puede generar inflación excesiva o precios inalcanzables para nuevos participantes.  
- Sin arbitraje externo: no hay integración automática con otros AMM, por lo que el precio puede desviarse del mercado secundario.  
- Dependencia total del contrato: cualquier fallo o error matemático afecta directamente al mecanismo de compraventa.  

## El conflicto de intereses en DeFi

Los principales actores en DeFi son las DAOs, los proveedores de liquidez, los traders y los emisores de tokens. Cada uno responde a incentivos distintos: las DAOs buscan preservar y hacer crecer su tesorería, los proveedores de liquidez tratan de maximizar su rendimiento ajustado al riesgo, los traders persiguen rentabilidad inmediata y los emisores intentan equilibrar el crecimiento del protocolo con la sostenibilidad a largo plazo.

Lanzar un token al mercado equivale a salir a bolsa: el proyecto se expone a la volatilidad, la presión del precio y a una nueva relación con una comunidad que pasa a ser copropietaria. En este contexto, el diseño del token es esencial. El proyecto debe considerar en qué grado el token servirá como herramienta económica del protocolo o como instrumento financiero de inversión (mas especulativo). Cuando el token carece de utilidad real, su valor depende únicamente de la demanda especulativa, y cuando el interés se desvanece, su precio se desploma.

La liquidez también debe ser gestionada con visión de sostenibilidad. Incentivos excesivos atraen liquidez mercenaria, capital que entra solo para capturar recompensas y sale cuando los rendimientos disminuyen. Este comportamiento desestabiliza los pools y debilita la economía interna del protocolo.

Las propias DAOs pueden agravar estos conflictos. En algunos casos utilizan su tesorería o su poder de voto para sostener artificialmente el valor de su token o proteger la estabilidad interna del protocolo, incluso si ello perjudica a los holders o al mercado en general. Esto ocurre, por ejemplo, cuando una DAO destina fondos a comprar su propio token, a rescatar posiciones en riesgo o a mantener la paridad de una stablecoin emitida por el protocolo. Tales decisiones pueden ser racionales desde la perspectiva de la supervivencia del sistema, pero generan tensiones con los inversores que esperan rentabilidad y transparencia.

En definitiva, el equilibrio en DeFi depende de cómo se alinean los incentivos entre sus actores. La transparencia, la gobernanza equilibrada y un diseño económico coherente son las únicas defensas reales frente a los conflictos de interés que surgen de manera natural en sistemas abiertos y descentralizados.

## DeFi evoluciona: L2, fees, RWA, staking líquido y re-staking, cross-chain y ZK

La evolución de DeFi no se detiene en los modelos clásicos de intercambio y préstamos. Actualmente, el ecosistema está incorporando innovaciones que amplían su alcance y funcionalidad:

L2 (Layer 2) y reducción de fees: Las soluciones de segunda capa (L2) escalan redes como Ethereum procesando transacciones fuera de la cadena principal. Esto reduce drásticamente las gas fees y acelera la confirmación, permitiendo que los pequeños inversores y las operaciones de alta frecuencia sean viables en DeFi.

RWA (Real World Assets): DeFi está comenzando a integrar activos del mundo real, como bienes raíces, bonos y otros instrumentos financieros tradicionales, tokenizándolos para que puedan ser gestionados y negociados en la blockchain. Esto permite que el capital fluya entre el mundo cripto y la economía tradicional, abriendo nuevas oportunidades de inversión y escalabilidad.

Staking líquido y re-staking: El staking líquido permite a los usuarios bloquear sus tokens para obtener recompensas, pero sin perder la liquidez, ya que reciben tokens representativos que pueden usar en otros protocolos DeFi. El re-staking lleva este concepto más allá, permitiendo que los activos bloqueados se utilicen simultáneamente en múltiples redes o protocolos, maximizando el rendimiento y la eficiencia del capital.

Cross-chain: La interoperabilidad entre diferentes blockchains es clave para el futuro de DeFi. Los protocolos cross-chain facilitan la transferencia de activos y datos entre distintas redes, eliminando las barreras de liquidez y permitiendo que los usuarios accedan a servicios DeFi en cualquier ecosistema, sin importar la blockchain de origen.

ZK (Zero-Knowledge): Las tecnologías de pruebas de conocimiento cero están transformando DeFi al abordar dos retos clave: la privacidad y la escalabilidad, especialmente en el contexto de regulaciones cada vez más estrictas. Estas tecnologías permiten validar transacciones y estados sin revelar datos sensibles, lo que facilita el cumplimiento normativo al proteger la identidad y la información financiera de los usuarios. Además, los rollups ZK contribuyen a escalar las blockchains, procesando muchas transacciones fuera de la cadena principal y consolidándolas de forma segura, lo que reduce costes operativos y mejora la eficiencia sin sacrificar la transparencia ni la seguridad.

## Trading en DeFi

Derivados como los perpetual swaps y otros similares —futuros con vencimiento, opciones, activos sintéticos o swaps de rendimiento— pueden entenderse, **bajo mi punto de vista**, como el patio de recreo donde “los mayores” se encargan de conseguir cobertura de sus operaciones a costa de un retail de incautos; es decir, el abusón de siempre, robándome el bocadillo al pardillo; en lo que sería un juego de suma cero controlado. Es una especie de sandbox donde entras y te roban. Entras como retail porque te bombardean con anuncios; cambian de rostro, pero la estrategia es la misma y empezó en EE.UU hace ya unos 50 años, con el auge de los derivados financieros modernos, que marcaron el inicio del trading especulativo tal y como lo conocemos hoy. Ahora lo ves con cara de gente de 20 años, pero el guion es el mismo. Como se ve, no soy parcial…

DeFi también tiene esto. Quizás menos manipulación directa por su naturaleza descentralizada, pero sigue habiendo dinámicas parecidas: liquidez concentrada en pocos actores, bots y arbitraje constante, liquidaciones automáticas y apalancamiento que te saca del juego en segundos.

Sin embargo, también funcionan como una antesala al sentimiento de mercado, actuando como un mecanismo clave para el descubrimiento de precios. Los futuros y perpetuals reflejan expectativas colectivas, guiando el precio spot a través del arbitraje, donde los traders alinean mercados para explotar discrepancias. Este proceso, aunque imperfecto y a veces manipulado, aporta eficiencia y liquidez. Así, los derivados son tanto un campo de batalla desigual como una herramienta esencial para que el mercado "haga sentido" de sí mismo, un equilibrio que el retail debe navegar con cautela.

Este repositorio no pretende hablar del trading de derivados, solo mencionar que existe. Además este autor es el menos indicado por conocimiento e interés, además con una opinión claramente sesgada y parcial sobre el trading retail.

## La seguridad en DeFi

Ya hemos hablado de impermanent loss en los pools de liquidez, de las manipulaciones tipo pump & dump o incluso de los rug pulls, que son estafas en las que los desarrolladores o administradores del proyecto retiran los fondos y desaparecen.

Pero los riesgos en DeFi no acaban ahí. Existen también errores en los contratos inteligentes, inherentes a la naturaleza del código abierto y la descentralización. Una simple vulnerabilidad mal auditada puede ser suficiente para drenar millones de dólares en segundos. Los flash loan attacks, por ejemplo, aprovechan préstamos instantáneos para manipular precios y explotar contratos en un solo bloque.

A esto se suman los riesgos del propio protocolo, como fallos de diseño en los mecanismos de gobernanza, errores en los oracles de precios que provocan liquidaciones masivas, o incluso la dependencia de infraestructuras centralizadas (como frontends o APIs) que pueden ser hackeadas o censuradas.

También existen los llamados ataques vampiro, en los que un nuevo protocolo ofrece incentivos agresivos para atraer la liquidez de otro proyecto rival. Es una forma de competencia desleal que puede vaciar los pools del protocolo original, reduciendo su volumen, su liquidez y su capacidad de generar comisiones. El caso más conocido fue el de SushiSwap contra Uniswap en 2020.

Por otro lado, hay que tener en cuenta los riesgos de custodia y de llaves privadas, sobre todo en proyectos híbridos o CeDeFi. Si no controlas tus claves, no controlas tus fondos (Not your keys, not your coins).

Y, por supuesto, abundan los proyectos fraudulentos o esquemas Ponzi, que prometen rendimientos imposibles sin un modelo económico sostenible. Muchos usuarios caen en ellos por la apariencia de “éxito rápido” o por recomendaciones superficiales.

En este entorno, la seguridad no depende solo del protocolo: depende de ti. Siempre se debe insistir en el principio DYOR (Do Your Own Research), pero en DeFi es aún más relevante. Analiza el código o revisa si ha sido auditado, evalúa la liquidez bloqueada, la reputación del equipo, los canales de gobernanza y la actividad real de la comunidad.

DeFi ofrece innovación y libertad financiera, pero sin seguridad ni criterio, la descentralización no sirve de nada. La responsabilidad recae en el usuario: sé tu propio banco, pero también tu propio auditor.

## Otros servicios que surgen de DeFi

El ecosistema DeFi ha evolucionado mucho más allá de los simples préstamos y swaps de tokens. A partir de sus bases —liquidez, contratos inteligentes y gobernanza descentralizada— han surgido nuevos sectores y servicios complementarios que amplían sus usos reales.

Seguros DeFi: plataformas como Nexus Mutual o InsurAce ofrecen cobertura contra fallos de contratos inteligentes, exploits o pérdida de fondos. Actúan como aseguradoras descentralizadas donde los usuarios aportan capital y reciben recompensas por cubrir riesgos.

GameFi: combina juegos en blockchain con economías descentralizadas. Los jugadores pueden ganar tokens, NFT u otros activos con valor real mediante el modelo play-to-earn. Títulos como Axie Infinity o Gods Unchained integran elementos DeFi como staking, préstamos de NFT y mercados secundarios.

SocialFi: fusiona redes sociales con incentivos DeFi. Permite monetizar la interacción, la influencia o los contenidos a través de tokens y DAOs. Ejemplos: Lens Protocol, Farcaster o Friend.tech.

DeFi + IA: proyectos emergentes usan inteligencia artificial para optimizar estrategias de yield farming, análisis de riesgo o gestión de tesorerías descentralizadas, automatizando decisiones financieras complejas.

CeDeFi (Centralized + DeFi): híbridos donde exchanges centralizados ofrecen productos DeFi (staking, préstamos, vaults) pero con una capa de custodia y soporte regulado. Binance, por ejemplo, ha impulsado varios productos de este tipo.

Infraestructura de oráculos y datos: servicios como Chainlink, Pyth o Band Protocol proporcionan datos del mundo real (precios, clima, eventos) a los contratos inteligentes, esenciales para seguros, derivados y mercados predictivos.

NFT Finance (NFTFi): integra NFTs con DeFi. Se pueden usar como colateral para préstamos, fraccionarlos, alquilarlos o generar yield mediante su tokenización. Plataformas: Blend, NFTX, FloorDAO.

En conjunto, todos estos servicios forman la base del nuevo ecosistema Web3 financiero, donde cada capa —desde el juego hasta los seguros— se interconecta sin intermediarios tradicionales.

## El Padrino de DeFi: Andre Cronje

Andre Cronje es una figura icónica en DeFi, apodado el "Padrino de DeFi" por su impacto transformador. Su fama explotó con Yearn Finance (YFI) en 2020, un protocolo de yield aggregation que automatizaba rendimientos y lideró el "DeFi Summer", con un fair launch legendario que llevó a YFI a superar temporalmente a Bitcoin. Su estilo de "testing in production" y su rol en +20 proyectos (Hegic, Keep3r, etc.) generaron miles de millones en valor, aunque con controversias como exploits. Cronje no solo codifica; define tendencias, critica el hype y encarna el ethos crypto al priorizar comunidad sobre VCs.
Tras un retiro dramático en 2022, volvió en 2024 con Sonic Labs (evolución de Fantom) y en 2025 lanzó Flying Tulip, un presale reembolsable que recaudó $200M a $1B de valoración, con mecánicas innovadoras que protegen inversores. Su influencia persiste porque combina visión técnica con narrativa: sus fair launches, posts en X y críticas al oportunismo resuenan con devs y [degens](https://www.ledger.com/es/academy/glossary/degen). En 2025, Cronje sigue siendo el nombre que mueve mercados y comunidades, un "filósofo DeFi" cuyo próximo movimiento todos esperan.

## Utilidades

En el ecosistema DeFi existen múltiples herramientas que facilitan el seguimiento, análisis y gestión de protocolos, métricas y activos. Estas utilidades permiten tener una visión clara del estado del mercado y de los riesgos asociados.

[DeFi Pulse](https://defipulse.com/): una de las primeras plataformas en medir el Total Value Locked (TVL) de los protocolos DeFi. Permite comparar proyectos por capital bloqueado, rentabilidad, categoría (préstamos, DEX, derivados, etc.) y evolución histórica. Fue referencia durante el auge inicial de DeFi.

[DeFiLlama](https://defillama.com/): actualmente la herramienta más completa para monitorear el ecosistema. Ofrece métricas en tiempo real de TVL, ingresos, rendimiento por cadena, airdrops, bridges, yield farms y fees. También permite analizar protocolos multichain, comparar DEX, o ver datos consolidados de L2.

[Zapper](https://zapper.xyz/) y [Zerion](https://zerion.io/): permiten conectar una wallet y gestionar portafolios DeFi desde un único panel. Muestran balances, posiciones en staking, deuda, farming y NFTs, con interfaces visuales sencillas.

[Dune Analytics](https://dune.com/): plataforma de análisis basada en consultas SQL sobre datos on-chain. Los usuarios pueden crear dashboards personalizados y compartir estadísticas públicas sobre protocolos, volumen, o actividad de usuarios.

[DefiLlama APIs](https://defillama.com/docs/api) y dashboards agregadores: se usan también a nivel técnico para integrar métricas de rendimiento, precios y TVL en proyectos o documentación.

## Referencias

Cada enlace de ayuda representa un recurso adicional para profundizar en DeFi y su ecosistema. Puedes seguir descubriendo más en:

- [Introducción a DeFi (YouTube - Whiteboard Crypto, lista de reproducción)](https://www.youtube.com/watch?v=TlfOjahDGi0&list=PLaDcID4s1KronHMKojfjwiHL0DdQEPDcq&index=1)
- [Finematics (Web y recursos educativos)](https://finematics.com/)
- [Whiteboard Crypto (Canal de YouTube)](https://www.youtube.com/@WhiteboardCrypto)
- [Ethereum.org - DeFi](https://ethereum.org/es/defi/)
- [Academy Binance - Stablecoins](https://academy.binance.com/en/articles/what-is-a-stablecoin)
- [Cointelegraph - Launchpads](https://es.cointelegraph.com/news/launchpads-funding-ideas-not-products)

---

DeFi tiene una curva de entrada complicada, pero si entiendes sus pilares, motivaciones y orígenes, y haces un pequeño cambio mental, verás que detrás de explicaciones complejas o protocolos enrevesados, muchas veces hay conceptos sencillos. No intentes comprenderlo todo; la economía es compleja por naturaleza, y quizás necesites la perspectiva de alguien con formación económica. Lo importante es entender que, detrás de esas mecánicas, hay un “juego” de incentivos. Existen protocolos que nacen con la rentabilidad como fin y, sí, puede que tu instinto sea correcto: algunos no funcionan, y otros directamente son estafas. DeFi es tan complejo como la ambición humana, y a la vez, es lo que permite que el sistema siga funcionando. No lo juzgues tanto como yo; simplemente, entiéndelo.

---
