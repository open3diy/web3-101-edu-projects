# Reputación Web3

En [identidad Web3](7-1-identity.md) vimos cómo esta responde a la pregunta *quién eres* mediante atributos verificables y reputación, por eso está tan relacionado.

La reputación responde a una pregunta distinta: *qué has hecho y qué autoridad has acumulado por ello*. No es un perfil estático que un emisor externo te otorga, sino un historial dinámico que construyes con cada acción verificable on-chain.

Esta distinción importa porque cambia quién tiene poder para definirte. Tu identidad depende en gran medida de emisores con autoridad reconocida —una universidad, un proveedor KYC, un protocolo de prueba de humanidad—. Tu reputación, en cambio, emerge de la propia red: quién te sigue, qué DAOs te aceptan como contribuidor, cuántas propuestas has votado, qué protocolo llevas años usando. Nadie te la concede; la acumulas acción a acción.

La reputación en Web3 determina mucho más de lo que tienes: dice lo que eres. Es un concepto fundamental para la gobernanza efectiva en DAOs y para la participación en el ecosistema, porque la influencia no debería reducirse solo a los tokens que posees —lo que derivaría en plutocracia— sino también a si eres un humano real activo y comprometido, algo muy relevante en muchas decisiones colectivas.

El concepto fundamental detrás de la reputación Web3 es la creación de lo que Vitalik Buterin y otros investigadores denominan "juicio colectivo programable". Esta idea, explorada en profundidad en el paper [Decentralized Society: Finding Web3's Soul](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763), plantea que la confianza y la coordinación social pueden codificarse on-chain sin depender de autoridades centrales.

Como participante en este ecosistema emergente, cada interacción on-chain que haces, cada credencial que ganas, cada contribución que realizas, no solo construye tu reputación personal sino que también ayuda a definir qué significa reputación en el futuro descentralizado que estamos construyendo juntos.

Las primitivas técnicas con las que la reputación cobra vida —SBTs, POAPs y atestaciones EAS— son las mismas que soportan la identidad on-chain, ya que el ecosistema utiliza las mismas herramientas para propósitos distintos. Aquí las exploraremos con el foco puesto en cómo se convierten en instrumentos de reputación: cómo se construyen, agregan y utilizan para determinar influencia, acceso y peso en la gobernanza.

## Visión de la Reputación

La reputación Web3 representa uno de los experimentos socio-técnicos más ambiciosos de nuestra era. Estamos intentando construir sistemas de confianza y coordinación que funcionan globalmente sin autoridades centrales, que resisten censura y manipulación, y que empoderan individuos en lugar de corporaciones.

El camino está lleno de desafíos técnicos sin resolver, dilemas éticos complejos, y incertidumbre regulatoria. Pero el potencial es transformador: un mundo donde tu reputación es portátil, verificable, y verdaderamente tuya. Donde la contribución importa tanto como el capital. Donde la confianza se construye mediante acciones verificables, no mediante intermediarios que pueden manipular o censurar.

Si los sistemas de reputación Web3 tienen éxito, podrían transformar fundamentalmente cómo funciona la coordinación humana a escala global.

**Reputación como Capital Social Tokenizable**:

En lugar de capital financiero siendo la única forma de participar en economía, la reputación se convierte en un activo igualmente valioso y líquido. Alguien sin dinero pero con excelente reputación on-chain puede acceder a capital, oportunidades e influencia.

Podría democratizar el acceso de forma significativa. Un desarrollador talentoso en Nigeria con reputación on-chain verificable tiene las mismas oportunidades que uno en Silicon Valley. Una artista en Indonesia puede construir audiencia global basándose puramente en la calidad de su trabajo verificable on-chain.

**Gobernanza Global Post-Plutocrática**:

Los sistemas de votación puramente financieros (one dollar, one vote) concentran poder en manos de los más ricos. Los sistemas de reputación permiten modelos más sofisticados donde el expertise, la participación histórica y la contribución importan tanto como el capital.

Esto podría permitir que las DAOs gobiernen recursos digitales compartidos —como protocolos open source o fondos de bienes públicos— de forma más justa y legítima: quien más ha contribuido y participado tiene más peso en las decisiones, no solo quien más capital ha invertido.

**Identidad Universal Portable**:

Tu reputación on-chain se convierte en tu identidad universal que llevas a través de todas las plataformas, aplicaciones, y contextos. En lugar de crear perfiles nuevos en cada aplicación, simplemente conectas tu wallet y toda tu reputación relevante es inmediatamente visible y verificable.

Esto reduce la fricción drásticamente. No más CVs, no más entrevistas repetitivas, no más probar las mismas cosas una y otra vez. Tu historial on-chain habla por sí mismo.

**Fin de la Economía de Reputación Extractiva**:

En Web2, las plataformas poseen tu reputación. Tus reviews de Uber, tu rating de Airbnb, tu karma de Reddit, todo pertenece a esas corporaciones. Si te bannean o la plataforma cierra, pierdes años de reputación acumulada.

Web3 invierte esto: tú posees completamente tu reputación y las plataformas son intercambiables. Si una aplicación social te trata mal, migras a otra llevando todos tus seguidores y contenido. Como ninguna plataforma puede retenerte atrapando tus datos, su único recurso es ofrecerte un servicio genuinamente mejor que el de la competencia.

Esto podría crear economía digital más justa donde el valor se acumula en usuarios que generan contenido y construyen comunidades, no en plataformas que meramente intermedian.

## Riesgos y Desafíos

Los sistemas de reputación Web3 heredan las tensiones propias de blockchain: lo que los hace robustos y descentralizados también generan riesgos y desafíos por considerar.

### Límites Técnicos

Los sistemas de reputación en Web3 se construyen sobre infraestructura descentralizada, lo que introduce desafíos tecnológicos específicos que aún no están resueltos del todo. Estos límites afectan cómo se registra, interpreta y traslada la reputación.

**Inmutabilidad y Errores de Lógica**:

La reputación Web3 hereda la naturaleza inmutable de la blockchain. Si el smart contract encargado de calcular o emitir credenciales tiene un error de diseño, los registros generados con esa lógica defectuosa quedarán guardados permanentemente. Aunque el contrato pueda actualizarse para el futuro, corregir retroactivamente el daño o la reputación mal asignada es técnicamente complejo y a menudo imposible sin crear un sistema paralelo.

**Falta de Interoperabilidad y Estándares**:

Existen iniciativas serias de estandarización: la [Chain Agnostic Standards Alliance (CASA)](https://chainagnostic.org/) publica CAIPs que resuelven cómo identificar cadenas, cuentas y activos de forma universal; el W3C mantiene los estándares de [DIDs](https://www.w3.org/TR/did-core/) y [Verifiable Credentials](https://www.w3.org/TR/vc-data-model/) como base interoperable para credenciales digitales; y EAS se ha convertido en el formato de facto para atestaciones en el ecosistema Ethereum. El problema no es ausencia de estándares, sino fragmentación en cómo los protocolos de reputación los adoptan e interpretan. Gitcoin Passport, Proof of Humanity y BrightID comparten la misma capa conceptual pero definen criterios de elegibilidad y arquitecturas incompatibles entre sí. La reputación acumulada en un ecosistema rara vez es interoperable o traducible de forma directa a otro, no porque no existan estándares comunes para expresar credenciales, sino porque cada protocolo decide qué emisores reconoce y qué señales considera válidas. La componibilidad técnica es posible; la componibilidad social —el acuerdo sobre qué vale qué— sigue sin resolverse.

**Fragmentación del Estado entre Cadenas**:

La capa anterior describe la fragmentación de estándares entre protocolos. Hay una segunda dimensión igual de estructural: la fragmentación del historial del mismo usuario entre cadenas distintas. Un usuario puede tener un historial de gobernanza impecable en Base, ser un completo desconocido en Arbitrum y acumular una década de reputación profesional en LinkedIn. El problema es que los contratos inteligentes están aislados por diseño: no pueden leer lo que ocurre en otras cadenas ni lo que existe en servidores tradicionales. El resultado es una reputación inevitablemente dispersa que el protocolo receptor no puede agregar sin introducir alguna forma de confianza externa.

El ecosistema ha desarrollado varias estrategias para manejarlo. La más austera delega la prueba al propio usuario: las atestaciones off-chain de EAS viajan como documentos portátiles firmados por un emisor reconocido, que cada aplicación verifica localmente sin consultar otra cadena. Para importar credenciales del mundo Web2 —historial bancario, reputación en plataformas cerradas— herramientas de zkTLS generan pruebas criptográficas de datos privados sin revelarlos. Cuando una aplicación necesita orquestar acciones automáticas entre cadenas, protocolos de mensajería como CCIP propagan el estado de identidad desde un hub hacia los spokes donde operan las dApps. Construir sobre grafos sociales unificados como Lens o Farcaster evita el problema desde la raíz: la identidad reside en el protocolo y las aplicaciones son ventanas sobre el mismo estado compartido. Ninguna estrategia resuelve todos los casos sin compromisos, ya sea en confianza, coste o complejidad operacional. El análisis completo de estas opciones está en [fragmentación del estado y portabilidad cross-chain](../infrastructure/ethereum/reputation-state-fragmentation.md).

**Privacidad frente a Verificabilidad**:

La transparencia por defecto de la blockchain pública entra en conflicto con el derecho a la privacidad. Para que una credencial funcione como reputación, suele ser visible para todos, lo que permite trazar el comportamiento y las afiliaciones de una persona. Aunque existen soluciones criptográficas como las pruebas de conocimiento cero para proteger los datos, integrarlas en los sistemas de reputación actuales añade una enorme complejidad computacional que aún limita su uso masivo.

> Algo que por cierto ya analizamos en parte en [el desafío de la privacidad](4-3-challenges-privacy.md).

**Sesgo Cuantitativo y de Dominio**:

Hay además un sesgo conceptual que vale la pena nombrar. Los sistemas actuales de reputación Web3 miden lo tangible y verificable: transacciones, votos, badges. Esto responde a una visión muy práctica de lo que significa contribuir. La confianza, la capacidad de escuchar, la habilidad para resolver conflictos o formar a otros no dejan rastro on-chain fácilmente medible. No es un fallo técnico resoluble con mejores herramientas, sino una limitación de qué tipo de realidad puede representar un protocolo. Y el riesgo derivado es conocido: inferir competencias de un dominio a otro. Que alguien sea un desarrollador excelente no dice nada sobre si será un buen coordinador de DAO o un buen mentor. La reputación on-chain puede reforzar este salto lógico si no se diseña con cuidado.

### Manipulación y Confianza

Cuanto más valioso es un sistema, más incentivos hay para engañarlo. La reputación Web3 no es una excepción.

La forma más directa de manipularlo es crear muchas identidades falsas para acumular reputación en masa y luego utilizarla para votar, obtener acceso o recibir recompensas que no corresponden a una participación real. Esto se conoce como ataque Sybil. Pero existe una variante más sutil y difícil de detectar: usar una identidad legítima —una wallet real, con historial real— para simular participación sin tener ninguna intención genuina. Por ejemplo, votar en propuestas sin leerlas, completar tareas de forma mecánica para acumular puntos, o ponerse de acuerdo con conocidos para intercambiarse credenciales mutuamente. Desde fuera, todo parece actividad auténtica. Por eso es tan complicado de frenar.

Para reducir este comportamiento, algunos sistemas aplican un principio sencillo: la reputación pierde valor si no se mantiene activa, o bien las ultimas acciones cuentan más que las repetidas, de modo que acumular en masa resulte menos rentable. Estas medidas dificultan el abuso, pero no lo eliminan del todo.

Hay además un problema de fondo que ninguna regla técnica sobre "intransferibilidad" puede resolver: aunque credenciales como los SBTs no se puedan mover de una cuenta a otra, **la cuenta entera puede cambiar de dueño**. Por un lado, existen mercados informales oscuros donde se compran y venden llaves privadas de wallets antiguas con reputación acumulada por miles de dólares. El estándar [ERC-6551](https://eips.ethereum.org/EIPS/eip-6551) (*Token Bound Accounts*) amplifica este vector de forma indirecta: al permitir que cualquier NFT tenga su propia smart contract wallet, crea una cuenta secundaria que puede acumular tokens, credenciales y SBTs bajo ese NFT como contenedor raíz. Esto tiene valor genuino para casos como personajes de juegos con inventario verificable o carteras temáticas de activos relacionados, pero introduce una consecuencia directa para la reputación: transferir el NFT raíz transfiere automáticamente toda su wallet asociada y, con ella, cada credencial acumulada dentro. Lo que el contrato declara intransferible a nivel individual se vuelve indirectamente vendible a través del NFT que lo contiene. La solución de diseño es simple pero exige disciplina por parte del emisor: las credenciales de reputación deben emitirse siempre a la dirección principal del usuario —su EOA o su smart contract wallet—, nunca a una token-bound account derivada de un NFT. ERC-6551 no es en sí mismo el problema; el problema es emitir reputación a una dirección cuyo control puede transferirse junto con el token que la originó.

### Inclusión y Exclusión Estructural

El problema no es el coste de las transacciones —los L2 lo han resuelto en gran medida— sino que los mecanismos de reputación están construidos sobre historial on-chain acumulado en el tiempo. Quien llega hoy parte de cero: no tiene transacciones pasadas, no ha votado en ninguna propuesta, no ha completado ningún bounty. Los sistemas de scoring interpretan esa ausencia como señal negativa, independientemente de la capacidad real del nuevo participante.

Esta dinámica tiene nombre en sociología: el [efecto Mateo](https://en.wikipedia.org/wiki/Matthew_effect), formulado por Robert K. Merton a partir del evangelio de Mateo («al que tiene se le dará más»). En sistemas de reputación Web3 opera sin necesidad de intención: las DAOs delegan trabajo a wallets con historial consolidado, los protocolos conceden acceso preferencial a cuentas antiguas, y los sistemas de scoring amplifican las ventajas de quienes ya las tienen. Estudios sobre redes descentralizadas como [Measuring Decentralization in Web3 Social Networks](https://arxiv.org/abs/2302.10825) muestran que la concentración en estos sistemas reproduce, y a veces amplifica, la del mundo off-chain.

Hay una segunda dimensión del mismo problema: el historial relevante de una persona no empieza en blockchain. Un contribuidor con diez años de experiencia en desarrollo open source, liderazgo comunitario o resolución de conflictos llega a Web3 con una reputación que el protocolo no puede ver porque no ocurrió on-chain. Importar esa credibilidad off-chain requiere oráculos o puentes de validación centralizados, y la blockchain solo puede registrar eventos deterministas: lo que no deja rastro programáticamente cuantificable —liderazgo, mentoría, capacidad de escucha— simplemente no existe para el sistema. Esto no es un límite técnico resoluble, sino una consecuencia estructural de medir únicamente lo verificable en cadena, algo que analizamos en detalle en [el desafío de integrar el mundo off-chain](4-4-challenges-off-chain-integration.md).

A estas dos barreras se suma una tercera, menos visible: participar activamente requiere navegar foros de gobernanza, leer propuestas técnicas en inglés y moverse por comunidades con normas no escritas heredadas de la cultura anglosajona de internet. No es exclusión intencional, pero su efecto práctico es el mismo.

### Regulación y Vacío Jurídico

El [GDPR europeo](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32016R0679) exige cosas que una blockchain, por diseño, no puede dar. Garantiza el derecho a borrar datos personales, pero una *attestation* on-chain es inmutable. Las soluciones técnicas que se intentan, como guardar la información fuera de la cadena (*off-chain*) o usar funciones de revocación que ocultan la credencial pero dejan su rastro, son parches que, estrictamente, no cumplen el espíritu de la norma.

Más delicado aún es el problema de la responsabilidad. Si un emisor publica una credencial falsa y eso causa un daño económico, ¿a quién se denuncia? No hay un juzgado claro ni una empresa identificable a la que exigir cuentas. El daño ocurre en el mundo real, pero no existe un remedio legal para solucionarlo.

Además, el uso de la reputación ya está entrando en terrenos altamente regulados en el mundo tradicional. Protocolos como [Spectral Finance](https://www.spectral.finance) usan el historial de la wallet para decidir las condiciones de un préstamo. En casi cualquier país, esto activa inmediatamente la normativa sobre *scoring* crediticio: el usuario tiene derecho a saber qué criterios se han usado, a reclamar si no está de acuerdo y a que se justifique la decisión. Nada de esto existe hoy en DeFi.

Todo apunta a que, a la larga, no se creará una ley especial a medida para Web3. Lo más probable es que se apliquen directamente las leyes que ya existen —sobre protección de datos, sobre crédito, contra la discriminación— a una tecnología que se construyó creyendo que las reglas del mundo tradicional no le afectaban.

## Primitivas de reputación basadas en emisor

La reputación on-chain no existe en abstracto: necesita mecanismos concretos para registrarse, verificarse y componerse. En estas primitivas, la confianza descansa en el emisor: una entidad con autoridad reconocida —un protocolo, una DAO, el organizador de un evento— certifica algo sobre ti, y el valor de la credencial depende directamente de cuánto confía el ecosistema en quien la emite.

### Soulbound Tokens

Los Soulbound Tokens (SBTs) son la primitiva técnica que hace posible la reputación on-chain no transferible. El concepto fue propuesto por Vitalik Buterin, Glen Weyl y Puja Ohlhaver en el paper [Decentralized Society: Finding Web3's Soul](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763): tokens permanentemente vinculados a una dirección que no pueden venderse ni transferirse. La motivación es directa —en el ecosistema NFT todo es comercializable, lo que destruye el valor de cualquier credencial digital; alguien podría vender el certificado de que completó un curso de Solidity a quien no tiene esos conocimientos—. Los SBTs resuelven esto a nivel de contrato: el smart contract rechaza activamente cualquier transferencia, registra quién emitió el token, a quién y cuándo, y permite que el emisor lo revoque si las circunstancias cambian. La estandarización técnica se recoge en el [EIP-4973 (Account-bound Tokens)](https://eips.ethereum.org/EIPS/eip-4973), que elimina las funciones `transfer()` y `approve()` presentes en ERC-721.

El paper introduce también el concepto de *Soul*: la suma total de SBTs que posee una dirección, representando su capital social verificable —educación, empleo, participación en comunidades, logros— en contraposición al capital financiero que expresan los tokens convencionales. La metáfora viene de los videojuegos RPG, donde los *soulbound items* son objetos vinculados al personaje que no puedes intercambiar porque su valor reside en que tú los ganaste.

Los casos de uso son concretos: certificar participación como desarrollador core en un protocolo, ponderar el voto en una DAO según historial de contribuciones en lugar de solo capital, emitir credenciales profesionales que no pueden falsificarse ni cederse.

**El desafío de la recuperación**:

La no-transferibilidad de los SBTs amplifica las consecuencias de perder las claves privadas: no puedes mover tus credenciales a una dirección nueva como harías con un NFT convencional. Las propuestas de 2022-2023 eran parches a nivel de protocolo que no escalaron porque no resolvían el problema de raíz. La solución llegó con AA (Account Abstraction): con ERC-4337 y EIP-7702 (Pectra, 2025), las smart contract wallets con recuperación social por guardianes son infraestructura real hoy —Argent y Safe llevan años en producción—. Lo que en 2022 parecía un defecto estructural de los SBTs es, en 2026, un problema resuelto de gestión de claves.

Un desafío adicional es la privacidad: los SBTs públicos on-chain exponen toda la historia de una persona. Las soluciones emergentes combinan ZK-proofs para demostrar posesión de credenciales sin revelarlas (proyectos como [Sismo](https://sismo.io)), almacenamiento encriptado de metadata off-chain con solo el hash registrado on-chain, y arquitecturas de disclosure selectivo que permiten revelar solo el subconjunto relevante según el contexto.

**¿Se usan los SBTs hoy?**

El concepto está vivo, pero el término "SBT" no dominó el ecosistema. Lo que triunfó en la práctica es la misma idea bajo otro nombre: las attestations de [Ethereum Attestation Service (EAS)](https://attest.sh). Gitcoin Passport emite stamps como attestations EAS; Optimism las usa para certificar participación en su ecosistema. La diferencia es técnica y de posicionamiento, no conceptual: una attestation EAS es exactamente lo que el paper describía como SBT, solo que en un estándar más interoperable que terminó imponiéndose.

Lo que fracasó fue el modelo de plataforma standalone centrada en SBTs. Otterspace, discontinuado, apostó por que las DAOs emitieran sus propios badges —nombre habitual para estos tokens cuando representan un logro concreto, por analogía con las insignias físicas de mérito— actuando como entidades certificadoras, pero las DAOs no tenían incentivo suficiente para mantener esa infraestructura cuando el valor dependía de que otras aplicaciones reconocieran los badges, y ese ecosistema nunca llegó a escala crítica. [Noox](https://noox.world), que pausó operaciones en 2023, intentó el modelo opuesto con emisión automática basada en historial on-chain, pero sin una comunidad que reconociera esos badges (medallas) como señal de algo, acumularlos no tenía utilidad práctica. Los badges valen lo que valen quienes los aceptan.

### Ethereum Attestation Service (EAS)

[Ethereum Attestation Service (EAS)](https://attest.sh) es la infraestructura neutral que convirtió la idea de los SBTs en protocolo operativo a escala. Su premisa es simple: cualquier entidad —un protocolo, una DAO, un usuario— puede hacer declaraciones verificables sobre cualquier otra entidad, y esas declaraciones quedan registradas de forma interoperable. Donde los SBTs se planteaban como tokens vinculados a un alma, EAS generaliza el concepto hasta convertirlo en un primitivo de propósito general: la attestation, una firma criptográfica que afirma algo sobre alguien en un contexto específico.

El protocolo se articula en dos componentes. El primero es el registro de schemas: antes de emitir una attestation, el emisor define su estructura —qué campos contiene, qué tipo de datos y con qué semántica—. Un schema de "Contribuidor DAO" podría incluir dirección del contribuidor, nombre de la DAO, tipo de contribución y timestamp. El segundo componente es el registro de attestations propiamente dicho, que almacena cada declaración vinculada a su schema, con el emisor, el destinatario, la fecha y la posibilidad de revocación.

Las attestations pueden ser on-chain, registradas directamente en Ethereum o en las L2 donde EAS está desplegado, u off-chain, firmadas criptográficamente pero almacenadas fuera de la cadena para reducir costes, con solo el hash on-chain. Esta flexibilidad es clave: permite que protocolos con millones de usuarios emitan credenciales sin hacer la economía inviable.

Lo que convirtió a EAS en el estándar emergente no fue la tecnología sino la adopción coordinada. Gitcoin Passport migró sus stamps a attestations EAS, convirtiendo cada verificación de identidad —cuenta de GitHub con dos años de antigüedad, participación en Gitcoin Grants, holdings de tokens— en una credencial interoperable. Optimism usa EAS para certificar participación en su ecosistema y distribuir RetroPGF. Coinbase emite attestations de verificación de identidad (Coinbase Verified ID) que cualquier protocolo puede consultar. El resultado es un grafo creciente de credenciales cruzadas donde la confianza se propaga de emisor en emisor.

La diferencia práctica respecto a los SBTs no es técnica sino de estándar. Una attestation EAS puede expresar exactamente lo mismo que un SBT —no transferibilidad, emisor conocido, estado de revocación— pero en un formato que cualquier aplicación integrada con EAS puede leer directamente. En lugar de un ecosistema fragmentado de contratos ERC-4973 incompatibles entre sí, EAS ofrece un registro compartido donde la composabilidad es la norma.

**Limitaciones**:

EAS resuelve el problema de interoperabilidad técnica, pero traslada el problema de confianza a una capa superior: la del emisor. El protocolo no verifica si lo que afirma una attestation es verdad, solo que fue firmada por quien dice haberla emitido. Una attestation de "desarrollador senior" emitida por una DAO desconocida vale exactamente lo que vale esa DAO como institución —que puede ser nada—. La cadena de confianza sigue dependiendo de que haya actores con reputación consolidada dispuestos a emitir, y en la práctica eso concentra el valor en unos pocos emisores reconocidos: Gitcoin, Coinbase, Optimism. El protocolo es abierto, pero el ecosistema útil es estrecho.

Un segundo problema es la proliferación de schemas incompatibles. Cualquiera puede registrar un schema, y el resultado predecible es que para el mismo concepto —"contribuidor de DAO", "asistente a conferencia", "auditor verificado"— existen decenas de schemas sin coordinación. La promesa de composabilidad se degrada si no hay convención sobre qué schemas usar, y EAS no tiene mecanismo nativo de curaduría o descubrimiento. La interoperabilidad real exige esfuerzo social de coordinación que el protocolo no puede sustituir.

Las attestations off-chain resuelven el coste pero reintroducen dependencias de almacenamiento centralizado: el hash queda on-chain, pero el contenido vive en IPFS o en servidores propios del emisor. Si el emisor desaparece o deja de pinear sus archivos en IPFS, las attestations se convierten en referencias rotas. Es el mismo punto de fragilidad que afecta a la metadata de los NFTs, resuelto de forma incompleta.

### POAP (Proof of Attendance Protocol)

[POAP](https://poap.xyz) es el estándar de facto para certificar presencia en Web3: cada token es un NFT ERC-721 emitido en Gnosis Chain que registra que estuviste en un evento concreto en una fecha concreta. El organizador distribuye los tokens mediante QR codes, claim links o envío directo; la restricción de una reclamación por dirección y la ventana temporal reducida son los mecanismos principales para desincentivar el farming. Los casos de uso van desde conferencias como ETHDenver —que emite POAPs diferenciados por taller, rol o side event— hasta DAOs que los usan para certificar participación en calls de gobernanza, votes on-chain o contribuciones de contenido.

**POAPs como señal de reputación**:

Su valor no está en el token en sí sino en lo que otros hacen con él. [Guild.xyz](https://guild.xyz) es una herramienta que permite a comunidades definir reglas de acceso basadas en activos on-chain: poseer ciertos POAPs puede ser el requisito para entrar a un canal de Discord, acceder a un repositorio privado o reclamar un rol. Algunos protocolos ponderan el voto de gobernanza según el historial de participación certificado por POAPs. Tu colección se convierte en un diario verificable: no solo "estuviste en ETHDenver" sino "asististe al taller de ZK-proofs y presentaste en el hackathon".

**Limitaciones**:

Un POAP prueba presencia física o virtual, no comprensión ni contribución real: asistir pasivamente a cien conferencias genera más tokens que contribuir a fondo en un solo proyecto. El gaming más difícil de frenar es pagar a alguien para que escanee el QR en tu lugar. Y aunque los tokens son on-chain, el artwork y la metadata dependen de la infraestructura centralizada de POAP.xyz. La dirección en la que evoluciona el formato —POAPs que desbloquean capas adicionales al completar un quiz, o que progresan visualmente al alcanzar hitos de participación— intenta precisamente responder a esa crítica: pasar de "proof of attendance" a algo más cercano a "proof of action".

## Redes de confianza

Las primitivas del apartado anterior —SBTs, attestations EAS, POAPs— construyen reputación desde el emisor: alguien con autoridad reconocida certifica algo sobre ti. Pero hay una dimensión distinta donde la confianza no proviene de un emisor designado, sino que emerge del propio comportamiento de la red: quién reconoce tu trabajo, quién te sigue, quién te avala, quién te incluye en sus registros.

Hay un concepto con el que esto converge: el web of trust. Su idea central —que la confianza puede derivarse de la acumulación de relaciones verificables entre pares, sin depender de una autoridad central— aparece formalizada matemáticamente en el paper [EigenTrust: Reputation Management in P2P Networks](https://nlp.stanford.edu/pubs/eigentrust.pdf), que modela cómo la confianza se propaga en redes P2P usando teoría de grafos. Más que una génesis de los mecanismos que veremos a continuación, es un marco descriptivo que comparten: todos ellos son formas de construir confianza desde el reconocimiento mutuo, no desde registros de un emisor autorizado.

Los mecanismos que materializan esta dimensión en Web3 son los Hypercerts —donde publicas tu trabajo y la validación llega si fondos de la comunidad deciden reconocerlo—, el grafo social, las listas curadas y el vouching con coste económico.

### Hypercerts

En las primitivas del apartado anterior la confianza viene del emisor: Gitcoin, Coinbase, el organizador del evento certifica algo sobre ti. [Hypercerts](https://hypercerts.org) rompe ese modelo: es un smart contract permisionless en Optimism que tú llamas directamente para auto-declarar tu propio trabajo —qué hiciste, en qué periodo, quién contribuyó y con qué porcentaje, con qué evidencia—. No hay emisor con autoridad que te valide previamente; tú eres el emisor.

El token que minteas puede dividirse en fracciones transferibles. La idea es que tras publicar el trabajo, un fondo como [Optimism RetroPGF](https://app.optimism.io/retropgf) puede decidir —voluntariamente, sin ninguna obligación— reconocerlo económicamente transfiriéndote ETH a cambio de una fracción. Esa transacción queda on-chain como señal de reputación verificable: "Optimism reconoció este trabajo" es un hecho público. Es más una subvención retroactiva que una compra comercial: el fondo no obtiene nada fungible a cambio, simplemente reconoce impacto pasado. El protocolo fue desarrollado por [Protocol Labs](https://protocol.ai) y adoptado por Gitcoin complementando sus rondas prospectivas: Gitcoin Grants financia trabajo futuro, los Hypercerts documentan el trabajo ya entregado para que pueda ser reconocido después.

**Limitaciones**:

El protocolo registra lo que tú declaras sin verificación previa, así que el certificado vale lo que otros decidan reconocer. El reconocimiento no es para cerrar un proyecto acabado sino para señalizar que un trabajo continuo merece seguir: quien paga dice "esto es valioso, continúa". El problema es que nadie está obligado a hacerlo aunque el trabajo sea bueno y público. La credibilidad del modelo descansa en que los fondos tengan reputación que perder si no reconocen trabajo valioso, lo que es un incentivo social frágil. A esto se suma que quien llega al ecosistema sin historial previo de Hypercerts reconocidos es más difícil que los fondos lo encuentren.

### Grafo Social

Los protocolos de grafo social descentralizado convierten las relaciones entre usuarios en activos on-chain verificables. Los principales son [Lens Protocol](https://lens.xyz) y [Farcaster](https://www.farcaster.xyz). Lens es un grafo donde los follows, comentarios y mirrors son NFTs on-chain: seguir a alguien emite un token que representa esa relación, composable y reutilizable por cualquier aplicación construida sobre el protocolo. Farcaster opera con una arquitectura diferente —identidades on-chain en Optimism, pero contenido almacenado en hubs descentralizados fuera de la cadena— con el objetivo declarado de ser lo suficientemente descentralizado para que ninguna entidad pueda censurar o capturar el protocolo.

[RSS3](https://rss3.io/) complementa estos protocolos como capa de indexación cross-chain. A diferencia de Lens y Farcaster que gestionan el grafo social en sí, RSS3 es un protocolo de distribución de información descentralizada que agrega feeds de actividad on-chain de múltiples blockchains —transacciones DeFi, actividad NFT, interacciones sociales en Lens y Farcaster, gobernanza de DAOs— en un formato estándar consumible por cualquier aplicación. Funciona como el "RSS del Web3", permitiendo que el historial completo de actividad de un usuario sea portable y consultable desde cualquier plataforma sin depender de indexadores centralizados. Esta indexación agregada es especialmente valiosa para sistemas de reputación que necesitan evaluar comportamiento cross-chain sin mantener infraestructura de indexación propia.

El vínculo con la reputación es doble. La estructura del grafo en sí es ya una señal: quien acumula seguidores genuinos entre personas con alto capital social on-chain tiene una reputación relacional que no puede fabricarse fácilmente, porque requiere que otras personas reales con historial verificable decidan seguirte. Y el grafo puede analizarse algorítmicamente para derivar scores: [Karma3Labs](https://karma3labs.com) aplica EigenTrust al grafo de Farcaster para calcular scores de confianza que los protocolos pueden consumir como señal anti-Sybil.

La limitación fundamental es que la reputación social hereda los sesgos del grafo. Si el grafo está dominado por early adopters anglosajones —que es la situación actual tanto en Lens como en Farcaster— el score refleja proximidad a ese núcleo, no mérito universal. Un desarrollador excelente pero recién llegado puede tener score bajo simplemente porque aún no está conectado a los nodos con mayor peso, reproduciendo en la práctica las jerarquías que el sistema aspira a reemplazar.

### Listas Curadas

Las listas curadas representan un mecanismo distinto de construcción de reputación: la inclusión verificada por la comunidad en registros específicos. A diferencia de acumular credenciales individuales o construir un grafo social, aquí la reputación emerge de pasar un proceso de validación colectiva para formar parte de una lista reconocida. El valor reputacional no reside en cuántas acciones has realizado, sino en que un grupo de validadores ha certificado públicamente que cumples ciertos criterios objetivos.

**Kleros Curate**:

[Kleros Curate](https://curate.kleros.io/) implementa este modelo mediante listas descentralizadas donde cualquiera puede proponer la inclusión o remoción de elementos, y las disputas se resuelven mediante el sistema de arbitraje descentralizado de Kleros descrito en detalle en [resolución de conflictos](7-4-conflict-resolution.md). El funcionamiento es directo: alguien propone añadir una entrada a una lista existente —por ejemplo, "direcciones de auditores verificados" o "tokens sin scam verificados"— depositando una pequeña cantidad económica como garantía. Durante un período de desafío, cualquier observador puede disputar esa inclusión si considera que no cumple los criterios establecidos en la política de la lista. Si hay disputa, jurados de Kleros evalúan la evidencia y deciden. Quien tenía razón recupera su depósito más una compensación; quien se equivocó lo pierde.

**Otros sistemas de listas curadas**:

Kleros Curate es el sistema más robusto de arbitraje descentralizado para listas, pero existen otros enfoques al mismo problema. [Uniswap Token Lists](https://tokenlists.org/) estableció un estándar técnico (el JSON schema de token lists) adoptado por la mayoría de DEXs: cualquiera puede publicar una lista de tokens, pero solo las listas mantenidas por entidades reconocidas —Uniswap Foundation, CoinGecko, Gemini— son consumidas masivamente por las interfaces. El mecanismo de confianza aquí no es arbitraje on-chain sino reputación del curador off-chain, más simple pero también más centralizado.

[The Graph](https://thegraph.com) implementa curación mediante staking económico: los curadores hacen stake de tokens GRT sobre subgraphs específicos para señalizar calidad. Los indexadores priorizan subgraphs con más curación, y los curadores ganan fees si eligieron subgraphs que generan mucho query volume. Es curación por incentivos de mercado, no por validación de criterios objetivos.

[Everest](https://everest.link), un proyecto ahora descontinuado, intentó crear un registro universal de proyectos crypto verificados mediante un modelo de curación híbrido: stake económico más votación de miembros existentes. Su fracaso ilustra el desafío de arranque en frío: sin suficientes proyectos verificados inicialmente, la lista no tiene valor, pero sin valor percibido, los proyectos no tienen incentivo para pagar por verificarse.

La diferencia fundamental entre estos sistemas y Kleros está en cómo se resuelven los desacuerdos. Uniswap Token Lists depende de la autoridad del curador. The Graph usa señales de mercado. Kleros aplica arbitraje humano descentralizado. Cada modelo tiene su lugar: para listas donde los criterios son subjetivos o cambiantes, la autoridad del curador funciona mejor. Para listas donde la utilidad es medible objetivamente, las señales de mercado pueden ser suficientes. Para listas con criterios objetivos verificables pero que requieren evaluación humana, el arbitraje descentralizado es la opción más robusta.

El mecanismo de incentivos económicos desincentiva spam y propuestas fraudulentas, porque proponer algo falso tiene coste real si alguien lo desafía. Al mismo tiempo, recompensa a quienes vigilan la calidad de las listas detectando entradas incorrectas. El resultado es un sistema de curaduría colaborativa donde el interés económico alinea a los participantes hacia mantener listas precisas.

Como primitiva de reputación, las listas curadas funcionan de forma binaria pero con alta señal de confianza. Estar incluido en la lista verificada de "proveedores de oráculos auditados" o en el registro de "desarrolladores de contratos certificados" no dice cuánta experiencia tienes ni cuánto has contribuido, pero certifica públicamente que pasaste un filtro que otros no superaron. Esta inclusión es consultable on-chain por cualquier protocolo: un marketplace de servicios puede filtrar solo a quienes aparecen en listas curadas reconocidas, o un protocolo DeFi puede otorgar condiciones preferenciales a direcciones verificadas mediante este proceso.

El modelo escala más allá de identidades individuales. Existen listas curadas de tokens seguros, de direcciones de contratos auditados, de protocolos de lenguaje de señas para accesibilidad, de palabras censuradas para filtros de contenido. La lógica es la misma: un registro público donde la inclusión tiene valor porque implica validación colectiva verificable.

**Limitaciones y riesgos**:

El valor de una lista curada depende directamente de dos factores: la claridad de sus criterios de inclusión y la reputación de quienes la mantienen. Una lista con criterios ambiguos genera disputas constantes sin resolución clara, degradando la confianza en todo el sistema. Y una lista mantenida por una comunidad pequeña o desconocida no aporta señal reputacional relevante, porque nadie más reconoce su autoridad.

Existe también el riesgo de captura: si los costes de desafío son demasiado altos o la comunidad de curadores se coordina entre sí, la lista puede convertirse en un mecanismo de exclusión arbitraria en lugar de validación objetiva. El caso extremo es una lista dominada por un grupo de interés que rechaza sistemáticamente a competidores legítimos mediante desafíos espurios.

La descentralización del arbitraje a través de Kleros mitiga parte de este riesgo, pero introduce otro vector de fragilidad: la calidad de las decisiones depende de que los jurados seleccionados comprendan los criterios técnicos de la lista. Para listas especializadas —como "contratos que implementan correctamente ERC-4626"— un jurado generalista puede carecer del expertise necesario para evaluar evidencia técnica, llevando a decisiones incorrectas que erosionan la utilidad de la lista.

Finalmente, las listas curadas funcionan bien para atributos relativamente estáticos y verificables objetivamente, pero mal para reputación dinámica o cualitativa. Puedes listar "auditores con certificación X completada", pero no "auditores en los que confiarías para código crítico", porque eso requiere juicio subjetivo que el sistema de arbitraje no puede resolver de forma determinista.

### Vouching (abalar / recomendar) con coste económico: Ethos Network

Los mecanismos anteriores —el grafo social y las listas curadas— construyen reputación a través de relaciones o validaciones colectivas, pero sin que quien avala asuma un riesgo personal. [Ethos Network](https://ethos.network) introduce una dimensión diferente: la confianza que otros depositan en ti a costa de su propia reputación y su capital.

El protocolo se articula sobre tres primitivas que se agregan en un único *credibility score*. La primera es el vouching: avalar a alguien requiere depositar ETH propio como garantía. Si la persona avalada se comporta de forma deshonesta o maliciosa —verificado mediante el mecanismo de disputa del protocolo— el depósito puede ser confiscado parcialmente. Esto invierte la lógica habitual de los sistemas de referidos, donde recomendar a alguien no tiene coste: en Ethos, avalar tiene precio si te equivocas, lo que convierte cada aval en una señal costosa y por tanto creíble. La segunda primitiva es el staking: además del vouching, cualquier usuario puede hacer stake de ETH sobre el perfil propio o ajeno como señal de confianza financiera, con la misma mecánica de confiscación ante comportamiento malicioso verificado. La tercera es el sistema de reviews: texto público firmado criptográficamente donde cualquiera puede describir su experiencia con otro participante. Las reviews se publican on-chain de forma permanente e inatacable —quien las recibe no puede borrarlas—, y están ponderadas por la reputación del autor: una review de alguien con alto credibility score pesa más que la de una cuenta nueva.

El credibility score agrega las tres señales —avales recibidos, ETH en stake sobre el perfil, y reviews— en una puntuación consultable por cualquier protocolo o aplicación. La idea de fondo es que la confianza transitiva, formalizada matemáticamente en el paper [EigenTrust](https://nlp.stanford.edu/pubs/eigentrust.pdf), tiene más señal cuando quien avala arriesga algo propio: la diferencia entre un like en redes sociales y una firma notarial es exactamente esa fricción económica.

El resultado práctico es un marketplace de confianza: protocolos que necesitan seleccionar contribuidores, DAOs que quieren delegar responsabilidades, o usuarios que buscan colaboradores pueden ordenar perfiles por credibility score con la garantía de que ese score fue construido por personas que pusieron capital real en el proceso de evaluación.

**Limitaciones**:

El sistema requiere que quien avala tenga ya reputación consolidada para que sus avales importen: los primeros avales de una cuenta nueva aportan poco al credibility score del receptor, lo que reproduce el problema del arranque en frío presente en todos los mecanismos de reputación on-chain. Además, la mecánica de confiscación depende de que los disputantes lleguen al mecanismo de resolución, lo que introduce un sesgo hacia conflictos lo suficientemente graves como para que valga la pena disputar, dejando sin penalización comportamientos problemáticos pero menores.

## Guía Práctica para Construir Reputación

Esta sección proporciona pasos concretos para usuarios que quieren comenzar a construir su reputación Web3, organizados por nivel de experiencia.

### Configuración Inicial

El primer paso para cualquier usuario es establecer las fundaciones básicas de identidad y seguridad antes de comenzar a acumular reputación verificable.

**Establecer tu identidad on-chain**:

El primer paso es elegir una dirección que planeas mantener durante años y consolidar en ella toda tu actividad pública. Un error frecuente es crear múltiples wallets y fragmentar el historial: si repartes tus contribuciones, tus POAPs y tus votos entre varias direcciones, ninguna cuenta la historia completa. Puedes usar otras direcciones para privacidad financiera, pero tu reputación debería vivir en una sola identidad principal.

Una vez tienes esa dirección, registra un nombre [ENS (Ethereum Name Service)](https://ens.domains). En lugar de compartir 0x1234...5678, compartes tusername.eth, que es mucho más memorable y funciona como punto de entrada reconocible en cualquier aplicación Web3. El coste es aproximadamente $5-20 al año según la longitud del nombre. Algunos empleadores en Web3 piden directamente el ENS en lugar de un CV tradicional. Para visualizar y compartir tu historial DeFi de forma agregada, [DeBank](https://debank.com) es el dashboard estándar: conectas tu wallet y ves todos tus holdings y transacciones históricas a través de más de treinta cadenas. Puedes crear un perfil público con handle propio que muestra tu actividad verificable y que algunos usuarios incluyen en aplicaciones a DAOs o en su presentación a protocolos.

**Conectar Gitcoin Passport**:

Visita [passport.gitcoin.co](https://passport.gitcoin.co) y conecta tu wallet. Comienza vinculando las fuentes más fáciles: cuenta de Google, cuenta de Twitter (si tiene más de 6 meses de antigüedad), y cualquier cuenta de redes sociales que tengas.

El objetivo inicial es alcanzar score de 15-20 puntos, que es el mínimo para ser considerado "probablemente humano" por la mayoría de aplicaciones. Esto típicamente requiere 5-8 stamps diferentes. No te preocupes por maximizar tu score inmediatamente, crecerá orgánicamente mientras participas en el ecosistema.

Si tu score inicial es bajo porque eres nuevo en crypto, enfócate en los stamps que puedes obtener sin inversión: verificación de cuentas sociales existentes, participación en [BrightID](https://www.brightid.org/) (requiere una videollamada de 5 minutos), y completar tu perfil ENS.

**Crear perfil social en Lens**:

Visita [claim.lens.xyz](https://claim.lens.xyz) para verificar si calificas para un handle Lens gratuito. Si no, puedes comprar uno en marketplaces secundarios por aproximadamente $10-30. Tu perfil Lens se convierte en tu identidad social portable en Web3.

Configura tu perfil con información real: foto de perfil, bio describiendo tus intereses, y enlaces a tus otras presencias online. Comienza siguiendo proyectos y personas relevantes a tus intereses. No necesitas postear constantemente, pero tener un perfil establecido muestra que estás realmente participando en el ecosistema, no solo farming.

### Construcción Activa de Reputación

Una vez establecidas las bases, comienza a participar activamente en el ecosistema para acumular credenciales verificables.

**Completar quests educativas**:

[RabbitHole](https://rabbithole.gg) y [Layer3](https://layer3.xyz) ofrecen quests para principiantes que no requieren capital significativo. Este modelo de acumular reputación mediante participación verificable on-chain se conoce como [reputation mining](https://www.coindesk.com/sponsored-content/reputation-mining-builds-new-trust-via-web-3): al igual que los mineros obtienen recompensas por contribuir a la red, los usuarios ganan historial demostrable por interactuar con protocolos reales. Comienza con quests de "onboarding" que te enseñan conceptos básicos como usar swaps en Uniswap, conectar a diferentes L2s, o interactuar con protocolos de staking. [Galxe](https://galxe.com) opera a mayor escala: más de tres mil proyectos han lanzado campañas ahí, y cada una genera un NFT de credencial on-chain consultable. Galxe además calcula un Galxe Score agregado de tu participación total que cientos de proyectos usan como filtro anti-Sybil en sus airdrops, por lo que acumular credenciales en Galxe tiene valor directo más allá de las recompensas inmediatas.

Otro sistema de scoring complementario es [DegenScore](https://degenscore.com), que analiza específicamente tu actividad DeFi on-chain para generar un score de reputación. A diferencia de Gitcoin Passport que verifica identidad humana, o Galxe que mide participación en campañas, DegenScore se enfoca en señales de comportamiento DeFi real: antigüedad de la wallet, volumen de transacciones, diversidad de protocolos usados, tenencia histórica de NFTs, y participación en lanzamientos tempranos de proyectos. El score resultante ha sido usado por algunos protocolos para acceso preferencial a mints de NFTs, whitelists de airdrops, y programas de early adopters. Su utilidad principal es demostrar que tienes experiencia práctica navegando DeFi, no solo conocimiento teórico. No requiere verificación manual y se calcula automáticamente analizando el historial público de tu dirección.

Estrategia recomendada: no farmees quests aleatoriamente solo por recompensas. Enfócate en protocolos que genuinamente te interesan y donde podrías ver valor en participar a largo plazo. Las credenciales que ganas deberían contar una historia coherente sobre tus intereses y expertise, no parecer farming aleatorio.

Por ejemplo, si te interesa DeFi, completa todas las quests relacionadas con AMMs, lending, y yield farming. Si te interesa gobernanza, enfócate en quests de DAO participation y voting. Esta especialización hace que tus credenciales sean más valiosas que un perfil genérico que hizo todo superficialmente.

**Participar en protocolos DeFi**:

Aún con capital modesto (incluso $50-100), puedes comenzar a construir historial DeFi verificable. Usa L2s como [Arbitrum](https://arbitrum.io) o [Optimism](https://www.optimism.io) donde los fees son mínimos.

Opciones de bajo riesgo para principiantes incluyen proveer liquidez en stablecoin pairs en Uniswap (riesgo de impermanent loss es mínimo con stablecoins), depositar en protocolos de lending como Aave para ganar interés, o usar protocolos de liquid staking como [Lido](https://lido.fi) para stakear ETH mientras mantienes liquidez.

Lo importante no es el monto sino la consistencia y diversidad. Es mejor usar 5 protocolos diferentes con $20 cada uno durante 6 meses que hacer una transacción única de $100 y nunca volver. El historial de participación sostenida es lo que construye reputación.

**Coleccionar POAPs**:

Asiste a eventos virtuales de Web3 y colecciona POAPs. [POAP.fun](https://poap.fun) lista eventos con distribución de POAPs. Las conferencias como [ETHDenver](https://ethdenver.com/), [ETHGlobal](https://ethglobal.com/) o [Devcon](https://devcon.org/en/) distribuyen POAPs diferenciados por sesión; muchas comunidades de protocolo —Uniswap, Aave, ENS— hacen calls de gobernanza periódicos que también los emiten.

Los POAPs más valiosos provienen de eventos con alta barrera de entrada, no de distribuciones masivas. Un POAP de presentar en ETHDenver vale más reputacionalmente que un POAP de unirte a un server de Discord. Prioriza calidad sobre cantidad.

Algunos POAPs históricos se vuelven coleccionables valiosos (POAPs de los primeros eventos de Ethereum, por ejemplo), pero no deberías coleccionar por valor financiero sino por construcción de reputación genuina.

**Contribuir a DAOs**:

El proceso para empezar a colaborar en una DAO no requiere enviar un currículum o pasar entrevistas tradicionales. En Web3, tu reputación se construye demostrando directamente lo que sabes hacer. Para lograrlo, no debes buscar un empleo fijo de entrada, sino utilizar plataformas como [DeWork](https://dework.xyz) o [Station](https://station.groupos.xyz). Estas webs funcionan como tablones de anuncios donde las DAOs publican trabajos específicos y puntuales que cualquier persona puede intentar resolver (a estos micro-trabajos se les llama *bounties*).

La estrategia recomendada es comenzar eligiendo tareas pequeñas y bien acotadas, como traducir un texto, diseñar un gráfico o resumir las notas de un foro. Cuando entregas este trabajo y la comunidad lo aprueba, ocurre la base de la reputación on-chain: además de recibir un pago económico, la DAO envía directamente a tu wallet una credencial digital, comúnmente llamada *badge* o insignia. Piensa en este *badge* como un "mini-diploma" digital y público que certifica ante todo el mundo que tú resolviste esa tarea con éxito para ellos.

El paso definitivo para conseguir reputación real es la constancia. Tu plan de acción debe ser acumular entre 5 y 10 de estas credenciales demostrables dentro de una misma DAO, en lugar de hacer tareas sueltas en proyectos distintos. Al reunir estas insignias en tu wallet bajo un mismo proyecto, estás creando un portafolio o historial de trabajo que es matemáticamente verificable y que nadie te puede borrar ni quitar.

Cualquier miembro de la organización podrá mirar tu perfil y comprobar que has estado aportando valor de forma continua. Así es como verdaderamente dejas de ser un recién llegado y te ganas la confianza plena de la DAO, lo que de forma orgánica te permitirá acceder a posiciones con mayor responsabilidad, ingresos regulares o poder de decisión.

**Participar en gobernanza**:

Votar en las decisiones de los proyectos (protocolos) que usas es una de las formas más fuertes de demostrar que no eres un simple especulador, sino un usuario comprometido. Cada comunidad plantea propuestas para mejorar o cambiar su protocolo: desde decidir qué nuevas funcionalidades desarrollar, hasta cómo gestionar los fondos de la tesorería.

Existe un mito de que para tener voz en estas votaciones necesitas comprar y poseer grandes cantidades de tokens de gobernanza, algo que suele ser económicamente inviable para la mayoría. La realidad es que muchos protocolos en Web3 permiten un sistema de "delegación". Esto significa que usuarios o inversores que sí tienen muchos tokens pero no tienen tiempo de analizar las propuestas, pueden prestarte (delegarte) temporalmente su poder de voto si demuestras ser alguien activo y con criterio. De este modo, puedes construir un peso significativo en las votaciones simplemente aportando conocimiento y atención, sin necesidad de gastar tu propio dinero.

[Snapshot](https://snapshot.org) es donde la mayoría de votaciones de DAOs ocurren off-chain. Crea una cuenta, conecta tu wallet, y comienza votando en propuestas de proyectos que conoces bien. Lee las propuestas completas antes de votar y ocasionalmente comenta explicando tu razonamiento.

Participación consistente en gobernanza (votando en 10+ propuestas durante varios meses) es una señal fuerte de que no eres un holder especulativo sino un participante comprometido del ecosistema.

**Construir respaldo entre pares**:

[Ethos Network](https://ethos.network) implementa un mecanismo distinto a todos los anteriores: puedes avalar públicamente a otras personas, pero si quien avalas se comporta mal, tu propia reputación también baja. Avalar no es gratis en términos reputacionales. El resultado es un marketplace de confianza donde buscar colaboradores —desarrolladores, diseñadores, auditores— rankeados por los avales de personas con alta reputación, y donde recibir avales de usuarios reconocidos añade una señal de confianza que no puede fabricarse sin que haya personas reales con historial dispuestas a arriesgar su propio score. Ethos también permite hacer staking de ETH sobre un perfil propio o ajeno como señal financiera de confianza, con posibilidad de confiscación si se verifica comportamiento malicioso. No es una herramienta para empezar desde cero —necesitas primero un historial on-chain para que tus avales importen— pero a partir de los meses 4-6 del roadmap tiene sentido empezar a usarla activamente.

### Roadmap de Progresión

Esta sección proporciona hitos concretos organizados por timeline realista.

**Primeras 4 semanas — Fundaciones**:

Al final del primer mes, deberías tener tu infraestructura básica completa. Esto incluye wallet segura con seed phrase respaldado, nombre ENS registrado y configurado, Gitcoin Passport con score mínimo de 15 puntos, perfil Lens creado y básicamente configurado, y tus primeros 3-5 POAPs de eventos virtuales.

También deberías haber completado al menos 3 quests en RabbitHole o Layer3, interactuado con al menos 2 protocolos DeFi diferentes (aunque sea con montos pequeños), y seguido 20-30 proyectos/personas relevantes en Lens Protocol.

El objetivo no es impresionar a nadie todavía sino establecer presencia verificable que no parezca cuenta nueva creada ayer. Muchos filtros anti-Sybil simplemente verifican antigüedad básica de la cuenta.

**Meses 2-3 — Participación activa**:

Durante este período, profundiza tu participación para demostrar constancia. Tu meta ahora es elevar tu puntuación de [Gitcoin Passport](https://passport.gitcoin.co/) a más de 25 puntos obteniendo validaciones (*stamps*) que requieran mayor compromiso. Por ejemplo:

- **Holdings históricos**: Conservar ciertos tokens en tu billetera durante varios meses para probar que tu cuenta no se creó ayer.
- **Bienes públicos**: Donar pequeñas cantidades a proyectos comunitarios (como Gitcoin Grants).
- **Verificación de humanidad**: Si aún no completaste el stamp de [BrightID](https://www.brightid.org/) en la fase anterior (la videollamada de 5 minutos), este es el momento de hacerlo. Existen otras opciones igualmente válidas como stamp en Gitcoin Passport: [Proof of Humanity](https://www.proofofhumanity.id) requiere grabar un vídeo público y depositar una pequeña cantidad de ETH como garantía; [Idena](https://idena.io) te pide conectarte a una sesión de verificación sincronizada a una hora fija junto a otros usuarios. Las tres funciones tienen el mismo propósito —certificar que eres una persona única y real— pero BrightID es la más rápida y sin coste económico, por eso es la opción recomendada para empezar.

Completa al menos 10 quests adicionales enfocadas en áreas específicas de interés. Colecciona 15-20 POAPs total, priorizando eventos de comunidades donde realmente quieres involucrarte a largo plazo.

Haz tu primera contribución sustancial a una DAO (completar un bounty, escribir documentación, ayudar con traducción). Participa en al menos 5 votaciones de gobernanza en protocolos que usas regularmente.

Tu wallet debería mostrar interacciones regulares con 5-7 protocolos diferentes distribuidas a lo largo de estos meses, no transacciones en ráfagas cortas que parecen farming.

**Meses 4-6 — Especialización y profundidad**:

En esta fase, tu reputación comienza a tener valor real. Deberías tener Gitcoin Passport score de 30+, lo que te califica para prácticamente cualquier airdrop o programa selectivo.

Enfócate en convertirte en contribuidor reconocido en 1-2 DAOs específicas. Completa +5 bounties en las mismas organizaciones, participa activamente en sus discusiones de gobernanza, y gana credenciales digitales verificables (como *attestations* usando un estándar actual como EAS, o roles criptográficos en Hats Protocol) que certifiquen públicamente tu valor para la comunidad.

Tu portfolio DeFi debería ser diversificado: experiencia con AMMs, lending, staking, y quizás yield farming o protocols más avanzados. No necesitas grandes cantidades de capital, pero sí historial sostenido de al menos 90-120 días.

Comienza a ser activo en Lens publicando insights sobre protocolos que usas, compartiendo experiencias, o contribuyendo a discusiones técnicas. Tu perfil social complementa tu actividad on-chain.

**Más allá de 6 meses — Reputación establecida**:

Con 6+ meses de participación consistente, tu reputación tiene peso real. Deberías tener Humanity Score de 35+, portfolio diversificado de 10+ protocolos usados regularmente, colección de 30+ POAPs curados (no spam), SBTs y badges de múltiples contribuciones verificables, y perfil Lens con actividad regular y seguidores genuinos.

En este punto, calificas para oportunidades reales: préstamos subcolateralizados en protocolos experimentales, selección para airdrops de alta calidad, consideración para roles pagados en DAOs, y reconocimiento en comunidades específicas como contributor serio.

Algunos usuarios en este nivel comienzan a recibir ofertas laborales directas basándose en su reputación on-chain visible, o son invitados a participar en programas selectivos de aceleradores y grants.

### Ejemplos de Perfiles Reales

Para ilustrar cómo se ve reputación construida exitosamente, analicemos perfiles anonymizados de usuarios reales.

**El trader DeFi experimentado**:

Este perfil muestra 600+ transacciones on-chain distribuidas a lo largo de 18 meses. Interacciones con 20+ protocolos DeFi diferentes incluyendo Uniswap, Aave, Compound, Curve, Convex, y protocols más nicho. Proveyó liquidez continuamente durante 12+ meses en varios pools, acumulando más de $100,000 en volumen total (no necesariamente de capital propio, sino volumen generado).

Gitcoin Passport score de 38 puntos con stamps de prácticamente todas las categorías. Colección de 45 POAPs enfocados en eventos DeFi y conferencias Ethereum. Participó en votaciones de gobernanza de 8 protocolos diferentes, con historial visible en Snapshot.

Resultado medible: accedió a beta cerrado de [Spectral Finance](https://www.spectral.finance) para préstamos subcolateralizados, calificó para airdrop de [dYdX](https://dydx.exchange) recibiendo $2,000+, y fue reclutado como liquidity manager para una nueva DAO de DeFi.

**La contribuidora de DAO prolífica**:

Perfil con menos actividad DeFi (50 transacciones totales) pero profunda participación en gobernanza y construcción comunitaria. Contribuidora activa en 4 DAOs diferentes, con credenciales de contribución verificables (vía EAS) que lo demuestran en todas ellas: Gitcoin, MakerDAO, ENS, y Optimism.

Completó 30+ bounties documentados on-chain totalizando $15,000 en compensación. Participó en 50+ votaciones de gobernanza con delegaciones recibidas de otros miembros de la comunidad. Escribió 10+ propuestas de gobernanza que fueron implementadas.

Gitcoin Passport score de 32 puntos. Perfil Lens muy activo con 1,200 seguidores genuinos (no bots), mayormente otros contribuidores de DAO. Colección de 60+ POAPs concentrados en eventos de gobernanza, DAO summits, y conferencias de Web3.

Resultado medible: ofreció posición full-time como Governance Lead en protocol importante con salario de $120k + equity, reconocida públicamente por Vitalik Buterin en Twitter por sus contribuciones a gobernanza descentralizada.

**El desarrollador open source**:

Wallet con relativamente pocas transacciones (150 total) pero cada una significativa. Deployó 12 smart contracts en mainnet, varios auditados por firmas reconocidas. Contribuidor verificado en GitHub con 2,000+ commits a repositorios Web3 (verificable mediante [GitPOAP](https://www.gitpoap.io)).

Ganador de 3 hackathons de ETH Global con badges verificables. SBTs de completar programas de seguridad de [OpenZeppelin](https://www.openzeppelin.com/defender) y [Secureum](https://secureum.xyz). Participación activa en foros técnicos de Ethereum Research y contribuciones documentadas a EIPs.

Gitcoin Passport score relativamente modesto de 25 puntos (no prioriza stamps sociales). Colección selecta de solo 20 POAPs, todos de eventos técnicos de alta relevancia como Devcon, ETHDenver, y ZK Summit.

Resultado medible: múltiples ofertas de trabajo de protocolos tier-1 sin aplicar formalmente, grants de $50k+ de Ethereum Foundation para investigación, invitado a advisory boards de nuevos protocolos.

## Implementación para dev

Esta sección está dirigida a desarrolladores, product managers y founders que quieren implementar sistemas de reputación en sus propios protocolos o aplicaciones.

### Definir objetivos y casos de uso

Antes de tocar código, necesitas saber exactamente qué problema resuelve la reputación en tu protocolo. Sin esa claridad, acabarás midiendo cosas que no importan o creando incentivos contradictorios.

Los cuatro casos de uso con más tracción real son los siguientes. En DeFi, la reputación permite reducir el colateral exigido en préstamos: protocolos como [Spectral Finance](https://www.spectral.finance) analizan el historial on-chain —préstamos repagados, antigüedad de wallet, diversidad de protocolos usados— para ofrecer ratios de colateralización más bajos a quienes demuestran comportamiento responsable. En gobernanza de DAOs, sirve para escapar de la plutocracia pura: [Optimism](https://www.optimism.io) usa citizenship badges no transferibles para dar peso de voto a contribuidores verificados, independientemente de cuántos tokens posean. En distribución de airdrops y quadratic funding, [Gitcoin](https://grants.gitcoin.co) exige un Humanity Score mínimo para que las contribuciones cuenten, haciendo económicamente inviable crear miles de cuentas falsas. Y en identidad profesional, la dirección [ENS](https://ens.domains) actúa como currículum verificable: contratos deployados, hackathons ganados, auditorías superadas, todo comprobable en segundos.

Una vez identificado tu caso de uso, define qué comportamientos quieres incentivar y cuáles quieres desincentivar. Esta decisión es más importante que cualquier elección técnica posterior. Si quieres participación genuina en gobernanza, no basta con contar votos: deberías requerir consistencia temporal (haber votado en al menos tres de las últimas cinco propuestas, no solo en las controvertidas). Si quieres proveedores de liquidez a largo plazo, importa la duración continuada, no el volumen puntual. El criterio que elijas define qué tipo de comportamiento se vuelve racional optimizar, y los usuarios siempre optimizarán lo que midas.

### Herramientas y arquitectura

Antes de elegir herramientas concretas, conviene tener el mapa completo del sistema. Un stack de reputación bien diseñado tiene cuatro capas que se construyen una sobre otra. La base son los datos brutos: transacciones on-chain, votos, contribuciones a GitHub, participación en Discord. Sobre ellos opera la capa de atestación, donde protocolos como EAS convierten esos datos en declaraciones verificables y firmadas. La tercera capa es la agregación: algoritmos que combinan múltiples attestations en scores o roles consultables. Y en la cima está la aplicación que consume esos scores para tomar decisiones reales, ya sea conceder un préstamo, ponderar un voto o asignar un rol en una DAO. La ventaja de pensar en capas es que cada una puede cambiar sin romper las demás: puedes sustituir el algoritmo de scoring sin tocar los contratos de attestation, y puedes actualizar las fuentes de datos sin modificar la lógica de aplicación.

Las herramientas descritas en la sección anterior —EAS, POAPs, grafos sociales— son también tu stack de implementación. Aquí la pregunta práctica es cómo combinarlas y qué añadir para cerrar el sistema.

La primera decisión es dónde viven los datos. Los datos on-chain ofrecen máxima verificabilidad pero están limitados a lo que ocurre en la blockchain. Para incorporar actividad externa —GitHub, Discord, formularios de contribución— necesitas attestations emitidas por un tercero confiable que actúe de puente, o bien [Chainlink Functions](https://chain.link/functions) para traer datos off-chain de forma descentralizada, asumiendo que siempre introduces un punto de confianza adicional. La arquitectura que mejor funciona en producción combina ambas: datos on-chain como base objetiva y attestations EAS para todo lo que requiere juicio humano externo.

Para almacenar datos de perfil mutables —una bio, preferencias, configuración de privacidad— sin cambiar el identificador del usuario, [Ceramic Network](https://ceramic.network) proporciona almacenamiento descentralizado vinculado a DIDs. Y para que las consultas de reputación histórica sean instantáneas sin escanear toda la cadena, lo estándar es desplegar un subgraph en [The Graph](https://thegraph.com) que indexe los eventos relevantes de tu contrato o los de EAS. Para casos centrados en actividad social y reputación relacional cross-chain, [RSS3](https://rss3.io/) ofrece una alternativa especializada: indexa automáticamente interacciones sociales on-chain en protocolos como Lens y Farcaster, actividad DeFi, eventos de gobernanza y transacciones NFT a través de múltiples blockchains en un formato estándar, permitiendo que aplicaciones consulten el historial completo de un usuario sin mantener infraestructura de indexación propia. En cualquier caso, el principio de diseño es el mismo: nunca encierres la reputación de un usuario en una base de datos propia de tu aplicación. Si tu protocolo desaparece, las credenciales deben sobrevivir; EAS y Ceramic existen precisamente para eso.

La tercera capa —la de agregación— admite tres enfoques distintos, y la elección entre ellos tiene consecuencias prácticas importantes. El primero es el modelo de múltiples fuentes: combinar señales heterogéneas en un score único ponderado. Gitcoin Passport es el ejemplo canónico, con más de veinte stamps que representan tipos de verificación muy diferentes —antigüedad de cuenta de GitHub, participación en BrightID, holdings de ETH— y un peso distinto para cada uno en función de lo difícil que es falsificarlo. El resultado es un número único que cualquier aplicación puede usar directamente, a cambio de que el algoritmo de ponderación sea necesariamente arbitrario. El segundo enfoque es el modelo contextual: reconocer que la reputación no es universal sino específica a un dominio. Lo que hace un buen contribuidor de una DAO de desarrollo de software no es lo mismo que hace un buen curador en una DAO de arte. Orange Protocol permite que cada comunidad defina su propio modelo de scoring seleccionando qué fuentes importan y con qué peso, en lugar de importar el criterio de otro contexto. El tercer enfoque es el modelo basado en grafos: calcular reputación según las conexiones entre entidades, no solo por las acciones individuales. La idea es que una attestation emitida por alguien con alta reputación vale más que la misma attestation emitida por alguien desconocido, porque es mucho más difícil fabricar endorsements de entidades legítimas que crear actividad sintética. Karma3Labs implementa esta lógica sobre el grafo de Farcaster. Ninguno de los tres es superior en abstracto: el modelo de múltiples fuentes es el más fácil de integrar, el contextual es el más representativo de lo que realmente importa en cada comunidad, y el basado en grafos es el más robusto frente a ataques Sybil porque devalúa automáticamente los clusters de cuentas que solo se atestiguan entre sí.

El diseño de schemas en EAS merece atención especial. El error habitual es crear un schema cerrado tipo "contribuidor de MiDAO" que nadie más puede reutilizar. Lo correcto es diseñar schemas genéricos y componibles: un schema "DAOContribution" con campos para dirección de DAO, tipo de contribución, timestamp y enlace a prueba de trabajo puede ser adoptado por cualquier organización, y cualquier aplicación que lo reconozca puede agregar automáticamente el historial completo de un usuario a través de múltiples DAOs. La interoperabilidad real depende de esta decisión de diseño, no de la tecnología.

### Cómo debe evolucionar la reputación en el tiempo

Hay dos errores de diseño opuestos que destruyen un sistema de reputación antes de que madure. El primero es tratar la puntuación como un contador que solo sube: en pocos meses, los primeros usuarios acumulan tanta ventaja histórica que los nuevos no pueden competir aunque sean más activos hoy. La puntuación deja de medir quién contribuye ahora y se convierte en un certificado de quién llegó antes. El segundo error es diseñar un sistema que se puede saturar a ráfagas: un usuario detecta que votar en propuestas da puntos, vota en 200 propuestas en un fin de semana sin leerlas, llega al máximo posible y deja de participar. En el ecosistema se llama a esto *farming* —cosechar recompensas de forma mecánica y oportunista, sin ninguna intención genuina—, y cualquier sistema mal diseñado lo incentiva sin quererlo.

Los tres mecanismos que se describen a continuación existen precisamente para evitar ambas trampas: la acumulación con pesos y topes, la degradación por inactividad y la revocación por mal comportamiento.

**Acumulación con pesos y topes**:

La acumulación (*accumulation*) es el proceso por el que las acciones de un usuario suman puntos a su reputación. El diseño más básico asigna un peso diferente a cada tipo de acción según el valor real que aporta al protocolo. Proveer liquidez durante un mes completo —manteniendo capital bloqueado y asumiendo riesgo real— debería valer más que emitir un voto en un clic. Definir esos pesos es una decisión de negocio, no técnica: dice qué comportamientos considera valiosos el protocolo.

El problema es que sin límites, la acumulación invita al *farming*. La solución es el tope (*cap*): un límite máximo de puntos que una misma acción puede aportar en total. Si solo las primeras 50 votaciones otorgan puntos, votar 500 veces en un día no sirve de nada. El incentivo a participar sigue existiendo, pero el incentivo a participar sin criterio desaparece.

El complemento natural del tope es el multiplicador por consistencia: el mismo comportamiento vale más si se mantiene en el tiempo que si se concentra en una ráfaga. Votar en diez propuestas a lo largo de seis meses podría valer el doble que votar en diez propuestas en una semana. Esto premia la participación sostenida frente al oportunismo puntual.

**Degradación por inactividad**:

La degradación (*decay*, que en física describe cómo una señal pierde intensidad con el tiempo si no se renueva) es el mecanismo inverso: la puntuación disminuye progresivamente cuando el usuario deja de participar. Resuelve el problema del historial obsoleto: si alguien fue muy activo en 2023 pero lleva dieciocho meses sin aparecer, su puntuación alta sigue pesando en cualquier votación ponderada por reputación, desplazando a participantes que están presentes todos los días.

La forma más limpia de implementarlo es no modificar la puntuación almacenada, sino calcular en el momento de la consulta una puntuación efectiva que descuenta el tiempo transcurrido desde la última actividad. El dato guardado en la cadena no cambia —evitar escrituras innecesarias reduce el coste de gas—, pero el valor que ve cualquier aplicación refleja la realidad actual del usuario. Cuando vuelve a participar, su actividad actualiza el punto de referencia y detiene la degradación.

El mismo principio aplica a los puntos negativos. Un usuario penalizado que lleva años comportándose bien debería poder recuperar reputación progresivamente. La asimetría razonable es que los puntos negativos se degraden más despacio que los positivos: quien se portó mal tarda más en recuperar el nivel anterior, pero si mantiene buen comportamiento el tiempo suficiente, eventualmente lo consigue.

**Revocación y penalidades proporcionadas**:

La revocación es retirar reputación ya asignada cuando se verifica comportamiento malicioso, no simplemente cuando se sospecha. Puede ser automática —si el contrato detecta una violación objetiva, como un intento de doble voto— o gobernada —mediante una propuesta que la DAO aprueba colectivamente—.

Las penalidades deben ser proporcionales para que el sistema se perciba como justo. El spam de propuestas es molesto pero no destructivo: un descuento pequeño es suficiente. Un intento documentado de explotar el contrato es un ataque directo al protocolo: resetear la puntuación e imponer un período de bloqueo durante el cual no se puede acumular reputación nueva es una respuesta razonable.

Lo que no puede faltar en ningún caso es trazabilidad: cada penalidad debe quedar registrada en la cadena con la razón que la motivó. Sin esa transparencia, las penalidades parecen arbitrarias desde fuera y erosionan la confianza en el sistema incluso entre quienes no han sido sancionados. El complemento necesario a la trazabilidad es un mecanismo de apelación: el usuario penalizado debe poder publicar una contra-attestation con su versión de los hechos, visible en el mismo registro que la penalidad. No tiene por qué ser un sistema de arbitraje formal; basta con que la información agregada sea consultable por cualquiera que evalúe esa dirección. La apelación no revierte automáticamente la penalidad, pero permite que quien contrata o delega forme su propio criterio con acceso a ambas partes.

**Plataformas y protocolos que ya implementan estos patrones**:

No es necesario construir estos mecanismos desde cero. [Karma.xyz](https://www.showkarma.xyz) es una DApp: entras con tu wallet, conectas tu DAO y obtienes un dashboard que agrega la actividad on-chain y off-chain de cada contribuidor en una puntuación con pesos configurables por comunidad. Cualquier protocolo puede consultarla también por API. [Coordinape](https://coordinape.com) es otra DApp orientada al reconocimiento entre pares: el administrador de la DAO crea un "círculo" de miembros, y al final de cada ciclo cada persona reparte tokens de reconocimiento entre sus colegas. El resultado es una distribución de recompensas y un historial de quién valora a quién, que funciona de facto como acumulación con reset parcial por ciclo. Ambas tienen interfaz web y no requieren escribir código para usarlas.

[Hats Protocol](https://www.hatsprotocol.xyz) es distinto: es un protocolo de smart contracts desplegado en múltiples cadenas, con una DApp visual en [app.hatsprotocol.xyz](https://app.hatsprotocol.xyz) donde puedes diseñar la jerarquía de roles de tu organización sin código. Cada rol es un token que puede concederse y revocarse en una sola transacción, con el historial completo on-chain. Es la capa natural para traducir un score de reputación en acceso real a herramientas, fondos o poder de voto.

[SourceCred](https://sourcecred.io) es un caso diferente: es un toolkit de código abierto que instalas y ejecutas tú mismo, pensado originalmente para calcular la contribución de desarrolladores en repositorios GitHub con degradación temporal integrada. Su desarrollo se ralentizó significativamente desde 2022, pero el código sigue disponible y varias comunidades lo mantienen adaptado a sus fuentes de datos. No es una plataforma lista para usar sino una base sobre la que construir.

La estrategia habitual en producción es combinar estas piezas según el nivel de control que necesite la DAO: Karma o Coordinape para el scoring sin fricción técnica, Hats para los roles y la revocación on-chain, y EAS para los attestations que certifican el historial portablemente.

## Futuro de la Reputación Web3

### Reputación para Agentes de IA

Un agente de IA autónomo es un programa que opera de forma independiente: puede gestionar fondos en DeFi, votar en propuestas de gobernanza o firmar transacciones sin que un humano apruebe cada acción. La pregunta es: ¿deberías confiarle capital o poder de voto a un programa que funciona en base probabilidades y que además puede tener alucinaciones? Para responder surge la necesidad de reputación para estas entidades no-humanas.

El problema central es que un agente de IA, al contrario que una persona, puede copiarse infinitamente. Tú solo puedes ser tú; una IA puede clonarse en mil instancias idénticas, cada una acumulando reputación limpia por separado y luego coordinándose para explotar el sistema. La reputación de un agente, por sí sola, no garantiza nada: siempre puedes lanzar una copia nueva cuando la reputación de la original se deteriora.

La solución que se perfila no es tratar al agente como si fuera una persona, sino anclar su identidad a quien lo controla: el desarrollador o la DAO responsable de su código y su comportamiento. Si el agente actúa mal, la penalización recae sobre esa identidad humana o colectiva, no solo sobre el programa. Esto se implementa mediante attestations en cadena que establecen explícitamente esa cadena de responsabilidad: esta IA está bajo el control de esta entidad, que responde por ella.

[Autonolas](https://www.autonolas.network) es el proyecto más avanzado en este espacio: sus agentes tienen identidades on-chain propias y acumulan historial de decisiones verificable. Con el tiempo, ese historial podrá traducirse en algo equivalente a un scoring crediticio para programas: cuánto capital está dispuesta la comunidad a delegar en un agente concreto basándose en cómo se ha comportado hasta ahora.

### Sistemas de Karma dinámicos y contextuales

Los sistemas actuales usan pesos fijos: proveer liquidez vale X puntos, votar vale Y puntos. Los sistemas futuros usarán algoritmos adaptativos donde esos pesos cambian en función de cómo se está comportando el conjunto de usuarios del protocolo en cada momento.

Por ejemplo: si de repente muchos usuarios empiezan a votar masivamente en propuestas solo para acumular puntos, el algoritmo detecta ese patrón y reduce automáticamente cuánto vale cada voto. El truco pierde rentabilidad por sí solo, sin que nadie tenga que intervenir manualmente.

[Orange Protocol](https://www.orangeprotocol.io) experimenta con modelos contextuales donde tu reputación es diferente en cada comunidad basándose en comportamientos específicos valorados por esa comunidad, en lugar de un score global único.

### Mercados de predicción reputacional

Imagina poder apostar sobre el futuro comportamiento de una dirección basándote en su reputación histórica. Esto crearía mercados líquidos donde la reputación tiene precio explícito descubrible.

Por ejemplo, podrías apostar que una dirección con alta reputación DeFi no hará default en préstamos durante los próximos 12 meses. Si tienes razón, ganas rendimiento. Si la dirección hace default, pierdes tu stake.

Esto crea incentivos económicos directos para mantener buena reputación: tu reputación literalmente tiene valor de mercado que puedes perder por comportamiento malicioso. Protocolos como [Augur](https://augur.net) o [Polymarket](https://polymarket.com) podrían evolucionar para incluir markets de reputación.

### Proof of Being y Biometría descentralizada

Todo lo desarrollado en este documento —SBTs, EAS, grafos sociales, vouching con coste económico, scoring dinámico, agentes de IA con identidad on-chain— asume implícitamente algo que no está resuelto: que detrás de cada dirección hay exactamente una persona real y única. Si eso no es cierto, cualquier sistema de reputación puede vaciarse creando mil cuentas. No importa cuánto sofistiques el scoring si el actor que lo acumula puede clonarse.

Proof of Being —o Proof of Personhood— es el problema de demostrar on-chain esa unicidad. No certifica quién eres ni qué has hecho; solo responde a la pregunta más básica: ¿hay un humano ahí, y solo uno? Es la capa cero de la que dependen los anti-Sybil, los airdrops selectivos y las votaciones cuadráticas. Sin ella, todo lo construido encima es provisional.

Como se analiza en detalle en [la guía de identidad Web3](7-1-identity.md), estos mecanismos comparten un problema estructural conocido como el trilema de Proof of Personhood: ningún sistema puede ser simultáneamente descentralizado, privado y resistente a Sybil. Cada implementación cede en alguna de las tres dimensiones.

BrightID, Proof of Humanity e Idena ya existen hoy y se describieron en la guía práctica: cada una usa un mecanismo diferente para certificar que eres una persona única. El problema común es que ninguna es definitiva: siguen siendo atacables con suficiente esfuerzo y coordinación, o requieren sacrificar privacidad de formas que muchos usuarios no aceptan. Worldcoin intenta resolverlo con biometría —escanea el iris con un dispositivo físico llamado Orb para generar una prueba criptográfica de unicidad sin revelar la identidad—, lo que la convierte en la solución técnicamente más robusta contra ataques Sybil, pero centraliza el registro biométrico en una sola empresa y exige confiarle datos corporales permanentes. La comunidad no ha llegado a consenso sobre si ese intercambio es aceptable.

La conclusión honesta es que en 2026 la reputación Web3 es una arquitectura sofisticada construida sobre suelo no consolidado. Los mecanismos descritos en este documento funcionan y tienen valor real, pero todos operan asumiendo que el problema de fondo —distinguir humanos únicos de bots a escala global, sin depender de una empresa, sin revelar datos sensibles, sin excluir a quien no tiene smartphone ni documento de identidad— tiene solución suficientemente buena. Hoy no la tiene. Ese es el problema estructural pendiente del que depende todo lo demás.

### Integración cross-chain

La fragmentación de la reputación entre cadenas sigue siendo un problema a resolver en futuro —tu historial en Ethereum no es visible desde Arbitrum ni desde Solana— es un problema de infraestructura que se aborda en detalle en [La fragmentación de la reputación y el estado](../infrastructure/ethereum/reputation-state-fragmentation.md), dentro del documento de identidad Web3.

## Referencias

- [The Rise of Web3 Reputation - Gate.io](https://www.gate.com/es/learn/articles/the-rise-of-web3-reputation/7140) - Overview comprehensivo del ecosistema de reputación Web3.
- [Reputation in Web3 World - Pharos Production](https://medium.com/pharos-production/reputation-in-web3-world-1f8242438fce) - Análisis de arquitecturas de reputación descentralizada.
- [Decentralized Reputation Frontier - Kevin Owocki](https://thedefiant.io/news/research-and-opinion/decentralized-reputation-is-about-to-open-a-new-web3-frontier-kevin-owocki) - Visión del fundador de Gitcoin sobre el futuro de reputación descentralizada.
- [Decentralized Society: Finding Web3's Soul](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763) - Vitalik Buterin, Glen Weyl, Puja Ohlhaver. El paper seminal que introduce Soulbound Tokens y articula visión de sociedad descentralizada basada en reputación.
- [EigenTrust: Reputation Management in P2P Networks](https://nlp.stanford.edu/pubs/eigentrust.pdf) - Sep Kamvar, Mario Schlosser, Hector Garcia-Molina. Algoritmo clásico para calcular reputación en redes descentralizadas usando teoría de grafos.

---
