# Intents y Solvers en Ethereum

Mover activos entre redes distintas ha sido históricamente uno de los puntos de mayor fricción en el ecosistema Ethereum. Los puentes tradicionales obligan al usuario a conocer qué cadena de origen y destino usa, qué token necesita, cuánto tiempo tardará la transacción y cuánto gas pagará en cada paso. El paradigma de [*intents* y solvers](https://www.paradigm.xyz/2023/06/intents) invierte completamente este modelo: el usuario declara qué quiere conseguir, y una red de agentes especializados —los solvers— compite para satisfacer ese deseo de la forma más eficiente posible.

La idea central es simple pero poderosa. En lugar de construir una transacción técnica paso a paso, el usuario firma un *intent*: una declaración de intención con parámetros como "quiero recibir al menos 500 USDC en Arbitrum a cambio de 0.2 ETH que tengo en Base, y la oferta expira en 5 minutos". Ese intent no es una transacción en sí mismo, sino una promesa condicional que cualquier solver puede cumplir siempre que respete las condiciones pactadas. Esta separación entre "qué quiero" y "cómo se ejecuta" es el núcleo filosófico del paradigma.

## Cómo funcionan los solvers

Un solver es un agente off-chain —generalmente un sistema automatizado operado por un creador de mercado, un protocolo DeFi o un operador especializado— que vigila continuamente los intents que se van publicando. No existe un mempool único y compartido de intents como el de las transacciones: cada protocolo difunde los suyos por su propio canal —el orderbook de CoW Protocol, el feed de subastas de UniswapX, los eventos de depósito de Across—, y el solver sigue cada uno por separado. Cuando detecta un intent que puede satisfacer de forma rentable, construye la transacción o secuencia de transacciones necesarias para cumplirlo y la envía a la blockchain.

La rentabilidad del solver surge del diferencial entre el tipo de cambio que el usuario aceptó como mínimo y el precio real que el solver puede obtener en el mercado. Si el usuario pidió al menos 500 USDC y el solver puede conseguir 502 USDC redirigiendo la liquidez a través de tres protocolos distintos, los 2 USDC de diferencia son su beneficio. Este mecanismo alinea los incentivos: el solver solo actúa si puede cumplir la condición del usuario, y compite con otros solvers para ofrecer la mejor ejecución posible.

La red de solvers introduce una dinámica de competencia que, en la práctica, beneficia al usuario final. Cuando múltiples solvers ven el mismo intent, tienden a mejorar sus ofertas para ganar la ejecución, lo que aproxima el resultado al precio de mercado real. Es similar a cómo los agregadores de vuelos compiten para mostrarte la tarifa más baja, pero automatizado y ejecutado criptográficamente.

## La relación con los puentes tradicionales

Los puentes clásicos como [Hop Protocol](https://hop.exchange/) o [Stargate](https://stargate.finance/) resuelven el problema técnico de mover activos entre cadenas, pero trasladan toda la complejidad al usuario: este debe decidir qué puente usar, aprobar contratos manualmente, esperar períodos de confirmación que pueden ser largos y gestionar tokens intermedios. Los intents abstraen exactamente esa capa de complejidad.

Un solver puede usar internamente cualquier combinación de puentes, protocolos de liquidez o posiciones propias para cumplir un intent. El usuario no sabe —ni necesita saber— si su ETH viajó por Across, si el solver tenía liquidez propia en Arbitrum o si se usaron tres saltos intermedios. El contrato de liquidación solo verifica que el usuario recibió el mínimo pactado en la dirección y cadena especificadas.

Esto tiene una consecuencia importante para la experiencia de usuario: el *tiempo de finalidad percibido* se reduce drásticamente. Los solvers que actúan como *filler* —el rol que ERC-7683 define para quien ejecuta la orden, como hace Across— suelen adelantar los fondos con su propia liquidez en el destino y recuperan los suyos después usando el puente en segundo plano. El usuario recibe sus tokens en segundos, aunque el settlement criptográfico completo tarde minutos.

## Infraestructura de referencia: ERC-7683 y UniswapX

El ecosistema ha convergido en torno a [ERC-7683 (Cross-Chain Intents Standard)](https://eips.ethereum.org/EIPS/eip-7683), un estándar propuesto conjuntamente por Uniswap Labs y Across Protocol que define una interfaz común para que los intents sean interoperables entre diferentes sistemas de solvers. Antes de este estándar, cada protocolo tenía su propio formato de intent, lo que obligaba a los solvers a implementar integraciones separadas para cada uno.

[UniswapX](https://uniswap.org/whitepaper-uniswapx.pdf) fue uno de los primeros sistemas de producción a gran escala basados en intents. Introduce un mecanismo de subasta donde el precio mínimo aceptado por el usuario decrece suavemente con el tiempo durante la ventana de validez del intent, incentivando a los solvers a ejecutar rápido para capturar el mejor diferencial antes de que la competencia lo haga. Este mecanismo de "Dutch auction" se ha convertido en un patrón de diseño común en el ecosistema.

[Across Protocol](https://across.to/) va un paso más allá especializándose exclusivamente en intents cross-chain, con una red de fillers —el rol que define ERC-7683— optimizada para detectar y ejecutar transferencias entre L2s. Su arquitectura separa el settlement (que ocurre en Ethereum mainnet como capa de liquidación de confianza) de la ejecución rápida en las L2s, combinando la seguridad de L1 con la velocidad de L2.

## La conexión con Account Abstraction y EIP-7702

El paradigma de intents adquiere una nueva dimensión combinado con [EIP-7702](https://eips.ethereum.org/EIPS/eip-7702) y Account Abstraction. Cuando una EOA delega su código a un contrato inteligente —una delegación que queda activa hasta que el usuario la revoca con otra autorización firmada, no algo que caduque por sí solo— es posible que el propio contrato de intent gestione autorizaciones granulares: el usuario aprueba una sola vez que un solver puede mover hasta X cantidad de un token durante los próximos 30 minutos, y todos los intents dentro de esos parámetros se ejecutan sin firmas adicionales. Ese límite de 30 minutos no lo impone EIP-7702, sino la lógica del contrato al que la cuenta delega.

Las *session keys* —claves temporales con permisos limitados— son la consecuencia natural. Un usuario puede autorizar a una interfaz como [Uniswap](https://uniswap.org/) para que gestione intents de swap durante una sesión de trading, sin que cada operación individual interrumpa la experiencia con una ventana de firma. La seguridad se mantiene porque los permisos son estrictamente limitados en cantidad, token y tiempo.

## Riesgos y limitaciones

La abstracción que ofrecen los intents no elimina todos los riesgos, solo los redistribuye. El principal nuevo vector es la confianza en los solvers: si el sistema no tiene suficiente competencia, un solver monopólico podría ejecutar con peor precio del posible sin que el usuario lo detecte fácilmente. Los diseños basados en subastas mitigan esto, pero no lo eliminan completamente en mercados poco líquidos.

También existe el riesgo de censura selectiva: un solver puede decidir ignorar ciertos intents si considera que son poco rentables o si hay presión regulatoria para no procesar ciertos tipos de transacciones. La descentralización de la red de solvers es, por tanto, un factor de salud del sistema tan importante como la descentralización del protocolo subyacente.

Finalmente, la complejidad se traslada a los solvers, que deben gestionar liquidez en múltiples cadenas, monitorizar precios en tiempo real y ejecutar transacciones bajo condiciones de competencia. Esta complejidad operativa tiende a concentrar el mercado de solvers en pocos actores con los recursos técnicos y financieros para participar eficientemente, lo que puede crear puntos centralizados de facto aunque el protocolo sea formalmente descentralizado.

> Para entender cómo esta abstracción se manifiesta en la experiencia del usuario final, consulta [experiencia de usuario en Web3](../../101/8-1-user-experience.md).
