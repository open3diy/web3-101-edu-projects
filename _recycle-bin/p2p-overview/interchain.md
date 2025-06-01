# Introducción a redes peer to peer (p2p)

## Redes entre pares - peer-to-peer o p2p

### Redes interconectadas (interchain)

> Lo descarto porque esto es para blockchain, pero es contenido útil para cuando hable de ello..

Las redes interconectadas, también conocidas como *interchain* o *cross-chain*, son redes P2P independientes que pueden comunicarse y colaborar entre sí mediante protocolos de interoperabilidad. Cada red mantiene su propio dominio, reglas y protocolo, pero se habilitan mecanismos para transferir datos, activos o mensajes entre ellas de forma segura y confiable.

Estas conexiones suelen implementarse mediante puentes (*bridges*), protocolos de mensajería entre cadenas, o estándares comunes que permiten la interacción entre diferentes sistemas distribuidos. Ejemplos de tecnologías de interchain incluyen Cosmos (con su protocolo IBC), Polkadot (con parachains y relays), y soluciones de bridges entre Ethereum y otras cadenas.

La interoperabilidad entre redes permite ampliar la funcionalidad, compartir recursos y facilitar la colaboración entre ecosistemas previamente aislados, manteniendo la autonomía y seguridad de cada red participante.

<img src="assets/p2pInterchain.png" alt="p2pInterchain" width="350">

Como implementaciones habituales de interoperabilidad entre redes P2P se pueden encontrar:

* Atomic Swap, permite el intercambio directo de activos entre dos redes diferentes sin necesidad de intermediarios centralizados, garantizando que ambas partes cumplan las condiciones del intercambio o ninguna lo haga.
* IBC (Inter-Blockchain Communication Protocol), protocolo estándar utilizado principalmente en el ecosistema Cosmos para la transferencia segura de datos y activos entre blockchains independientes.
* Cross-Chain Messaging, soluciones que permiten enviar mensajes o datos entre diferentes cadenas, facilitando la coordinación y ejecución de operaciones entre redes separadas. Ejemplos incluyen protocolos como Polkadot XCM, LayerZero o Wormhole.