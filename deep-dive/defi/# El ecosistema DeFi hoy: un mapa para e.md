# El ecosistema DeFi hoy: un mapa para entender quién hace qué

Este no es un manual técnico. Es un mapa. Si te acercas a DeFi en 2026 sintiendo que es más complejo que en 2021 tienes razón: no porque la tecnología se haya complicado por capricho, sino porque el ecosistema ha desarrollado **roles especializados** que antes no existían. La distancia entre "depositar en una pool" y "depositar en una vault curada por Steakhouse Financial" no es solo de palabras: es la aparición de toda una capa profesional intermedia que hoy decide por ti.

Este documento sirve para tres tipos de lector:

- **Retail curioso** — quieres entender en qué te estás metiendo antes de meterte, o por qué tu vecino habla de "vaults", "LRTs" y "puntos" como si fueran cosas distintas a las de hace dos años.
- **Fundador** — vas a construir sobre DeFi y necesitas saber qué piezas existen, quién las opera y dónde están los puntos de fallo que vas a heredar.
- **Observador del espacio** (VC, analista, curioso técnico) — quieres una taxonomía que distinga ruido de estructura.

No vamos a explicar cómo funciona cada protocolo por dentro. Vamos a dibujar el barrio: quién vive aquí, qué hace cada uno, en qué lugares ocurre la actividad, y cómo te mueves tú dentro según quién seas.

---

## Parte 1 — Quién está en DeFi: el mapa de actores

DeFi en 2021 tenía básicamente tres actores: usuarios, protocolos y tokens. En 2026 hay al menos doce roles diferenciados, y muchos de ellos no existían cuando empezó la historia. Reconocerlos es la mitad del trabajo de entender el ecosistema.

### Actores que ponen capital

**Retail individual.** Persona que opera por su cuenta con su wallet. Hace swaps, deposita en algún producto de yield, a veces participa en gobernanza. El cambio respecto a 2021 es que ya no necesita entender cada protocolo: ahora puede delegar la gestión a un curador (más abajo).

**Power user / "degen".** Retail sofisticado que entiende loops de apalancamiento, hace farming activo entre varios protocolos, persigue programas de puntos antes de que se conviertan en airdrop. Asume riesgos altos a cambio de rendimiento bruto. Es minoría pero genera volumen desproporcionado.

**Tesorería de DAO.** El DAO de un protocolo (Uniswap, Aave, Arbitrum, ENS, etc.) tiene millones o cientos de millones en tokens y stables. Alguien tiene que decidir qué hacer con eso: diversificar, generar yield conservador, financiar contribuyentes. Esa decisión hoy se lleva en propuestas de gobernanza con análisis profesional detrás.

**VC y fondos cripto.** Dos especies distintas. Los **venture funds** invierten en equity y tokens prelanzamiento (vía SAFT, SAFE+token warrant). Los **liquid funds** operan posiciones DeFi como un hedge fund: yield estructurado, arbitraje cross-chain, market making.

**Institucional tradicional.** BlackRock, Franklin Templeton, Fidelity. Han entrado vía treasuries tokenizadas (BUIDL, BENJI) y vía ETFs. No interactúan directamente con DeFi permissionless, pero su capital se filtra por las capas de cumplimiento (CeDeFi, RWA).

**Market makers profesionales.** Wintermute, GSR, Flow Traders, Jump. Proveen liquidez tanto en exchanges centralizados como en pools concentradas de DEXs. No son "usuarios", son infraestructura.

### Actores que construyen

**Fundador / equipo de protocolo.** Construye un DEX, un mercado de lending, un vault, una stablecoin. Su trabajo en 2026 incluye decisiones que en 2021 no existían: qué L2 elegir, qué oráculo integrar, qué curador invitar a su mercado, cómo distribuir el token (ya casi nadie hace ICO; lo que hay son programas de puntos que terminan en airdrop).

