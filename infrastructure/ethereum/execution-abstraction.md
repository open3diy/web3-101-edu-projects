# Abstracción de Ejecución en Ethereum

Este documento describe una capa **distinta** del stack clásico de **Account Abstraction**. Mientras Account Abstraction se centra en **cómo valida, firma, paga y ejecuta una cuenta**, la **Abstracción de Ejecución** se centra en **cómo se consigue el resultado final para el usuario**, incluso cuando este ya no controla directamente la ruta, la red, el pagador del gas o el canal exacto de ejecución.

Dicho de otra forma:

- **Account Abstraction** responde a: *¿cómo funciona la cuenta?*
- **Execution Abstraction** responde a: *¿cómo se logra el resultado que quiere el usuario?*

Este cambio de modelo es importante porque buena parte de la UX moderna de Ethereum ya no gira solo en torno a wallets y firmas, sino a sistemas que abstraen la propia ejecución: **[relayers](https://pixelplex.io/glossary/relayer/), bundlers, paymasters, solvers, rutas cross-chain e infraestructuras de settlement**.

Mover activos entre redes distintas ha sido históricamente uno de los puntos de mayor fricción en el ecosistema Ethereum. Los puentes tradicionales obligan al usuario a conocer qué cadena de origen y destino usa, qué token necesita, cuánto tiempo tardará la transacción y cuánto gas pagará en cada paso. El paradigma de [*intents* y solvers](https://www.paradigm.xyz/2023/06/intents) invierte completamente este modelo: el usuario declara qué quiere conseguir, y una red de agentes especializados —los solvers— compite para satisfacer ese deseo de la forma más eficiente posible.

La idea central es simple pero poderosa. En lugar de construir una transacción técnica paso a paso, el usuario firma un *intent*: una declaración de intención con parámetros como "quiero recibir al menos 500 USDC en Arbitrum a cambio de 0.2 ETH que tengo en Base, y la oferta expira en 5 minutos". Ese intent no es una transacción en sí mismo, sino una promesa condicional que cualquier solver puede cumplir siempre que respete las condiciones pactadas. Esta separación entre "qué quiero" y "cómo se ejecuta" es el núcleo filosófico del paradigma.

## Cómo funcionan los solvers

Un solver es un agente off-chain —generalmente un sistema automatizado operado por un creador de mercado, un protocolo DeFi o un operador especializado— que monitoriza continuamente el flujo de intents publicados en una red de difusión (*mempool* de intents). Cuando detecta un intent que puede satisfacer de forma rentable, construye la transacción o secuencia de transacciones necesarias para cumplirlo y la envía a la blockchain.

La rentabilidad del solver surge del diferencial entre el tipo de cambio que el usuario aceptó como mínimo y el precio real que el solver puede obtener en el mercado. Si el usuario pidió al menos 500 USDC y el solver puede conseguir 502 USDC redirigiendo la liquidez a través de tres protocolos distintos, los 2 USDC de diferencia son su beneficio. Este mecanismo alinea los incentivos: el solver solo actúa si puede cumplir la condición del usuario, y compite con otros solvers para ofrecer la mejor ejecución posible.

La red de solvers introduce una dinámica de competencia que, en la práctica, beneficia al usuario final. Cuando múltiples solvers ven el mismo intent, tienden a mejorar sus ofertas para ganar la ejecución, lo que aproxima el resultado al precio de mercado real. Es similar a cómo los agregadores de vuelos compiten para mostrarte la tarifa más baja, pero automatizado y ejecutado criptográficamente.

## La infraestructura cross-chain que los solvers usan internamente

Antes de que existieran los intents, el usuario tenía que manejar directamente las herramientas cross-chain: elegir el bridge, comparar rutas, aprobar cada paso. Los intents no eliminaron esas herramientas —siguen existiendo y funcionando—, sino que transfirieron esa responsabilidad al solver. El usuario firma una promesa condicional y el solver decide qué combinación de bridges, pools y rutas usar para cumplirla. Entender qué herramientas tiene disponibles el solver ayuda a entender qué puede optimizar.

**Bridges de mensajería nativa** son el transporte más básico: mueven un activo de cadena A a cadena B usando el mecanismo oficial del rollup, como [Arbitrum Bridge](https://bridge.arbitrum.io/) o [Optimism Gateway](https://app.optimism.io/bridge). Ofrecen la máxima seguridad pero son lentos —hasta 7 días para salir de un optimistic rollup hacia L1 debido al período de desafío—. Un solver casi nunca los usa para ejecución rápida, pero puede usarlos en segundo plano para reequilibrar su propia liquidez sin coste de urgencia.

**Bridges de liquidez** como [Hop Protocol](https://hop.exchange/), [Across Protocol](https://across.to/) o [Stargate](https://stargate.finance/) resuelven la latencia adelantando fondos desde una pool de liquidez en el destino y recuperando el capital después mediante el bridge oficial. El resultado llega en 1-3 minutos, con un fee de entre 0,3% y 0,5%. Son la herramienta habitual de los solvers para transferencias cross-chain rápidas: el solver adelanta sus propios fondos al usuario casi de inmediato y recupera los suyos a través del bridge de liquidez en segundo plano.

**Agregadores de rutas** como [Socket](https://socket.tech/), [LI.FI](https://li.fi/) o [Bungee](https://bungee.exchange/) no mueven activos directamente: comparan en tiempo real las rutas disponibles entre múltiples bridges y devuelven la opción más barata, rápida o segura según el criterio elegido. Antes de los intents, el usuario consultaba un agregador para no tener que comparar bridges manualmente. Con intents, el solver hace el mismo trabajo internamente —y va un paso más allá, porque no solo elige la mejor ruta estática sino que puede ajustar la ejecución según las condiciones del mercado en ese momento.

**Plataformas de swap cross-chain** como [Jumper Exchange](https://jumper.exchange/) o [Rango Exchange](https://rango.exchange/) combinan bridge y swap en una sola operación: el usuario puede pedir "quiero cambiar USDC en Polygon por ETH en Arbitrum" y la plataforma compone la ruta completa —bridge y DEX— ejecutable con una sola firma. Es la experiencia más parecida a los intents desde el punto de vista del usuario, pero con una diferencia fundamental: la plataforma elige una ruta y el usuario la aprueba o rechaza. No hay competencia entre ejecutores. Con intents, múltiples solvers compiten en tiempo real para ofrecer el mejor resultado dentro de los límites que el usuario firmó, sin que el usuario vea ni apruebe ninguna ruta concreta.

**Agregación integrada en wallets** representa un paso intermedio que a menudo se omite en la narrativa de intents pero que ha tenido un impacto masivo en la experiencia real de millones de usuarios. En lugar de que el usuario visite una web de bridge externa, son las propias wallets las que integran la agregación de bridges y DEXs directamente en su interfaz. El ejemplo más significativo es [MetaMask](https://metamask.io/), que a través de [MetaMask Bridge](https://portfolio.metamask.io/bridge) consulta agregadores como Socket y LI.FI por debajo para presentar al usuario las rutas de bridging disponibles sin salir de la wallet. Combinado con [MetaMask Swaps](https://metamask.io/swaps/) para intercambios dentro de la misma red y [MetaMask Portfolio](https://portfolio.metamask.io/) como panel unificado multichain, una wallet EOA tradicional ofrece hoy una experiencia cross-chain que hace pocos años requería navegar por múltiples webs de terceros. No es un modelo de intents —el usuario sigue aprobando transacciones manualmente, pagando gas explícitamente y eligiendo entre las rutas que la wallet presenta—, pero sí es la primera capa de abstracción de ejecución que el usuario retail experimentó de forma masiva. Para los solvers, este modelo es relevante porque la misma infraestructura de agregación que usan las wallets internamente (Socket, LI.FI) es la que los solvers también consultan, solo que los solvers lo hacen de forma automatizada y compiten entre sí para optimizar el resultado.

Lo que cambia con los intents no es la infraestructura subyacente, sino quién toma las decisiones sobre cómo usarla. El usuario deja de ser el coordinador del flujo y pasa a ser el que define el resultado mínimo aceptable. El solver asume el riesgo de ejecución y captura el diferencial si logra un resultado mejor que el mínimo pactado. El contrato de liquidación solo verifica que el usuario recibió lo acordado, independientemente del camino que tomó el capital.

Esto tiene una consecuencia directa sobre el tiempo percibido: los solvers suelen adelantar fondos con su propia liquidez en el destino y recuperan los suyos después usando el bridge que prefieran. El usuario recibe sus tokens en segundos, aunque el settlement criptográfico completo tarde minutos.

## Infraestructura de referencia: ERC-7683 y UniswapX

El ecosistema ha convergido en torno a [ERC-7683 (Cross-Chain Intents Standard)](https://eips.ethereum.org/EIPS/eip-7683), un estándar propuesto conjuntamente por Uniswap Labs y Across Protocol que define una interfaz común para que los intents sean interoperables entre diferentes sistemas de solvers. Antes de este estándar, cada protocolo tenía su propio formato de intent, lo que obligaba a los solvers a implementar integraciones separadas para cada uno.

[UniswapX](https://uniswap.org/whitepaper-uniswapx.pdf) fue uno de los primeros sistemas de producción a gran escala basados en intents. Introduce un mecanismo de subasta donde el precio mínimo aceptado por el usuario decrece suavemente con el tiempo durante la ventana de validez del intent, incentivando a los solvers a ejecutar rápido para capturar el mejor diferencial antes de que la competencia lo haga. Este mecanismo de "Dutch auction" se ha convertido en un patrón de diseño común en el ecosistema.

[Across Protocol](https://across.to/) va un paso más allá especializándose exclusivamente en intents cross-chain, con una red de solvers optimizada para detectar y ejecutar transferencias entre L2s. Su arquitectura separa el settlement (que ocurre en Ethereum mainnet como capa de liquidación de confianza) de la ejecución rápida en las L2s, combinando la seguridad de L1 con la velocidad de L2.

## La conexión con Account Abstraction y EIP-7702

Para entender cómo encajan los intents con Account Abstraction, conviene distinguir primero dos roles de infraestructura que el ecosistema frecuentemente confunde: bundlers y solvers.

Un bundler es un componente específico de [EIP-4337](https://eips.ethereum.org/EIPS/eip-4337), el estándar de Account Abstraction. Su función es recoger UserOperations —las "pseudo-transacciones" que emiten las smart contract wallets— desde un mempool alternativo y agruparlas en una única transacción real que envía al contrato `EntryPoint` en la blockchain. El bundler no decide qué hacer con los activos del usuario: simplemente actúa como relayer que convierte operaciones de alto nivel en transacciones válidas de Ethereum, cobrando una comisión por el gas. Es análogo a un minero o validador en su función de ordenar y publicar operaciones, pero operando sobre la capa de abstracción de cuentas.

Un solver, en cambio, tiene agencia económica sobre la ejecución: decide cómo cumplir el intent del usuario, qué rutas de liquidez usar y compite activamente para maximizar su propio beneficio dentro de las condiciones aceptadas por el usuario. Mientras el bundler opera a nivel de protocolo sin lógica de negocio, el solver opera a nivel de mercado con estrategia. En la práctica, un mismo operador puede actuar como bundler y como solver simultáneamente, lo que tiende a difuminar la distinción para el usuario final.

El paradigma de intents adquiere una nueva dimensión combinado con Account Abstraction y con [EIP-7702](https://eips.ethereum.org/EIPS/eip-7702). Aquí conviene ser preciso: **EIP-7702 no convierte mágicamente una EOA en una smart contract wallet completa**, sino que introduce un mecanismo por el que una EOA puede **delegar su ejecución a código externo** mediante una designación de código en protocolo. Esto permite que una cuenta tradicional actúe con capacidades programables sin cambiar de dirección.

Sin embargo, esa delegación **no es temporal por diseño**. La representación delegada permanece hasta que se sustituye o se elimina explícitamente. La “temporalidad” que muchas interfaces muestran al usuario —por ejemplo, permisos por sesión o autorizaciones acotadas— no la impone el protocolo base de 7702, sino la lógica del contrato delegado o las políticas de autorización construidas encima.

Cuando una EOA delega a lógica programable, es posible que el propio contrato o la infraestructura asociada gestione autorizaciones granulares: el usuario puede aprobar una vez que cierto flujo puede mover hasta X cantidad de un token durante un tiempo determinado, y múltiples operaciones posteriores pueden ejecutarse dentro de esos límites sin requerir una firma adicional cada vez.

Las [*session keys*](session-keys.md) —autorizaciones programadas en el contrato delegado con permisos acotados en token, cantidad y tiempo— son la consecuencia natural. Un usuario puede autorizar a una interfaz como [Uniswap](https://uniswap.org/) para que gestione intents de swap durante una sesión de trading, sin que cada operación individual interrumpa la experiencia con una ventana de firma. La seguridad se mantiene porque los permisos son estrictamente limitados en cantidad, token y tiempo.

## De Account Abstraction a Execution Abstraction

Hasta hace poco, la abstracción que interesaba al ecosistema era principalmente la **abstracción de cuenta**: cómo conseguir que una cuenta pudiera validar firmas de formas más flexibles, pagar el gas de forma distinta o ejecutar múltiples operaciones en un solo flujo.

Pero la dirección actual del ecosistema apunta a algo más profundo: **abstraer la propia ejecución**.

Esto significa que el usuario ya no controla necesariamente:

- Qué red se usa realmente,
- Qué ruta de liquidez se sigue,
- Qué infraestructura retransmite la operación,
- Qué actor adelanta el capital,
- Ni cómo se produce el settlement final.

La wallet sigue existiendo, pero su papel evoluciona: en lugar de firmar cada operación individual, cada vez más actúa como una **capa de autorización criptográfica** que delega permisos acotados a otros agentes del sistema. La tendencia no es solo autenticar quién eres, sino autorizar qué puede hacerse en tu nombre, con qué límites y durante cuánto tiempo. Desde esta perspectiva, puede decirse que:

- **ERC-4337** abstrae la cuenta.
- **EIP-7702** abstrae parte de la programabilidad de una EOA.
- **Intents** abstrae la descripción del plan de ejecución.
- **Chain Abstraction** abstrae incluso la red donde se liquida el resultado.

Esta evolución mejora radicalmente la experiencia de usuario, pero también plantea una cuestión importante de soberanía: **cuanto más se abstrae la ejecución, menos control explícito tiene el usuario sobre cómo se consigue el resultado final**.

## Riesgos y limitaciones

La abstracción que ofrecen los intents no elimina todos los riesgos, solo los redistribuye. El principal nuevo vector es la confianza en los solvers: si el sistema no tiene suficiente competencia, un solver [monopólico](https://es.wikipedia.org/wiki/Monopolio) podría ejecutar con peor precio del posible sin que el usuario lo detecte fácilmente. Los diseños basados en subastas mitigan esto, pero no lo eliminan completamente en mercados poco líquidos.

También existe el riesgo de censura selectiva: un solver puede decidir ignorar ciertos intents si considera que son poco rentables o si hay presión regulatoria para no procesar ciertos tipos de transacciones. La descentralización de la red de solvers es, por tanto, un factor de salud del sistema tan importante como la descentralización del protocolo subyacente.

Finalmente, la complejidad se traslada a los solvers, que deben gestionar liquidez en múltiples cadenas, monitorizar precios en tiempo real y ejecutar transacciones bajo condiciones de competencia. Esta complejidad operativa tiende a concentrar el mercado de solvers en pocos actores con los recursos técnicos y financieros para participar eficientemente, lo que puede crear puntos centralizados de facto aunque el protocolo sea formalmente descentralizado.

A esto se suma un riesgo menos visible pero más estructural: la pérdida de control explícito por parte del usuario sobre el canal de ejecución. En un stack de Execution Abstraction, la wallet ya no es necesariamente la interfaz soberana desde la que el usuario decide “solo me conecté a Ethereum”; la dApp, el solver o la infraestructura intermedia pueden terminar determinando dónde y cómo se ejecuta realmente la intención firmada.

---
