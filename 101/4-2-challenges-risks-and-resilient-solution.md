# Riesgos y solución resiliente

La seguridad es un aspecto fundamental en cualquier sistema descentralizado. Saber enfrentarse a las amenazas es importante, resolver los ataques es fundamental, pero lo primero y más crítico es conocer los riesgos para poder anticiparlos y mitigarlos antes de que se materialicen.

Los riesgos que amenazan la sostenibilidad de un protocolo descentralizado van mucho más allá de las vulnerabilidades técnicas. Debemos considerar un espectro completo de factores que pueden provocar el colapso del sistema: económicos, sociales, de proyecto y regulatorios. Cada uno de estos vectores puede ser tan destructivo como un exploit en el código, y frecuentemente actúan de forma combinada, amplificando su impacto.

## Riesgos Técnicos y de Ciberseguridad

Los sistemas descentralizados son objetivos constantes de actores maliciosos que buscan explotar vulnerabilidades técnicas para robar fondos, interrumpir servicios o manipular el protocolo. Estos ataques pueden manifestarse de múltiples formas, desde exploits en contratos inteligentes que aprovechan vulnerabilidades, hasta ataques más sofisticados a nivel de red. Pero no solo ataques, bots y snippers están constantemente examinando cualquier situacion de beneficio para beneficiarse, dentro un marco operativo normal.

### Ataques de reentrancy

Los ataques de reentrancy explotan que un contrato puede llamar a código externo antes de actualizar su estado interno. El infame hack de The DAO en 2016 robó $60M usando esta vulnerabilidad. El atacante creó un contrato que, al recibir fondos, llamaba nuevamente a la función de retiro antes de que el balance se actualizara, drenando el contrato repetidamente.

