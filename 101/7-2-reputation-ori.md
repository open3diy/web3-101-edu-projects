# Reputación Web3

## 1. Fundamentos Conceptuales

### 1.4 Mecanismos de Construcción de Reputación



## 3. Arquitectura de Sistemas de Reputación

Construir un sistema de reputación efectivo requiere entender cómo diferentes capas de tecnología se integran para crear una solución completa. La arquitectura típica sigue un modelo de capas donde cada nivel abstrae la complejidad del nivel inferior y proporciona servicios al nivel superior.

### 3.1 Stack Tecnológico Completo

La arquitectura completa de un sistema de reputación Web3 se puede visualizar como una torre de cuatro capas principales, cada una con responsabilidades específicas.

En la base está la Capa de Datos, que incluye todas las transacciones on-chain (interacciones con smart contracts, transferencias, votaciones) y datos off-chain complementarios (actividad en redes sociales, contribuciones a GitHub, participación en foros). Esta capa es puramente informativa y no tiene lógica de negocio, simplemente proporciona los datos brutos que alimentan las capas superiores.

La segunda capa es la Capa de Atestación, donde protocolos como Ethereum Attestation Service, Verax y Otterspace convierten datos brutos en declaraciones verificables. Por ejemplo, el hecho de que hayas votado en 50 propuestas de gobernanza de diferentes DAOs (dato bruto) se convierte en una attestation firmada que certifica tu nivel de participación en gobernanza descentralizada. Esta capa es crucial porque añade verificabilidad criptográfica y estandarización a los datos.

La tercera capa es la Capa de Agregación y Algoritmos, donde protocolos como Orange Protocol, los scores de Gitcoin Passport, o los sistemas de scoring de Noox toman múltiples attestations y datos on-chain para calcular puntuaciones agregadas. Esta capa implementa la lógica de negocio: ¿cómo ponderamos diferentes tipos de participación? ¿Es más valioso haber contribuido código a un protocolo o haber provisto liquidez? ¿Cómo prevenimos gaming del sistema?

Finalmente, en la cima está la Capa de Aplicación, donde DApps como plataformas de préstamos DeFi, interfaces de gobernanza DAO, o marketplaces NFT consumen los scores de reputación para tomar decisiones. Por ejemplo, Aave podría consultar tu score agregado para determinar si calificas para un préstamo subcolateralizado.

La belleza de esta arquitectura modular es que cada capa puede evolucionar independientemente. Nuevos protocolos de atestación pueden emerger sin romper las aplicaciones existentes, y nuevos algoritmos de agregación pueden competir ofreciendo mejores modelos de scoring.

### 3.2 Modelos de Agregación

La forma en que se agregan múltiples señales de reputación en un score único o conjunto de scores es quizás la decisión más crítica en el diseño de un sistema de reputación. Existen tres modelos principales, cada uno con ventajas y limitaciones.

**Modelo de Múltiples Fuentes**:

