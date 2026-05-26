# Fundamentos Económicos para Web3

## Prólogo

Este documento es tu guía educativa para entender los principios económicos que sostienen proyectos Web3 exitosos. No encontrarás historias de colapsos aquí, sino **conceptos fundamentales explicados sistemáticamente** con fórmulas, métricas y ejemplos de cómo aplicarlos correctamente.

**¿Para quién es este documento?**:

- Founders diseñando su primera tokenomics desde cero
- Desarrolladores que necesitan entender el "por qué" detrás de decisiones económicas
- Cualquiera que quiera analizar protocolos con rigor económico
- Personas sin formación en economía que necesitan un punto de partida sólido

**¿Qué encontrarás aquí?**:

- Glosario completo de métricas (Market Cap, TVL, FDV, APY vs APR)
- Conceptos económicos fundamentales aplicados a Web3
- Fórmulas para calcular inflación, dilución, CAC, LTV
- Frameworks para valorar protocolos y analizar cohortes
- Guías sobre gestión de tesorería y riesgos

**¿Qué NO es este documento?**:

- No es una colección de casos de estudio de fracasos (para eso lee [economic-failures-and-lessons.md](economic-failures-and-lessons.md))
- No es una receta única que funcione para todo proyecto
- No reemplaza asesoría legal, financiera o fiscal profesional

**Estructura pedagógica**: Cada sección construye sobre la anterior. Si un concepto te parece confuso, retrocede a las secciones previas. El documento está diseñado para leerse secuencialmente desde el principio, pero el glosario inicial te permite usarlo como referencia rápida.

**Orden de lectura recomendado**: Lee este documento primero para construir tu base conceptual. Luego lee [economic-failures-and-lessons.md](economic-failures-and-lessons.md) para ver cómo estos conceptos fueron ignorados en proyectos reales y qué consecuencias tuvieron.

---

Construir en Web3 no solo requiere entender tecnología blockchain, smart contracts o criptografía. Requiere entender economía. Cada protocolo descentralizado es, en esencia, una economía en miniatura con sus propias reglas de creación, distribución y captura de valor. Cada token es un activo financiero con dinámicas de oferta y demanda. Cada DAO es una organización que debe gestionar recursos escasos para maximizar valor.

Este documento es una guía práctica de conceptos económicos fundamentales aplicados al contexto Web3. No asume conocimiento previo de economía, pero sí asume que estás involucrado o interesado en proyectos descentralizados. El objetivo es que, al terminar, puedas entender las métricas que importan, evaluar la salud económica de protocolos, y diseñar sistemas tokenómicos sostenibles.

La estructura sigue un camino de aprendizaje: empezamos con conceptos básicos de economía, avanzamos hacia finanzas corporativas y métricas empresariales, y terminamos aplicando todo esto específicamente a proyectos Web3 con tokens. Cada sección conecta teoría económica clásica con ejemplos concretos del ecosistema descentralizado.

## Glosario de métricas fundamentales

Antes de profundizar, es útil tener un vocabulario común de métricas básicas que se usan constantemente en Web3. Estas definiciones te ayudarán a seguir el resto del documento y a analizar protocolos efectivamente.

**Market Cap (Capitalización de Mercado)**: El valor total de todos los tokens en circulación. Se calcula como `Market Cap = Precio del token × Supply circulante`. Si un token cotiza a $10 y hay 50M tokens circulando, el market cap es $500M. Nota importante: usa supply circulante, no supply total. Los tokens bloqueados en vesting o sin desbloquear no cuentan para market cap, pero sí para FDV.

**FDV (Fully Diluted Valuation)**: El valor que tendría el protocolo si todos los tokens prometidos existieran hoy. Se calcula como `FDV = Precio del token × Supply máximo total`. Si planeas emitir 1B tokens totalmente pero solo 100M circulan hoy, y el precio es $10, tu market cap es $1B pero tu FDV es $10B. Un ratio FDV/Market Cap >3x indica que hay mucha dilución futura esperando a los holders actuales.

**TVL (Total Value Locked)**: El valor total de activos depositados en un protocolo DeFi. Un lending protocol cuenta todos los depósitos de usuarios. Un DEX cuenta la liquidez en sus pools. Un protocolo de staking cuenta todos los tokens stakeados. Mayor TVL generalmente indica mayor confianza y uso. Aave tiene ~$5-10B en TVL. Uniswap tiene ~$3-5B. Protocolos pequeños tienen <$100M.

**Liquidez**: La facilidad de comprar o vender un activo sin afectar significativamente su precio. Un token con alta liquidez tiene grandes volúmenes de trading y muchos compradores/vendedores. Puedes vender $100K sin mover el precio 5%. Un token con baja liquidez ve slippage masivo en trades pequeños. La liquidez en DEXs se mide por el tamaño de los pools. Un pool ETH/USDC con $50M de liquidez es profundo. Uno con $500K es superficial.

**Volume (Volumen)**: El valor total de transacciones en un período. Los DEXs reportan volumen diario o mensual. Uniswap procesa $1-3B de volumen diario en bull markets. Curve procesa $500M-1B diario en stablecoin swaps. Mayor volumen genera más fees. El ratio Volume/TVL mide eficiencia de capital: si tienes $100M de TVL generando $50M de volumen diario, tu capital se usa 0.5x por día (excelente).

**APY vs APR**: Ambos miden rendimiento anual, pero APY incluye compounding, APR no. Si un pool paga 50% APR y reinviertes ganancias diariamente, tu APY será ~64% porque estás compounding. La fórmula es `APY = (1 + APR/n)^n - 1` donde n es frecuencia de compounding. Muchos protocolos reportan APY para sonar más atractivos. Siempre pregunta si es APY o APR y con qué frecuencia de compounding se calculó el APY.

**Slippage**: La diferencia entre el precio esperado y el precio ejecutado en un trade. Si intentas comprar un token a $10 pero se ejecuta a $10.50, tu slippage es 5%. Esto pasa por baja liquidez o trades grandes. Los DEXs modernos te dejan establecer máximo slippage tolerable (ej: "no ejecutes si slippage >2%"). En pools profundos, slippage es <0.5%. En pools superficiales, puede ser 10%+.

**Impermanent Loss (IL)**: La pérdida que experimentan LPs (proveedores de liquidez) cuando el precio de tokens en el pool cambia vs. simplemente holdear esos tokens. Si depositas 1 ETH + 3000 USDC en un pool (ETH a $3000), y ETH sube a $6000, el pool te rebalancea a 0.707 ETH + 4242 USDC = $8484. Pero si hubieras holdeado, tendrías 1 ETH + 3000 USDC = $9000. La diferencia ($516) es impermanent loss. Se llama "impermanent" porque si el precio vuelve a $3000, la pérdida desaparece. Pero si retiras cuando el precio está diferente, la pérdida se vuelve permanente.

**Protocol Revenue**: Los ingresos brutos que genera el protocolo de fees de usuarios. Diferente de token holder value. Uniswap genera $200-500M anuales en revenue, pero ese dinero va a LPs, no a holders de UNI (aún). GMX genera $100M+ anuales y distribuye 70% a stakers. Cuando analices protocolos, pregunta: ¿el revenue va al protocolo/token holders, o a otros participantes?

**Circulating Supply**: Cantidad de tokens que existen y están disponibles para tradear hoy. Excluye tokens en vesting de equipo/inversores, tokens en tesorería sin desbloquear, y tokens quemados. Bitcoin tiene ~19.5M circulating supply de máximo 21M. Muchos tokens lanzan con 10-20% circulating supply y van desbloqueando el resto en 2-4 años.

Con estas métricas básicas definidas, podemos adentrarnos en los conceptos más profundos que construyen sobre ellas.

## Dinero y valor: los cimientos

Antes de hablar de tokens, necesitamos entender qué es el dinero. Suena básico, pero la confusión sobre este concepto ha causado el colapso de numerosos proyectos cripto. El dinero no es solo un medio de intercambio, es un sistema de tres funciones interconectadas que deben cumplirse simultáneamente.

La primera función es servir como medio de cambio. El dinero facilita transacciones eliminando la necesidad de trueque. En Web3, los tokens nativos de protocolos intentan cumplir esta función dentro de sus ecosistemas. ETH es el medio de cambio en Ethereum, usado para pagar gas fees. MATIC cumple la misma función en Polygon. Pero para que un token sea buen medio de cambio, necesita liquidez y aceptación amplia dentro de su contexto.

La segunda función es reserva de valor. El dinero debe mantener poder adquisitivo en el tiempo. Esta es donde muchos tokens fallan. Si tu token pierde 90% de su valor en seis meses, nadie quiere guardarlo. Bitcoin fue diseñado explícitamente como reserva de valor con su supply limitado a 21 millones. Las stablecoins como USDC y DAI intentan ser reservas de valor perfectas manteniendo paridad con el dólar. Los tokens de gobernanza de protocolos establecidos (UNI, AAVE, MKR) funcionan como reservas de valor en la medida que el protocolo mantiene su utilidad y captura valor.

La tercera función es unidad de cuenta. El dinero mide el valor de bienes y servicios. En Web3, esto se vuelve interesante porque diferentes comunidades usan diferentes unidades de cuenta. Los maxi-bitcoiners piensan en satoshis. Los DeFi degens piensan en ETH. Los builders piensan en dólares (via stablecoins). Cuando un protocolo fija precios o reporta métricas, la elección de unidad de cuenta importa. Un protocolo que reporta ingresos en su token nativo puede mostrar crecimiento exponencial mientras el valor real en dólares colapsa.

Para que algo funcione como dinero completo, debe cumplir las tres funciones. Bitcoin es fuerte en reserva de valor y unidad de cuenta (para su comunidad), pero débil como medio de cambio por fees altos y tiempos lentos. ETH es fuerte en medio de cambio (dentro de Ethereum) y cada vez más fuerte como reserva de valor post-Merge. Las stablecoins son excelentes para las tres funciones, pero dependen de confianza en el emisor o mecanismos de colateralización complejos (por ejemplo DAI usa crypto como colateral (depositas ETH para mintear DAI), lo cual es descentralizado pero complejo).

