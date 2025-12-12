# Acerca de

La infraestructura web3 que son piezas componibles, puede parecer que todos son “servicio”, pero estos se reserva para aquello que facilitan su uso, normalmente mediante una API, automatización o alguna abstracción.

Quien ofrece ese servicio suele aportar valor adicional y, a cambio, existe una contraparte (suscripción, pago por uso, fees, etc.). Por eso, lo normal es que sea necesario acceder a una web previamente, registrarte, pagar una suscripción y obtener un API key.

*¿Participar en una red de nodos es un servicio?*

No.
Participar ejecutando un nodo es infraestructura, no un servicio Web3. Es simplemente un rol dentro de la red: validación, consenso, propagación o almacenamiento.

Solo se convierte en “servicio” cuando alguien usa tu nodo o infraestructura como producto, por ejemplo: acceso RPC, pinning, automatización, relaying, etc.

*¿Usar una librería es un servicio?*

Tampoco.
Una librería es una pieza standalone, técnica, que se integra en otra infraestructura o en una DApp. No ofrece un servicio autónomo a terceros. Para ser servicio, debe proporcionar una funcionalidad completa directamente utilizable por otros, no simplemente formar parte de una cadena de construcción.

*¿Usar una pool de liquidez DeFi es un servicio?*

Es cierto que las pools de liquidez cumplen una función importante en el ecosistema, ya que permiten la existencia de un mercado secundario para un proyecto. Sin embargo, también están disponibles para un público más general, como los inversores, y no requieren necesariamente un contexto específico para su uso. Por ejemplo, una DApp consolidada como Safe, utilizada para la gestión de tesorería, ofrece un servicio claro y dirigido principalmente a DAOs y sus aplicaciones; fuera de ese contexto, su uso pierde sentido. En cambio, en una DApp DeFi de pool de liquidez, cualquier usuario puede participar sin necesidad de un contexto previo o especializado.

Existen servicios de muchos tipos y la comunidad ya los ha catalogado:

**Servicios tipo SaaS**:

Cuando envuelven a otra red descentralizada, que siguen una filosofía SaaS, se les conoce como los -as-a-service, siendo una capa, un tercero que te facilita ese acceso principalmente via API principalmente, pero también con UI. Ejemplos claros: RPC-as-a-service, Indexing-as-a-service, Storage-as-a-service, Automation-as-a-service.

Puedes empezar en [Servicios SaaS 101](SaaS-services-101.md).

**Servicio descentralizado**:

En otros casos, son servicios o, mejor dicho, capas descentralizadas sobre una infraestructura de red de nodos. Esto puede resultar confuso de entender. Por ejemplo, Filecoin como capa de almacenamiento descentralizada tiene un mecanismo de fees que puede hacer pensar que es infraestructura pura, pero el matiz es claro: no participas en la red, simplemente haces uso de ella porque necesitas una funcionalidad específica. Ese matiz es importante.

Igualmente, existen servicios creados desde cero con los principios de la descentralización, donde hay una red de nodos que deben realizar validaciones para llegar a un consenso. En esos casos también se consideran servicios descentralizados.

Puedes empezar en [Servicios descentralizados 101](decentralized-services-101.md).

**Servicios off-chain**:

Son los servicios habituales que pueden usarse en cualquier proyecto y desarrollo. Lo normal es que sean centralizados, aunque en algunos casos adoptan principios de descentralización. Muchos cubren necesidades básicas como GitHub o Discord, siendo estándares de facto en muchos casos, o simplemente la mejor o única solución disponible.

Puedes empezar en [Servicios off-chain 101](off-chain-services-101.md).

**DApp considerada como plataforma de amplio uso**:

Aquí, igualmente, se puede decir que son aplicaciones externas que ofrecen un servicio desde el punto de vista del creador de una aplicación, MVP o DApp. Son aquellas con un enfoque más B2B, que realmente parecen contribuir a un ecosistema. Es cierto que existe una línea gris al respecto, pero son servicios que casi se consideran estándar de facto y que aportan al ecosistema de un creador de una DApp.

En muchos casos se accede a una URL centralizada y pueden parecer una aplicación más, pero ya sabemos que en Web3 cualquier aplicación que use elementos descentralizados como smart contracts, sobre todo si se gestiona con una DAO y tokens, se considera DApp.

Puedes empezar en [DApps como servicio 101](DApp-services-101.md).

## Validación comunitaria

Este marco coincide en parte con la forma en que la comunidad Web3 suele analizar estos conceptos. No es una definición formal universal, pero sí un consenso operativo ampliamente aceptado. Hay que considerar, sobre todo, que esta agrupación es simplemente una división funcional para este repositorio, de modo que cualquiera que quiera emprender pueda navegar por áreas claras respecto a elementos que se consideran servicio y pueden usarse como tal.

## ¿Por qué esta clasificación?

Lo cierto es que se podría clasificar por categorías, no tanto por su arquitectura. Es verdad, en lugar de clasificar por almacenamiento, tareas o índice, etc...se clasifica si es centralizado o no, o si se ofrece como servicio. Pero esto no es casual: esto demuestra la gran importancia que le da el ecosistema a la descentralización. Puede ser algo clasista, pero la diferencia entre un servicio descentralizado y uno SaaS tiene implicaciones muy diferentes en resiliencia y sostenibilidad.

---
