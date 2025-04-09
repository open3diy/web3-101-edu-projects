# Primer acercamiento a IPFS: la red de contenido descentralizado

IPFS (InterPlanetary File System, o Sistema de Archivos Interplanetario) es un sistema descentralizado para compartir contenido que también está descentralizado.

IPFS es un protocolo abierto, debidamente documentado que usa el modelo de datos [IPLD](https://docs.ipfs.tech/concepts/how-ipfs-works/#how-ipfs-represents-and-addresses-data) y además es un red pública p2p de nodos que siguen el protocolo.

🔗 Si quieres saber qué es IPFS y qué resuelve, accede al siguiente contenido de referencia:

* <https://docs.ipfs.tech/concepts/what-is-ipfs>.
* <https://docs.ipfs.tech/concepts/ipfs-solves>.

## Ficha de la solución

El fundador es Protocol Labs <https://www.protocol.ai/>.

Su web <https://ipfs.tech/>.

Es una solución [libre](https://es.wikipedia.org/wiki/Software_libre), de [código abierto](https://es.wikipedia.org/wiki/C%C3%B3digo_abierto) con [licencia MIT](https://es.wikipedia.org/wiki/Licencia_MIT) con repositorio en <https://github.com/ipfs>.

* Las propuestas de mejora se denominan `IPIP` (IPFS Improvement Proposal) <https://specs.ipfs.tech/meta/ipip-process/>.

El estándar y especificaciones están en <https://specs.ipfs.tech/>.

Como tipo de solución, IPFS se considera más como [infraestructura](https://en.wikipedia.org/wiki/IT_infrastructure) del ecosistema de la Web3, por lo que si quieres que el contenido exista y se mantengan en el tiempo, debes considerar alguna de estas opciones:

* Subir el contenido en un cliente y usar la capa de incentivos [Filecoin](https://docs.ipfs.tech/concepts/faq/#ipfs-and-filecoin) para que el contenido siga siendo mantenido en el tiempo por un tercero en una red descentralizada.
* Igualmente subir el contenido, pero fijarlo por un tercereo [Pinning Services](https://docs.ipfs.tech/how-to/work-with-pinning-services/#use-a-third-party-pinning-service), que es un servicio de fijado centralizado con las condiciones particulares de cada proveedor, a diferencia de filecoin, que es una red descentralizada.
* Crear tus propia infraestructura y nodos de IPFS para almacenar contenido, preferiblemente gestionados mediante [IPFS Cluster](https://docs.ipfs.tech/install/server-infrastructure/).
* Usarlo como suele ser más conocido, mediante servicios SaaS como [Infura](https://www.infura.io/product/ipfs) o [Web3.Storage](https://web3.storage/).

## Casos de uso

Podemos resumir los principales casos de uso de IPFS en:

* Web descentralizada, el caso de uso más natural para IPFS, donde los sitios se sirven sin servidores centrales.
* Almacenamiento de archivos servidos para apps o smart contrats o servicios multimedia, etc.., considerando que el contenido es público por defecto, es necesario cifrar antes de subir si se requiere privacidad.
* Representación de datos de Ethereum usando el modelo IPLD, por ejemplo, el proyecto [go-ipld-eth-import](https://github.com/ipfs/go-ipld-eth-import?utm_source=chatgpt.com) facilita la importación permitiendo explorar la blockchain de Ethereum como un grafo de datos interconectados.

Puedes comparar IPFS con otros sistemas con propósitos parecidos, tal como indica su web <https://docs.ipfs.tech/concepts/comparisons/#comparing-the-key-features-of-other-solutions-to-ipfs>.

---

## Descentralizando el contenido con IPLD

<img src="./assets/ipfsInterplanetary.png" alt="proceso" width="300">

IPFS se dice que es interplanetario porque permite distribuir la información a lo largo del planeta con su modelo IPLD (InterPlanetary Linked Data).

**IPLD el estándar para la estructura de datos**.

IPLD es la propuesta de Protocol Labs de un estándar de estructura de datos descentralizado.

🔗 <https://ipld.io/>.

En IPLD, cada contenido, como un archivo o directorio, es fragmentado (chunks) en diferentes bloques codificados, los cuales son identificados por su hash, llamado [CID](https://docs.ipfs.tech/concepts/content-addressing/#what-is-a-cid) (Content Identifier).

> ℹ️ *Una aclaración sobre la terminología*, un bloque es un conjunto de datos codificados almacenados como unidad mínima. Al deserializarlo, se interpreta como un nodo dentro del grafo de datos enlazados. Comúnmente nos referimos sobre lo mismo llamándolo bloque o nodo.

Por lo tanto, tenemos un contenido que se fragmenta en diferentes bloques o nodos, donde se parte uno raíz, con su CID, el cual enlaza con otros bloques hijos correspondientes, para reconstruir el contenido completo.

IPFS para fragmentar tiene en cuenta los objetos [UnixFS](https://docs.ipfs.tech/concepts/file-systems/#unix-file-system-unixfs), es decir, si el contenido es un archivo o directorio, es considerado como un nodo en sí, siendo un objeto UnixFs, que referencia a otros nodos intermedios o de datos.

Teniendo en cuenta esto, un mismo nodo con un CID puede estar referenciado en diferentes nodos padre, con el ejemplo más claro de dos directorios diferentes que tienen el mismo archivo, en ese caso, ocurre lo que se conoce como deduplicación y se consigue evitar almacenar datos idénticos ahorrando espacio y haciéndolo más eficiente.

Como podemos ver, el contenido se divide, porque así es más óptimo de replicar y distribuir, facilita la verificación, permite descarga paralela y además la deduplicación optimiza no repetir información y sobre todo es más descentralizado.

Este contenido dividido y organizado en nodos enlazados entre sí, la estructura que forma, es un árbol de Merkle y es acíclico dirigido, es decir, un DAG (Directed Acyclic Graph). por lo tanto, se dice que el modelo IPLD sigue el modelo Merkle-DAG.

* 🔗 <https://docs.ipfs.tech/concepts/merkle-dag/>

ℹ️ Para entender Merkle DAG, aquí tienes estas explicaciones con las que puedes iniciar:

* [Jugando con DAG](../_misc/dag_playground.ipynb).
* [Jugando con árbol Merkle](../_misc/merkle_playground.ipynb).

🤔 Es confuso de entender que sea un árbol de Merkle y además DAG, cuando un árbol ya es en sí un tipo de DAG, esto es así por dos razones:

* Es un árbol de Merkle, sigue sus propiedades: tiene un nodo raíz, nodos intermedios que referencian a otros nodos, y cada CID se genera en función del contenido propio y los CIDs referenciados.
* También se le llama DAG, como vimos en [jugando con DAG](../_misc/dag_playground.ipynb), porque se quiere enfatizar que un mismo nodo (como un nodo hoja) puede ser referenciado por múltiples padres, que es el caso de la deduplicación, por ejemplo cuando un archivo idéntico aparece en varias carpetas.

> 🛠️ Seguro que tanta explicación teórica no ayuda a entender nada, por eso, con la siguiente [práctica para entender IPLD](./_first-approach-to-IPFS-attachments/practice-understand-IPLD.md) podremos comprender todo mejor. Una vez hayas realizado la práctica, vuelve a leer de nuevo este apartado de "[Descentralizando el contenido con IPLD](#descentralizando-el-contenido-con-ipld)", verás como está más claro ahora.

## La red de nodos p2p

el almacenamiento y localización de contenido se basan en nodos distribuidos mediante una tabla hash distribuida (DHT). Todo el contenido se almacena en nodos, sin necesidad de un mecanismo de consenso o blockchain para registrar información. IPFS es una red peer-to-peer descentralizada pero no es una blockchain.

IPFS es una red P2P (peer-to-peer) de nodos diseñada para almacenar, compartir y localizar contenido de forma descentralizada.

no broadcast total, sino estilo IPFS: solicitud -> transferencia

> Ejemplo práctica de propagación de contenido

## Los principios de IPFS

Si has llegado hasta aquí...como resumen, podemos extraer los siguientes principios en IPFS.

Con su modelo de datos IPLD nos ofrece:

* División del contenido, siguiendo el modelo Merkle DAG, para permitir almacenamiento distribuido, facilitando verificación, descargas paralelas y deduplicación.

* La identificación del contenido por su CID basado en su [hash](https://docs.ipfs.tech/concepts/hashing/) en lugar de su ubicación como una URL, asegura la [inmutabilidad](https://docs.ipfs.tech/concepts/immutability/) del contenido.

Como solución técnica, IPFS es:

* Una suite modular de protocolos abiertos como lip2p y bitswap.
* Red de [nodos](https://docs.ipfs.tech/concepts/nodes/#nodes) p2p con una [DHT](https://docs.ipfs.tech/concepts/dht/) que implementa el algoritmo Kademlia para una búsqueda o lookup de contenido eficiente basado en su CID.

## Seguridad del contenido

Estas son las medidas que se suelen aplicar en la red de IPFS respecto a la seguridad del contenido:

* Listas de bloqueo coordinadas: Algunos nodos y gateways colaboran para mantener listas de CID maliciosos como <https://badbits.dwebops.pub/>.

* Responsabilidad del usuario: Si se usa IPFS como red, los usuarios deben cifrar datos sensibles y utilizar software antivirus para escanear archivos descargados.

> Pero IPFS como protocolo, puede ser usado en cualquier red privada o con el control de acceso deseado, simplemente deberás crear tú propia red y usar cualquiera implementación disponibles.

## Las implementaciones de IPFS

Una implementación es un software que ejecuta el protocolo IPFS completo, manejando directamente bloques, CIDs, red P2P y almacenamiento.

Todas las implementaciones de IPFS puedes verlas en <https://docs.ipfs.tech/concepts/ipfs-implementations/#popular-node-implementations-and-tools>.

Cuando inicias una implementación, se usan la lista de nodos [bootstrap](https://docs.ipfs.tech/how-to/modify-bootstrap-list), es decir, la lista de nodos conocidos y confiables de protocol lab, que te conectan a la red p2p interplanetaria de IPFS, llamada `Amino DHT`.

> Si quieres crear tú propia red, deberás crear una lista diferente de nodos bootstrap.

Cuando empezamos a usar IPFS, inicialmente usaremos la aplicación de escritorio [IPFS Desktop](https://docs.ipfs.tech/install/ipfs-desktop/), pero tenemos que entender que esto es solo la interfaz gráfica que incluye, aquí sí, la implementación del CLI [Kubo-IPFS](https://docs.ipfs.tech/install/command-line/#install-ipfs-kubo).

## Práctica de IPFS usando IPFS Desktop

En primer lugar, aprovecho para comentarte que puedes ir a las pruebas de laboratorio de IPFS de [open3diy.org sobre web3-101](https://github.com/open3diy/web3-101/blob/main/IPFS/README.md). Ahí verás cómo configurar `IPFS Dektop`, si tienes problemas para acceder al contenido en internet por estar detrás de un CGNAT.