Cuando evalúes un token, pregúntate: ¿Para qué de estas tres funciones fue diseñado? ¿Las cumple efectivamente? Un token de gobernanza puro no pretende ser medio de cambio, y está bien. Un token de utilidad debe facilitar transacciones pero no necesariamente ser reserva de valor. El problema surge cuando proyectos afirman que su token cumple funciones que claramente no puede cumplir, o cuando la tokenómica destruye la función declarada.

## Oferta y demanda: la ley fundamental

Si solo pudieras entender un concepto económico para trabajar en Web3, debería ser oferta y demanda. Es simple pero poderoso: cuando la oferta de algo aumenta y la demanda se mantiene constante, el precio cae. Cuando la demanda aumenta y la oferta se mantiene constante, el precio sube. Toda la tokenómica exitosa respeta esta ley. Toda la tokenómica fallida la ignora.

En economía tradicional, oferta y demanda se equilibran naturalmente en mercados libres. Los productores ajustan cuánto producen basándose en el precio. Los consumidores ajustan cuánto compran basándose en el precio. El mercado encuentra un equilibrio. En Web3 con tokens, la oferta a menudo está programada y no responde dinámicamente a la demanda. Esto crea problemas si el schedule de emisión no anticipa correctamente la adopción.

Veamos la oferta primero. En un token, la oferta está determinada por el supply total y el schedule de emisión. Bitcoin tiene supply fijo de 21 millones y emisión decreciente (halvings cada 4 años). Esto crea escasez programada. Ethereum post-Merge tiene emisión baja (~0.5% anual) que puede volverse negativa (deflacionaria) cuando hay mucha actividad on-chain y se queman más fees que los que se emiten. Muchos tokens de protocolos DeFi tienen emisión inflacionaria alta inicialmente para bootstrapping, que se reduce con el tiempo.

El error común es emisión inflacionaria sin límite o reducción planificada. Si emites 10% de nuevo supply cada mes indefinidamente, estás constantemente diluyendo a los holders existentes. Para que el precio se mantenga, necesitas que entren nuevos compradores que absorban ese 10% cada mes. Esto raramente es sostenible. Es el modelo que usaron los forks de OlympusDAO y todos colapsaron.

Ahora la demanda. ¿Qué crea demanda por un token? Hay dos fuentes principales: utilidad real y especulación. La utilidad real viene de necesitar el token para hacer algo. Necesitas ETH para pagar gas. Necesitas AAVE para votar en gobernanza de Aave o para stakeralo en el safety module y ganar fees. Necesitas CRV para dirigir emisiones en Curve. Esta es demanda orgánica sostenible.

La especulación es demanda basada en expectativa de apreciación futura. No hay nada intrínsecamente malo en especulación, todos los activos financieros tienen componente especulativo. El problema es cuando la especulación es la única fuente de demanda. Si un token no tiene utilidad real, la única razón para comprarlo es esperar que otros lo compren después a mayor precio. Esto es la definición de esquema Ponzi.

Los mejores tokens combinan ambas fuentes de demanda. ETH tiene utilidad (pagar gas, staking para validar, colateral en DeFi) y especulación (apreciación por adopción de Ethereum). UNI tiene utilidad (gobernanza, potencial fee switch) y especulación (apreciación si Uniswap sigue dominando). Los peores tokens solo tienen especulación sin utilidad subyacente.

Para diseñar tokenómica sostenible, debes alinear oferta con demanda esperada. Si planeas emitir grandes cantidades de tokens como incentivos, necesitas crear utilidad equivalente que genere demanda orgánica. Si no puedes crear esa utilidad, reduce la emisión. Es mejor tener un token escaso con alta demanda que un token abundante con demanda inexistente.

## Inflación del token: matemáticas y dilución

La inflación del token es uno de los conceptos más críticos y peor entendidos en tokenómica. Muchos founders diseñan schedules de emisión sin calcular realmente qué significan para los holders. Muchos holders compran tokens sin entender cuánto serán diluidos. Esto causa desalineación, sell pressure, y colapsos de precio evitables.

Empecemos con la definición básica. La inflación del token es la tasa a la cual aumenta el supply circulante. Si tienes 100M tokens en circulación hoy y 110M en un año, tu tasa de inflación anual es 10%. Esto es diferente de inflación de precios: el token puede inflarse en supply pero apreciarse en precio si la demanda crece más rápido que la oferta.

La matemática fundamental es simple pero poderosa: **para mantener el precio constante con X% de inflación anual, necesitas X% más de demanda (capital entrante) cada año**. Si tu supply crece 20% anualmente, necesitas que $20 de cada $100 de market cap entren como nueva demanda solo para mantener el precio. Para que el precio suba, necesitas aún más demanda.

Veamos ejemplos concretos. Bitcoin tiene inflación decreciente por halvings. Actualmente emite ~1.8% anual (900 BTC/día con ~19.5M supply). Después del próximo halving (2024), será ~0.9% anual. En 2032, será ~0.45%. Eventualmente se aproxima a cero. Esto hace Bitcoin deflacionario en el largo plazo, especialmente considerando loss de keys (se estima 3-4M BTC perdidos para siempre).

Ethereum post-Merge tiene inflación nominal de ~0.5% anual de emisión a validadores. Pero EIP-1559 quema fees en cada transacción. Cuando la actividad on-chain es alta, se queman más ETH del que se emite, haciendo el supply deflacionario. Durante 2021 bull market, ETH fue deflacionario a tasas de -2% a -5% anual. Durante bear markets con baja actividad, vuelve levemente inflacionario. El punto clave es que la inflación de ETH es dinámica y puede ser negativa.

Los tokens DeFi típicos tienen inflación mucho más alta. Curve (CRV) emitía ~50% anual en sus primeros años, reduciéndose gradualmente. Muchos tokens de AMMs y lending protocols emiten 10-30% anual como incentivos a LPs y usuarios. Esto crea presión vendedora masiva: si los usuarios farmean tokens y los venden inmediatamente (comportamiento común), ese 10-30% de nuevo supply entra al mercado como sell pressure constante.

El concepto de **terminal inflation rate** es crucial en diseño. Es la tasa de inflación a la que eventualmente llegas cuando las emisiones iniciales altas terminan. Bitcoin tiene terminal rate de ~0% (llega a 21M y para). Ethereum tiene terminal rate de ~0.5% (sin contar burning). Muchos tokens DeFi no tienen terminal rate claro, lo cual es problema: inflación indefinida alta eventualmente colapsa el precio.

Calculemos dilución concreta para holders. Supón que tienes 1% del supply de un token (1M de 100M tokens). Si el protocolo emite 20M tokens adicionales este año como incentivos, el nuevo supply total es 120M. Tu 1M tokens ahora representa 0.833% del supply (1/120 = 0.00833). Has sido diluido de 1% a 0.833%, perdiendo 16.7% de tu porcentaje de ownership. Si el precio no sube 16.7%, tu holding vale menos en términos absolutos.

La **presión vendedora** de emisiones es a menudo subestimada. Si emites $10M en tokens como incentivos anuales y los recipientes venden 80% inmediatamente (común con mercenary capital), eso es $8M de sell pressure que debe ser absorbida por nueva demanda. Si tu volumen de trading diario es $500K, esos $8M anuales son ~$22K diarios, o 4.4% del volumen. Eso es presión significativa.

El trade-off fundamental en diseño de emisiones es: **alta inflación inicial para bootstrapping vs. sostenibilidad a largo plazo**. Los protocolos necesitan atraer usuarios y liquidez tempranamente. Las emisiones altas (30-50% APY) lo logran rápido. Pero si no reduces esas emisiones gradualmente, destruyes valor para holders a largo plazo. El schedule ideal empieza alto y decrece suavemente hacia un terminal rate bajo (0-5%).

Curve diseñó esto inteligentemente. CRV empezó con emisión muy alta (~300M CRV primer año de ~2B supply inicial), pero decrece gradualmente cada año según una curva programada. La inflación anual de CRV hoy es ~15%, bajará a ~5% en años futuros, y eventualmente a ~2%. Esto permitió bootstrapping masivo (Curve dominó stablecoin swaps rápido) mientras creaba sostenibilidad eventual.

El **burning** puede contrarrestar inflación. MakerDAO quema MKR con surplus de fees del protocolo. Binance quema BNB trimestralmente. Si tu inflación es 10% pero quemas 8%, tu inflación neta es 2%. Algunos protocolos buscan ser "net deflationary" donde burning excede emisión. Esto solo funciona si el burning está financiado por revenue real, no por imprimir tokens para quemar (lo cual es circular y sin sentido).

Las **métricas clave** que debes calcular para cualquier token son:

1. **Inflación anual actual**: (Tokens emitidos próximo año / Supply circulante actual) × 100
2. **Terminal inflation rate**: ¿A qué tasa llegas en 5-10 años?
3. **FDV (Fully Diluted Valuation)**: Precio × Supply máximo total
4. **Ratio FDV/Market Cap**: FDV / (Precio × Supply circulante). Ratios >3x indican mucha dilución futura.
5. **Inflación neta**: Inflación nominal - burning (si aplica)
6. **Sell pressure por día**: (Emisiones diarias × % vendido) / Volumen de trading diario

Ejemplo práctico: Estás diseñando un token para tu DEX. Planeas 1B tokens totales. Lanzas con 100M circulantes (10%). Quieres emitir 200M en primeros 2 años como incentivos a LPs (100M por año). Tu inflación año 1 es 100M/100M = 100%. Año 2 es 100M/200M = 50%. Eso es insosteniblemente alto. Los holders serán diluidos masivamente. A menos que tu protocolo crezca 2-3x en uso, el precio colapsará.

Alternativa: Emite 30M año 1 (30% inflación), 20M año 2 (15%), 15M año 3 (10%), decreciendo a 5M/año después (2-3%). Total de emisiones a largo plazo es similar, pero distribuidas más sosteniblemente. Esto da tiempo para que la demanda se acumule sin abrumar el mercado con supply.

