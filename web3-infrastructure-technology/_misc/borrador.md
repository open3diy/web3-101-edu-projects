## Redes entre pares peer-to-peer





**Descubrimiento de nodos y propagación de consultas**.

pueden ser redes persistentes establecen conexiones por defecto al iniciarse, manteniendo un número fijo de pares conectados, aunque no haya tráfico inmediato,  o  pueden ser más efímeras o específicas, solo conectan al necesitar consultar o propagar.

Normalmente, el programa ejecutado como servicio en el nodo, suele tener pre-configurados una lista de nodos conocidos a los que conectarse en el inicio. Estos nodos suelen estar siempre disponibles, son confiables y normalmente son nodos de los propios fundadores del protocolo. Son conocidos como [nodos bootstrap](https://en.wikipedia.org/wiki/Bootstrapping_node) y gracias a ellos, al ser un punto común de encuentro, un nodo, no solo puede conectarse a estos nodos, también puede descubrir al resto de nodos


protocolos de enrutamiento como kademlia


Proceso mediante el cual un nodo localiza y se conecta a otros nodos para integrarse y participar en la red P2P.

Hay varios modelos, principalmente:

* Basado en flooding (topología desestructurada): método donde un nodo envía un mensaje a todos sus vecinos, que lo reenvían a sus propios vecinos, y así sucesivamente, hasta alcanzar un límite ([TTL](https://es.wikipedia.org/wiki/Tiempo_de_vida_(inform%C3%A1tica))). Es simple pero genera mucho tráfico redundante..
* Tablas de enrutamiento (topología estructurada): como en [DHTs](https://es.wikipedia.org/wiki/Tabla_de_hash_distribuida), con nodos conocidos y organizados.



**Propagación de consultas**.

Proceso de difundir peticiones entre nodos para localizar información, es decir, un nodo recibe la pregunta y si no lo sabe, consulta a sus próximos nodos.

El descubrimiento entre nodos permite conocer a quién consultar, y la propagación usa ese conocimiento para difundir la petición. A veces, la propia consulta sirve para descubrir nodos.


En las redes p2p, existen mecanismos de descubrimiento y propagación de consultas y se puede decir que unos se ajustan mejor topología estructuradas y otros desestructuradas.

Como ejemplo, en las estructuradas podemos ver las siguientes



Donde vemos:

* Distributed Hash Table, DHT (Tabla Hash Distribuida): Asigna claves a nodos; permite localizar recursos eficientemente mediante hashing.
* ID-based Routing (Enrutamiento por ID): Envía consultas hacia nodos cuyo ID se aproxima al de la clave buscada.
* Neighbor Tables (Tablas de Vecinos): Cada nodo mantiene una lista estructurada de otros nodos para enrutar consultas.
* Logarithmic Search (Búsqueda Logarítmica): Reduce el número de saltos necesarios al buscar, típicamente `O(logN)`.
* Self-Maintenance (Auto-Mantenimiento): Los nodos actualizan sus tablas y rutas para adaptarse a cambios en la red.

En las desestructuradas:


* Flooding (Inundación): El nodo reenvía la consulta a todos sus vecinos. Alta cobertura, alto coste de ancho de banda.
* Gossip Protocol (Protocolo de Rumores): Cada nodo reenvía la consulta a un subconjunto aleatorio de vecinos. Menos tráfico, difusión probabilística.
* Random Walks (Búsqueda Aleatoria): La consulta se propaga siguiendo un camino aleatorio. Eficiente en tráfico, pero puede no encontrar el objetivo.
* Query Caching (Caché de Consultas): Los nodos guardan respuestas recientes. Evita búsquedas repetidas y acelera futuras consultas.
* Scoped Flooding (Inundación Acotada): Igual que Flooding, pero con TTL limitado. Controla el alcance y reduce la sobrecarga.

Mixtas:


* Supernodes, Supernodos (Hybrid P2P):
* Directory Servers (Servidores de directorio): Listan nodos activos desde un punto central.
* Caching of Queries (Caché de consultas): Guarda respuestas recientes para acelerar búsquedas.
* Rendezvous Nodes (Nodos de encuentro): Coordina conexiones entre pares dispersos.
* Clustered Overlays (Superposiciones en clústeres): Agrupa nodos en estructuras lógicas organizadas.

Y finalmente, híbridas con elementos centralizados como Napster Model, eDonkey Model, Kazaa Model...

**Como otras características**.


Bootstrap nodes son nodos conocidos y preconfigurados en una red P2P que ayudan a los nuevos nodos a descubrir y conectarse con el resto de la red.



funciona en capa de servicio TCP


