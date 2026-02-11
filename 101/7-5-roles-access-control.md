# Roles y Control de Acceso en Web3

La gestión de permisos en sistemas descentralizados plantea uno de los desafíos más delicados del ecosistema Web3. A diferencia de sistemas tradicionales donde un administrador puede modificar permisos desde un servidor central y revertir errores mediante backups de base de datos, en Web3 el control de acceso está codificado en smart contracts inmutables cuyas decisiones son irreversibles. Cuando un protocolo DeFi custodia miles de millones de dólares o una DAO controla treasuries valorados en cientos de millones, la arquitectura de permisos no es un detalle técnico secundario sino la frontera que separa un ecosistema seguro de uno vulnerable.

Este documento explora cómo los sistemas descentralizados están construyendo mecanismos de control de acceso que mantienen principios de descentralización mientras proporcionan flexibilidad operativa y protección contra abuso. Veremos desde modelos simples de propiedad única hasta complejas jerarquías de roles con delays temporales, desde sistemas multi-firma que requieren consenso hasta lógica programática que ejecuta reglas de negocio automáticamente. Entender estos mecanismos es fundamental porque la mayoría de exploits históricos en Web3 no provienen de vulnerabilidades criptográficas sofisticadas, sino de fallos básicos en quién puede hacer qué.

## Tipos de control de acceso: del mundo tradicional a Web3

Antes de explorar control de acceso específico de blockchain, es útil entender los modelos que informática tradicional ha desarrollado durante décadas y por qué Web3 adoptó RBAC como arquitectura predominante.

**DAC (Discretionary Access Control)** es el modelo más intuitivo y ampliamente usado en sistemas tradicionales. El propietario de un recurso decide discrecionalmente quién puede acceder. Piensa en el sistema de archivos de Linux o Windows: si creas un archivo, tú decides si otros usuarios pueden leerlo, modificarlo o ejecutarlo. Este modelo es simple y flexible pero depende completamente de que propietarios individuales tomen decisiones correctas de seguridad, lo cual raramente sucede consistentemente en sistemas complejos.

**MAC (Mandatory Access Control)** invierte la autoridad. En lugar de que usuarios decidan permisos, el sistema operativo aplica políticas de seguridad obligatorias que usuarios individuales no pueden modificar, incluso si son propietarios del recurso. Implementaciones como SELinux y AppArmor en Linux usan MAC para confinar procesos mediante políticas centralizadas. Un proceso web comprometido no puede acceder a archivos de configuración del sistema incluso si el exploit le da privilegios del usuario web, porque las políticas MAC del sistema lo prohíben explícitamente. Este modelo proporciona mayor seguridad mediante aplicación rigurosa de principio de menor privilegio, pero sacrifica flexibilidad y requiere administración centralizada sofisticada.

**RBAC (Role-Based Access Control)** emergió como punto medio pragmático especialmente valioso en organizaciones grandes. En lugar de asignar permisos individualmente a miles de empleados o confiar en que cada empleado configure permisos correctamente, la organización define roles abstractos como "Contador", "Ingeniero", "Gerente", cada uno con permisos específicos. Cuando contratas un nuevo contador, simplemente le asignas el rol Contador y automáticamente hereda todos los permisos apropiados. Cuando alguien cambia de departamento, revocas el rol antiguo y asignas el nuevo. Esta separación entre identidad y capacidad hace que sistemas complejos con muchos usuarios y recursos sean administrables.

Web3 adoptó RBAC casi universalmente por razones que reflejan tanto las fortalezas inherentes del modelo como las limitaciones únicas de blockchain. La inmutabilidad hace que DAC sea peligroso: si el propietario pierde su clave privada, el recurso queda inaccesible permanentemente sin mecanismo de recuperación. RBAC permite que múltiples direcciones compartan roles, proporcionando redundancia. La transparencia hace que MAC sea innecesario: cualquiera puede auditar el código del contrato para verificar que aplica políticas correctamente, eliminando necesidad de autoridad central que aplique políticas. Y la descentralización hace que RBAC sea natural: los protocolos necesitan delegar responsabilidades específicas a grupos diferentes sin concentrar todo el poder, exactamente lo que roles permiten.

La diferencia crítica es que en Web2, violar control de acceso típicamente requiere explotar vulnerabilidades técnicas sofisticadas o comprometer sistemas mediante malware. En Web3, el código del contrato define permisos absolutamente y está visible públicamente. No hay capa adicional de sistema operativo o firewall. Si el contrato dice que una dirección con cierto rol puede ejecutar una función, esa dirección puede ejecutarla, punto. Esta simplicidad radical hace que diseño correcto de control de acceso sea absolutamente crítico desde el deployment inicial.

## El dilema de permisos en sistemas inmutables

El control de acceso en Web2 es conceptualmente directo. Existe un servidor central, una base de datos con usuarios y permisos, y un administrador con capacidad de modificar todo. Cuando algo falla, el sistema puede pausarse, los cambios pueden revertirse mediante backups, y el código puede parchearse. Este modelo centralizado proporciona flexibilidad operativa a costa de concentrar poder en pocas manos.

Web3 elimina esa autoridad central mediante inmutabilidad. Una vez que un smart contract se despliega en blockchain, su código está permanentemente grabado. No existe botón de deshacer ni administrador omnipotente que pueda revertir transacciones. Si despliegas un contrato con un bug crítico en el sistema de permisos, un atacante podría drenar fondos sin que haya mecanismo de recuperación mediante intervención administrativa.

Esta inmutabilidad fundamental crea una tensión inherente. Los protocolos necesitan flexibilidad para evolucionar, arreglar bugs inevitables, añadir funcionalidades demandadas por la comunidad y ajustar parámetros económicos conforme cambian condiciones de mercado. Pero simultáneamente necesitan garantías criptográficamente sólidas de que nadie puede abusar de esos privilegios administrativos. Si un contrato puede ser pausado para proteger fondos durante un ataque, ¿quién controla ese poder de pausa? Si los parámetros económicos pueden ajustarse, ¿cómo prevenimos que un desarrollador malicioso o comprometido destruya el protocolo?

La transparencia radical de blockchain amplifica el desafío. Cualquier atacante puede leer el código completo del contrato, analizar exactamente quién tiene qué permisos, estudiar vulnerabilidades potenciales y planear exploits meticulosamente. No existe seguridad por oscuridad. El sistema de control de acceso debe ser tan robusto que, incluso cuando un adversario conoce exactamente cómo funciona, aún no puede comprometerlo.

La historia de exploits en Web3 revela un patrón consistente. El hack de The DAO en 2016 que costó 50 millones de dólares, Ronin Bridge en 2022 con pérdidas de 625 millones, Poly Network en 2021 con 611 millones robados, todos estos incidentes involucraron fallos fundamentales donde atacantes pudieron ejecutar acciones que nunca deberían haber estado autorizados a realizar. La lección es clara: el control de acceso no es un detalle de implementación sino la primera línea de defensa.

## Control de acceso basado en roles

El patrón más ampliamente adoptado en Web3 para gestionar permisos es el control de acceso basado en roles, conocido como RBAC por sus siglas en inglés. La idea fundamental es elegante en su simplicidad: en lugar de asignar permisos individuales a cada dirección wallet específica, el protocolo define roles abstractos con nombres descriptivos, y luego asigna esos roles a las direcciones que deben ejercer esas responsabilidades.

Piensa en roles como ADMIN, MINTER, PAUSER, BURNER, UPGRADER. Cada uno representa un conjunto específico de capacidades dentro del sistema. Cuando alguien intenta ejecutar una función crítica, el contrato verifica que la dirección llamante posea el rol correspondiente antes de permitir la ejecución. Este modelo separa la identidad de la capacidad, permitiendo que roles se transfieran o revoquen sin cambiar el código del protocolo.

