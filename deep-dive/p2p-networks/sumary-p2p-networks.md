# Presentación y resumen: Redes P2P – Arquitecturas entre iguales

> Este es el resumen del análisis sobre [redes P2P](../../infrastructure/miscelanea/p2p_overview.md) realizado en la sección de la `infraestructura web3`.

## Qué es una red P2P

Una red P2P es un sistema en el que los nodos o participantes se comunican directamente entre sí sin necesidad de un servidor central. Cada nodo actúa simultáneamente como cliente y servidor, compartiendo recursos, información o capacidad de cómputo. Este principio de igualdad entre nodos es el núcleo de su fortaleza: las redes P2P son resilientes, distribuidas y difíciles de censurar.

No debe confundirse una red P2P con una red distribuida. Como su nombre indica, una red P2P implica comunicación entre pares: si un nodo no puede conectarse en igualdad de condiciones con otro, no es una red P2P. Tampoco debe confundirse que una red P2P sea inherentemente descentralizada; una red entre pares puede tener un nodo coordinador central, y en ese caso no lo sería del todo.

Si lo vemos de forma menos abstracta, podemos ver el ejemplo de [BitTorrent](https://es.wikipedia.org/wiki/BitTorrent), donde cada persona instala un programa en su PC, que sería un nodo. Cuando quieres un archivo, tu programa busca otros usuarios (otros nodos) que ya tienen partes de ese archivo para descargar varias partes a la vez, que ese sería el propósito de la red.
Al mismo tiempo, tú también compartes las partes que ya tienes con otros, sin depender de un servidor central.

Una red p2p elimina el punto único de fallo (SPOF), aumentando la resiliencia y dificultando la censura, ya que no depende de un único nodo o servidor central para funcionar.

Existen matices: no todas las redes P2P son totalmente descentralizadas. Algunas mantienen nodos especiales o nodos de coordinación, conocidos como supernodos, que facilitan la comunicación o gestionan partes críticas del sistema.

## Diferencia con Blockchain

Aunque frecuentemente se confunden, P2P y blockchain no son lo mismo. Blockchain es una estructura de datos distribuida que almacena transacciones o información de forma inmutable. P2P es la infraestructura de comunicación que hace posible el intercambio de información entre los nodos que mantienen esa cadena de bloques.

Podemos imaginarlo así: la red P2P es la carretera, y blockchain es el vehículo que circula sobre ella. La una no depende de la otra, pero blockchain no podría existir sin una red P2P subyacente.

## Modelo de confianza

Define cómo y en quién confían los nodos para interactuar, validar información y alcanzar consenso. Determina si la red requiere identidad, reputación o prueba criptográfica para garantizar seguridad y funcionamiento correcto.

En las redes P2P, especialmente en el ámbito de web3, el modelo de confianza suele ser "sin confianza" (trustless): los nodos interactúan y validan información mediante mecanismos criptográficos, sin necesidad de confiar unos en otros, es decir, los nodos deben demostrar que son confiables entre ellos y para ello deben crear pruebas o evidencias al respecto.

## Modelos de gobernanza

Las redes P2P requieren tomar decisiones que influyen directamente en su diseño, funcionamiento y evolución. Estas decisiones determinan cómo se participa, cómo se proponen cambios en el protocolo, cómo se resuelven conflictos entre los participantes y qué normas rigen la interacción. Detrás de toda red P2P hay actores, organizaciones o personas que influyen en su desarrollo, por lo que la gobernanza resulta esencial.

La gobernanza en una red P2P define cómo se toman las decisiones, cómo se gestionan los cambios y quién tiene autoridad o capacidad de influencia dentro del sistema.

Como modelos concretos podemos encontrarnos normalmente, centralizada o federada: un grupo de entidades coordina la red. Suele encontrarse en entornos empresariales o institucionales.

Pero en web3 sobre todo tenemos dos tipos: descentralizada o DAO. En descentralizada la toma de decisiones se distribuye entre todos los participantes. Aquí entran modelos como Bitcoin, donde las reglas se aplican mediante consenso técnico; y las DAO (Organizaciones Autónomas Descentralizadas), que es una evolución de la descentralización, donde los participantes usan tokens para votar y definir el rumbo de la red.

Además existen los mecanismos de decisión: pueden ser por mayoría simple, mayoría absoluta, delegación de voto (como en Proof of Stake), o consenso total, que busca la unanimidad, como en ciertos protocolos tolerantes a fallos bizantinos.

## Grado de descentralización y sus compensaciones

El grado de descentralización mide cuánto poder o responsabilidad se distribuye entre los nodos. En el extremo más centralizado, hay servidores que controlan gran parte del tráfico; en el extremo opuesto, cada nodo es totalmente independiente y autónomo.

Sin embargo, la descentralización tiene un equilibrio inherente con la seguridad y el rendimiento. Cuanto más descentralizada es una red, mayor resistencia a fallos y censura logra, pero también puede perder eficiencia y velocidad, ya que la coordinación entre muchos nodos requiere más tiempo y recursos.

Igualmente, una red muy descentralizada no está exenta de fallos de seguridad. Por ejemplo, resulta más complicado coordinar una defensa ante ataques y está expuesta a vulnerabilidades específicas como los ataques de aislamiento (por ejemplo, eclipse o Erebus). Además, existen problemas asociados al churn (alta rotación de nodos), lo que puede afectar la disponibilidad y la estabilidad de la red.

Por eso, el diseño de una red P2P busca siempre un equilibrio entre rendimiento, seguridad y autonomía. Bitcoin, por ejemplo, privilegia la descentralización y la confianza criptográfica sobre la rapidez, mientras que otras redes priorizan la eficiencia sacrificando algo de descentralización.

## Modelo de autorización

Define quién puede participar y con qué permisos, lo cual influye en la resistencia a la censura, tolerancia a fallos y gobernanza.

En el contexto de web3, lo más habitual es que las redes P2P sean públicas y abiertas, permitiendo la participación de cualquier nodo. Sin embargo, también existen redes permisionadas, donde el acceso está controlado y solo ciertos participantes pueden interactuar. Además, hay redes privadas, consorcios (gestionadas por un grupo de entidades) e híbridas, que combinan características de los modelos anteriores según las necesidades de gobernanza y seguridad.

## Estrategias de almacenamiento en redes p2p

El almacenamiento en redes P2P enfrenta retos importantes debido al gran volumen de datos y la necesidad de asegurar disponibilidad y eficiencia. Por ello, es fundamental definir cómo se organiza y distribuye la información entre los nodos participantes, buscando optimizar la localización de datos y el equilibrio de carga.

En este contexto, el almacenamiento siempre es distribuido, para mejorar la resiliencia y disponibilidad, y se emplean técnicas como la replicación, donde múltiples nodos almacenen copias de los datos, reduciendo el riesgo de pérdida y facilitando el acceso. Esta replicación puede ser por ejemplo parcial, total o bajo demanda (como en IPFS demanda por el usuario).

Para optimizar aún más el almacenamiento, pueden aplicarse estrategias como la indexación y el sharding (fragmentación de datos en subredes), aunque esto a veces implique reducir el grado de descentralización. Estas decisiones dependen de las necesidades específicas de cada red.

Otras técnicas complementarias incluyen el pruning (podado de datos antiguos o irrelevantes) y la compresión, que ayudan a gestionar el espacio y mantener la eficiencia operativa de la red.

## Redes estructuradas y no estructuradas

Una característica fundamental de las redes P2P es su topología lógica, que influye directamente en la estrategia de almacenamiento y en la eficiencia de acceso a los datos. Las redes estructuradas gestionan el almacenamiento y la búsqueda de información de forma determinista, utilizando índices distribuidos como las DHT (Distributed Hash Table), lo que permite búsquedas rápidas y eficientes. Por el contrario, en las redes no estructuradas, los datos se almacenan y localizan de manera más aleatoria, propagando consultas entre nodos; esto puede ser menos eficiente, pero aporta mayor resiliencia frente a desconexiones y alta rotación de nodos (churn).

Ejemplos de redes estructuradas incluyen DHTs como Kademlia, mientras que en las no estructuradas predominan protocolos como gossip o flooding.

**¿Cuándo se utiliza una red estructurada o no estructurada?**

La elección depende del propósito de la red. Una red pública, con alto grado de descentralización y churn, que requiera resiliencia y simplicidad, suele optar por una topología no estructurada. En cambio, una red más estable, escalable y con bajo churn, donde la eficiencia es prioritaria, preferirá una estructura determinista, aunque esto implique mayor complejidad en el diseño.

## Mecanismos en redes p2p

Las redes P2P implican una serie de engranajes complejos, no necesitamos comprenderlo todo pero para hacernos una idea podemos explicar algunos relevantes.

Primero está la conexión inicial (Bootstrap), donde el nodo necesita descubrir otros nodos de la red. Para ello recurre a nodos semilla, que son nodos especiales mantenidos por la organización y que concentran la mayor cantidad de pares conocidos, sirviendo como punto de entrada al sistema.

Además, los nodos deben comunicarse entre sí, y no siempre lo hacen todos con todos. De hecho, este descubrimiento y la comunicación posterior pueden estar organizados, como ocurre en redes estructuradas (por ejemplo, DHT/Kademlia), donde la relación es determinista y se utilizan tablas de enrutamiento. También pueden ser más caóticas y más resilientes, como en redes no estructuradas, que se basan en la propagación probabilística, como en los protocolos Gossip y Flooding.

La forma en que los nodos replican la información y la consistencia con la que lo hacen puede variar. Por ejemplo, la replicación puede ser total, donde todos los nodos de la red tienen la misma copia; parcial, donde solo los nodos relevantes almacenan la información; o incluso bajo demanda del usuario, como ocurre en IPFS. En cuanto a la consistencia, puede ser fuerte, donde cada nodo debe confirmar que ha recibido el dato, aunque esto implica un coste elevado de trabajo. Lo más habitual es la consistencia causal, en la que no se exige confirmación posterior y se asume que la información fue recibida correctamente.

Este resumen nos da una idea de la complejidad de todo esto, y ayuda a conocer cómo estos mecanismos permiten que las redes P2P sean escalables, resilientes y descentralizadas, adaptándose a diferentes necesidades de diseño.

## Clasificación y agrupación de nodos en redes P2P

Aunque los nodos en una red P2P se diseñan para ser homogéneos, en la práctica aparecen diferencias según su capacidad y función. Un ejemplo claro es Ethereum: por capacidad existen nodos históricos y podados, donde los primeros almacenan toda la información de la cadena y los segundos solo una parte. Por función, también encontramos nodos que se dedican a atender peticiones sin participar en el consenso, optimizando así el rendimiento en tareas específicas.

También hay nodos con tareas especiales dentro de la infraestructura, como los nodos puente (bridge nodes) en redes blockchain, que conectan distintas cadenas.

Además, los nodos pueden agruparse, por ejemplo en subredes, que les permite operar de forma más eficiente. Un ejemplo típico es el sharding de Ethereum, donde la red se divide en múltiples shards y cada grupo de nodos gestiona solo una parte del estado o los datos, permitiendo un procesamiento paralelo y más escalable.

---
