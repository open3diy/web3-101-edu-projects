# Sistemas centralizados y descentralizados

> También puedes este contenido en [el vídeo del canal proyectos web3](https://www.youtube.com/watch?v=KegmopgGi8M).

En un sistema descentralizado, como puede ser uan red p2p, los nodos están normalmente distribuidos y todo esto puede confundirnos con un sistema centralizado y distribuido que no tiene nada que ver.

Por eso, lo mejor es ver un pequeño ejemplo.

## El sistema centralizado

<img src="./assets_1_2/sistemaCentralizado.gif" alt="sistemaCentralizado" width="600">

Primero veremos un sistema centralizado, el cual depende de una autoridad central, donde los usuarios pueden interactuar.

Por ejemplo, en un sistema de pagos, Ana puede enviar 5 dólares a Pedro y la autoridad central verá que todo es correcto.

En ese momento Pedro podrá consultar su saldo de 5 dólares.

## Fallo del sistema centralizado

<img src="./assets_1_2/SC-Escalabilidad.gif" alt="SC-Escalabilidad" width="600">

Pero este sistema no escala muy bien, la demanda de los usuarios o los ataques maliciosos podrían saturar el servicio.

## Escalabildiad de los sistemas centralizados

<img src="./assets_1_2/Nube-distribuida.gif" alt="nubeDistribuida" width="600">

Así que este sistema centralizado puede ser distribuido, pero la distribución es para escalar mejor, por ejemplo una "nube distribuida" puede tener varios nodos y ofrecer un servicio geolocalizado a sus usuarios.
Es centralizado y distribuido, donde los diferentes nodos necesitan coordinarse y actualizar su estado con la autoridad central.

En esta ocasión, cuando Ana envía 5 dólares, usa uno de los nodos delegados más próximos.

En ese momento el nodo delegado avisa a la autoridad central sobre el pago a Pedro.

Y la autoridad central y el resto de nodos delegados se sincronizan, con el nuevo estado de saldo de 5 dólares de Pedro.

Finalmente, Pedro puede consultar su nuevo saldo de 5 dólares usando uno de los nodos que tiene más cercano.

## Sistema descentralizado

<img src="./assets_1_2/protocoloSD.gif" alt="protocoloSD" width="600">

Un sistema descentralizado no tiene una autoridad central, no existen decisiones únicas, existe un protocolo predefinido que los nodos tienen que seguir.

Normalmente, los nodos forman una red entre pares, es decir, una red P2P, donde cada nodo tiene la lista de los otros nodos con los que se relaciona y así sucesivamente para crear una red de propagación de información.

La distribución de los nodos en este caso es para asegurar la descentralización, evitar el punto único de fallar y no tanto para poder escalar. Aunque se consigue más resilencia, tener que esperara a que los nodos lleguen a un consenso, es un proceso menos inmediato.

> Aunque lo cierto es que los sistemas distribuidos actuales trabajan duro para dar una experiencia de transacciones en tiempo real.

---

<img src="./assets_1_2/SD-p2p.gif" alt="SD-p2p" width="600">

Entonces...cuando Ana envía 5 dólares, podrá usar cualquier nodo, quizás sea un nodo que ha creado ella misma.

Seguidamente, cada nodo propaga esa información a la lista de nodos que conoce, indicando que Pedro tiene 5 dólares.

---

### El consenso

<img src="./assets_1_2/SD-consenso.gif" alt="SD-p2p" width="600">

*Normalmente y según el protocolo*, cada nodo, de forma coordinada, se toma un tiempo para recibir suficientes operaciones, validarlas e iniciar el consenso de la red para el ciclo.

* Como llegar a un acuerdo entre los nodos cuesta un tiempo, es común que se acumulen las operaciones en tandas, de está forma es más eficiente. Por ejemplo, el consenso no se inicia solo cuando Ana realiza una operación, se espera a que varias personas hagan más pagos, asi es mas eficiente.
  * Este consenso es cíclico, se repite tantas veces sea necesario al existir nuevas operaciones que requieran volver a llegar a un nuevo consenso.

* En el consenso, cada nodo participante tiene que validar las operaciones y luego debe crear una evidencia para que el resto de nodos lo consideren confiable, de esta forma la red puede llegar a un acuerdo.

  * Por ejemplo, la evidencia que debe generar el nodo puede ser algo que demuestre su autoridad o un trabajo realizado o si demuestra que tiene algo que perder...esto se ve en detalle con [PoA](https://academy.bit2me.com/que-es-proof-of-authority-poa/), [PoW](https://academy.bit2me.com/que-es-proof-of-work-pow/) o [PoS](https://academy.bit2me.com/que-es-proof-of-stake-pos/).

* El acuerdo sobre el estado único, se establece según determine la mayoría o tengo mayor peso o exista mayor confianza. Por ejemplo, 3 nodos de 4 han acordado que en efecto Ana dispone 5 dólares para poder ser enviados a Pedro y así lo reflejan en un libro contable.

> Esto es una generalización, cada protocolo es complejo de entender y tiene sus particularidades.

<img src="./assets_1_2/SD-AcuerdodePago.gif" alt="SD-elAcuerdo" width="600">

Finalmente Pedro, si accede a un nodo y consulta, puede confirmar que tiene 5 dólares, porque los nodos así llegaron a ese acuerdo siguiendo el protocolo, no porque ninguna autoridad central lo haya decidido.

---

Este ejemplo puede ser algo abstracto y es posible que no terminemos de comprendedlo, pero sirve para tener una primera introducción sobre los sistemas descentralizados, y además ver la diferencia con uno centralizado sea o no distribuido.

> La clave del sistema descentralizado está en que no necesita una **autoridad** central, ya que es el **protocolo** el que lo determina.

Con esta explicación deberíamos despejar la duda sobre si un sistema descentralizado escala mejor, y lo cierto es que escala mejor en resilencia, disponibilidad y resistencia a la censura, pero no es tan inmediato como un sistema centralizado y distribuido.

Con el tiempo intentaremos profundizar en esta mecánica con modelos descentralizados concretos y veremos como la criptografía es fundamental, mientras tanto, espero que esta explicación les ayude...
