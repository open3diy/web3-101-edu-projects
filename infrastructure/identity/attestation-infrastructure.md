# Attestation Infrastructure

> 🚧 Documento en construcción...

Más allá de las Verifiable Credentials que vimos como estándar W3C para credenciales off-chain, el ecosistema blockchain ha desarrollado lo que se conoce como Attestation Layer o Capa de Atestación: infraestructura on-chain diseñada específicamente para registrar, verificar y gestionar attestations de forma nativa.

Una attestation es, en su concepto más fundamental de seguridad informática, una declaración firmada digitalmente por un emisor que da fe de ciertos atributos o afirmaciones sobre un sujeto. Este concepto existe desde hace décadas en sistemas de seguridad tradicionales. Se habla de capa de atestación y no de credenciales porque el enfoque es más primitivo: las attestations son declaraciones emitidas por terceros sobre un sujeto, no evidencias que el propio sujeto presenta para identificarse.

Las attestations son tecnológicamente neutrales y pueden usarse para múltiples propósitos: identidad autosoberana genuina (diplomas universitarios, membresías en DAOs, contribuciones open source), reputación social (asistencia a eventos, participación comunitaria), o compliance regulatorio (verificación KYC, sanctions screening). La diferencia fundamental con las VCs es que las attestations típicamente viven públicamente on-chain donde smart contracts pueden componerlas, mientras que las VCs priorizan el almacenamiento privado off-chain bajo control del usuario. Ejemplos reales incluyen universidades como [MIT Digital Credentials](https://digitalcredentials.mit.edu/) que emiten diplomas verificables, proveedores KYC que atestiguan "usuario verificado" sin exponer datos sensibles, o sistemas de reputación profesional donde las habilidades son attestations emitidas por organizaciones reconocidas.

## EAS como infraestructura de referencia

[Ethereum Attestation Service (EAS)](https://attest.sh/) es la implementación más extendida de la Attestation Layer en Ethereum y sus L2s compatibles. EAS no define la arquitectura general de las attestations, sino que ofrece una implementación concreta y estandarizada: proporciona smart contracts y APIs donde cualquiera puede emitir attestations verificables on-chain sin necesidad de desplegar contratos propios ni inventar formatos incompatibles.

El modelo conceptual de EAS gira en torno a dos elementos: schemas y attestations. Los schemas son plantillas reutilizables que definen qué campos debe contener una attestation (por ejemplo, un schema de "asistencia a eventos" incluiría nombre del evento, fecha y participante). Las attestations son instancias concretas de esos schemas, firmadas por emisores específicos sobre sujetos específicos.

**Schemas y reusabilidad**:

El Schema Registry de EAS funciona como un catálogo público donde la comunidad puede descubrir y reutilizar schemas existentes en lugar de fragmentar el ecosistema con formatos incompatibles. Si una DAO necesita atestiguar membresía, probablemente ya existe un schema estándar que múltiples organizaciones usan, y esa estandarización permite que cualquier aplicación que consuma attestations entienda datos de emisores distintos sin integraciones personalizadas para cada uno.

El diseño de los schemas tiene además implicaciones directas de privacidad. La práctica recomendada es incluir únicamente los campos estrictamente necesarios, sustituyendo datos personales por sus hashes criptográficos cuando sea posible. Un schema de verificación de mayoría de edad, por ejemplo, no necesita la fecha de nacimiento literal sino únicamente `bool isOver18`. Este principio de mínima divulgación reduce la exposición de información sensible sin sacrificar la utilidad de la attestation. Adicionalmente, las attestations pueden encadenarse entre sí mediante un campo de referencia, construyendo credenciales jerárquicas verificables: un diploma que referencia la attestation de admisión universitaria, que a su vez referencia la attestation de examen de acceso.

Aunque EAS domina como infraestructura de attestations, existe un ecosistema más amplio de soluciones. El documento [9-1-ecosystem-DApps](9-1-ecosystem-DApps.md) explora estas implementaciones concretas y sus casos de uso prácticos.

## On-chain, off-chain e híbrido

EAS soporta dos modos de almacenamiento con implicaciones técnicas y económicas muy diferentes.

Las attestations on-chain se registran directamente en smart contracts desplegados en Ethereum L1 o sus L2s. Cada attestation se almacena permanentemente en blockchain storage y es accesible mediante consultas a los contratos EAS. Sus ventajas son la verificabilidad máxima —cualquiera puede consultar la blockchain sin confiar en servicios externos—, la permanencia garantizada mientras exista la red, y la composabilidad nativa porque otros smart contracts pueden leer y reaccionar a estas attestations de forma programática. Los trade-offs son costos de gas significativos (en Ethereum L1, entre $5 y $50 por attestation según la congestión de red, aunque en L2s como Optimism o Base se reducen a céntimos), exposición pública permanente de los datos, y latencia vinculada al tiempo de bloque.

Las attestations off-chain se firman criptográficamente pero se almacenan fuera de la blockchain, típicamente en IPFS u otras soluciones de almacenamiento descentralizado. Solo el hash de la attestation y los metadatos mínimos se publican on-chain, lo que reduce dramáticamente los costos. Su contenido completo se sirve mediante las APIs de EAS o infraestructura propia del emisor. Las ventajas son costos órdenes de magnitud menores, privacidad mejorada porque el contenido sensible no toca la blockchain, y flexibilidad para actualizar metadatos o revocar attestations sin transacciones adicionales. El precio a pagar es la dependencia de disponibilidad del almacenamiento externo —si desaparece, solo queda el hash— y una verificación más compleja que requiere obtener el contenido completo, recomputar su hash y compararlo con el registrado on-chain.

La dicotomía on-chain / off-chain no es absoluta. Muchas implementaciones maduras adoptan estrategias intermedias: registrar on-chain únicamente los campos mínimos que los smart contracts necesitan consultar (como `isVerified: bool, level: uint8`), manteniendo fuera de la blockchain los documentos de respaldo completos. Un patrón más sofisticado consiste en acumular múltiples attestations off-chain y publicar periódicamente on-chain un Merkle root que las compromete a todas. Esto permite probar criptográficamente la existencia e integridad de cualquier attestation individual sin el coste de haberlas registrado todas on-chain, equilibrando economía con verificabilidad garantizada.

## Composabilidad

La verdadera potencia de la Attestation Layer emerge cuando múltiples protocolos componen attestations de diversas fuentes para construir sistemas de reputación ricos. Imagina un protocolo de préstamos descentralizado que evalúa la solvencia de un solicitante considerando attestations de membresía en DAOs respetadas, attestations de historial de repago en otros lending protocols, attestations de tenencia de tokens específicos, y si el protocolo debe cumplir regulaciones, attestations de verificación KYC de proveedores autorizados. Cada attestation proviene de un emisor diferente, pero todas son verificables mediante la misma infraestructura on-chain. El lending protocol implementa lógica que pondera estas attestations según su confianza en cada emisor y la relevancia de los claims, generando un credit score componible que es imposible en sistemas centralizados donde cada plataforma mantiene silos de reputación incompatibles.

[Gitcoin Passport](https://passport.gitcoin.co/) ejemplifica perfectamente esta composabilidad. Como sistema de Proof of Personhood anti-Sybil, agrega attestations de docenas de fuentes: verificación de Twitter, staking de ETH, participación histórica en Gitcoin Grants, verificación biométrica de BrightID. Cada stamp es una attestation on-chain. El Passport score se calcula ponderando estas attestations según algoritmos anti-Sybil, demostrando cómo múltiples credenciales componibles construyen una identidad verificable robusta y resistente a la manipulación.

Los patrones de composición que emergen de este modelo se pueden sistematizar: la agregación combina múltiples attestations del mismo tipo para calcular un score acumulativo; la lógica condicional requiere una combinación específica de attestations como condición de acceso (KYC y membresía activa y reputación por encima de un umbral); la composición jerárquica establece que ciertas attestations son prerequisito de otras; la ponderación temporal asigna mayor peso a attestations recientes sobre las antiguas; y la agregación ponderada por fuente reconoce que no todos los emisores merecen igual confianza.

Vale destacar además que las attestations no se dirigen exclusivamente a personas o wallets. El destinatario puede ser cualquier dirección Ethereum, incluidos NFTs que representan objetos físicos o digitales. En logística, cada paso del proceso productivo puede recibir attestations sobre origen, transporte o calidad que quedan vinculadas permanentemente al NFT del producto, haciendo trazable y verificable toda su cadena de custodia sin depender de bases de datos centralizadas.

## Lógica programable: resolver contracts

EAS permite asociar opcionalmente resolver contracts a schemas específicos. Estos son smart contracts que actúan como intermediarios programables: cuando alguien intenta emitir, revocar o verificar una attestation usando ese schema, el resolver ejecuta automáticamente código personalizado que puede aprobar, rechazar o modificar la operación. Es importante no confundirlos con los DID Resolvers que vimos en secciones anteriores: un DID Resolver es software que convierte un identificador DID en su documento asociado consultando la infraestructura del método correspondiente, mientras que un EAS Resolver Contract es un smart contract que ejecuta lógica de negocio al operar attestations. Son conceptos completamente distintos que comparten el término "resolver" pero operan en contextos diferentes.

Los resolvers permiten agregar lógica de negocio compleja. Un resolver puede verificar automáticamente que el destinatario posee un token de membresía antes de permitir la emisión, o desencadenar acciones automáticas cuando se emite una attestation: acuñar un NFT, transferir tokens como recompensa, o notificar a otros contratos. En el caso de revocaciones, el resolver puede implementar reglas de gobernanza que determinen quién tiene autoridad para revocar, protegiendo las attestations legítimas frente a actores maliciosos. Sin embargo, los resolvers añaden complejidad técnica y superficie de ataque: un bug en el código puede bloquear completamente la emisión de attestations o introducir vulnerabilidades de seguridad. Por esta razón, la mayoría de schemas operan sin resolvers, confiando en que los verificadores implementen su propia lógica al momento de consultar las attestations.

## Tensiones y límites del modelo

Las attestations resuelven muchos problemas de las credenciales tradicionales, pero introducen tensiones propias que conviene entender antes de adoptar el modelo.

**La confianza en los emisores**:

La verificación criptográfica demuestra que un emisor específico firmó la attestation, pero no dice nada sobre si ese emisor merece confianza. Dos mecanismos principales abordan esta tensión. El primero es el modelo de listas de emisores autorizados: el protocolo consumidor mantiene una lista curada de emisores cuyas attestations acepta. El segundo es la meta-atestación: organizaciones de confianza emiten attestations sobre otros emisores, construyendo un grafo de confianza donde la reputación de los propios emisores es verificable on-chain. Este segundo enfoque es más descentralizado pero traslada el problema un nivel más arriba, dado que la cadena de confianza siempre ancla en algún punto en un actor humano o institucional.

**Privacidad y reidentificación**:

Las attestations on-chain públicas introducen un riesgo no evidente: cuando una attestation KYC vincula una dirección Ethereum con una identidad real, cualquier actor puede correlacionar esa identidad con toda la actividad histórica de esa dirección en la blockchain. La dirección deja de ser seudónima para convertirse en nominativa. La respuesta emergente son las pruebas de conocimiento cero aplicadas a credenciales: en lugar de revelar la attestation, el titular puede demostrar criptográficamente que posee una attestation con cierta propiedad —"soy mayor de edad" o "tengo verificación KYC nivel 2"— sin exponer el contenido de la credencial ni revelar su emisor. Sistemas como [Privado ID](https://www.privadoid.com/) aplican este enfoque, desacoplando la verificabilidad de la exposición de datos personales.

**Inmutabilidad y el derecho al olvido**:

Las attestations on-chain no pueden borrarse. Pueden revocarse, pero la attestation original permanece visible en la blockchain indefinidamente. Esto entra en conflicto directo con regulaciones como el GDPR europeo, que reconoce el derecho de cualquier persona a solicitar la eliminación de sus datos personales. Para reconciliar ambas realidades, la práctica recomendada consiste en no incluir información de identificación personal directamente en las attestations on-chain, sino hashes de esos datos. El hash registrado on-chain prueba la existencia e integridad de la credencial sin revelar su contenido; los datos originales permanecen off-chain bajo control del sujeto o del emisor, y son el objeto sobre el cual aplicar el derecho al olvido.

**La dependencia de indexación**:

Consultar attestations eficientemente desde una aplicación requiere indexación off-chain. Las blockchains no están diseñadas para consultas complejas del tipo "todas las attestations del usuario X de tipo Y no revocadas ordenadas por fecha". Las aplicaciones reales dependen de indexadores especializados como [The Graph](https://thegraph.com/) para que esas consultas sean viables. Esto introduce una dependencia de infraestructura off-chain incluso en sistemas diseñados para ser completamente descentralizados, un trade-off que toda arquitectura de attestations asume de forma pragmática.

Las tensiones descritas en este apartado tienen contrapartida en el modelo de VCs off-chain. Para un análisis comparativo de confianza en emisores, semántica temporal y mecanismos de revocación que aplican a ambos modelos, ver [vc-attestation-best-practices.md](vc-attestation-best-practices.md).

## Referencias

- [EAS Documentation](https://docs.attest.sh/)
- [EAS GitHub](https://github.com/ethereum-attestation-service/eas-contracts)
- [EASSCAN Explorer](https://easscan.org/)
- [EAS Schema Registry](https://base.easscan.org/schemas)
- [Attestation Use Cases](https://docs.attest.sh/docs/category/use-cases/)
- [Gitcoin Passport](https://passport.gitcoin.co/)
- [The Graph](https://thegraph.com/)
- [MIT Digital Credentials](https://digitalcredentials.mit.edu/)
- [Mejores prácticas en VC y Attestations](vc-attestation-best-practices.md) - Confianza en emisores, semántica temporal y revocación comparativa

---