[OpenZeppelin AccessControl](https://docs.openzeppelin.com/contracts/4.x/access-control) se ha convertido en el estándar de facto para implementar RBAC en Ethereum y chains compatibles con EVM. Su diseño permite crear cualquier número de roles, cada uno con su propio rol administrador que controla quién puede otorgar o revocar ese rol específico. Múltiples direcciones pueden compartir el mismo rol, y una sola dirección puede acumular múltiples roles, proporcionando flexibilidad organizacional considerable.

La arquitectura soporta jerarquías de roles donde ciertos roles tienen autoridad sobre otros. Por defecto existe un rol de administrador principal que controla todos los demás roles, pero esta estructura puede refinarse para crear separación de poderes. Un rol de administrador de seguridad podría controlar quién puede pausar el protocolo, mientras que un rol de administrador de tesorería controla permisos relacionados con manejo de fondos. Esta granularidad permite descentralización progresiva donde diferentes aspectos del protocolo pueden delegarse a distintos grupos.

En la práctica, los casos de uso varían según el tipo de protocolo. Un token típico podría tener un rol MINTER que puede crear nuevos tokens para recompensas de staking o liquidez, un rol PAUSER que puede congelar transferencias durante emergencias, y un rol SNAPSHOT que puede crear instantáneas del estado del token para votaciones de gobernanza. Una DAO podría definir roles para crear propuestas, ejecutar decisiones aprobadas, pausar operaciones en emergencias y gestionar delays temporales en ejecuciones críticas. Protocolos DeFi suelen tener roles para administrar parámetros de pools de liquidez, ajustar fees del protocolo y actualizar oráculos de precios. Para más contexto sobre cómo las DAOs estructuran su gobernanza, consulta [7-3-DAO.md](7-3-DAO.md).

## El modelo de propiedad única

En el extremo opuesto de complejidad está el patrón de propiedad única, donde un solo propietario controla todas las funciones administrativas del protocolo. Este modelo, conocido como Ownable en el ecosistema [OpenZeppelin](https://docs.openzeppelin.com/contracts/4.x/api/access#Ownable), sacrifica descentralización a cambio de simplicidad operativa extrema.

La lógica es directa: cada función crítica verifica que quien la llama sea el propietario actual. Si la verificación falla, la transacción revierte. El propietario puede transferir este control a otra dirección en cualquier momento, permitiendo transiciones de liderazgo o delegación a estructuras más complejas como multisigs.

Esta centralización radical representa un punto único de fallo crítico. Una sola clave privada controla el protocolo completo. Si esa clave se compromete mediante hackeo, ingeniería social, pérdida física del dispositivo de almacenamiento o coacción del poseedor, el atacante obtiene control total e irreversible. No hay mecanismo de recuperación ni contrapesos.

Por esta razón, el modelo de propiedad única solo es aceptable en contextos muy específicos. Contratos experimentales en redes de prueba donde no hay valor real en riesgo. Proyectos en fase extremadamente temprana donde la velocidad de iteración es crítica y la infraestructura de gobernanza aún no existe. Como paso transitorio explícitamente temporal en la ruta hacia descentralización, con compromiso público de migrar a modelos más robustos antes de manejar fondos significativos.

Una variante mejorada llamada [Ownable2Step](https://docs.openzeppelin.com/contracts/4.x/api/access#Ownable2Step) mitiga uno de los riesgos más embarazosos: transferir accidentalmente la propiedad a una dirección incorrecta. Este patrón requiere un proceso de dos pasos donde el propietario actual propone un nuevo propietario, y luego el nuevo propietario debe aceptar explícitamente desde su propia dirección. Esto previene errores fatales como enviar la propiedad a una dirección con un carácter incorrecto, o a un contrato que no puede ejecutar la función de aceptación, lo cual causaría pérdida permanente e irreversible de control sobre el protocolo.

## Wallets multi-firma como descentralización de control

Los sistemas multi-firma, conocidos como multisigs, resuelven el problema del punto único de fallo mediante un mecanismo conceptualmente simple pero profundamente efectivo: en lugar de una clave privada que controla el protocolo, requieren consenso de múltiples partes independientes. Un multisig configurado como 3-de-5 significa que cualquier transacción requiere aprobación de al menos tres de cinco claves autorizadas antes de ejecutarse.

Esta arquitectura distribuye poder y riesgo simultáneamente. Un atacante que compromete una de las cinco claves no gana nada, ya que no puede actuar unilateralmente. Incluso comprometer dos claves es insuficiente. Solo mediante coordinación de tres partes independientes puede ejecutarse cualquier acción crítica, haciendo que ataques exitosos requieran esfuerzos exponencialmente más sofisticados.

[Safe](https://safe.global/), anteriormente conocido como Gnosis Safe, se ha convertido en el estándar de la industria para multisigs en Ethereum y ecosistemas compatibles con EVM. No es simplemente una wallet multi-firma básica, sino infraestructura completa para gestión de activos descentralizada con capacidades extensibles. Puede configurar umbrales de firma arbitrarios, añadir módulos que implementan lógica personalizada como límites de gasto diarios o whitelists de contratos, agrupar múltiples operaciones en una sola transacción para eficiencia, y designar guardianes que pueden pausar operaciones peligrosas.

Los protocolos DeFi usan multisigs en múltiples niveles según criticidad de operaciones. Un protocolo típico podría tener un multisig 4-de-7 controlando ownership de contratos core con participación de fundadores, advisors y representantes comunitarios. Para operaciones rutinarias como ajustes menores de fees o actualizaciones de oráculos, un multisig 2-de-3 proporciona agilidad sin sacrificar completamente seguridad. Para capacidad de pausa de emergencia durante ataques activos, un multisig 3-de-5 de guardianes de seguridad permite respuesta rápida pero no unilateral.

Las DAOs típicamente custodian sus treasuries principales en Safe, configuran módulos que permiten ciertos gastos pre-aprobados sin coordinación multisig completa, e implementan límites de gasto donde operaciones menores de cierto umbral requieren menos firmas mientras que gastos mayores requieren consenso más amplio.

Sin embargo, los multisigs no son solución perfecta. Introducen coordinación off-chain donde las partes autorizadas deben comunicarse externamente para coordinar firmas, típicamente mediante plataformas de mensajería o herramientas específicas de gobernanza. La disponibilidad se convierte en riesgo: si suficientes signatarios pierden acceso a sus claves o simplemente desaparecen del proyecto, el multisig puede quedar permanentemente bloqueado sin capacidad de recuperación. La colusión permanece posible si el número mínimo de signatarios se coordinan maliciosamente. Y la complejidad de experiencia de usuario ralentiza decisiones urgentes donde cada operación requiere múltiples pasos de aprobación.

## MPC Wallets: criptografía distribuida avanzada

Multi-Party Computation (MPC) representa una evolución técnica significativa sobre multisigs tradicionales, usando criptografía avanzada para distribuir control de claves privadas sin que ninguna parte individual posea la clave completa en ningún momento. A diferencia de multisigs donde cada participante tiene su propia clave completa y las firmas se agregan on-chain, MPC divide la clave privada en fragmentos criptográficos distribuidos entre múltiples partes que colaboran para generar firmas válidas mediante protocolos criptográficos interactivos.

La diferencia arquitectural fundamental radica en dónde ocurre la computación. En multisigs tradicionales, cada signatario firma independientemente con su clave completa, y las múltiples firmas se combinan on-chain donde el smart contract verifica que se alcanzó el umbral requerido. Esto significa múltiples transacciones on-chain para cada operación, pagando gas por cada firma individual. En MPC wallets, los participantes ejecutan un protocolo criptográfico off-chain donde cada uno usa su fragmento de clave para contribuir a generar una única firma válida. Solo esa firma final se publica on-chain, indistinguible de una firma estándar generada por una clave privada única.

Esta indistinguibilidad on-chain proporciona ventajas importantes. Las MPC wallets son compatibles con cualquier blockchain sin requerir soporte específico de smart contracts para lógica multi-firma. Bitcoin, que tiene capacidades de scripting limitadas comparado con Ethereum, puede beneficiarse completamente de seguridad MPC sin modificaciones de protocolo. Los costos de gas son menores porque solo se publica una transacción en lugar de múltiples. Y la privacidad mejora porque observadores on-chain no pueden distinguir transacciones de wallet MPC de transacciones de wallet individual, ocultando el hecho de que múltiples partes controlan los fondos.

El proceso de threshold signature mediante MPC típicamente funciona así. Durante setup inicial, los participantes ejecutan un protocolo de Distributed Key Generation (DKG) donde generan colectivamente un par de claves pública-privada sin que la clave privada completa exista nunca en un solo lugar. Cada participante recibe un fragmento secreto de la clave privada. La clave pública se comparte abiertamente y se usa como dirección de la wallet. Cuando necesitan firmar una transacción, los participantes ejecutan un protocolo de threshold signing donde cada uno usa su fragmento secreto para computar una porción de la firma. Las porciones se combinan para formar una firma completa válida que cualquiera puede verificar contra la clave pública. Crucialmente, incluso durante el proceso de firma, la clave privada completa nunca se reconstruye, los participantes colaboran sin revelar sus fragmentos individuales.

Los esquemas más comunes incluyen threshold signatures basadas en ECDSA (el algoritmo de firma usado por Ethereum y Bitcoin), donde se requieren t-de-n participantes para generar firmas válidas, y Schnorr signatures que ofrecen agregación más eficiente y son nativamente soportadas en Bitcoin post-Taproot. Threshold BLS signatures permiten agregar firmas de múltiples grupos en una sola firma ultra-compacta, aunque aún no son ampliamente soportadas en blockchains principales.

Firmas como Fireblocks, Qredo, Sepior, y Unbound Security proveen soluciones MPC enterprise-grade para instituciones que custodian criptoactivos a escala masiva. Fireblocks, usada por exchanges, fondos de hedge crypto, y grandes tesorerías corporativas, combina MPC con enclaves seguros de hardware para prevenir que fragmentos de clave sean extraídos incluso si servidores son comprometidos. Qredo implementa MPC Layer 2 donde las computaciones de firma ocurren en red distribuida descentralizada en lugar de servidores controlados por la empresa, aumentando resistencia a censura. ZenGo ofrece MPC wallet consumer-friendly donde un fragmento reside en el teléfono del usuario y otro fragmento en servidores de ZenGo, eliminando seed phrases completamente mientras mantiene seguridad de que la empresa no puede unilateralmente mover fondos.

La comparación directa con multisigs tradicionales revela trade-offs específicos. MPC wallets proporcionan mejor privacidad porque estructuras de control no son públicamente visibles on-chain, eficiencia de gas porque solo requieren una firma on-chain por transacción, y compatibilidad universal con blockchains legacy que no soportan smart contracts complejos. Sin embargo, requieren complejidad criptográfica sustancialmente mayor, con protocolos interactivos que demandan comunicación en tiempo real entre participantes durante proceso de firma, introduciendo latencia y requisitos de disponibilidad simultánea. Los multisigs son conceptualmente más simples, auditables mediante inspección de smart contract en blockchain, y no requieren que participantes estén online simultáneamente, cada uno puede firmar asincrónicamente cuando le convenga.

Para protocolos DeFi, la elección típicamente depende de requisitos específicos. Treasuries que necesitan máxima transparencia y auditabilidad pública prefieren multisigs on-chain donde toda la lógica de permisos es verificable públicamente. Instituciones que custodian activos de clientes y priorizan privacidad operacional y costos de transacción usan MPC. Protocolos híbridos están emergiendo donde control de alto nivel usa multisig transparente pero operaciones frecuentes de bajo valor usan MPC para eficiencia.

Los riesgos específicos de MPC incluyen dependencia crítica de implementación correcta de protocolos criptográficos complejos donde bugs sutiles pueden comprometer seguridad completamente. El protocolo TSS (Threshold Signature Scheme) de Fireblocks fue auditado múltiples veces pero aún reveló vulnerabilidades en versiones tempranas. La centralización de proveedores MPC comerciales introduce riesgo de vendor lock-in y dependencia de disponibilidad del servicio. Y la complejidad de debugging cuando algo falla es sustancialmente mayor que con multisigs donde el flujo de transacciones es transparente on-chain.

La frontera tecnológica incluye MPC con refresh periódico de fragmentos de clave, donde participantes rotan sus secretos sin cambiar la clave pública, mitigando el riesgo de que fragmentos comprometidos lentamente acumulen hasta alcanzar el umbral. Protocolos de MPC que soportan key resharing dinámico permiten añadir o remover participantes sin regenerar claves completamente. Y la integración de MPC con Trusted Execution Environments (TEEs) como Intel SGX proporciona garantías de hardware de que computaciones ocurren correctamente incluso en infraestructura potencialmente comprometida.

## Delays temporales para transparencia y respuesta

Los timelocks introducen un delay obligatorio entre la aprobación de una acción administrativa y su ejecución efectiva. Este mecanismo aparentemente simple proporciona una propiedad de seguridad crítica: visibilidad pública de intenciones antes de que se materialicen. Cuando un protocolo programa cambiar un parámetro económico crítico, ese cambio no se ejecuta instantáneamente sino que entra en una cola visible públicamente con un timestamp de ejecución mínima, típicamente entre 24 horas y dos semanas dependiendo de la criticidad.

Este delay da tiempo a la comunidad para revisar cambios propuestos, analizar si representan riesgos o comportamiento malicioso, y reaccionar apropiadamente antes de que se ejecuten. Si un multisig comprometido o un desarrollador deshonesto intenta drenar fondos mediante cambio de parámetros, los usuarios tienen ventana de oportunidad para retirar sus activos antes de que el ataque se materialice. La comunidad puede organizarse para votar cancelación de la propuesta, bifurcar el protocolo o al menos alertar a otros participantes del riesgo inminente.

El [TimelockController](https://docs.openzeppelin.com/contracts/4.x/api/governance#TimelockController) de OpenZeppelin es la implementación estándar en Ethereum. El flujo operativo tiene tres fases distintas. Primero, una dirección autorizada llamada proposer programa una operación específica, por ejemplo actualizar un parámetro económico o cambiar una dirección de contrato dependiente. La operación entra en cola con un timestamp que indica la primera vez que podrá ejecutarse. Después de que transcurre el delay mínimo, otra dirección autorizada llamada executor puede ejecutar la operación, materializando el cambio. Opcionalmente, un rol de canceller puede cancelar operaciones pendientes si la comunidad detecta problemas antes de la ejecución.

El caso de Compound Finance en 2021 ilustra vívidamente por qué importan los timelocks. El protocolo desplegó una actualización con un bug que por error distribuyó 80 millones de dólares en tokens COMP extra a usuarios. Si hubieran tenido un timelock robusto con suficiente delay, la comunidad habría detectado el error en el código durante la revisión pública antes de que se ejecutara, evitando completamente el incidente.

Inversamente, protocolos sin timelocks han sufrido rug pulls donde developers cambiaron parámetros críticos instantáneamente, configuraron fees al cien por ciento o pausaron retiros, drenando fondos antes de que nadie pudiera reaccionar. La ausencia de delay equivale a confianza ciega en que quienes controlan el protocolo nunca abusarán de ese poder.

La duración del delay típicamente se calibra según criticidad del cambio y volatilidad del mercado. Cambios de parámetros menores como ajustes de fees dentro de rangos predefinidos podrían requerir 24 a 48 horas. Upgrades significativos de contratos que cambian lógica core típicamente requieren 7 a 14 días. Cambios en sistemas de gobernanza que modifican quién puede hacer qué podrían requerir 14 a 30 días. La capacidad de pausa de emergencia durante ataques activos generalmente no tiene delay, siendo ejecutable inmediatamente por guardianes designados, aceptando el riesgo de abuso a cambio de capacidad de respuesta rápida ante amenazas reales.

Delays largos aumentan seguridad pero reducen agilidad. En mercados cripto extremadamente volátiles donde condiciones pueden cambiar radicalmente en horas, no poder ajustar parámetros rápidamente puede ser fatal para la competitividad del protocolo. Por eso muchos implementan timelocks escalonados donde operaciones rutinarias requieren delays cortos, cambios significativos requieren delays medios, cambios críticos requieren delays largos, pero capacidades de emergencia permanecen disponibles inmediatamente para guardianes de confianza.

## Listas de control de acceso granular

Mientras el control basado en roles asigna capacidades amplias donde un rol puede ejecutar funciones completas sin restricciones adicionales, las listas de control de acceso permiten permisos ultra-granulares con condiciones específicas. En lugar de simplemente preguntar si una dirección tiene un rol, estos sistemas preguntan si esa dirección puede ejecutar una función específica en un contrato particular con parámetros dentro de rangos definidos.

[Aragon](https://aragon.org/) implementa uno de los sistemas de listas de control de acceso más sofisticados del ecosistema. Permite definir permisos con condiciones arbitrariamente complejas. Por ejemplo, un rol de tesorero podría transferir hasta 100 ETH del vault sin requerir aprobación adicional, pero transferencias mayores automáticamente escalan a votación completa de la DAO. Un rol de gestor de parámetros podría ajustar fees del protocolo entre 0.1% y 2%, pero cualquier valor fuera de ese rango requiere consenso de la organización. Un rol de guardián podría pausar el protocolo unilateralmente ante amenaza inminente, pero solo puede reactivarlo mediante votación comunitaria.

Este enfoque de permisos condicionales permite crear lo que podríamos llamar governance programática, donde el contrato mismo aplica reglas de negocio complejas sin intervención humana constante. Los parámetros pueden incluir lógica temporal como permitir ciertas operaciones solo durante horarios específicos, o condiciones económicas como permitir acciones solo si ciertos indicadores on-chain están dentro de rangos aceptables, o requisitos temporales como imponer delays mínimos entre operaciones similares consecutivas.

Esta granularidad resuelve uno de los problemas más espinosos de la governance descentralizada: balancear eficiencia operativa con control democrático. Operaciones verdaderamente rutinarias y de bajo riesgo pueden delegarse a roles especializados con límites claramente definidos, permitiendo que el protocolo funcione ágilmente sin requerir votaciones para cada decisión trivial. Simultáneamente, cualquier acción que exceda los parámetros predefinidos automáticamente requiere consenso más amplio, previniendo que poder delegado sea abusado para cambios fundamentales.

El costo de esta sofisticación es complejidad tanto en implementación como en comprensión. Sistemas de permisos demasiado elaborados pueden volverse opacos donde incluso participantes bien intencionados no entienden completamente quién puede hacer qué bajo qué circunstancias, creando riesgos de configuraciones incorrectas o vulnerabilidades inadvertidas.

## Delegación temporal y permisos programáticos

Más allá de asignar roles permanentes que persisten hasta ser revocados explícitamente, algunos protocolos necesitan permisos temporales, delegables o condicionales que se ajustan dinámicamente según contexto.

El estándar [EIP-2612](https://eips.ethereum.org/EIPS/eip-2612), conocido como Permit, permite que usuarios autoricen a otros contratos para gastar sus tokens mediante firmas off-chain en lugar de transacciones on-chain. Tradicionalmente, cuando querías usar tus tokens en un protocolo DeFi, primero debías ejecutar una transacción de aprobación pagando gas, y solo entonces podías ejecutar la transacción real. Permit elimina ese primer paso permitiendo que firmes un mensaje criptográfico off-chain autorizando el gasto, y el protocolo usa esa firma para ejecutar ambas operaciones en una sola transacción. Esto mejora experiencia de usuario reduciendo friccón y costos, mientras habilita meta-transactions donde terceros pueden pagar el gas en nombre del usuario.

[ERC-4337](https://eips.ethereum.org/EIPS/eip-4337) (Account Abstraction) permite wallets con lógica de autorización arbitrariamente compleja: multi-firma nativa, límites de gasto por categoría, whitelists/blacklists, recuperación social, delegación de gas. Ver [Experiencia de usuario](9-1-user-experience.md) para arquitectura completa.

Un ejemplo concreto ilustra el poder de esta flexibilidad: una wallet podría configurarse para que cualquier transacción con protocolos DeFi requiera confirmación biométrica adicional para proteger contra malware que intenta iniciar transacciones maliciosas, pero transferencias menores de cierto umbral a direcciones previamente usadas se aprueban automáticamente para conveniencia, mientras que transferencias a direcciones completamente nuevas requieren delay de 24 horas para prevenir estafas de ingeniería social.

Algunos protocolos están experimentando con capability-based security donde permisos se representan como tokens transferibles. Poseer un NFT específico llamado Admin Badge podría otorgar derechos administrativos transferibles, permitiendo mercados de permisos donde quien ya no quiere responsabilidades administrativas puede vender el badge a quien desee asumirlas. Staking tokens del protocolo podría otorgar poder de votación proporcional que existe solo mientras mantienes el stake. Completar logros on-chain verificables podría otorgar credentials que desbloquean funcionalidades o acceso a comunidades exclusivas.

## Control de acceso off-chain mediante ownership on-chain

El control de acceso no se limita a smart contracts que ejecutan lógica on-chain. Las comunidades Web3 están usando ownership verificable de tokens y NFTs para gestionar permisos en plataformas off-chain, creando puentes entre identidad descentralizada y acceso a recursos tradicionales.

Servicios como [Collab.Land](https://collab.land/) y [Guild.xyz](https://guild.xyz/) integran plataformas de comunicación como Discord y Telegram con verificación blockchain. La lógica es directa: si posees cierta cantidad de tokens del proyecto o un NFT de una colección específica, automáticamente recibes roles correspondientes en el servidor de Discord. Poseer 100 o más tokens otorga rol de Holder con acceso a canales de discusión exclusivos. Poseer un NFT de la colección oficial otorga acceso a espacios donde el equipo comparte updates tempranos. Staking en el protocolo otorga rol de Contributor con permisos para participar en decisiones de governance.

Este modelo alinea incentivos de forma elegante. Quienes tienen skin in the game porque poseen tokens del proyecto participan en decisiones estratégicas y tienen acceso a información privilegiada. Quienes solo observan desde afuera sin compromiso económico tienen acceso limitado. El ownership on-chain actúa como proof of stake inmediatamente verificable que no puede falsificarse ni manipularse mediante ingeniería social.

[Snapshot](https://snapshot.org/) lleva esta idea más lejos permitiendo que DAOs conduzcan votaciones off-chain con pesos basados en ownership on-chain. El proceso elimina costos de gas mientras mantiene verificabilidad criptográfica. La DAO configura una estrategia de votación, típicamente algo como un token equivale a un voto, opcionalmente con pesos cuadráticos u otras fórmulas más sofisticadas. Los miembros firman sus votos off-chain usando sus wallets, sin pagar gas. El resultado se calcula verificando balances on-chain en un snapshot específico del estado de blockchain, típicamente el bloque cuando comenzó la votación para prevenir manipulación mediante compra de tokens después de ver resultados preliminares. Si la propuesta pasa, un multisig o contrato on-chain ejecuta la decisión de forma vinculante.

Esta arquitectura híbrida combina eficiencia de coordinación off-chain con seguridad de verificación on-chain. Las votaciones no cuestan gas a participantes, eliminando fricción que históricamente reducía participación especialmente de holders pequeños. Pero el resultado es igualmente legítimo porque cualquiera puede verificar independientemente que los votos corresponden a ownership real verificable criptográficamente. Para más contexto sobre cómo funcionan los sistemas de identidad y reputación que sustentan estos mecanismos, consulta [Identidad Web3](7-1-identity.md) y [Reputación Web3](7-2-reputation.md).

## Gestión de permisos en wallets: la responsabilidad del usuario

Mientras las secciones anteriores se enfocaron en cómo protocolos diseñan control de acceso a nivel de smart contract, existe un vector de ataque crítico que depende completamente del comportamiento del usuario final: las aprobaciones de tokens que wallets otorgan a contratos.

Cuando interactúas con un protocolo DeFi que necesita mover tus tokens, por ejemplo para depositar en un pool de liquidez o intercambiar mediante un DEX, primero debes aprobar que el contrato pueda gastar esos tokens en tu nombre. Esta aprobación es técnicamente una llamada a la función `approve()` del contrato del token, autorizando a la dirección del protocolo para transferir hasta cierta cantidad desde tu wallet.

El problema crítico es que muchos protocolos solicitan aprobaciones ilimitadas por conveniencia, y la mayoría de usuarios aprueban sin entender las implicaciones. Cuando MetaMask u otra wallet muestra "Aprobar acceso a tus USDC", frecuentemente el monto es el máximo valor posible en uint256, efectivamente infinito. Esto significa que el contrato puede drenar todos tus tokens en cualquier momento futuro, no solo la cantidad que necesitas para la transacción actual.

Los ataques de drainer explotan sistemáticamente este vector. Un sitio web malicioso que parece legítimo solicita aprobación para "verificar tu wallet" o "preparar transacción". El usuario firma la aprobación pensando que es inofensiva. El atacante ahora tiene permiso permanente para transferir todos los tokens aprobados desde esa wallet. Días o semanas después, cuando el usuario ya olvidó el incidente, el atacante drena los fondos. Para el momento en que el usuario nota las transferencias no autorizadas, es demasiado tarde: la aprobación era legítima desde la perspectiva de blockchain, y la transferencia posterior simplemente ejerció ese permiso.

La higiene de permisos en wallets requiere disciplina continua:

**Aprobar solo montos mínimos necesarios**: Cuando un protocolo solicita aprobación, edita manualmente el monto para que sea solo lo que necesitas para la transacción actual, no ilimitado. Si vas a intercambiar 100 USDC, aprueba 100 USDC, no infinito. Esto requiere un clic adicional pero elimina riesgo de drenaje futuro.

**Revocar aprobaciones después de usar protocolos**: Servicios como [revoke.cash](https://revoke.cash/) y [etherscan.io/tokenapprovalchecker](https://etherscan.io/tokenapprovalchecker) permiten visualizar todas las aprobaciones activas desde tu wallet y revocarlas selectivamente. Después de terminar de usar un protocolo, especialmente uno con el que no interactúas frecuentemente, revoca las aprobaciones. Esto cuesta gas pero previene que contratos retengan permisos indefinidamente.

**No dejar aprobaciones activas a protocolos abandonados**: Si un protocolo deja de desarrollarse activamente o muestra señales de problemas de seguridad, revoca inmediatamente todas las aprobaciones. Un contrato que hoy es seguro puede ser explotado mañana, y si mantiene aprobaciones de tu wallet, el exploit podría drenar tus fondos incluso si no estabas usando el protocolo activamente cuando ocurrió el compromiso.

**Auditar aprobaciones regularmente**: Establece un hábito mensual o trimestral de revisar todas las aprobaciones activas desde tus wallets principales. La mayoría serán de protocolos que usaste una vez y olvidaste. Revocar sistemáticamente aprobaciones no utilizadas reduce dramáticamente superficie de ataque.

**Usar wallets separadas para actividades de riesgo diferente**: Una wallet "caliente" para interactuar con protocolos nuevos o experimentales, con cantidad limitada de fondos. Una wallet "fría" para holdings principales que solo aprueba contratos extremadamente establecidos y auditados. Una wallet específica para NFTs. Esta compartimentalización limita daño potencial si una wallet se compromete o aprueba contrato malicioso.

**Entender qué estás firmando**: Las wallets modernas están mejorando visualización de transacciones, pero aún es fácil firmar algo sin entender completamente las consecuencias. Si una transacción solicita aprobación y no entiendes por qué el protocolo la necesita, investiga antes de aprobar. Un minuto de verificación puede prevenir pérdida total de fondos.

La realidad dolorosa es que la responsabilidad de gestión de permisos recae desproporcionadamente en usuarios que frecuentemente carecen de conocimiento técnico para evaluar riesgos correctamente. El ecosistema está evolucionando hacia mejores defaults como aprobaciones con límites temporales o montos máximos más razonables, pero mientras tanto, la educación de usuarios sobre higiene de permisos es tan crítica como el diseño correcto de control de acceso en protocolos.

## Principios de seguridad y diseño robusto

La arquitectura de control de acceso exitosa en Web3 emerge de principios fundamentales que los protocolos maduros han destilado mediante experiencia dolorosa con exploits y governance fallida.

**Separación de poderes**:

Nunca concentres capacidades heterogéneas en un único rol. Los sistemas robustos separan claramente quién decide cambios de quién ejecuta esas decisiones y quién puede intervenir en emergencias. Governance representa quién toma decisiones estratégicas, típicamente la DAO o un multisig representativo de stakeholders. Execution representa quién materializa decisiones aprobadas, frecuentemente un timelock o un rol de executor que simplemente implementa lo que governance decidió. Guardianship representa quién puede pausar el protocolo durante ataques activos, usualmente un multisig pequeño de expertos en seguridad que pueden responder rápidamente. Operations representa quién gestiona tareas rutinarias de bajo riesgo como actualizar feeds de oráculos o ajustar parámetros menores dentro de rangos predefinidos.

Esta separación crea checks and balances donde comprometer cualquier actor individual no otorga control completo del protocolo. Un atacante que captura governance no puede ejecutar cambios instantáneamente si existe timelock. Un guardian corrupto puede pausar temporalmente pero no puede modificar lógica fundamental. Un operator comprometido solo puede causar daño limitado dentro de sus parámetros restringidos.

**Principio de mínimo privilegio**:

Cada rol debe poseer exactamente los permisos necesarios para cumplir su función, absolutamente nada más. Si un rol solo necesita capacidad de pausar el protocolo durante emergencias, no debe tener simultáneamente capacidad de cambiar parámetros económicos o transferir fondos. Esta restricción minimiza superficie de ataque y contiene daño potencial si el rol se compromete.

**Descentralización progresiva**:

Los proyectos raramente nacen completamente descentralizados. La trayectoria típica es evolutiva, comenzando con control centralizado para velocidad de iteración y gradualmente delegando poder conforme el protocolo madura y la comunidad se desarrolla. La fase inicial frecuentemente usa propiedad única donde fundadores tienen control completo, permitiendo iteración rápida sin fricción de coordinación. La segunda fase transfiere ownership a un multisig con participación de fundadores más advisors de confianza. La tercera fase añade timelocks para cambios críticos, dando transparencia pública de intenciones. La cuarta fase delega roles específicos a gobernanza on-chain donde la comunidad vota decisiones. La fase final transfiere ownership definitivo a la DAO con timelocks largos más multisigs de emergencia, minimizando pero no eliminando completamente capacidad de intervención humana.

**Inmutabilidad selectiva**:

Ciertos parámetros fundamentales deben ser completamente inmutables desde deployment inicial, codificados como constantes que ni siquiera roles administrativos pueden modificar. Fees máximos deben tener hard caps codificados para prevenir extracción predatoria donde governance capturada aumenta fees arbitrariamente. Direcciones de contratos core que el protocolo llama deben ser inmutables o solo modificables mediante proceso de governance extremadamente riguroso, previniendo redirección maliciosa de flujos de fondos. Supply caps de tokens deben estar grabados permanentemente donde aplicable, garantizando que nadie puede inflar arbitrariamente el suministro.

Si algo genuinamente no debería cambiar nunca bajo ninguna circunstancia, eliminando esa capacidad del código eliminas completamente ese vector de ataque. No existe riesgo de abuso de poder que no puede existir.

**Auditoría mediante eventos**:

Cada cambio de permisos, cada asignación o revocación de rol, cada transferencia de ownership debe emitir eventos on-chain que quedan permanentemente registrados en la blockchain. Estos eventos permiten que herramientas de monitoreo como [Tenderly](https://tenderly.co/) o [OpenZeppelin Defender](https://www.openzeppelin.com/defender) detecten cambios sospechosos en tiempo real y alerten a la comunidad inmediatamente, permitiendo respuesta rápida ante compromisos. Los eventos también proporcionan transparencia histórica completa donde cualquiera puede auditar la evolución completa del control del protocolo desde su deployment.

## Lecciones de exploits históricos

Los mayores desastres en la historia de Web3 proporcionan lecciones dolorosamente claras sobre qué falla cuando el control de acceso es inadecuado.

**The DAO en 2016**:

El infame hack que resultó en la pérdida de 50 millones de dólares y eventualmente llevó al controversial fork de Ethereum no fue primariamente un ataque de reentrancia, aunque ese fue el mecanismo técnico. El problema fundamental era ausencia de mecanismos de pausa de emergencia. Si The DAO hubiera implementado un rol de guardian con capacidad de pausar transferencias durante ataques activos, el daño habría sido dramáticamente limitado. La comunidad detectó el ataque mientras estaba en progreso pero no tenía herramientas para detenerlo.

**Ronin Bridge en 2022**:

El protocolo requería 5 de 9 firmas para autorizar transferencias de fondos, una configuración multisig aparentemente robusta. Atacantes lograron comprometer cinco claves mediante combinación sofisticada de ingeniería social y spear phishing dirigido a validadores individuales. La lección crítica es que multisigs no proporcionan seguridad si las claves se almacenan inseguramente. La solución combina multisigs con hardware wallets para cada signatario, distribución geográfica amplia de participantes para reducir probabilidad de compromiso simultáneo, y timelocks que dan tiempo para detectar compromiso antes de ejecución.

**Poly Network en 2021**:

El contrato contenía una función privilegiada que permitía cambiar ownership, pero la verificación de permisos estaba implementada incorrectamente, permitiendo que cualquiera la llamara. El atacante simplemente ejecutó la función y se convirtió en propietario, drenando 611 millones de dólares. La lección es auditar exhaustivamente que modificadores de control de acceso están presentes en absolutamente todas las funciones críticas, sin excepciones. Un solo olvido crea vulnerabilidad catastrófica.

**Compound COMP distribution bug en 2021**:

El deployment de una nueva versión del protocolo contenía un bug que distribuía tokens COMP extra por valor de 80 millones de dólares. Si hubiera existido un timelock de 48 horas entre aprobación y ejecución del upgrade, la comunidad habría revisado el código, detectado el error mediante simulación y pruebas, y cancelado el deployment antes de que se materializara el daño. La ausencia de delay transformó un bug detectable en pérdida irreversible.

## Herramientas del ecosistema

El ecosistema ha desarrollado infraestructura especializada para implementar y monitorear control de acceso robusto.

Las librerías estándar proporcionan componentes probados en batalla. [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts/) ofrece implementaciones auditadas de AccessControl para sistemas basados en roles, Ownable para propiedad simple y TimelockController para delays obligatorios. [Safe contracts](https://github.com/safe-global/safe-contracts) proporciona la infraestructura multisig más ampliamente usada y confiable del ecosistema. [Aragon](https://aragon.org/) ofrece un framework completo de governance y listas de control de acceso para DAOs.

Las herramientas de auditoría y monitoreo permiten detectar problemas antes de que se conviertan en exploits. [Tenderly](https://tenderly.co/) proporciona monitoreo en tiempo real de eventos de cambios de roles, simulación de transacciones para probar cambios antes de ejecutarlos en mainnet, y alertas automatizadas cuando ocurren operaciones sospechosas. [OpenZeppelin Defender](https://www.openzeppelin.com/defender) automatiza monitoreo continuo de permisos y puede ejecutar respuestas programadas ante cambios detectados. [Forta](https://forta.org/) implementa un sistema de detección descentralizado que alerta sobre cambios sospechosos en ownership o roles mediante análisis de patrones on-chain.

Los frameworks de testing como [Hardhat](https://hardhat.org/) y [Foundry](https://getfoundry.sh/) permiten testing exhaustivo de lógica de permisos, simulando escenarios donde atacantes intentan ejecutar funciones sin autorización apropiada. [Slither](https://github.com/crytic/slither) realiza análisis estático del código de contratos para detectar automáticamente problemas comunes de control de acceso como funciones críticas sin modificadores de permiso o jerarquías de roles mal configuradas.

## Seguridad como proceso continuo

El control de acceso en Web3 no es un estado que alcanzas mediante deployment correcto y luego olvidas, sino un proceso continuo de evaluación, mejora y adaptación conforme el protocolo evoluciona y nuevas amenazas emergen.

Los protocolos exitosos siguen patrones reconocibles en su evolución. Comienzan simples, frecuentemente con propiedad única durante desarrollo inicial, y evolucionan progresivamente hacia descentralización conforme maduran. Separan roles siguiendo el principio de mínimo privilegio donde cada función tiene exactamente los permisos necesarios y nada más. Combinan múltiples capas defensivas en lugar de depender de un único mecanismo, integrando multisigs con timelocks con guardianes de emergencia con parámetros fundamentales inmutables. Monitorizan cambios de permisos en tiempo real mediante herramientas automatizadas que alertan inmediatamente ante actividad sospechosa. Auditan código y procesos operativos exhaustivamente antes de manejar valor significativo, reconociendo que el costo de auditoría profesional es trivial comparado con el costo de un exploit exitoso.

Crucialmente, aprenden de exploits históricos tanto propios como ajenos. La comunidad Web3 tiene memoria colectiva de desastres pasados, y los mejores protocolos estudian sistemáticamente qué falló en otros proyectos para no repetir los mismos errores. El ecosistema está madurando mediante esta acumulación de conocimiento doloroso.

La realidad fundamental es que en Web3, el código es ley. Si tu contrato tiene un bug en el control de acceso, no existe customer support que pueda revertir transacciones maliciosas. No hay autoridad central que pueda intervenir para recuperar fondos robados. No hay sistema legal tradicional que pueda forzar cumplimiento contra atacantes pseudónimos operando globalmente. La única defensa verdadera es diseño cuidadoso informado por principios de seguridad sólidos, implementación correcta siguiendo estándares probados, testing exhaustivo que simula escenarios adversarios, y auditoría profesional por expertos independientes.

Los mejores protocolos no nacen perfectamente descentralizados desde el primer día. Eso sería optimismo ingenuo que ignora realidades de desarrollo de software complejo. En cambio, transicionan gradualmente desde control centralizado que permite velocidad de iteración durante fases tempranas hacia governance descentralizada que proporciona seguridad y legitimidad conforme el protocolo maneja más valor y sirve más usuarios. El arte del diseño de control de acceso está en balancear estos trade-offs según la etapa específica de madurez del proyecto, reconociendo que lo óptimo para un experimento en testnet es fundamentalmente diferente de lo óptimo para un protocolo que custodia miles de millones de dólares.

## El futuro del control de acceso en Web3

La evolución del control de acceso en Web3 está siendo impulsada por tecnologías emergentes que prometen resolver limitaciones fundamentales de arquitecturas actuales mientras introducen capacidades completamente nuevas.

**Account Abstraction (ERC-4337)** representa quizás el cambio más fundamental en cómo funcionan las cuentas en Ethereum. Tradicionalmente, existen dos tipos de cuentas: Externally Owned Accounts (EOAs) controladas por claves privadas donde firmar una transacción requiere posesión de esa clave única, y Contract Accounts con lógica programable pero que no pueden iniciar transacciones por sí mismas. Esta distinción limita severamente qué tipos de control de acceso pueden implementarse a nivel de wallet.

Account Abstraction elimina esta distinción permitiendo que las wallets de los usuarios sean smart contracts con lógica de autorización arbitrariamente compleja. Una wallet podría requerir múltiples firmas de diferentes dispositivos que el usuario controla, implementando multisig personal sin necesidad de protocolo externo. Podría imponer límites de gasto diarios donde transferencias menores se aprueban automáticamente pero transferencias grandes requieren confirmación adicional mediante segundo factor. Podría implementar whitelists de contratos permitidos o blacklists de direcciones conocidas como maliciosas, rechazando automáticamente interacciones peligrosas antes de que el usuario siquiera vea la solicitud.

La capacidad de pagar gas en tokens distintos de ETH o delegar pago de gas a terceros (meta-transactions) se vuelve nativa. Esto elimina fricción donde usuarios necesitan mantener ETH específicamente para gas, permitiendo que onboarding de nuevos usuarios sea más fluido. Los protocolos pueden subsidiar gas para sus usuarios sin arquitecturas complejas de relayers.

**Passkeys y WebAuthn: autenticación biométrica nativa**:

Los Passkeys representan la convergencia de estándares de autenticación web (WebAuthn/FIDO2) con blockchain, habilitando control de wallets mediante autenticación biométrica de dispositivos sin necesidad de gestionar seed phrases. Esta tecnología elimina uno de los mayores obstáculos de adopción mainstream: la responsabilidad aterradora de custodiar correctamente 12 o 24 palabras cuya pérdida significa pérdida permanente de fondos.

WebAuthn (Web Authentication) es un estándar W3C que permite sitios web usar autenticadores fuertes como biometría (Face ID, Touch ID, Windows Hello) o hardware security keys (YubiKey) en lugar de contraseñas. FIDO2 es el conjunto completo de estándares que incluye WebAuthn para la parte web y CTAP (Client to Authenticator Protocol) para comunicación entre dispositivo y autenticador. Cuando creas un passkey para un sitio, tu dispositivo genera un par de claves público-privada específico para ese sitio. La clave privada se almacena seguramente en el hardware del dispositivo, protegida por el secure enclave (iPhone/Mac) o TPM (Windows/Android), accesible solo mediante tu biometría. La clave pública se registra con el sitio.

Para autenticarte posteriormente, el sitio envía un challenge. Tu dispositivo usa tu biometría para desbloquear la clave privada, firma el challenge, y envía la firma. El sitio verifica la firma contra la clave pública almacenada. En ningún momento la clave privada sale del dispositivo ni necesitas recordar contraseñas o seed phrases.

La integración con blockchain tradicionalmente ha sido problemática porque passkeys usan el algoritmo de firma secp256r1 (también conocido como P-256), mientras que Ethereum y la mayoría de blockchains usan secp256k1. Verificar firmas secp256r1 en smart contracts era extremadamente costoso en gas, haciendo que passkeys fueran impracticales para control de wallets on-chain.

EIP-7212 resuelve este problema introduciendo un precompile nativo para verificación de firmas secp256r1. Un precompile es una función implementada directamente en el código del cliente de Ethereum a nivel de protocolo, ejecutándose con eficiencia de código nativo en lugar de bytecode de EVM. Con EIP-7212, verificar firmas de passkeys cuesta aproximadamente lo mismo que verificar firmas secp256k1 estándar, haciendo viable su uso en producción.

La arquitectura práctica combina Account Abstraction con passkeys. Tu wallet es un smart contract que verifica firmas secp256r1. Tu teléfono o laptop almacena la clave privada en su secure enclave. Cuando quieres firmar una transacción, usas Face ID o Touch ID para autorizar, tu dispositivo genera la firma secp256r1, y el smart contract de tu wallet la verifica mediante el precompile EIP-7212 antes de ejecutar la transacción. Desde tu perspectiva, la experiencia es idéntica a desbloquear tu teléfono o laptop, sin interacción con seed phrases, extensiones de navegador complejas, o conceptos criptográficos explícitos.

Proyectos como Coinbase Smart Wallet, Privy, y Turnkey están implementando esta stack completa. Coinbase Smart Wallet permite crear wallets usando Face ID sin tocar seed phrases. Privy ofrece SDK para developers que quieren integrar autenticación con passkeys en sus dApps. Turnkey proporciona infraestructura de custodia donde las claves están protegidas por passkeys y políticas programáticas sin que Turnkey pueda mover fondos unilateralmente.

Los beneficios para adopción mainstream son sustanciales. La eliminación de seed phrases reduce dramáticamente la barrera de entrada técnica y psicológica. Usuarios que nunca podrían gestionar seguramente 24 palabras pueden usar la misma biometría que ya usan para desbloquear su teléfono. El riesgo de phishing donde usuarios revelan accidentalmente seed phrases desaparece porque no existen credenciales portables que revelar. Las claves privadas nunca salen del secure enclave del hardware, proporcionando garantías de seguridad físicas imposibles con software puro.

Los trade-offs incluyen dependencia de hardware específico, si pierdes tu único dispositivo con la clave y no configuraste recovery, pierdes acceso. Por eso las implementaciones maduras combinan passkeys con social recovery o múltiples dispositivos registrados. La centralización de ecosistemas de plataforma como Apple y Google introduce riesgos sistémicos, aunque las especificaciones FIDO2 son estándares abiertos que previenen lock-in completo. Y la privacidad puede verse comprometida si proveedores de servicios correlacionan passkeys entre sitios, aunque el diseño del estándar usa claves específicas por sitio para prevenir esto.

La combinación de EIP-7212 + Account Abstraction + Passkeys representa probablemente el stack de autenticación del futuro para Web3 mainstream. Permite que personas normales usen criptomonedas con la misma facilidad que apps Web2 mientras mantienen autocustodia real de sus activos, sin comprometer seguridad mediante custodios centralizados. Los early adopters actuales que dominan gestión de seed phrases pueden parecer esto innecesario, pero para los próximos mil millones de usuarios, esta UX es requisito no negociable para adopción.

Para arquitectura completa de Account Abstraction y su impacto en experiencia de usuario, consulta [Experiencia de usuario](9-1-user-experience.md).

**Social Recovery** aborda uno de los problemas más agudos de Web3: la irreversibilidad de pérdida de claves privadas. Si pierdes tu clave privada en sistemas tradicionales, pierdes acceso permanentemente a todo lo que esa wallet controlaba. No existe proceso de recuperación mediante verificación de identidad o reseteo de contraseña.

Los sistemas de social recovery permiten designar un conjunto de guardianes de confianza, típicamente amigos, familiares o instituciones, que colectivamente pueden ayudarte a recuperar acceso si pierdes tu clave privada. La wallet requiere consenso de mayoría de guardianes para cambiar la clave de control. Si pierdes tu dispositivo, contactas a tus guardianes, cada uno firma una transacción de recuperación, y cuando suficientes han firmado, tu wallet actualiza su clave a una nueva que tú controlas.

Esto preserva descentralización porque tú eliges a tus guardianes, no hay autoridad central que puede recuperar cuentas unilateralmente. Pero proporciona fallback pragmático contra pérdida de acceso que hace Web3 más usable para personas normales que no son expertos en seguridad operacional.

[Argent](https://www.argent.xyz/) fue pionero en implementar social recovery en producción, demostrando que el modelo puede funcionar para usuarios mainstream. El desafío es educación: usuarios necesitan entender que elegir guardianes es decisión de seguridad crítica, no pueden ser personas que podrían coluden maliciosamente o ser fácilmente comprometidas mediante ingeniería social.

**Zero-Knowledge Proofs** están abriendo posibilidades completamente nuevas para control de acceso que preserva privacidad. Tradicionalmente, demostrar que tienes permiso para ejecutar una acción requiere revelar tu identidad o credentials. Con ZK-proofs, puedes demostrar que satisfaces requisitos de acceso sin revelar información específica sobre quién eres.

Un protocolo podría requerir que usuarios demuestren que poseen al menos 10,000 tokens del proyecto para acceder a funcionalidad premium, pero sin revelar exactamente cuántos tokens poseen ni desde qué dirección. Esto previene targeting de holders grandes por atacantes mientras mantiene control de acceso basado en stake. Sistemas de votación podrían verificar que cada voto proviene de holder legítimo sin vincular públicamente votos específicos a direcciones específicas, preservando privacidad de votación mientras previene double-voting.

La integración de identidad descentralizada con ZK-proofs permitiría escenarios donde demuestras que pasaste KYC con una institución acreditada sin revelar a qué institución ni qué información específica proporcionaste, solo que cumples requisitos regulatorios. Esto balancea compliance con privacidad de formas que sistemas tradicionales no pueden.

**AI-Assisted Governance** está emergiendo como herramienta para analizar complejidad creciente de propuestas de governance. Cuando DAOs gestionan protocolos con miles de millones de dólares y propuestas involucran cambios de código complejos que requieren expertise técnica profunda, la mayoría de holders no pueden evaluar riesgos realísticamente.

Sistemas de IA pueden analizar código de propuestas automáticamente, comparar contra patrones conocidos de vulnerabilidades, simular efectos económicos de cambios de parámetros, identificar inconsistencias entre descripción de propuesta y código real, y generar reportes comprensibles para holders no técnicos. Esto no reemplaza auditoría humana pero aumenta capacidad de comunidad para detectar problemas antes de que propuestas maliciosas o defectuosas se ejecuten.

La IA también puede ayudar a detectar comportamiento sospechoso en tiempo real, analizando patrones de transacciones para identificar cambios de permisos anómalos o concentración de poder de votación que sugiere intento de captura de governance. Los sistemas pueden alertar automáticamente a la comunidad cuando detectan actividad que estadísticamente se desvía de normas históricas.

El riesgo es que dependencia excesiva en IA para governance crea nuevo tipo de centralización donde quienes controlan los modelos de análisis ejercen influencia desproporcionada. Pero usado como herramienta complementaria que aumenta capacidad humana sin reemplazar juicio humano, tiene potencial para hacer governance más informada y segura.

**Contratos Upgradeable y patrones de proxy** merecen mención especial en contexto de control de acceso futuro. Mientras la sección anterior cubrió timelocks y governance, los mecanismos técnicos específicos de upgradeability introducen vectores de ataque únicos.

**Transparent Proxy** separa estrictamente funciones administrativas de funciones de usuario. El admin solo puede actualizar la implementación pero no puede llamar funciones del contrato de lógica. Los usuarios pueden llamar funciones pero no pueden actualizar. Esta separación previene confusión donde llamadas de admin podrían ser interpretadas como llamadas de usuario si funciones tienen nombres coincidentes, un bug sutil que ha causado exploits.

**UUPS (Universal Upgradeable Proxy Standard)** coloca la lógica de actualización en el contrato de implementación en lugar del proxy. Esto reduce costos de gas en llamadas normales porque el proxy es más simple, pero introduce riesgo crítico: si despliegas nueva implementación que no incluye función de upgrade, el contrato queda permanentemente bloqueado en esa versión. No hay forma de actualizar nuevamente porque la capacidad de actualización misma se perdió.

Ambos patrones requieren control de acceso extremadamente cuidadoso en el rol de upgrader. Este rol debe estar en multisig o DAO, nunca en EOA individual. Debe tener timelock largo antes de que upgrades puedan ejecutarse. Y la comunidad debe tener plan claro de cómo migrar a versión inmutable eventualmente, eliminando capacidad de upgrade una vez que el protocolo está suficientemente maduro y probado en batalla.

La tendencia general es hacia minimización progresiva de upgradeability. Protocolos comienzan completamente upgradeable durante desarrollo temprano, luego restringen capacidad de upgrade a parámetros específicos, finalmente renuncian a upgradeability completamente excepto mecanismos de emergencia extremadamente limitados. El objetivo final de muchos protocolos es inmutabilidad completa donde el código se convierte en ley literal sin ninguna capacidad de modificación humana.

---

**Para profundizar**:

- Sobre identidad y verificación: [Identidad Web3](7-1-identity.md)
- Sobre governance en DAOs: [DAO](7-3-DAO.md)
- Sobre reputación on-chain: [Reputación Web3](7-2-reputation.md)
- Sobre resolución de conflictos: [Resolución de Conflictos](7-4-conflict-resolution.md)

## Attestations de membresía como credenciales organizacionales

Más allá del control de acceso técnico dentro de smart contracts, las organizaciones Web3 necesitan emitir credenciales verificables sobre sus miembros que sean portátiles y utilizables fuera del contexto de un contrato específico. Mientras RBAC gestiona permisos operativos on-chain, las attestations organizacionales construyen identidad profesional y reputación que trasciende un protocolo individual.

Utilizando infraestructura como [Ethereum Attestation Service (EAS)](https://attest.sh/), las DAOs pueden emitir attestations verificables que confirman membresía, roles específicos, contribuciones realizadas, o duración de participación. Estas attestations funcionan como credenciales laborales descentralizadas donde la organización firma criptográficamente declaraciones sobre el individuo que cualquier tercero puede verificar independientemente.

A diferencia de roles RBAC que existen internamente en un contrato y solo tienen significado dentro de ese sistema específico, las attestations son credenciales externas portátiles. Si contribuiste significativamente a una DAO reconocida, esa organización puede emitir una attestation on-chain vinculada a tu dirección. Meses o años después, cuando aplicas a otra DAO o protocolo, simplemente conectas tu wallet y la nueva organización verifica criptográficamente que la attestation fue emitida por la DAO original y no ha sido revocada. Tu reputación profesional se vuelve verificable sin depender de cartas de recomendación tradicionales, llamadas de verificación de empleo, o confianza en plataformas centralizadas como LinkedIn.

El modelo es particularmente poderoso para contributors que participan en múltiples DAOs simultáneamente. En lugar de reconstruir reputación desde cero en cada comunidad, tus attestations acumuladas de organizaciones previas sirven como proof of work verificable. Una DAO de desarrollo puede emitir attestation confirmando que completaste 50 pull requests en su repositorio. Una DAO de inversión puede atestiguar que participaste en due diligence de 10 propuestas. Una DAO de educación puede certificar que completaste cierto programa de formación. Colectivamente, estas attestations construyen un CV on-chain verificable que nadie puede falsificar ni manipular.

La revocación es importante para mantener integridad del sistema. Si un miembro es expulsado por comportamiento dañino o simplemente deja de participar activamente, la organización puede revocar las attestations correspondientes. Los verificadores consultan el estado de revocación antes de confiar en una credencial, asegurando que solo attestations actualmente válidas tienen peso.

Para arquitectura técnica completa de attestations, protocolos de emisión y verificación, y cómo se integran con identidad descentralizada más amplia, consulta [Identidad Web3](7-1-identity.md). Para cómo las attestations contribuyen a sistemas de reputación agregada, ver [Reputación Web3](7-2-reputation.md).

## Identidad corporativa: arquitecturas jerárquicas con DIDs

Las organizaciones Web3 necesitan estructuras de identidad que reflejen jerarquías corporativas mientras mantienen descentralización y verificabilidad. Los sistemas de identidad jerárquica basados en DIDs permiten que organizaciones emitan identidades derivadas para empleados, departamentos, o subsidiarias donde la raíz corporativa mantiene control último pero delega autoridad operacional a identidades subordinadas.

**Arquitectura de DIDs corporativos**:

Una organización establece un DID raíz corporativo controlado mediante multisig de ejecutivos o DAO governance. Este DID corporativo firma y emite DIDs subordinados para diferentes niveles: subsidiarias regionales, departamentos funcionales (legal, finanzas, operaciones), y finalmente empleados individuales. Cada nivel puede delegar capacidades específicas al nivel inferior mientras retiene capacidad de revocar esas delegaciones si es necesario.

Un empleado de marketing en subsidiaria europea podría tener DID jerárquico: `did:example:corporation/europe/marketing/employee123`. Este DID hereda implícitamente confianza de los niveles superiores en la jerarquía. Cuando el empleado firma algo, verificadores pueden trazar la cadena de confianza hasta el DID raíz corporativo, confirmando que es representante legítimo autorizado de esa organización específica.

La separación de niveles permite gestión eficiente de ciclo de vida. Cuando un empleado cambia de departamento, su DID subordinado se transfiere a nueva rama jerárquica sin alterar el DID raíz. Cuando alguien deja la empresa, su DID subordinado se revoca sin afectar a otros. Si toda una subsidiaria se vende o cierra, toda esa rama del árbol de identidades puede revocarse o transferirse de una vez.

**Compliance y auditoría organizacional**:

Las identidades corporativas jerárquicas facilitan auditoría regulatoria y compliance. Cada acción firmada por un DID subordinado queda vinculada criptográficamente a la jerarquía que la autorizó. Los auditores pueden verificar que quien firmó cierto contrato tenía autoridad delegada apropiada en ese momento, consultando el estado histórico de la jerarquía de DIDs.

Para entornos regulados como finanzas, las organizaciones pueden implementar políticas donde ciertos tipos de transacciones requieren firmas de múltiples niveles jerárquicos. Una transferencia menor puede ser autorizada por empleado individual, transferencia media requiere aprobación adicional de manager de departamento, y transferencia grande requiere firma de ejecutivo nivel C. Estas políticas se codifican on-chain en forma verificable.

**Governance multi-nivel**:

Los DIDs corporativos pueden integrarse con governance multi-firma donde diferentes decisiones requieren consenso de diferentes partes de la jerarquía. Una propuesta técnica podría requerir aprobación de mayoría de departamento de ingeniería, mientras que decisión financiera requiere consenso de CFO, CEO y board. La estructura de DID jerárquico mapea naturalmente a estas políticas de governance, haciendo la autorización explícita y auditable.

**Trade-offs y consideraciones prácticas**:

La centralización inherente en jerarquías corporativas tensiona con filosofía descentralizada de Web3. Los empleados subordinados dependen de que el nivel superior no revoque maliciosamente su autoridad. Por eso muchas implementaciones incluyen compromisos de governance donde revocaciones requieren justificación pública y proceso de apelación mediante DAO o mecanismo neutral.

La complejidad técnica de gestionar árboles de identidad puede ser sustancial, especialmente para organizaciones grandes con frecuentes cambios de estructura. Las herramientas y estándares están madurando pero aún no alcanzan la facilidad de administración de Active Directory corporativo tradicional.

Para especificaciones técnicas de métodos DID, estructura de documentos DID, y protocolos de resolución que hacen posible estas jerarquías, consulta documentación técnica en [infrastructure/did-protocols.md](../infrastructure/did-protocols.md).

## Capabilities y delegación: Authorization Capabilities (ZCAP)

Más allá de sistemas RBAC donde permisos están centralizados en registros de contrato, los **Authorization Capabilities (ZCAPs)** ofrecen modelo descentralizado de autorización donde los permisos mismos son tokens portátiles que pueden ser delegados, atenuados, y revocados sin coordinación centralizada.

**Modelo de capabilities vs ACLs**:

En Access Control Lists (ACLs) tradicionales, un sistema central mantiene registro de "quién puede hacer qué". Cuando intentas una acción, el sistema consulta su base de datos para verificar tus permisos. En modelo de capabilities, la autorización es un token que llevas contigo. Si posees el capability, puedes ejecutar la acción, sin necesidad de consultar lista central.

Imagina la diferencia entre una lista de invitados (ACL) donde el guardia de seguridad consulta tu nombre en su clipboard antes de dejarte entrar, versus un ticket físico (capability) donde simplemente presentas el ticket y entras. El ticket es transferible, puedes delegarlo a otra persona sin interacción con quien organizó el evento. Esta es la esencia de capabilities.

**Arquitectura de ZCAPs**:

Los ZCAPs implementan capabilities utilizando criptografía de clave pública y chains of custody verificables. Un capability es un documento firmado que especifica:

- **Invocation target**: Qué recurso o operación está autorizada (por ejemplo, "ejecutar función transferTokens en contrato 0x123")
- **Caveat/attenuation**: Restricciones adicionales (por ejemplo, "solo transferencias hasta 100 tokens", "solo hasta fecha X")  
- **Issuer**: Quién emitió este capability (DID del emisor)
- **Subject**: A quién se otorgó (DID del receptor)
- **Proof chain**: Cadena de firmas que demuestra delegación legítima desde authority original

Cuando invocas un capability, presentas el documento firmado completo incluyendo toda la cadena de delegación. El sistema verifica criptográficamente que cada nivel de la cadena autorizó legítimamente al siguiente nivel, y que las atenuaciones acumuladas se respetan.

**Delegación transitiva y atenuación**:

La potencia de capabilities emerge en delegación transitiva. Alice tiene capability para gastar hasta 1000 tokens del tesorero de una DAO. Ella delega a Bob un capability derivado que lo autoriza a gastar hasta 100 tokens. Bob puede delegar ulteriormente a Carol un capability aún más restringido de gastar hasta 10 tokens. En cada paso, los permisos solo pueden atenuarse (reducirse), nunca amplificarse.

Cuando Carol intenta gastar 5 tokens, presenta su capability que incluye la cadena completa: capability original de Alice firmado por la DAO, delegación de Alice a Bob con atenuación a 100, delegación de Bob a Carol con atenuación a 10. El contrato verifica todas las firmas y confirma que los límites se respetan en cada nivel. No necesita consultar ninguna lista centralizada; toda la autorización está en el capability presentado.

Si Bob descubre que Carol está abusando del permiso, puede revocar su capability publicando revocación firmada en registry descentralizado. Futuras invocaciones del capability de Carol fallarán cuando el sistema consulte el estado de revocación. Crucialmente, Alice no necesita involucrarse; Bob puede revocar su propia delegación sin interacción con niveles superiores.

**Casos de uso organizacionales**:

**Governance de DAO con delegación escalonada**: Los holders de tokens governance delegan capabilities de voto a delegados especializados. El delegado puede ulteriormente sub-delegar a expertos para propuestas técnicas específicas fuera de su expertise. La cadena de delegación es auditable on-chain, y los holders originales pueden revocar en cualquier momento si pierden confianza en su delegado.

**Autoridad de firma corporativa**: CFO tiene capability de aprobar cualquier gasto corporativo. Delega capabilities atenuados a managers departamentales con límites de presupuesto específicos. Cada manager delega capabilities aún más limitados a team leads. Cada nivel puede operar autónomamente dentro de sus límites sin requerir aprobación constante de superiores, pero toda la cadena de autoridad es criptográficamente verificable.

**Automatización DeFi con guardrails**: Un protocol DAO delega capability a strategy contract para realizar operaciones específicas de farming (por ejemplo, deposit en Aave, swap en Uniswap). El capability incluye caveats estrictos: solo pares de tokens whitelist, solo slippage bajo 1%, solo interacción con contratos auditados. El strategy contract opera autónomamente dentro de estos límites pero no puede excederlos sin nueva delegación explícita.

**Social recovery con timelock progresivo**: Un usuario delega capabilities limitados a sus guardianes de social recovery. Inicialmente, los guardianes solo pueden iniciar propuesta de recuperación que entra en timelock de 7 días. Si el usuario no cancela durante ese periodo (presumiblemente porque realmente perdió acceso), el capability de los guardianes se amplía automáticamente para ejecutar la recuperación. Esto previene que guardianes maliciosos roben fondos inmediatamente pero permite recuperación legítima si el usuario está realmente incapacitado.

**Beneficios sobre RBAC tradicional**:

- **Delegación sin coordinación central**: No necesitas modificar contrato para delegar permisos, simplemente emites nuevo capability firmado
- **Privacy mediante selective disclosure**: Puedes presentar capabilities sin revelar toda tu estructura de permisos o relaciones de delegación a terceros no involucrados
- **Funcionamiento off-line**: Capabilities pueden ser verificados con solo criptografía de clave pública, sin necesidad de consultar blockchain para cada operación
- **Revocación granular**: Cada delegador puede revocar solo las delegaciones que él mismo emitió sin afectar niveles superiores o paralelos de la cadena
- **Auditoría post-hoc**: La cadena completa de autorización queda capturada en cada invocación, permitiendo análisis forense detallado de quién autorizó qué

**Desafíos de implementación**:

Los ZCAPs introducen complejidad sustancial comparado con RBAC simple. Los desarrolladores deben gestionar verificación de cadenas de firmas, validación de atenuaciones acumuladas, manejo de revocaciones distribuidas, y prevención de replay attacks. Los sistemas necesitan infrastructure robusta para publicar y consultar revocaciones, típicamente mediante registros descentralizados o redes P2P.

La experiencia de usuario puede ser compleja porque los usuarios deben gestionar capabilities como artefactos digitales, entender qué capabilities poseen, rastrear a quién delegaron, y monitorear si sus delegaciones fueron ulteriormente sub-delegadas. Las herramientas de wallet para gestionar capabilities están menos maduras que las UIs para RBAC tradicional.

Las implementaciones de referencia incluyen el [W3C zcap-ld specification](https://w3c-ccg.github.io/zcap-ld/) que define formato estándar para capabilities usando Linked Data Signatures, y [Object Capabilities (ocaps)](http://erights.org/elib/capability/ode/ode.pdf) pattern implementado en lenguajes como Agoric que construyen capacidades directamente en el modelo de objetos del lenguaje.

Para casos de uso concretos de delegación temporal en DAOs y workflows multi-paso, consulta [DAO](7-3-DAO.md).

## DIDComm: mensajería segura para organizaciones

Las organizaciones Web3 necesitan canales de comunicación seguros y verificables entre entidades identificadas por DIDs. **DIDComm** es el protocolo de mensajería construido sobre infraestructura de identidad descentralizada que habilita comunicación autenticada, encriptada y privada sin depender de intermediarios centralizados.

**Arquitectura de DIDComm**:

A diferencia de email donde confías en servidores de correo centralizados, o mensajería corporativa donde confías en Slack/Microsoft Teams, DIDComm permite comunicación peer-to-peer donde los participantes se autentican mediante sus DIDs. Cada mensaje está firmado criptográficamente por el DID del remitente y encriptado para el DID del destinatario, garantizando autenticidad, integridad y confidencialidad end-to-end.

El protocolo utiliza las claves públicas publicadas en los DID Documents de los participantes. Cuando Alice (con `did:example:alice`) quiere enviar mensaje a Bob (`did:example:bob`), su cliente DIDComm:
1. Resuelve el DID de Bob para obtener su DID Document y extraer sus claves públicas y endpoints de servicio
2. Encripta el mensaje usando clave pública de Bob
3. Firma el mensaje encriptado con clave privada de Alice
4. Envía el mensaje al endpoint especificado en el DID Document de Bob

Bob puede verificar criptográficamente que el mensaje provino de Alice consultando su DID Document público, y solo él puede desencriptarlo con su clave privada. No hay servidor central que puede leer el contenido ni falsificar el remitente.

**Flujos de onboarding organizacional**:

Cuando una organización contrata nuevo empleado, el proceso tradicional implica correos inseguros con credenciales temporales, múltiples sistemas de login, y riesgo de phishing durante setup inicial. Con DIDComm:

1. La organización emite DID subordinado para el empleado como parte del árbol de identidad corporativo
2. Envía mensaje DIDComm inicial al DID del empleado conteniendo invitaciones a sistemas internos, llaves de acceso encriptadas, y documentación
3. El empleado verifica criptográficamente que la comunicación proviene del DID corporativo legítimo
4. Responde mediante DIDComm para confirmar recepción y completar setup de accesos
5. Todos los pasos quedan auditados mediante mensajes firmados sin pasar por email inseguro o slack corporativo vulnerable

El offboarding es igualmente auditable: la organización envía mensaje DIDComm notificando revocación de accesos, el empleado firma recepción, y toda la comunicación de desprovisioning queda verificable on-chain mediante las firmas de ambas partes.

**Canales B2B y comunicación inter-organizacional**:

Las organizaciones frecuentemente necesitan establecer canales seguros con partners, proveedores o clientes corporativos. DIDComm permite establecer conexiones verificables entre DIDs corporativos de diferentes entidades:

- **Negociación de contratos**: Borradores de smart contracts y términos legales pueden intercambiarse mediante DIDComm donde cada versión está firmada por quien la propuso, creando audit trail verificable de todo el proceso de negociación
- **Coordinación de multisig**: Para transacciones que requieren firmas de múltiples organizaciones, DIDComm sirve como canal seguro para compartir propuestas de transacción, aprobar firmas, y coordinar ejecución final
- **Supply chain tracking**: Cada organización en cadena de suministro puede emitir mensajes DIDComm firmados confirmando recepción de mercancía o completar paso de proceso, creando registro inmutable del flujo de productos
- **Incident response**: Cuando se descubre vulnerabilidad de seguridad que afecta múltiples protocolos, las organizaciones pueden usar DIDComm para comunicación verificada y encriptada de detalles antes de disclosure público

**Integración con infraestructura existente**:

DIDComm puede funcionar como capa de autenticación y encriptación sobre transporte existente. Los mensajes pueden enviarse sobre HTTPS, WebSocket, IPFS, o incluso email tradicional como sobre encriptado. La diferencia crítica es que independientemente del transporte subyacente, la autenticación y encriptación dependen solo de los DIDs de las partes, no de confianza en el proveedor de transporte.

Para organizaciones transicionando desde sistemas legacy, puede implementarse gateway que traduce entre mensajería interna tradicional y DIDComm externo. Empleados internos continúan usando Slack o Teams familiarmente, pero cuando se comunican con entidades externas, el gateway automáticamente convierte mensajes a formato DIDComm con firmas del DID corporativo.

**Forward secrecy y rotación de claves**:

DIDComm v2 implementa forward secrecy mediante uso de claves efímeras para cada sesión. Incluso si clave privada de largo plazo de un participante se compromete en el futuro, mensajes de sesiones pasadas permanecen seguros porque fueron encriptados con claves de sesión que ya no existen. Esta propiedad es crítica para comunicaciones corporativas sensibles que pueden contener información competitiva valiosa años después.

La rotación de claves se gestiona mediante actualización de DID Document. Cuando una organización rota sus claves (por política de seguridad o porque se compromete clave antigua), publica nuevo DID Document con las claves actualizadas. Los participantes que envían mensajes nuevos automáticamente usan las claves nuevas después de resolver el DID actualizado. No se requiere coordinación manual con cada contacto.

**Privacidad mediante DIDs efímeros**:

Para comunicaciones que requieren máxima privacidad, DIDComm puede usar DIDs efímeros de corta duración que no están vinculados a identidad de largo plazo. Una organización puede crear DID temporal específicamente para una negociación particular, usarlo para toda comunicación relacionada con ese deal, y desecharlo al finalizar. Observadores externos no pueden vincular esa comunicación con la identidad corporativa principal.

Esta técnica es especialmente valiosa para proteger contra análisis de graph social. Si todas las comunicaciones corporativas usan el mismo DID corporativo permanente, adversarios pueden construir mapa completo de con quién interactúa la organización. Los DIDs efímeros rompen estas correlaciones while still allowing verification within the specific interaction context.

**Limitaciones y consideraciones**:

DIDComm introduce overhead de implementación comparado con email o mensajería centralizada. Los desarrolladores deben integrar librerías de DID resolution, gestión de claves, criptografía de curva elíptica, y lógica de routing. La experiencia de usuario requiere que participantes gestionen wallets con claves privadas en lugar de simplemente recordar contraseña.

La delivery de mensajes no es garantizada como en sistemas centralizados donde el proveedor asegura eventual delivery. DIDComm es más cercano a email en este aspecto; si el endpoint del destinatario está temporalmente inalcanzable, el remitente debe reintentar o usar queuing mechanisms. Para casos de uso críticos, se necesitan confirmaciones explícitas de recepción codificadas en protocolo de aplicación.

La disponibilidad de endpoints es responsabilidad del participante. Si publicas endpoint en tu DID Document que luego va offline, nadie puede enviarte mensajes hasta que actualices el DID Document con endpoint funcional. Servicios de mediator pueden ayudar; actúan como relayers que almacenan mensajes cuando el destinatario está offline y los entregan cuando vuelve online, similar a servidores de correo pero sin capacidad de descifrar contenido.

Para especificaciones completas de DIDComm, protocolos de routing, y ejemplos de implementación, consulta [DIDComm Messaging v2.0](https://identity.foundation/didcomm-messaging/spec/) de Decentralized Identity Foundation.

---