La lección: **haz las matemáticas antes de lanzar**. Calcula cuánto diluirás a holders. Modela escenarios de precio asumiendo que toda la emisión se vende. Si tu tokenómica solo funciona asumiendo que nadie vende, fallará. Diseña para el caso donde los farmers son mercenarios y venden todo, porque muchos lo harán.

## Macro y microeconomía aplicadas

La economía se divide tradicionalmente en dos ramas: macroeconomía y microeconomía. La macroeconomía estudia sistemas económicos completos, ciclos, inflación, política monetaria. La microeconomía estudia agentes individuales, empresas, consumidores, y cómo toman decisiones. En Web3, necesitas entender ambas.

La perspectiva macroeconómica es crucial para entender el contexto en que opera tu proyecto. Crypto está profundamente conectado con macroeconomía global. Cuando la Reserva Federal de Estados Unidos sube tasas de interés, el capital fluye de activos riesgosos (como crypto) hacia activos seguros (como bonos del tesoro). Esto causa bear markets. Cuando la Fed baja tasas e inyecta liquidez, el capital busca retornos más altos y fluye hacia activos riesgosos. Esto causa bull markets.

No puedes controlar la macroeconomía, pero puedes planear para ella. Los proyectos que lanzaron en 2021 durante el bull market y diseñaron su tokenómica asumiendo que ese mercado continuaría, colapsaron en 2022. Los proyectos que planearon para ciclos completos (bull y bear) sobrevivieron. Esto significa dimensionar equipos sosteniblemente, convertir tesorería a stablecoins durante bull markets, y diseñar emisiones que funcionen incluso si el precio del token cae 80%.

La inflación macroeconómica también afecta crypto. Cuando la inflación del dólar es alta, activos escasos como Bitcoin se vuelven más atractivos. Pero cuando la inflación causa que bancos centrales suban tasas agresivamente, el efecto neto suele ser negativo para crypto a corto plazo. Entender estas dinámicas te ayuda a tomar decisiones sobre cuándo fundraisear, cuándo lanzar, y cómo posicionar tu tesorería.

La perspectiva microeconómica te ayuda a entender el comportamiento de usuarios individuales en tu protocolo. Cada usuario es un agente económico racional que toma decisiones para maximizar su propio beneficio. Si diseñas incentivos pensando que los usuarios actuarán altruistamente por el bien del protocolo, estás equivocado. Actuarán en su propio interés, y tu trabajo es alinear ese interés con la salud del protocolo.

Un ejemplo de microeconomía aplicada es el diseño de pools de liquidez en AMMs. Los proveedores de liquidez (LPs) son agentes racionales que buscan maximizar retornos ajustados por riesgo. Comparan el APY de tu pool con pools competidores, consideran impermanent loss, y mueven su capital donde obtengan mejor retorno. Si quieres retener liquidez, debes ofrecer retornos competitivos o crear switching costs (como lockups, tokens vote-escrowed, o NFT positions).

Otro ejemplo es la participación en gobernanza. Los holders de tokens de gobernanza son agentes racionales. Si votar no les genera valor directo, no votarán. Por eso muchas DAOs tienen bajísima participación en votaciones. Los protocolos exitosos crean incentivos para participar: Curve da fees a holders de veCRV que votan, lo que genera participación alta. MakerDAO paga a delegates para que investiguen propuestas y voten informadamente.

La lección microeconómica fundamental es: diseña como si cada usuario fuera perfectamente racional y egoísta. Si tu sistema funciona bajo esa asunción, funcionará en la realidad donde la mayoría son racionales y algunos altruistas. Si tu sistema requiere altruismo para funcionar, fallará cuando encuentre usuarios racionales (que son la mayoría).

## Finanzas corporativas en protocolos descentralizados

Las finanzas corporativas estudian cómo las empresas toman decisiones sobre inversión, financiación, y distribución de valor. Aunque los protocolos descentralizados no son empresas tradicionales, enfrentan decisiones similares. Un tesorero DAO debe decidir cómo invertir fondos. Un protocolo debe decidir si usar deuda o equity para financiarse. Una comunidad debe decidir cómo distribuir valor entre stakeholders.

Empecemos con métricas básicas de rentabilidad. En empresas tradicionales, EBITDA (Earnings Before Interest, Taxes, Depreciation, and Amortization) mide ganancias operativas antes de costos financieros y contables. En Web3, el equivalente es protocol revenue: los ingresos que genera el protocolo de sus usuarios. Uniswap genera revenue de trading fees. Aave genera revenue de intereses en préstamos. Lido genera revenue de comisiones en staking.

La diferencia crucial es que en Web3 debemos distinguir entre protocol revenue y token holder value. Uniswap genera cientos de millones en revenue anualmente, pero ese valor va a LPs (proveedores de liquidez), no a holders de UNI. El "fee switch" que permitiría enviar parte de esas fees a holders de UNI nunca se ha activado. Entonces UNI captura valor solo via gobernanza, no via cash flows. Esto es radicalmente diferente de equity tradicional.

GMX, en contraste, distribuye 70% de sus fees a stakers de GMX y GLP. Esto crea captura de valor directa. Si stakeas GMX, recibes un porcentaje de todos los fees que genera el protocolo. Es similar a recibir dividendos de una empresa tradicional. Los holders de GMX pueden calcular un P/E ratio (precio/ganancias) real, porque el token genera cash flows medibles.

Otra métrica corporativa importante es ROA (Return on Assets): cuánto beneficio generan tus activos. En un protocolo DeFi, los "activos" principales son la liquidez en pools, el TVL (Total Value Locked), y la tesorería. Un protocolo con $100M en TVL que genera $10M en fees anuales tiene un ROA de 10%. Si esas fees van al protocolo o a holders, es excelente. Si van completamente a LPs mientras el protocolo no captura valor, entonces el protocolo mismo tiene ROA de 0%.

ROE (Return on Equity) mide retorno sobre el capital propio. En Web3, el "equity" es el market cap del token más la tesorería. Un protocolo con $50M en market cap y $20M en tesorería ($70M equity total) que genera $7M en ganancias para token holders tiene ROE de 10%. Es una métrica potente para comparar protocolos: cuánto valor generan por dólar de capitalización.

Ahora hablemos de valoración. En finanzas tradicionales, el VAN (Valor Actual Neto) descuenta flujos de caja futuros al presente. Si un proyecto generará $1M anuales durante 10 años, esos flujos futuros valen menos que $10M hoy porque podrías invertir ese dinero ahora y ganar retornos. Usas una tasa de descuento (típicamente el WACC - costo promedio ponderado de capital) para calcular el valor presente.

En Web3, puedes aplicar VAN para valorar tokens que generan cash flows. Si GMX distribuye $20M anuales a stakers y esperas que eso continúe, puedes descontar esos flujos para calcular el valor "justo" del token. Si usas una tasa de descuento de 15% (apropiada para un activo riesgoso), el VAN de flujos perpetuos es aproximadamente $133M. Si el market cap de GMX es $300M, está sobrevalorado. Si es $80M, está subvalorado.

La mayoría de tokens en Web3 no generan cash flows directos a holders, lo que hace valoración más difícil. Debes valorar basándote en utilidad esperada, poder de gobernanza, o especulación sobre cash flows futuros. Esto es similar a valorar empresas de crecimiento que no son rentables aún: estás apostando a adopción futura y captura de valor eventual.

La TIR (Tasa Interna de Retorno) es útil para evaluar inversiones. Si inviertes en un token a $10, proyectas cash flows o apreciación futura, y calculas que obtendrás 25% anual, esa es tu TIR. Compárala con tu costo de oportunidad (¿qué otro activo podrías comprar con ese dinero?) y tu tolerancia al riesgo. Una TIR de 25% en un protocolo establecido es excelente. La misma TIR en un protocolo experimental puede no ser suficiente dado el riesgo.

## Teoría de juegos e incentivos

La teoría de juegos es fundamental en Web3 porque estamos diseñando sistemas donde múltiples participantes toman decisiones estratégicas que afectan a todos los demás. Cada holder de token, cada LP, cada validador, cada voter en gobernanza es un jugador en un juego complejo. Si no entiendes teoría de juegos, diseñarás sistemas que colapsan cuando los jugadores actúen racionalmente.

El concepto central es el equilibrio de Nash: una situación donde ningún jugador puede mejorar su resultado cambiando unilateralmente su estrategia. En un sistema bien diseñado, el equilibrio de Nash debería estar alineado con el bien del protocolo. En un sistema mal diseñado, el equilibrio de Nash puede destruir el protocolo.

Un ejemplo clásico es la tragedy of the commons aplicada a DAOs. Imagina una DAO con tesorería de $10M y 1000 holders de governance tokens. Si cada holder puede votar para transferirse fondos del tesorero, y si todos los holders votan simultáneamente, el equilibrio de Nash es que todos votan para extraer el máximo posible antes de que otros lo hagan. El resultado es que la tesorería se vacía y el protocolo muere.

La solución no es confiar en que los holders actuarán altruistamente. La solución es diseñar mecanismos donde extraer valor tiene costos o riesgos. MakerDAO hace que MKR sea el backstop: si el sistema se vuelve insolvente por malas decisiones de gobernanza, se mintea nuevo MKR para cubrir pérdidas, diluyendo a todos los holders. Esto crea skin in the game: votar irresponsablemente te perjudica directamente.

Otro concepto crucial es el dilema del prisionero. Dos jugadores se benefician si cooperan, pero cada uno tiene incentivo individual de traicionar al otro. En Web3, esto aparece en situaciones de coordinación. Los holders se benefician si todos mantienen sus tokens (precio sube por baja presión vendedora), pero cada holder individualmente se beneficia de vender si otros mantienen. El equilibrio es que nadie confía en que otros mantengan, entonces todos venden, colapsando el precio.

Los mejores protocolos crean mecanismos que revierten el dilema del prisionero. El modelo vote-escrowed (veCRV de Curve) requiere que bloquees tokens por hasta 4 años para obtener máximo voting power. Esto crea commitment creíble: al bloquear tokens, señalas que estás comprometido a largo plazo. Otros ven esto y tienen más confianza en mantener también, creando círculo virtuoso.

