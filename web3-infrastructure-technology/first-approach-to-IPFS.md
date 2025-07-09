# Primer acercamiento a IPFS: la red de contenido descentralizado

## TL;DR

IPFS (InterPlanetary File System, o Sistema de Archivos Interplanetario) es un sistema descentralizado para compartir contenido que también está descentralizado.

IPFS es un protocolo abierto, debidamente documentado que usa el modelo de datos [IPLD](https://docs.ipfs.tech/concepts/how-ipfs-works/#how-ipfs-represents-and-addresses-data) y además es un red pública p2p de nodos que siguen el protocolo.

🔗 Si quieres saber qué es IPFS y qué resuelve, accede al siguiente contenido de referencia:

* <https://docs.ipfs.tech/concepts/what-is-ipfs>.
* <https://docs.ipfs.tech/concepts/ipfs-solves>.

> Pero claro esta, a continuación veremos una explicación sobre IPFS, asi que continua leyendo.

## Ficha de la solución

El fundador es Protocol Labs <https://www.protocol.ai/>.

  > Protocol Labs también impulsa iniciativas relacionadas, como el laboratorio de innovación [Probelab](https://probelab.io/).

La web de IPFS: <https://ipfs.tech/>.

Es una solución [libre](https://es.wikipedia.org/wiki/Software_libre), de [código abierto](https://es.wikipedia.org/wiki/C%C3%B3digo_abierto) con [licencia MIT](https://es.wikipedia.org/wiki/Licencia_MIT) con repositorio en <https://github.com/ipfs>.

* Las propuestas de mejora se denominan `IPIP` (IPFS Improvement Proposal) <https://specs.ipfs.tech/meta/ipip-process/>.

El estándar y especificaciones están en <https://specs.ipfs.tech/>.

Como tipo de solución, IPFS se considera como [infraestructura](https://en.wikipedia.org/wiki/IT_infrastructure) del ecosistema Web3. Esto implica que, si quieres que el contenido exista y se mantenga en el tiempo, debes encargarte de alojarlo tú mismo o utilizar servicios de terceros que lo hagan, por lo tanto, debes considerar alguna de estas opciones:

* Subir el contenido en un cliente IPFS y usar la capa de incentivos [Filecoin](https://docs.ipfs.tech/concepts/faq/#ipfs-and-filecoin) para que el contenido siga siendo mantenido en el tiempo en una red descentralizada.
* Igualmente subir el contenido, pero fijarlo por un tercereo [Pinning Services](https://docs.ipfs.tech/how-to/work-with-pinning-services/#use-a-third-party-pinning-service), que es un servicio de fijado centralizado con las condiciones particulares de cada proveedor, a diferencia de Filecoin, que es una red descentralizada.
* Crear tus propia infraestructura y nodos de IPFS para almacenar contenido, preferiblemente gestionados mediante [IPFS Cluster](https://docs.ipfs.tech/install/server-infrastructure/).
* Usarlo como suele ser más conocido, mediante servicios SaaS como [Infura](https://www.infura.io/product/ipfs) o [Web3.Storage](https://web3.storage/).

## Casos de uso

Podemos resumir los principales casos de uso de IPFS en:

* Web descentralizada, el caso de uso más natural para IPFS, donde los sitios Web se sirven sin servidores centrales.
* Almacenamiento de archivos para dApps o smart contrats o servicios multimedia, etc.., considerando que el contenido es público por defecto y es necesario cifrar antes de subir si se requiere privacidad.
* Representación de datos de Ethereum usando el modelo IPLD, por ejemplo, el proyecto [go-ipld-eth-import](https://github.com/ipfs/go-ipld-eth-import) facilita la importación, permitiendo explorar la blockchain de Ethereum como un grafo de datos interconectados.

> Puedes comparar IPFS con otros sistemas con propósitos parecidos, tal como indica su web <https://docs.ipfs.tech/concepts/comparisons/#comparing-the-key-features-of-other-solutions-to-ipfs>.

## Descentralizando el contenido con IPLD

<img src="_first-approach-to-IPFS-attachments/assets/ipfsInterplanetary.png" alt="proceso" width="300">

IPFS se dice que es interplanetario porque permite distribuir la información a lo largo del planeta con su modelo IPLD (InterPlanetary Linked Data).

**IPLD el estándar de la estructura de datos**.

IPLD es la propuesta de Protocol Labs de un estándar de estructura de datos descentralizado.

🔗 <https://ipld.io/>.

En IPLD, cada contenido, como un archivo o directorio, es fragmentado (chunks) en diferentes bloques codificados, los cuales son identificados por su hash, llamado [CID](https://docs.ipfs.tech/concepts/content-addressing/#what-is-a-cid) (Content Identifier).

> ℹ️ *Una aclaración sobre la terminología*, un bloque es un conjunto de datos codificados almacenados como unidad mínima. Al deserializarlo, se interpreta como un nodo dentro del grafo de datos enlazados. Comúnmente nos referimos sobre lo mismo llamándolo bloque o nodo.

Por lo tanto, tenemos un contenido que se fragmenta en diferentes bloques o nodos, donde se parte uno raíz, con su CID, el cual enlaza con otros bloques hijos correspondientes, para reconstruir el contenido completo.

IPFS para fragmentar tiene en cuenta los objetos [UnixFS](https://docs.ipfs.tech/concepts/file-systems/#unix-file-system-unixfs), es decir, si el contenido es un archivo o directorio, es considerado como un nodo en sí, siendo un objeto UnixFs, que referencia a otros nodos intermedios o de datos.

Teniendo en cuenta esto, un mismo nodo con un CID puede estar referenciado en diferentes nodos padre, con el ejemplo más claro de dos directorios diferentes que tienen el mismo archivo, en ese caso, ocurre lo que se conoce como **deduplicación** y consigue evitar almacenar datos idénticos, ahorrando espacio y haciéndolo más eficiente.

Como podemos ver, el contenido se divide, porque así es más óptimo de replicar y distribuir, facilita la verificación, permite descarga paralela y además la deduplicación optimiza no repetir información y sobre todo es más descentralizado.

Este contenido dividido y organizado en nodos enlazados entre sí, la estructura que forma, es un árbol de Merkle y es acíclico dirigido, es decir, un DAG (Directed Acyclic Graph). por lo tanto, se dice que el modelo IPLD sigue el modelo Merkle-DAG.

* 🔗 <https://docs.ipfs.tech/concepts/merkle-dag/>

ℹ️ Para entender Merkle DAG, aquí tienes estas explicaciones con las que puedes practicar:

* [Jugando con DAG](../_misc/dag_playground.ipynb).
* [Jugando con árbol Merkle](../_misc/merkle_playground.ipynb).

🤔 Es confuso de entender que sea un árbol de Merkle y además DAG, cuando un árbol ya es en sí un tipo de DAG, esto es así por dos razones:

* Es un árbol de Merkle, sigue sus propiedades: tiene un nodo raíz, nodos intermedios que referencian a otros nodos, y cada CID se genera en función del contenido propio y los CIDs de los nodos referenciados (hijos), no de los padres.
* También se le llama DAG, como vimos en [jugando con DAG](../_misc/dag_playground.ipynb), porque se quiere enfatizar que un mismo nodo (como un nodo hoja) puede ser referenciado por múltiples padres, que es el caso de la deduplicación, por ejemplo cuando un archivo idéntico aparece en varias carpetas.

> 🛠️ Seguro que tanta explicación teórica no ayuda a entender nada, por eso, con la siguiente [práctica para entender IPLD](./_first-approach-to-IPFS-attachments/practice-understand-IPLD.md) podremos comprender todo mejor. Una vez hayas realizado la práctica, vuelve a leer de nuevo este apartado de "[Descentralizando el contenido con IPLD](#descentralizando-el-contenido-con-ipld)", verás como está más claro ahora.

## Fijando el contenido

IPFS da al usuario la potestad de elegir que contenido puede ser fijado en un nodo.

Desde cualquier cliente IPFS, puedes seleccionar un CID y fijarlo (pinning) para que el contenido asociado permanezca almacenado de forma permanente en tu nodo, evitando que sea eliminado por las políticas de caché o limpieza automática.

Si me permites la expresión, puede entenderse como un consenso no coordinado sobre el contenido que puede perdurar, que es a voluntad de cada usuario.
Esto refleja un modelo de persistencia por interés o utilidad, donde el “consenso” es resultado de decisiones autónomas, no de votación ni de consenso distribuido.

## La red de nodos p2p

IPFS es un protocolo para una red P2P diseñada para almacenar, compartir y localizar contenido de forma descentralizada. Puedes usarlo para crear tu propia red privada de nodos, pero también existe una red pública llamada `Amino DHT`, que se configura por defecto y cuyos otros nodos de la red se descubren al [iniciar el nodo](https://docs.ipfs.tech/concepts/public-utilities/#amino-dht-bootstrappers).

La red pública de nodos `Amino DHT` es monitorizada para asegurar su correcto funcionamiento por [ProbeLab](https://probelab.io/ipfs/amino/), una iniciativa impulsada por los fundadores de Protocol Labs.

IPFS es una red pública P2P que usa una adaptación de la DHT Kademlia.

> 🎓 Si quieres conocer más sobre redes P2P, puedes acceder a la siguiente [introducción](_misc/p2p_overview.md), donde intentaré despejar todas las dudas.

Como red pública, `Amino DHT` implementa el protocolo IPFS y se clasifica como una red de [autorización pública](_misc/p2p_overview.md#modelo-de-autorización), donde cualquier otro nodo puede participar sin restricciones, con un [modelo de gobernanza](_misc/p2p_overview.md#modelo-de-gobernanza) descentralizado y abierto, aunque Protocol Labs (<https://www.protocol.ai/>) tiene un papel relevante en la evolución del protocolo.

Es una red [clasificada](_misc/p2p_overview.md#clasificación-principal-de-redes-p2p) como estructurada, basada en DHT (Kademlia), para un [modelo de confianza](_misc/p2p_overview.md#modelo-de-confianza) trustless, donde los nodos no necesitan confiar entre sí, ya que la integridad y autenticidad del contenido se verifica mediante el CID (Content Identifier).

Es una red con un [grado de descentralización](_misc/p2p_overview.md#grado-de-descentralización) totalmente descentralizada, que usa una [estrategia de almacenamiento](_misc/p2p_overview.md#estrategias-de-almacenamiento-en-redes-p2p) distribuido donde la [replicación](_misc/p2p_overview.md#técnicas-de-replicación) es parcial, lo que significa que no todos los nodos almacenan todos los datos, sino solo aquellos que se solicitan o se elige mantener (pinning), optimizando así el uso de recursos. El [modelo de consistencia](_misc/p2p_overview.md#modelos-de-consistencia) es eventual, es decir, los cambios se propagan gradualmente y, tras cierto tiempo, todos los nodos alcanzan el mismo estado; además, ofrece [consistencia](_misc/p2p_overview.md#modelos-de-consistencia) de lectura tras escritura, lo que garantiza que un nodo que escribe un dato podrá leer inmediatamente esa versión, aunque otros nodos puedan tardar en verla.

**IPFS es una adaptación de Kademlia** porque introduce varias diferencias clave para priorizar disponibilidad y flexibilidad:

En Kademlia, un contenido se almacena únicamente en los nodos más cercanos a su clave (como se explica en [resumen de redes P2P](_misc/p2p_overview.md)), lo que implica que el nodo que origina el contenido no lo almacena. En cambio, en IPFS, gracias al mecanismo de pinning, el nodo que crea y conserva el contenido puede anunciarlo (mediante comando `Provide`), comunicando su dirección ([multiaddr](https://richardschneider.github.io/net-ipfs-core/articles/multiaddress.html)) a los nodos más cercanos al CID. Esto representa una diferencia clave respecto al modelo STORE clásico de Kademlia.

En Kademlia clásico el dato se replica automáticamente con una persistencia garantizada (mientras haya al menos un nodo activo), pero en IPFS solo se anuncia la ubicación del dato y si el origen lo borra, se pierde (a menos que otro nodo lo haya guardado explícitamente).

Tenemos que considerar que el mecanismo de pinning cobra especial importancia: asegura que un nodo retenga localmente un bloque específico, impidiendo que sea eliminado por políticas de caché o recolección.

  > El pinning convierte a un nodo en un proveedor fiable del contenido, garantizando su permanencia en la red. Sin pinning, los anuncios pueden volverse inconsistentes o efímeros.



## Los principios de IPFS

Si has llegado hasta aquí...como resumen, podemos extraer los siguientes principios en IPFS.

Con su modelo de datos IPLD nos ofrece:

* División del contenido, siguiendo el modelo Merkle DAG, para permitir almacenamiento distribuido, facilitando verificación, descargas paralelas y deduplicación.
* La identificación del contenido por su CID basado en su [hash](https://docs.ipfs.tech/concepts/hashing/) en lugar de su ubicación como una URL, asegura la [inmutabilidad](https://docs.ipfs.tech/concepts/immutability/) del contenido.
* Se da la potestad a la demanda y al usuario la disponibilidad del contenido.

ℹ️ Para entender Merkle DAG,
  > ipfs_cid_playground.ipynb

Como solución técnica, IPFS es:

* Una suite modular de protocolos abiertos como lip2p y bitswap.
* Red de [nodos](https://docs.ipfs.tech/concepts/nodes/#nodes) p2p con una [DHT](https://docs.ipfs.tech/concepts/dht/) que implementa el algoritmo Kademlia para una búsqueda o lookup de contenido eficiente basado en su CID.

## Seguridad del contenido

Estas son las medidas que se suelen aplicar en la red de IPFS respecto a la seguridad del contenido:

* Listas de bloqueo coordinadas: Algunos nodos y gateways colaboran para mantener listas de CID maliciosos como <https://badbits.dwebops.pub/>.

* Responsabilidad del usuario: Si se usa IPFS como red, los usuarios deben cifrar datos sensibles y utilizar software antivirus para escanear archivos descargados.

> Pero IPFS como protocolo, puede ser usado en cualquier red privada o con el control de acceso deseado, simplemente deberás crear tú propia red y usar cualquiera implementación disponibles.

## Las implementaciones de IPFS

Una implementación es el software que ejecuta el protocolo IPFS.

Todas las implementaciones de IPFS puedes verlas en <https://docs.ipfs.tech/concepts/ipfs-implementations/#popular-node-implementations-and-tools>.

Cuando inicias una implementación, se usan la lista de nodos [bootstrap](https://docs.ipfs.tech/how-to/modify-bootstrap-list) ya configurados por defecto por Protocol Labs/IPFS Foundation, accediendo a la red pública `Amino DHT`.

> Si quieres crear tú propia red, deberás crear una lista diferente de nodos bootstrap.

El uso inicial más fácil de IPFS es mediante la aplicación de escritorio [IPFS Desktop](https://docs.ipfs.tech/install/ipfs-desktop/), pero tenemos que entender que esto es solo la interfaz gráfica que incluye, aquí sí, la implementación del CLI [Kubo-IPFS](https://docs.ipfs.tech/install/command-line/#install-ipfs-kubo).

## Práctica de IPFS usando IPFS Desktop

En primer lugar, aprovecho para comentarte que puedes ir a las pruebas de laboratorio de IPFS de [open3diy.org sobre web3-101](https://github.com/open3diy/web3-101/blob/main/IPFS/README.md). Ahí verás cómo configurar `IPFS Dektop`, si tienes problemas para acceder al contenido en internet por estar detrás de un CGNAT.
