Claro, te explico paso a paso de forma clara y sin tecnicismos innecesarios:

    Cada nodo en Kademlia tiene un ID, como si fuera un número binario largo (por ejemplo: 101011...).

    En su tabla de rutas (routing table) guarda otros nodos, pero no todos mezclados, sino organizados en grupos llamados "buckets".

    Cada bucket representa nodos que están a una distancia determinada del tuyo. Esa distancia se mide por el primer bit donde los ID difieren.

    Cuando quieres encontrar un hash objetivo (por ejemplo: 0001...), Kademlia mira en qué bucket caería ese hash, basándose en cuán diferente es ese hash de tu propio ID.

    Una vez sabe el bucket, busca ahí los nodos que ya conoce y calcula cuál está más cerca del hash que buscas.

    Si ese bucket no tiene nodos suficientes, va probando con los buckets de al lado (más cercanos o más lejanos).


    Cuando un nodo anuncia su existencia (por ejemplo, al publicar una clave o participar en el DHT), otros nodos pueden almacenar su Peer ID y multiaddrs temporalmente en caché local.

    sí la guarda, pero no como un STORE tradicional, sino como efecto colateral de ADD_PROVIDER. con ttl 10 min


    La DHT con ttl, esencial para la escalabilidad y resilencia.
    Se guarda routing table volaltir por el hecho de que el nodo se apague o no entre como nodo mas cercano