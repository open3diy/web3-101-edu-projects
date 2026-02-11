# Mejores prácticas en VC y Attestations

## La importancia crítica de confiar en el emisor

Determinar si debes confiar en el emisor de un VC o atestación está es quizás el aspecto más importante y a menudo malentendido de las credenciales verificables.

La criptografía garantiza que la universidad con DID `did:ethr:0x123...` emitió tu diploma, pero no puede decirte si esa entidad realmente es Stanford University o un impostor. La tecnología verifica la firma, pero tú como verificador debes decidir si confías en la reputación y autoridad del emisor para hacer esas afirmaciones. Un diploma firmado por una universidad prestigiosa tiene valor porque confías en su proceso de evaluación académica; el mismo diploma firmado por una entidad desconocida no tiene peso, aunque técnicamente ambas credenciales sean válidas criptográficamente.

En la práctica, la confianza en emisores se construye mediante varios mecanismos que operan en capas superiores. Algunos ecosistemas mantienen registries on-chain de emisores autorizados gobernados por DAOs. Otros confían en la reputación acumulada y el reconocimiento social del emisor. Proyectos empresariales pueden establecer trust frameworks donde organizaciones participantes acuerdan mutuamente reconocer sus credenciales. Plataformas de análisis blockchain pueden construir scores de reputación basados en el historial de emisión.

La descentralización significa que no existe una autoridad central que certifique emisores globalmente, lo cual es intencional por diseño. Cada contexto define sus propios criterios de confianza. Una DAO puede aceptar credenciales de ciertos emisores para membresía, mientras otra DAO rechaza esos mismos emisores pero confía en otros diferentes. Esta flexibilidad contextual es poderosa pero requiere que verificadores hagan su diligencia debida sobre qué emisores aceptan.

## Diseño correcto: semántica temporal de para attestations y VCs

Un aspecto crucial que aplica tanto a Verifiable Credentials como a attestations on-chain es la semántica temporal de las afirmaciones. Muchos malentienden que firmar digitalmente una credencial o registrarla permanentemente en blockchain garantiza su validez perpetua. En realidad, solo certifica que esa afirmación específica fue hecha en un momento determinado por un emisor verificable. Si tu empleador emite una credencial en 2023 que dice "trabaja en la empresa X", esa credencial registra permanentemente esa afirmación. Sin embargo, la afirmación era verdadera en 2023, pero puede dejar de serlo en 2024 si te despiden.

Por esto, el diseño de credenciales debe ser muy cuidadoso con la semántica temporal independientemente de si son VCs off-chain o attestations on-chain. Existen varias aproximaciones correctas que aplican a ambos modelos:

**Credenciales con fecha de expiración explícita**: "trabajó en empresa X desde enero 2023 hasta diciembre 2023", donde la validez temporal está codificada en los datos del claim. Cuando alguien verifica la credencial en 2025, puede ver que ya expiró sin necesidad de consultar mecanismos de revocación. Esto funciona bien para contratos temporales, certificaciones que caducan, o membresías por tiempo limitado.

**Credenciales de estado actual con revocación**: "actualmente emplea a esta persona", que se entiende válida desde la emisión hasta que sea revocada explícitamente. El emisor tiene la responsabilidad de revocarla cuando el estado cambie. Esto es apropiado para relaciones continuas donde la fecha de finalización no se conoce al momento de emisión.

**Credenciales de eventos puntuales**: "completó este curso en marzo 2023" o "asistió a este evento en 2024", donde la afirmación describe un hecho histórico que no cambia con el tiempo y por tanto raramente requiere revocación. Estas son las credenciales más simples porque su validez es intrínsecamente permanente.

El problema surge cuando las credenciales se diseñan ambiguamente sin considerar su semántica temporal. Si un claim dice "es empleado de la empresa X" sin especificar temporalidad ni implementar mecanismos de revocación proactivos, estás creando una afirmación que pretende ser verdad indefinidamente pero no tienes forma de invalidarla cuando deje de ser cierta. Esta es una falla de diseño, no una limitación técnica de la infraestructura.

Para attestations on-chain, la inmutabilidad blockchain es ventajosa para auditoría histórica: puedes demostrar que en 2023 tenías esa afirmación válida sobre ti, incluso si después fue revocada. Para VCs off-chain, el archivo firmado en tu wallet cumple función similar: prueba que en algún momento el emisor hizo esa afirmación sobre ti. En ambos casos, confundir "registro permanente de que se hizo una afirmación" con "la afirmación es verdadera para siempre" es un error conceptual fundamental que debe evitarse mediante diseño correcto de schemas y procesos de gestión de credenciales.

## Revocación: mecanismos para attestations y VCs

La revocación es un aspecto crítico tanto para attestations on-chain como para Verifiable Credentials off-chain, pero los mecanismos son diferentes según el tipo de credencial.

**Revocación de attestations on-chain (EAS y similares)**:

Cuando una attestation se registra en un smart contract como EAS, el mecanismo de revocación está integrado en el protocolo. El emisor original puede llamar a la función de revocación del contrato, que marca esa attestation específica como revocada en el registro on-chain mediante un flag booleano.

El proceso es directo: el smart contract registra quién emitió cada attestation. Solo ese emisor (o direcciones autorizadas según el schema) puede revocarla posteriormente. El titular sigue "poseyendo" la attestation en el sentido de que fue emitida a su dirección, pero ahora tiene estado de revocación marcado. Cuando un verificador consulta la attestation, el smart contract devuelve tanto los datos como el estado de revocación actual. Este proceso es instantáneo porque solo requiere consultar el contrato, sin necesidad de contactar al emisor.

EAS implementa revocación nativa mediante la función `revoke()` documentada en [docs.attest.sh/docs/core--concepts/revocation](https://docs.attest.sh/docs/core--concepts/revocation). Otras implementaciones de Attestation Layer pueden usar mecanismos similares con variaciones en los detalles técnicos.

**Revocación de Verifiable Credentials off-chain**:

Para VCs que siguen el estándar W3C y se almacenan off-chain en la wallet del usuario, el mecanismo es diferente. El emisor mantiene una lista de revocación separada que puede ser un archivo JSON publicado en un servidor, un registro on-chain específico para revocaciones, o un servicio API.

Cuando el emisor decide revocar una VC, agrega el ID único de esa credencial a su lista de revocación. El usuario conserva físicamente el archivo JSON de la VC en su wallet, pero cuando un verificador la comprueba, además de validar la firma criptográfica consultando el DID Document del emisor, debe consultar la lista de revocación para verificar si esa credencial específica ha sido invalidada. Si está en la lista, los verificadores la rechazan aunque técnicamente la firma sea válida.

Esta separación entre posesión y validez es fundamental: el usuario siempre tiene el archivo (posesión), pero el emisor controla si sigue siendo válida (validez). La autoridad del emisor deriva de su DID: como firmó la credencial con su clave privada asociada a ese DID, solo él puede actualizar el registro de revocación de credenciales firmadas por ese DID.

La revocación plantea desafíos de privacidad importantes. Si cada verificación requiere consultar un registro centralizado controlado por el emisor, éste puede rastrear cuándo y dónde usas tus attestations. Cada consulta a la lista de revocación revela que alguien está verificando esa credencial específica en ese momento. Soluciones avanzadas como [accumulator-based revocation](https://eprint.iacr.org/2020/777) permiten verificar que una attestation no ha sido revocada sin revelar cuál attestation específica estás verificando, preservando privacidad del titular. Estos sistemas usan estructuras criptográficas donde puedes probar que tu credencial no está en el conjunto de revocadas sin identificarla explícitamente.

---
