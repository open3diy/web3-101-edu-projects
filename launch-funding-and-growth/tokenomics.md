# Tokenomics

Un tokenomics no es una hoja de cálculo con números. Es un contrato social codificado que diseña las reglas para que participantes egoístas, cada uno persiguiendo su propio beneficio, produzcan un resultado colectivo que sostenga el protocolo de forma descentralizada. Es, en esencia, un [equilibrio de Nash](https://es.wikipedia.org/wiki/Equilibrio_de_Nash) aplicado: un estado donde ningún participante puede mejorar su posición cambiando de estrategia unilateralmente, porque las reglas hacen que cooperar sea más rentable que traicionar.

Por eso un tokenomics es siempre un documento de concesiones. Cada decisión de diseño es un toma y daca: dar más incentivos de crecimiento significa aceptar más inflación. Exigir más seguridad significa sacrificar velocidad de adopción. Priorizar la sostenibilidad implica frenar el crecimiento inicial. No existe un tokenomics que maximice todo simultáneamente, y quien prometa uno está mintiendo o no entiende lo que diseña.

Estas concesiones operan entre tres dimensiones que deben mantenerse en equilibrio:

La dimensión de **crecimiento** agrupa todo lo que atrae participantes y capital: airdrops, incentivos de liquidez, recompensas agresivas, programas de referidos, emisiones altas en las primeras fases. Son las palancas que arrancan el motor. Sin ellas, nadie llega. Pero si dominan sin contrapeso, el protocolo se convierte en un juego especulativo donde el capital mercenario entra, extrae rendimiento, y se va dejando un cadáver inflacionario.

La dimensión de **valor** agrupa todo lo que da sentido al protocolo: la utilidad real del token, la captura de comisiones, la demanda orgánica que genera el producto, el efecto red que hace que cada nuevo usuario incremente el valor para todos los demás. Es lo que convierte un token en algo más que un número en una pantalla. Sin utilidad real, los incentivos de crecimiento son una subvención temporal que se agota.

La dimensión de **seguridad y sostenibilidad** agrupa todo lo que protege al protocolo a largo plazo: el staking y slashing que aseguran la red, los mecanismos de quema que controlan la inflación, los ve-tokenomics que reducen la velocidad de circulación, los timelocks que previenen ataques de gobernanza, y los presupuestos de seguridad que garantizan que atacar el sistema sea más caro que defenderlo. Sin esta dimensión, un protocolo exitoso es un protocolo con un cartel de "róbame" colgado en la puerta.

Ningún tokenomics nace perfecto. Todo diseño inicial es una hipótesis educada que el contacto con la realidad modificará. Si el tokenomics se diseña como un sistema cerrado con reglas inmutables, fracasará cuando las condiciones cambien, y cambiarán. Si se diseña como un decreto impuesto por los fundadores sin consenso con la comunidad, nadie lo adoptará como propio, y un tokenomics sin comunidad que lo sostenga es solo código muerto. Los mecanismos de evolución y el consenso comunitario no son extras opcionales: son requisitos de supervivencia. Cómo preparar esa evolución [se detalla más adelante](#evolución-y-consenso-el-tokenomics-como-sistema-vivo).

Al igual que un banco central define política monetaria, los diseñadores de un token definen parámetros equivalentes: cuántos tokens existirán, cómo se distribuyen, quién los recibe y por qué, qué mecanismos sostienen su valor, y qué ocurre cuando alguien los vende. La diferencia es que en Web3 esas reglas se codifican en smart contracts y, una vez desplegadas, nadie puede cambiarlas sin el consentimiento de la comunidad.

## Gestión de la oferta: la primera concesión

La primera decisión de cualquier tokenomics es cuántos tokens existirán y cómo entrarán en circulación. Parece una decisión técnica, pero es profundamente política: determina cuánta capacidad tendrá el protocolo para incentivar crecimiento futuro, cuánta dilución sufrirán los holders actuales, y cuánta rigidez o flexibilidad tendrá el sistema ante lo inesperado. Es la primera gran concesión entre las tres dimensiones: un supply fijo favorece la sostenibilidad pero limita el crecimiento; un supply flexible favorece el crecimiento pero genera incertidumbre sobre el valor.

**Oferta fija**:

Se define un número máximo de tokens que nunca se superará. [Bitcoin](https://bitcoin.org/bitcoin.pdf) fijó 21 millones como límite absoluto, creando escasez programática que, combinada con demanda creciente, tiende a apreciar el valor. La ventaja es la previsibilidad total: cualquiera puede calcular cuánta dilución habrá en el futuro, y la respuesta es cero. El trade-off es la rigidez: si el ecosistema necesita más incentivos de los previstos para sobrevivir una crisis o financiar un crecimiento inesperado, no hay margen para emitir. La sostenibilidad gana, pero el crecimiento queda atado.

**Oferta dinámica**:

ETH tras [The Merge](https://ethereum.org/roadmap/merge/) opera con emisión continua compensada por quema. Cada transacción destruye parte de las comisiones (la base fee bajo [EIP-1559](https://eips.ethereum.org/EIPS/eip-1559)), así que cuando la actividad de la red es alta se quema más de lo que se emite, y cuando la actividad baja ocurre lo contrario. Este equilibrio dinámico conecta la política monetaria directamente con el uso real del protocolo: la dimensión de valor regula automáticamente la sostenibilidad. Dogecoin, por contraste, tiene emisión constante sin quema, lo que produce inflación perpetua, una apuesta por accesibilidad (crecimiento) que sacrifica la sostenibilidad del precio.

**Oferta elástica**:

Algunos tokens ajustan su oferta algorítmicamente según la demanda. [Ampleforth](https://www.ampleforth.org/) (AMPL) implementa rebasing: si el precio sube por encima del objetivo, el protocolo aumenta el supply en todas las wallets proporcionalmente; si baja, lo reduce. [RAI](https://reflexer.finance/) de Reflexer usaba un controlador PID inspirado en ingeniería de control para ajustar su precio de referencia gradualmente. Son modelos experimentales que intentan resolver la concesión de raíz: mantener estabilidad sin hipotecar ni el crecimiento ni la sostenibilidad. Los resultados han sido mixtos, pero ilustran que la gestión de oferta no tiene por qué ser estática.

**Vesting: los calendarios de desbloqueo como alineación temporal**:

Los tokens asignados a fundadores, inversores y equipo no deberían estar disponibles desde el primer día. El vesting controla cuándo esos tokens se vuelven líquidos, y su diseño es una concesión directa entre las tres dimensiones. Un vesting corto permite que el equipo tenga liquidez pronto (crecimiento), pero crea riesgo de dump masivo que destruye el precio (sostenibilidad). Un vesting largo protege el precio, pero puede desmotivar a contribuidores que necesitan pagar facturas. El patrón habitual es cliff + linear: un periodo inicial donde no se libera nada (típicamente un año, señal de compromiso), seguido de liberación gradual durante tres o cuatro años adicionales (alineación progresiva).

El momento del lanzamiento, el Token Generation Event (TGE), define qué porcentaje del supply total estará circulando desde el primer momento. Un float demasiado bajo (menos del 10%) causa volatilidad extrema porque cualquier compra o venta mueve el precio significativamente. Un rango saludable suele estar entre el 15% y el 30% del supply circulante en TGE. Los calendarios de desbloqueo deben ser públicos y verificables on-chain desde antes del lanzamiento, porque los eventos de unlock masivos crean presión vendedora previsible que los inversores informados anticipan.

**Quema y deflación: reducir la oferta como mecanismo de sostenibilidad**:

Quemar tokens significa destruirlos permanentemente, reduciendo la oferta total. [Binance](https://www.binance.com/) ejecuta quemas trimestrales de BNB usando el 20% de sus beneficios operativos hasta alcanzar un supply objetivo de 100 millones de tokens. Ethereum quema la base fee de cada transacción continuamente. Estos mecanismos operan en la dimensión de sostenibilidad: crean presión deflacionaria proporcional al uso real del protocolo, lo que sostiene el valor para quienes se quedan.

El riesgo es la espiral deflacionaria: si la quema es demasiado agresiva, incentiva el holding extremo y nadie usa el token para su función real, lo que mata la dimensión de valor. La quema funciona cuando es proporcional a la actividad real y absorbe la inflación de las emisiones de crecimiento, no cuando es un artificio para sostener el precio artificialmente.

## Utilidad del token: la dimensión de valor

Un token sin utilidad real es solo un activo especulativo cuyo precio depende exclusivamente de que alguien esté dispuesto a pagar más que tú. La utilidad es lo que ancla la dimensión de valor: crea demanda orgánica que sostiene el precio independientemente del sentimiento del mercado, y es la razón por la que alguien retiene el token en lugar de venderlo en cuanto sube. Sin utilidad, las otras dos dimensiones no tienen base: los incentivos de crecimiento se convierten en inflación pura, y la seguridad pierde sentido porque no hay nada que proteger.

**Gobernanza**:

El token otorga poder de decisión sobre la evolución del protocolo: es la herramienta que hace posible que participantes egoístas negocien las reglas del juego sin un árbitro central. Los holders votan propuestas on-chain mediante herramientas como [Snapshot](https://snapshot.org/) (votación off-chain sin costes de gas) o [Tally](https://www.tally.xyz/) (votación on-chain vinculante). [MakerDAO](https://makerdao.com/) usa MKR para votar sobre parámetros de riesgo que determinan qué colaterales acepta el protocolo y a qué ratios. La delegación permite que holders que no quieren participar activamente cedan su voto a representantes especializados. Para una descripción más completa del token de gobernanza como tipo de activo, consulta la [taxonomía de criptoactivos](../../101/5-2-crypto-asset-taxonomy.md#clasificación-regulatoria-y-normativa).

La concesión aquí es que la gobernanza pura no genera demanda económica directa. Tener derecho a votar no es una razón suficiente para que alguien compre y retenga un token si no hay nada más en juego. Por eso muchos tokens combinan gobernanza con otros mecanismos de utilidad o captura de valor.

**Staking y seguridad**:

El token se bloquea como garantía para asegurar la red o el protocolo. Esta es la utilidad que conecta directamente con la dimensión de seguridad. En redes de Proof of Stake como [Ethereum](https://ethereum.org/), [Solana](https://solana.com/) o [Polkadot](https://polkadot.network/), los validadores hacen staking del token nativo para participar en el consenso. Si actúan de forma deshonesta, pierden tokens mediante slashing: esa es la concesión que el participante acepta a cambio de recompensas. En protocolos DeFi como [GMX](https://gmx.io/) o [Convex](https://www.convexfinance.com/) (CVX), el staking funciona como mecanismo de revenue sharing: los stakers reciben un porcentaje de las comisiones generadas por el protocolo a cambio de bloquear sus tokens. La diferencia es crucial: en el primer caso el staking asegura infraestructura (seguridad), en el segundo captura ingresos del protocolo (valor). Un staking que no tiene fuente clara de revenue ni función de seguridad real es teatro: alguien está pagando esos rendimientos y probablemente sean los propios holders a través de la dilución de nuevas emisiones.

**Gas y comisiones**:

El token funciona como medio de pago interno para acceder a los servicios del protocolo. ETH paga las comisiones de cada transacción en Ethereum, SOL en Solana. Este uso crea demanda orgánica constante: mientras haya actividad en la red, alguien necesita comprar el token para operar. Es la forma de utilidad más directa y difícil de falsificar, y conecta el valor del token directamente con el uso real del protocolo. No hay concesión aquí: más uso significa más demanda, sin dilución ni artificios.

**Colateral**:

El token se deposita como garantía para acceder a préstamos u otros servicios financieros. Los usuarios depositan ETH o WBTC en [Aave](https://aave.com/) o [Compound](https://compound.finance/) para pedir prestado contra ese colateral. [Synthetix](https://synthetix.io/) usa SNX como colateral para emitir activos sintéticos que replican el precio de activos del mundo real. Esta utilidad crea demanda de bloqueo que reduce la oferta circulante, operando simultáneamente en las tres dimensiones: genera valor (acceso a servicios), reduce velocidad de circulación (sostenibilidad) y, en algunos casos, asegura el protocolo contra insolvencia (seguridad).

**Tokens sin utilidad real**:

Si el token solo sirve para "gobernar" un protocolo que no tiene decisiones relevantes que tomar, la gobernanza es decorativa. Si el staking paga rendimientos sin que exista una fuente real de ingresos, alguien está pagando esos rendimientos y probablemente seas tú. Si la utilidad prometida es "coming soon" después de meses o años, probablemente nunca llegue. Estos tokens tienen la dimensión de valor vacía, lo que significa que los incentivos de crecimiento están sosteniendo un castillo de naipes: en cuanto los incentivos se reduzcan, no queda nada que retenga a nadie.

## El token de gobernanza: de la teoría a la implementación

El token de gobernanza es el tipo más común en DAOs y merece atención específica porque es donde se cruzan el diseño económico, la implementación técnica y la distribución de poder político.

**Qué hace un token de gobernanza**:

En su forma más básica, un token de gobernanza permite tres cosas: proponer cambios al protocolo, votar sobre propuestas de otros, y en algunos modelos, delegar tu voto a alguien de confianza. Cada token equivale por defecto a un voto, aunque existen variantes como el voto cuadrático que reduce el peso de los grandes holders. El token puede ser puramente de gobernanza (UNI de [Uniswap](https://uniswap.org/)) o híbrido, combinando gobernanza con otras utilidades como descuentos en comisiones o acceso a staking (AAVE de [Aave](https://aave.com/)).

**Implementación técnica**:

Un token de gobernanza es el instrumento que permite que el equilibrio de Nash se renegocie con el tiempo. Sin gobernanza codificada, las reglas del tokenomics son estáticas y el protocolo no puede adaptarse. Con gobernanza, el protocolo puede ajustar las concesiones entre las tres dimensiones según las condiciones reales del mercado, pero introduce un nuevo riesgo: que alguien capture el proceso de decisión y lo use para extraer valor a costa de todos los demás.

En Ethereum, un token de gobernanza se implementa como un contrato ERC-20 con la extensión [ERC20Votes](https://docs.openzeppelin.com/contracts/4.x/api/token/erc20#ERC20Votes) de [OpenZeppelin](https://www.openzeppelin.com/). Esta extensión añade tres capacidades que un ERC-20 estándar no tiene: tracking eficiente de poder de voto, soporte de delegación (un holder puede asignar su poder de voto a otra dirección sin transferir los tokens), y snapshots históricos que permiten consultar cuántos votos tenía una dirección en un bloque concreto, evitando que alguien compre tokens justo antes de una votación y los venda justo después.

El contrato del token se conecta con un contrato Governor (también de OpenZeppelin) que maneja el ciclo completo de propuestas: creación, periodo de votación, verificación de quórum, y ejecución. Entre la aprobación y la ejecución se interpone un Timelock, un contrato que introduce un retraso de seguridad (típicamente entre 24 y 48 horas) para que la comunidad pueda reaccionar si una propuesta maliciosa se aprueba mediante manipulación.

**Pasos prácticos para crear un token de gobernanza**:

El proceso empieza por decidir los parámetros antes de escribir código: supply total, distribución inicial entre stakeholders, y qué poderes concretos tendrá la gobernanza. Una vez definidos, los pasos son directos. Se despliega el contrato ERC-20 con la extensión ERC20Votes, configurando el supply total y la distribución. Se despliega el contrato Timelock con el retraso deseado. Se despliega el contrato Governor, vinculándolo al token y al timelock, configurando la duración de votaciones, el quórum requerido y el umbral mínimo de tokens para crear propuestas. Se transfiere la ownership de los contratos del protocolo al timelock, de forma que solo la gobernanza pueda modificar parámetros críticos.

Para proyectos que no necesitan gobernanza on-chain completa, una alternativa más pragmática es desplegar un ERC-20 estándar y usar [Snapshot](https://snapshot.org/) para votaciones off-chain sin coste de gas. Las decisiones aprobadas las ejecuta un [multisig de Safe](https://safe.global/) controlado por miembros de confianza. Este modelo es más sencillo, más barato, y suficiente para la mayoría de DAOs en etapa temprana. La migración a gobernanza on-chain puede hacerse después, cuando el protocolo gestione capital suficiente para justificar la complejidad.

**El problema de la participación: la concesión entre eficiencia y descentralización**:

En la práctica, la mayoría de holders de tokens de gobernanza no votan. Las tasas de participación típicas oscilan entre el 5% y el 15% del supply, lo que significa que una minoría activa toma decisiones que afectan a todos. Esto genera un riesgo directo para la dimensión de seguridad: si unos pocos holders con posiciones grandes pueden controlar la dirección del protocolo, el equilibrio de Nash se rompe porque un actor puede cambiar las reglas a su favor unilateralmente. La delegación mitiga parcialmente este problema, pero crea sus propias dinámicas de poder donde los delegados acumulan influencia desproporcionada. Los mecanismos que intentan resolver esta concesión (voto cuadrático, conviction voting, delegación líquida) se detallan en la [arquitectura de gobernanza](DAO/governance-architecture.md). La interacción específica entre el token de gobernanza y la gestión de la tesorería de la DAO, incluyendo cómo se financian las operaciones, cómo se diversifican los fondos, y cómo la gobernanza decide la asignación de capital, se desarrolla en profundidad en la [gestión de tesorería](DAO/treasury-management.md).

## Captura de valor: conectar el éxito del protocolo con el precio del token

Un protocolo puede tener millones de usuarios y generar actividad masiva, pero si su token no captura ninguna parte de ese valor, el precio no se sostendrá. Los mecanismos de captura de valor son el puente entre la dimensión de valor (utilidad real, demanda orgánica) y la dimensión de sostenibilidad (que el precio refleje algo tangible y no solo especulación). Sin captura de valor, los incentivos de crecimiento son pura dilución disfrazada de rendimiento.

**Fee switch (revenue sharing)**:

El patrón más directo: el protocolo cobra comisiones por sus servicios y distribuye una parte a los holders del token. [GMX](https://gmx.io/) reparte el 70% de las comisiones de su exchange perpetuo a los stakers de GMX y GLP. [Aave](https://aave.com/) dirige parte de los ingresos al Safety Module, donde los stakers de AAVE funcionan como seguro descentralizado del protocolo, y cuyo coste potencial (slashing en caso de insolvencia) es la concesión que aceptan a cambio de rendimiento. [Uniswap](https://uniswap.org/) tiene el fee switch técnicamente implementado pero no activado, lo que convierte a UNI en un token de gobernanza puro sin captura directa de ingresos: toda la dimensión de valor depende de la expectativa de que algún día se active, una apuesta frágil.

**Activos productivos**:

Algunos tokens generan rendimiento automáticamente por el simple hecho de poseerlos. [stETH](https://lido.fi/) de Lido representa ETH en staking y acumula recompensas de validación continuamente. [rETH](https://rocketpool.net/) de Rocket Pool se aprecia respecto a ETH a medida que se acumulan recompensas. [sDAI](https://spark.fi/) de Spark aplica automáticamente el DAI Savings Rate. Estos tokens wrapeados son un ejemplo de las tres dimensiones en armonía: generan rendimiento real (valor), aseguran la red mediante staking (seguridad), y crean demanda estructural que reduce la circulación (sostenibilidad). Además permiten que el rendimiento sea composable: puedes usar stETH como colateral en otro protocolo mientras sigues ganando recompensas de staking.

**Vote-Escrowed (ve-model): alinear tiempo con poder**:

El modelo popularizado por [Curve Finance](https://curve.fi/) lleva la alineación de incentivos un paso más allá. Los holders bloquean sus tokens CRV durante un periodo de hasta cuatro años y reciben veCRV, que otorga poder de voto sobre la distribución de emisiones, acceso a boosts en las recompensas de liquidez, y una parte de las comisiones del protocolo. Cuanto más largo el bloqueo, más poder. Este modelo es la concesión más explícita posible: el participante sacrifica liquidez personal (crecimiento) a cambio de mayor influencia y rendimiento (valor y seguridad). El resultado es una reducción drástica de la velocidad de circulación que favorece la sostenibilidad del precio. [Balancer](https://balancer.fi/) con veBAL y [Velodrome](https://velodrome.finance/) con veVELO implementan variantes del mismo patrón.

**Modelos de doble token**:

Algunos protocolos separan funciones en dos tokens para evitar que las concesiones entre dimensiones se resuelvan en un solo instrumento. [OlympusDAO](https://www.olympusdao.finance/) separa OHM (tradeable en mercado abierto) de gOHM (wrapped con rendimiento acumulado), diferenciando la función de intercambio de la de gobernanza. [GMX](https://gmx.io/) usa GMX para gobernanza y GLP como token del pool de liquidez: el primero opera en la dimensión de seguridad (decisions-making), el segundo en la de valor (exposure a comisiones). [THORChain](https://thorchain.org/) usa RUNE como token de settlement y emite activos sintéticos separados. La separación permite optimizar cada token para su función sin compromisos de diseño, aunque añade complejidad que puede confundir a usuarios menos sofisticados.

## Valoración y métricas: medir el equilibrio entre las tres dimensiones

Evaluar si un token está sobrevalorado, infravalorado, o es directamente insostenible requiere métricas que vayan más allá del precio. El precio solo refleja sentimiento; las métricas que importan revelan si las tres dimensiones están en equilibrio o si alguna está sosteniendo artificialmente a las demás.

**Market cap vs FDV: cuánta dilución falta por llegar**:

La capitalización de mercado (market cap) se calcula multiplicando el precio actual por el supply circulante: representa lo que el mercado valora hoy. La Fully Diluted Valuation (FDV) multiplica el precio por el supply total, incluyendo tokens que aún no se han desbloqueado: representa lo que el mercado valoraría si todos los tokens existieran. La diferencia entre ambas cifras es una medida directa de la concesión entre crecimiento y sostenibilidad: un ratio FDV/Market Cap superior a 3x indica que la mayoría de tokens aún no están en circulación, lo que implica dilución significativa futura que comprimirá el precio. Ratios superiores a 5x son señal de alarma seria: el protocolo está apostando masivamente al crecimiento futuro y quien compra hoy pagará esa apuesta con dilución.

**Ratio precio/comisiones (P/F): la realidad de la dimensión de valor**:

Equivalente al Price-to-Earnings (P/E) de las acciones tradicionales. Se calcula dividiendo la FDV entre las comisiones anuales del protocolo. Un protocolo con $1B de FDV que genera $50M anuales en comisiones tiene un P/F de 20x. Comparar este ratio entre protocolos similares (por ejemplo, DEXs entre sí) revela cuáles tienen la dimensión de valor sólida y cuáles cotizan por expectativas desconectadas de la realidad. Un P/F de 500x significa que el mercado está pagando 500 años de comisiones actuales: la apuesta implícita es que la actividad del protocolo crecerá órdenes de magnitud, y eso rara vez sucede. [Token Terminal](https://tokenterminal.com/) y [DefiLlama](https://defillama.com/) publican estas métricas.

**Sostenibilidad de incentivos: el test definitivo del equilibrio**:

Esta es la métrica que revela si el equilibrio de Nash es real o fabricado. Muchos protocolos pagan incentivos en tokens que superan con creces los ingresos reales que genera el protocolo. Si un proyecto emite $100M en tokens anuales como incentivos de liquidez pero solo genera $10M en comisiones reales, el ratio 10:1 significa que la dimensión de crecimiento está devorando a la de sostenibilidad: está subsidiando crecimiento con dilución, y cuando los incentivos se reduzcan, el TVL y la actividad colapsarán porque el capital mercenario irá donde mejor le paguen. El colapso de [Terra/Luna](https://www.terra.money/), donde Anchor Protocol prometía un 20% APY sin fuente real de ingresos, fue el ejemplo más devastador de un tokenomics donde la dimensión de crecimiento asfixió a las otras dos hasta que todo colapsó. [OlympusDAO](https://www.olympusdao.finance/) y su meme (3,3), basado en teoría de juegos simplificada, prometía rendimientos astronómicos mediante bonding y staking sin fuente real de ingresos: los nuevos compradores financiaban los rendimientos de los anteriores, una estructura que colapsó cuando el flujo de capital nuevo se detuvo. Cuando los incentivos de un protocolo solo funcionan si entra capital fresco continuamente, no es tokenomics: es ponzinomics.

## Distribución y lanzamiento: quién tiene poder y quién tiene incentivos

Cómo se distribuyen los tokens inicialmente es la concesión fundacional del protocolo: determina quién tiene poder, quién tiene incentivos para contribuir, y si la descentralización es real o cosmética. Una distribución que favorece a insiders maximiza la capacidad de ejecución del equipo (crecimiento) pero centraliza el poder y genera riesgo de dump coordinado (destruye seguridad y sostenibilidad). Una distribución que favorece a la comunidad maximiza la descentralización (seguridad) pero puede dejar al equipo sin recursos para construir.

**Distribución entre stakeholders**:

Una distribución típica asigna entre el 15% y el 25% al equipo fundador y advisors (con vesting largo de cuatro años), entre el 10% y el 20% a inversores tempranos (también con vesting), entre el 20% y el 30% a la tesorería comunitaria (controlada por gobernanza, cuya gestión se detalla en la [gestión de tesorería de la DAO](DAO/treasury-management.md)), y el resto a la comunidad mediante airdrops, incentivos de liquidez o venta pública. Cuando la comunidad recibe menos del 20% del supply total, la descentralización es decorativa y el equilibrio de Nash es falso: unos pocos actores pueden cambiar las reglas unilateralmente, lo que significa que no hay equilibrio real. Cuando el equipo y los VCs controlan más del 40%, las votaciones de gobernanza son un teatro donde el resultado está predeterminado.

**Modelos de lanzamiento**:

El fair launch distribuye tokens sin preventa, permitiendo que todos accedan en las mismas condiciones. [Yearn Finance](https://yearn.fi/) (YFI) y el lanzamiento inicial de [Uniswap](https://uniswap.org/) (UNI) son los ejemplos canónicos: sin preminado, sin asignación al equipo, todo distribuido mediante liquidity mining desde el primer día. Es el modelo que maximiza la dimensión de seguridad (descentralización real desde el día uno) pero sacrifica crecimiento porque dificulta financiar el desarrollo previo al lanzamiento.

Las ICOs e IDOs permiten recaudar capital vendiendo tokens antes o durante el lanzamiento. Las ICOs fueron el modelo dominante en 2017-2018: [Ethereum](https://ethereum.org/) recaudó 18 millones de dólares en su ICO de 2014, y [Polkadot](https://polkadot.network/) levantó 145 millones en 2017. Pero el modelo generó fraudes masivos y la mayoría de proyectos de esa era desaparecieron. Los IDOs en exchanges descentralizados como Uniswap eliminan el intermediario centralizado pero exponen a los compradores a front-running y sniping por bots. Las plataformas de lanzamiento centralizadas como Binance Launchpad o ByBit requieren KYC/AML completo, lo que limita el acceso pero ofrece cierta protección regulatoria; los IDOs descentralizados eliminan esas barreras pero transfieren el riesgo legal íntegramente al usuario. Son modelos que priorizan la financiación (crecimiento) aceptando riesgos de concentración y manipulación (seguridad).

Los airdrops retroactivos distribuyen tokens gratuitos a usuarios que ya interactuaron con el protocolo. [Uniswap](https://uniswap.org/) distribuyó 400 UNI a cada wallet que había usado el protocolo antes del snapshot. [Arbitrum](https://arbitrum.io/) basó su distribución en métricas de actividad on-chain. El problema creciente es el sybil farming: atacantes que crean cientos de wallets para maximizar la recepción de airdrops, diluyendo la distribución a usuarios reales y convirtiendo un mecanismo de crecimiento orgánico en una transferencia de valor a granjeros profesionales.

**Bootstrapping de liquidez: la infraestructura del mercado**:

El token necesita liquidez suficiente en exchanges descentralizados para ser tradeable sin slippage prohibitivo. Sin liquidez, no hay mercado real; sin mercado real, no hay precio de referencia; y sin precio de referencia, los incentivos no funcionan porque nadie sabe cuánto vale lo que recibe.

La forma más directa es crear pools de liquidez pareando el token con ETH o stablecoins. El equipo puede proveer liquidez inicial con fondos de tesorería, pero esto expone esos fondos a impermanent loss: una concesión entre accesibilidad del token (crecimiento) y preservación de capital (sostenibilidad). Los programas de liquidity mining incentivan a terceros a proveer liquidez ofreciendo tokens adicionales como recompensa, pero atraen capital mercenario que desaparece cuando los incentivos terminan, la trampa de crecimiento insostenible más común en DeFi.

Las bonding curves ofrecen otro mecanismo donde el precio del token aumenta automáticamente con cada unidad vendida según una función matemática predefinida. [Bancor](https://bancor.network/) popularizó este modelo, y las parachain auctions de [Polkadot](https://polkadot.network/) usan variantes del mismo principio. La ventaja es que el descubrimiento de precio es continuo y transparente, sin necesidad de market makers externos.

Los Liquidity Bootstrapping Pools (LBP) de [Balancer](https://balancer.fi/) ofrecen un mecanismo más sofisticado: la pool arranca con un peso muy desigual (típicamente 95/5 a favor del token) que se reequilibra gradualmente hacia 50/50, creando un descubrimiento de precio orgánico que dificulta el front-running. El modelo de protocol-owned liquidity, popularizado por [Olympus](https://www.olympusdao.finance/), permite al protocolo acumular sus propios LP tokens comprándolos con descuento mediante bonding, eliminando la dependencia de liquidez rentada. Es una inversión en sostenibilidad a largo plazo que sacrifica velocidad de crecimiento inmediato.

En todos estos modelos, la liquidez inicial del equipo debe bloquearse con periodos mínimos de un año para señalar compromiso. Herramientas como [Unicrypt](https://unicrypt.network/) y [Team Finance](https://www.team.finance/) permiten bloquear LP tokens en contratos verificables on-chain, ofreciendo a la comunidad la garantía de que la liquidez no será retirada de golpe.

## Aspectos legales y regulatorios: la dimensión de seguridad que no está en el código

El riesgo regulatorio opera en la dimensión de seguridad pero fuera del smart contract: ningún mecanismo on-chain protege contra una orden judicial que congele las cuentas del equipo o una clasificación regulatoria que haga ilegal la tenencia del token en jurisdicciones clave. Ignorar esta dimensión no la elimina; la convierte en una bomba de relojería.

El riesgo regulatorio más relevante es que el token sea clasificado como security (valor) por los reguladores. En Estados Unidos, el [test de Howey](https://www.sec.gov/corpfin/framework-investment-contract-analysis-digital-assets) determina si un activo es un valor basándose en si existe una inversión de dinero con expectativa de beneficio derivado del esfuerzo de terceros. Muchos tokens de gobernanza caen en zona gris porque, aunque no prometen retornos explícitos, los compradores esperan que el precio suba gracias al trabajo del equipo fundador. Esta ambigüedad es en sí misma una concesión: cuanto más clara es la utilidad real del token (dimensión de valor), menor el riesgo de clasificación como security; cuanto más depende del trabajo del equipo, mayor el riesgo.

En la Unión Europea, el [reglamento MiCA](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32023R1114) establece un marco regulatorio unificado para criptoactivos que distingue entre tokens referenciados a activos, tokens de dinero electrónico y otros criptoactivos. En España, la [CNMV](https://www.cnmv.es/) tiene obligaciones de registro específicas. Cada jurisdicción tiene sus propias reglas, y lo que es legal en una puede ser ilegal en otra: un tokenomics que funciona económicamente pero ignora la regulación es un tokenomics con un vector de ataque abierto que ningún smart contract puede mitigar.

**Documentación pre-lanzamiento**:

Antes del lanzamiento, el whitepaper y la documentación de tokenomics deben ser completos y transparentes. Un whitepaper que promete un roadmap imposible o que oculta los mecanismos reales de distribución es una señal de alarma inmediata. La documentación debe incluir la distribución exacta del supply entre stakeholders con sus calendarios de vesting, los mecanismos de captura de valor y su fuente de ingresos, las simulaciones de escenarios adversos, y el plan de evolución del tokenomics a lo largo del tiempo. Sin esta documentación, los inversores están comprando una caja negra.

**Auditorías técnicas y económicas**:

Las auditorías son la verificación externa de que las tres dimensiones funcionan como se diseñaron. Las auditorías técnicas, realizadas por firmas como [Trail of Bits](https://www.trailofbits.com/), [OpenZeppelin](https://www.openzeppelin.com/) y [Certik](https://www.certik.com/), revisan el código buscando vulnerabilidades que podrían permitir que alguien rompa las reglas codificadas. Un solo reporte de auditoría no es suficiente: múltiples auditorías independientes reducen la probabilidad de que una vulnerabilidad pase desapercibida, y sus reportes completos deben publicarse íntegramente. Las auditorías económicas, realizadas por empresas como [Gauntlet](https://www.gauntlet.xyz/) y [Chaos Labs](https://chaoslabs.xyz/), simulan escenarios adversos para validar que el equilibrio de Nash se mantiene bajo estrés: ¿qué pasa si el precio cae un 90%? ¿Y si un actor acumula el 30% del supply? ¿Los incentivos siguen alineados o colapsan? Publicar los reportes completos, incluyendo los hallazgos y las correcciones, es no negociable para la credibilidad del proyecto. Complementariamente, los programas de bug bounty en plataformas como [Immunefi](https://immunefi.com/) o [HackerOne](https://www.hackerone.com/) mantienen la seguridad viva después del lanzamiento: pagar a investigadores externos por encontrar vulnerabilidades antes de que un atacante las explote es una inversión en la dimensión de seguridad con retorno asimétrico.

## Marketing y construcción de comunidad: crecimiento con sustancia

Los incentivos económicos atraen capital, pero la comunidad sostiene el protocolo. Sin una base de usuarios que entienda lo que el token hace y por qué importa, los incentivos de crecimiento se convierten en subsidios a mercenarios que desaparecerán cuando el rendimiento baje. El marketing de un protocolo Web3 no es publicidad: es educación, transparencia y alineación.

**Marketing basado en educación**:

El contenido técnico que explica el "por qué" del protocolo crea usuarios informados que toman decisiones racionales, en contraste con el hype que crea especuladores que entran y salen según el sentimiento del mercado. La documentación técnica completa, las sesiones AMA (Ask Me Anything) con el equipo, los vídeos explicativos y los embajadores técnicos que hablan desde el conocimiento y no desde la promesa son las herramientas que construyen demanda orgánica real. El hype genera un spike de atención seguido de un crash de decepción; la educación genera adopción gradual pero resistente.

**Incentivos para early adopters**:

Los primeros usuarios asumen el mayor riesgo y merecen una compensación proporcional. Las recompensas por participar en testnets, los NFTs conmemorativos que marcan contribuciones verificables, y los sistemas de puntos que se convierten en tokens en el TGE son mecanismos que premian la participación real. La clave es distinguir entre contribución genuina y farming mercenario: criterios cualitativos (calidad de feedback, reportes de bugs, participación en gobernanza) filtran mejor que los puramente cuantitativos (número de transacciones, volumen). Sin esos filtros, los programas de incentivos atraen bots y granjeros profesionales en lugar de usuarios reales.

**Transparencia operativa**:

La comunidad necesita ver que el protocolo funciona como se prometió. Los dashboards públicos en [Dune Analytics](https://dune.com/) que muestran métricas en tiempo real, la transparencia de los fondos de tesorería mediante [Safe](https://safe.global/) (antes Gnosis Safe) donde cualquiera puede verificar los movimientos de capital, y la comunicación constante en Discord y foros de gobernanza donde el equipo responde preguntas y comparte decisiones son la infraestructura de confianza que sostiene la comunidad. Un protocolo opaco que solo comunica buenas noticias y oculta los problemas está construyendo sobre arena.

## Post-lanzamiento: mercado secundario y monitorización

El lanzamiento no es el final del diseño tokenómico, es el inicio de su prueba real. Las decisiones sobre cómo se gestiona el mercado secundario, cómo se monitoriza la salud del ecosistema, y cómo se ajustan los parámetros según los datos reales determinan si el tokenomics sobrevive al contacto con la realidad o colapsa en los primeros meses. La [gestión de la salud de la DAO](DAO/dao-health-practices.md) proporciona un marco diagnóstico completo para detectar señales de deterioro temprano.

**Gestión del mercado secundario**:

El market making profesional, realizado por firmas especializadas como Wintermute, GSR o Jump Trading, proporciona liquidez continua y spreads ajustados que reducen la volatilidad artificial. La diferencia entre market making legítimo y manipulación de mercado es la intención: el primero mantiene un libro de órdenes saludable; el segundo infla volúmenes artificialmente mediante wash trading para crear una falsa impresión de actividad. Los listings en exchanges centralizados (CEX) como Binance o Coinbase son un multiplicador de accesibilidad, pero el timing importa: listar demasiado pronto, antes de que exista volumen real en DEXs, expone el token a manipulación en un mercado con poca profundidad. Los costes de listing oscilan entre 50.000 y más de 500.000 dólares, y los exchanges de primer nivel exigen tracción demostrable antes de aceptar un token.

Los token buybacks, donde el protocolo compra sus propios tokens del mercado abierto con ingresos operativos, son un mecanismo de captura de valor legítimo cuando se financian con revenue real. Cuando se financian con la tesorería sin una fuente de ingresos que la reponga, son solo una transferencia de riqueza de la tesorería a los vendedores actuales que erosiona la sostenibilidad. La [gestión de tesorería](DAO/treasury-management.md) de la DAO detalla cómo implementar estos mecanismos de forma sostenible.

**Monitorización on-chain**:

Los datos on-chain revelan si las tres dimensiones están en equilibrio real o si los números de vanidad ocultan problemas estructurales. La distribución de holders muestra si el token está concentrado en pocas wallets (riesgo de dump coordinado) o distribuido saludablemente. El número de usuarios activos distingue entre crecimiento real y actividad inflada por bots. La token velocity, la frecuencia con la que el token cambia de manos, indica si se usa para su función real o si solo se holdea esperando apreciación sin utilidad subyacente.

**Descentralización progresiva**:

La mayoría de protocolos arrancan con el equipo fundador manteniendo control significativo sobre parámetros críticos, las llamadas training wheels. Esta centralización inicial es pragmática: permite reaccionar rápido a problemas imprevistos durante la fase más frágil del protocolo. Pero si las training wheels no se retiran gradualmente, la descentralización es decorativa. La transición hacia gobernanza comunitaria plena debe seguir un calendario público con hitos verificables: primero se delegan los parámetros menos críticos, después los más sensibles, hasta que el equipo fundador se convierte en un participante más sin poderes especiales. La [arquitectura de gobernanza](DAO/governance-architecture.md) detalla los mecanismos específicos para esta transición, y el [marco operativo de la DAO](DAO/operations-framework.md) describe cómo estructurar los equipos de trabajo durante cada fase.

**Optimización de incentivos**:

Los incentivos de crecimiento que funcionaron en la fase de lanzamiento deben reducirse gradualmente a medida que la demanda orgánica los reemplaza. Mantener emisiones altas indefinidamente diluye a los holders leales y subsidia a mercenarios. La transición natural es migrar de liquidity mining (pagar liquidez con emisiones de tokens) a protocol revenue (distribuir ingresos reales), un indicador directo de que la dimensión de valor ha madurado lo suficiente para sostenerse sin muletas. Los protocolos que dependen permanentemente de emisiones para retener capital no han encontrado product-market fit tokenómico.

## Evolución y consenso: el tokenomics como sistema vivo

Ningún tokenomics sobrevive intacto al contacto con el mercado real. Los parámetros que parecían razonables en una hoja de cálculo se revelan inadecuados cuando miles de participantes interactúan con ellos de formas que nadie previó. El quórum puede ser inalcanzable, la inflación puede ser excesiva, los incentivos pueden atraer exactamente el tipo de comportamiento que se quería evitar. La pregunta no es si habrá que cambiar el tokenomics, sino si el sistema está preparado para cambiar sin romperse.

**Mecanismos de evolución**:

La forma más básica de evolución es la parametrización: diseñar el tokenomics con variables ajustables en lugar de constantes fijas. En lugar de codificar "el quórum es el 10% del supply" como valor inmutable, el contrato expone ese parámetro a la gobernanza para que la comunidad pueda ajustarlo mediante votación. Los parámetros que típicamente deben ser ajustables incluyen tasas de emisión, porcentajes de quema, ratios de distribución de comisiones, umbrales de quórum, y duración de los periodos de vesting para nuevas asignaciones.

El siguiente nivel es la modularidad: diseñar la arquitectura de contratos para que los módulos puedan añadirse, reemplazarse o desactivarse sin redesplegar todo el sistema. Los [proxies upgradeable de OpenZeppelin](https://docs.openzeppelin.com/contracts/4.x/api/proxy) permiten actualizar la lógica de un contrato manteniendo su estado y dirección, aunque introducen riesgos de centralización si el poder de upgrade no está controlado por la gobernanza. Una alternativa más descentralizada es el patrón de módulos, donde cada funcionalidad (staking, distribución de fees, quema) vive en un contrato separado que el contrato principal puede intercambiar.

El tercer nivel es la evolución programada: diseñar fases explícitas con transiciones predefinidas. Muchos protocolos arrancan con emisiones altas y las reducen automáticamente según un calendario (como el halving de Bitcoin) o según métricas on-chain (como la quema dinámica de Ethereum). Codificar estas transiciones desde el inicio permite que el tokenomics evolucione sin necesidad de votación para cada ajuste, manteniendo previsibilidad mientras se adapta a la maduración del ecosistema.

Finalmente, las válvulas de emergencia son mecanismos que permiten respuestas rápidas ante situaciones imprevistas. Un circuit breaker que pausa emisiones si el precio cae un 80% en 24 horas, un cap dinámico que limita la velocidad de desbloqueo de tokens si la liquidez del mercado cae por debajo de un umbral, o un mecanismo de ragequit que permite a los holders salir con su parte proporcional de la tesorería si una propuesta aprobada cambia las reglas fundamentales del juego. Estos mecanismos no se activan nunca en condiciones normales, pero su existencia previene catástrofes.

**El consenso como requisito**:

Un tokenomics impuesto es un tokenomics muerto. Si los fundadores diseñan las reglas económicas en una sala cerrada y las presentan como un hecho consumado, la comunidad las percibirá como arbitrarias y no las defenderá cuando vengan las crisis. Y las crisis siempre vienen.

El proceso de diseño debe incluir a la comunidad desde las fases más tempranas. Publicar varias opciones de diseño para parámetros críticos (distribución del supply, tasa de emisión, mecanismos de captura de valor) y someter cada una a debate público antes de codificar nada. Las votaciones preliminares en [Snapshot](https://snapshot.org/) permiten testear preferencias sin coste de gas. Los foros de gobernanza como [Commonwealth](https://commonwealth.im/) o simplemente Discord permiten deliberación pública donde los argumentos se registran y cualquiera puede participar.

Esto no significa que la comunidad diseñe el tokenomics por comité, lo cual produciría un compromiso mediocre sin visión. Los fundadores proponen, la comunidad valida, cuestiona y ajusta. El resultado tiene legitimidad porque la gente siente que participó en su creación, no porque le guste cada detalle. Un tokenomics con el que nadie está completamente satisfecho pero todos sienten que es justo es infinitamente más resiliente que uno perfecto en teoría pero impuesto sin consulta.

La transparencia total sobre las motivaciones detrás de cada decisión de diseño es no negociable. Si el equipo se asigna un 20% del supply, debe explicar públicamente por qué ese porcentaje y no otro, qué compromisos de vesting asume, y qué ocurre con esos tokens si algún miembro del equipo abandona el proyecto. Si se eligen incentivos agresivos para la fase inicial, debe explicarse cuánto durará esa fase, qué los reemplazará después, y qué ocurre si los objetivos de crecimiento no se alcanzan. La información asimétrica entre fundadores y comunidad corroe la confianza, y un tokenomics sin confianza es solo código.

## Señales de alarma: cómo detectar un equilibrio falso

Detectar proyectos con tokenomics destructivo es tan importante como diseñar tokenomics saludable. Todo lo expuesto en las secciones anteriores se puede resumir en una pregunta: ¿las tres dimensiones están en equilibrio real, o alguna está inflada artificialmente mientras las otras están vacías?

Un ratio FDV/Market Cap superior a 5x indica que la dimensión de crecimiento está hipotecando la sostenibilidad: hay tanta dilución pendiente que el precio actual no refleja el coste real de participar. Tokens del equipo sin vesting significan que la alineación temporal es inexistente: quienes diseñaron las reglas pueden abandonar el juego en cualquier momento sin consecuencias, rompiendo el equilibrio de Nash desde la raíz. Equipos completamente anónimos eliminan la accountability social que complementa la accountability codificada. Código copiado sin auditoría hereda vulnerabilidades conocidas, dejando la dimensión de seguridad abierta de par en par. Promesas de rendimientos garantizados o tácticas de urgencia ("última oportunidad", "solo hoy") son señales inequívocas de que no hay equilibrio: hay un mecanismo de extracción disfrazado de protocolo.

En el diseño, los errores más destructivos son los incentivos que premian comportamiento dañino (pagar por volumen genera wash trading, lo que infla la dimensión de crecimiento con datos falsos), las espirales de muerte donde la presión vendedora perpetua se refuerza con inflación alta y utilidad nula (las tres dimensiones colapsando simultáneamente), la gobernanza centralizada donde unas pocas ballenas controlan todas las votaciones (dimensión de seguridad comprometida), la ausencia de mecanismos de captura de valor que desconecta el éxito del protocolo del precio del token (dimensión de valor vacía mientras se simula crecimiento), y el lanzamiento de token antes de tener producto funcional, un síntoma inequívoco de que no existe product-market fit y el token solo sirve como vehículo especulativo. Para un análisis completo de fracasos económicos reales y las lecciones que dejaron, consulta los [fallos económicos y lecciones aprendidas](economic-failures-and-lessons.md).

## Recursos y herramientas

Diseñar un tokenomics requiere datos reales, simulación de escenarios, y verificación legal. Cada fase del proceso tiene herramientas especializadas, y la elección depende del presupuesto, la complejidad del protocolo y la experiencia técnica del equipo.

**Análisis y seguimiento on-chain**:

Para validar que las tres dimensiones están en equilibrio una vez el protocolo está en producción, se necesitan datos reales. [DefiLlama](https://defillama.com/) ofrece datos de TVL, comisiones y revenue de todos los protocolos, y es el punto de partida para evaluar la dimensión de valor de cualquier proyecto. [Token Terminal](https://tokenterminal.com/) publica métricas financieras como ratios P/F y P/S que permiten comparar protocolos como se comparan empresas. [Messari](https://messari.io/) produce research reports profesionales con análisis cualitativos que complementan los datos cuantitativos. [Dune Analytics](https://dune.com/) permite crear dashboards custom con datos on-chain para métricas específicas que las plataformas genéricas no cubren. [TokenomicsDAO](https://tokenomicsdao.com/) publica frameworks de diseño y análisis comparativos de modelos tokenómicos. [Nansen](https://www.nansen.ai/) rastrea movimientos de smart money y distribución de holders, lo que permite detectar concentración peligrosa o patrones de venta coordinada que amenazan la sostenibilidad. Para datos de mercado básicos como precio, volumen y market cap, [CoinGecko](https://www.coingecko.com/) y [CoinMarketCap](https://coinmarketcap.com/) son las referencias universales.

**Simulación y modelado antes del lanzamiento**:

Antes de codificar nada, las concesiones entre las tres dimensiones deben simularse para verificar que el equilibrio se mantiene bajo escenarios adversos. [Cenit Finance](https://www.cenit.finance/tokenomics-simulator-template) proporciona un simulador interactivo basado en hojas de cálculo para modelar supply schedules, vesting, emisiones y quemas bajo diferentes escenarios, con versión básica gratuita y versión completa de pago. [Outlier Ventures Token Designer](https://github.com/OutlierVentures/TokenDesigner) es un framework open-source en Python para simulaciones Monte Carlo de economías token, más técnico pero completamente gratuito. [TokenSPICE](https://github.com/tokenspice/tokenspice), desarrollado originalmente por Ocean Protocol, permite modelar comportamientos complejos de múltiples agentes mediante agent-based modeling, ideal para simular cómo actores con estrategias egoístas interactúan con las reglas del tokenomics. [Machinations](https://machinations.io/) ofrece una plataforma visual de diagramas de flujo para modelar circulación de tokens y pools de incentivos, con versión gratuita limitada y planes de pago. [CadCAD](https://cadcad.org/) es el framework open-source de simulación de sistemas complejos usado por proyectos DeFi serios (MakerDAO, BlockScience) para modelar políticas, parámetros y comportamientos emergentes. Es extremadamente potente pero requiere expertise en ciencia de datos y Python; esencial para protocolos complejos con riesgos sistémicos, overkill para proyectos pequeños.

Para equipos sin presupuesto ni perfil técnico, Cenit Finance o Machinations en sus versiones gratuitas son el punto de entrada más accesible. Para equipos técnicos sin presupuesto, TokenSPICE o Outlier Ventures Token Designer son completamente gratuitos y open-source. Con presupuesto pero sin perfil técnico, Cenit Finance versión completa o Machinations Pro cubren la mayoría de necesidades. Para protocolos DeFi complejos donde un error de diseño puede causar pérdidas millonarias, CadCAD combinado con consultoría especializada de [Gauntlet](https://www.gauntlet.xyz/) o [BlockScience](https://block.science/) es el estándar de la industria.

**Formación en token engineering**:

Para profundizar en la disciplina de diseño de sistemas económicos descentralizados, [TokenEngineering Academy](https://www.tokenengineering.net/) ofrece cursos estructurados y organiza el Token Engineering Research Symposium (TERSE) en colaboración con EthCC.

**Compliance y regulación**:

Para la dimensión legal, la [CNMV](https://www.cnmv.es/) gestiona la regulación española incluyendo el sandbox regulatorio. El [reglamento MiCA](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32023R1114) define el marco europeo vigente. El [test de Howey](https://www.sec.gov/corpfin/framework-investment-contract-analysis-digital-assets) sigue siendo el framework de referencia en Estados Unidos para determinar si un token es un security. El [Token Taxonomy Framework](https://tokentaxonomyframework.org/) proporciona estándares internacionales para clasificación de tokens.

El diseño del tokenomics no existe en aislamiento: es el sistema económico que sostiene toda la estructura organizativa y técnica de un protocolo descentralizado. La [guía práctica de creación de una DAO](DAO/creation-practical-guide.md) describe cómo integrar el tokenomics en el proceso completo de lanzamiento, y la [gestión de recursos](DAO/resource-management.md) detalla cómo los diferentes tipos de recursos (financieros, humanos, técnicos) interactúan con el diseño económico del token a lo largo de la vida del protocolo.

---
