# Attestation Infrastructure: Arquitectura Técnica EAS

> 🚧 Este material está en construcción, se deja como referencia pero todavía no ha sido completamente validado en este repositorio de open3diy.

Más allá de las Verifiable Credentials que vimos como estándar W3C para credenciales off-chain, el ecosistema blockchain ha desarrollado lo que se conoce como Attestation Layer o Capa de Atestación: infraestructura on-chain diseñada específicamente para registrar, verificar y gestionar attestations de forma nativa.

Un attestation, en su concepto más fundamental de seguridad informática, es una declaración firmada digitalmente por un emisor que da fe de ciertos atributos o afirmaciones sobre un sujeto. Este concepto existe desde hace décadas en sistemas de seguridad tradicionales. Se define como capa de atestación en lugar de credenciales porque tiene un enfoque más primitivo, son documentos de verificación no evidencias de un sujeto que utiliza para identificarse.

Al igual que las VCs, las attestations son tecnológicamente neutrales y pueden usarse para múltiples propósitos: identidad autosoberana genuina (diplomas universitarios, membresías en DAOs, contribuciones open source), reputación social (asistencia a eventos, participación comunitaria), o compliance regulatorio (verificación KYC, sanctions screening). La diferencia fundamental con VCs es que las attestations típicamente viven públicamente on-chain donde smart contracts pueden componerlas, mientras que VCs priorizan almacenamiento privado off-chain bajo control del usuario.

