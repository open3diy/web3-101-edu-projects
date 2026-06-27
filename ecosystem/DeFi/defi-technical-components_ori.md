# La infraestructura DeFi: cómo situar cada pieza sin confundirlas

Existe una forma de leer DeFi que produce confusión permanente: tratar cada nombre propio como si fuera una cosa del mismo tipo. En esa lectura, LayerZero, Uniswap, Aave, Across, LI.FI y un pool de liquidez son "protocolos DeFi", como si fueran objetos comparables. No lo son. Pertenecen a niveles distintos del sistema y cumplen funciones distintas. Mezclarlos es como meter en la misma categoría "el motor", "el combustible", "el coche" y "el GPS": todos participan en un viaje, pero son cosas de naturaleza completamente diferente.

Este documento propone un marco para leer cualquier pieza de la infraestructura DeFi y saber inmediatamente qué tipo de cosa es, en qué nivel del sistema vive y de qué otras piezas depende. No es un catálogo del ecosistema ni una foto del mercado actual. Es un andamiaje cognitivo.

El marco descansa en una distinción que conviene fijar desde el principio: hay **mercados**, hay **componentes que hacen posibles los mercados**, hay **protocolos que transportan valor o mensajes entre cadenas**, y hay **capas de abstracción** que coordinan todo lo anterior para que el usuario no tenga que hacerlo manualmente. Estas cuatro clases no son intercambiables.

## Los mercados: donde ocurre realmente la actividad económica

Un mercado es el sistema donde se produce el intercambio, el préstamo, la liquidación o la formación de precio. Los AMMs, los lending markets, los mercados de derivados y los sistemas basados en intents son todos mercados, aunque resuelven problemas económicos distintos con mecanismos distintos. La [anatomía detallada de cada tipo de mercado](defi-markets-anatomy.md) está desarrollada en otro documento. Lo que importa aquí es la distinción de nivel: un mercado no es lo mismo que los componentes que lo hacen posible, ni que los protocolos que conectan cadenas, ni que las capas de abstracción que deciden cómo ejecutar una operación.

## Los componentes: las piezas que hacen posible que los mercados funcionen

Ningún mercado DeFi opera en el vacío. Por debajo de cualquier AMM, lending market o mercado de derivados hay piezas de infraestructura que no son el mercado pero sin las cuales el mercado no puede existir. Estas piezas no forman precios ni cruzan oferta con demanda: proveen liquidez, traen información externa, gestionan capital o representan posiciones.

### Pools de liquidez

Un pool de liquidez es un contrato inteligente que contiene una reserva de activos depositada por proveedores de liquidez. No es un mercado. Es el contenedor de capital sobre el que un mercado opera. La diferencia importa: el AMM es el mecanismo que usa ese capital para ejecutar swaps; el pool es donde está ese capital guardado.

Los proveedores de liquidez depositan activos y reciben a cambio un LP token que representa su participación proporcional en el pool. Ese LP token es componible: se puede usar como colateral en un lending market, depositarse en una vault que gestiona la posición, o transferirse a otro usuario que quiera asumir esa posición. Esta componibilidad —la capacidad de convertir cualquier posición en un activo reutilizable— es uno de los rasgos más característicos de DeFi.

El riesgo específico del proveedor de liquidez en un AMM se llama pérdida impermanente. Cuando el precio relativo de los dos activos del pool cambia, los arbitrajistas reequilibran el pool hasta que refleja el precio de mercado. Ese reequilibrado deja al proveedor con una mezcla distinta a la que depositó: más del activo que cayó de precio, menos del que subió. Si retira en ese momento, el valor total puede ser inferior al que habría obtenido simplemente guardando los activos. Las comisiones de trading son la compensación por asumir ese riesgo; si son suficientes, la posición es rentable. Si no lo son, el proveedor habría ganado más sin hacer nada.

### Oráculos de precios

