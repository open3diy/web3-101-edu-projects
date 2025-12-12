# Nueva capa de arquitectura de software: lógica de estado on-chain

La lógica de estado on‑chain es una nueva capa donde los smart contracts consolidan acuerdos y registran transacciones de forma replicada, transparente e inmutable. Se ejecutan por transacciones iniciadas por cuentas externas y aportan transparencia, auditabilidad, resiliencia y propiedad/portabilidad de datos; sus principales trade‑offs son coste, latencia y privacidad. No toda la lógica debe moverse on‑chain: diseñar una arquitectura híbrida (on‑chain para validaciones críticas y estados finales; off‑chain para cálculos, UX y datos sensibles). Para adoptar esta capa en una empresa: avanzar con pilotos controlados, auditorías, gestión segura de claves y uso de servicios BaaS cuando convenga.

Con el surgimiento de los smart contracts, se introduce una nueva abstracción en el diseño de sistemas: una capa lógica dedicada a la gestión de acuerdos entre partes. En esta capa, las transacciones se registran y su estado final queda disponible para ser consultado y verificado, aportando transparencia y confianza en el proceso.

> Este nuevo concepto redefine la autoridad y confianza en el software. Ya no se confía en un servidor, sino en una red que verifica, ejecuta y certifica acuerdos mediante código.

Un smart contract es el lugar donde se codifican las condiciones que debe cumplir un acuerdo. Para una transacción dada, puede ejecutarse automáticamente uno o varios smart contracts, considerados como una secuencia de promesas que deben confirmarse. Desde un punto de vista técnico, un contrato puede recibir una transacción, validar condiciones, revertir la transacción o invocar otro contrato, todo de forma automática según la lógica implementada. Si alguna condición no se cumple, el contrato puede revertir la operación o seguir flujos alternativos definidos en el código.

Estas condiciones se ejecutan automáticamente y es importante aclarar una confusión común: las condiciones se ejecutan automáticamente, pero los smart contracts no se inician por sí solos. Su ejecución surge de una transacción, originada por una cuenta externa (EOA). La lógica interna del contrato se ejecuta de forma determinista, pero el inicio siempre viene dado, ya sea de un usuario o de una infraestructura off-chain que interactúa con la cadena.

Esta lógica basada en promesas y condiciones consensuadas introduce una nueva capa en la arquitectura de software: la **lógica de estado on-chain**. A diferencia de la lógica de negocio tradicional, que suele residir en un backend centralizado, esta capa opera sobre una red de nodos descentralizados que deben alcanzar consenso sobre la ejecución y el estado único de cada transacción. Esto aporta mayor seguridad y resiliencia, superando las limitaciones de las arquitecturas convencionales. El principal trade-off es una menor velocidad y el hecho de que las transacciones son inmutables y públicas; aunque existe seudoanonimato, la privacidad real es limitada.

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
- Registro inmutable de eventos o evidencias como hashes, firmas o marcas de tiempo.
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