La defensa fundamental es el patrón checks-effects-interactions: primero verificas condiciones, luego actualizas estado interno, y finalmente interactúas con código externo. Bibliotecas como [OpenZeppelin](https://www.openzeppelin.com/contracts) proveen guards que previenen llamadas recursivas automáticamente, eliminando esta clase de vulnerabilidades si se implementan correctamente.

### Flash loan attacks

Los flash loans permiten pedir préstamos masivos sin colateral que deben repagarse en la misma transacción. Los atacantes los usan para manipular precios temporalmente y explotar vulnerabilidades en otros protocolos. Un ataque típico involucra pedir $100M, manipular el precio en un exchange poco líquido, explotar un protocolo de lending que usa ese exchange como oráculo de precios, repagar el préstamo y quedarse con la ganancia, todo en una sola transacción.

La defensa requiere usar oracles resistentes a manipulación como TWAP (Time-Weighted Average Price) de [Uniswap v3](https://docs.uniswap.org/), que promedian precios a lo largo del tiempo en lugar de usar valores instantáneos. También es crítico implementar límites razonables en operaciones que pueden ejecutarse dentro de un solo bloque.

### MEV y front-running

El Maximal Extractable Value (MEV) es el profit que validators pueden extraer reordenando, insertando o censurando transacciones en un bloque. El sandwich attack es el ejemplo clásico: un atacante ve tu transacción en el mempool, ejecuta una compra antes que tú para subir el precio, tu transacción ejecuta al precio inflado, e inmediatamente el atacante vende con ganancia.

En 2023, los validators de Ethereum extrajeron más de $300M en MEV, afectando directamente a usuarios ordinarios que sufren peores precios de ejecución. [Flashbots](https://www.flashbots.net/) desarrolló MEV-Boost para permitir transacciones privadas directamente a builders de bloques. Otros protocolos como [Cowswap](https://cow.fi/) usan batch auctions donde todas las órdenes en un período se ejecutan al mismo precio uniforme, eliminando el beneficio de front-running.

### Descentralización del validator set y ataques 51%

La descentralización del consensus es crítica para resistencia a censura y seguridad. Bitcoin tiene miles de mineros independientes, aunque los pools concentran el hash power: los top 4 pools controlan más del 50% del hashrate, creando riesgo teórico de ataque 51%.

Ethereum post-merge tiene más de 1 millón de validators, pero Lido controla aproximadamente 30% del stake total. Si Lido se comporta maliciosamente o es forzado por reguladores a censurar transacciones, compromete la neutralidad de Ethereum.

El coeficiente de Nakamoto mide cuántas entidades necesitas comprometer para atacar la red. Para Ethereum es aproximadamente 4-5 considerando los grandes staking pools. Para blockchains más pequeñas puede ser tan bajo como 1-2, indicando centralización peligrosa.

Ethereum implementó slashing para desincentiva comportamiento malicioso: validators que firman bloques contradictorios pierden una porción significativa de su stake. El correlation penalty castiga más severamente si muchos validators fallan simultáneamente, desincentivando concentración en infraestructura compartida.

### Auditorías y verificación formal

Las auditorías de smart contracts son esenciales pero no perfectas. Firmas especializadas como [Trail of Bits](https://www.trailofbits.com/), [OpenZeppelin](https://www.openzeppelin.com/security-audits), o [ConsenSys Diligence](https://consensys.io/diligence) revisan el código buscando vulnerabilidades comunes, lógica de negocio incorrecta, o malas prácticas. Sin embargo, las auditorías son snapshots: si modificas el código después, necesitas re-auditar.

Los protocolos serios complementan auditorías con bug bounties en plataformas como [Immunefi](https://immunefi.com/), incentivando a hackers white-hat a reportar bugs en lugar de explotarlos. Los bounties pueden alcanzar millones de dólares para vulnerabilidades críticas.

La verificación formal va más allá de las auditorías tradicionales: usa matemáticas para probar que el código cumple ciertas propiedades bajo todas las condiciones posibles. Herramientas como [Certora](https://www.certora.com/) permiten especificar invariantes que el contrato debe mantener y probar formalmente que ninguna secuencia de transacciones puede violarlas. Por ejemplo, "el total supply de tokens debe siempre igualar la suma de todos los balances individuales".

### Bridges y comunicación cross-chain

Los bridges permiten transferir assets entre blockchains, pero son el vector de ataque más lucrativo en crypto. Ronin Bridge en 2022 perdió $600M cuando atacantes comprometieron 5 de 9 validator keys. Wormhole perdió $320M por un bug en verificación de firmas. Nomad Bridge perdió $190M por un bug que permitió retirar fondos sin prueba válida.

Existen varios modelos de bridges con diferentes trade-offs de seguridad:

Los trusted bridges como WBTC usan custodios centralizados que controlan los fondos bloqueados. Confías en que el custodio mantiene 1:1 backing y no desaparecerá con tu dinero.

Los federated bridges usan un multisig de validadores donde M-of-N deben firmar para aprobar transferencias. Si los validadores se coludían o son hackeados simultáneamente, los fondos pueden robarse.

Los trustless bridges verifican pruebas criptográficas de transacciones en la otra chain, garantizando que realmente ocurrieron sin confiar en intermediarios. Sin embargo, la complejidad de implementar estas verificaciones correctamente crea superficie de ataque masiva.

Los atomic swaps usando Hash Time-Locked Contracts (HTLCs) permiten intercambios completamente trustless: ambas partes bloquean fondos con el mismo secreto criptográfico. Quien revela el secreto primero puede reclamar los fondos de la contraparte, y si nadie revela el secreto antes del timeout, ambos recuperan sus fondos.

Las lecciones de bridges: federated models con pocos validadores son honeypots esperando ser comprometidos. Un solo bug en verificación de proofs puede drenar todo el TVL. Los usuarios deben considerar bridges como componentes de alto riesgo y minimizar exposición, usando solo bridges battle-tested con múltiples auditorías independientes y bug bounties activos.

## Riesgos Económicos

Los sistemas descentralizados deben crear una economía viable alrededor del protocolo para ser sostenibles. Un modelo económico mal diseñado puede colapsar sin necesidad de ataques externos, simplemente por sus propias contradicciones internas o incentivos mal alineados.

El caso de [friend.tech](https://www.friend.tech/) ilustra perfectamente este problema. Esta plataforma de redes sociales Web3 creó un modelo donde los usuarios podían comprar "shares" o acciones de perfiles de creadores. Sin embargo, los incentivos estaban mal alineados desde el inicio, favoreciendo la especulación sobre el uso real de la plataforma. No había suficiente utilidad real más allá del trading de shares, lo que significaba que el modelo dependía exclusivamente de la especulación constante. Cuando la especulación inicial se enfrió y los usuarios comenzaron a buscar valor real, simplemente abandonaron la plataforma. El modelo colapsó porque no creó valor sostenible a largo plazo, solo una burbuja especulativa.

Aún más dramático fue el colapso de [Terra/LUNA](https://www.coindesk.com/learn/the-fall-of-terra-a-timeline-of-the-meteoric-rise-and-crash-of-ust-and-luna/), el caso más conocido donde se explotó el vínculo algorítmico entre ambos tokens. El diseño económico tenía puntos de fallo críticos que permitieron un ataque en espiral que destruyó miles de millones de dólares en cuestión de días. El sistema dependía de que la confianza se mantuviera intacta, pero cuando esta se rompió, el mecanismo algorítmico amplificó la caída en lugar de estabilizarla.

Relacionado con esto están los ataques a incentivos. Los sistemas descentralizados ofrecen recompensas para fomentar la participación, pero agentes maliciosos pueden abusar de estos mecanismos. La explotación de programas de yield farming permite que atacantes acumulen recompensas temporalmente y retiren fondos sin contribuir realmente al sistema. Los llamados "vampire attacks" ocurren cuando nuevos protocolos copian funcionalidades de otros y ofrecen mejores incentivos temporalmente para robar toda su liquidez. Existe también el fenómeno del "mercenary capital", capital que salta constantemente entre protocolos buscando solo las mejores recompensas del momento, sin ningún compromiso real con ningún proyecto.

La clave para evitar estos problemas es diseñar incentivos que promuevan comportamiento a largo plazo y penalicen la extracción de valor sin contribución real al ecosistema.

## Riesgos de Gobernanza y Sociales

Los sistemas descentralizados implementan protocolos de gobernanza para permitir que la comunidad tome decisiones colectivas. Sin embargo, estos mecanismos pueden ser manipulados por participantes maliciosos que buscan beneficio personal.

El ataque Sybil, ampliamente documentado en sistemas distribuidos, consiste en crear múltiples identidades falsas para centralizar el poder de votación y aprobar propuestas maliciosas que beneficien al atacante. Esta es solo una de las formas de manipular la gobernanza. Grandes tenedores de tokens, conocidos como "whales", pueden controlar decisiones simplemente por su poder económico. En casos extremos, hemos visto hostile takeovers donde actores externos compran masivamente tokens de gobernanza específicamente para tomar control del protocolo y dirigirlo según sus intereses.

No todos los problemas de gobernanza vienen de actores maliciosos. A veces, el simple desacuerdo entre participantes honestos puede generar una parálisis por desacuerdos que impide evolucionar el protocolo, dejándolo congelado mientras competidores avanzan. Este fenómeno, conocido como "governance gridlock", puede ser tan dañino como un ataque directo.

Las defensas contra estos ataques incluyen varios mecanismos:

Primero, sistemas de identidad que dificultan crear múltiples cuentas falsas. Por ejemplo, requerir verificación o vincular el poder de voto a participación histórica real en el protocolo.

Segundo, el voto cuadrático, un sistema donde tu poder de voto no crece linealmente con tus tokens. Si tienes 100 tokens, no obtienes 100 votos, sino la raíz cuadrada: 10 votos. Para tener 100 votos necesitarías 10,000 tokens. Esto reduce drásticamente el impacto de las "ballenas" (grandes tenedores), ya que comprar más tokens tiene rendimientos decrecientes en poder de voto.

Tercero, timelocks en las propuestas. Cuando alguien propone un cambio importante, no se ejecuta inmediatamente aunque la votación pase. Hay un período de espera obligatorio, por ejemplo 48 horas, durante el cual la comunidad puede revisar exactamente qué hará la propuesta, detectar intenciones maliciosas, y en casos extremos, salir del protocolo si no están de acuerdo.

Finalmente, diversificar el poder de gobernanza. No concentrar todas las decisiones en un solo tipo de voto, sino distribuir diferentes tipos de control entre diferentes grupos: desarrolladores, usuarios, inversores, cada uno con su propio peso en diferentes tipos de decisiones.

Pero quizás uno de los ataques más insidiosos no viene del código ni de la gobernanza formal, sino de la manipulación de la percepción. De la misma forma que conocemos el FOMO (Fear Of Missing Out, miedo a estar fuera), existe el FUD: Fear, Uncertainty, and Doubt, miedo, incertidumbre y duda.

Podríamos sufrir ataques de coordinación social que provoquen FUD mediante campañas de desinformación en redes sociales, noticias falsas sobre vulnerabilidades o problemas del proyecto, manipulación del sentimiento del mercado para afectar el precio del token, o ataques directos a la reputación de fundadores y miembros clave del equipo. Estos ataques no buscan romper el código, sino romper la confianza, que es el verdadero pilar de cualquier sistema descentralizado.

La mejor defensa contra el FUD es la comunicación transparente y constante con la comunidad, construyendo una relación de confianza basada en hechos verificables y honestidad radical.

## Riesgos de Proyecto y Equipo

Uno de los riesgos más devastadores que puede enfrentar un protocolo descentralizado es que el equipo fundador abandone el proyecto. Este riesgo se amplifica cuando el protocolo no está suficientemente descentralizado, existen dependencias técnicas críticas en el equipo original, la comunidad no está preparada para tomar el control, o no hay mecanismos claros de transición y sucesión.

Las señales de alerta suelen ser evidentes para quienes las buscan. Fundadores vendiendo grandes cantidades de tokens, especialmente si lo hacen de forma discreta o a través de múltiples wallets. Una disminución repentina de la actividad en desarrollo visible en los repositorios de código. Falta de comunicación con la comunidad o ausencia de un roadmap claro y actualizado. Conflictos internos que se vuelven públicos entre miembros del equipo central.

La mitigación de este riesgo requiere múltiples estrategias complementarias. La descentralización progresiva del desarrollo es fundamental, donde cada vez más contribuidores externos puedan mantener el código. El uso de [GitHub](https://github.com/) como repositorio público se ha convertido en el estándar de la industria, no solo porque facilita la colaboración, sino porque garantiza que el código esté permanentemente accesible incluso si el equipo original desaparece. Cualquier desarrollador puede hacer fork del proyecto y continuar su desarrollo.

Pero tener el código disponible no es suficiente si nadie puede entenderlo. La documentación exhaustiva es crítica: no solo comentarios en el código, sino guías completas de arquitectura, decisiones de diseño explicadas, tutoriales de despliegue y mantenimiento. Herramientas como [Read the Docs](https://about.readthedocs.com/) o [GitBook](https://www.gitbook.com/) permiten mantener documentación viva que evoluciona con el proyecto.

La construcción de una comunidad técnicamente capaz es igualmente vital. Esto significa no solo atraer usuarios, sino cultivar contribuidores activos que entiendan profundamente el sistema. Programas de grants para desarrolladores, bug bounties gestionados por plataformas como [Immunefi](https://immunefi.com/), y programas de mentoría que transfieran conocimiento del equipo core a la comunidad son inversiones en la supervivencia a largo plazo del protocolo.

La governance on-chain con controles multifirma distribuidos entre miembros de la comunidad asegura que ninguna persona individual pueda controlar aspectos críticos del protocolo.

¿Qué significa esto en la práctica? Imaginemos que el proyecto tiene una "tesorería" (treasury) con 1 millón de dólares en fondos para desarrollo. En un proyecto centralizado, el CEO podría simplemente transferir ese dinero a su cuenta. Con multifirma, se requieren por ejemplo 5 de 7 firmas para mover fondos. Estas 7 personas son miembros respetados de la comunidad, geográficamente distribuidos, sin relación entre ellos. Para robar los fondos, tendrías que corromper a 5 de ellos simultáneamente, lo cual es extremadamente difícil.

El uso de DAOs con herramientas como [Snapshot](https://snapshot.org/) para votaciones (donde la comunidad propone y vota cambios sin gastar gas) y [Gnosis Safe](https://safe.global/) para administración de fondos (el sistema multifirma que ejecuta las decisiones aprobadas) distribuye el poder efectivamente. La comunidad decide qué hacer con Snapshot, y los guardianes multifirma simplemente ejecutan lo que la comunidad decidió.

Finalmente, la financiación del desarrollo debe estar asegurada más allá del equipo fundador.

La treasury del protocolo (el fondo común del proyecto) debe ser manejada por la comunidad, no por los fundadores. Esto significa que aunque los fundadores se vayan, el dinero para pagar desarrolladores sigue disponible y bajo control comunitario.

Los sistemas de funding continuo son presupuestos recurrentes donde los contribuidores son compensados directamente por el protocolo. Por ejemplo, cada mes el protocolo genera 50,000 dólares en fees, y automáticamente 20,000 van a un fondo para pagar desarrolladores activos. Esto funciona sin necesidad de que nadie "apruebe" los pagos manualmente.

Además existen mecanismos de retroactive public goods funding (financiación retroactiva de bienes públicos), como los implementados por [Optimism](https://round3.optimism.io/). En este modelo, la comunidad vota retrospectivamente para recompensar proyectos que ya demostraron ser útiles. Es como decir "este desarrollador creó una herramienta que todos usamos, démosle una recompensa". Esto incentiva construir cosas útiles aunque no tengas funding inicial.

Todos estos mecanismos garantizan que el desarrollo pueda continuar incluso si los fundadores originales se retiran, porque el dinero y los sistemas de compensación están descentralizados y automatizados.

Pero incluso con un equipo comprometido y una comunidad activa, un protocolo puede fallar por falta de efecto red. Un protocolo puede ser técnicamente sólido, económicamente bien diseñado, y aún así fracasar por no lograr la masa crítica de usuarios necesaria para ser útil.

Este es el clásico problema del huevo y la gallina en Web3. Los usuarios no llegan porque no hay contenido, liquidez, o actividad en el protocolo. Y no hay contenido ni liquidez porque no hay usuarios. Romper este círculo vicioso es uno de los desafíos más difíciles. La competencia con plataformas establecidas que ya tienen millones de usuarios hace aún más difícil atraer a esos primeros adoptantes críticos. Y la fragmentación del ecosistema, con demasiados protocolos similares compitiendo por la misma base de usuarios, divide a la comunidad en lugar de concentrarla.

Sin efecto red, el protocolo no genera suficiente valor para justificar su existencia y mantenimiento. Por eso es crítico enfocarse en estrategias de adopción que generen valor inmediato, incluso para los primeros usuarios, y en casos de uso que resuelvan problemas reales de forma notablemente mejor que las alternativas existentes.

## Riesgos Regulatorios

La relación entre los sistemas descentralizados y los gobiernos es compleja y, en muchos casos, abiertamente hostil. Algunos gobiernos perciben la descentralización como un rival o amenaza directa al control tradicional del sistema financiero y del flujo de información.

Las prohibiciones directas han ocurrido en varios países, con restricciones severas o prohibiciones totales de criptomonedas y sistemas descentralizados. Pero a veces, el daño no viene de prohibiciones explícitas sino de la regulación por incertidumbre. La falta de claridad legal paraliza proyectos que no saben si están operando dentro o fuera de la ley. Los emprendedores se encuentran en un limbo donde lanzar un proyecto puede significar enfrentar consecuencias legales años después, cuando finalmente se aclaren las regulaciones.

Existe también la persecución selectiva, donde las autoridades aplican enforcement agresivo contra ciertos protocolos o fundadores, a veces sin criterios claros o consistentes. Esto crea un ambiente de miedo que inhibe la innovación.

Pero quizás el problema más profundo no es la hostilidad activa, sino la inadecuación estructural. El compliance, los requisitos regulatorios, las normas y controles del sistema financiero tradicional, simplemente no terminan de entender o encajar en la economía de los sistemas descentralizados.

Aplicar regulación financiera tradicional a protocolos autónomos que no tienen una entidad central responsable es conceptualmente problemático. Los requisitos de KYC (Know Your Customer) y AML (Anti-Money Laundering) contradicen los principios fundamentales de privacidad y descentralización que muchos protocolos buscan preservar. La regulación fiscal frecuentemente no contempla la naturaleza única de los tokens, tratándolos como acciones cuando no lo son, o ignorando aspectos cruciales de su utilidad.

El resultado es que, ante la duda, los reguladores tienden a aplicar lo más restrictivo, lo que ha provocado indignación en la comunidad Web3 y un distanciamiento creciente con las autoridades. Muchos proyectos se han visto forzados a relocalizarse en jurisdicciones más amigables o a limitar su acceso geográfico, excluyendo usuarios de ciertos países para evitar problemas legales.

## La Solución: Resiliencia

Existen muchos más riesgos de los que hemos cubierto aquí, y nuevos surgirán constantemente. La historia de Web3 está llena de colapsos que nadie anticipó, de vectores de ataque que parecían imposibles hasta que ocurrieron. Sin embargo, esto nos ayuda a entender que debemos considerar amenazas que van mucho más allá de lo puramente técnico.

El objetivo no es ni puede ser eliminar todos los riesgos. Eso es imposible en cualquier sistema, y más aún en sistemas que operan en ambientes adversarios donde hay incentivos económicos directos para atacarlos. El objetivo es construir sistemas resilientes, capaces de absorber impactos, adaptarse a nuevas amenazas y seguir funcionando a pesar de los ataques.

La resiliencia se construye sobre varios pilares fundamentales. La transparencia radical es quizás el más importante: código completamente opensource que cualquiera pueda auditar, comunicación constante con la comunidad, decisiones tomadas en público con sus razones claramente explicadas. El uso de GitHub como plataforma de desarrollo se ha consolidado como el estándar de facto de la industria Web3, no solo por sus capacidades técnicas, sino porque garantiza que el proyecto pueda sobrevivir independientemente de sus fundadores. Cuando el código es público y cualquiera puede hacer fork, el proyecto se vuelve prácticamente inmortal mientras tenga valor para alguien.

Esta transparencia debe extenderse más allá del código. Imaginemos un proyecto donde los fundadores desaparecen repentinamente. Si todas las decisiones importantes se tomaron a puerta cerrada, la comunidad no sabría por qué se hicieron ciertos cambios, qué problemas se consideraron, o cuál era la visión del proyecto. Estarían perdidos.

Ahora imaginemos el mismo escenario, pero con transparencia radical. Las discusiones de diseño ocurrieron en foros públicos como [Commonwealth](https://commonwealth.im/) o [Discourse](https://www.discourse.org/), donde cualquiera puede leerlas años después. Por ejemplo, alguien propuso cambiar el sistema de recompensas, y en el foro está toda la discusión: pros, contras, alternativas consideradas, por qué se eligió una opción sobre otra. Las finanzas del proyecto están visibles on-chain: cualquiera puede ver cuántos fondos quedan, cómo se han gastado, qué wallets tienen acceso. Las decisiones de gobernanza están registradas permanentemente en la blockchain con el voto de cada participante.

Con toda esta información pública, la comunidad puede simplemente continuar donde el equipo original lo dejó. Conocen la visión, entienden las decisiones pasadas, tienen acceso a los fondos a través de la gobernanza, y pueden tomar el control sin perder el rumbo. La transparencia no es solo un valor ético, es un seguro de supervivencia del proyecto.

La adopción de soluciones consolidadas significa no reinventar la rueda en aspectos críticos de seguridad. Usar bibliotecas de contratos auditadas como [OpenZeppelin](https://www.openzeppelin.com/contracts), emplear mecanismos de consenso probados en batalla, implementar estándares establecidos por la industria. La innovación es valiosa, pero debe hacerse cuidadosamente en las capas correctas, no en los fundamentos de seguridad.

La descentralización progresiva reduce puntos únicos de fallo gradualmente, permitiendo que el sistema se fortalezca con el tiempo. Un proyecto puede comenzar más centralizado por necesidades prácticas de desarrollo rápido, pero debe tener un camino claro y público hacia la descentralización real del control técnico, económico y de gobernanza.

Esto incluye descentralizar no solo la governance, sino también la infraestructura técnica.

Por ejemplo, los proveedores de RPC (Remote Procedure Call, los servicios que permiten a las aplicaciones comunicarse con la blockchain) son un punto crítico. Si tu aplicación depende de un solo proveedor como Infura o Alchemy, y ese servicio cae o te bloquea, tu aplicación deja de funcionar. La solución es usar múltiples proveedores simultáneamente, con failover automático: si uno falla, otro toma su lugar.

Distribuir nodos entre diferentes geografías y operadores significa que no todos los servidores que ejecutan tu protocolo estén en AWS en Virginia, USA. Si están distribuidos entre AWS, Google Cloud, servidores independientes, diferentes países, entonces ningún gobierno o empresa puede apagar tu protocolo con una sola acción.

Asegurar que la documentación y el conocimiento estén distribuidos entre muchos miembros de la comunidad, no concentrados en pocas personas, significa que si pierdes a tu desarrollador principal, no pierdes todo el conocimiento de cómo funciona el sistema. Varios miembros de la comunidad deben poder mantener, actualizar y explicar el protocolo.

Los contratos multifirma para operaciones críticas deben incluir signatarios diversos geográfica y organizacionalmente. No sirve de mucho tener 5 firmas requeridas si las 5 personas trabajan en la misma oficina en San Francisco. Si el FBI llega, las tiene a todas. Mejor tener firmantes en diferentes países, diferentes compañías, diferentes contextos, para que sea imposible presionar a todos simultáneamente.

La alineación de incentivos busca diseñar economías donde hacer lo correcto sea también lo más rentable a largo plazo. Si atacar el sistema es más costoso y arriesgado que participar honestamente, la mayoría elegirá participar honestamente. Si extraer valor rápidamente y abandonar es más lucrativo que construir a largo plazo, el sistema atraerá extractores, no constructores.

La construcción de comunidad no es un aspecto secundario sino fundamental. Una comunidad fuerte, educada y comprometida es la mejor defensa contra casi todos los tipos de ataques. Una comunidad que entiende el sistema puede detectar anomalías. Una comunidad leal puede resistir campañas de FUD. Una comunidad técnicamente competente puede mantener el protocolo si los fundadores desaparecen.

Las auditorías y la revisión continua, tanto técnica como de modelo económico, deben ser parte del proceso normal de desarrollo, no eventos únicos previos al lanzamiento. El sistema debe ser constantemente reevaluado a medida que crece y enfrenta nuevos desafíos.

Los planes de contingencia son esenciales. ¿Qué pasa si hay un ataque en curso?

Primero, circuit breakers (interruptores de circuito): funciones de emergencia que pueden pausar el sistema si se detecta algo anormal. Por ejemplo, si de repente se retiran 10 millones de dólares en 5 minutos cuando lo normal son 50,000 dólares por hora, el sistema automáticamente se pausa para evitar más daño mientras la comunidad investiga qué está pasando.

Segundo, mecanismos de actualización de emergencia con los controles apropiados. Si se descubre una vulnerabilidad crítica, necesitas poder actualizar el contrato rápidamente, pero sin que una sola persona pueda hacerlo (porque esa sería otra vulnerabilidad). Por ejemplo, un multifirma de emergencia que puede actualizar el contrato con 3 de 5 firmas, pero solo durante las primeras 48 horas después de activar la emergencia, después de lo cual vuelve a requerir el proceso normal de gobernanza.

Tercero, fondos de emergencia para cubrir pérdidas en caso de exploits. Si alguien roba 1 millón de dólares aprovechando un bug, y el protocolo tiene un fondo de seguro, puede reembolsar a los usuarios afectados y mantener la confianza en lugar de colapsar.

Esperar lo mejor pero prepararse para lo peor. Los mejores protocolos nunca necesitan usar estas medidas de emergencia, pero las tienen listas por si acaso.

Y finalmente, la educación constante. Mantenerse informado de nuevas amenazas y mejores prácticas, compartir conocimiento con la comunidad, aprender de los fallos de otros proyectos. La industria avanza rápido y lo que era seguro ayer puede ser vulnerable mañana.

Precisamente este canal intenta explorar estas soluciones para que, con el trabajo de todos, podamos construir una Web3 más confiable y sostenible. No buscamos eliminar el riesgo, sino aprender a vivir con él de forma inteligente, construyendo sistemas que puedan prosperar incluso en ambientes hostiles.

---