Un contrato inteligente, por diseño, solo puede leer el estado de su propia cadena. No puede consultar el precio de ETH en Binance ni el tipo de cambio EUR/USD. Pero muchos protocolos necesitan esa información para funcionar: un lending market que no sepa el precio del colateral no puede calcular si una posición debe liquidarse; un mercado de perpetuos que no conozca el precio spot no puede calcular el funding rate ni cerrar posiciones.

Los oráculos son el canal por el que esa información externa entra a los contratos. Y aquí conviene distinguir dos modelos que funcionan de manera radicalmente distinta.

Los **oráculos de red externa** —Chainlink, Pyth, Redstone— son sistemas que agregan datos de fuentes off-chain y los publican on-chain. Chainlink opera con una red de nodos independientes que consultan múltiples exchanges, calculan una mediana y actualizan el precio on-chain cuando se supera un umbral de desviación. La descentralización de la red es su garantía de resistencia a la manipulación. Pyth opera de manera diferente: trabaja con publishers que son market makers e instituciones financieras reales, y publica precios de alta frecuencia directamente desde esas fuentes. Eso lo hace más rápido y más preciso para mercados de derivados donde la latencia importa, pero depende de que esos publishers actúen honestamente.

Los **TWAP oracles** —time-weighted average price— no traen ningún precio de fuera. Toman el precio histórico de una pool on-chain y calculan su media durante una ventana temporal. Un TWAP de treinta minutos pregunta "cuál fue el precio medio de este par en los últimos 1.800 bloques". La ventaja es resistencia a manipulación puntual: para falsear un TWAP, no basta con mover el precio en un bloque; hay que mantenerlo desviado durante toda la ventana, lo que es caro. La desventaja es el retraso: en mercados rápidos, el TWAP puede reflejar un precio que ya no existe.

### Vaults, estrategias y curadores

Si los pools son contenedores de liquidez y los oráculos son canales de información, las vaults son productos de gestión de capital. Un usuario deposita en una vault y la vault aplica una estrategia sobre mercados subyacentes para generar rendimiento. La vault no crea un mercado nuevo; empaqueta acceso a mercados existentes.

La separación en tres capas ayuda a entender qué está pasando realmente. La **vault** es el contenedor: acepta depósitos, emite un token de participación —normalmente conforme al estándar ERC-4626— y gestiona la contabilidad de cuánto corresponde a cada depositante. La **estrategia** es la lógica que mueve el capital: prestar en Aave, aportar liquidez en Uniswap, reinvertir las recompensas, rebalancear entre protocolos cuando el rendimiento cambia. El **curador** —cuando existe— es la capa que decide qué estrategias puede usar la vault, qué mercados están permitidos y qué límites de riesgo aplican. Morpho tiene curadores externos que definen los parámetros de las vaults que se construyen sobre su protocolo; Yearn tiene strategists que proponen estrategias que el protocolo aprueba o rechaza.

Para el usuario, la experiencia es simple: depositar y recibir rendimiento. Por debajo, hay decisiones de riesgo reales. Una vault de USDC puede estar prestando en cinco lending markets diferentes con parámetros distintos; si uno de esos mercados es explotado, el impacto llega al depositante aunque nunca haya interactuado directamente con ese protocolo.

## La interoperabilidad: mover mensajes y mover valor entre cadenas

El ecosistema blockchain está fragmentado en decenas de redes que no pueden comunicarse de forma nativa. Ethereum no conoce el estado de Solana; un contrato en Arbitrum no puede leer directamente lo que ocurre en Base. Esta fragmentación crea dos problemas distintos que requieren dos tipos de solución distintos: el problema de **comunicar** entre cadenas y el problema de **mover valor** entre cadenas. Confundir estas dos cosas —y es la confusión más frecuente en este dominio— lleva a no entender ninguna de ellas.

### Mensajería cross-chain: mover información

Un protocolo de mensajería cross-chain permite que un contrato en una cadena envíe un mensaje a un contrato en otra cadena. Solo eso. El mensaje puede ser cualquier cosa: una instrucción, una prueba de que algo ocurrió, una llamada a función remota, información de estado. Lo que el protocolo de mensajería garantiza es que el mensaje llega íntegro y que proviene de quien dice provenir.