**Curador.** **Esta figura es nueva y central.** Un curador es una entidad —puede ser una persona, una empresa o un colectivo— que diseña vaults: selecciona qué estrategias incluir, qué colaterales aceptar, qué parámetros de riesgo aplicar. Cobra una fee de gestión sobre los activos depositados. Nombres que verás: [Steakhouse Financial](https://www.steakhouse.financial/), Re7 Labs, MEV Capital, Block Analitica, Gauntlet (que también hace risk management para protocolos completos), [Chaos Labs](https://chaoslabs.xyz/). El curador es quien decide en tu nombre. Si depositas en una vault de Morpho, lo que importa no es Morpho: es quién curó esa vault.

**Solver.** Otra figura nueva. En las arquitecturas de "intents" (intenciones), tú declaras lo que quieres conseguir y un solver compite con otros para ejecutarlo de la mejor forma. Es invisible para el usuario pero ya mueve volumen importante en [CoW Protocol](https://cow.fi/), UniswapX, 1inch Fusion. Los solvers son a veces market makers profesionales operando bajo otro nombre.

**Operador de AVS (Actively Validated Service).** En el mundo del restaking, hay servicios que necesitan validadores: oráculos descentralizados, redes de disponibilidad de datos, secuenciadores compartidos. Quien corre la infraestructura de esos servicios es un operador de AVS.

**Validador y restaker.** El validador corre nodos para asegurar una blockchain (Ethereum, una L2). El restaker reutiliza su ETH stakeado para asegurar también AVS adicionales a través de [EigenLayer](https://www.eigenlayer.xyz/), Symbiotic o Karak. A cambio gana yield extra y asume riesgo extra (slashing por mala conducta en cualquiera de los servicios).

### Actores de servicio

**Proveedor de oráculos.** [Chainlink](https://chain.link/), [Pyth](https://pyth.network/), Redstone, Chronicle. Llevan precios del mundo real a los contratos. Sin ellos no hay lending ni derivados.

**Auditor / firma de risk management.** Trail of Bits, OpenZeppelin, Spearbit, Code4rena (que organiza auditorías competitivas), Cantina. Distintos de los curadores: estos verifican que el código no tiene fallos; los curadores deciden qué hacer con código que ya está auditado.

**Aseguradora descentralizada.** [Nexus Mutual](https://nexusmutual.io/), Sherlock. Cubren posiciones contra fallos de smart contract, depegs, hackeos. Cualquier análisis profesional de yield resta el coste del seguro al APY bruto.

**Infraestructura MEV.** Builders, searchers, relays. Ordenan transacciones dentro de cada bloque y extraen valor de ese ordenamiento. Para el usuario son invisibles pero le afectan en cada swap.

---

## Parte 2 — Los barrios del ecosistema

Si los actores son "quién", los barrios son "dónde". Cada barrio cumple una función económica distinta y ha desarrollado sus propias variantes.

### Mercados de intercambio (DEX)

Donde cambias un token por otro.

- **AMM clásico** ([Uniswap](https://uniswap.org/) v2, SushiSwap): pools donde todo el rango de precios tiene liquidez por igual. Sencillo, ineficiente, pero sigue dominando para tokens de cola larga.
- **AMM de liquidez concentrada** (Uniswap v3, PancakeSwap v3): los proveedores eligen el rango de precios donde quieren proveer liquidez. Más capital-eficiente pero requiere gestión activa.
- **Stableswap** ([Curve](https://curve.fi/)): optimizado para activos que deberían valer lo mismo (stables entre sí, ETH/stETH).
- **Order book on-chain** ([Hyperliquid](https://hyperliquid.xyz/), dYdX): libro de órdenes como en un exchange centralizado, pero on-chain. En 2026 Hyperliquid disputa volumen seriamente a los CEX.
- **Intents / agregadores de solver** (CoW Protocol, UniswapX, 1inch Fusion): el usuario no especifica ruta, declara intención. Solvers compiten.
- **Agregadores tradicionales** (1inch, Matcha, Odos, KyberSwap): consultan todas las fuentes y rutean automáticamente.

### Mercados de crédito (lending)

Donde depositas para que otros pidan prestado, o pides prestado contra colateral.

- **Pool compartido** ([Aave](https://aave.com/), Compound): todos los activos comparten un pool de riesgo. Si un colateral falla, afecta a todo el sistema. Es el modelo histórico.
- **Mercados aislados** ([Morpho](https://morpho.org/) Blue, Euler v2): cada par colateral/préstamo es un mercado independiente con sus propios parámetros. Si uno falla, los demás no. Sobre estos mercados aislados se construyen las vaults curadas.
- **CDP (Collateralized Debt Position)** ([Sky](https://sky.money/), antes MakerDAO; Liquity): bloqueas colateral y emites una stablecoin sobrecollateralizada (USDS/DAI, LUSD).
- **Tasa fija** ([Pendle](https://www.pendle.finance/), Notional, Term): te aseguran un tipo durante un periodo, separando principal y rendimiento.

### Yield y vaults

Donde delegas la generación de rendimiento.

- **Vaults nativas** ([Yearn](https://yearn.fi/)): protocolo dedicado a vaults con su propio modelo, sus estrategias internas y su token de gobernanza (YFI). Yearn es el pionero histórico de la categoría: en 2020 inventó el concepto de yield aggregator que después se generalizó como estándar (ERC-4626) y que hoy todo el mundo llama "vault". Su evolución a v3 separó estrategias y vaults, modelo que se parece al que después adoptó Morpho. Si entiendes Yearn, entiendes el concepto.
- **Vaults sobre infraestructura ajena** (vaults sobre [Morpho](https://morpho.org/) Blue, Sommelier): el protocolo base es solo plomería; los vaults los construyen curadores externos como Steakhouse Financial, Re7 Labs, MEV Capital. La separación entre infraestructura y curación es explícita.
- **Vaults institucionales**: mismo concepto que las anteriores pero con requisitos de KYC/acreditación; lo opera un curador con mandato de cliente institucional.
- **Productos estructurados con opciones** (Aevo, antes Ribbon): venden opciones cubiertas o spreads para generar yield.

### Restaking y validación

Donde el ETH (u otro activo) gana rendimiento por asegurar redes.

- **Staking líquido** ([Lido](https://lido.fi/) → stETH, Rocket Pool → rETH, Frax → sfrxETH): stakeas ETH, recibes un token líquido que representa tu posición y puedes seguir usando en DeFi.
- **Restaking** (EigenLayer, Symbiotic, Karak): el ETH ya stakeado vuelve a comprometerse para asegurar AVS adicionales.
- **Liquid Restaking Tokens, LRT** ([ether.fi](https://ether.fi/) → eETH, Renzo → ezETH, KelpDAO → rsETH, Puffer → pufETH): el equivalente líquido de una posición de restaking. Son los activos más usados como colateral en los loops de yield apalancado de 2024-2026.

### Stablecoins

No es un único producto: es una familia con riesgos muy distintos.

- **Centralizadas** (USDC de Circle, USDT de Tether): respaldadas por activos en cuentas bancarias. Riesgo: el emisor.
- **Sobrecollateralizadas on-chain** (USDS/DAI, LUSD): respaldadas por cripto bloqueada en contratos. Riesgo: caídas violentas del colateral.
- **Sintéticas delta-neutral** (USDe de [Ethena](https://www.ethena.fi/)): respaldadas por una posición larga en spot y corta en perpetuos que se cancelan. Riesgo: tasas de financiación negativas prolongadas, riesgo de exchange.
- **Yield-bearing** (sUSDe, sDAI/sUSDS, sFRAX): versiones de las anteriores que pagan yield al tenedor. Han cambiado profundamente cómo retail piensa en "tener stables".

### Derivados

- **Perpetuos** (Hyperliquid, GMX, dYdX, Aevo): contratos sin vencimiento con financiación periódica. Es el segmento que más volumen mueve en DeFi.
- **Opciones** (Aevo, Lyra, Premia): mucho menos volumen que perps, pero clave para productos estructurados.
- **Yield trading** (Pendle): se separa el principal de un activo que paga yield (un LRT, un sDAI) y se negocian por separado. Muy usado para apostar a la dirección del rendimiento futuro.

### Activos del mundo real (RWA)

- **Treasuries tokenizadas** ([Ondo](https://ondo.finance/) USDY, BlackRock BUIDL, Franklin BENJI): bonos del Tesoro de EEUU empaquetados como token.
- **Crédito privado** (Maple, Goldfinch, Centrifuge): préstamos a entidades reales tokenizados.
- **Otros activos** (oro tokenizado, real estate fraccional): existen pero el volumen serio está en treasuries.

### Bridges y mensajería cross-chain

- **Bridges canónicos** de cada L2: la vía oficial entre la L1 y su rollup.
- **Bridges de mensajería general** (LayerZero, Wormhole, Axelar, Hyperlane): permiten que un contrato en una cadena llame a otro en otra cadena.
- Han sido el vector de ataque más explotado de la historia de DeFi. Cualquier estrategia cross-chain hereda este riesgo.

### Distribución y lanzamiento

- **Programas de puntos**: el equivalente actual del ICO. Acumulas puntos por usar el protocolo y te dan tokens cuando se lanzan. Lo inventó Blur, hoy lo hace casi todo el mundo.
- **Lanzamientos directos** (LBP en Fjord, fair launches en plataformas como Pump.fun para memecoins).
- **Airdrops** condicionados a actividad histórica.

### Mercados especiales

- **Mercados de predicción** ([Polymarket](https://polymarket.com/)): apuestas sobre eventos del mundo real, liquidadas por oráculos. Volumen real, no juguete.
- **NFT financieros** (lending sobre NFT, fraccionalización): existe pero ha quedado como nicho tras el invierno de 2022-2023.

---

## Parte 3 — Recorridos según quién eres

El mismo mapa, leído desde cuatro perspectivas distintas.

### Si eres retail curioso

Tu recorrido natural en orden de complejidad:

1. **Custodia y swap.** Aprender a manejar una wallet, hacer swaps en un agregador (1inch, Matcha), entender slippage y fees de red. Si esto no es sólido, lo demás no importa.
2. **Stablecoins yield-bearing.** Es probablemente el primer producto DeFi que tiene sentido para alguien sin experiencia: tener "dólares" que pagan rendimiento (sDAI/sUSDS, sUSDe). Los riesgos son acotados y comprensibles. **Esto es la "boveda" que mencionabas**: tú depositas, el rendimiento llega solo, no necesitas hacer nada. La diferencia con una pool tradicional es que no estás proveyendo liquidez para otros traders, simplemente posees un activo que rinde.
3. **Vaults curadas.** Un escalón arriba. Aquí sí estás eligiendo a un gestor. La pregunta clave es **quién es el curador y qué mandato tiene**. Una vault de Morpho curada por Steakhouse Financial no tiene los mismos riesgos que otra del mismo Morpho curada por alguien anónimo.
4. **Liquid staking y restaking.** Tener ETH que gana yield (stETH, rETH) es razonable. Tener LRTs es un escalón más: ganas más yield, asumes más riesgo de correlación entre AVS.
5. **Provisión de liquidez en DEX.** Aquí entras a operar de verdad. La impermanent loss en pools concentradas no es trivial.
6. **Derivados y apalancamiento.** Ya estás en territorio profesional.

Lo que necesitas vigilar siempre, en cualquier punto del recorrido:

- **Quién custodia tu posición.** Si la respuesta no es "yo", asume que puede salir mal.
- **De dónde sale el rendimiento.** Si el APY es alto y nadie sabe explicar por qué, sale de inflación de un token de gobernanza, y eso colapsa cuando se acaba el incentivo.
- **A qué oráculos y puentes está expuesto el producto.** Casi nunca aparece en la interfaz, casi siempre es el punto de fallo cuando hay un hackeo.

### Si eres fundador

Tus decisiones de partida, en orden:

1. **Dónde despliegas.** Ethereum mainnet es caro pero da prestigio y composabilidad. Una L2 (Base, Arbitrum, Optimism) es donde está el volumen retail. Una appchain (vía OP Stack, Arbitrum Orbit, Hyperliquid) te da control pero te aísla. Una L1 alternativa (Solana) tiene su propio ecosistema.
2. **Qué primitivos consumes.** Si haces lending, ¿construyes desde cero o lanzas un mercado sobre Morpho Blue / Euler? Lo segundo es 2026, lo primero es 2020.
3. **Qué oráculos integras.** Chainlink es el estándar conservador. Pyth es más rápido y sensible. La elección impacta perfil de riesgo.
4. **Cómo creas liquidez para tu token.** Pool en Uniswap v3 (capital-eficiente, requiere gestionar el rango), Curve (si es algo similar a stable), Aerodrome/Velodrome (si despliegas en Base/Optimism y quieres pagar por liquidez con votes), o LBP en Fjord para el lanzamiento inicial.
5. **Cómo gestionas tu tesorería.** Casi todo fundador serio en 2026 parquea el USDC de la ronda en treasuries tokenizadas (BUIDL, USDY) o en sUSDS. Tener millones en USDC quieto es perder dinero.
6. **Cómo distribuyes el token.** Programas de puntos seguidos de airdrop son el patrón dominante. Hay que tener pensada la distribución antes del primer punto.
7. **Quién hace risk management.** Si construyes algo donde el riesgo importa (lending, derivados, vaults), Gauntlet o Chaos Labs es una conversación que vas a tener.
8. **Quién audita.** Mínimo dos auditorías de firmas reconocidas más una competitiva en Code4rena o Cantina antes de manejar capital ajeno.

Lo que vas a heredar quieras o no:

- El riesgo de cada oráculo que uses.
- El riesgo de cada puente si haces algo cross-chain.
- El riesgo de cualquier protocolo sobre el que construyas.
- El riesgo de cualquier curador que invites a tu protocolo, si tu protocolo permite curación externa.

Tu protocolo es solo una capa más en una pila que tú no controlas entera. Esto es verdad incluso si tu equipo escribe todo el código.

### Si eres tesorería de DAO

Tu trabajo es distinto del retail aunque uses los mismos productos.

- Necesitas **diversificación real**. Estar 100% en tu propio token significa que la salud financiera del DAO depende del precio del token, justo cuando una caída es el momento en que más necesitas munición.
- Usas **yield conservador**: sUSDS, treasuries tokenizadas (BUIDL, USDY, BENJI), stETH para la parte en ETH. Yields agresivos no son tu trabajo.
- Provees **liquidez en tu propio par** (tu token contra ETH o stable) porque sin eso no hay mercado secundario sano.
- Tienes que **votar en los protocolos donde tienes posición**. Si tienes COMP, tu voto importa en Compound. Olvidarte de eso es ceder poder.
- Cualquier movimiento mayor pasa por **propuesta de gobernanza** con análisis profesional. Esto es lento. Acéptalo.

### Si eres VC o liquid fund

- Si eres venture, tu producto principal sigue siendo equity y tokens prelanzamiento. Tu valor añadido es ayudar al fundador a navegar el resto del mapa: tokenomics, distribución, conexiones con curadores, market makers, exchanges.
- Si eres liquid, operas como hedge fund: yield estructurado en vaults curadas, arbitraje cross-chain entre L2s, market making concentrado, posiciones direccionales en perps. La frontera con un trading desk profesional es cada vez más fina.

---

## Parte 4 — Qué cambió desde 2021 (y por qué hoy es así)

Si te ayuda más entender de dónde viene la complejidad que su forma actual:

**De pool compartido a mercados aislados.** En 2021 todos depositábamos en Aave en un único pool. Si un colateral exótico fallaba, el riesgo se propagaba a todos. Después del colapso de Terra/LUNA en mayo de 2022 quedó claro que componer riesgos sin separación formal era frágil. Morpho Blue y Euler v2 separaron cada par en su propio mercado. Aave respondió con su propio modelo de aislamiento. Esta es la razón principal por la que aparecieron los curadores: alguien tiene que componer mercados aislados en productos accesibles.

**Apareció la figura del curador.** Ya no es razonable esperar que el retail entienda cada mercado individual. La gestión de riesgo se profesionalizó. El concepto no es nuevo —Yearn lo inventó en 2020 con sus primeras vaults, donde estrategias automatizadas decidían en nombre del depositante— pero ha pasado de ser un caso aislado a ser la arquitectura dominante: hoy hay decenas de curadores compitiendo sobre infraestructura compartida (Morpho, Euler) en lugar de uno solo operando su propio protocolo. Esto te da accesibilidad a cambio de tener que confiar en alguien explícito.

**Restaking.** EigenLayer en 2023 abrió la posibilidad de que el mismo ETH stakeado asegurara más servicios. Encima nacieron los LRTs como tokens líquidos de esas posiciones. Encima de los LRTs nacieron loops de apalancamiento. Encima de esos loops, riesgos de correlación que aún no han tenido un test de estrés serio.

**L2s baratos y ubicuos.** Base, Arbitrum, Optimism. Los costes de transacción bajaron uno o dos órdenes de magnitud. La actividad retail migró fuera de mainnet. Esto creó fragmentación de liquidez que los agregadores y los intents intentan resolver.

**Stablecoins que pagan yield.** sDAI/sUSDS, sUSDe, sFRAX. La idea de "tener un dólar" se convirtió en "tener un dólar que rinde". Cambió el comportamiento de las tesorerías y de los retail más informados.

**RWA en serio.** BlackRock lanzó BUIDL en 2024. Ondo, Maple, Centrifuge maduraron. El capital institucional ya tiene puentes hacia DeFi sin tener que tocar DeFi permissionless.

**Intents.** Pasamos de "el usuario especifica la ruta" a "el usuario declara qué quiere y solvers compiten". Cambia el modelo adversarial: el MEV que antes te robaban bots ahora se subasta y vuelve parcialmente al usuario.

**Hyperliquid y los perps on-chain serios.** El order book on-chain dejó de ser una promesa. Compite por volumen con exchanges centralizados.

**Programas de puntos como pre-airdrop.** Inventado por Blur en 2022, hoy es el patrón dominante de distribución. Tiene su propia economía paralela: hay quien farmea puntos profesionalmente.

**CeDeFi y cumplimiento.** ZK proofs para verificar atributos regulatorios (residencia fiscal, acreditación) sin exponer datos. Polygon ID y otros. Esto no es DeFi traicionando sus principios; es la respuesta pragmática a dónde está el capital grande.

---

## Parte 5 — Vocabulario imprescindible (en una línea cada uno)

Si has llegado hasta aquí pero alguno de estos términos te bloqueaba, esta es la traducción rápida:

- **Vault**: contrato donde depositas un activo y un curador opera estrategias con él en tu nombre.
- **Curador**: persona o entidad que decide qué hace una vault. Cobra fee.
- **Pool**: contrato donde varios usuarios depositan activos para que otros los usen (intercambien, tomen prestado, etc.).
- **Oráculo**: servicio que lleva precios externos a la blockchain. Punto de fallo crítico.
- **Bridge / puente**: contrato que mueve valor entre dos cadenas. Vector de ataque histórico.
- **MEV (Maximal Extractable Value)**: valor extraíble por reordenar, insertar o censurar transacciones dentro de un bloque. Te afecta aunque no lo veas.
- **Intent**: declaración de "esto es lo que quiero conseguir", sin especificar cómo. Solvers compiten para ejecutarla.
- **Solver**: agente que ejecuta intents.
- **Liquid Staking Token (LST)**: token líquido que representa una posición de staking (stETH, rETH).
- **Restaking**: comprometer ETH ya stakeado para asegurar servicios adicionales.
- **AVS (Actively Validated Service)**: servicio asegurado por restaking (oráculo, DA, secuenciador, etc.).
- **Liquid Restaking Token (LRT)**: token líquido de una posición de restaking (eETH, ezETH, rsETH).
- **Slashing**: castigo a un validador por mala conducta. Le retiran parte de su stake.
- **CDP (Collateralized Debt Position)**: posición donde bloqueas colateral y emites una stablecoin contra él (DAI/USDS, LUSD).
- **Impermanent loss**: pérdida que sufre un proveedor de liquidez en AMM cuando el precio se mueve respecto al momento del depósito.
- **APY emisión vs APY actividad**: el primero viene de imprimir tokens nuevos (frágil); el segundo de fees pagadas por usuarios reales (sostenible).

---

## Parte 6 — El mapa por dentro: cómo se accede y qué se arrastra

Hasta aquí hemos descrito actores, barrios y recorridos como si fueran cosas separables. En la práctica no lo son: cada actor entra al ecosistema por una vía concreta, y cada pieza visible arrastra una cadena de piezas invisibles que la sostienen. Esta parte traza ambas cosas.

### Cómo accede cada actor

Un retail con una wallet con Account Abstraction llega hoy a casi todo el ecosistema sin firmar transacciones de bajo nivel. Cuando quiere intercambiar un token por otro, no elige pool ni ruta: firma una intención que un solver ejecuta por él en CoW Protocol o UniswapX, o pasa por un agregador como 1inch que enruta entre todas las pools disponibles y le devuelve el mejor precio. Cuando quiere generar yield, no estudia mercados: deposita en una vault y delega en su curador, o simplemente posee una stablecoin que rinde por sí misma como sUSDS o sUSDe. Su mapa subjetivo es pequeño y plano: wallet, producto, resultado. Toda la complejidad ocurre debajo y no necesita verla para operar, lo cual es a la vez la gran conquista del ecosistema actual y su mayor peligro pedagógico, porque facilita olvidar que esa complejidad existe.

El fundador habita un mapa completamente distinto. Para él los protocolos no son productos sino piezas de infraestructura sobre las que decide construir. Cuando necesita liquidez para su token despliega una pool en Uniswap v3 si quiere capital-eficiencia, paga por liquidez con votos en Aerodrome si está en Base, o lanza un evento inicial con un LBP en Fjord. Cuando necesita parquear el USDC que levantó en la ronda lo lleva a sUSDS o a treasuries tokenizadas como BUIDL o USDY, porque tener millones quietos es perder dinero. Cuando su producto requiere un mercado de lending no construye uno desde cero como en 2020, sino que lanza un mercado aislado sobre Morpho Blue o Euler v2. Y cuando quiere ofrecer un vault a sus usuarios, o lo cura él mismo o invita a un curador externo —Steakhouse Financial, Re7 Labs, MEV Capital— a operar bajo su marca con su mandato. Para el fundador el ecosistema no es un menú de productos sino un conjunto de bloques de Lego con interdependencias explícitas que él combina.

Una tesorería de DAO se mueve por un mapa más estrecho pero más cargado de proceso. No accede a nada directamente: cualquier movimiento serio pasa por una propuesta de gobernanza con análisis cuantitativo detrás, frecuentemente preparado por Gauntlet o Chaos Labs si el DAO ya tiene relación con esas firmas. Las piezas que toca son las más conservadoras del ecosistema, porque su trabajo no es maximizar yield sino preservar capacidad operativa: stables yield-bearing como sUSDS, treasuries tokenizadas, posiciones de liquid staking en stETH para la parte denominada en ETH, y la pool de su propio par contra ETH o stable porque sin liquidez en mercado secundario el token del DAO no es realmente líquido. Lo que distingue a una tesorería bien gestionada en 2026 de una mal gestionada no es el rendimiento que obtiene sino la diversificación real que mantiene y la disciplina con la que evita dependencias de su propio token.

Un VC se mueve por dos mapas distintos según su tipo. El venture casi no toca DeFi como producto: invierte en equity y en tokens prelanzamiento mediante SAFTs, y su valor añadido para el fundador está en ayudarle a navegar el mismo mapa que él no opera directamente, conectándolo con curadores, market makers, exchanges y otros fundadores. El liquid, en cambio, opera como un hedge fund tradicional con instrumentos cripto: yield estructurado en vaults curadas, separación de principal y rendimiento en Pendle para apostar a la dirección del yield futuro, posiciones direccionales en perpetuos de Hyperliquid, arbitraje cross-chain entre L2s. La frontera entre un VC liquid y un trading desk profesional es cada vez más fina, y muchos antiguos analistas de venture han migrado a esta operativa porque permite generar retornos sin esperar al ciclo largo de las inversiones tempranas.

### Cadenas de dependencia

Lo que a un usuario le aparece como "una vault" es en realidad la punta visible de una cadena que desciende hasta capas que él raramente ve. Esa vault toma capital y lo despliega en estrategias que viven sobre uno o varios mercados de lending; cada uno de esos mercados consulta uno o varios oráculos para precios; cada oráculo a su vez agrega fuentes externas y tiene su propio modelo de actualización y de tolerancia a manipulación. Si la vault opera en más de una cadena, hay un puente o un protocolo de mensajería conectándolas, con su propio modelo de seguridad, sus propios validadores y su propia historia. Y si los activos depositados son LRTs, debajo hay una pila adicional: el restaking que respalda al LRT depende de una red de validadores cuya buena conducta determina si el activo se mantiene íntegro o se reduce por slashing, y cada AVS asegurado por ese restaking añade un compromiso más al mismo capital subyacente.

La regla práctica que organiza todo esto es sencilla de enunciar y difícil de interiorizar: las garantías de seguridad de cada capa no se propagan hacia arriba por defecto. Una vault muy bien diseñada sobre un mercado mediocre hereda el riesgo del mercado. Un mercado muy bien parametrizado sobre un oráculo manipulable hereda el riesgo del oráculo. Una posición muy bien gestionada en una cadena que se conecta vía un puente débil hereda el riesgo del puente. Y a la inversa: protocolos que individualmente serían excelentes pueden componerse en productos cuya seguridad efectiva es la del eslabón más débil de toda la cadena que los une, porque la composabilidad que hace poderoso a DeFi es exactamente el mismo mecanismo que propaga sus fallos.

Esa es la razón por la que analizar DeFi protocolo por protocolo, como hacían los primeros dashboards y como sigue haciendo buena parte del análisis amateur, es engañoso. Lo relevante para un usuario que deposita en algo, o para un fundador que construye encima de algo, no es la seguridad de la pieza visible sino la del recorrido completo de dependencias que tiene debajo. Esa cadena rara vez aparece en la interfaz, casi nunca en los dashboards de TVL, y casi siempre es donde se origina el daño cuando algo se rompe. Trazarla es trabajo del usuario informado, del curador profesional o del auditor; descansar en que "el protocolo está auditado" sin haberla trazado es exactamente el error que el ecosistema lleva pagando desde 2020.

## Cómo seguir desde aquí

Este mapa es deliberadamente plano: presenta a todos los actores y todos los barrios al mismo nivel, sin entrar en cómo funciona cada uno por dentro. Eso es trabajo de los siguientes deep-dives, que pueden organizarse por barrio (un documento sobre vaults curadas, otro sobre restaking, otro sobre RWA, otro sobre stablecoins yield-bearing) o por actor (un manual del curador, un manual del fundador en lending, un manual de tesorería de DAO).

Si vuelves a este documento dentro de seis meses y notas que algo de lo que dice ya no cuadra, no te asustes: el mapa cambia. Los actores que hoy son centrales pueden ser nicho mañana, y al revés. Lo que difícilmente cambiará es la estructura: capital, infraestructura, curación, riesgo heredado. Esa pila es la que conviene tener clara.