Este modelo combina datos de diversas fuentes en un score compuesto único. [Gitcoin Passport](https://passport.gitcoin.co) ejemplifica este enfoque. El Humanity Score de Gitcoin agrega más de 20 "stamps" diferentes: verificación de Google, cuenta de Twitter con cierta antigüedad, tenencia de un ENS domain, participación en BrightID, holdings de ETH, participación histórica en Gitcoin Grants, y muchos más.

Cada stamp contribuye un cierto número de puntos al score total, con diferentes pesos según la dificultad de falsificar ese stamp. Por ejemplo, tener una cuenta de GitHub con 5 años de antigüedad y contribuciones regulares podría valer más puntos que simplemente verificar tu cuenta de Google, porque es mucho más costoso en tiempo crear una cuenta de GitHub legítima.

La ventaja es simplicidad para aplicaciones: obtienen un número único que pueden usar en sus decisiones. La desventaja es que el algoritmo de ponderación es necesariamente arbitrario y puede no ser apropiado para todos los contextos.

**Modelo Contextual**:

Este modelo reconoce que la reputación no es universal sino específica al dominio. Tu reputación como trader DeFi es independiente de tu reputación como artista NFT o como contribuidor a protocolos de infraestructura.

[Orange Protocol](https://www.orangeprotocol.io) permite este tipo de reputación contextual. Las comunidades y aplicaciones pueden definir sus propios modelos de reputación específicos para su contexto, seleccionando qué fuentes de datos son relevantes y cómo deben ponderarse.

Por ejemplo, una DAO enfocada en desarrollo de software podría valorar contribuciones a GitHub, participación en hackathons, y ownership de SBTs de cursos técnicos. Mientras tanto, una DAO de arte generativo valoraría ownership de NFTs de artistas reconocidos, participación en comunidades creativas, y curación exitosa de colecciones.

Este enfoque es más sofisticado pero requiere que cada aplicación o comunidad invierta esfuerzo en definir su modelo de reputación específico.

**Modelo Basado en Grafos**:

Este modelo utiliza teoría de redes para calcular reputación basándose en las conexiones entre entidades. La idea fundamental es que la reputación de una entidad está influenciada por la reputación de las entidades que la avalan.

El algoritmo [EigenTrust](https://nlp.stanford.edu/pubs/eigentrust.pdf), desarrollado originalmente para redes peer-to-peer, es un ejemplo de este enfoque. Si tres personas con alta reputación atestiguan sobre ti, recibes más valor reputacional que si tres personas con baja reputación lo hacen.

Este modelo es particularmente poderoso para prevenir Sybil attacks. Crear mil cuentas falsas es fácil, pero hacer que esas cuentas reciban attestations de entidades con reputación genuina es extremadamente difícil. El modelo basado en grafos naturalmente devalúa clusters de entidades que solo se atestiguan entre sí sin conexiones al grafo más amplio.

Protocolos como [Karma3 Labs](https://www.karma3labs.com) implementan algoritmos basados en grafos especializados para diferentes casos de uso, desde detección de spam hasta cálculo de influencia en comunidades.

### 3.3 Capas del Proceso de Atestación

Entender el ciclo de vida completo de una attestation es crucial para implementar sistemas robustos. El proceso se divide en cuatro etapas principales.

**Creación y Emisión**:

Esta primera etapa es donde una entidad (el Emisor) decide hacer una declaración verificable sobre otra entidad (el Sujeto). El emisor podría ser una organización (como una universidad emitiendo un diploma digital), un smart contract (como un protocolo DeFi emitiendo una attestation de "liquidez provista por 100+ días"), o incluso otro individuo (como en sistemas de endorsement peer-to-peer).

El emisor debe decidir qué schema usar o crear uno nuevo. Por ejemplo, si estás emitiendo una certificación de completar un curso, podrías usar el schema existente de [VerifiableCredentials del W3C](https://www.w3.org/TR/vc-data-model/) o crear uno específico para tu institución que incluya campos adicionales como calificación final o proyecto capstone completado.

La attestation se firma criptográficamente con la clave privada del emisor, asegurando que cualquiera pueda verificar su autenticidad pero nadie pueda falsificarla.

**Registro On-chain o Off-chain**:

Una vez creada, la attestation debe ser registrada en algún lugar verificable. Las opciones principales son on-chain directamente en Ethereum u otra blockchain, o off-chain usando sistemas como Ceramic Network o IPFS con un hash o merkle root publicado on-chain.

El tradeoff es clásico: almacenamiento on-chain es más costoso pero más permanente y verificable. Almacenamiento off-chain con anclaje on-chain es más barato pero requiere que los datos off-chain estén disponibles para verificación.

[EAS](https://attest.sh) soporta ambos modos. Para attestations críticas como certificaciones académicas o pruebas de propiedad de activos, tiene sentido pagar el gas para almacenamiento on-chain completo. Para attestations más efímeras como "asistió a un evento comunitario semanal", el modo off-chain con anclaje on-chain puede ser suficiente.

**Verificación**:

Esta es la etapa donde una tercera parte (el Verificador) consulta una attestation para tomar una decisión. El verificador necesita confirmar tres cosas: que la attestation es auténtica (realmente firmada por quien dice ser el emisor), que sigue siendo válida (no ha sido revocada y no ha expirado), y que el emisor es confiable para ese tipo de attestation específico.

La verificación puede ser muy simple (revisar una firma criptográfica) o muy compleja. Por ejemplo, con zero-knowledge proofs, podrías verificar que alguien tiene una credencial sin revelar los detalles de esa credencial. Sismo permite estos tipos de verificaciones preservando privacidad, donde puedes probar que tienes un balance de ETH superior a 10 sin revelar tu dirección específica o balance exacto.

**Revocación**:

La capacidad de revocar attestations es controversial pero necesaria. Imagina que una universidad emite diplomas digitales como attestations y luego descubre que un estudiante hizo fraude académico. Necesita poder revocar esa credencial.

Los mecanismos de revocación varían. Algunos sistemas usan listas de revocación on-chain donde el emisor puede marcar attestations como inválidas. Otros usan criptografía de acumuladores que permite probar que una attestation no ha sido revocada sin revelar qué otras attestations existen. Algunos simplemente usan fechas de expiración, donde las attestations automáticamente se vuelven inválidas después de cierto tiempo a menos que sean renovadas.

El [Status List 2021 del W3C](https://www.w3.org/TR/vc-status-list/) proporciona un estándar para manejar el estado de credenciales verificables, incluyendo revocación y suspensión.

**Características Clave del Diseño**:

Un sistema robusto de attestations debe incluir mecanismos de apelación donde los sujetos de attestations negativas puedan disputarlas. Esto podría ser tan simple como permitir que el sujeto publique una contra-attestation explicando su posición, o tan complejo como un sistema de arbitraje donde terceros neutrales revisan disputas.

Las fechas de caducidad son importantes para la higiene del sistema. Una attestation de "conoce Solidity" de hace 10 años probablemente no es relevante dado lo rápido que evoluciona el ecosistema. Implementar expiración automática o requerir renovación periódica mantiene el sistema actualizado.

Finalmente, los esquemas de atestación reutilizables permiten que comunidades converjan en estándares comunes. En lugar de que cada institución educativa cree su propio formato de diploma digital, todos pueden usar el mismo schema subyacente, facilitando interoperabilidad y reconocimiento automático.



## 5. Herramientas y Plataformas

El ecosistema de reputación Web3 ha madurado significativamente con docenas de herramientas especializadas que permiten a usuarios construir, visualizar y monetizar su reputación on-chain. Esta sección explora las plataformas más importantes organizadas por su función principal.

### 5.1 Verificación de Identidad y Humanidad: Proof of Personhood

Establecer que eres una persona real única es el primer paso para construir reputación significativa. El desafío técnico fundamental es resolver el problema de Sybil attacks en sistemas descentralizados donde crear nuevas identidades es trivial y gratuito. **Proof of Personhood** (PoP) es el conjunto de mecanismos criptográficos, sociales y económicos que permiten verificar unicidad humana sin depender de autoridades centralizadas.

**El Trilema de Proof of Personhood**:

Existen tres propiedades deseables que ningún sistema actual logra simultáneamente de forma óptima:

1. **Descentralización**: No depender de gobiernos, corporaciones o cualquier entidad central que pueda censurar, manipular o cerrar el sistema.

2. **Privacidad**: No requerir revelar identidad legal real ni información personal sensible que pueda ser usada para vigilancia o correlación.

3. **Resistencia Sybil**: Imposibilidad práctica y económica de que un individuo cree múltiples identidades verificadas.

Cada implementación de PoP debe elegir trade-offs entre estas tres propiedades. Entender estos trade-offs es crucial para elegir el mecanismo apropiado según el contexto.

#### Gitcoin Passport: Agregación Multi-Fuente

[Gitcoin Passport](https://passport.gitcoin.co) se ha convertido en el estándar de facto para verificación de humanidad en el ecosistema Ethereum mediante un enfoque de agregación de señales diversas.

**Arquitectura técnica**:

El sistema funciona como un agregador de "stamps" (sellos) donde cada stamp representa una verificación independiente. Conectas tu wallet y luego vinculas diferentes aspectos de tu identidad digital:

- **Web2 Social**: Cuentas de Google, Twitter, GitHub, Discord, Facebook, LinkedIn
- **Web3 Native**: ENS domain, tenencia histórica de ETH/tokens, participación en protocolos DeFi
- **Cross-verification**: BrightID, Proof of Humanity, Idena
- **Behavioral**: Antigüedad de cuentas, patrones de actividad, interacciones auténticas

Cada stamp contribuye puntos a tu **Humanity Score** total según un algoritmo sofisticado que pondera:
- **Antigüedad**: Cuenta de GitHub con 5 años de historia vale más que una recién creada
- **Costo de falsificación**: ENS domain ($5/año) es más costoso de falsificar a escala que cuenta de Twitter gratuita
- **Correlación**: Stamps que raramente aparecen juntos en cuentas Sybil reciben peso mayor cuando se combinan

**Almacenamiento descentralizado**:

Las credenciales se almacenan en [Ceramic Network](https://ceramic.network), no en servidores de Gitcoin. Tú controlas completamente qué stamps revelar a cada aplicación mediante selective disclosure: puedes mostrar tu verificación de Google a una aplicación pero no tu cuenta de Twitter a otra, manteniendo privacidad granular.

**Umbrales de confianza**:

- Score 0-10: Cuenta nueva o con verificación mínima, alto riesgo Sybil
- Score 10-20: Humano probable, aceptable para casos de uso de bajo riesgo
- Score 20-30: Humano verificado, estándar para airdrops y votaciones
- Score 30+: Alta confianza, para aplicaciones críticas o privilegi os especiales

**Adopción masiva**:

Más de 1,000 aplicaciones integran Gitcoin Passport para protección anti-Sybil, incluyendo Optimism, Arbitrum, zkSync, Polygon, y prácticamente todo airdrop significativo post-2022. El protocolo ha verificado más de 2 millones de identidades únicas, estableciendo el mayor grafo de identidad descentralizada verificable.

**Limitaciones y ataques**:

- **Farms sofisticados**: Atacantes con recursos pueden crear cuentas Google/Twitter antiguas y farmar ENS domains, aunque el costo escala linealmente
- **Compra de cuentas**: Mercados grises venden cuentas verificadas de Google/GitHub, aunque Gitcoin actualiza constantemente algoritmos para detectar patrones
- **Privacidad limitada**: Aunque Ceramic permite selective disclosure, vincular múltiples stamps Web2 a una wallet crea superficie de ataque para deanonimización

#### Worldcoin: Biometría con Zero-Knowledge

[Worldcoin](https://worldcoin.org), cofundado por Sam Altman (CEO de OpenAI), representa el enfoque más audaz mediante biometría de iris combinada con criptografía de preservación de privacidad.

**Arquitectura técnica**:

1. **Orb scanning**: Dispositivos especializados llamados Orbs escanean el iris del usuario, capturando patrones únicos con cámaras de alta resolución.

2. **Generación de hash biométrico**: El patrón de iris se procesa localmente en el Orb mediante algoritmos propietarios para generar un hash único. Crucialmente, la imagen del iris no se almacena ni transmite, solo el hash resultante.

3. **Registro on-chain con ZK**: El hash se registra en el blockchain de Worldcoin (Optimism fork) mediante una transacción que usa zero-knowledge proofs. El ZK-proof demuestra que:
   - Este hash de iris no ha sido registrado previamente (unicidad)
   - El proceso de scanning siguió el protocolo correcto
   - Sin revelar el hash mismo ni permitir correlación entre transacciones

4. **World ID**: El usuario recibe un World ID único que puede usar para probar humanidad verificada en aplicaciones sin exponer su biometría.

**Garantías de privacidad**:

- **No hay base de datos centralizada de iris**: Los hashes biométricos están distribuidos en blockchain, no en servidores de Worldcoin
- **Imposibilidad de reconstruir iris**: Los hashes son unidireccionales, matemáticamente imposible reconstruir el iris original
- **Anonimato de uso**: Cuando usas tu World ID, la aplicación solo ve "humano verificado #XYZ", no tu información biométrica

**Controversy y consideraciones**:

La controversia es sustancial y multifacética:

**Riesgos de privacidad**: A pesar de las garantías criptográficas, recopilar biometría crea riesgos inherentes. Si los Orbs son comprometidos o el algoritmo de hashing tiene vulnerabilidades, podría filtrarse información sensible. Gobiernos autoritarios podrían forzar a Worldcoin a modificar Orbs para almacenar imágenes completas de iris.

**Centralización de hardware**: Los Orbs son dispositivos propietarios fabricados y distribuidos centralizadamente. Esto crea single point of failure y dependencia en la fundación Worldcoin. Aunque el protocolo aspira a descentralización, el hardware permanece centralizado.

**Exclusión geográfica**: Orbs solo están disponibles en ciertas ciudades de ciertos países. Esto crea disparidad de acceso donde residentes de países desarrollados tienen ventaja sobre residentes de países donde Worldcoin no opera.

**Regulación legal**: Varios países (España, Francia, Kenya) han prohibido o restringido Worldcoin por preocupaciones de protección de datos bajo GDPR y legislaciones similares. La viabilidad a largo plazo depende de navegar marcos regulatorios incompatibles.

**Adopción y escala**:

A pesar de las controversias, Worldcoin ha verificado más de 5 millones de identidades globalmente (Enero 2026) y procesa cientos de miles de verificaciones mensuales. Protocolos DeFi como [Uniswap](https://uniswap.org) y marketplaces NFT experimentan con World ID para access gating y prevención de bots.

#### Proof of Humanity: Verificación Social en Video

[Proof of Humanity](https://www.proofofhumanity.id) implementa un registro curado por humanos mediante videos de verificación y desafíos económicos.

**Proceso de registro**:

1. **Submisión de perfil**: Usuario crea perfil con nombre, foto, y video corto (20 segundos) donde se muestra sosteniendo un papel con su dirección Ethereum y el texto "I certify that I'm a real human and that I'm not already registered in this registry".

2. **Depósito de seguridad**: Usuario deposita ETH como stake (típicamente 0.125 ETH). Este depósito protege contra spam y se devuelve tras verificación exitosa.

3. **Periodo de desafío**: La submisión entra en periodo de challenge (3-7 días) donde cualquiera puede disputarla si cree que es falsa, duplicada, o viola las reglas.

4. **Arbitraje via Kleros**: Si hay disputa, el caso se escala a [Kleros Court](https://kleros.io), una plataforma de arbitraje descentralizado donde jurados analizan evidencia y votan. Si la submisión es legítima, el challenger pierde su stake. Si es fraudulenta, el submitter pierde su deposit.

5. **Renovación periódica**: El registro expira anualmente y debe renovarse con nuevo video, previniendo registros zombies y permitiendo detección de duplicados que surgen con el tiempo.

**Trade-offs del sistema**:

✅ **Ventajas**:
- Resistencia Sybil extremadamente fuerte: falsificar identidades requiere videos únicos de personas reales diferentes, físicamente imposible a escala
- Descentralizado: No hay entidad central que aprueba, la comunidad verifica mediante incentivos económicos
- Recuperable: Si pierdes acceso a tu wallet, puedes re-registrarte con nuevo video desde nueva dirección

❌ **Desventajas**:
- Privacidad cero: Tu video, foto y nombre están públicos on-chain permanentemente
- Barrera de entrada: Depositar 0.125 ETH excluye a usuarios de países con economías débiles
- Susceptible a desafíos maliciosos: Atacantes pueden disputar registros legítimos forzándote a pagar fees de arbitraje para defender
- Escalabilidad limitada: Procesar videos manualmente es lento, solo ~15,000 humanos registrados (Enero 2026)

**Integración con UBI y sistemas económicos**:

Proof of Humanity fue diseñado originalmente para distribuir [UBI token](https://www.democracy.earth), un experimento de ingreso básico universal donde cada humano verificado recibe tokens periódicamente por el simple hecho de existir. La premisa es que en sociedades post-escasez o economías con automatización masiva, todos los humanos deberían recibir sustento básico.

#### BrightID: Web of Trust Social

[BrightID](https://www.brightid.org) implementa el modelo de web of trust donde la confianza emerge de conexiones sociales verificables y transitivas.

**Arquitectura de verificación**:

1. **Conexiones iniciales**: Nuevos usuarios se conectan con usuarios existentes que conocen en la vida real, estableciendo el grafo social base.

2. **Sesiones de verificación**: Para alcanzar estatus "Verified", debes participar en sesiones de verificación en video (usualmente via Zoom) donde múltiples humanos ya verificados te conocen y confirman tu identidad única.

3. **Análisis de grafo social**: El algoritmo BrightID analiza el grafo de conexiones usando métricas como:
   - **Clustering coefficient**: Usuarios legítimos tienen conexiones recíprocas formando clusters densos. Bots Sybil crean grafos dispersos tipo star.
   - **Temporal patterns**: Conexiones genuinas se forman gradualmente. Farms Sybil conectan cientos de cuentas simultáneamente.
   - **Behavioral consistency**: Humanos reales tienen patrones de uso orgánicos, bots tienen patrones repetitivos detectables.

4. **Niveles de verificación**: BrightID asigna confianza incremental:
   - **Connected**: Tienes algunas conexiones, confianza mínima
   - **Verified**: Pasaste sesión de verificación, confianza media
   - **Seed**: Contribuidor activo con muchas verificaciones exitosas, confianza máxima

**Trade-offs del sistema**:

✅ **Ventajas**:
- Privacidad moderada: No requieres revelar identidad legal, solo participar en verificación social
- Costo cero: No hay deposits económicos necesarios
- Resistencia Sybil fuerte: Crear miles de identidades verificadas requiere engañar a miles de humanos reales en sesiones de video

❌ **Desventajas**:
- Bootstrapping difícil: Si no conoces a nadie en BrightID, es complicado empezar
- Centralización de coordinación: Aunque el protocolo es descentralizado, las sesiones de verificación son coordinadas semi-centralizadamente
- Susceptible a colusión: Grupos de atacantes pueden verificarse mutuamente creando clusters Sybil aislados

**Uso en ecosistema**:

BrightID se integra principalmente con Gitcoin Passport como uno de los stamps de verificación. También es usado por aplicaciones de votación y distribución de recursos donde Sybil resistance es crítica pero privacidad biométrica estricta no es requerida.

**Comparación final de mecanismos PoP**:

| Mecanismo | Descentralización | Privacidad | Resistencia Sybil | Costo | Escalabilidad |
|-----------|------------------|------------|-------------------|-------|---------------|
| Gitcoin Passport | Media | Media | Media | Bajo | Alta |
| Worldcoin | Baja | Alta | Muy Alta | Bajo | Alta |
| Proof of Humanity | Alta | Muy Baja | Muy Alta | Alto | Baja |
| BrightID | Alta | Alta | Media | Bajo | Media |

No existe "mejor" solución universal. Gitcoin Passport optimiza para adopción pragmática agregando múltiples señales. Worldcoin maximiza resistencia Sybil mediante biometría pero sacrifica descentralización. Proof of Humanity prioriza descentralización y resistencia extrema a costa de privacidad. BrightID balancea privacidad y descentralización pero requiere esfuerzo social significativo.

El futuro probablemente implica interoperabilidad donde diferentes aplicaciones consumen diferentes mecanismos PoP según sus requisitos específicos de seguridad, privacidad y UX.

**Gitcoin Passport**:

[Gitcoin Passport](https://passport.gitcoin.co) se ha convertido en el estándar de oro para verificación de humanidad en el ecosistema Ethereum. La plataforma funciona como un agregador de "stamps" (sellos) que representan diferentes formas de verificación. Conectas tu wallet y luego vinculas diferentes aspectos de tu identidad digital: cuenta de Google, Twitter, GitHub, Discord, Facebook, LinkedIn, tenencia de ENS, participación en BrightID, holdings de criptomonedas, y docenas más.

Cada stamp contribuye puntos a tu Humanity Score total. El algoritmo que calcula cuántos puntos vale cada stamp es sofisticado y evoluciona constantemente para prevenir gaming. Por ejemplo, una cuenta de GitHub creada hace 5 años con contribuciones regulares vale más que una cuenta nueva, porque es mucho más costoso falsificar antigüedad y actividad genuina.

El Passport usa un modelo de datos descentralizado donde tus credenciales se almacenan en Ceramic Network, no en servidores de Gitcoin. Tú controlas completamente qué stamps revelar a cada aplicación. Podrías mostrar tu verificación de Google a una aplicación pero no tu cuenta de Twitter a otra, manteniendo privacidad granular.

Más de 1,000 aplicaciones integran Gitcoin Passport para protección anti-Sybil, incluyendo Optimism, Arbitrum, zkSync, y prácticamente todo airdrop significativo. Un score de 20+ se considera el mínimo para ser tratado como humano verificado, mientras que scores de 30+ indican usuarios de alta confianza.

**Worldcoin**:

[Worldcoin](https://worldcoin.org), cofundado por Sam Altman de OpenAI, representa el enfoque más audaz de Proof of Personhood mediante biometría. El proyecto distribuye dispositivos llamados Orbs que escanean tu iris, creando un hash biométrico único que se registra on-chain.

La promesa es resolver definitivamente el problema de unicidad: tu iris es único y no puede ser duplicado. El sistema usa zero-knowledge proofs para verificar que no has registrado previamente sin almacenar tu imagen biométrica real, preservando privacidad.

La controversia es sustancial. Críticos argumentan que recopilar biometría centralizada crea riesgos masivos de privacidad y vigilancia. El proyecto ha enfrentado prohibiciones o restricciones en varios países preocupados por protección de datos. Defensores responden que es el único mecanismo escalable para garantizar una persona = un voto en sistemas democráticos descentralizados.

Independientemente de la controversia, Worldcoin ha registrado más de 2 millones de usuarios globalmente y distribuido cientos de millones en grants condicionales a humanos verificados, demostrando demanda real por Proof of Personhood robusto.

**Spruce**:

[Spruce](https://spruce.systems) se enfoca en credenciales verificables que funcionan cross-chain y integran identidades Web2 y Web3. El proyecto desarrolló Sign-In with Ethereum (SIWE), un estándar que permite usar tu wallet Ethereum como método de autenticación en cualquier sitio web, similar a "Sign in with Google" pero descentralizado.

Spruce también trabaja en SpruceID, un sistema de credenciales verificables que permite demostrar atributos específicos sin revelar información innecesaria. Por ejemplo, podrías probar que vives en la Unión Europea sin revelar tu país específico, o que eres mayor de 21 sin revelar tu fecha de nacimiento exacta.

### 5.2 Construcción y Acumulación de Reputación

Estas plataformas permiten ganar reputación activamente mediante participación en ecosistemas Web3.

**RabbitHole**:

[RabbitHole](https://rabbithole.gg) gamifica el aprendizaje de Web3 mediante quests que requieren interacciones reales con protocolos. No se trata de quizzes de opción múltiple, sino de tareas on-chain verificables. Una quest típica podría ser "provee liquidez a un pool Balancer v2 con al menos tres tokens" o "vota en una propuesta de Compound Governance".

Al completar quests, ganas tokens (recompensas directas del protocolo que estás aprendiendo), XP (experiencia que se acumula en tu perfil RabbitHole), y frecuentemente SBTs que certifican que completaste ese desafío específico. El XP total y los SBTs coleccionados se convierten en un registro verificable de tu expertise en diferentes áreas de Web3.

Protocolos pagan a RabbitHole para crear quests porque es marketing extremadamente efectivo: consiguen usuarios que no solo instalaron una app sino que realmente entienden cómo funciona. RabbitHole ha facilitado más de $10 millones en recompensas a learners y generado millones de interacciones on-chain verificables.

**Layer3**:

[Layer3](https://layer3.xyz) funciona similarmente a RabbitHole pero con enfoque en diversidad de ecosistemas. Layer3 tiene quests no solo en Ethereum pero en Polygon, Arbitrum, Optimism, Solana, Cosmos, y docenas de otras chains. Esto permite construir reputación multi-chain.

La plataforma también introduce "bounties" donde proyectos publican tareas más complejas con recompensas mayores. Por ejemplo, un bounty podría ser "crea un thread de Twitter explicando el nuevo mecanismo de staking de Protocol X" combinando trabajo off-chain con verificación on-chain de que realmente entiendes el protocolo.

Layer3 ha distribuido más de $15 millones en recompensas y sus NFTs de completar quests son coleccionables que algunos usuarios comercian como status symbols de estar activos en el ecosistema.

**Galxe**:

[Galxe](https://galxe.com) (anteriormente Project Galaxy) es la plataforma de campaña más grande de Web3 con más de 3,000 partners. Proyectos lanzan campañas en Galxe donde usuarios completan tareas para ganar NFTs, tokens, o whitelist spots.

Lo que distingue a Galxe es su infraestructura de credenciales. Cada campaña completada genera un NFT credential on-chain que puede ser usado como requisito en otras campañas. Esto crea un grafo de dependencias donde completar campañas tempranas te califica para oportunidades más avanzadas.

Galxe también calcula un Galxe Score agregado basado en tu participación total en el ecosistema. Este score es usado por cientos de proyectos como filtro anti-Sybil para airdrops y distribuciones de tokens.

**Ethos Network**:

[Ethos Network](https://ethos.network) implementa un sistema único de reputación peer-to-peer donde usuarios se "vouches" mutuamente. Cuando voucho por ti, estoy apostando mi propia reputación en tu credibilidad. Si te comportas mal, mi score también baja.

El sistema crea un marketplace de confianza donde puedes buscar proveedores de servicios (desarrolladores, diseñadores, auditores) rankeados por sus vouches de gente con alta reputación. Es como LinkedIn pero donde las recomendaciones tienen consecuencias económicas reales.

Ethos también permite staking: puedes apostar ETH en tu propio perfil como señal de confianza en ti mismo, o en perfiles de otros como endorsement financiero. El stake puede ser slashed (confiscado) si hay comportamiento malicioso verificado, creando incentivos económicos alineados con reputación.

**Orange Protocol**:

[Orange Protocol](https://www.orangeprotocol.io) implementa el patrón de reputation oracles, proporcionando infraestructura para calcular y publicar scores de reputación on-chain basados en comportamiento DeFi verificable. El protocolo funciona como una capa de agregación entre datos on-chain brutos y aplicaciones que necesitan tomar decisiones basadas en reputación.

La arquitectura de Orange permite que comunidades y DAOs creen sus propios sistemas de reputación personalizados. En lugar de un algoritmo único que sirve a todos, Orange proporciona herramientas para que cada comunidad defina qué significa "buena reputación" en su contexto específico. Este enfoque contextual reconoce que reputación no es universal: lo que hace a alguien confiable como trader DeFi puede ser completamente diferente a lo que lo hace confiable como curator de NFTs.

**Credit Scoring On-Chain**:

Una aplicación crítica de Orange es credit scoring descentralizado. El protocolo puede agregar múltiples señales on-chain para calcular creditworthiness: historial de repago de préstamos previos, antigüedad de la wallet, diversidad de protocolos utilizados, volatilidad de balance, participación en gobernanza, y más. Estos scores son verificables y auditables, a diferencia de credit scores tradicionales que son opacos y controlados por agencias centralizadas.

Un protocolo de préstamos podría consultar el Orange score de un usuario para determinar términos de crédito personalizados. Un score alto podría calificar para ratios de colateralización más bajos (120% en lugar de 150%) o tasas de interés reducidas. El scoring es dinámico: tu reputación mejora con cada préstamo repagado exitosamente y se degrada si entras en default o comportamiento sospechoso.

**Modelos Especializados por Dominio**:

Una DAO de gaming podría valorar logros en juegos específicos y participación en torneos, usando Orange para crear un modelo que agrega data de múltiples juegos blockchain. Una DAO de DeFi valoraría volumen de trading, provision de liquidez, y participación en gobernanza. Una comunidad de creadores de contenido podría ponderar engagement rates, consistency de publicación, y endorsements de otros creadores.

Orange permite que estas comunidades diseñen algoritmos de scoring específicos para sus necesidades, definiendo qué fuentes de datos consultar, cómo ponderarlas, y qué umbral califica como "buena reputación". Los scores resultantes pueden emitirse como credenciales verificables o consultarse on-chain por smart contracts para tomar decisiones programáticas.

### 5.3 Credenciales, Badges y Proof of Attendance

Estas plataformas se especializan en emitir y gestionar credenciales no transferibles que representan logros, participación o membresía.

**Otterspace**:

[Otterspace](https://www.otterspace.xyz) se especializa en badges para DAOs. Mientras POAP se enfoca en eventos y Noox en logros automáticos, Otterspace facilita que DAOs emitan credenciales manualmente a sus miembros y contribuidores.

Una DAO podría crear badges como "Core Contributor 2024", "Governance Participant", "Grants Committee Member", o "Community Moderator". Estos badges son emitidos por la DAO mediante votación o mediante decisión de un comité específico, certificando roles y contribuciones.

Los badges de Otterspace son no transferibles pero pueden ser revocados por la DAO si alguien deja de cumplir su rol o se comporta mal. Esto los hace ideales para representar membresías y responsabilidades actuales en lugar de solo logros históricos.

Organizaciones como Optimism, Gitcoin, y MetaCartel usan Otterspace para gestionar credenciales de sus contribuidores, creando un sistema de reputación interno verificable.

**Sismo**:

[Sismo](https://sismo.io) implementa el patrón de zero-knowledge badges, permitiendo probar atributos específicos sin revelar tu identidad completa ni información adicional. Este enfoque resuelve la tensión fundamental entre reputación verificable y privacidad personal que caracteriza a muchos sistemas de identidad descentralizada.

El patrón arquitectónico funciona así: mantienes múltiples direcciones Ethereum (tu dirección pública para transacciones diarias, tus wallets de inversión, tus cuentas de gobernanza DAO) pero quieres probar algo sobre todas ellas agregadamente sin vincularlas públicamente. Sismo te permite generar un badge ZK que certifica "poseo más de 10 ETH agregado en múltiples wallets" sin revelar qué direcciones específicas controlas ni tu balance exacto.

**Casos de Uso Técnicos**:

En contextos de gobernanza, Sismo permite votación anónima pero verificable. Puedes probar que eres elegible para votar (porque posees el token de gobernanza requerido) sin revelar qué dirección específica posee esos tokens. Esto previene compra de votos porque los votantes no pueden demostrar convincentemente cómo votaron sin comprometer su privacidad permanentemente.

Para acceso a comunidades exclusivas, Sismo permite probar membresía sin exposición pública. Por ejemplo, podrías demostrar que eres holder de un NFT de Bored Ape Yacht Club para acceder a un evento privado, pero sin revelar qué ape específico posees. Esto preserva privacidad financiera mientras mantiene verificabilidad de criterios de acceso.

Otro caso poderoso es la agregación de reputación cross-wallet. Un developer podría tener contribuciones en GitHub vinculadas a una wallet, actividad DeFi en otra por privacidad, y participación en DAOs en una tercera. Con Sismo, puede generar un badge que prueba "he contribuido a 5+ protocolos diferentes" sin vincular públicamente todas estas identidades.

**Arquitectura de Data Vaults**:

Sismo funciona mediante Data Vaults donde tus datos se almacenan de forma privada y selectivamente generas proofs sobre ellos. Cuando necesitas probar algo, el sistema genera una prueba ZK-SNARK que verifica la declaración sin exponer los datos subyacentes. El verificador puede confirmar matemáticamente que la prueba es válida sin jamás ver tu balance, direcciones o transacciones específicas.

Esta tecnología es crucial para casos de uso donde la reputación debe ser verificable pero la privacidad es crítica: periodistas que necesitan probar credenciales sin exponerse, activistas que quieren participar en gobernanza sin riesgo político, o simplemente usuarios que valoran privacidad financiera pero necesitan probar solvencia.

### 5.4 Visualización y Análisis

Estas herramientas permiten visualizar y analizar reputación agregada de forma comprensible.

**DeBank**:

[DeBank](https://debank.com) es el dashboard más popular para visualizar portfolios DeFi completos. Conectas tu wallet y ves instantáneamente todos tus holdings a través de Ethereum, BSC, Polygon, Arbitrum, y 30+ otras chains.

Para reputación, DeBank muestra tu historial completo de interacciones: protocolos que has usado, NFTs que posees, POAPs coleccionados, y transacciones históricas. También calcula métricas como cuántos días has sido activo, valor total bloqueado histórico, y diversidad de protocolos utilizados.

DeBank permite crear un perfil público con handle personalizado, permitiendo que compartas tu reputación DeFi fácilmente. Algunos usuarios incluyen su perfil DeBank en CVs o aplicaciones a DAOs como prueba de experiencia verificable.

**Etherscan**:

[Etherscan](https://etherscan.io) es el block explorer estándar para Ethereum, pero también funciona como herramienta de verificación de reputación. Cualquiera puede ver el historial completo de transacciones de una dirección, qué contratos ha interactuado, cuánto gas ha gastado total, y la antigüedad de la cuenta.

Para reputación, Etherscan permite verificar claims objetivamente. Si alguien dice que fue early adopter de Uniswap, puedes revisar su dirección y ver si realmente tiene transacciones con Uniswap desde 2019. Si alguien afirma experiencia en DeFi, puedes ver la diversidad y sofisticación de sus interacciones on-chain.

Etherscan también muestra labels públicos aplicados a direcciones conocidas (exchanges, protocolos famosos, scammers identificados), ayudando a contextualizar con quién ha interactuado una dirección.