LayerZero, Hyperlane, Axelar y Wormhole son protocolos de mensajería. Pero no funcionan igual, y esa diferencia de diseño es lo que define su perfil de riesgo real.

**LayerZero** descompone el proceso de verificación en dos piezas independientes: un DVN —decentralized verifier network— que atestigua que un mensaje en la cadena origen es válido, y un ejecutor que lo entrega en destino. La aplicación que usa LayerZero puede elegir qué DVNs quiere que validen sus mensajes y puede requerir consenso entre varios. Esto hace la seguridad configurable pero también la hace dependiente de las decisiones que cada aplicación toma al desplegarse. Un protocolo que usa solo un DVN poco robusto hereda esa debilidad.

**Hyperlane** lleva la personalización más lejos: cualquier cadena puede desplegar Hyperlane sin permiso, y los ISMs —interchain security modules— permiten definir exactamente qué modelo de verificación aplica. El espacio de diseño es amplio, pero eso también significa que la calidad de seguridad varía según cómo esté configurada cada instancia.

**Wormhole** opera con un conjunto de 19 guardianes —validadores conocidos, incluyendo instituciones como Jump Crypto, Everstake y otros— que observan eventos en las cadenas conectadas y firman attestations multisig. Su modelo de seguridad es más centralizado que el de IBC o que un light client, pero con 19 entidades independientes el umbral de colusión es alto en la práctica. El exploit de Wormhole en 2022 —320 millones de dólares— no fue un fallo de los guardianes sino una vulnerabilidad en el contrato de verificación de firmas de Solana que permitía falsificar attestations.

Lo que todos estos protocolos tienen en común es lo que no hacen por sí solos: no mueven activos. LayerZero entrega un mensaje; no mueve USDC. Wormhole atestigua que algo ocurrió en una cadena; no transfiere ETH. Pero ese mensaje es lo que autoriza que el activo se mueva en el otro lado: en un bridge lock-and-mint, el mint en destino ocurre precisamente porque llegó un mensaje verificado que confirma que el lock en origen es real. Sin ese mensaje, no hay mint. La mensajería no ejecuta la transferencia, pero es la condición que la desencadena.

### Bridges: mover valor

Un bridge mueve activos o representaciones de valor entre cadenas. El puente siempre incluye algún mecanismo de mensajería o verificación por debajo —necesita confirmar que el depósito en la cadena origen es real antes de liberar fondos en destino— pero el bridge no se reduce a esa mensajería. Lo que lo define es la lógica de activos: qué se bloquea, qué se acuña, qué se quema, quién adelanta fondos y cómo se produce el settlement (es decir consolidación en el registro principal de liquidaciones).

Hay cuatro patrones fundamentales, y entenderlos es entender el 90% del espacio de diseño de bridges.

**Lock-and-mint** es el patrón más antiguo y más explotado históricamente. El usuario deposita un activo en la cadena origen; el bridge lo bloquea en un contrato custodio; y en la cadena destino se acuña un token representativo —wETH, USDC.e, cualquier "wrapped" token. Para volver, el usuario quema el token representativo en destino y el bridge desbloquea el original en origen. El problema estructural es que el contrato custodio en origen acumula activos reales mientras los tokens representativos circulan libremente. Si el contrato es explotado o los validadores que autorizan los mints son comprometidos, todos esos activos pueden robarse de una sola vez. El bridge de Ronin —625 millones de dólares— y Nomad —190 millones— siguieron este patrón.

**Burn-and-mint nativo** resuelve el problema del custodio trasladando el control al emisor del activo. Circle, el emisor de USDC, lanzó CCTP —Cross-Chain Transfer Protocol— con este modelo: el usuario quema USDC en la cadena origen y Circle emite USDC nativo de nuevo en la cadena destino. No hay un custodio intermedio que hackear; el riesgo se concentra en Circle como entidad centralizada, que ya era el riesgo que asumías al tener USDC. El resultado es que el USDC en Base, en Arbitrum y en Ethereum es el mismo token nativo, no tres envoltorios distintos con distintos perfiles de riesgo. CCTP no es un protocolo de mensajería genérico; es una primitiva específica para USDC que otros protocolos pueden usar internamente.

