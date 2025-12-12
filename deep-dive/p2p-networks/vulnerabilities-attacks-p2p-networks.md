# Vulnerabilidades y Ataques en redes P2P

> Este es el resumen del análisis sobre [redes P2P](../../infrastructure/miscelanea/p2p_overview.md) realizado en la sección de la `infraestructura web3`.

Las redes peer-to-peer (P2P) son sistemas sin servidores centrales que permiten conectar usuarios directamente y mejorar la resiliencia frente a fallos o censura, es decir, evitan el punto único de fallo. Sin embargo, esa misma arquitectura introduce vectores de ataque y limitaciones específicas. Este documento resume las principales amenazas y problemas inherentes o especialmente relevantes en entornos P2P.

## Insuficiente cantidad de nodos

Una red con baja participación es más vulnerable. Cuantos menos nodos existan, menor será la redundancia y la diversidad de rutas, facilitando ataques de aislamiento o manipulación. La seguridad en redes distribuidas depende en gran medida del número y dispersión de nodos activos.

## Concentración de nodos bajo un mismo control

Cuando muchos nodos están alojados o gestionados por la misma entidad o infraestructura, se rompe el principio de descentralización. Una concentración excesiva de nodos bajo un único control facilita censura, manipulación de tráfico o recolección de datos. Esto reduce la resiliencia global y crea puntos únicos de fallo.

## Fragmentación de la red y estado paralelo (forks)

Las bifurcaciones o forks ocurren cuando la red se divide en dos o más subconjuntos que mantienen visiones distintas del estado global. En blockchains esto puede generar doble gasto o pérdida temporal de consenso. En redes P2P generales puede producir inconsistencias o desincronización entre grupos de nodos, afectando la coherencia y la disponibilidad.

## Disponibilidad: churn

El churn describe la rotación constante de nodos que se unen y abandonan la red. Una tasa alta de churn degrada la estabilidad y puede dejar segmentos inaccesibles o sin replicación suficiente. Los sistemas P2P deben diseñarse para tolerar esta volatilidad mediante redundancia, persistencia distribuida y descubrimiento dinámico.

## Latencia y velocidad de la red

La descentralización introduce latencia adicional y menor velocidad de propagación comparada con arquitecturas centralizadas. Factores como la distancia entre nodos, el ancho de banda desigual o la falta de optimización global afectan el rendimiento. Esto puede ser crítico en sistemas donde la sincronización o la inmediatez son esenciales.

## Identidades falsas: el ataque Sybil

El ataque Sybil consiste en la creación masiva de identidades falsas o nodos fantasma para ganar influencia desproporcionada o sabotear la red desde dentro. En redes de intercambio, un atacante puede poblar la red con nodos que simulan ofrecer recursos pero no los entregan, degradando disponibilidad y rendimiento. La facilidad de incorporación en sistemas abiertos convierte la apertura en un talón de Aquiles si no existen mecanismos de coste o verificación.

## Aislar al nodo: ataques Eclipse y Erebus

Los ataques de aislamiento buscan controlar la visión que un nodo tiene de la red. En un ataque Eclipse, el atacante manipula las conexiones de un nodo hasta que todas o la mayoría apuntan a nodos maliciosos bajo su control. De esta forma, la víctima queda "eclipsada": solo recibe la información que el atacante decide transmitirle. Esto permite ocultar transacciones, retrasar bloques o alterar la percepción del estado global de la red. En sistemas de consenso, el impacto puede ser crítico, ya que el nodo actúa con información sesgada.

El ataque Erebus es una variante más sofisticada. En lugar de actuar únicamente a nivel de aplicación, manipula la infraestructura de red, como el enrutamiento, para interceptar y controlar las conexiones entre nodos. Así logra el mismo efecto de aislamiento, pero desde una capa inferior del protocolo, lo que lo hace más difícil de detectar y mitigar.

## Saturar la red: ataques DoS

Los ataques de denegación de servicio buscan inundar nodos o segmentos de la red con tráfico malicioso hasta causar su degradación o caída. En aplicaciones P2P de streaming o descubrimiento de recursos, un DoS puede reducir drásticamente la disponibilidad. Mitigar DoS en entornos descentralizados exige coordinación entre nodos honestos y estrategias de priorización de tráfico.

## Corromper los datos: DHT Poisoning

Las tablas hash distribuidas (DHT) permiten localizar nodos y recursos en redes P2P. Si un atacante logra manipularlas, puede redirigir tráfico, ocultar contenidos o provocar errores de resolución. El ataque de Poisoning consiste en inyectar información falsa o maliciosa en la red, como malware disfrazado de archivos legítimos. Sin mecanismos de validación, la confianza se vuelve una vulnerabilidad estructural.

## Vulnerabilidades a la lógica on-chain en redes blockchain

Las blockchains, como sistemas P2P especializados, presentan vulnerabilidades adicionales en su capa lógica. Los scripts o contratos inteligentes pueden ser explotados mediante ataques de replay, re-entrancy o incluso el 51 por ciento y doble gasto. Aunque no todas estas amenazas son exclusivas de las P2P, comparten el origen en la ausencia de control centralizado, lo que amplía el espacio de ataque y dificulta la defensa coordinada.

## Escalabilidad de la seguridad (dificultad de aplicación de políticas uniformes)

A medida que la red crece, aplicar políticas de seguridad uniformes se vuelve complejo. Los nodos pueden ejecutar diferentes versiones del software, configuraciones o políticas de validación. Esto complica la auditoría, el monitoreo forense y la respuesta a incidentes, aumentando la superficie de ataque y reduciendo la capacidad de coordinación.

## Exposición de direcciones IP

En muchas redes P2P, las direcciones IP de los nodos son visibles públicamente como parte del mecanismo de descubrimiento. Esto facilita ataques dirigidos, rastreo de ubicación o identificación de usuarios. La exposición de metadatos como horarios de actividad o patrones de tráfico puede comprometer la privacidad y la anonimato de los participantes.
