# Nueva capa de arquitectura de software: lógica de estado on-chain

La lógica de estado on-chain es una nueva capa donde los acuerdos se consolidan de forma inmutable y verificable. Sus atributos más relevantes son la transparencia, la resiliencia, propiedad y portabilidad de los datos por parte del usuario; sus principales trade-offs son coste, latencia y privacidad limitada.

Esto es posible gracias a una red descentralizada de nodos que alcanza consenso sobre el estado global, registrando cada transición en la estructura de datos que comúnmente se conoce como blockchain.

> Este concepto redefine la autoridad y la confianza en el software. Ya no se confía en un servidor, sino en una red que verifica, ejecuta y certifica acuerdos mediante código.

No toda la lógica debe vivir on-chain. El enfoque más pragmático es una arquitectura híbrida: la cadena gestiona validaciones críticas y estados finales, mientras la lógica sensible, los cálculos complejos y la UX permanecen off-chain. Para adoptar esta capa en una organización, lo razonable es avanzar con pilotos controlados, auditorías de contratos, gestión segura de claves y el uso de servicios [BaaS](https://observatorioblockchain.com/blockchain/que-es-blockchain-como-servicio-baas-y-cual-es-uso-empresarial/) cuando convenga.

Redes como Ethereum actúan como un gran ordenador distribuido, lento pero seguro. Las piezas de software que definen la lógica de esas transiciones son los smart contracts: el lugar donde se codifican las condiciones de un acuerdo. Son en esencia máquinas de estado distribuidas, donde toda transición del estado global es desencadenada por una transacción firmada por una cuenta externa ([EOA](https://www.binance.com/es/academy/glossary/externally-owned-account-eoa)). Los smart contracts encadenan esas transiciones como una secuencia de promesas; cada una puede validar condiciones, invocar otros contratos o revertir la operación completa si algo falla. Esta mecánica da lugar a la **lógica de estado on-chain** como nueva capa en la arquitectura de software.

Conviene aclarar una confusión frecuente: aunque la lógica del contrato se ejecuta de forma automática y determinista, los smart contracts no se inician solos. Siempre hay una transacción EOA en el origen, ya provenga de un usuario directamente o de una infraestructura off-chain que interactúa con la cadena.

## Comparación con la arquitectura tradicional

En una arquitectura clásica se distingue entre:

- Capa de presentación (UX/UI)
- Lógica de negocio (backend)
- Acceso a datos (repositorios o abstracciones)

La lógica de estado on-chain surge como una capa adicional que permite consolidar los acuerdos entre las partes con un nuevo estado consolidado. Sus principales características son:

- Transparencia y verificación: El código de los smart contracts, las transacciones y el estado final son públicos para cualquier participante de la red, permitiendo la replicación y verificación independiente de las condiciones y resultados.
- Auditabilidad: Todo cambio de estado queda registrado de forma inmutable, facilitando la trazabilidad y auditoría de las operaciones.
- Resiliencia: Al estar replicada entre múltiples nodos, la lógica on-chain no depende de una infraestructura central, aumentando la tolerancia a fallos y ataques evitando el punto único de fallo.
- Aprobación y propiedad de los datos: Los usuarios pueden aprobar la ejecución de contratos y elegir en cuáles confiar; además las transacciones y en consecuencia sus estados finales, están firmados por la clave privada del usuario, lo que le otorga la propiedad y potestad sobre ellos, permitiendo que puedan ser utilizados en otras aplicaciones o contratos de la red.

Quizás no debamos verlo como un lugar donde registrar toda la información, sobre todo por lo que implica en privacidad; es más bien un espacio donde reflejar un resumen o estado final que consolide el acuerdo entre las partes, es decir, **el registro contable de liquidaciones**. Este estado, además, pertenece al usuario y puede ser reutilizado por él, por ejemplo, para demostrar reputación, compartir información relevante o utilizar como token o llave (sea fungible o no) que le permita interactuar en otras aplicaciones de terceros o plataformas interoperables. Así, la capa on-chain actúa como un registro confiable y reutilizable de los aspectos más importantes del acuerdo, donde no debería exponerse datos sensibles, siendo sobre todo información de interoperabilidad.

## ¿Qué contiene esta lógica on-chain?

No debe albergar toda la lógica de negocio por razones de coste, latencia y privacidad, la lógica on-chain, por ejemplo, puede contener lo siguiente:

- Validación de condiciones críticas como acuerdos, votaciones o reglas de acceso.
- Definición de consecuencias en caso de cumplimiento o incumplimiento.
- Registro de evidencias verificables: desde compromisos criptográficos básicos hasta pruebas de conocimiento cero ([ZK proofs](https://ethereum.org/es/zero-knowledge-proofs/)) que permiten demostrar que una condición se cumple sin revelar los datos subyacentes.
- Registros contables tokenizados: representación on‑chain de activos fungibles (p. ej. ERC‑20) y no fungibles (p. ej. ERC‑721), que actúan como tokens, llaves o pruebas de propiedad y habilitan operaciones en aplicaciones de terceros dentro de la red.

## Hacia una arquitectura híbrida

No todo debe ejecutarse on-chain. Sería ineficiente y poco práctico. El enfoque más sano es aceptar que el futuro de los sistemas distribuidos es híbrido:

- Off-chain: cálculos complejos, lógica sensible, experiencia de usuario, privacidad.
- On-chain: validaciones críticas, pruebas de integridad, ejecución de acuerdos, estados que requieren consenso, información de interoperabilidad dentro de la red.

## Hablando claro al CTO

Para un [CTO](https://es.wikipedia.org/wiki/Director_de_tecnolog%C3%ADa) lo relevante no es la novedad técnica sino cómo mitigar riesgos y habilitar nuevas oportunidades de negocio donde la seguridad y la confianza sean fundamentales. La capa de estado on‑chain aporta beneficios concretos: inmutabilidad y auditabilidad de acuerdos, eliminación de puntos únicos de fallo, propiedad y portabilidad de datos por parte del usuario, y mecanismos verificables para reputación e interoperabilidad.

Sin embargo, es necesaria capacidad de adaptación. Existen proveedores y soluciones de blockchain‑as‑a‑service (p. ej. Alchemy) que facilitan el acceso a la red y la gestión operativa, y que pueden ayudar a optimizar costes como el gas; aun así, no eliminan retos clave como el desarrollo y auditoría de smart contracts, la gestión segura de claves, la integración de oráculos o la gobernanza de protocolos. Además, la experiencia de usuario se ve condicionada por la velocidad de confirmación de la red, por lo que suele ser necesario diseñar mecanismos de compensación (reintentos, UX asíncrona, estimación de costes) para mantener la usabilidad.

Más allá de la tecnología, el mayor freno suele ser que la empresa aún no tenga la cultura, los procesos ni las personas preparadas para trabajar en este modelo. Por eso es clave avanzar con pilotos controlados, auditorías y automatización operativa, integrando la descentralización de forma gradual mientras se educa y se genera conciencia interna. Al final, el gran reto es la seguridad, y la descentralización ha demostrado ser, por diseño, la respuesta más sólida para afrontarlo.

---