**Los bridges basados en pools de liquidez** evitan el custodio central manteniendo reservas del activo en varias cadenas. Cuando alguien quiere mover USDC de Ethereum a Optimism, el bridge toma USDC de su pool en Optimism y lo entrega; luego reequilibra las pools cuando el flujo neto lo justifica. Hop Protocol usa este modelo. El riesgo deja de ser un custodio centralizado y pasa a ser la disponibilidad de liquidez en cada cadena: si hay mucho flujo en una dirección y el pool en destino se vacía, el cruce no puede ejecutarse o se encarece. Stargate, construido sobre LayerZero, combina este modelo de pools con mensajería cross-chain para la coordinación.

**Los intent bridges** son el modelo más reciente y conceptualmente más distinto. El usuario no especifica el mecanismo del cruce; especifica el resultado: "quiero 1.000 USDC en Base". Un filler —actor que mantiene capital propio en varias cadenas— detecta esa intención, adelanta los fondos en destino de inmediato, y después el protocolo le reembolsa el capital que depositó el usuario en origen, con una comisión. El usuario recibe los fondos en segundos; el filler asume el riesgo del settlement.

Across Protocol es el ejemplo más maduro de este modelo. Su pieza diferenciadora es el mecanismo de liquidación: usa el UMA optimistic oracle para validar que las condiciones del cruce se cumplieron correctamente antes de reembolsar al filler. El modelo optimistic asume que las liquidaciones son válidas por defecto y abre una ventana de disputa; si nadie la disputa en el plazo establecido, el filler cobra. Este diseño permite liquidaciones rápidas sin verificación costosa en el caso normal, asumiendo que los actores económicamente motivados disputarán cualquier fraude.

Hay un quinto patrón que merece mención porque no encaja bien en ninguna de las categorías anteriores:

**Los atomic swaps** son el único modelo de cruce verdaderamente sin intermediario. Dos partes intercambian activos nativos en dos cadenas distintas mediante contratos HTLC —hashed timelock contracts. Una de las partes elige un secreto y publica su hash; ambas bloquean sus fondos bajo la condición de que se liberen a quien revele ese secreto. Cuando una parte revela el secreto para cobrar su lado, la otra puede leerlo y cobrar el suyo. El secreto es el hilo que une las dos patas del intercambio: no se puede tirar de una sin que la otra se mueva.

El resultado es un intercambio donde nadie custodia nada, no se acuña ningún token representativo y no hay ningún contrato central que hackear. Es el modelo más limpio en términos de riesgo de contraparte. Su limitación es práctica: necesita una contraparte que quiera exactamente el intercambio inverso, en el momento adecuado, con un volumen compatible. En mercados poco activos o para pares poco frecuentes, encontrar esa contraparte es difícil. Bisq lo usa para bitcoin; las submarine swaps de Lightning aplican la misma idea entre la cadena de Bitcoin y sus canales de pago —que no es exactamente un cruce entre dos blockchains soberanas sino entre la cadena base y su capa de pago.

### ThorChain: un mercado cross-chain, no un bridge

ThorChain ocupa una categoría propia que los documentos de referencia clasifican correctamente pero que conviene explicar bien. ThorChain no es un bridge clásico —no bloquea activos y acuña wrappers— ni un protocolo de mensajería. Es un **DEX cross-chain nativo**: permite intercambiar BTC nativo por ETH nativo, o cualquier activo nativo de una cadena por cualquier otro, sin que ninguno de los dos activos se convierta en un token representativo.

Cómo lo consigue es la parte importante. ThorChain opera su propia red de validadores —los "thorchain nodes"— que custodian activos nativos en las cadenas que soporta mediante wallets multisig. Cuando alguien deposita BTC en ThorChain para hacer un swap, los nodos reciben ese BTC en una dirección controlada colectivamente por el conjunto de nodos. El BTC no se bloquea en un smart contract de Ethereum; está en una wallet de Bitcoin controlada por los nodos. Esto elimina el wrapped token pero introduce un modelo de custodia distribuida que depende de la honestidad y seguridad de ese conjunto de nodos. La garantía económica es el RUNE que los nodos tienen en stake: si actúan de forma fraudulenta o si un exploit drena los activos bajo su custodia, pierden ese stake. La seguridad del sistema está directamente acoplada al valor de mercado de RUNE.