El staking con slashing es otro mecanismo anti-dilema del prisionero. En Ethereum PoS, validadores maliciosos pierden su stake. Esto hace que atacar sea mucho más costoso que validar honestamente, revirtiendo los incentivos del dilema. Cooperar (validar honestamente) genera retornos positivos. Traicionar (atacar) genera pérdidas garantizadas.

Los incentivos perversos son consecuencias no intencionales de mecanismos mal diseñados. El caso más famoso en Web3 es el capital mercenario en liquidity mining. Protocolos ofrecían tokens como incentivos a LPs, esperando construir liquidez permanente. En realidad, atrajeron yield farmers que entraban, farmeaban tokens, los vendían inmediatamente, y se iban al siguiente protocolo con mejor APY. La liquidez era temporal y costosa.

El problema no era incentivar liquidez per se. El problema era que los incentivos creaban comportamiento extractivo en lugar de constructivo. Los LPs maximizaban su ganancia individual (farming y dump) a expensas del protocolo (token dilution sin liquidez permanente). El protocolo asumió que los LPs actuarían en interés del protocolo, pero no habían alineado los incentivos para que actuar en interés propio beneficiara al protocolo.

Protocol-Owned Liquidity (POL) resolvió esto cambiando el mecanismo. En lugar de rentar liquidez continuamente, el protocolo compra liquidez permanentemente via bonding. Los participantes obtienen tokens con descuento a cambio de LP tokens. El protocolo retiene esos LP tokens para siempre. Ambos lados ganan: el participante obtiene ganancia inmediata del descuento, el protocolo obtiene liquidez que no se va cuando los incentivos cambian.

La lección de teoría de juegos es: asume que cada participante actuará en su propio interés racional. Modela cómo responderán a tus incentivos, especialmente en casos extremos. Si el comportamiento racional individual destruye el sistema colectivo, rediseña los incentivos hasta que actuar en interés propio simultáneamente beneficie al sistema.

## Métricas empresariales: CAC, LTV y Churn

Las métricas empresariales tradicionales son perfectamente aplicables a protocolos Web3. De hecho, son más importantes porque la competencia es global, sin fronteras, y con switching costs cercanos a cero. Un usuario puede cambiar de protocolo en minutos. Debes entender qué cuesta adquirir usuarios, cuánto valor generan, y con qué frecuencia se van.

CAC (Customer Acquisition Cost) es lo que cuesta adquirir un usuario nuevo. En empresas tradicionales, incluye marketing, ventas, onboarding. En Web3, incluye incentivos de tokens, airdrops, campaigns en redes sociales, partnerships, y grants. Si gastas $100K en un campaign de airdrop y adquieres 1000 usuarios activos, tu CAC es $100 por usuario.

El error común es no calcular CAC correctamente. Muchos protocolos airdroppean tokens valorados al precio de mercado actual. Si tu token cotiza a $10 y airdroppeas 100 tokens por usuario a 10,000 usuarios, contablemente gastaste $10M ($10 x 100 x 10,000). Pero en realidad no gastaste $10M en efectivo, emitiste tokens que pueden o no mantener ese valor. Debes considerar la dilución real y el costo de oportunidad de esos tokens.

Un CAC sostenible depende del LTV (Lifetime Value): cuánto valor genera cada usuario durante su ciclo de vida. Si tu CAC es $100 pero cada usuario solo genera $50 de valor, estás perdiendo dinero en cada adquisición. Si cada usuario genera $500, tienes un ratio LTV/CAC de 5x, lo cual es excelente.

En protocolos DeFi, el valor por usuario viene de fees generados. Si un usuario tradea en tu DEX generando $10 en fees promedio por mes, y permanece 12 meses, su LTV es $120. Si tu CAC fue $30, tu ratio LTV/CAC es 4x, sostenible. El desafío es que en Web3, muchos usuarios son mercenarios que vienen por incentivos y se van cuando terminan, generando LTV cercano a cero.

Para calcular LTV correctamente, necesitas tres componentes: valor promedio por transacción (o interacción), frecuencia de transacciones, y tiempo de retención. En un lending protocol, el valor por usuario viene de intereses pagados. Un usuario que deposita $10K generando $300 anuales en intereses, y permanece 3 años, tiene LTV de $900. Si le diste $200 en tokens airdropeados, tu ratio es 4.5x.

El Churn rate (tasa de abandono) es el porcentaje de usuarios que dejan de usar tu protocolo en un período. Si tienes 10,000 usuarios activos a inicio de mes y 9,000 a fin de mes, tu churn mensual es 10%. El churn anualizado sería mucho mayor (no simplemente 10% x 12, es exponencial). Alto churn significa que constantemente pierdes usuarios y debes gastar más en adquisición para mantener crecimiento.

Web3 tiene churn naturalmente alto porque switching costs son bajos. Los usuarios pueden usar múltiples protocolos simultáneamente sin exclusividad. Un usuario puede tener liquidez en Uniswap, Curve, y Balancer al mismo tiempo. No es "churn" en sentido tradicional, es fragmentación de atención. Debes competir continuamente por el capital y atención del usuario.

Reducir churn en Web3 requiere crear switching costs artificiales o proporcionar valor único. Los switching costs pueden ser tokens vote-escrowed que se deben bloquear largo plazo, NFT positions que generan valor creciente con tiempo, o reputation systems on-chain que se pierden al cambiar de protocolo. El valor único viene de liquidez profunda, integraciones con otros protocolos, o features que nadie más ofrece.

El funnel de conversión es el proceso desde awareness hasta usuario activo. En Web3, el funnel típico es: awareness (oyen del protocolo) → visita (exploran el dapp) → conexión wallet → transacción inicial → usuario activo → power user. Mides conversión en cada etapa. Si 10,000 personas visitan tu dapp, 1,000 conectan wallet, 100 hacen transacción, y 50 se vuelven activos, tienes tasas de conversión de 10%, 10%, y 50% respectivamente.

Optimizar el funnel significa identificar donde pierdes usuarios y mejorar esa etapa. Si muchos conectan wallet pero no transactan, quizá tus fees son muy altos o la UX es confusa. Si muchos transactan una vez pero no vuelven, quizá tu producto no tiene retención. Cada protocolo tiene cuellos de botella diferentes.

## Análisis de cohortes: midiendo retención real

El análisis de cohortes es la herramienta más poderosa para entender si tu protocolo realmente retiene usuarios o solo los atrae temporalmente. Una cohorte es un grupo de usuarios que comparten una característica común en un período de tiempo específico. La característica más común es "usuarios que hicieron su primera transacción en el mismo mes".

La diferencia entre métricas agregadas y análisis de cohortes es fundamental. Si reportas "10,000 usuarios activos este mes", suena bien. Pero si 9,000 son nuevos y solo 1,000 son del mes pasado, tu retención es terrible (10%). Si 8,000 son antiguos y 2,000 son nuevos, tu retención es excelente (80%). Las métricas agregadas esconden esta diferencia crítica. Las cohortes la revelan.

Así se construye un análisis de cohortes básico. Divide usuarios por mes de adquisición (primera transacción). Para cada cohorte, mide qué porcentaje permanece activo cada mes subsecuente. Ejemplo:

- **Cohorte Enero 2024**: 1,000 usuarios adquiridos
  - Febrero: 400 activos (40% retención mes 1)
  - Marzo: 250 activos (25% retención mes 2)
  - Abril: 180 activos (18% retención mes 3)
  - Mayo: 150 activos (15% retención mes 4)
  - Junio: 140 activos (14% retención mes 5)

- **Cohorte Febrero 2024**: 1,500 usuarios adquiridos
  - Marzo: 600 activos (40% retención mes 1)
  - Abril: 400 activos (27% retención mes 2)
  - Mayo: 300 activos (20% retención mes 3)
  - Junio: 270 activos (18% retención mes 4)

Lo que ves inmediatamente: la retención se estabiliza alrededor de 15-20% después de 3-4 meses. Los usuarios que sobreviven los primeros 3 meses tienden a quedarse. Esto es típico en Web3: hay mucho churn inicial, pero un core de usuarios leales emerge.

Las **curvas de retención** revelan salud del producto. Una curva ideal tiene drop inicial seguido de plateau. Una curva que cae constantemente a cero indica producto sin retención (solo turistas). Una curva que plateaus a 20-40% indica producto con core de usuarios leales. Una curva que plateaus a >50% es excepcional en Web3.

Puedes segmentar cohortes por más que tiempo de adquisición. Cohortes por:

- **Fuente de adquisición**: Usuarios de Twitter vs. Discord vs. airdrop vs. partnerships
- **Primera acción**: Usuarios que swappearon vs. que proveyeron liquidez vs. que stakearon
- **Tamaño de transacción**: Ballenas (>$10K) vs. retail ($100-10K) vs. pequeños (<$100)
- **Incentivos recibidos**: Usuarios que recibieron airdrop vs. que no
- **Período de mercado**: Usuarios adquiridos en bull vs. bear market

Esto permite optimización quirúrgica. Ejemplo real: un lending protocol descubrió que usuarios adquiridos via partnerships con wallets tenían 60% retención a 6 meses, mientras usuarios de campañas Twitter tenían 15%. Conclusión: doblar inversión en partnerships, reducir gastos en Twitter ads. Sin análisis de cohortes, ambos canales parecían "generar usuarios".

El **LTV por cohorte** es aún más potente. No solo mides retención, sino valor generado. Si la cohorte de Enero tuvo 1,000 usuarios que generaron $50,000 en fees durante 6 meses, el LTV promedio es $50 por usuario. Si el CAC para esa cohorte fue $30, tu ratio LTV/CAC es 1.67x, marginalmente positivo. Si la cohorte de Marzo tiene LTV de $80 y CAC de $25 (3.2x ratio), algo mejoró: mejor targeting, mejor producto, o mejores incentivos.

Los protocolos Web3 tienen ventaja única: **todos los datos on-chain son públicos**. Puedes analizar cohortes de tus competidores. Dune Analytics, Nansen, y Flipside Crypto tienen dashboards de cohortes para protocolos mayores. Estudia qué funciona. Si Uniswap retiene 40% de usuarios nuevos al mes 3 y tú retienes 15%, hay mucho que aprender.