Ejemplos reales incluyen universidades como [MIT Digital Credentials](https://digitalcredentials.mit.edu/) que emiten diplomas verificables, certificaciones profesionales que pueden verificarse instantáneamente, sistemas de reputación profesional como LinkedIn pero donde las habilidades son attestations verificables emitidas por organizaciones reconocidas, o proveedores KYC que emiten attestations confirmando "usuario verificado" sin exponer datos sensibles.

**Ethereum Attestation Service (EAS): implementación específica de Attestation Layer**:

[Ethereum Attestation Service (EAS)](https://attest.sh/) es un producto y servicio concreto que se ha establecido como una de las implementaciones líderes de la Attestation Layer en Ethereum y L2s compatibles. EAS no es "la arquitectura" de attestations, sino una implementación específica y popular de esta arquitectura más amplia. La propuesta de valor de EAS radica en su simplicidad: proporciona smart contracts estandarizados y APIs donde cualquiera puede emitir attestations verificables on-chain sin necesidad de desplegar contratos propios ni inventar formatos incompatibles.

El modelo conceptual de EAS gira alrededor de dos elementos: schemas y attestations. Los schemas definen estructuras de datos reutilizables, como plantillas que especifican qué campos debe contener una attestation (por ejemplo, un schema de "asistencia a eventos" incluiría campos como nombre del evento, fecha, y participante). Las attestations son instancias concretas de estos schemas, firmadas por emisores específicos sobre sujetos específicos.

Lo importante del Schema Registry de EAS es que funciona como un catálogo público donde la comunidad puede descubrir y reutilizar schemas existentes en lugar de fragmentar el ecosistema con formatos incompatibles. Si tu DAO necesita atestiguar membresía, probablemente ya existe un schema estándar que múltiples organizaciones usan. Esta estandarización permite que aplicaciones que consumen attestations entiendan datos de múltiples emisores sin integraciones personalizadas para cada uno.

EAS soporta attestations tanto on-chain como off-chain según las necesidades del caso de uso. Las attestations on-chain viven permanentemente en blockchain con verificabilidad máxima y composabilidad directa con smart contracts, pero implican costos de gas. Las attestations off-chain se firman criptográficamente y almacenan fuera de blockchain, con solo un hash registrado on-chain, reduciendo dramáticamente costos pero introduciendo dependencia de disponibilidad externa.

**Más allá de EAS: ecosistema de attestations**:

Aunque EAS domina como infraestructura de attestations, existe un ecosistema más amplio de soluciones de identidad y credenciales. El documento [9-1-ecosystem-DApps](../../101/9-1-ecosystem-DApps.md) explora estas implementaciones concretas y sus casos de uso prácticos.

**On-chain vs off-chain attestations: trade-offs críticos**:

EAS soporta dos modos de almacenamiento con implicaciones técnicas y económicas significativas.

Las attestations on-chain se registran directamente en smart contracts desplegados en Ethereum L1 o L2s. Cada attestation se almacena permanentemente en blockchain storage, accesible mediante queries a los contratos EAS. Las ventajas incluyen verificabilidad máxima porque cualquiera puede consultar la blockchain directamente sin confiar en servicios externos, permanencia garantizada porque los datos sobrevivirán mientras exista la blockchain, y composabilidad nativa porque otros smart contracts pueden leer y reaccionar a estas attestations programáticamente.

Los trade-offs incluyen costos de gas significativos. En Ethereum L1, emitir una attestation puede costar $5-50 dependiendo de congestión de red. L2s como Optimism reducen esto a centavos, pero aún existe fricción económica. El storage permanente también significa que attestations sensibles quedan públicamente visibles para siempre, aunque el contenido puede encriptarse antes de registration. Para casos de uso de alto volumen, estos costos se acumulan rápidamente: un sistema de reputation scoring que emite millones de attestations diarias enfrentaría costos prohibitivos on-chain.

Las attestations off-chain se firman criptográficamente por el emisor pero almacenan fuera de blockchain, típicamente en bases de datos tradicionales o storage descentralizado como IPFS. Solo el hash de la attestation y metadata mínima se publican on-chain, reduciendo dramáticamente costos. El contenido completo se sirve mediante APIs de EAS o infraestructura propia del emisor.

Las ventajas incluyen costos órdenes de magnitud menores, adecuados para aplicaciones de alta frecuencia, flexibilidad para actualizar metadata o revocar attestations sin transacciones on-chain adicionales, y privacidad mejorada porque el contenido sensible puede almacenarse con acceso controlado. Los trade-offs son dependencia de disponibilidad de servicios externos porque si el storage off-chain desaparece, solo queda el hash on-chain, y verificación más compleja porque los verificadores deben confiar en que el contenido servido coincide con el hash registrado.

**Composabilidad: attestations como legos de reputación**:

La verdadera potencia de la Attestation Layer emerge cuando múltiples protocolos componen attestations de diversas fuentes para construir sistemas de reputación ricos. Imagina un protocolo de préstamos descentralizado que evalúa solvencia considerando attestations de membresía en DAOs respetadas, attestations de historial de repago en otros lending protocols, attestations de tenencia de tokens específicos, y si el protocolo debe cumplir regulaciones, attestations de verificación KYC de proveedores autorizados.

Cada attestation proviene de un emisor diferente, pero todos son verificables mediante la misma infraestructura on-chain. El lending protocol implementa lógica que pondera estas attestations según su confianza en cada emisor y la relevancia de los claims, generando un credit score componible. Las attestations de reputación social (membresías, contribuciones) construyen confianza descentralizada genuina, mientras que attestations de KYC permiten cumplir requisitos legales sin comprometer privacidad más allá de lo estrictamente necesario. Este modelo híbrido es imposible en sistemas centralizados donde cada plataforma mantiene silos de reputación incompatibles.

Gitcoin Passport ejemplifica perfectamente esta composabilidad. Como sistema de Proof of Personhood anti-Sybil, Gitcoin Passport agrega attestations de docenas de fuentes diferentes: verificación de Twitter, staking de ETH, participación histórica en Gitcoin Grants, verificación biométrica de BrightID. Cada stamp es una attestation on-chain. El Passport score se calcula ponderando estas attestations según algoritmos anti-Sybil, demostrando cómo múltiples credenciales componibles crean identidad verificable robusta resistente a manipulación.

**Lógica programable en EAS: Resolver Contracts**:

EAS permite opcionalmente asociar resolver contracts a schemas específicos. Estos resolver contracts son smart contracts que actúan como intermediarios programables dentro del ecosistema EAS: cuando alguien intenta emitir, revocar o verificar una attestation usando ese schema, el resolver ejecuta automáticamente código personalizado que puede aprobar, rechazar o modificar la operación.

Es importante no confundir estos resolver contracts de EAS con los DID Resolvers que vimos en secciones anteriores. Un DID Resolver es software que convierte un DID string en su DID Document consultando la infraestructura del método correspondiente. Un EAS Resolver Contract es un smart contract específico que ejecuta lógica de negocio cuando se operan attestations. Son conceptos completamente diferentes que comparten el término "resolver" pero operan en contextos distintos.

Los resolver contracts de EAS permiten agregar lógica de negocio compleja a las attestations. Imagina que quieres emitir attestations de acceso premium solo a miembros verificados de tu DAO. El resolver puede verificar automáticamente que el destinatario posee un token de membresía antes de permitir la emisión. Si no cumple el requisito, la transacción falla directamente en el smart contract.

Los resolvers también pueden desencadenar acciones automáticas. Cuando se emite una attestation específica, el resolver podría acuñar un NFT para el usuario, transferir tokens como recompensa, o notificar a otros contratos del evento. En el caso de revocaciones, el resolver puede implementar reglas de gobernanza que determinen quién tiene autoridad para revocar attestations específicas, protegiendo contra ataques donde actores maliciosos intentan eliminar attestations legítimas.

Sin embargo, los resolvers añaden complejidad técnica y superficie de ataque. Un bug en el código del resolver puede bloquear completamente la emisión de attestations o introducir vulnerabilidades de seguridad. Por esta razón, la mayoría de schemas operan sin resolvers. En lugar de validar condiciones durante la emisión, estos sistemas confían en que los verificadores implementen su propia lógica al momento de consultar las attestations.

## Arquitectura conceptual de EAS

EAS proporciona una infraestructura estandarizada que resuelve el problema de interoperabilidad en attestations. En lugar de que cada protocolo implemente su propio sistema de credenciales incompatible, EAS ofrece componentes reutilizables que crean un ecosistema coherente.

### Schemas: plantillas reutilizables

Los schemas funcionan como plantillas que definen qué información debe contener cada tipo de attestation. Son similares a formularios estandarizados: un schema de "certificación educativa" especifica que debe incluir campos como estudiante, curso, fecha de finalización y calificación, mientras que un schema de "verificación KYC" incluye campos como estado de verificación, nivel de cumplimiento y fecha de expiración.

La potencia de los schemas radica en su reutilización. En lugar de que cada universidad invente su propio formato de diploma digital, todas pueden usar el mismo schema estandarizado de "certificación educativa". Esto permite que empleadores construyan sistemas que reconocen automáticamente diplomas de cualquier institución sin necesidad de integraciones personalizadas.

### Attestations: instancias de datos verificables

Las attestations son los documentos específicos creados usando un schema determinado. Si el schema es la plantilla, la attestation es el formulario completado y firmado. Cada attestation incluye los datos específicos, la identidad del emisor, el destinatario, timestamps de creación y expiración, y una firma criptográfica que garantiza autenticidad.

### Resolvers: lógica programable opcional

Los resolvers permiten añadir reglas automáticas a los schemas. Por ejemplo, un schema de "acceso premium" puede incluir un resolver que verifica automáticamente que el destinatario posee un NFT de membresía antes de emitir la attestation. Si no cumple el requisito, la emisión falla automáticamente.

Los resolvers también pueden desencadenar acciones: cuando se emite una attestation de "tarea completada", el resolver puede transferir automáticamente tokens como recompensa al destinatario. En caso de revocaciones, pueden implementar reglas de gobernanza que determinen quién tiene autoridad para revocar attestations específicas.

## Consideraciones económicas y técnicas

### Costos y escalabilidad

Las attestations on-chain implican costos de gas que pueden ser significativos en Ethereum mainnet (entre $5-50 por attestation según congestión), pero se reducen dramáticamente en Layer 2s como Base, Optimism o Arbitrum (entre $0.05-0.30). Esto ha llevado a muchos proyectos a adoptar estrategias híbridas donde las attestations críticas van en mainnet para máxima seguridad, mientras que las de alto volumen van en L2s.

### Privacidad vs transparencia

El modelo on-chain público de EAS crea un trade-off fundamental entre verificabilidad y privacidad. Las attestations son auditables por cualquiera, lo que facilita la composabilidad pero puede comprometer la privacidad del usuario. Para casos sensibles, existen implementaciones que combinan EAS con Zero-Knowledge Proofs, permitiendo probar "tengo una attestation válida con propiedad X" sin revelar detalles específicos.

### Confianza en emisores

Las attestations son tan confiables como sus emisores. La infraestructura verifica que la attestation fue firmada por quien dice haberla firmado, pero no garantiza que el emisor sea confiable o que los datos sean veraces. Esto ha llevado al desarrollo de sistemas de reputación de emisores, whitelists curadas por comunidades, y mecanismos de stake económico donde los emisores arriesgan tokens por la calidad de sus attestations.

## Casos de uso y patrones emergentes

### Reputación componible

El patrón más prometedor es la "reputación componible", donde múltiples protocolos agregan attestations de diversas fuentes para tomar decisiones. Un protocolo de préstamos puede considerar attestations de verificación KYC, membresía en DAOs reconocidas, historial de repago en otros protocolos, y scores de sistemas anti-Sybil como Gitcoin Passport. Cada fuente mantiene su independencia, pero el conjunto crea un perfil de reputación rico y resistente a manipulación.

### Credenciales educativas y profesionales

Las universidades y organizaciones profesionales han comenzado a adoptar attestations para credenciales verificables. MIT emite diplomas como attestations que empleadores pueden verificar instantáneamente sin contactar a la universidad. Certificaciones profesionales, licencias médicas, y membresías en organizaciones pueden seguir el mismo patrón, creando un ecosistema de credenciales interoperables.

### Anti-Sybil y gobernanza

Los sistemas de gobernanza descentralizada utilizan attestations para prevenir ataques Sybil y ponderar la participación según contribuciones verificadas. En lugar de "una dirección, un voto", pueden implementar "votos ponderados por attestations de contribución", donde desarrolladores con attestations de código merged tienen más peso en decisiones técnicas, mientras que usuarios con attestations de participación comunitaria tienen más influencia en decisiones de producto.

### Compliance regulatorio privado

Las attestations permiten cumplir requisitos regulatorios sin comprometer completamente la privacidad. Un proveedor KYC puede emitir attestations que confirman "usuario verificado, sin banderas de sanciones, jurisdicción permitida" sin revelar identidad específica, datos de localización exacta o detalles de verificación. Los protocolos DeFi pueden entonces restringir acceso basándose en estas attestations mientras mantienen cierto grado de privacidad para los usuarios.

## Integración con el ecosistema

EAS no opera en aislamiento sino como parte de un ecosistema más amplio de infraestructura de identidad y reputación. Se complementa con:

**Verifiable Credentials (VCs)** para casos que requieren control total del usuario y almacenamiento privado off-chain

**Sistemas de identidad descentralizada (DIDs)** como ancla de confianza para emisores y resolución de identidades

**Protocolos de Zero-Knowledge** para privacidad mejorada cuando se necesita verificación sin revelación

**Redes sociales descentralizadas** como Lens o Farcaster que pueden integrar attestations como badges de verificación

**Protocolos DeFi** que pueden condicionar acceso, tasas, o límites basándose en attestations de reputación

Esta composabilidad es fundamental para el valor a largo plazo de las attestations: no son simplemente credenciales aisladas, sino primitivas que permiten construir sistemas de confianza y reputación más sofisticados que cualquier plataforma centralizada.

## Referencias

- [EAS Documentation](https://docs.attest.sh/) - Documentación oficial
- [EASSCAN](https://easscan.org/) - Explorador de attestations
- [EAS Schema Registry](https://base.easscan.org/schemas) - Catálogo de schemas públicos
- Para casos de uso prácticos consulta [9-1-ecosystem-DApps.md](../../101/9-1-ecosystem-DApps.md)

---