### Atomic swaps: intercambio P2P entre cadenas, sin intermediario

Los [atomic swaps](https://academy.binance.com/es/articles/atomic-swaps-explained) tampoco son un bridge. Son un mecanismo de intercambio directo entre dos partes: cada una bloquea su activo en su propia cadena mediante un contrato HTLC —hashed timelock contract— y el desbloqueo de ambos lados está atado a un mismo secreto criptográfico. Quien revela el secreto para cobrar su parte automáticamente permite que la otra parte lo use para cobrar la suya. Si el tiempo expira sin que nadie revele el secreto, ambas partes recuperan sus fondos. No hay custodio, no hay wrapped token, no hay contrato central que pueda ser explotado.

El límite de este modelo es práctico: necesita una contraparte que quiera exactamente el intercambio inverso, con el volumen y el momento adecuados. [Bisq](https://bisq.network/) lo usa para intercambios de bitcoin, y las submarine swaps de [Lightning](https://lightning.network/) aplican la misma idea entre la cadena base de Bitcoin y sus canales de pago. Para pares poco frecuentes o volúmenes grandes, encontrar esa contraparte es difícil, y por eso el modelo no escala como infraestructura general.

---

## Frameworks de interoperabilidad nativa: cuando la cadena y la comunicación se diseñan juntas

Todo lo anterior asume un punto de partida: cadenas independientes que existen y necesitan comunicarse mediante infraestructura añadida encima. Hay una alternativa que parte de un supuesto distinto: ecosistemas donde la interoperabilidad forma parte del diseño desde el principio.

### IBC: interoperabilidad entre cadenas soberanas en el ecosistema Cosmos

El Inter-Blockchain Communication protocol no es un bridge de terceros. Es un estándar de comunicación que cualquier blockchain puede implementar para conectarse con otras cadenas que también lo implementen. La diferencia conceptual es importante: un bridge clásico es infraestructura externa que conecta dos cadenas que no fueron diseñadas para ello; IBC es un protocolo que las cadenas adoptan como parte de su diseño.

El mecanismo de IBC descansa en light clients. Cuando la cadena A establece un canal con la cadena B, mantiene un light client de B que le permite verificar pruebas del estado de B sin depender de un tercero. Un relayer —que puede ser cualquier nodo, sin permiso— transmite los paquetes y las pruebas entre cadenas; las cadenas los verifican por sí mismas usando su propio light client de la contraparte. No hay un conjunto de validadores especiales que autoricen el cruce; la verificación es criptográfica y descentralizada.

IBC no es solo transferencia de tokens —eso es ICS-20, uno de los estándares que corre sobre IBC. El protocolo en sí es un mecanismo de paso de mensajes verificados entre cadenas, sobre el que se puede construir cualquier tipo de coordinación interchain: transferir tokens, llamar funciones remotas, sincronizar estado. En este sentido, IBC es a la vez messaging y el transporte sobre el que corre el asset transfer en el ecosistema Cosmos, sin que ambas cosas sean lo mismo.

dYdX v4 migró a su propia cadena Cosmos en 2023 para controlar su secuenciación. Osmosis es el DEX principal del ecosistema y opera sobre IBC para conectar docenas de cadenas. La solidez de IBC como protocolo es alta; la limitación del ecosistema Cosmos es la liquidez fragmentada entre muchas cadenas con poca actividad cada una.

### XCM y Polkadot: seguridad compartida con mensajería nativa

Polkadot propone un modelo diferente a Cosmos: en lugar de cadenas soberanas que se comunican de igual a igual, una relay chain central proporciona seguridad compartida a las parachains que se conectan. Una parachain no necesita construir su propio conjunto de validadores; delega esa seguridad en los validadores de la relay chain. A cambio, todas las parachains dentro del ecosistema Polkadot comparten la misma base de seguridad.

La comunicación entre parachains usa XCM —Cross-Consensus Message Format. XCM no es un protocolo de transporte; es un lenguaje para describir operaciones cross-chain. Un mensaje XCM puede decir "transfiere X tokens", pero también puede decir "ejecuta esta llamada en destino" o "si esto falla, devuelve esto en origen". La relay chain garantiza la entrega de esos mensajes porque ha validado los bloques de las parachains que participan.

La distinción práctica entre IBC y XCM es que IBC conecta cadenas soberanas con su propia seguridad, mientras que XCM conecta cadenas dentro de un ecosistema que comparte una base de seguridad común. Son respuestas a problemas de diseño distintos.

---

## Las capas de abstracción: quién decide cómo se ejecuta

Por encima de los mercados, los componentes y los protocolos de interoperabilidad existe una capa que no ejecuta operaciones económicas ni mueve activos: decide **cómo** se ejecuta algo para obtener el mejor resultado posible. Esta capa es la que el usuario suele ver sin saber que está ahí.

### Agregadores de DEX

Un agregador de DEX como 1inch, Matcha u Odos consulta en tiempo real múltiples fuentes de liquidez dentro de una misma cadena —distintos AMMs, libros de órdenes, pools especializados— y encuentra la ruta de menor slippage y menor coste para una operación dada. Puede dividir una orden entre varios pools simultáneamente si eso produce mejor precio que ejecutar en uno solo.

El agregador no forma precios ni custodia liquidez. El precio lo forman los mercados subyacentes; el agregador solo decide cuál de ellos —o qué combinación— ofrece la mejor ejecución en ese momento. Es una capa de routing, no un mercado.

### Agregadores cross-chain

LI.FI y Socket hacen lo mismo pero extendiéndolo a cadenas distintas y a los mecanismos que las conectan. Cuando un usuario quiere mover USDC de Ethereum a Base, LI.FI consulta múltiples bridges —Across, Stargate, CCTP, Hop— compara tiempo de llegada, coste total y output final, y ejecuta la ruta más eficiente. El usuario no decide qué bridge usa; el agregador lo decide por él.

Esta capa es la que muchos wallets y frontends usan internamente para ofrecer una experiencia de "bridging en un clic" sin que el usuario sepa qué protocolo está detrás. Desde el punto de vista del sistema, LI.FI no es una pieza de interoperabilidad; es una pieza de abstracción y routing sobre piezas de interoperabilidad.

### Solvers y fillers: el motor de ejecución de los intents

El solver y el filler son los actores que hacen posible los mercados basados en intents, y aunque los términos se usan a veces de forma intercambiable, tienen roles distintos en el mecanismo.

El **filler** es el actor que adelanta capital para cumplir una intención. En Across, cuando un usuario quiere 1.000 USDC en Base, el filler los entrega de su propio inventario; el filler es quien asume el riesgo de que el protocolo le reembolse después. En este sentido, el filler es esencialmente un market maker: tiene capital en varias cadenas, monitorea intenciones entrantes y las cumple cuando el margen lo justifica.

El **solver** es más amplio: es cualquier actor que compite por encontrar y ejecutar la mejor manera de cumplir una intención, y puede usar cualquier fuente de liquidez disponible. En CoW Swap, los solvers compiten para encontrar la mejor ruta de ejecución, que puede incluir coincidencias directas entre órdenes del mismo batch —los llamados Coincidence of Wants o CoWs—, pools de AMMs, o market makers fuera de cadena. El solver que gana el batch es quien ofrece la mejor ejecución a los usuarios.

La diferencia entre un solver y un agregador es de posición en el flujo: el agregador calcula la ruta antes de que el usuario firme y ejecuta lo que el usuario ya aceptó; el solver recibe una intención ya firmada por el usuario y compite con otros solvers para encontrar la mejor ejecución posible, con grado de libertad para usar las fuentes que quiera. El agregador optimiza dentro de un espacio definido; el solver descubre ese espacio y compite en él.

---