La aplicación más valiosa de cohortes es **optimizar emisiones de tokens**. Supón que emites 100K tokens mensuales como incentivos a LPs. Descubres que usuarios que entran por incentivos tienen 5% retención a 3 meses, mientras usuarios orgánicos tienen 50% retención. Los usuarios incentivados son mercenary capital que farmea y se va. Solución: reduce emisiones a 40K mensuales (ahorrando 60K), acepta menos usuarios mercenarios, enfócate en atraer usuarios orgánicos que realmente retienen.

Otro ejemplo: descubres que cohortes que recibieron onboarding personalizado (tutorial, discord support) tienen 45% retención vs. 20% sin onboarding. El onboarding cuesta $10 por usuario en tiempo de community managers. Pero aumenta LTV de $40 a $90 (+$50). El ROI es claro: invierte en onboarding. Sin análisis de cohortes, no sabrías que esos $10 generan $50 de valor incremental.

El patrón para usar cohortes efectivamente:

1. **Establece cohortes base** por mes de adquisición
2. **Mide retención mensual** de cada cohorte durante 6-12 meses
3. **Calcula LTV promedio** por cohorte (fees generados / número de usuarios)
4. **Segmenta por variables** (fuente, acción inicial, tamaño de transacción)
5. **Identifica qué cohortes retienen mejor** y por qué
6. **Ajusta estrategia**: invierte más en lo que genera mejores cohortes
7. **Re-mide después de cambios** para validar mejoras

Las herramientas específicas para esto en Web3 son Dune Analytics (SQL queries sobre datos on-chain), Nansen (dashboards pre-construidos), Flipside Crypto (queries y visualizaciones), y tu propio analytics interno si tienes off-chain data (emails, discord activity). Todos los protocolos serios usan al menos una.

La lección fundamental: **los usuarios no son fungibles**. Un usuario orgánico que usa tu producto porque resuelve su problema vale 10x más que un farmer que entró por 50% APY y se irá cuando baje a 40%. Cohortes te permiten distinguirlos, medir la diferencia, y optimizar para usuarios que importan. Sin cohortes, estás volando ciego con presupuestos de millones en incentivos.

## Gestión de tesorería y riesgos

La gestión de tesorería en DAOs y protocolos es fundamentalmente similar a gestión corporativa tradicional, pero con desafíos únicos de Web3. Una tesorería debe financiar operaciones (salarios, contractors, infraestructura), invertir para crecimiento (grants, partnerships, marketing), y mantener reservas para contingencias. La diferencia es que las tesorerías Web3 suelen estar en tokens volátiles, sujetas a gobernanza descentralizada, y completamente transparentes on-chain.

El primer principio de gestión de tesorería es diversificación. Si tu tesorería está 100% en tu token nativo, estás maximalmente expuesto a riesgo de precio. Si el token cae 80%, tu capacidad operativa se reduce 80%. Los protocolos prudentes convierten parte de su tesorería a stablecoins o activos menos volátiles. Olympus, en su momento pico, tenía tesorería casi completamente en activos que ellos controlaban pero que dependían del precio de OHM. Cuando OHM colapsó, la tesorería se evaporó.

El ratio común recomendado es mantener al menos 2-3 años de runway en stablecoins o activos de bajo riesgo. Esto significa que si tus gastos operativos son $2M anuales, deberías tener $4-6M en stablecoins. El resto puede estar en tokens nativos, LP positions, u otras inversiones más riesgosas. Esto te permite sobrevivir un bear market prolongado sin tener que vender tokens nativos a precios deprimidos.

El NOF (Necesidades Operativas de Fondo) mide cuánto capital necesitas para operaciones día a día. Incluye pagos a contributors, fees de infraestructura (nodes, front-ends, audits), y gastos administrativos. Muchos protocolos descentralizados operan con equipos lean de 5-20 personas full-time más contributors part-time, resultando en NOF de $100K-500K mensuales. Grandes protocolos con equipos de 50+ personas tienen NOF de $1-3M mensuales.

El fondo de maniobra es la diferencia entre activos corrientes y pasivos corrientes. En DAOs, los "activos corrientes" son stablecoins y tokens líquidos. Los "pasivos corrientes" son compromisos a corto plazo como grants aprobados o salarios del próximo trimestre. Un fondo de maniobra positivo indica capacidad de cumplir obligaciones. Un fondo negativo indica problemas de liquidez.

La gestión de riesgos en Web3 tiene dimensiones únicas. El riesgo de smart contract es peculiar del sector: tu tesorería puede ser hackeada si los contratos tienen vulnerabilidades. Los protocolos mitigan esto con audits múltiples, bug bounties, formal verification, y diversificación de custody (multi-sigs, timelockes para cambios grandes). MakerDAO tiene uno de los sistemas más robustos con múltiples capas de seguridad y procesos de gobernanza extensos.

El riesgo de gobernanza es que holders maliciosos o desinformados tomen malas decisiones. Si un whale acumula 51% de tokens de gobernanza, puede drenar la tesorería. Los protocolos mitigan esto con quórums elevados, timelocks que dan tiempo de reacción, y a veces vetos de emergency multisigs. Compound tiene un timelock de 2 días en cambios de gobernanza, permitiendo que la comunidad detecte propuestas maliciosas.

El riesgo de mercado es la volatilidad de tus assets. Si tu tesorería es $50M pero está en tokens que pueden caer 80% en un bear market, tu tesorería real es $10M en el peor caso. Debes planear para escenarios adversos, no solo para el caso base. Los mejores protocolos hacen stress testing: ¿cuánto tiempo sobrevivimos si el mercado cae 90%? ¿Necesitamos cambiar nuestro burn rate o diversificar más?

El riesgo operacional incluye perder contributors clave, regulaciones adversas, ataques de reputación, o competencia inesperada. A diferencia de empresas tradicionales, los protocolos descentralizados no pueden simplemente contratar un CEO y pivotear. Los cambios requieren consenso de gobernanza, que es lento. La resiliencia operacional viene de documentación exhaustiva, distribución de conocimiento, y cultura de descentralización real.

## Riesgo de contraparte y custodia de tesorería

El colapso de FTX en noviembre 2022 fue el wake-up call definitivo sobre riesgo de contraparte en Web3. DAOs y protocolos que tenían tesorerías de decenas o cientos de millones en FTX lo perdieron todo instantáneamente. Yuga Labs (Bored Ape), BlockFi, Genesis, y docenas de otros proyectos fueron afectados. La lección brutal: no importa qué tan establecido parezca un exchange o custodio, puede colapsar overnight.

El **riesgo de contraparte** es el riesgo de que la entidad que custodia tus assets no pueda o no quiera devolvértelos. En finanzas tradicionales, esto existe pero está mitigado por regulación, seguros (FDIC en bancos), y procesos de quiebra. En crypto, la regulación es mínima, no hay seguros garantizados, y recuperar fondos en quiebra es casi imposible. Si tu contraparte colapsa, asume pérdida total.

El espectro de custody va de totalmente centralizado a totalmente descentralizado. Cada opción tiene trade-offs:

**1. Exchanges centralizados (CEXs)**: Coinbase, Kraken, Binance, etc.

- **Pros**: Liquidez inmediata, fácil de convertir a fiat, interfaz user-friendly, seguros parciales (Coinbase tiene seguro para hot wallets).
- **Contras**: Contraparte centralizada, riesgo de hack, riesgo de quiebra, posible congelación de fondos por regulación.
- **Caso de uso**: Tesorería operativa pequeña que necesitas convertir a fiat frecuentemente ($100K-500K máximo).

Después de FTX, los exchanges "tier 1" (Coinbase, Kraken, Gemini) implementaron proof of reserves y mayor transparencia. Pero ninguno es riesgo cero. Binance ha enfrentado problemas regulatorios en múltiples jurisdicciones. Coinbase es público en NASDAQ lo cual da más transparencia, pero eso no elimina riesgo.

**2. Custodios institucionales**: Coinbase Prime, Anchorage, Fireblocks, BitGo.

- **Pros**: Servicios para instituciones, seguros de hasta $320M (BitGo), cumplimiento regulatorio, auditorías frecuentes.
- **Contras**: Fees más altos, proceso de onboarding complejo, aún es contraparte centralizada.
- **Caso de uso**: Tesorería grande que necesita servicios institucionales ($5M-50M).

Coinbase Prime es el más usado por DAOs y funds. Ofrece custody segregada, seguros, y complimiento con regulaciones. Pero aún requieres confiar en Coinbase. Si Coinbase colapsa (improbable pero no imposible), tus fondos están en riesgo a pesar de seguros.

**3. Multisigs on-chain**: Gnosis Safe (ahora Safe), multisigs nativos de chains.

- **Pros**: Verdadero self-custody, sin contraparte centralizada, transparencia total on-chain, control completo.
- **Contras**: Requiere gestión de keys, riesgo de pérdida de keys, sin recurso si múltiples signers pierden acceso o se confabulan.
- **Caso de uso**: Tesorería principal de protocolo descentralizado ($10M-$1B+).

La mayoría de DAOs serias usan Gnosis Safe con configuración M-of-N (ej: 4-of-7, 6-of-9). Los signers son miembros confiados de la comunidad o multisigs de sub-grupos. Esto distribuye riesgo: necesitas compromiso de múltiples personas para mover fondos, previniendo robo pero también agregando fricción operativa.

**4. Smart contracts del protocolo**: Fondos locked en contratos de tu protocolo.

- **Pros**: Máxima descentralización, sin trust en individuos, reglas programadas.
- **Contras**: Riesgo de smart contract bug o hack, inflexibilidad (cambios requieren upgrades).
- **Caso de uso**: Protocol-owned liquidity, insurance funds, staking rewards pools.

Protocolos DeFi establecidos mantienen cientos de millones o miles de millones en sus propios contratos (ej: Aave safety module, MakerDAO surplus buffer, Compound reserves). Esto es confiable si los contratos están bien auditados, pero hacks masivos (The DAO, Ronin bridge) muestran que ningún contrato es 100% seguro.

