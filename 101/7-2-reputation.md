# Reputación Web3

En [identidad Web3](7-1-identity.md) vimos cómo la identidad responde a la pregunta *quién eres*: atributos verificables que te definen independientemente de tu historial de acción. La reputación responde a una pregunta distinta: *qué has hecho y qué autoridad has acumulado por ello*. No es un perfil estático que un emisor externo te otorga, sino un historial dinámico que construyes con cada acción verificable on-chain.

Esta distinción importa porque cambia quién tiene poder para definirte. Tu identidad depende en gran medida de emisores con autoridad reconocida —una universidad, un proveedor KYC, un protocolo de prueba de humanidad—. Tu reputación, en cambio, emerge de la propia red: quién te sigue, qué DAOs te aceptan como contribuidor, cuántas propuestas has votado, qué protocolo llevas años usando. Nadie te la concede; la acumulas acción a acción.

La reputación en Web3 determina mucho más de lo que tienes: dice lo que eres. Es un concepto fundamental para la gobernanza efectiva en DAOs y para la participación en el ecosistema, porque la influencia no debería reducirse solo a los tokens que posees —lo que derivaría en plutocracia— sino también a si eres un humano real activo y comprometido, algo muy relevante en muchas decisiones colectivas.

El concepto fundamental detrás de la reputación Web3 es la creación de lo que Vitalik Buterin y otros investigadores denominan "juicio colectivo programable". Esta idea, explorada en profundidad en el paper [Decentralized Society: Finding Web3's Soul](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763), plantea que la confianza y la coordinación social pueden codificarse on-chain sin depender de autoridades centrales.

Como participante en este ecosistema emergente, cada interacción on-chain que haces, cada credencial que ganas, cada contribución que realizas, no solo construye tu reputación personal sino que también ayuda a definir qué significa reputación en el futuro descentralizado que estamos construyendo juntos.

Las primitivas técnicas con las que la reputación cobra vida —SBTs, POAPs y atestaciones EAS— son las mismas que soportan la identidad on-chain, ya que el ecosistema utiliza las mismas herramientas para propósitos distintos. Aquí las exploraremos con el foco puesto en cómo se convierten en instrumentos de reputación: cómo se construyen, agregan y utilizan para determinar influencia, acceso y peso en la gobernanza.

## Visión de la Reputación

La reputación Web3 representa uno de los experimentos socio-técnicos más ambiciosos de nuestra era. Estamos intentando construir sistemas de confianza y coordinación que funcionan globalmente sin autoridades centrales, que resisten censura y manipulación, y que empoderan individuos en lugar de corporations.

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

Actualmente existe una gran fragmentación en cómo se define a un participante legítimo. Protocolos como Gitcoin Passport, Proof of Humanity o BrightID utilizan criterios y arquitecturas diferentes. Al no existir un estándar técnico universal, la reputación acumulada en un ecosistema rara vez es interoperable o traducible de forma directa a otro. Esta falta de componibilidad técnica limita la promesa de una identidad verdaderamente portable.

**El Problema del Arranque en Frío y el Oráculo Social**:

Construir un historial on-chain requiere, por definición, interactuar en la blockchain desde cero, lo que excluye el valor aportado previamente por un usuario en el mundo tradicional. Para mitigar esto, se intenta importar credibilidad off-chain, pero esto requiere oráculos y puentes de validación centralizados. Técnicamente, la blockchain solo puede registrar eventos deterministas, lo que dificulta integrar acciones cualitativas humanas (como liderazgo o mentoría) sin depender de un punto central de confianza, sesgando el sistema a medir únicamente lo programáticamente cuantificable.

**Privacidad frente a Verificabilidad**:

La transparencia por defecto de la blockchain pública entra en conflicto con el derecho a la privacidad. Para que una credencial funcione como reputación, suele ser visible para todos, lo que permite trazar el comportamiento y las afiliaciones de una persona. Aunque existen soluciones criptográficas como las pruebas de conocimiento cero para proteger los datos, integrarlas en los sistemas de reputación actuales añade una enorme complejidad computacional que aún limita su uso masivo.

**Sesgo Cuantitativo y de Dominio**:

Hay además un sesgo conceptual que vale la pena nombrar. Los sistemas actuales de reputación Web3 miden lo tangible y verificable: transacciones, votos, badges. Esto responde a una visión muy práctica de lo que significa contribuir. La confianza, la capacidad de escuchar, la habilidad para resolver conflictos o formar a otros no dejan rastro on-chain fácilmente medible. No es un fallo técnico resoluble con mejores herramientas, sino una limitación de qué tipo de realidad puede representar un protocolo. Y el riesgo derivado es conocido: inferir competencias de un dominio a otro. Que alguien sea un desarrollador excelente no dice nada sobre si será un buen coordinador de DAO o un buen mentor. La reputación on-chain puede reforzar este salto lógico si no se diseña con cuidado.

### Manipulación y Confianza

Cuanto más valioso es un sistema, más incentivos hay para engañarlo. La reputación Web3 no es una excepción.

La forma más directa de manipularlo es crear muchas identidades falsas para acumular reputación en masa y luego utilizarla para votar, obtener acceso o recibir recompensas que no corresponden a una participación real. Esto se conoce como ataque Sybil. Pero existe una variante más sutil y difícil de detectar: usar una identidad legítima —una wallet real, con historial real— para simular participación sin tener ninguna intención genuina. Por ejemplo, votar en propuestas sin leerlas, completar tareas de forma mecánica para acumular puntos, o ponerse de acuerdo con conocidos para intercambiarse credenciales mutuamente. Desde fuera, todo parece actividad auténtica. Por eso es tan complicado de frenar.

Para reducir este comportamiento, algunos sistemas aplican un principio sencillo: la reputación pierde valor si no se mantiene activa, o bien las ultimas acciones cuentan más que las repetidas, de modo que acumular en masa resulte menos rentable. Estas medidas dificultan el abuso, pero no lo eliminan del todo.

Hay además un problema de fondo que ninguna regla técnica sobre "intransferibilidad" puede resolver: aunque credenciales como los SBTs no se puedan mover de una cuenta a otra, **la cuenta entera puede cambiar de dueño**. Por un lado, existen mercados informales oscuros donde se compran y venden llaves privadas de wallets antiguas con reputación acumulada por miles de dólares. Por otro lado, como explicaremos en su propia sección, la llegada de estándares como el **ERC-6551 (Token Bound Accounts)** estandariza esto: al permitir que un NFT controle una wallet, toda la reputación de esa wallet queda atrapada dentro de un activo intercambiable. Puedes vender legalmente en un mercado abierto tu "NFT de perfil" con todos sus diplomas y reputación dentro. Esta financiarización de la identidad significa que, cuanto más valiosa e influyente se vuelve la reputación en Web3, mayor es el incentivo económico para empaquetarla, venderla o manipularla.

### Inclusión y Exclusión Estructural

El problema no es el coste de las transacciones —los L2 lo han resuelto en gran medida— sino que los mecanismos de reputación están construidos sobre historial on-chain acumulado en el tiempo. Esto privilegia estructuralmente a los early adopters: quien llega hoy parte de cero, y los sistemas de scoring penalizan esa ausencia histórica sin importar la capacidad real del nuevo participante. El efecto Mateo opera sin necesidad de intención: la reputación tiende a acumularse donde ya existe, porque las DAOs delegan trabajo y los protocolos seleccionan a wallets con actividad consolidada. Estudios sobre redes descentralizadas como [Measuring Decentralization in Web3 Social Networks](https://arxiv.org/abs/2302.10825) muestran que la concentración en estos sistemas reproduce, y a veces amplifica, la del mundo off-chain. A eso se suma una barrera cultural menos visible: participar requiere navegar foros de gobernanza, leer propuestas técnicas en inglés y moverse por comunidades con normas no escritas heredadas de la cultura anglosajona de internet.

### Regulación y Vacío Jurídico

El [GDPR europeo](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32016R0679) exige cosas que una blockchain, por diseño, no puede dar. Garantiza el derecho a borrar datos personales, pero una *attestation* on-chain es inmutable. Las soluciones técnicas que se intentan, como guardar la información fuera de la cadena (*off-chain*) o usar funciones de revocación que ocultan la credencial pero dejan su rastro, son parches que, estrictamente, no cumplen el espíritu de la norma.

Más delicado aún es el problema de la responsabilidad. Si un emisor publica una credencial falsa y eso causa un daño económico, ¿a quién se denuncia? No hay un juzgado claro ni una empresa identificable a la que exigir cuentas. El daño ocurre en el mundo real, pero no existe un remedio legal para solucionarlo.

Además, el uso de la reputación ya está entrando en terrenos altamente regulados en el mundo tradicional. Protocolos como [Spectral Finance](https://www.spectral.finance) usan el historial de la wallet para decidir las condiciones de un préstamo. En casi cualquier país, esto activa inmediatamente la normativa sobre *scoring* crediticio: el usuario tiene derecho a saber qué criterios se han usado, a reclamar si no está de acuerdo y a que se justifique la decisión. Nada de esto existe hoy en DeFi.

Todo apunta a que, a la larga, no se creará una ley especial a medida para Web3. Lo más probable es que se apliquen directamente las leyes que ya existen —sobre protección de datos, sobre crédito, contra la discriminación— a una tecnología que se construyó creyendo que las reglas del mundo tradicional no le afectaban.

## Herramientas y Protocolos de Reputación

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

### ERC-6551 (Token Bound Accounts): La Reputación del Avatar

Hasta ahora, en este documento hemos asumido que la reputación se vincula a tu cuenta principal (tu wallet). Tú, como usuario, recibes los POAPs participando en eventos y acumulas *attestations* por tu trabajo.

El estándar **ERC-6551 (Token Bound Accounts o TBA)** introduce un giro conceptual muy potente: **permite que un NFT tenga su propia wallet**. 

Para entenderlo de forma sencilla: imagina que tienes un NFT que representa tu personaje en un juego o tu credencial vitalicia de una comunidad. Con este estándar, ese "personaje" adquiere su propia dirección en la blockchain. A partir de ese momento, cuando haces una tarea para una DAO usando ese personaje, es el NFT (y no tu wallet personal) quien recibe el pago, el POAP o el *Soulbound Token* (SBT) que certifica el logro. **La reputación ya no te pertenece a ti como individuo, le pertenece al activo digital.**

Esto aporta dos dimensiones indispensables que cambian las reglas del juego:

1. **Identidades separadas y portables:** Puedes "compartimentar" tu vida digital sin gestionar docenas de contraseñas. Un NFT puede ser tu perfil profesional (acumulando certificaciones formales) y otro NFT distinto puede ser tu perfil de *gamer* (acumulando torneos). Lo más interesante es que si alguna vez sospechas que tu wallet principal ha sido comprometida por un hacker, o simplemente quieres usar un nuevo software de seguridad, puedes simplemente enviar estos NFTs a tu nueva wallet. Tu reputación viaja empaquetada con el NFT; un cambio de llaves no significa perder tu identidad.
2. **Transferibilidad de la reputación (El vacío legal):** Los *Soulbound Tokens* (SBTs) nacieron para no poder moverse; si estudiaste algo, no le puedes vender tu diploma a otra persona. Sin embargo, ERC-6551 crea un vacío legal (un *loophole*): si tu diploma (SBT) se envía a la wallet interna de tu NFT, el diploma sigue sin poder moverse de ahí... pero **tú sí puedes vender el NFT completo en un mercado como OpenSea**. Le acabas de vender a un tercero un "personaje" que ya incluye años de reputación intachable, credenciales y acceso a zonas exclusivas. Esto formaliza la compra y venta de historial.

### Grafo Social y Web of Trust

La reputación basada en credenciales —SBTs, attestations EAS, POAPs— responde a la pregunta de qué has hecho y quién lo certifica. Hay otra dimensión igualmente importante: quién te conoce y confía en ti. Esta distinción separa la reputación acreditada de la reputación relacional, y es la que captura el concepto de web of trust.

El web of trust tiene origen en criptografía: en los años noventa, PGP formalizó la idea de que la confianza en una clave pública puede derivarse no de una autoridad central sino de la acumulación de firmas de otros usuarios que ya se confían entre sí. Quien tiene muchas firmas de personas reconocidas en la comunidad es implícitamente más confiable que quien no tiene ninguna, aunque sus credenciales formales sean equivalentes. Este principio, trasladado a Web3, convierte el grafo de relaciones sociales en señal de reputación. El paper [EigenTrust: Reputation Management in P2P Networks](https://nlp.stanford.edu/pubs/eigentrust.pdf) formalizó matemáticamente cómo la confianza se propaga en estas redes usando teoría de grafos.

Los protocolos que materializan esta idea en Web3 son principalmente [Lens Protocol](https://lens.xyz) y [Farcaster](https://www.farcaster.xyz). Lens es un grafo social descentralizado donde los follows, comentarios y mirrors son activos on-chain: seguir a alguien emite un NFT que representa esa relación, composable y reutilizable por cualquier aplicación construida sobre el protocolo. Farcaster opera con una arquitectura diferente —identidades on-chain en Optimism, pero contenido almacenado en hubs descentralizados fuera de la cadena— con el objetivo declarado de ser "sufficiently decentralized": lo suficientemente descentralizado para que ninguna entidad pueda censurar o capturar el protocolo.

El vínculo entre estos grafos y la reputación es doble. Por un lado, la estructura del grafo en sí es ya una señal: quien acumula seguidores genuinos entre personas con alto capital social on-chain tiene una reputación relacional que no puede fabricarse fácilmente, porque requiere que otras personas reales con historial verificable decidan seguirte. Por otro lado, el grafo puede analizarse algorítmicamente para derivar scores. [Karma3Labs](https://karma3labs.com) aplica EigenTrust al grafo de Farcaster para calcular scores de confianza que los protocolos pueden consumir como señal de reputación anti-Sybil, materializando en producción lo que el paper de Stanford describía en teoría.

La limitación más importante de la reputación social es que hereda los sesgos del grafo. Si el grafo está dominado por early adopters anglosajones —que es la situación actual tanto en Lens como en Farcaster— el score refleja proximidad a ese núcleo, no mérito universal. Un desarrollador excelente pero recién llegado puede tener score bajo simplemente porque aún no está conectado a los nodos con mayor peso. La promesa del web of trust es la portabilidad y la composabilidad; el riesgo es la reproducción y amplificación de las jerarquías existentes.

## Mecanismos de Construcción de Reputación

La reputación en Web3 no se declara, se construye mediante acciones verificables on-chain. A continuación exploramos los principales mecanismos que permiten esta construcción.

**Reputation Mining**:

El concepto de reputation mining se refiere al proceso de acumular reputación mediante participación activa y verificable en protocolos y ecosistemas. Similar a cómo los mineros de Bitcoin ganan recompensas por asegurar la red, los usuarios ganan reputación por contribuir valor a los ecosistemas Web3.

Un ejemplo concreto es [RabbitHole](https://rabbithole.gg), una plataforma donde los usuarios completan "quests" que implican interactuar con protocolos DeFi reales. Al completar una quest como "proveer liquidez en Uniswap V3" o "votar en una propuesta de gobernanza de Compound", ganas tanto tokens como experiencia (XP) verificable on-chain. Este historial de participación se convierte en tu reputación demostrable.

El artículo de CoinDesk sobre [Reputation Mining](https://www.coindesk.com/sponsored-content/reputation-mining-builds-new-trust-via-web-3) explora cómo este mecanismo está creando nuevas formas de confianza verificable que no dependen de autoridades centrales.

## Guía Práctica para Construir Reputación

Esta sección proporciona pasos concretos para usuarios que quieren comenzar a construir su reputación Web3, organizados por nivel de experiencia.

### Configuración Inicial

El primer paso para cualquier usuario es establecer las fundaciones básicas de identidad y seguridad antes de comenzar a acumular reputación verificable.

**Establecer tu identidad on-chain**:

El primer paso es elegir una dirección que planeas mantener durante años y consolidar en ella toda tu actividad pública. Un error frecuente es crear múltiples wallets y fragmentar el historial: si repartes tus contribuciones, tus POAPs y tus votos entre varias direcciones, ninguna cuenta la historia completa. Puedes usar otras direcciones para privacidad financiera, pero tu reputación debería vivir en una sola identidad principal.

Una vez tienes esa dirección, registra un nombre [ENS (Ethereum Name Service)](https://ens.domains). En lugar de compartir 0x1234...5678, compartes tusername.eth, que es mucho más memorable y funciona como punto de entrada reconocible en cualquier aplicación Web3. El coste es aproximadamente $5-20 al año según la longitud del nombre. Algunos empleadores en Web3 piden directamente el ENS en lugar de un CV tradicional.

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

[RabbitHole](https://rabbithole.gg) y [Layer3](https://layer3.xyz) ofrecen quests para principiantes que no requieren capital significativo. Comienza con quests de "onboarding" que te enseñan conceptos básicos como usar swaps en Uniswap, conectar a diferentes L2s, o interactuar con protocolos de staking.

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
- **Verificación de humanidad**: Usar herramientas como [BrightID](https://www.brightid.org/) para certificar que eres una persona única.

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

## Implementación para Proyectos y Builders

Esta sección está dirigida a desarrolladores, product managers y founders que quieren implementar sistemas de reputación en sus propios protocolos o aplicaciones.

### Definir Objetivos y Casos de Uso

Antes de implementar cualquier infraestructura técnica, necesitas claridad absoluta sobre por qué estás implementando reputación y qué problemas específicos resuelve.

**Identificar el Propósito Principal**:

Los sistemas de reputación pueden servir cuatro propósitos principales, cada uno con requisitos técnicos diferentes. El control de acceso usa reputación para determinar quién puede usar tu protocolo o acceder a features específicos. Por ejemplo, un protocolo de préstamos podría requerir Gitcoin Passport score mínimo de 20 para acceder a préstamos subcolateralizados.

Los sistemas de incentivos usan reputación para distribuir recompensas de forma más justa. Un programa de airdrops podría ponderar distribución basándose en scores de reputación en lugar de solo token holdings, previniendo que ballenas dominen completamente.

La gobernanza ponderada combina reputación con holdings de tokens para la votación. Como vimos con Optimism, esto previene la plutocracia pura al tiempo que mantiene el compromiso económico de los participantes.

La reducción de riesgo usa reputación para identificar actores maliciosos o comportamiento sospechoso. Marketplaces descentralizados podrían usar reputación de vendedores para proteger compradores.

Define tu propósito primario claramente porque determina qué tipos de datos de reputación son relevantes y cómo deben ponderarse.

**Mapear Comportamientos Deseados**:

Especifica exactamente qué comportamientos quieres incentivar. Si quieres participación en gobernanza, ¿valoras más la cantidad de votos o la calidad del análisis? Si quieres proveedores de liquidez a largo plazo, ¿cómo defines "largo plazo" y cómo prevenir gaming mediante pools de rotación?

Crea una tabla que mapee comportamientos específicos a rewards de reputación específicos. Por ejemplo, votar en propuesta de gobernanza = +5 puntos de reputación, pero solo si votaste en al menos 3 de las últimas 5 propuestas (previene voto selectivo solo en propuestas controvertidas).

### Seleccionar Fuentes de Datos y Arquitectura

Una vez definidos los objetivos, decide qué datos consumir y cómo estructurar tu sistema.

**On-Chain versus Off-Chain**:

Datos on-chain puros proporcionan máxima verificabilidad y resistencia a censura pero están limitados a transacciones blockchain. Esto funciona bien si tu reputación se basa exclusivamente en comportamiento on-chain como provision de liquidez, votaciones, o uso de smart contracts.

Datos off-chain permiten incorporar actividad en GitHub, Twitter, Discord, o bases de datos propietarias. Esto amplía scope dramáticamente pero requiere oráculos confiables. [Chainlink Functions](https://chain.link/functions) puede ayudar a traer datos off-chain on-chain de forma descentralizada, pero siempre introduce un punto de confianza.

La arquitectura híbrida óptima usa datos on-chain como base primaria y complementa con datos off-chain verificados mediante attestations de terceros confiables. Por ejemplo, Gitcoin Passport usa transacciones on-chain directamente pero consume attestations de proveedores de identidad para datos sociales.

**Elegir Protocolos de Infraestructura**:

Para attestations, [Ethereum Attestation Service](https://attest.sh) es la opción estándar. Permite crear schemas personalizados y emitir attestations on-chain o off-chain. La ventaja es interoperabilidad: attestations emitidas mediante EAS pueden ser consumidas por otras aplicaciones.

Para almacenamiento de datos de identidad, [Ceramic Network](https://ceramic.network) proporciona almacenamiento descentralizado de datos mutables vinculados a DIDs. Esto permite que usuarios actualicen sus perfiles sin cambiar identificadores.

Para indexación y queries eficientes, deploy un subgraph en [The Graph](https://thegraph.com) que indexe eventos relevantes de tu contrato o consume datos de EAS. Esto hace que consultar reputación histórica sea instantáneo en lugar de require escanear toda la blockchain.

**Diseño de Schemas**:

Si usas EAS, diseña schemas de attestation cuidadosamente. Un schema bien diseñado es reutilizable y componible. Por ejemplo, en lugar de crear un schema específico "contribuidor de MiDAO", crea un schema genérico "DAOContribution" con campos para: dirección de DAO, tipo de contribución, timestamp, monto de compensación, y enlace a prueba de trabajo.

Este schema puede ser usado por cualquier DAO, creando un estándar emergente. Aplicaciones de agregación pueden reconocer el patrón y visualizar contribuciones de todas las DAOs que usan este schema.

### Implementar Mecanismos de Actualización y Decay

La reputación no debe ser estática; debe evolucionar basándose en comportamiento continuo.

**Acumulación de Reputación**:

Define reglas claras sobre cómo crece la reputación. Usa sistemas de puntos donde diferentes acciones otorgan diferentes cantidades. Proveer liquidez durante 30 días podría valer 10 puntos, votar en una propuesta 2 puntos, referir un nuevo usuario verificado 5 puntos.

Considera multiplicadores por consistencia. El mismo comportamiento repetido durante meses debería valer más que actividad explosiva de corto plazo. Por ejemplo, votar en 10 propuestas a lo largo de 6 meses podría valer 30 puntos, mientras que votar en 10 propuestas en una semana solo vale 15 puntos.

Implementa caps para prevenir farming infinito. Quizás solo las primeras 50 votaciones otorgan puntos, previniendo que usuarios simplemente voten en todo sin análisis.

**Decay y Degradación**:

La reputación debería decaer con inactividad para mantener scores actualizados. Un score de gobernanza de hace 2 años cuando alguien era activo pero ha estado ausente desde entonces no refleja participación actual.

Implementa decay temporal: por ejemplo, 5% de decay por mes de inactividad. Esto significa que mantener reputación alta requiere participación sostenida. Alternativamente, usa fechas de expiración en attestations individuales que deben ser renovadas periódicamente.

El decay también debería aplicarse a comportamiento negativo. Un mal actor que se rehabilita mediante años de buen comportamiento eventualmente debería poder recuperar reputación. Considera que eventos negativos decaigan más lento que eventos positivos, pero que eventualmente desaparezcan.

**Revocación y Penalidades**:

Implementa mecanismos para revocar reputación cuando comportamiento malicioso es verificado. Esto podría ser automated (si smart contract detecta violación de reglas) o governed (mediante votación de la comunidad).

Las penalidades deberían ser proporcionales. Spam podría resultar en -10 puntos. Intento de exploit de contrato podría resultar en ban completo con score reducido a cero. Provee transparencia: cuando reputación es penalizada, registra la razón on-chain para accountability.

### Preservar Privacidad y Permitir Portabilidad

Estos dos principios son cruciales para sistemas de reputación éticos y sostenibles.

**Implementar Selective Disclosure**:

Los usuarios deberían poder probar aspectos específicos de su reputación sin revelar todo su historial. Esto requiere zero-knowledge proofs, que es técnicamente complejo pero cada vez más accesible.

[Sismo](https://sismo.io) proporciona SDK que permite integrar ZK proofs de reputación. Podrías implementar sistema donde usuarios prueban "mi Gitcoin Passport score es > 25" sin revelar su score exacto o qué stamps específicamente tienen.

Para casos de uso menos sensibles, permite que usuarios configuren qué partes de su perfil son públicas versus privadas. Quizás muestran su score agregado pero ocultan breakdown específico de fuentes.

**Garantizar Exportabilidad**:

Nunca encierres datos de reputación en tu sistema. Proporciona APIs públicas y documentadas para que usuarios puedan exportar toda su información de reputación en formatos estándar como JSON-LD o Verifiable Credentials del W3C.

Idealmente, almacena reputación en infraestructura neutral como EAS o Ceramic en lugar de bases de datos propietarias. Esto garantiza que incluso si tu aplicación desaparece, las credenciales de usuarios persisten.

Implementa estándares abiertos como DIDs del W3C para identidades en lugar de identificadores propietarios. Esto permite que reputación sea portable entre diferentes aplicaciones y ecosistemas.

## Futuro de la Reputación Web3

### Reputación para Agentes de IA

Con el surgimiento de agentes de IA autónomos que ejecutan transacciones on-chain, surge la necesidad de reputación para entidades no-humanas. Un agente de IA que gestiona un fondo de inversión DeFi necesitará construir reputación basándose en su track record de decisiones.

Esto es fundamentalmente diferente de reputación humana porque los agentes pueden ser copiados infinitamente. La solución probablemente involucre vincular agentes de IA a identidades humanas responsables (el desarrollador o DAO que lo controla) mediante attestations en cadena de responsabilidad.

[Autonolas](https://www.autonolas.network) está explorando este espacio con agentes autónomos que tienen identidades on-chain y acumulan reputación mediante sus acciones. Surgirán "credit scores" para agentes de IA que determinen cuánto capital la comunidad está dispuesta a confiarles.

### Sistemas de Karma Dinámicos y Contextuales

Los sistemas actuales usan pesos fijos: proveer liquidez vale X puntos, votar vale Y puntos. Los sistemas futuros usarán algoritmos adaptativos donde los pesos cambian basándose en comportamiento agregado de la cohorte.

Si el 90% de usuarios están farmeando un tipo específico de actividad, el algoritmo automáticamente reduce el peso de esa actividad para prevenir dilución de valor. Esto crea un sistema auto-balanceado donde gaming es cada vez más difícil porque los farmers se compiten entre sí.

[Orange Protocol](https://www.orangeprotocol.io) experimenta con modelos contextuales donde tu reputación es diferente en cada comunidad basándose en comportamientos específicos valorados por esa comunidad, en lugar de un score global único.

### Mercados de Predicción Reputacional

Imagina poder apostar sobre el futuro comportamiento de una dirección basándote en su reputación histórica. Esto crearía mercados líquidos donde la reputación tiene precio explícito descubrible.

Por ejemplo, podrías apostar que una dirección con alta reputación DeFi no hará default en préstamos durante los próximos 12 meses. Si tienes razón, ganas rendimiento. Si la dirección hace default, pierdes tu stake.

Esto crea incentivos económicos directos para mantener buena reputación: tu reputación literalmente tiene valor de mercado que puedes perder por comportamiento malicioso. Protocolos como [Augur](https://augur.net) o [Polymarket](https://polymarket.com) podrían evolucionar para incluir markets de reputación.

### Proof of Being y Biometría Descentralizada

El mayor desafío sin resolver de reputación es Proof of Personhood definitivo. Worldcoin representa un enfoque mediante biometría centralizada, pero la comunidad busca alternativas descentralizadas.

Tecnologías emergentes como [Proof of Humanity](https://www.proofofhumanity.id) combinan video verificación, depósitos económicos, y arbitraje descentralizado. [Idena](https://idena.io) usa validation puzzles síncronos. Futuros sistemas podrían usar análisis de comportamiento on-chain sofisticado para detectar patrones que son prácticamente imposibles de replicar por bots a escala.

El objetivo final es un sistema que distinga definitivamente humanos únicos de Sybils sin requerir un sacrificio extremo de privacidad.

### Integración Cross-Chain Universal

Actualmente, reputación está mayormente fragmentada por chain. Tu actividad en Ethereum no se refleja automáticamente en Polygon o Solana. El futuro requiere agregación cross-chain transparente.

Protocolos como [LayerZero](https://layerzero.network) y [Axelar](https://axelar.network) están construyendo infraestructura de mensajería cross-chain que podría permitir que attestations emitidas en una chain sean verificables en cualquier otra.

Surgirán "reputation oracles" que agregan datos de múltiples chains en scores unificados. Tu reputación total incorporaría actividad en Ethereum, Polygon, Arbitrum, Solana, y cualquier otra chain donde participas.

## Referencias

- [The Rise of Web3 Reputation - Gate.io](https://www.gate.com/es/learn/articles/the-rise-of-web3-reputation/7140) - Overview comprehensivo del ecosistema de reputación Web3.
- [Reputation in Web3 World - Pharos Production](https://medium.com/pharos-production/reputation-in-web3-world-1f8242438fce) - Análisis de arquitecturas de reputación descentralizada.
- [Decentralized Reputation Frontier - Kevin Owocki](https://thedefiant.io/news/research-and-opinion/decentralized-reputation-is-about-to-open-a-new-web3-frontier-kevin-owocki) - Visión del fundador de Gitcoin sobre el futuro de reputación descentralizada.
- [Decentralized Society: Finding Web3's Soul](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763) - Vitalik Buterin, Glen Weyl, Puja Ohlhaver. El paper seminal que introduce Soulbound Tokens y articula visión de sociedad descentralizada basada en reputación.
- [EigenTrust: Reputation Management in P2P Networks](https://nlp.stanford.edu/pubs/eigentrust.pdf) - Sep Kamvar, Mario Schlosser, Hector Garcia-Molina. Algoritmo clásico para calcular reputación en redes descentralizadas usando teoría de grafos.

---
