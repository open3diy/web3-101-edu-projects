# Taxonomía de activos digitales

El ecosistema de activos digitales se ha expandido enormemente desde la creación de Bitcoin, generando una diversidad de tokens y criptomonedas con características y propósitos muy distintos. Comprender esta taxonomía resulta fundamental para navegar el espacio cripto de forma informada y tomar decisiones acertadas, ya sea como usuario, inversor o desarrollador.

Antes de explorar las distintas clasificaciones, conviene establecer con precisión qué entendemos por activo digital, criptomoneda y token, términos que a menudo se usan de forma intercambiable pero que poseen matices importantes tanto técnicos como regulatorios y culturales.

**Un activo digital**:

Constituye el término más amplio de los tres. Desde una perspectiva técnica, se trata de cualquier información representada en formato digital que posee valor y puede ser poseída, transferida o intercambiada. Esto incluye desde criptomonedas hasta NFTs, pasando por representaciones tokenizadas de activos tradicionales, derechos digitales, identidades verificables y cualquier otra forma de valor almacenado criptográficamente en redes descentralizadas.

El término activo digital se ha consolidado como la denominación formal y profesional preferida en contextos institucionales, financieros y regulatorios, precisamente por su neutralidad y amplitud.

**Criptomoneda**:

Representa un subtipo específico de activo digital diseñado principalmente como medio de intercambio, unidad de cuenta o reserva de valor. Técnicamente, una criptomoneda opera sobre su propia blockchain nativa con su propio protocolo de consenso, libro mayor distribuido y mecanismos criptográficos de validación. Bitcoin, Litecoin o Ethereum ejemplifican perfectamente este concepto, cada una con su propia red independiente. La distinción técnica fundamental radica en que las criptomonedas poseen soberanía tecnológica completa, no dependen de otra infraestructura blockchain para existir y fueron concebidas específicamente para funcionar como sistemas monetarios descentralizados.

Culturalmente, el término criptomoneda evoca la visión original del movimiento cypherpunk: dinero resistente a la censura, transferible sin intermediarios y fuera del control de autoridades centrales.

**Token**:

En contraste, representan activos digitales creados sobre blockchains existentes utilizando estándares de tokenización predefinidos. Técnicamente, un token no posee blockchain propia sino que hereda la seguridad, el consenso y la infraestructura de la red que lo aloja. Los tokens ERC-20 sobre Ethereum, por ejemplo, son contratos inteligentes que siguen un estándar específico de funciones y eventos, permitiendo su creación sin necesidad de desarrollar toda una blockchain desde cero. Esta dependencia técnica constituye la diferencia esencial: mientras una criptomoneda es la moneda nativa de su propia red, un token existe gracias a otra blockchain.

Culturalmente, el término token se asocia con la era de las ICOs y la explosión de proyectos descentralizados que aprovecharon la infraestructura de Ethereum para crear nuevos ecosistemas económicos sin las barreras técnicas de lanzar blockchains completas.

La distinción práctica entre estos conceptos resulta crucial. Cuando alguien dice que Bitcoin es una criptomoneda, está afirmando que posee su propia blockchain y protocolo. Cuando menciona que USDC es un token, reconoce que este stablecoin existe como contrato inteligente sobre Ethereum y otras blockchains compatibles. Y cuando habla de activos digitales en general, abarca todo el espectro: desde criptomonedas nativas hasta tokens de cualquier tipo, NFTs, representaciones de activos reales y cualquier otro valor digital descentralizado. Esta precisión terminológica no es mera pedantería académica, sino que tiene implicaciones legales, técnicas y estratégicas concretas para desarrolladores, inversores y reguladores.

## El proceso de tokenización

La tokenización es el mecanismo que convierte cualquier forma de valor, ya sea un activo del mundo real, un derecho, una identidad o una función dentro de un protocolo, en una representación digital que puede existir, transferirse y verificarse sobre una blockchain. Comprender este proceso es esencial porque es precisamente la variedad de cosas que pueden tokenizarse, y cómo se tokenizan, lo que da origen a toda la taxonomía de activos digitales.

El proceso parte de una pregunta simple: ¿qué se quiere representar? Un proyecto puede querer tokenizar euros para crear una stablecoin, acciones de una empresa para emitir un security token, el derecho a usar un servicio para crear un utility token, o incluso un obra de arte única para crear un NFT. Cada respuesta conduce a decisiones técnicas distintas sobre cómo construir ese token.