La **estrategia óptima para DAOs es diversificación en capas**:

- **Tier 1 (80-90% de tesorería)**: Multisig on-chain con activos de bajo riesgo (stablecoins, ETH). Gnosis Safe con 6-of-9 signers distribuidos geográficamente.
- **Tier 2 (5-10%)**: Custodio institucional (Coinbase Prime) para operaciones que requieren servicios off-chain o conversion a fiat.
- **Tier 3 (5-10%)**: Inversiones en DeFi (lending, LPing, staking) para generar yield. Acepta riesgo adicional pero genera retornos.
- **Tier 4 (<5%)**: Hot wallet operativa para gastos diarios pequeños (pagar contractors, fees, etc).

Ejemplo concreto: Una DAO con $50M de tesorería podría tener $40M en Gnosis Safe (30M USDC, 10M ETH), $3M en Coinbase Prime (para facilitar pagos fiat y liquidez), $5M en protocolos DeFi como Aave y Compound (generando 3-5% APY), y $2M en hot wallets para operaciones.

El **proof of reserves** es crítico para evaluar CEXs. Después de FTX, muchos exchanges publicaron proof of reserves: demostraciones criptográficas de que controlan las wallets que dicen controlar. Pero proof of reserves solo muestra assets, no liabilities. Un exchange puede tener $1B en assets pero $2B en liabilities (lo que FTX tenía). El proof of reserves completo debe incluir auditoría de liabilities, lo cual pocos hacen.

Las **cuentas segregadas vs omnibus** son otra distinción crítica. En cuenta segregada, tus assets están separados legalmente y en wallets distintas de assets del exchange. Si el exchange quiebra, tus assets no son parte de la quiebra (en teoría). En cuenta omnibus, tus assets están mezclados con assets del exchange. En quiebra, eres acreedor general y puede que recuperes poco o nada. Coinbase Prime ofrece segregación. La mayoría de exchanges retail no.

La posición más prudente para founders: **asume que cualquier fondo en exchange centralizado puede desaparecer mañana**. Dimensiona tus holdings en CEXs como si fueran de alto riesgo. Si no puedes tolerar perder $X, no dejes $X en un CEX. Usa CEXs solo para lo mínimo necesario para operaciones, mantén el resto en self-custody.

Después de gestión de custodia, el siguiente riesgo es **gestión de keys**. Multisigs requieren que múltiples personas controlen keys privadas. Si 3 de 7 signers pierden sus keys, el multisig puede quedar inutilizable. Las mejores prácticas incluyen:

- **Documentación de signers**: Quién tiene qué key, cómo contactarlos, backup contacts.
- **Hardware wallets para keys**: Ledger, Trezor. Nunca keys en hot wallets o software wallets en computadoras conectadas.
- **Distribución geográfica**: Signers en diferentes países reduce riesgo de que todos sean afectados por mismo evento.
- **Proceso de rotación**: Capacidad de reemplazar signers si alguien se vuelve inactivo o no confiable.
- **Timelock para cambios grandes**: Propuestas de gasto >$X requieren 72h timelock, dando tiempo para detectar compromiso.

Algunos protocolos usan esquemas aún más sofisticados como **Shamir Secret Sharing**, donde la key está dividida en N partes y necesitas M para reconstruirla. O **social recovery** como Argent wallet, donde personas de confianza pueden ayudarte a recuperar acceso. Pero estos agregan complejidad.

La decisión fundamental para tu DAO es: **¿Cuánta descentralización vs. cuánta conveniencia operativa?** Máxima descentralización (todo en multisig, 9-of-12 signers) es más seguro pero lento y friction-full. Más centralización (tesorería en Coinbase Prime con 2-of-3 signers del core team) es conveniente pero riesgoso. El balance correcto depende del tamaño de tesorería, madurez del protocolo, y filosofía de la comunidad.

Protocolos early-stage con <$5M y equipo pequeño a menudo empiezan con 3-of-5 multisig del core team. Protocolos establecidos con >$50M transicionan a gobernanza más descentralizada con 6-of-9 o mayor, incluyendo community members. El anti-pattern es tener todo controlado por 2 personas (riesgo de rugpull o secuestro) o tan distribuido que no puedes ejecutar decisiones operativas.

## Ciclos económicos y timing

Crypto se mueve en ciclos pronunciados, más extremos que mercados tradicionales. Entender estos ciclos es crucial para decisiones de funding, lanzamiento, contratación, y tesorería. El patrón histórico es claro: aproximadamente cada 4 años hay un bull market de 12-18 meses seguido de un bear market de 12-24 meses. Este patrón está parcialmente impulsado por el halving de Bitcoin, pero también por ciclos macroeconómicos más amplios.

### Definiendo bull y bear markets

Técnicamente, un **bull market** se define como aumento sostenido de >20% desde un bottom reciente, acompañado de sentimiento positivo, volumen creciente, y adopción expandiéndose. Un **bear market** se define como caída sostenida de >20% desde un peak reciente, acompañado de sentimiento negativo, volumen decreciente, y capitulación.

Pero en crypto, los umbrales son más extremos. Una caída de 20% puede pasar en una semana y luego recuperar. Los bull markets crypto típicamente ven subidas de 300-1000% desde bottoms. Los bear markets ven caídas de 70-90% desde peaks. La volatilidad hace que los ciclos sean más pronunciados que en mercados tradicionales donde bull/bear de 20% son significativos.

Las **señales tempranas de bull market** incluyen:

1. **Bitcoin dominance bajando**: Cuando BTC domina <40% del market cap total, indica que capital fluye a altcoins (risk-on).
2. **Funding rates positivos sostenidos**: En perpetuals (Binance, Deribit), funding rates positivos significan que más traders están long que short.
3. **Volumen en CEXs subiendo**: Mayor actividad de trading indica FOMO entrando.
4. **Google Trends subiendo**: Búsquedas de "Bitcoin", "cryptocurrency" correlacionan con retail FOMO.
5. **Tasas de interés macro bajando**: Fed bajando tasas envía capital hacia activos riesgosos.
6. **Narrativas emergiendo**: NFTs (2021), DeFi (2020), ICOs (2017). Cada bull tiene su narrativa.

Las **señales tempranas de bear market** incluyen:

1. **Bitcoin dominance subiendo**: Capital huye de altcoins de vuelta a BTC (flight to safety).
2. **Funding rates negativos persistentes**: Más shorts que longs indica expectativa de caídas.
3. **TVL declinando en DeFi**: Capital saliendo de protocolos indica risk-off.
4. **Caídas de proyectos grandes**: Cuando protocolos establecidos empiezan a fallar (Terra, FTX), indica fragilidad sistémica.
5. **Tasas de interés macro subiendo**: Fed subiendo tasas drena liquidez de activos riesgosos.
6. **Falta de nuevas narrativas**: Cuando no hay excitement sobre nuevas tecnologías o aplicaciones.

El bull market de 2021 fue espectacular. Bitcoin llegó a $69K. ETH llegó a $4.8K. Capitalización total de crypto superó $3 trillones. Cientos de protocolos lanzaron con valoraciones astronómicas. Los TVLs explotaron. Las tesorerías de DAOs tenían cientos de millones o miles de millones en papel. Parecía que esto era el nuevo normal. No lo era.

El bear market de 2022 fue brutal. Bitcoin cayó a $16K (-77% del pico). ETH cayó a $900 (-81% del pico). Capitalización total cayó bajo $800B (-73%). Los TVLs colapsaron. Las tesorerías en tokens nativos se evaporaron. Proyectos que parecían imparables quebraron. Terra/Luna, que tenía $40B en market cap, colapsó a cero en días. Celcius, Voyager, BlockFi, y otros prestamistas centralizados quebraron. Tres Arrows Capital, un hedge fund masivo, colapsó arrastrando múltiples protocolos.

### Timing y estrategia según fase del ciclo

La fase del ciclo debe influenciar profundamente tus decisiones:

**En bull market:**

- **Fundraising**: Más fácil, valoraciones altas, pero también expectativas infladas. Si levantas a $1B valuation, necesitas justificarlo con ejecución masiva.
- **Token launch**: Puedes obtener valoración inicial alta, pero prepárate para caída 70-90% en próximo bear. Asegúrate de que tu tokenómica funcione a precios 10x menores.
- **Tesorería**: **CRÍTICO - Convierte tokens nativos a stablecoins agresivamente**. Si tu tesorería es $100M en tu token a $50, y cae a $5, ahora tienes $10M. Vende 50-70% a stablecoins durante el bull.
- **Hiring**: Más caro, más competencia por talento. Considera si realmente necesitas ese headcount o puedes esperar.
- **Emissions**: Puedes reducir APYs de incentivos porque usuarios vienen por apreciación del token. No necesitas pagar 100% APY cuando el token está subiendo 500%.

**En bear market:**

- **Fundraising**: Más difícil, valoraciones comprimidas, pero inversores más comprometidos. Los que invierten en bear creen en largo plazo.
- **Token launch**: Valoración inicial baja pero más espacio para sorpresa positiva. Usuarios que llegan en bear son más leales (no turistas).
- **Tesorería**: Si tienes stablecoins, puedes comprar assets (tokens, NFTs, partnerships) a descuento masivo. Es momento de acumular.
- **Hiring**: Talento más disponible y más barato. Developers que trabajaban en proyectos que murieron están buscando. Puedes construir equipo fuerte económicamente.
- **Emissions**: Puede que necesites mantener incentivos más altos porque no hay apreciación de precio para atraer usuarios. Pero también puedes filtrar mercenarios: solo los comprometidos quedan.

**En fase de transición (bottom o top):**

- **Bottom a bull**: Momento óptimo para lanzar. Puedes atraer usuarios early con valoraciones razonables, y surfear la ola cuando llega el bull.
- **Top a bear**: Momento de preservación. Convierte assets a stablecoins, reduce headcount a sostenible, prepara para 18-24 meses de inverno.

### El rol de macroeconomía

Los ciclos crypto no existen en vacío. Están profundamente ligados a política monetaria global, especialmente de la Reserva Federal (Fed) de Estados Unidos. La relación es directa:

- **Fed baja tasas + imprime dinero (QE)**: Liquidez fluye a activos riesgosos → crypto sube.
- **Fed sube tasas + retira liquidez (QT)**: Liquidez se drena → crypto cae.

El bull market 2020-2021 fue impulsado por tasas de interés en ~0% y $5 trillones en estímulo COVID. El bear market 2022 fue causado por la Fed subiendo tasas de 0% a 5.25% en 18 meses, el hiking más agresivo en 40 años. Esto drenó liquidez de todos los activos riesgosos, incluyendo tech stocks y crypto.

Los builders deben seguir indicadores macro:

- **Tasa de Fed Funds**: Tasa de interés base de Estados Unidos. <2% es favorable para crypto. >4% es desfavorable.
- **Balance sheet de Fed**: Cuando crece (QE), crypto sube. Cuando se contrae (QT), crypto cae.
- **Inflación (CPI)**: Alta inflación causa que Fed suba tasas (malo para crypto). Inflación controlada permite tasas bajas (bueno).
- **Curva de yield (2yr vs 10yr treasuries)**: Invertida indica recesión entrante (malo). Normal indica crecimiento (bueno).

Ejemplo práctico: En marzo 2023, la Fed pausó rate hikes después de la crisis bancaria (Silicon Valley Bank). Crypto rally inmediatamente, con Bitcoin subiendo 40% en semanas. Los traders anticiparon que la Fed podría empezar a bajar tasas pronto. Este es el tipo de señal macro que debes seguir.

### Timing de lanzamiento de token

La pregunta que todos los founders hacen: **¿Cuándo lanzar mi token?** La respuesta corta: **el timing importa menos de lo que piensas, la ejecución importa más**. Uniswap lanzó UNI en septiembre 2020 (pre-bull). Curve lanzó CRV en agosto 2020 (pre-bull). Optimism lanzó OP en mayo 2022 (inicio de bear). Todos son exitosos porque construyeron productos con PMF real.

La respuesta larga:

- **Si lanzas en bull**: Aprovecharás la atención y podrás obtener valoración alta. Pero estarás compitiendo con cientos de otros lanzamientos. Y cuando el bear llegue (y llegará), tu token puede caer 90%. Asegúrate de que tu utilidad sobrevive esa caída.

- **Si lanzas en bear**: Obtendrás menos atención inicial y valoración más baja. Pero los usuarios que llegan son más serios. Y cuando el bull llegue, tienes más espacio para sorprender positivamente. Muchos protocolos que dominaron el bull 2021 (GMX, Lido) lanzaron o crecieron durante el bear 2018-2020.

El anti-pattern es lanzar en el **pico absoluto** del bull, pensando que seguirá subiendo. Los proyectos que lanzaron noviembre-diciembre 2021 (pico) están casi todos down 95%+. Sus valoraciones iniciales fueron insostenibles y nunca las recuperarán.

La estrategia correcta es: **lanza cuando tu producto tenga PMF y tokenómica diseñada para ciclos completos, independientemente de la fase del mercado**. Si cumples esos dos requisitos, puedes tener éxito en cualquier fase. Si no los cumples, fallarás en cualquier fase.

## Valoración de protocolos y tokens

Valorar protocolos y tokens Web3 es parte ciencia, parte arte. No hay un método universalmente aceptado como en equity tradicional. Pero hay frameworks que proporcionan rangos razonables. El método más directo es valoración por flujos de caja descontados, aplicable a tokens que generan cash flows.

Si un token distribuye fees a holders (como GMX), puedes proyectar esos fees futuros y descontarlos al presente. GMX generó aproximadamente $90M en fees en 2022. Si asumes crecimiento moderado y aplicás una tasa de descuento del 15%, el valor presente de esos flujos perpetuos es alrededor de $600M. El market cap actual de GMX nos dice si está sobre o sub-valorado vs. ese modelo.

El desafío es que la mayoría de tokens no distribuyen cash flows directamente. UNI, AAVE, CRV, y muchos otros no dan dividendos. Su valor viene de gobernanza, utilidad dentro del protocolo, o especulación sobre captura de valor futura. ¿Cómo los valoras? Una opción es valorar el protocolo subyacente y asumir que el token eventualmente capturará parte de ese valor.

Puedes valorar protocolos por múltiplos de sus métricas fundamentales. En tech tradicional, usas P/E (price/earnings), P/S (price/sales), EV/EBITDA. En Web3, los equivalentes son Market Cap / Protocol Revenue, Market Cap / TVL, o Market Cap / Active Users. Si el promedio de la industria es 10x revenue y tu protocolo genera $10M, una valoración razonable podría ser $100M.

El problema con múltiplos es que varían enormemente. En 2021 bull market, algunos protocolos cotizaban a 50-100x revenue. En 2022 bear market, cotizaban a 3-5x revenue. El múltiplo "correcto" depende de expectativas de crecimiento, márgenes, competencia, y sentimiento general. No es ciencia exacta.

Otra aproximación es valorar por TVL (Total Value Locked), especialmente en protocolos DeFi. El argumento es que mayor TVL indica mayor network effect y eventual captura de valor. Un protocolo con $1B TVL probablemente vale más que uno con $10M TVL. Pero el ratio Market Cap / TVL varía. Algunos protocolos cotizaban a 0.1x TVL (muy barato), otros a 2x TVL (caro).

La valoración por FDV (Fully Diluted Valuation) considera todo el supply futuro de tokens. Si un protocolo tiene 100M tokens circulantes a $10 cada uno ($1B market cap), pero eventualmente habrá 1B tokens, el FDV es $10B. Esta métrica expone protocolos sobrevalorados que tienen la mayoría de su supply aún por desbloquear. Cuando ese supply entre al mercado, la dilución colapsará el precio.

Las valoraciones en Web3 también deben considerar intangibles: fortaleza de la comunidad, reputación del equipo, posicionamiento estratégico, partnerships, moats tecnológicos. Un protocolo con liquidez profunda y efectos de red fuertes (como Uniswap) puede justificar valoración premium vs. competidores técnicamente similares. Un protocolo con equipo anónimo y sin audits justifica descuento por riesgo.

Un método práctico es comparación con competidores (comps). Si estás valorando un lending protocol, miras Aave, Compound, Euler. Calculas sus ratios (Market Cap / TVL, Market Cap / Revenue, etc). Aplicas rangos similares a tu protocolo ajustando por tamaño, crecimiento, y riesgo. Es imperfecto pero te da un benchmark.

Finalmente, la valoración última viene del mercado. Los tokens valen lo que alguien está dispuesto a pagar, influenciado por oferta, demanda, sentimiento, y especulación. Puedes hacer todos los modelos que quieras, pero si el mercado decide que tu token vale $X, esa es su valoración real. Tu trabajo es entender si esa valoración es sostenible o una burbuja/descuento temporal.

## Financiación para proyectos Web3

Los proyectos Web3 tienen opciones de financiación únicas comparado con startups tradicionales. Además de equity tradicional de VCs, puedes hacer token sales públicos, grants de foundations, airdrops retro-activos, Protocol-Owned Liquidity bonding, y más. Cada método tiene trade-offs en dilución, descentralización, compliance, y velocidad.

El equity tradicional sigue siendo común, especialmente para proyectos early-stage. Levantas capital de VCs vendiendo porcentaje de tokens futuros o, si aún no hay token, equity tradicional en una entidad legal. Los fondos más grandes en crypto (a16z, Paradigm, Pantera, Coinbase Ventures) invierten cientos de millones. Las rondas típicas van desde $2-5M en seed hasta $20-100M en Series A/B para proyectos prometedores.

El problema con equity tradicional es que no es nativo a Web3. Vendes tokens o derechos sobre tokens a VCs a precios con descuento, prometiendo unlocks en X años. Esto crea misalignment porque los VCs quieren liquidez (desbloquear y vender) mientras la comunidad quiere que holdeen largo plazo. Además, grandes allocations a VCs centralizan poder de gobernanza.

Los token sales públicos (ICOs, IEOs, IDOs) permiten levantar directamente de la comunidad. Un ICO (Initial Coin Offering) vende tokens a público general, usualmente en fases con precios crecientes. Un IEO (Initial Exchange Offering) usa un exchange (como Binance Launchpad) que da credibilidad y acceso a usuarios. Un IDO (Initial DEX Offering) lanza inmediatamente en un DEX con liquidez.

Los sales públicos tienen ventajas: distribución amplia, menos dilución a VCs, y potencial viral. Pero tienen desafíos: regulaciones (muchos países consideran ICOs como securities), riesgo de dump inmediato si no hay vesting, y posible fracaso si el mercado no tiene demanda. Los ICOs fueron enormes en 2017-2018, colapsaron después de regulaciones, y han sido parcialmente reemplazados por métodos alternativos.

Los grants de foundations son financiación no-dilutiva. Ethereum Foundation, Optimism, Arbitrum, Polygon, y otros dan grants a proyectos construyendo en sus ecosistemas. Los montos van desde $10K para proyectos pequeños hasta $1M+ para infraestructura crítica. Es capital gratis sin vender equity ni tokens, pero competitivo y usualmente insuficiente para financiar una company completa.

Los airdrops retro-activos (como Uniswap, dYdX, Optimism) recompensan usuarios que usaron el protocolo antes del lanzamiento del token. No levantas capital directamente, pero distribuyes tokens ampliamente creando comunidad alineada. Si hiciste un airdrop bien, miles de usuarios ya están usando tu producto cuando lanzas token, dándote legitimidad y liquidez inmediata.

El Protocol-Owned Liquidity via bonding (modelo Olympus) te permite levantar liquidez sin vender tokens a precio fijo. Ofreces tokens con descuento a cambio de LP tokens o stablecoins. El comprador obtiene ganancia del descuento. Tú obtienes activos que controlas para siempre. Es una forma de financiación continua que crece con demanda: si más gente quiere bondear, levantas más.