Técnicamente, la tokenización se implementa mediante contratos inteligentes que definen las reglas del activo: quién puede poseerlo, cómo se transfiere, cuántos existen y qué derechos confiere. Para que estos contratos sean interoperables entre sí y con los exchanges, wallets y protocolos del ecosistema, la comunidad ha desarrollado estándares que formalizan la interfaz mínima que todo token debe cumplir. Ethereum fue el primer ecosistema en sistematizar estos estándares a través de los EIP (Ethereum Improvement Proposals), entre los que destacan ERC-20 para tokens fungibles, ERC-721 para tokens no fungibles y ERC-1155 para contratos que gestionan múltiples tipos de tokens simultáneamente. Estos estándares se describen formalmente en la [documentación de Ethereum sobre tokens](https://ethereum.org/es/developers/docs/standards/tokens/).

Una distinción fundamental que emerge del proceso de tokenización es la de fungibilidad. Un token es fungible cuando cada unidad es idéntica e intercambiable con cualquier otra unidad del mismo token: un USDC siempre vale lo mismo que otro USDC. En cambio, un token no fungible (NFT) es único e irrepetible, representando un activo específico que no puede intercambiarse por otro de la misma clase sin que el poseedor pierda algo particular. Esta diferencia no es solo conceptual: determina el estándar técnico que se usa, la semántica de propiedad, el mecanismo de transferencia y, en última instancia, el tipo de valor que el token puede representar.

La tokenización también introduce la cuestión del respaldo o colateral. Algunos tokens representan activos que existen de forma independiente fuera de la blockchain, como dólares en una cuenta bancaria o un inmueble inscrito en un registro. En estos casos, la tokenización crea un vínculo entre el mundo on-chain y el mundo off-chain que requiere mecanismos de confianza adicionales: auditorías, reservas verificables o garantías legales que aseguren que el token realmente corresponde al activo que dice representar. Este vínculo no es automático ni trivial: la blockchain por sí sola no puede abrir una bóveda bancaria, verificar que un inmueble existe ni confirmar que una factura fue pagada. Necesita fuentes externas de información y marcos legales que conecten ambos mundos, un problema con soluciones específicas que se exploran en detalle en [Los desafíos de la integración off-chain](4-4-challenges-off-chain-integration.md). Otros tokens, en cambio, son nativos de la blockchain, sin representación en el mundo físico, y su valor surge únicamente de la utilidad o los derechos que el propio protocolo les otorga.

Entender la tokenización como proceso previo a la clasificación permite comprender por qué la taxonomía de activos digitales no es arbitraria. Las distintas categorías de tokens no son etiquetas de marketing sino que reflejan diferencias fundamentales en qué se ha tokenizado, con qué mecanismo técnico, bajo qué condiciones de respaldo y con qué derechos se han programado en el contrato. Es precisamente esta diversidad de posibilidades lo que hace que clasificar tokens resulte complejo y, al mismo tiempo, necesario.

## Clasificación histórica y cultural

Desde una perspectiva histórica, la comunidad cripto suele dividir las criptomonedas entre Bitcoin y altcoins. Bitcoin, como pionero y referencia del mercado, mantiene un estatus único. Todas las demás criptomonedas, sin importar su utilidad o capitalización, se consideran altcoins o monedas alternativas.

Dentro de las altcoins existe un fenómeno particular: las memecoins. Estas criptomonedas nacen generalmente como proyectos humorísticos o especulativos, sin una propuesta de valor tecnológico sólida, aunque algunas han conseguido comunidades amplias y valoraciones significativas. En el extremo negativo de este espectro encontramos las shitcoins, término despectivo para proyectos sin fundamento real, muchas veces esquemas fraudulentos o scams diseñados únicamente para enriquecer a sus creadores.

## Clasificación regulatoria y normativa

La regulación de activos digitales ha evolucionado para adaptarse a la complejidad y diversidad de estos instrumentos, creando marcos específicos que intentan equilibrar innovación con protección al inversor. Europa y Estados Unidos han desarrollado enfoques diferentes pero complementarios para clasificar y regular estos activos.

**Utility token**:

En el contexto europeo, el Reglamento MiCA define con precisión qué constituye un utility token. Bajo esta normativa, un utility token es aquel criptoactivo que proporciona acceso digital a un bien o servicio disponible en una plataforma de tecnología de registro distribuido, y que solo es aceptado por el emisor de dicho token. Esta definición técnica establece límites claros:

- El token debe tener una función práctica específica dentro de un ecosistema
- No puede ser transferible más allá de ese contexto original sin perder su naturaleza de utility.
- Su valor deriva de la utilidad que proporciona, no de expectativas especulativas de apreciación.

MiCA establece para estos tokens requisitos de transparencia mediante white papers obligatorios, revelación de información sobre el proyecto y sus desarrolladores, y mecanismos de protección al consumidor, aunque con cargas regulatorias significativamente menores que los valores mobiliarios tradicionales.

**Security tokens**:

Los security tokens representan instrumentos financieros en el sentido tradicional del término, pero emitidos, registrados y gestionados mediante tecnología blockchain. Cuando un token otorga derechos de propiedad, participación en beneficios, derechos de voto corporativos o cualquier característica típica de acciones, bonos o instrumentos financieros, se clasifica como security token y queda sujeto a regulación financiera estricta.

**Marco regulatorio europeo**:

En Europa, los security tokens caen bajo el ámbito de MiFID II (Directiva sobre Mercados de Instrumentos Financieros), que regula valores negociables, instrumentos del mercado monetario y otros productos financieros complejos. Es importante destacar que el Reglamento MiCA, aunque regula criptoactivos, **excluye expresamente a los security tokens** de su ámbito de aplicación, manteniéndolos bajo la legislación de valores tradicional.

**Regulación específica en España**:

En España, aunque no existe una ley específica para tokens, la naturaleza jurídica de cada token determina su tratamiento legal. Si un token cumple las características de valor negociable según la Ley del Mercado de Valores (LMV) y MiFID II, está sujeto a supervisión de la [CNMV](https://www.cnmv.es/) (Comisión Nacional del Mercado de Valores). La normativa aplicable incluye:

- **Ley del Mercado de Valores (LMV)**: Marco principal para valores mobiliarios
- **Reglamento (UE) 2017/1129 sobre folletos**: Requisitos de documentación para ofertas públicas
- **MiFID II**: Normativa de servicios de inversión y protección al inversor
- **DLT Pilot Regime (Reglamento UE 2022/858)**: Sandbox regulatorio europeo para mercados tokenizados experimentales

**Criterios de identificación**:

Un token se considera security token en España si cumple estas características:

- Representa un **derecho económico** (dividendos, intereses, revalorización)
- Es **transferible y negociable** en mercados secundarios
- Se ofrece como **inversión con expectativa de beneficio** derivado principalmente de esfuerzos de terceros

Cláusula clave de la CNMV: si un token cumple la definición de "valor negociable" según LMV y MiFID II, debe cumplir requisitos legales aplicables a valores tradicionales.

**Test de Howey en Estados Unidos**:

Estados Unidos aplica el test de Howey, establecido por la Corte Suprema en 1946, para determinar si un activo constituye un contrato de inversión (security). Según este test, existe un security cuando hay una inversión de dinero en una empresa común con expectativa de beneficios derivados principalmente de los esfuerzos de terceros. Este criterio ha generado considerable fricción en el espacio cripto, ya que muchos tokens que se presentaban como utilities han sido considerados securities por la SEC (Comisión de Valores estadounidense), generando litigios importantes contra proyectos como Ripple o Telegram.

**Requisitos para emisión en España**:

Emitir un security token en España implica cumplir requisitos estrictos:

1. **Estructura legal del emisor**: La emisión debe realizarse a través de entidad jurídica con capacidad legal para emitir valores (S.L., S.A., fondo, SPV, etc.)

2. **Documentación informativa**:
   - **Ofertas públicas**: Folleto aprobado por la CNMV según Reglamento 2017/1129
   - **Emisiones privadas o limitadas**: Puede aplicarse exención, pero requiere documentación adecuada

3. **Registro y custodia**: Aunque el token se registre en blockchain, puede requerirse proveedor de servicios de custodia, registro contable o representación legal según el tipo de activo

4. **Cumplimiento normativo**:
   - Políticas de **KYC/AML** (Know Your Customer / Anti-Money Laundering)
   - Transparencia y protección al inversor
   - Gobernanza clara y trazable mediante smart contracts auditables

**Mercados secundarios y negociación**:

Actualmente, no existen mercados secundarios plenamente regulados para security tokens abiertos al público retail en España. Sin embargo:

- Existen **plataformas de negociación privadas** bajo el DLT Pilot Regime
- Se están desarrollando **infraestructuras reguladas** de custodia, compensación y liquidación
- Algunas empresas están solicitando autorización como **SSMN** (Sistemas Multilaterales de Negociación) tokenizados
- Es posible negociar mediante **smart contracts con control de acceso** y KYC verificado on-chain

**Beneficios de emisión regulada**:

Emitir security tokens bajo supervisión de la CNMV ofrece ventajas:

- **Acceso a inversores institucionales**: Cumplimiento legal fortalece confianza y reputación
- **Reducción de costes operativos**: Menos intermediarios tradicionales, automatización mediante contratos inteligentes
- **Liquidez potencial**: Aunque incipiente, los mercados secundarios tokenizados están en desarrollo activo
- **Eficiencia de liquidación**: Transacciones on-chain reducen tiempos de settlement de días a minutos
- **Divisibilidad fraccionaria**: Permite inversiones mínimas mucho menores que valores tradicionales

**Equity tokens**:

Los equity tokens representan una subcategoría específica de security tokens que funcionan como acciones digitales. En la práctica regulatoria europea, estos tokens deben cumplir con todos los requisitos aplicables a valores mobiliarios tradicionales: registro ante autoridades competentes, elaboración de prospectos de emisión detallados, cumplimiento de normativas de prevención de blanqueo de capitales, y sometimiento a reglas estrictas de comercialización y custodia.

La ventaja promovida por los defensores de equity tokens radica en la eficiencia de liquidación, la divisibilidad extrema que permite inversiones fraccionarias, y la posibilidad de programar dividendos y derechos de voto directamente en el código del contrato inteligente. Sin embargo, la realidad regulatoria ha demostrado ser más compleja, ya que la tokenización no elimina las responsabilidades legales ni las cargas de cumplimiento normativo.

**Debt tokens**:

Los debt tokens constituyen la otra subcategoría principal de security tokens, representando instrumentos de deuda tradicionales tokenizados mediante blockchain. Al igual que los bonos corporativos o gubernamentales en mercados tradicionales, estos tokens otorgan al poseedor un derecho de crédito sobre el emisor, quien se compromete a devolver el principal más intereses según condiciones predefinidas.

Desde una perspectiva regulatoria, los debt tokens se clasifican como valores mobiliarios bajo MiFID II en Europa y como securities bajo la normativa de la SEC en Estados Unidos, sometiéndose a los mismos marcos legales que los bonos tradicionales. La emisión de debt tokens requiere cumplir con requisitos de registro, divulgación de información financiera del emisor, calificaciones crediticias cuando corresponda, y protocolos estrictos de protección al inversor. En España, la CNMV supervisa estos instrumentos bajo la Ley del Mercado de Valores, exigiendo folletos informativos que detallen términos del préstamo, perfil de riesgo del emisor, garantías o colaterales cuando existan, y condiciones de reembolso.

La tokenización de deuda ofrece ventajas técnicas significativas respecto a bonos tradicionales. Los contratos inteligentes pueden automatizar pagos de cupones mediante transferencias programadas on-chain, eliminar intermediarios en la liquidación reduciendo costos operativos, y permitir divisibilidad extrema que hace accesibles bonos corporativos o gubernamentales a inversores minoristas que tradicionalmente quedaban excluidos por montos mínimos de inversión elevados. Proyectos como Obligate tokenizaron bonos de empresas suecas sobre Ethereum, mientras plataformas como Centrifuge permiten a empresas emitir deuda respaldada por activos reales como facturas o inventarios.

La distinción fundamental entre equity y debt tokens radica en los derechos que confieren: mientras los equity tokens otorgan propiedad parcial de la empresa emisora con derechos de voto y participación en beneficios sin garantía de retorno, los debt tokens representan un contrato de préstamo con obligación legal de devolución del capital más intereses, pero sin derechos de propiedad ni voto corporativo. Esta diferencia determina perfiles de riesgo distintos, tratamientos fiscales diferenciados, y jerarquías de prelación en caso de liquidación del emisor, donde los tenedores de debt tokens generalmente tienen prioridad sobre los equity holders.

**Stablecoins bajo MiCA: E-Money Tokens y Asset-Reference Tokens**:

El Reglamento MiCA en Europa clasifica las stablecoins en dos categorías principales según su mecanismo de respaldo y objetivo de estabilidad.

Los **E-Money Tokens (EMT)** o tokens de dinero electrónico representan stablecoins diseñadas para mantener una paridad 1:1 con una **moneda fiat específica**, típicamente el dólar estadounidense o el euro. Esta categoría emerge de la Directiva de Dinero Electrónico europea, que define e-money como valor monetario almacenado electrónicamente que representa un crédito sobre el emisor, emitido contra la recepción de fondos con el propósito de realizar operaciones de pago, y que es aceptado por terceros distintos del emisor. Stablecoins como USDC, USDT o EURD encajan en esta definición cuando cumplen ciertos criterios.

Los **Asset-Reference Tokens (ART)**, por su parte, son stablecoins diseñadas para mantener un valor estable **referenciado a una cesta diversificada de activos** en lugar de una sola moneda fiat. Esta cesta puede incluir múltiples divisas (por ejemplo, una combinación de USD, EUR, JPY), commodities (oro, plata, petróleo), bonos gubernamentales u otros activos que proporcionen estabilidad. Aunque menos comunes que los EMT, los ART representan el intento de crear monedas estables con menor dependencia de una sola moneda soberana, ofreciendo mayor diversificación pero introduciendo mayor complejidad operativa.

Cuando una stablecoin cumple con los criterios de EMT o ART bajo MiCA, su emisor debe obtener licencia como entidad regulada dentro del Espacio Económico Europeo, mantener reservas equivalentes al cien por cien del valor emitido en activos seguros y líquidos, someterse a supervisión prudencial continua y cumplir con requisitos estrictos de transparencia y protección al consumidor. Los ART enfrentan requisitos regulatorios aún más estrictos debido a la complejidad de gestionar múltiples colaterales y el riesgo adicional que introduce la diversificación de activos.

Esta clasificación tiene implicaciones profundas: convierte a los emisores de stablecoins en entidades financieras reguladas con todas las obligaciones que ello conlleva, estableciendo un marco claro que distingue entre stablecoins ancladas a monedas únicas (EMT) y aquellas respaldadas por cestas diversificadas (ART).

**Payment tokens**:

Los payment tokens representan una categoría específica de activos digitales diseñados principalmente para funcionar como medio de intercambio y pago, sin las características que los convertirían en securities bajo marcos regulatorios como el test de Howey. Estos tokens se distinguen por su propósito primario: facilitar transacciones económicas de forma eficiente, rápida y sin intermediarios.

Desde una perspectiva regulatoria, los payment tokens ocupan un espacio distinto a utility y security tokens. La [Autoridad Suiza de Supervisión de los Mercados Financieros (FINMA)](https://www.finma.ch/en/news/2018/02/20180216-mm-ico-wegleitung/) estableció en su guía de 2018 una taxonomía que reconoce payment tokens como categoría separada, definiéndolos como tokens que funcionan como medio de pago para adquirir bienes o servicios, o como medio de transferencia de dinero o valor. Esta clasificación distingue payment tokens de utility tokens, que otorgan acceso a servicios específicos de un ecosistema, y de security tokens, que representan derechos de inversión.

Bitcoin ejemplifica el arquetipo de payment token, funcionando exclusivamente como sistema de pagos peer-to-peer sin otorgar derechos sobre ninguna empresa ni acceso exclusivo a servicios específicos. Litecoin, Bitcoin Cash y otras criptomonedas centradas en transferencias de valor comparten esta categorización. Las stablecoins como USDC o USDT, aunque técnicamente clasificadas bajo MiCA como E-Money Tokens, funcionan operativamente como payment tokens al facilitar transacciones sin volatilidad de precio.

La distinción entre payment token y utility token resulta crucial en términos regulatorios y técnicos. Un payment token puede utilizarse para pagar a cualquier receptor que lo acepte, sin restricción a un ecosistema específico, mientras que un utility token proporciona acceso a funcionalidades concretas dentro de una plataforma determinada. Esta diferencia determina cómo reguladores evalúan el token: los payment tokens enfrentan regulación bajo marcos de dinero electrónico o sistemas de pago, mientras los utility tokens se someten a normativas específicas de criptoactivos como MiCA que exigen transparencia sobre el proyecto y protección al consumidor.

En la práctica, la frontera entre categorías puede resultar difusa cuando un mismo token cumple múltiples funciones. XRP de Ripple, por ejemplo, funciona como payment token en su red para facilitar pagos transfronterizos, pero su relación con Ripple Labs y las expectativas de inversión generaron controversia regulatoria sobre si constituye un security. Esta ambigüedad ha llevado a que proyectos diseñen cuidadosamente la arquitectura y narrativa de sus tokens para evitar clasificaciones regulatorias indeseadas.

**Governance tokens**:

Los governance tokens representan una categoría de activos digitales que otorgan a sus poseedores derechos de voto y participación en las decisiones que determinan la evolución de protocolos descentralizados. A diferencia de los utility tokens puros, cuya función principal es habilitar acceso a servicios o pago de comisiones, los governance tokens confieren poder político dentro del ecosistema que los emite.

La arquitectura técnica de governance tokens se implementa mediante contratos inteligentes que vinculan la posesión del token con capacidad de proponer cambios al protocolo y votar sobre propuestas presentadas por otros miembros de la comunidad. El modelo típico utiliza un sistema de gobernanza on-chain donde cada token equivale a un voto, aunque existen variantes como voto cuadrático que mitigan la concentración de poder. Los holders pueden proponer modificaciones a parámetros del protocolo, aprobación de actualizaciones de código, asignación de fondos del tesoro comunitario, o cambios en la estructura de comisiones.

Uniswap con su token UNI ejemplifica este modelo: los poseedores de UNI votan sobre propuestas de mejora del protocolo (UIPs), decisiones sobre distribución de comisiones generadas por el DEX, y aprobación de nuevas funcionalidades. Compound implementó gobernanza descentralizada mediante su token COMP, permitiendo a holders votar sobre tasas de interés, activos soportados como colateral, y cambios al algoritmo de liquidación. MakerDAO, uno de los sistemas de gobernanza más sofisticados del ecosistema, utiliza MKR para permitir a su comunidad controlar parámetros críticos del protocolo DAI como tipos de colateral aceptados, ratios de colateralización, y tasas de estabilidad.

Desde una perspectiva regulatoria, los governance tokens ocupan un espacio complejo. Por un lado, otorgan derechos que podrían asemejarse a acciones corporativas tradicionales, particularmente cuando incluyen control sobre tesorerías valoradas en millones de dólares. Sin embargo, muchos proyectos argumentan que no constituyen securities bajo el test de Howey porque los beneficios no derivan principalmente de esfuerzos de terceros, sino de la participación activa de la comunidad gobernante. La SEC estadounidense no ha establecido una posición definitiva sobre esta categoría, evaluando caso por caso según el contexto específico de cada token.

La distinción entre governance token puro y token híbrido resulta crucial. Algunos tokens combinan funciones de utilidad y gobernanza: AAVE, por ejemplo, funciona como token de gobernanza permitiendo votar sobre el protocolo Aave, pero también otorga descuentos en comisiones y acceso a funcionalidades premium, convirtiéndolo en híbrido utility-governance. Esta dualidad introduce complejidad regulatoria adicional, ya que la presencia de utilidad práctica además de derechos de voto puede afectar cómo reguladores clasifican el activo.

Un fenómeno importante en governance tokens es el problema de la participación. Aunque conceptualmente democratizan el control de protocolos, en la práctica enfrentan bajas tasas de participación electoral donde grandes holders (ballenas) ejercen influencia desproporcionada mientras pequeños inversores no participan activamente en votaciones. Esto ha llevado a innovaciones como voto delegado, donde holders pueden delegar su poder de voto a representantes especializados que votan en su nombre, similar a democracias representativas tradicionales.

**Tokens híbridos y ambigüedad regulatoria**:

La taxonomía regulatoria de tokens asume categorías mutuamente excluyentes donde un activo digital es utility, security, payment o governance token. Sin embargo, la realidad técnica y económica de muchos proyectos blockchain produce tokens híbridos que combinan características de múltiples categorías simultáneamente, creando zonas grises regulatorias que desafían marcos legales tradicionales diseñados para activos financieros convencionales.

MiFID II en Europa aplica a tokens con características de instrumentos financieros tradicionales, obligando a plataformas que los negocian a cumplir requisitos estrictos como registro ante autoridades competentes, implementación de protocolos de protección al inversor, mantenimiento de capital regulatorio mínimo, y separación de activos de clientes. Simultáneamente, MiCA regula utility tokens que proporcionan acceso a servicios específicos. El desafío surge cuando un mismo token exhibe características que lo colocarían bajo ambos marcos: un token que otorga acceso a servicios del protocolo mientras simultáneamente confiere derechos de gobernanza y expectativas de apreciación económica derivada del éxito del proyecto.

El caso de AAVE ilustra perfectamente esta hibridez. Técnicamente, AAVE funciona como utility token permitiendo pagar comisiones reducidas en el protocolo de lending Aave y participar en el Safety Module aportando liquidez que absorbe deuda insolvente. Simultáneamente, funciona como governance token otorgando poder de voto sobre parámetros críticos del protocolo, tipos de interés, activos soportados y uso del tesoro. Adicionalmente, genera expectativas de inversión donde holders anticipan apreciación de precio vinculada al crecimiento del protocolo Aave y volumen de préstamos procesados. Esta triple naturaleza utility-governance-investment desafía clasificación binaria en marcos regulatorios existentes.

Binance Coin (BNB) representa otro ejemplo prominente de token híbrido. Originalmente lanzado como utility token para pagar comisiones reducidas en el exchange Binance, BNB evolucionó hacia múltiples funciones: medio de pago aceptado por comerciantes, gas token nativo de BNB Chain para ejecutar contratos inteligentes, colateral en protocolos DeFi, y activo de inversión con mecanismos de quema deflacionarios que crean expectativas de apreciación. Esta evolución funcional transforma la clasificación regulatoria del token a lo largo del tiempo, planteando la pregunta de si debe evaluarse según su diseño original o su uso actual predominante.

La evolución temporal de tokens genera incertidumbre regulatoria adicional. Un proyecto puede lanzarse inicialmente como utility token puro, proporcionando acceso exclusivo a servicios específicos sin derechos de inversión ni gobernanza. Con el tiempo, la comunidad demanda mayor participación en decisiones del protocolo, llevando a implementar gobernanza on-chain mediante el token existente. Este mismo token ahora combina utilidad original con derechos de voto, alterando potencialmente su clasificación regulatoria. La pregunta surge: ¿debe el token reclasificarse como security si adquiere características de inversión post-lanzamiento? La SEC no ha proporcionado guía clara sobre esta transición temporal.

El test de Howey en Estados Unidos, diseñado en 1946 para evaluar contratos de inversión en naranjales, enfrenta limitaciones fundamentales cuando se aplica a tokens multiusos. El test requiere inversión de dinero en empresa común con expectativa de beneficios derivados principalmente de esfuerzos de terceros. Un token híbrido que proporciona utilidad funcional real mientras simultáneamente genera expectativas de apreciación puede pasar o fallar el test según qué aspecto se enfatice. Si el uso predominante es acceso a servicios, argumentablemente no es security. Si la mayoría de holders nunca utilizan la utilidad y solo especulan sobre precio, argumentablemente sí lo es. Esta ambigüedad genera riesgo legal impredecible para proyectos.

La estrategia de descentralización progresiva emerge como respuesta pragmática a esta ambigüedad. Proyectos lanzan inicialmente bajo estructuras reguladas reconociendo el token como security durante fases tempranas cuando el equipo fundador ejerce control centralizado y el protocolo carece de utilidad funcional. Gradualmente transfieren control a la comunidad mediante gobernanza descentralizada, aumentan utilidad funcional del token mediante integración en el protocolo, y distribuyen tokens ampliamente para evitar concentración. La hipótesis sostiene que suficiente descentralización y utilidad real pueden transicionar el token desde security hacia utility o commodity, aunque la SEC no ha confirmado explícitamente este camino.

Las ventas geográficamente restringidas representan otra estrategia de mitigación de riesgo regulatorio. Proyectos lanzan tokens excluyendo compradores de jurisdicciones con marcos regulatorios estrictos, particularmente Estados Unidos, mediante geoblocking, verificaciones KYC que rechazan residentes estadounidenses, y disclaimers legales explícitos. Esta fragmentación crea mercados primarios balcanizados donde el mismo token se clasifica diferentemente según la jurisdicción, comprador estadounidense lo adquiere como security en mercado secundario mientras comprador europeo bajo MiCA lo trata como utility token.

Los lanzamientos en fases implementan temporalidad estructurada que intenta navegar ambigüedad regulatoria. Fase 1 vende a inversores acreditados bajo framework SAFT reconociendo explícitamente que son securities. Fase 2 lanza el protocolo con utilidad funcional limitada, distribuyendo tokens a holders de SAFT. Fase 3 descentraliza gobernanza y expande utilidad, argumentando transición hacia utility token. Esta estructura temporal reconoce realidades regulatorias mientras aspira a eventual desclasificación como security, aunque sin garantías legales.

El panorama regulatorio fragmentado globalmente amplifica la complejidad de tokens híbridos. Suiza bajo FINMA reconoce explícitamente posibilidad de tokens que combinan características utility-payment-asset, evaluándolos según función económica predominante. La FCA del Reino Unido utiliza enfoque funcional similar, clasificando según caso de uso real en lugar de diseño técnico. Estados Unidos mantiene aproximación más binaria bajo test de Howey, resistiendo categorías híbridas. Europa bajo MiCA establece categorías más rígidas pero incluye provisión para tokens que no encajan claramente en ninguna, sometiéndolos a supervisión caso por caso. Esta fragmentación obliga a proyectos globales a estructuras multi-jurisdiccionales complejas donde el mismo token opera bajo marcos legales diferentes según geografía del usuario.

La ambigüedad regulatoria de tokens híbridos no es simplemente inconveniencia burocrática sino que genera consecuencias económicas y estratégicas reales. Proyectos enfrentan riesgo de enforcement actions retroactivas si reguladores determinan post-facto que su utility token constituía security no registrado, potencialmente resultando en multas millonarias y obligación de devolver fondos a inversores. Esta incertidumbre disuade inversión institucional que requiere claridad legal antes de comprometer capital significativo. Paradójicamente, la ambigüedad beneficia proyectos menos escrupulosos que explotan zonas grises para evadir supervisión, mientras penaliza proyectos legítimos que intentan cumplir con regulaciones poco claras.

La evolución futura de marcos regulatorios determinará si tokens híbridos se reconocen como categoría legítima que requiere regulación adaptada a sus características únicas, o si reguladores fuerzan clasificación binaria que simplifica supervisión pero ignora realidades técnicas del ecosistema blockchain. La tendencia en jurisdicciones innovadoras como Suiza y Singapur sugiere movimiento hacia reconocimiento de hibridez, mientras que Estados Unidos mantiene posición más conservadora que favorece clasificación tradicional incluso cuando inadecuada para activos digitales multiusos.

**Asset-backed tokens y Real World Assets (RWA)**:

Los asset-backed tokens o tokens respaldados por activos representan instrumentos digitales cuyo valor deriva de activos tangibles o financieros del mundo real que los colateralizan. Esta categoría constituye uno de los puentes más directos entre las finanzas tradicionales y el ecosistema blockchain, permitiendo tokenizar prácticamente cualquier clase de activo con valor económico.

La arquitectura técnica de asset-backed tokens requiere una estructura que vincule el token digital on-chain con el activo físico o financiero que lo respalda. Este vínculo generalmente involucra custodios regulados que mantienen posesión legal del activo subyacente mientras el token circula en blockchain, contratos legales que establecen los derechos del poseedor del token sobre el activo, mecanismos de valoración que reflejan el precio del activo real en el token digital, y procedimientos de redención que permiten intercambiar tokens por los activos subyacentes bajo condiciones específicas.

Los bienes raíces tokenizados representan una de las aplicaciones más prominentes de RWA. Proyectos como [RealT](https://realt.co/) permiten fraccionar propiedad de inmuebles en Estados Unidos, donde cada token representa porcentaje de propiedad de una propiedad física específica que genera rentas de alquiler distribuidas automáticamente a holders mediante contratos inteligentes. [Propy](https://propy.com/) facilita compraventa de propiedades mediante títulos tokenizados registrados en blockchain, reduciendo fricción y costos de transacciones inmobiliarias tradicionales. Esta tokenización democratiza acceso a inversiones inmobiliarias que tradicionalmente requieren capital significativo, permite liquidez en un mercado históricamente ilíquido, y automatiza distribución de rentas eliminando intermediarios.

Las commodities tokenizadas constituyen otra categoría importante de RWA. [Paxos Gold (PAXG)](https://paxos.com/paxg/) y [Tether Gold (XAUT)](https://gold.tether.to/) representan onzas troy de oro físico almacenado en bóvedas auditadas, permitiendo inversión en oro sin necesidad de custodia física ni costos de almacenamiento directo. Cada token equivale a una cantidad específica de oro real, auditable mediante reportes públicos. Proyectos experimentales han tokenizado petróleo, metales industriales y productos agrícolas, aunque con adopción limitada por complejidad logística y regulatoria.

Los instrumentos financieros tradicionales tokenizados expanden el concepto de RWA a activos puramente financieros. [Ondo Finance](https://ondo.finance/) tokeniza bonos del tesoro estadounidense, permitiendo acceso on-chain a rendimientos de deuda soberana considerada libre de riesgo. [Backed Finance](https://backed.fi/) ofrece tokens respaldados por ETFs tradicionales, replicando exposición a índices bursátiles como S&P 500 en formato ERC-20. [Maple Finance](https://www.maple.finance/) tokeniza préstamos corporativos, creando mercados secundarios para deuda empresarial previamente ilíquida.

Desde una perspectiva regulatoria, los asset-backed tokens generalmente se clasifican como security tokens, especialmente cuando representan derechos económicos sobre activos que generan rendimientos. En Europa, caen bajo MiFID II si cumplen definición de valores negociables, requiriendo registro, divulgación mediante folletos, y cumplimiento de normativas KYC/AML. La CNMV en España supervisa emisiones de RWA bajo los mismos marcos que valores tradicionales, exigiendo estructuras legales robustas que establezcan claramente derechos del token holder sobre el activo subyacente.

Los desafíos fundamentales de RWA incluyen el problema del oráculo físico-digital: garantizar que el activo real efectivamente existe y está custodiado correctamente requiere confianza en entidades off-chain verificadoras, introduciendo riesgo de centralización. Las auditorías periódicas, seguros sobre activos custodiados, y marcos legales que reconozcan la tokenización como prueba de propiedad resultan esenciales para la viabilidad de estos instrumentos. Adicionalmente, la redención de tokens por activos físicos enfrenta fricciones logísticas y costos que pueden erosionar las ventajas de eficiencia que promete la tokenización.

**Synthetic assets**:

Los synthetic assets o activos sintéticos constituyen instrumentos financieros derivados implementados mediante contratos inteligentes que replican el comportamiento de precio de activos subyacentes sin requerir posesión directa de dichos activos. A diferencia de los asset-backed tokens que mantienen custodia del activo real, los sintéticos utilizan mecanismos de colateralización y oráculos de precio para crear exposición económica equivalente de forma puramente on-chain.

La arquitectura técnica de synthetic assets se fundamenta en tres componentes esenciales: colateral bloqueado en contratos inteligentes que respalda el valor del sintético, oráculos de precio que alimentan datos del activo subyacente desde fuentes externas a la blockchain, y mecanismos de liquidación que garantizan que el sintético mantiene su paridad con el activo que replica. Cuando un usuario desea crear un activo sintético, deposita colateral en el protocolo, generalmente sobrecola teralizado para absorber volatilidad, y acuña tokens sintéticos cuyo valor refleja el precio del activo subyacente reportado por oráculos.

[Synthetix](https://synthetix.io/) pionero en este espacio, permite crear activos sintéticos llamados Synths que replican prácticamente cualquier activo: sUSD sigue el dólar estadounidense, sBTC replica el precio de Bitcoin, sETH el de Ethereum, y sAAPL el precio de acciones de Apple sin necesidad de poseer acciones reales. Los usuarios bloquean SNX, el token nativo del protocolo, como colateral sobrecol ateralizado típicamente al 400-500%, y acuñan Synths contra ese colateral. Los oráculos de [Chainlink](https://chain.link/) alimentan precios actualizados que determinan el valor de cada Synth, permitiendo que traders obtengan exposición a activos tradicionales de forma descentralizada.

[Mirror Protocol](https://mirror.finance/) en el ecosistema Terra implementó sintéticos específicamente para acciones estadounidenses, permitiendo acceso global a mercados de valores que tradicionalmente excluyen inversores de jurisdicciones sin acceso a brokers internacionales. Los mAssets de Mirror replicaban precios de acciones como Tesla, Amazon o Google mediante colateralización con UST y oráculos de precio. Aunque el colapso de Terra destruyó Mirror Protocol, demostró demanda real por acceso descentralizado a mercados tradicionales.

La distinción fundamental entre synthetic assets y wrapped tokens radica en su mecanismo de respaldo. Un wrapped token como WBTC requiere custodia del Bitcoin real por un custodio centralizado que emite tokens equivalentes. Un sintético como sBTC no requiere Bitcoin subyacente, solo colateral suficiente y un oráculo confiable que reporte su precio. Esta diferencia elimina riesgo de custodia centralizada pero introduce riesgo de oráculo y riesgo de colateralización insuficiente durante volatilidad extrema.

Desde una perspectiva regulatoria, los synthetic assets plantean desafíos únicos. Cuando replican securities tradicionales como acciones, enfrentan escrutinio regulatorio por potencialmente permitir comercio de valores sin las protecciones que exigen marcos como MiFID II o SEC. La [SEC ha expresado preocupación](https://www.sec.gov/news/press-release/2021-127) sobre protocolos que ofrecen sintéticos de acciones estadounidenses, argumentando que constituyen valores mobiliarios no registrados. Mirror Protocol enfrentó investigaciones de la SEC antes del colapso de Terra, ilustrando la tensión entre innovación financiera descentralizada y cumplimiento regulatorio.

Los riesgos específicos de synthetic assets incluyen dependencia crítica de oráculos donde manipulación o fallas pueden descorrelacionar el sintético de su subyacente, generando pérdidas catastróficas. El riesgo de colateralización insuficiente durante eventos de cisne negro puede provocar que el protocolo se vuelva insolvente, incapaz de respaldar todos los sintéticos emitidos. La complejidad de estos instrumentos los hace inadecuados para inversores sin comprensión profunda de sus mecanismos y riesgos inherentes.

**SAFT: Simple Agreement for Future Tokens**:

El [SAFT (Simple Agreement for Future Tokens)](https://saftproject.com/) representa un marco legal desarrollado específicamente para estructurar ventas de tokens futuros de forma conforme con regulación de valores estadounidense. Este instrumento surgió como respuesta directa a la incertidumbre regulatoria que enfrentaban proyectos blockchain durante el auge de las ICOs entre 2017 y 2018, cuando la SEC comenzó a señalar que muchas ventas de tokens constituían ofertas de securities no registradas.

La estructura técnica y legal del SAFT funciona como contrato de inversión donde el comprador aporta capital al proyecto a cambio del compromiso de recibir tokens funcionales una vez que la red se lance y los tokens tengan utilidad real. Crucialmente, el SAFT se vende exclusivamente a inversores acreditados bajo Regulation D de la SEC, específicamente mediante exenciones 506(b) o 506(c) que permiten captación de capital privado sin registro público bajo condiciones estrictas. Esto convierte al SAFT en un security reconocido explícitamente, cumpliendo con normativas aplicables a instrumentos de inversión.

La premisa del framework SAFT distingue dos fases temporales con clasificaciones regulatorias diferentes. Durante la primera fase, el proyecto vende SAFTs como securities a inversores acreditados, recaudando capital para desarrollo mientras cumple plenamente con regulación de valores. En la segunda fase, una vez que la red blockchain se lanza y los tokens adquieren utilidad funcional real dentro del ecosistema operativo, se entregan tokens a los holders de SAFTs. El argumento legal sostiene que en esta segunda fase, los tokens funcionales ya no son securities porque cumplen propósito de utilidad en lugar de función primaria de inversión especulativa.

Filecoin ejemplifica la implementación más prominente del framework SAFT. En 2017, Protocol Labs recaudó más de 200 millones de dólares mediante venta de SAFTs a inversores acreditados, estructurando cuidadosamente la operación para cumplir con regulación SEC. Los compradores de SAFTs firmaron contratos reconociendo que adquirían securities y aceptando restricciones de reventa. Cuando Filecoin lanzó su mainnet en 2020, los holders de SAFTs recibieron tokens FIL funcionales utilizables para pagar almacenamiento descentralizado en la red Filecoin. Otros proyectos como Tezos y Blockstack también utilizaron estructuras SAFT durante sus captaciones de capital.

Las ventajas del framework SAFT para proyectos incluyen claridad regulatoria al reconocer explícitamente que la venta inicial es un security, evitando ambigüedad que podría resultar en enforcement actions de la SEC. Permite recaudar capital significativo de inversores institucionales y acreditados que requieren estructuras legales robustas. Proporciona potencial ruta hacia desclasificación del token como security una vez que adquiere utilidad funcional real, aunque este punto permanece debatido legalmente.

Las limitaciones críticas incluyen restricción a inversores acreditados durante la fase SAFT, excluyendo participación retail que históricamente constituía base comunitaria de proyectos cripto. La estructura introduce complejidad legal y costos significativos de estructuración, asesoría legal y cumplimiento que proyectos pequeños no pueden absorber. Críticamente, no existe garantía de que la SEC considere que los tokens finales escapan clasificación como securities, incluso después del lanzamiento de la red. La posición de la SEC sobre la transición de SAFT a utility token funcional permanece incierta, con casos como Telegram demostrando que el regulador puede considerar que tokens entregados post-lanzamiento siguen siendo securities.

El framework SAFT representa un intento pragmático de navegar marcos regulatorios tradicionales diseñados para valores mobiliarios en un contexto de innovación tecnológica descentralizada. Su adopción limitada refleja tanto la complejidad que introduce como la incertidumbre persistente sobre si realmente proporciona safe harbor regulatorio que sus creadores pretendían.

## Tokens fungibles y no fungibles

La distinción entre tokens fungibles y no fungibles constituye una clasificación técnica fundamental que define cómo interactuamos con activos digitales y qué tipos de valor pueden representar.

**Tokens fungibles**:

Un token fungible posee la propiedad de intercambiabilidad perfecta: cada unidad es idéntica e indistinguible de cualquier otra unidad del mismo tipo. Esta fungibilidad resulta esencial para activos que funcionan como dinero o medios de intercambio.

Es importante aclarar que las criptomonedas son inherentemente fungibles por su naturaleza como moneda nativa de una blockchain. La distinción entre fungibilidad y no fungibilidad surge específicamente en el contexto de tokens creados sobre blockchains existentes. Un bitcoin es equivalente a cualquier otro bitcoin por diseño fundamental de su protocolo, al igual que un ether es intercambiable por otro ether. Esta fungibilidad no es una característica opcional sino una propiedad intrínseca de las criptomonedas.

Sin embargo, la historia muestra intentos tempranos de romper esta fungibilidad. Los colored coins de Bitcoin, pioneros de la tokenización, "coloreaban" pequeñas cantidades de bitcoin (satoshis) para representar otros activos mediante metadatos externos. Aunque técnicamente seguían siendo bitcoins fungibles a nivel de protocolo, conceptualmente perdían intercambiabilidad al asignar significados específicos diferentes. Su fragilidad radicaba en depender de consenso social y software externo para mantener la "coloración", pudiendo romperse accidentalmente al usar wallets que no entendieran el protocolo de coloración.

Los tokens fungibles modernos, implementados mediante estándares como [ERC-20](https://eips.ethereum.org/EIPS/eip-20) en Ethereum, BEP-20 en BNB Chain o SPL en Solana, resolvieron estas limitaciones. Son verdaderos tokens porque son programables mediante contratos inteligentes que garantizan su comportamiento. El estándar ERC-20, cuyas siglas significan Ethereum Request for Comment 20, define una interfaz común que todo token fungible debe implementar. Las funciones fundamentales incluyen `transfer` para enviar tokens entre direcciones, `approve` para autorizar a terceros a gastar tokens en nombre del propietario, `transferFrom` para ejecutar transferencias autorizadas, y `balanceOf` para consultar el saldo de cualquier dirección. Esta estandarización permite que cualquier wallet, exchange o aplicación descentralizada interactúe con tokens ERC-20 de forma predecible sin necesidad de integración personalizada para cada token.

Implementaciones de referencia como las de [OpenZeppelin](https://docs.openzeppelin.com/contracts/5.x/erc20) o [Solmate](https://github.com/transmissions11/solmate) proporcionan código auditado y optimizado que proyectos pueden utilizar como base, reduciendo riesgos de seguridad y acelerando el desarrollo. La mayoría de tokens que representan utilidad, stablecoins y tokens de gobernanza son fungibles por diseño, garantizando mediante contratos inteligentes las reglas de intercambiabilidad que los colored coins no podían asegurar.

Más allá de ERC-20, existen extensiones y alternativas que abordan limitaciones específicas. [ERC-777](https://eips.ethereum.org/EIPS/eip-777) introduce hooks o ganchos que permiten ejecutar lógica personalizada cuando se reciben o envían tokens mediante las funciones `tokensReceived` y `tokensToSend`. Esta mayor flexibilidad permite casos de uso avanzados como rechazo de tokens no deseados o ejecución automática de acciones al recibir pagos. Sin embargo, esta complejidad adicional introduce vectores de ataque potenciales, particularmente vulnerabilidades de reentrancy donde contratos maliciosos pueden explotar la ejecución de código durante transferencias. Por esta razón, ERC-777 ha tenido adopción limitada y muchos proyectos prefieren la simplicidad y seguridad probada de ERC-20.

[ERC-4626](https://eips.ethereum.org/EIPS/eip-4626) representa una estandarización crucial para protocolos DeFi que gestionan depósitos y generación de rendimiento. Este estándar define una interfaz común para vaults tokenizados, contratos que aceptan depósitos de un activo base y emiten tokens representativos que acumulan valor con el tiempo. Las funciones core incluyen `deposit` para aportar activos y recibir shares, `withdraw` para recuperar activos quemando shares, y `convertToShares` para calcular la conversión entre activos base y shares del vault. Protocolos como Yearn V3 han adoptado ERC-4626, permitiendo que diferentes vaults se integren de forma modular mediante herramientas como ERC4626Router que optimizan movimientos de capital entre estrategias. Esta estandarización transforma vaults individuales en componibles interoperables, reduciendo fricción entre protocolos y facilitando agregadores que maximizan rendimientos automáticamente.

**Tokens no fungibles (NFTs)**:

Los tokens no fungibles representan activos únicos e indivisibles. Cada NFT posee un identificador único que lo distingue de todos los demás, incluso dentro de la misma colección. Esta característica los hace ideales para representar propiedad de elementos digitales únicos como arte, coleccionables, terrenos virtuales, identidades digitales o certificados de autenticidad.

El estándar [ERC-721](https://eips.ethereum.org/EIPS/eip-721) en Ethereum popularizó los NFTs, estableciendo la interfaz fundamental para tokens únicos. Cada token posee un `tokenId` que lo identifica unívocamente dentro del contrato. Las funciones core incluyen `ownerOf` para consultar el propietario de un token específico, `safeTransferFrom` para transferencias seguras que verifican que el receptor puede manejar NFTs, y un sistema de metadata URI que vincula cada token con información externa como imágenes, descripciones o atributos. Implementaciones como [OpenZeppelin ERC721](https://docs.openzeppelin.com/contracts/5.x/erc721) y [Solmate ERC721](https://github.com/transmissions11/solmate) proporcionan código base auditado que balancea funcionalidad con eficiencia de gas.

Posteriormente, [ERC-1155](https://eips.ethereum.org/EIPS/eip-1155) introdujo un enfoque híbrido que permite gestionar tanto tokens fungibles como no fungibles dentro del mismo contrato. Esta arquitectura multi-token resulta particularmente eficiente para casos de uso como videojuegos donde coexisten monedas fungibles, objetos únicos y ediciones limitadas de items. Las transferencias en batch permiten mover múltiples tipos de tokens en una sola transacción, reduciendo costos de gas significativamente comparado con ERC-721. Plataformas como OpenSea y proyectos gaming basados en Enjin han adoptado ampliamente ERC-1155 por su versatilidad y eficiencia operativa.

Más allá del arte digital y los coleccionables, los NFTs encuentran aplicaciones en tokenización de activos del mundo real, certificados académicos verificables, tickets de eventos con protección contra falsificación, y sistemas de identidad descentralizada.

Una aplicación particularmente relevante es el NFT gating: el uso de NFTs como llaves de acceso que otorgan derechos exclusivos a comunidades, servicios o contenidos. Los poseedores de NFTs específicos pueden acceder a Discord privados, eventos exclusivos, ventajas en juegos, contenido premium o incluso descuentos en productos físicos. Este modelo convierte a los NFTs en membresías verificables que crean valor de utilidad más allá del mero coleccionismo.

**Soulbound Tokens (SBT)**:

Los Soulbound Tokens representan una evolución específica de los NFTs caracterizada por su intransferibilidad. Introducidos conceptualmente por Vitalik Buterin y otros investigadores en su artículo [Decentralized Society: Finding Web3's Soul](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763), estos tokens están "atados al alma" de la dirección que los posee, imposibilitando su transferencia, venta o intercambio. Su propósito es representar credenciales, logros, afiliaciones o características inherentes a una identidad que no deberían ser comercializables.

Los SBT encuentran aplicaciones en certificaciones profesionales verificables, historial educativo, reputación on-chain, membresías no transferibles, historial de participación en DAOs y cualquier tipo de credencial que derive su valor de estar asociada a una identidad específica. A diferencia de los NFTs tradicionales, cuyo valor a menudo reside en su transferibilidad y potencial especulativo, los SBT crean valor a través de la acumulación de reputación y credenciales no falsificables. Ejemplos prácticos incluyen POAPs como proof of attendance que documentan participación en eventos, aunque técnicamente son transferibles, y Binance Account Bound tokens que verifican identidad sin posibilidad de comercio.

**Fractional NFTs**:

Los Fractional NFTs o F-NFTs permiten dividir la propiedad de un NFT de alto valor entre múltiples poseedores mediante tokenización fraccionaria. Un NFT costoso puede ser "fraccionado" en múltiples tokens fungibles ERC-20 que representan porcentajes de propiedad del NFT original. Plataformas como [Fractional.art](https://fractional.art/), [NFTX](https://nftx.io/) y Unicly han implementado estos mecanismos, permitiendo que coleccionables como CryptoPunks o Bored Ape Yacht Club sean accesibles a inversores que no pueden adquirir el NFT completo. Esto democratiza el acceso a arte digital y coleccionables de alto valor, creando liquidez para activos tradicionalmente ilíquidos y nuevos modelos de inversión colectiva en arte digital.

**ERC-404 y DN-404: tokens híbridos nativos**:

Los estándares experimentales [ERC-404](https://www.erc404.com/) y su evolución DN-404 representan una propuesta diferente en la búsqueda de liquidez para NFTs. A diferencia de los Fractional NFTs que dividen un NFT existente mediante contratos externos, estos estándares fusionan nativamente las características de tokens fungibles (ERC-20) y no fungibles (ERC-721).

El mecanismo funciona mediante acuñado y quemado automático: cuando un usuario posee una unidad completa del token fungible, automáticamente recibe un NFT asociado. Si transfiere o vende una fracción (por ejemplo, 0.5 tokens), el NFT se quema. Al volver a acumular una unidad completa, se acuña un nuevo NFT, potencialmente con características diferentes. Este diseño permite que los tokens se negocien simultáneamente en DEXs como tokens fungibles y en marketplaces NFT como coleccionables únicos.

Proyectos pioneros como [Pandora](https://twitter.com/Pandora_ERC404) demostraron la viabilidad del concepto con ERC-404, superando 100 millones de dólares en volumen durante su primera semana. Esta liquidez nativa contrasta con el fraccionamiento tradicional, donde el NFT original permanece bloqueado en un contrato mientras se comercian sus fracciones. DN-404 surgió como una mejora técnica que utiliza dos contratos separados (uno ERC-20 y otro ERC-721 que se sincronizan), reduciendo significativamente los costes de gas y mejorando la eficiencia respecto a la implementación original de ERC-404.

Ambos estándares permanecen experimentales y no han sido incorporados oficialmente al repositorio de propuestas de Ethereum (EIPs). Requieren auditorías exhaustivas antes de una adopción más amplia, especialmente considerando la complejidad adicional que introduce el mecanismo de acuñado/quemado automático. Aunque similares conceptualmente a ERC-1155 en su capacidad de gestionar tokens fungibles y no fungibles, se distinguen por su enfoque en liquidez nativa y fraccionamiento dinámico.

La capacidad de verificar autenticidad y propiedad de forma pública e inmutable mediante blockchain abre posibilidades que trascienden la especulación inicial que caracterizó el auge de los NFTs en 2021, estableciendo modelos sostenibles de acceso y pertenencia a comunidades digitales.

La distinción entre fungibilidad y no fungibilidad no es meramente técnica sino que responde a necesidades económicas diferentes: los tokens fungibles optimizan liquidez e intercambio, mientras los NFTs preservan unicidad y trazabilidad de elementos que derivan su valor precisamente de su singularidad.

**Ecosistema de aplicaciones NFT**:

Más allá de las categorías técnicas fundamentales (NFTs estándar, SBTs intransferibles, NFTs fraccionarios y ERC-404), existe un vasto ecosistema de aplicaciones construidas sobre estos estándares:

- **Arte digital y coleccionables**: Autenticidad verificable on-chain, regalías automáticas programadas en el contrato mediante royalties (típicamente 2.5-10% en ventas secundarias), y propiedad demostrable sin intermediarios. Marketplaces como [OpenSea](https://opensea.io/), [Rarible](https://rarible.com/), [SuperRare](https://superrare.com/) o [Foundation](https://foundation.app/) facilitan el comercio secundario con soporte multi-chain.

- **NFT Drops y colecciones**: Los NFT drops representan lanzamientos programados de colecciones limitadas que generan expectación mediante escasez artificial y marketing previo. Estos eventos de acuñación (minting) controlada, frecuentemente liderados por artistas reconocidos o proyectos establecidos, crean demanda mediante disponibilidad temporal restringida. Las mecánicas incluyen listas blancas (whitelists) para acceso prioritario, acuñación aleatoria con rasgos variables que determinan rareza, y ventanas temporales estrictas que amplifican urgencia. Este modelo transforma el lanzamiento en evento comunitario que construye hype y establece precio mínimo inicial (floor price) mediante oferta limitada verificable on-chain.

- **Gaming y GameFi**: Los NFTs revolucionan las economías de videojuegos al convertir items, personajes y skins en activos verdaderamente poseídos por jugadores en lugar de licencias revocables controladas por estudios. Juegos como Axie Infinity popularizaron el modelo Play-to-Earn donde actividades de juego generan tokens fungibles intercambiables por dinero fiat, mientras NFTs representan personajes únicos (Axies) con atributos heredables y comercializables. The Sandbox y Decentraland implementan economías virtuales completas donde lands (terrenos), wearables y construcciones son NFTs con utilidad funcional dentro del metaverso. Aavegotchi combina DeFi con gaming mediante NFTs que representan avatares cuyo valor está respaldado por tokens aTokens depositados en Aave, creando mecánicas donde el activo de juego simultáneamente genera rendimiento DeFi. Protocolos como Enjin utilizan ERC-1155 para gestionar inventarios complejos con items fungibles (pociones, munición) y únicos (armas legendarias) en el mismo contrato, reduciendo costos operativos. La interoperabilidad emergente permite que items obtenidos en un juego se utilicen en otros mediante estándares compartidos, aunque la fragmentación técnica y de diseño limita actualmente esta visión.

- **Metaversos y propiedad virtual**: Los metaversos implementan economías digitales persistentes donde NFTs representan propiedad de terrenos virtuales (lands), edificaciones, avatares y objetos con funcionalidad dentro de mundos 3D. Decentraland divide su mapa en parcelas LAND como NFTs ERC-721, permitiendo compraventa, desarrollo y monetización mediante experiencias que atraen visitantes. The Sandbox opera similarmente, con lands que los propietarios pueden poblar con assets creados mediante herramientas visuales sin código, generando ingresos por eventos, juegos o publicidad virtual. El metaverso Otherside de Yuga Labs (creadores de Bored Ape Yacht Club) otorgó acceso prioritario a holders de sus NFTs existentes, demostrando cómo colecciones establecidas extienden utilidad mediante expansión a mundos virtuales. Más allá de especulación inmobiliaria digital, estos espacios experimentan con gobernanza descentralizada donde holders de lands votan sobre reglas del mundo, y economías creativas donde diseñadores venden assets como NFTs a constructores de experiencias. La sostenibilidad requiere tráfico real de usuarios que justifique valoraciones, no solo acumulación especulativa.

- **NFT Lending y liquidez**: El mercado de NFTs enfrenta iliquidez estructural comparado con tokens fungibles: vender un NFT requiere encontrar comprador dispuesto a pagar el precio completo por el activo específico, proceso que puede tomar semanas o meses. NFT lending emerge como solución permitiendo a holders obtener liquidez sin vender, usando NFTs como colateral para préstamos. El modelo peer-to-peer implementado por plataformas como NFTfi conecta prestamistas con prestatarios: un holder publica su NFT especificando cantidad deseada y términos, prestamistas evalúan y ofrecen condiciones, y si ambos aceptan, el NFT queda bloqueado en contrato inteligente hasta que el préstamo se pague con intereses o el prestatario incumpla, cediendo el NFT al prestamista con descuento sobre su valor estimado. El modelo peer-to-protocol implementado por BendDAO y similares utiliza pools de liquidez donde prestamistas depositan capital y prestatarios solicitan préstamos contra NFTs de colecciones aprobadas mediante oráculos de precio que establecen ratios de colateralización, automatizando el proceso sin negociación individual. Este mercado crea nueva utilidad para NFTs al transformarlos en activos productivos que generan rendimiento para prestamistas y liquidez para holders, aunque introduce riesgos de volatilidad de precios y liquidaciones forzadas durante caídas abruptas del mercado.

- **Certificaciones y documentos**: Certificados académicos inmutables, títulos de propiedad tokenizados, credenciales profesionales verificables mediante SBTs. Elimina la necesidad de verificación manual y reduce fraude documental.

- **Membresías y acceso (NFT gating)**: Tokens de acceso a comunidades DAO, beneficios VIP en eventos físicos o digitales, descuentos exclusivos en productos. Los NFTs actúan como llaves programables que otorgan permisos específicos.

- **Música y derechos de autor**: Álbumes exclusivos tokenizados, entradas verificables para conciertos, distribución fraccionada de royalties entre colaboradores. Plataformas como Audius implementan streaming descentralizado donde artistas mantienen control sobre distribución y monetización, mientras protocolos como Royal permiten vender porcentajes de derechos de canciones como NFTs fraccionarios, convirtiendo fans en inversores que reciben parte de regalías generadas por reproducciones y licencias.

Cada aplicación utiliza los mismos estándares técnicos subyacentes (principalmente ERC-721 y ERC-1155) pero aplicados a diferentes contextos económicos y sociales. Este documento se centra en la taxonomía técnica fundamental, no en el catálogo exhaustivo de todas las implementaciones posibles del ecosistema NFT.

**Infraestructura técnica multi-chain**:

Aunque Ethereum popularizó los NFTs mediante ERC-721 y ERC-1155, múltiples blockchains han implementado soporte nativo con diferentes trade-offs entre costo, velocidad y descentralización:

- **Ethereum**: Máxima seguridad y liquidez, pero gas fees elevadas en mainnet. Soluciones L2 como Polygon, Arbitrum y Optimism reducen costos manteniendo compatibilidad.
- **Solana**: Transacciones extremadamente rápidas y baratas mediante su estándar Metaplex, ideal para drops masivos y gaming de alta frecuencia.
- **Flow**: Diseñado específicamente para NFTs y gaming por Dapper Labs, optimizado para experiencias de usuario fluidas sin gas fees visibles.
- **Tezos**: Enfoque eco-friendly con bajo consumo energético mediante Proof of Stake, adoptado por artistas conscientes del impacto ambiental.
- **Binance Smart Chain (BSC)**: Gas económico y compatibilidad EVM, aunque con mayor centralización en validadores.
- **Cosmos e IBC**: Interoperabilidad nativa entre chains mediante Inter-Blockchain Communication, permitiendo NFTs cross-chain sin bridges tradicionales.

La elección de blockchain depende del caso de uso: proyectos de arte de alto valor priorizan seguridad de Ethereum mainnet, mientras gaming necesita throughput de Solana o Flow, y experimentos comunitarios pueden aprovechar costos de BSC o Polygon.

**Consideraciones económicas y costos**:

Crear, transferir y comercializar NFTs implica múltiples costos que varían según la blockchain y el marketplace:

- **Minting (acuñación)**: Gas fees para ejecutar el contrato de creación. Ethereum mainnet puede costar 50-200 USD en periodos de alta demanda, mientras L2s como Polygon reducen esto a centavos. Algunos marketplaces ofrecen lazy minting, donde el NFT se acuña solo cuando se vende, transfiriendo el costo al comprador.
- **Transferencias**: Cada movimiento on-chain consume gas. Blockchains de bajo costo como Solana o Flow minimizan este friction.
- **Comisiones de marketplace**: Plataformas cobran típicamente 2.5-10% sobre cada venta. OpenSea cobra 2.5%, mientras marketplaces curados como SuperRare pueden cobrar hasta 15% a cambio de mayor exposición.
- **Royalties programados**: Los creadores configuran porcentajes (0-10%) que se pagan automáticamente en cada venta secundaria, generando ingresos pasivos continuos. Sin embargo, su enforcement depende del marketplace: algunos como Blur permiten desactivar royalties para competir en precio.
- **Almacenamiento descentralizado**: Aunque el NFT vive on-chain, los metadatos e imágenes suelen almacenarse en IPFS o Arweave. Servicios de pinning como Pinata cobran por mantener archivos disponibles permanentemente.

**Recursos técnicos y educativos**:

Para desarrolladores que desean implementar NFTs, existen múltiples recursos y librerías auditadas:

- **Estándares y especificaciones**: [ERC-721](https://eips.ethereum.org/EIPS/eip-721), [ERC-1155](https://eips.ethereum.org/EIPS/eip-1155) y documentación oficial en [Ethereum.org](https://ethereum.org/en/developers/docs/standards/tokens/).
- **Librerías de contratos**: [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts/) proporciona implementaciones seguras y auditadas de todos los estándares NFT, con extensiones modulares para funcionalidad adicional.
- **Herramientas de análisis**: [CryptoSlam](https://www.cryptoslam.io/) para estadísticas de mercado multi-chain, [Nansen](https://www.nansen.ai/) para analytics avanzado y wallet tracking, [Icy Tools](https://icy.tools/) para detectar drops y tendencias emergentes.
- **Cursos educativos**: [Bit2Me Academy - Curso NFT](https://learn.bit2me.com/cursos/curso-elemental-de-nft/) ofrece introducción completa al ecosistema NFT desde perspectiva técnica y económica.

**Metadatos y almacenamiento descentralizado**:

La arquitectura de NFTs separa el token on-chain de los datos que representa (imagen, video, audio, atributos). El contrato inteligente almacena únicamente un URI (enlace) que apunta a un archivo JSON con los metadatos del NFT, incluyendo descripción, atributos y URL de la imagen o medio principal. Esta separación es necesaria porque almacenar archivos grandes directamente en blockchain resulta prohibitivamente costoso: guardar una imagen de 1MB en Ethereum mainnet costaría decenas de miles de dólares en gas fees.

El método de almacenamiento de metadatos determina crucialmente la inmutabilidad real del NFT:

- **Almacenamiento centralizado (HTTP)**: Si el URI apunta a un servidor tradicional (`https://servidor.com/metadata/123.json`), el propietario del servidor puede modificar o eliminar el contenido arbitrariamente. El NFT on-chain permanece inmutable, pero la imagen y atributos que representa pueden desaparecer o cambiar, rompiendo la promesa de inmutabilidad. Proyectos que utilizan servidores centralizados introducen riesgo de censura, caída del servicio o manipulación post-venta.

- **IPFS (InterPlanetary File System)**: Protocolo de almacenamiento descentralizado que direcciona contenido mediante hash criptográfico en lugar de ubicación. Un URI IPFS (`ipfs://QmX...`) identifica contenido por su huella digital: cualquier modificación cambia el hash, garantizando que el contenido vinculado al NFT no puede alterarse silenciosamente. Sin embargo, IPFS requiere que al menos un nodo mantenga el archivo disponible (pinning). Sin servicios de pinning pagos como Pinata, Infura o NFT.Storage, el contenido puede volverse inaccesible si ningún nodo lo almacena.

- **Arweave**: Blockchain especializada en almacenamiento permanente mediante pago único. Los datos subidos a Arweave están diseñados para permanecer accesibles indefinidamente mediante incentivos económicos que recompensan nodos por almacenar históricos completos. Ofrece mayor garantía de permanencia que IPFS pero con costos iniciales más altos.

- **On-chain completo**: Algunos proyectos (como Autoglyphs o ciertas colecciones generativas) almacenan todos los metadatos y lógica de generación de imagen directamente en el contrato inteligente. Esto garantiza inmutabilidad absoluta y disponibilidad permanente mientras exista la blockchain, pero limita severamente complejidad y tamaño del contenido debido a costos prohibitivos.

La elección de almacenamiento refleja compromiso entre costo, descentralización y garantías de permanencia. Proyectos serios priorizan IPFS o Arweave para metadatos críticos, mientras experimentos o drops masivos pueden optar por soluciones centralizadas asumiendo riesgos de centralización.

**Riesgos y consideraciones de seguridad**:

Los NFTs, aunque inmutables on-chain, enfrentan vectores de riesgo específicos:

- **Metadata centralizada**: Si los metadatos se almacenan en servidores tradicionales (no IPFS/Arweave), el creador puede modificar o eliminar imágenes/atributos, rompiendo la promesa de inmutabilidad. Este riesgo es particularmente relevante para NFTs de alto valor donde la imagen o atributos determinan el precio.
- **Contratos maliciosos**: Proyectos fraudulentos pueden incluir funciones ocultas que permiten robar NFTs o bloquear transferencias (honeypot contracts). Auditorías y verificación del código son esenciales.
- **Phishing y wallet draining**: Ataques que engañan a usuarios para firmar transacciones maliciosas que transfieren todos sus NFTs. La educación sobre seguridad de wallets es crítica.
- **Royalties no garantizadas**: Aunque configurables on-chain, su pago depende de que el marketplace lo honre. Algunos competidores las eliminan para atraer traders.
- **Floor price manipulation**: En colecciones con baja liquidez, grandes holders pueden manipular el precio mínimo (floor) mediante wash trading o ventas coordinadas.

La diligencia debida (verificar contratos, almacenamiento de metadata, reputación del equipo, y liquidez de mercado) es fundamental antes de adquirir NFTs de alto valor.

## Interoperabilidad con las finanzas tradicionales

La convergencia entre activos digitales y el sistema financiero tradicional marca un hito crucial en la evolución del ecosistema blockchain. Durante mucho tiempo, ambos sistemas coexistieron de manera paralela, con interacciones limitadas. Sin embargo, el crecimiento del espacio cripto y el interés cada vez mayor por parte de instituciones financieras han generado una necesidad apremiante de construir puentes que permitan una integración técnica y regulatoria efectiva.

Esta interoperabilidad enfrenta desafíos significativos. Por un lado, las transacciones en blockchain son irreversibles por diseño, mientras que los sistemas bancarios tradicionales permiten cancelaciones y devoluciones. Además, las direcciones de criptomonedas operan bajo un modelo de seudoanonimato, lo que contrasta con los estrictos requisitos de identificación (KYC) que exigen las entidades financieras reguladas. También existen diferencias en los tiempos de liquidación: las blockchains procesan transacciones en minutos u horas, incluso durante fines de semana o festivos, mientras que las transferencias bancarias internacionales pueden tardar días hábiles. A esto se suma la diversidad de marcos regulatorios en cada jurisdicción y las diferencias fundamentales en los modelos de confianza: las blockchains confían en la criptografía y el consenso distribuido, mientras que las finanzas tradicionales se basan en instituciones centralizadas y marcos legales.

Un punto de tensión clave radica en la naturaleza abierta y sin permiso de las blockchains públicas frente a los sistemas financieros tradicionales, que requieren acceso regulado. Las redes blockchain permiten que cualquier persona con conexión a internet participe sin necesidad de aprobación institucional. Esto puede parecer trivial para quienes tienen acceso al sistema bancario en regiones como Europa o Estados Unidos, pero representa una herramienta esencial de inclusión financiera para millones de personas en países con sistemas financieros restrictivos, inestables o controlados por regímenes autoritarios. En contextos donde existen controles de capital estrictos, hiperinflación o congelación arbitraria de cuentas bancarias, las criptomonedas ofrecen una vía para preservar valor y realizar transacciones sin intermediarios. Por el contrario, las rampas fiat reguladas que conectan el mundo cripto con los bancos tradicionales imponen barreras como la necesidad de documentación de identidad, residencia en jurisdicciones específicas y cumplimiento de requisitos KYC, lo que deja fuera a quienes no pueden acceder a estos servicios debido a limitaciones estructurales o políticas.

Superar estas tensiones requiere un enfoque equilibrado que combine innovación técnica y evolución regulatoria. Es necesario reconocer las fortalezas únicas de cada sistema y construir puentes que permitan una integración efectiva sin comprometer el carácter abierto y sin permiso que hace de la blockchain una herramienta poderosa para la inclusión financiera global.

**Estándar ISO 20022**:

El estándar ISO 20022 emerge como pieza fundamental en esta integración. Este protocolo establece un lenguaje común de mensajería para transferencias financieras, permitiendo que diferentes instituciones bancarias a nivel global intercambien información de forma estandarizada y estructurada. La relevancia de ISO 20022 para criptomonedas radica en que facilita la integración directa con infraestructura bancaria existente sin necesidad de traducciones o adaptadores complejos.

Algunas criptomonedas han adoptado este estándar en su diseño arquitectural. Ripple, por ejemplo, implementa compatibilidad ISO 20022 en su protocolo de consenso y sistema de mensajería, aunque paradójicamente su token nativo XRP no necesariamente cumple todos los requisitos del estándar en su implementación técnica. IOTA también ha incorporado soporte para ISO 20022, posicionándose estratégicamente para casos de uso que requieren interoperabilidad con sistemas de pago tradicionales.

SWIFT ya ha adoptado ISO 20022 como su estándar de mensajería desde 2022, en un proceso de migración que finaliza en 2025. Adicionalmente, está explorando la incorporación de tecnología de registro distribuido mediante APIs, señalando una convergencia entre sistemas de mensajería tradicionales y blockchain.

**Las stablecoins**:

Representan quizás el mecanismo de interoperabilidad más exitoso y ampliamente adoptado hasta la fecha. Al mantener paridad con monedas fiat como el dólar, el euro o el yen, estas criptomonedas funcionan como puentes naturales entre economías tradicionales y descentralizadas. Un usuario puede convertir dólares en USDC mediante un exchange centralizado, operar en protocolos DeFi con la liquidez resultante, y eventualmente retirar a su cuenta bancaria tradicional. Este flujo, aunque aparentemente simple, involucra múltiples capas de interoperabilidad técnica y regulatoria. Los emisores de stablecoins deben mantener cuentas en bancos tradicionales para respaldar sus tokens, someterse a auditorías regulares y cumplir con normativas de prevención de blanqueo de capitales, creando un punto de conexión formal entre ambos sistemas.

**Wrapped tokens**:

Los wrapped tokens constituyen otra innovación importante para la interoperabilidad entre diferentes blockchains y entre cripto y activos tradicionales. Wrapped Bitcoin en Ethereum, por ejemplo, permite utilizar el valor de Bitcoin dentro del ecosistema DeFi de Ethereum sin abandonar la red. Este mecanismo se ha extendido a activos tradicionales, con proyectos que tokenizan acciones, commodities y bonos, permitiendo su comercio en redes blockchain mientras mantienen exposición al activo subyacente tradicional. La estructura técnica generalmente involucra custodios que mantienen el activo original mientras emiten tokens equivalentes en blockchain, creando un puente entre registros tradicionales y descentralizados.

**Rampas on-ramp y off-ramp fiat**:

Representan la infraestructura crítica que permite a usuarios comunes acceder al ecosistema cripto desde el sistema bancario tradicional. Exchanges centralizados como Coinbase, Kraken o Binance operan como instituciones financieras reguladas en múltiples jurisdicciones, manteniendo relaciones bancarias que permiten depósitos y retiros en moneda fiat.

Servicios especializados como Ramp, MoonPay o Wyre se han enfocado específicamente en facilitar estas conversiones de forma embebida en aplicaciones descentralizadas, permitiendo que usuarios compren criptomonedas directamente con tarjetas bancarias o transferencias sin salir de la aplicación que están utilizando.

Los custodios regulados han emergido como actores esenciales en la interoperabilidad institucional. Empresas como Coinbase Custody, BitGo o Anchorage Digital ofrecen servicios de custodia que cumplen con requisitos regulatorios bancarios tradicionales mientras manejan activos digitales. Esto permite que fondos de pensiones, family offices y otras instituciones financieras tradicionales inviertan en criptomonedas sin violar sus mandatos fiduciarios ni requisitos de custodia. Estos custodios implementan controles similares a bancos tradicionales, incluyendo seguros, auditorías externas y segregación de activos, creando un puente de confianza entre ambos mundos.

**CBDC**:

Las monedas digitales de bancos centrales o CBDCs representan potencialmente la forma más profunda de interoperabilidad entre finanzas tradicionales y tecnología blockchain. Varios bancos centrales están explorando o implementando versiones digitales de sus monedas nacionales utilizando tecnología de registro distribuido. China con el yuan digital, el Banco Central Europeo con el euro digital en fase de investigación, y múltiples iniciativas en países como Bahamas, Nigeria o Suecia demuestran que las autoridades monetarias reconocen la inevitabilidad de la convergencia. Estas CBDCs, cuando se implementen completamente, podrían permitir interoperabilidad directa entre dinero soberano digital y criptomonedas privadas, aunque bajo marcos regulatorios estrictos.

## Principales criptomonedas y su categorización

**Commodity y reserva de valor: Bitcoin**:

Bitcoin ocupa una posición única en esta taxonomía. No es un security token ni un utility token en sentido estricto, sino que la mayoría de jurisdicciones lo consideran una commodity o bien digital, similar a materias primas como el oro. Su función principal es servir como reserva de valor descentralizada.

**La utilidad del ordenador mundial: Ethereum**:

Ethereum, por su parte, funciona como utility token al permitir el pago de comisiones de red y la ejecución de contratos inteligentes, pero también ha sido clasificado como commodity por algunas autoridades regulatorias.

Desde Ethereum han surgido numerosos ecosistemas alternativos que compiten o complementan su funcionalidad, incluyendo Polkadot con su arquitectura de parachains donde cada cadena paralela tiene su propio token nativo, así como Cardano, Solana y Cosmos, cada uno con sus propios enfoques técnicos y filosóficos.

**Tokens de gobernanza y protocolos DeFi**:

Habilitados por la infraestructura del ordenador mundial de Ethereum, los tokens de gobernanza como UNI (Uniswap), AAVE, COMP (Compound) y MKR (MakerDAO) otorgan derechos de voto sobre protocolos descentralizados. Estos tokens permiten a sus poseedores participar en decisiones que afectan el funcionamiento y evolución de los protocolos DeFi correspondientes.

**Memecoins y fenómenos culturales**:

Dogecoin (DOGE) como criptomoneda nativa y Shiba Inu (SHIB) como token en Ethereum ejemplifican cómo factores culturales y comunitarios pueden generar valoraciones significativas independientemente de la utilidad técnica. Estos proyectos demuestran la importancia de narrativas y adopción social en el ecosistema cripto.

**Arte digital y NFTs**:

Habilitados por la programabilidad de Ethereum y sus competidores, los NFTs han creado un mercado para arte digital único, coleccionables y utilidades como NFT gating. Proyectos en blockchains como Ethereum, Solana y Polygon han expandido las posibilidades del arte y propiedad digital verificable.

**Anclaje a la deuda de EEUU: stablecoins**:

Las stablecoins merecen mención especial por su importancia en el ecosistema. USDT, USDC y DAI son las más utilizadas, cada una con diferentes mecanismos de respaldo y descentralización. Mientras USDT y USDC están respaldadas por reservas centralizadas de dólares, DAI utiliza un sistema de colateralización descentralizada mediante contratos inteligentes.

**XRP y los sistemas de pago transfronterizos**:

XRP representa una categoría especializada enfocada en facilitar pagos internacionales eficientes. Su posición regulatoria ha sido objeto de controversia, especialmente tras el litigio con la SEC estadounidense. Stellar (XLM) opera en un espacio similar, facilitando transferencias de dinero transfronterizas con enfoque en inclusión financiera y mercados emergentes.

**Privacidad y fungibilidad: monedas anónimas**:

Monero (XMR) y Zcash (ZEC) representan la categoría de criptomonedas centradas en la privacidad, utilizando tecnologías como [ring signatures](https://en.wikipedia.org/wiki/Ring_signature) y [zk-SNARKs](https://academy.bit2me.com/que-son-las-pruebas-zk-snark/) para ocultar detalles de transacciones. Estas monedas enfrentan presión regulatoria creciente debido a preocupaciones sobre su uso en actividades ilícitas.

## El token como herramienta económica y de coordinación

Más allá de las clasificaciones regulatorias y técnicas, los tokens funcionan como herramientas fundamentales que habilitan dos funciones económicas y sociales críticas en ecosistemas descentralizados: la captura de valor y el lanzamiento de proyectos, y la participación en economías de propiedad compartida. Comprender estas dimensiones resulta esencial para evaluar la sostenibilidad, viabilidad y potencial de cualquier proyecto blockchain.

el token suele tener tres funciones principales:

    Gobernanza: Es como una acción que te da derecho a voto. Si el proyecto quiere cambiar una regla, los dueños de los tokens votan.

    Utilidad (Utility): El token es la "llave" para usar un servicio. Sin el token, no puedes entrar a la plataforma o pagar sus funciones.

    Recompensa: Se le da a quien ayuda a que la red funcione (seguridad, datos, contenido).

   el valor, ese algo abstracto que hace subir la oferta y demanda por uso y no humo y existe metricas chulas como TVL

### Token como captura de valor y lanzamiento

Los tokens permiten a proyectos descentralizados capturar valor generado por su red y distribuirlo entre participantes de formas imposibles en estructuras corporativas tradicionales. Simultáneamente, funcionan como mecanismo de financiación que permite recaudar capital para desarrollo sin depender de venture capital tradicional ni estructuras societarias convencionales.

**Mecanismos de captura de valor**:

Los [tokenomics](https://academy.bit2me.com/que-es-tokenomics-economia-tokens/) o economía del token definen cómo un protocolo vincula su éxito operativo con el valor de su activo nativo. A diferencia de acciones corporativas tradicionales donde el valor deriva de participación en beneficios futuros, los tokens implementan mecanismos diversos que crean presión deflacionaria, generan rendimientos o incrementan utilidad conforme crece la red.

El mecanismo de quema o burning constituye una de las estrategias más directas de captura de valor. Protocolos como Ethereum después de EIP-1559 queman parte de las comisiones de transacción, reduciendo la oferta circulante del token conforme aumenta la actividad de red. Binance implementa quemas trimestrales de BNB basadas en volumen de trading en su exchange, creando escasez programada vinculada al uso del ecosistema. MakerDAO quema tokens MKR cuando el protocolo DAI genera beneficios mediante tasas de estabilidad, convirtiendo el éxito del stablecoin en reducción de oferta del token de gobernanza.

Los modelos de staking para rendimiento permiten que holders bloqueen tokens a cambio de recompensas, generalmente provenientes de comisiones del protocolo o emisión inflacionaria controlada. Ethereum 2.0 requiere que validadores depositen 32 ETH para participar en consenso, recibiendo recompensas por validación de bloques y comisiones de transacción. Protocolos DeFi como Curve permiten bloquear tokens CRV para recibir parte de las comisiones generadas por el DEX, alineando incentivos entre holders y liquidez proveedores.

La distribución de comisiones del protocolo crea flujos de valor directo hacia token holders. SushiSwap distribuye porcentaje de comisiones de trading a holders de xSUSHI, convirtiendo el token de gobernanza en activo generador de rendimiento proporcional al volumen del DEX. GMX reparte 30% de comisiones generadas por su exchange perpetuo entre holders que hacen staking de GMX, creando modelo donde mayor volumen de trading genera mayores rendimientos para participantes.

La utilidad creciente del token vinculada a adopción de la red representa otro mecanismo potente. Chainlink utiliza LINK para pagar servicios de oráculos, donde mayor adopción de contratos inteligentes que requieren datos externos incrementa demanda orgánica del token. Filecoin usa FIL para pagar almacenamiento descentralizado, vinculando directamente utilidad del token con crecimiento de demanda de almacenamiento en la red.

Los modelos de ve-tokenomics (vote-escrowed) implementados inicialmente por Curve Finance crean presión deflacionaria mediante bloqueos largos. Usuarios que bloquean CRV por hasta cuatro años reciben veCRV, obteniendo mayor poder de voto en gobernanza y mayores recompensas de staking. Este modelo incentiva compromiso largo plazo, reduciendo presión vendedora y alineando participantes con éxito futuro del protocolo.

**Lanzamiento y distribución inicial**:

La forma en que un proyecto lanza y distribuye su token determina profundamente su descentralización, legitimidad regulatoria y alineación de incentivos iniciales.

Las ICOs (Initial Coin Offerings) dominaron entre 2017-2018, permitiendo que cualquiera comprara tokens de proyectos en fase temprana. Ethereum recaudó aproximadamente 18 millones de dólares en su ICO de 2014 vendiendo ETH directamente a participantes globales. Sin embargo, la facilidad de lanzamiento generó numerosos proyectos fraudulentos, promoviendo intervención regulatoria de la SEC que clasificó muchas ICOs como ventas de securities no registradas.

Los IDOs (Initial DEX Offerings) surgieron como alternativa descentralizada donde proyectos lanzan tokens directamente en exchanges descentralizados, permitiendo liquidez inmediata y acceso sin intermediarios centralizados. Plataformas como Uniswap, PancakeSwap o Raydium facilitan estos lanzamientos, aunque frecuentemente generan alta volatilidad inicial y riesgo de manipulación de precios por bajo capital inicial.

El framework SAFT, como discutimos anteriormente, intenta resolver ambigüedad regulatoria vendiendo inicialmente a inversores acreditados bajo regulación de securities, entregando tokens funcionales tras lanzamiento de red. Filecoin y Tezos utilizaron este modelo, aunque su efectividad legal permanece debatida.

Los airdrops representan distribución gratuita de tokens a usuarios existentes de protocolos relacionados o participantes tempranos. Uniswap distribuyó 400 UNI a cada dirección que había usado el DEX antes de septiembre 2020, premiando adopción temprana y creando comunidad descentralizada de holders. Este modelo democratiza acceso pero puede generar holders sin compromiso real que venden inmediatamente.

Las ventas privadas a venture capital mantienen predominancia en proyectos bien financiados. Inversores institucionales reciben tokens con descuento y periodos de vesting, financiando desarrollo a cambio de participación significativa. Solana, Avalanche y múltiples layer-1 alternativos recaudaron decenas de millones mediante ventas privadas, aunque esto concentra propiedad inicial en pocas manos institucionales.

Los modelos de fair launch intentan democratizar distribución eliminando ventas privadas, pre-mines o asignaciones a fundadores antes del lanzamiento público. Yearn Finance distribuyó YFI exclusivamente mediante farming sin pre-mine ni venta privada, creando percepción de legitimidad y descentralización genuina. Sin embargo, este modelo dificulta financiar desarrollo pre-lanzamiento y puede concentrar tokens en primeros adoptantes técnicamente sofisticados.

### Token de participación y Ownership Economy

Los tokens transforman la relación tradicional entre usuarios, contribuidores y plataformas, permitiendo que participantes posean, gobiernen y capturen valor de redes que co-construyen. Este concepto de [Ownership Economy](https://variant.fund/articles/the-ownership-economy-crypto-and-consumer-software/) o economía de propiedad compartida representa un cambio paradigmático donde valor no se extrae hacia accionistas centralizados sino que se distribuye entre stakeholders que contribuyen activamente al ecosistema. Para una perspectiva práctica de implementación en la industria musical, ver [caso de estudio en Loop Fans](https://fortheloveofbands.com/2025/06/11/the-ownership-economy/).

**Alineación de incentivos y coordinación**:

Los tokens resuelven problemas fundamentales de acción colectiva al alinear intereses económicos de participantes diversos. En plataformas Web2 tradicionales, usuarios generan valor (contenido, datos, efectos de red) que captura la empresa propietaria, creando desalineación estructural donde incentivos de la plataforma divergen de usuarios. Los tokens invierten esta dinámica: holders exitosos requieren que la red prospere, incentivando contribuciones que aumenten utilidad colectiva.

Uniswap ejemplifica esta alineación mediante UNI, donde proveedores de liquidez, traders, holders y desarrolladores comparten interés en maximizar volumen de trading y adopción del protocolo. Mayor volumen genera más comisiones para LPs, mayor utilidad para traders, y potencial apreciación para holders, creando círculo virtuoso de crecimiento alineado.

Los protocolos DeFi implementan incentivos por liquidez mediante emisión de tokens a quienes aportan capital. Compound distribuye COMP a usuarios que depositan o toman prestado activos, subsidiando costos iniciales de participación mientras simultáneamente distribuye propiedad del protocolo a usuarios más activos. Este modelo bootstrapping acelera crecimiento convirtiendo usuarios en stakeholders.

**Gobernanza descentralizada y participación**:

Los tokens de gobernanza democratizan decisiones sobre evolución de protocolos, permitiendo que comunidades controlen parámetros críticos sin depender de equipos centralizados. MakerDAO utiliza MKR para votar sobre tipos de colateral aceptados en préstamos DAI, ratios de colateralización y tasas de estabilidad, distribuyendo poder de decisión entre holders globales en lugar de junta directiva centralizada.

La gobernanza on-chain implementa transparencia radical donde propuestas, debates y resultados quedan registrados inmutablemente en blockchain. Compound Governor permite que cualquier holder con suficiente COMP proponga cambios al protocolo, inicie votaciones y ejecute automáticamente código aprobado, eliminando intermediarios en implementación de decisiones colectivas.

Sin embargo, la gobernanza tokenizada enfrenta desafíos reales de participación y concentración de poder. Grandes holders (ballenas) frecuentemente dominan votaciones mientras pequeños holders no participan por costos de informarse y votar que exceden su influencia marginal. Protocolos experimentan con delegación de voto, votación cuadrática y sistemas de reputación para mitigar plutocracias emergentes.

**Contribución y recompensas distribuidas**:

Los tokens permiten que protocolos recompensen contribuciones diversas más allá de capital financiero. Desarrolladores pueden recibir grants en tokens del tesoro comunitario, creadores de contenido obtener propinas tokenizadas de audiencias, y colaboradores tempranos capturar valor mediante airdrops retroactivos.

Gitcoin utiliza modelos de funding cuadrático donde donaciones pequeñas de muchos contribuidores reciben matching multiplicado del tesoro, premiando proyectos con soporte comunitario amplio sobre aquellos con pocos donantes grandes. Este mecanismo incentiva construcción de bienes públicos que benefician al ecosistema completo.

ENS (Ethereum Name Service) distribuyó tokens ENS retroactivamente a usuarios que habían registrado dominios .eth, convirtiendo early adopters en co-propietarios del protocolo. Este modelo premia contribución histórica y alinea futuros usuarios con éxito del sistema que utilizan.

**Modelos cooperativistas digitales**:

La Ownership Economy habilita estructuras cooperativistas donde trabajadores, usuarios y contribuidores poseen colectivamente plataformas que utilizan. Braintrust, plataforma de freelancing descentralizada, distribuye tokens BTRUST a talento y clientes que usan el servicio, permitiendo que participantes capturen valor que tradicionalmente extraen intermediarios como Upwork o Fiverr cobrando comisiones del 20-30%.

PleasrDAO y otras DAOs coleccionistas permiten que comunidades posean colectivamente activos culturales valiosos, democratizando acceso a inversiones previamente reservadas para wealthy collectors. Modelo aplicable más allá de arte: Constitution DAO intentó comprar copia original de la Constitución estadounidense mediante crowdfunding tokenizado, aunque fracasó en subasta.

**Tensiones y desafíos de la Ownership Economy**:

La promesa de propiedad distribuida enfrenta realidades económicas complejas. Muchos proyectos concentran tokens en equipos fundadores y venture capital pese a retórica descentralizada. Reguladores cuestionan si estos modelos constituyen securities no registradas que prometen retornos a inversores pasivos.

La paradoja de coordinación surge cuando comunidades tokenizadas carecen de capacidad de ejecución rápida que caracteriza empresas centralizadas. Debates de gobernanza pueden paralizar decisiones críticas mientras mercados evolucionan aceleradamente. Protocolos exitosos balancean descentralización progresiva con equipos core capaces de ejecutar durante fases tempranas.

La sostenibilidad económica requiere que valor capturado por holders derive de utilidad real del protocolo, no solo especulación o ponzinomics donde early adopters extraen valor de participantes tardíos. Protocolos genuinamente valiosos generan comisiones de uso real que pueden distribuirse sosteniblemente, diferenciándose de esquemas insostenibles que colapsan cuando incentivos artificiales se agotan.

---

Esta relación entre captura de valor, coordinación descentralizada y distribución equitativa determina fundamentalmente la sostenibilidad y legitimidad de proyectos blockchain. El análisis profundo de estos mecanismos es esencial para evaluar protocolos, tema que exploraremos en detalle en la sección sobre [rendimiento del protocolo](./8-2-protocol-performance.md) y donde [DeFi](./6-3-ecosystem-DeFI.md) es fundamental.

---