Cada método tiene casos de uso óptimos. Para infraestructura early-stage sin producto, equity de VCs. Para protocolos con producto-market fit lanzando token, combinación de equity, grants, y distribución comunitaria via airdrop o fair launch. Para protocolos establecidos necesitando liquidez permanente, bonding. Para proyectos que quieren máxima descentralización desde día 1, fair launch sin preventa.

La decisión crucial es cuánto diluir a la comunidad vs. fundadores vs. inversores. Una distribución común es: 40-50% comunidad (emissions, airdrops, liquidity mining), 20-30% equipo/fundadores (con vesting de 3-4 años), 15-25% inversores (con vesting más corto), y 10-15% tesorería del protocolo. Protocolos que dan demasiado a fundadores/inversores (~60%+) suelen tener pushback de la comunidad.

## Métricas de protocolos Web3

Más allá de métricas empresariales tradicionales, los protocolos Web3 tienen métricas específicas que indican salud y adopción. Estas métricas son públicas on-chain, haciendo el análisis transparente pero también competitivo. Todos pueden ver todas las métricas de todos los protocolos en tiempo real.

TVL (Total Value Locked) es la métrica más citada en DeFi. Mide cuánto valor está depositado en el protocolo. Un lending protocol cuenta todos los depósitos. Un DEX cuenta liquidez en pools. Un staking protocol cuenta assets stakeados. Mayor TVL indica mayor confianza y utilidad. Pero TVL puede ser inflado con incentivos insostenibles o manipulado con capital propio.

El TVL debe contextualizarse con TVL/Employee (eficiencia del equipo) y Market Cap/TVL (valoración vs. uso real). Un protocolo con $1B TVL y 5 empleados es increíblemente eficiente. Un protocolo con $1B TVL y market cap de $10B está sobrevalorado (10x ratio). Un protocolo con $1B TVL y market cap de $100M está subvalorado (0.1x ratio).

Daily Active Users (DAU) y Monthly Active Users (MAU) miden cuántas wallets únicas interactúan con tu protocolo. En DeFi, DAUs suelen ser bajos (miles a decenas de miles) porque las transacciones son menos frecuentes que en web2. Un protocolo con 50K DAU es considerable. 500K DAU sería masivo. La tendencia importa más que el número absoluto: ¿estás creciendo o declinando?

Transaction Count mide cuántas transacciones ocurren. Un DEX puede tener millones de swaps diarios. Un lending protocol puede tener decenas de miles de borrows/repays. Más transacciones generan más fees, lo cual es positivo. Pero transacciones también pueden ser bots o wash trading, así que debes filtrar actividad orgánica vs. artificial.

Volume (volumen) es crucial para DEXs. Uniswap procesa $1-3B en volumen diario en bull markets, menos en bear markets. Mayor volumen genera más fees para el protocolo y LPs. El ratio Volume/Liquidity indica eficiencia de capital. Si tienes $1B liquidity generando $100M volumen diario, tu capital se usa 0.1x por día. Si generas $1B volumen, tu capital se usa 1x por día (mucho más eficiente).

Protocol Revenue es el ingreso bruto que genera el protocolo de fees. Esto es antes de distribuir a LPs, stakers, u otros stakeholders. Protocol Revenue muestra la demanda real por el servicio. Un protocolo generando $100M anuales en revenue claramente tiene product-market fit. Uno generando $1M tiene uso menor.

Fees to Token Holders es la porción de fees que va a holders del token de gobernanza. Muchos protocolos no distribuyen fees a token holders (aún), pero es la métrica más importante para valoración. Si GMX genera $100M en fees y distribuye $70M a GMX stakers, esos $70M justifican el market cap del token. Si UNI genera $500M en fees pero distribuye $0 a holders, UNI captura valor $0 directamente (solo via gobernanza).

El P/F Ratio (Price-to-Fees) es el equivalente de P/E en tokens. Si un token tiene $100M market cap y genera $20M fees anuales a holders, su P/F es 5x. Comparado con P/E de tech stocks (20-40x), DeFi tokens cotizando a 5-10x P/F están baratos si asumes similar estabilidad. Pero DeFi es más riesgoso y volátil, justificando múltiplos menores.

Staking Ratio mide qué porcentaje del supply está stakeado. Ethereum tiene ~15% de ETH stakeado. Si tu governance token tiene 60% stakeado, indica compromiso alto y presión vendedora baja. Si solo 5% está stakeado, indica falta de interés o incentivos insuficientes. Alto staking reduce supply circulante efectivo, lo cual puede aumentar precio.

Holder Distribution mide concentración. Si el top 10 wallets controla 80% del supply, hay riesgo de centralización y manipulación. Si el top 100 controla 40% y hay miles de holders medianos, la distribución es saludable. Protocolos transparentes publican dashboards mostrando distribución. Los mejores tienen curvas de distribución relativamente planas sin whales dominantes.

## Aplicando todo: diseño de tokenómica sostenible

Ahora integremos todos estos conceptos en un framework para diseñar tokenómica sostenible. Tu token debe cumplir funciones claras, capturar valor de actividad productiva, alinear incentivos de stakeholders, y ser sostenible en bear markets. No hay fórmula mágica, pero hay principios que aumentan probabilidad de éxito.

Primero, define la función del token. ¿Es governance puro? ¿Utility para pagar fees? ¿Stake para asegurar el protocolo? ¿Dividendos de fees? ¿Combinación? Cada función tiene implicaciones diferentes. Un token de governance puro sin cash flows se valorará por poder de decisión y potencial futuro. Un token que distribuye fees se valorará por cash flows reales. Sé explícito qué es y qué no es tu token.

Segundo, diseña captura de valor. Si tu protocolo genera fees, ¿cómo captura valor el token? Opciones: distribución directa de fees a stakers (GMX), burning de tokens con fees (MKR), vote-escrow con boosts y fees (CRV), o simplemente governance con potencial de activar fee switch futuro (UNI). La opción más clara para inversores es distribución directa, pero no siempre es óptima para growth.

Tercero, diseña el supply schedule. ¿Cuántos tokens existen? ¿Cómo se emiten? ¿A quién van? Una estructura típica podría ser: 1B tokens totales, 100M iniciales circulantes (10%), resto vestea en 4 años entre equipo (20%), inversores (15%), tesorería (15%), liquidity mining (20%), airdrops y community (20%). Los porcentajes varían, pero el principio es balancear entre stakeholders.

El vesting schedule debe alinear incentivos. Equipo e inversores deberían vestear al menos 3-4 años, idealmente con cliff de 1 año (nada el primer año, luego desviste gradualmente). Esto asegura commitment largo plazo. Community emissions deberían ser decrecientes: altas inicialmente para bootstrapping, reduciéndose con tiempo para sostenibilidad.

Cuarto, diseña mecanismos anti-dilución. Si emites tokens como incentivos, necesitas sinks (sumideros) que remuevan tokens de circulación. Opciones: burning de fees, lockup requirements para utilidad, staking con penalidades de early exit, o buybacks del protocolo. El objetivo es que la oferta neta crezca más lento que la demanda, creando presión alcista.

Quinto, diseña alineación de incentivos. Usa teoría de juegos: ¿qué comportamiento quieres incentivar? Si quieres commitment largo plazo, usa vote-escrow (lockup largo = más poder/rewards). Si quieres liquidez profunda, usa POL bonding. Si quieres participación en gobernanza, da rewards a votantes activos. Si quieres reducir sell pressure, da rewards en vesting gradual, no instant.

Sexto, modela escenarios adversos. Asume que el precio del token cae 80%. ¿Tu protocolo sigue funcionando? ¿Tu tesorería tiene runway? ¿Los incentivos aún atraen usuarios? Si todo colapsa cuando el precio baja, tu tokenómica no es sostenible. Los mejores protocolos tienen utility que funciona independiente del precio del token, aunque el precio afecta crecimiento.

Séptimo, planea para ciclos completos. Si lanzas en bull market, asume que vendrá bear market. Convierte parte de tesorería a stablecoins. Dimensiona equipo sosteniblemente. No prometas emissions que solo funcionan con precio actual. Si lanzas en bear market, planea para que tu tokenómica brille cuando llegue el bull. Ten utilidad real que justifique valoración creciente.

Octavo, prioriza distribución justa. La comunidad crypto valora descentralización y fairness. Si das 70% del supply a fundadores e inversores y solo 30% a comunidad, enfrentarás resistencia. Las distribuciones respetadas dan mayoría (50-70%) a la comunidad via emissions, airdrops, y tesorería controlada por gobernanza. Esto construye legitimidad.

Noveno, sé transparente. Publica tu tokenómica completa: supply total, distribución, vesting schedules, addressees de wallets de equipo/tesorería. La transparencia construye confianza. Los proyectos que ocultan información generan sospecha, especialmente en un ecosistema donde todo es verificable on-chain. Si alguien puede descubrirlo, mejor que lo publiques tú primero.

Décimo, itera basándose en datos. Lanza, mide, ajusta. Las mejores tokenómicas evolucionan con feedback de la comunidad y datos reales. Si tus emissions son muy altas y el precio está colapsando, propón reducirlas via gobernanza. Si el staking es muy bajo, aumenta rewards. Si la distribución se concentró demasiado, haz un segundo airdrop. No asumas que el diseño inicial es perfecto.

---

Web3 no elimina la necesidad de entender economía, la amplifica. Cada decisión de diseño de protocolo tiene consecuencias económicas que se desarrollan públicamente, en tiempo real, on-chain. Los fundamentos económicos - oferta y demanda, incentivos, valoración, gestión de riesgos - no son opcionales. Son las bases sobre las cuales construimos sistemas descentralizados que deben funcionar sin coordinación central.

Este documento te ha dado un framework para pensar económicamente sobre proyectos Web3. Ahora sal y aplícalo. Analiza protocolos existentes con estas lentes: ¿su tokenómica respeta oferta y demanda? ¿sus incentivos alinean stakeholders? ¿capturan valor sosteniblemente? Y cuando diseñes tu propio protocolo, usa estos principios no como restricciones sino como herramientas que aumentan probabilidad de construir algo duradero.

La economía no es el enemigo de la innovación. Es el lenguaje en que se expresa valor, coordinación, y sostenibilidad. Domínala.

---
