# Session Keys: un patrón de autorización delegada

## Qué son realmente las session keys

El término *session key* no corresponde a un único estándar cerrado ni a un EIP concreto. Es un patrón de diseño ampliamente adoptado en el ecosistema de smart accounts que describe cómo delegar a una clave secundaria permisos de ejecución acotados, sin necesidad de exponer la clave principal de la cuenta ni requerir autorización manual en cada operación.

La confusión es habitual por dos razones. La primera es que el término se usa para describir cosas distintas según el contexto: a veces se refiere a la clave efímera que vive en el cliente, a veces al permiso registrado on-chain en la smart account, y a veces al módulo validador completo que gestiona esos permisos. Son partes del mismo patrón, pero no la misma cosa.

La segunda es que algunos EIPs recientes han popularizado el término y es fácil confundirlos con el origen del patrón. [EIP-7715](https://eips.ethereum.org/EIPS/eip-7715) propone estandarizar la interfaz que un wallet expone para que una dApp solicite permisos de sesión, pero esa interfaz es solo la capa de negociación entre dApp y wallet. La mecánica subyacente —registrar una clave secundaria con permisos acotados en una smart account y validar sus firmas on-chain— existe como patrón independiente desde antes de ERC-4337, implementado de forma autónoma por proyectos como Gnosis Safe o Argent. EIP-7715 no inventó el mecanismo: propone estandarizar cómo se solicita desde fuera.

## Por qué las session keys requieren una smart account

En Ethereum existen dos tipos de direcciones. Las **EOA** (*Externally Owned Account*) son las cuentas estándar: están controladas por una única clave privada y no contienen código. Cuando un nodo de Ethereum recibe una transacción firmada por una EOA, la capa de ejecución verifica que la firma ECDSA corresponde a la dirección remitente. Si no es válida, la transacción se rechaza antes de que ningún contrato llegue a ejecutarse. No hay forma de personalizar esa validación: es fija, implementada en el software del cliente (Geth, Nethermind, etc.), y solo acepta la firma de la clave privada asociada a esa dirección.

Las **smart accounts** (también llamadas contract accounts) son contratos desplegados en la blockchain que tienen código propio. Ese código puede implementar cualquier lógica de validación: aceptar firmas de múltiples claves, comprobar permisos, aplicar límites de gasto. Las session keys funcionan precisamente porque la smart account puede ejecutar esa lógica cuando llega una operación firmada con la clave de sesión.

El patrón existía antes de que hubiera estándares: proyectos como Gnosis Safe o Argent eran smart accounts y podían implementar variantes de session keys en su propio código. No estaba estandarizado y cada implementación era incompatible con las demás.

[ERC-4337](https://eips.ethereum.org/EIPS/eip-4337) (2023) estandarizó el modelo de smart account con el flujo de UserOperation y el EntryPoint, haciendo que session keys como patrón fueran reproducibles e interoperables entre proyectos distintos.

[EIP-7702](https://eips.ethereum.org/EIPS/eip-7702) (Pectra, 2025) abrió una vía adicional, pero para entenderla hay que saber qué cambió en el protocolo.

Antes de EIP-7702, el campo `code` de una EOA estaba siempre vacío — era una invariante del protocolo. Una EOA no podía tener código.

EIP-7702 modificó esa regla en la especificación de la EVM: introdujo un nuevo tipo de transacción (tipo `0x04`) que incluye una lista de autorizaciones firmadas por el EOA. Cuando la capa de ejecución de Ethereum procesa esa transacción —los nodos, no ningún contrato— escribe en el campo `code` de la dirección EOA un puntero de delegación que apunta a un contrato existente. Esto es una operación a nivel de protocolo: modifica el estado global de la cadena igual que lo haría un cambio de saldo.

A partir de ese momento, cuando alguien llama a esa dirección EOA, la EVM detecta el puntero de delegación y ejecuta el código del contrato apuntado, pero en el contexto de la EOA: su almacenamiento, su saldo, su dirección. El resultado es que esa EOA se comporta exactamente como una smart account, con toda su lógica de validación personalizada, sin haber cambiado de dirección y sin que el usuario tenga que mover fondos.

La delegación persiste en el estado de la cadena hasta que el EOA envíe otra transacción tipo `0x04` para revocarla o apuntar a otro contrato.

El patrón de session keys no cambia en absoluto. Lo que cambia es que ya no es necesario desplegar una smart account en una nueva dirección para acceder a él: una EOA existente puede adquirir esa capacidad directamente.

## Cómo funciona el patrón

El propietario de la smart account genera un nuevo par de claves criptográficas temporal, directamente en el dispositivo o la aplicación. La clave privada nunca sale del cliente: se guarda en memoria o en almacenamiento local del navegador, y nunca se envía a la blockchain ni a ningún servidor. Solo la clave pública —junto con las reglas de permiso— se registra on-chain.

Esta clave tiene permisos limitados: solo puede ejecutar las acciones que se definieron al crear la sesión. Estas restricciones pueden incluir:

- Duración temporal: la sesión expira automáticamente pasado un tiempo,
- Contratos permitidos: solo se pueden llamar direcciones específicas,
- Límites de gasto: no se puede transferir más de una cantidad determinada,
- Tipos de operación: por ejemplo, solo swaps, no transferencias arbitrarias,
- Contexto de uso: ligado a una dApp o dominio concreto.

El patrón tiene dos fases bien diferenciadas:

**Fase de registro**: el propietario firma y envía una transacción que escribe en la smart account la clave pública de la session key y las reglas de permiso asociadas. A partir de ese momento, el contrato conoce qué clave está autorizada y qué puede hacer.

**Fase de uso**: cada operación que la dApp quiere ejecutar se firma con la clave privada de la sesión, del lado del cliente. La UserOperation resultante llega al contrato, que verifica dos cosas: que la firma corresponde a la clave pública registrada, y que la operación solicitada está dentro de los límites definidos en el registro. Si ambas comprobaciones pasan, la operación se ejecuta.

## Implementaciones del protocolo

El flujo de session keys tiene dos extremos estandarizados. EIP-7715 cubre el inicio: cómo la dApp solicita permisos al wallet. ERC-7710 cubre una variante del destino: cómo ejecutar esos permisos on-chain a través de un orquestador externo. Entre ambos extremos, la validación puede ocurrir de distintas formas según cómo esté construida la smart account.

### Origen: la dApp solicita permisos (EIP-7715)

Cuando una dApp quiere usar session keys, necesita pedirle al wallet del usuario que cree y registre una session key con determinados permisos. Sin un estándar, cada dApp tendría que conocer el tipo concreto de smart account del usuario y hablar con ella de forma específica.

[EIP-7715](https://eips.ethereum.org/EIPS/eip-7715) estandariza esa solicitud: define la interfaz que un wallet expone para que cualquier dApp pueda pedir permisos de sesión de forma interoperable, sin saber qué tipo de smart account hay detrás. La dApp declara qué quiere hacer —contratos, límites, duración— y el wallet gestiona la creación de la clave y su registro según su propia implementación.

Esta es una capa off-chain de negociación entre dApp y wallet. EIP-7715 no define cómo se valida nada on-chain.

### Destino: ejecución on-chain

Una vez que el wallet ha registrado la session key, las operaciones firmadas con ella se ejecutan on-chain. Hay tres formas de implementar la validación en la smart account, y una variante adicional con orquestador externo mediante ERC-7710.

**Validación en la lógica interna de la smart account**:

La smart account implementa directamente en su propio contrato la función `validateUserOp`, que es el punto de entrada que el EntryPoint de ERC-4337 llama para verificar si una operación está autorizada. En ese contexto, el contrato consulta su propio almacenamiento para saber si la clave pública que firmó la operación está registrada como session key activa, y si los parámetros de la operación (destinatario, valor, datos de llamada) están dentro de los permisos concedidos.

Esta opción da control total al equipo que diseña la cuenta, pero significa que la lógica de permisos queda mezclada con el contrato principal. Actualizar o extender ese sistema requiere migrar a una nueva implementación del contrato.

**Validación en módulos externos conectables (ERC-7579)**:

[ERC-7579](https://eips.ethereum.org/EIPS/eip-7579) define un estándar para cuentas modulares. Aquí, "módulo" significa un **contrato inteligente separado, desplegado en la blockchain**, que se registra dentro de la smart account. No es código que se añade al compilar el contrato base: es un contrato independiente con su propia dirección on-chain.

El flujo es el siguiente: cuando llega una UserOperation, la smart account —en lugar de validar ella misma— lee de su propio almacenamiento on-chain qué módulo validador tiene instalado, y le hace una llamada a ese contrato preguntando: *¿es válida esta firma para esta operación?* El módulo consulta sus propias reglas (también almacenadas on-chain) y responde.

"Instalar" un módulo significa ejecutar una transacción que registra la dirección del contrato módulo en el almacenamiento de la smart account. "Desinstalar" significa borrar ese registro. El contrato base de la cuenta no cambia en ningún momento: solo cambia a qué dirección delega la validación.

La ventaja es clara: si se quiere cambiar la lógica de sesión —añadir un nuevo tipo de restricción, corregir un bug en la validación— basta con desplegar un nuevo contrato módulo e instalarlo. No hay que migrar la cuenta ni mover fondos. Además, el mismo módulo puede ser usado por miles de cuentas distintas que sean compatibles con ERC-7579.

ZeroDev Kernel y Safe con su sistema de módulos usan exactamente este modelo.

**Validación distribuida en el flujo de ERC-4337**:

Para entender esta opción hay que saber cómo funciona ERC-4337 internamente. Cuando un usuario quiere ejecutar una operación, no envía una transacción directamente: envía una **UserOperation** a un contrato central llamado **EntryPoint**. Este contrato orquesta el proceso en dos pasos bien diferenciados:

1. **Fase de validación**: el EntryPoint llama a `validateUserOp` en la smart account. Aquí se verifica que la firma es correcta y que la cuenta tiene saldo para pagar el gas. Si falla, la operación se rechaza antes de ejecutar nada.
2. **Fase de ejecución**: si la validación pasa, el EntryPoint ejecuta la operación real —la llamada al contrato destino.

Entre y alrededor de estos dos pasos, algunas implementaciones de smart account permiten insertar **hooks**: funciones que se ejecutan justo antes o justo después de la ejecución, y que pueden abortar la operación si algo no cuadra.

La relevancia para session keys es esta: hay dos tipos de restricciones que se quieren verificar:

- **¿Es válida la firma?** Esto se comprueba en la fase de validación (`validateUserOp`), porque es barato de verificar y el EntryPoint lo exige.
- **¿Se respetan los límites de permisos?** —por ejemplo, que no se gaste más de 10 USDC en total durante la sesión. Esto requiere leer estado acumulado y puede ser más costoso. Algunas implementaciones lo delegan a un **hook post-ejecución** que actualiza un contador y aborta si se supera el límite.

Además, el flujo de ERC-4337 permite un tercer actor: el **Paymaster**, un contrato que puede pagar el gas en nombre del usuario. El Paymaster también tiene su propia fase de validación (`validatePaymasterUserOp`), y algunas arquitecturas aprovechan esto para que el Paymaster actúe como guardián de políticas: si la operación no cumple las condiciones del permiso, el Paymaster simplemente rechaza patrocinar el gas, lo que impide la ejecución.

En resumen: en este enfoque la validación no vive en un único lugar sino repartida. La verificación de firma ocurre en `validateUserOp`, los límites acumulados se comprueban en hooks, y el Paymaster puede añadir una capa adicional de control. Es el enfoque menos habitual para session keys puras, pero aparece en arquitecturas donde el mismo Paymaster gestiona tanto el pago de gas como las políticas de uso de una flota de usuarios.

**Variante con orquestador externo (ERC-7710)**:

[ERC-7710](https://eips.ethereum.org/EIPS/eip-7710) define un contrato estándar llamado **DelegationManager** que actúa como intermediario entre quien presenta la delegación firmada y la smart account que la ejecuta. En lugar de que la dApp llame directamente a la smart account, llama a `redeemDelegations()` en el DelegationManager, que verifica la delegación y si es válida, llama a la smart account para que ejecute la operación.

El DelegationManager no reemplaza los tres mecanismos anteriores: internamente, la smart account sigue validando con cualquiera de ellos. Lo que aporta ERC-7710 es desacoplar al actor que presenta la delegación de la cuenta original, lo que permite que un tercero redima permisos sin interactuar directamente con la cuenta.

ERC-7710 está en estado Draft. A fecha de redacción, MetaMask lo implementa a través de su [Delegation Toolkit](https://github.com/MetaMask/delegation-framework).

## Implementaciones de referencia

El patrón está adoptado de forma autónoma por los principales proyectos del ecosistema de smart accounts:

- [Safe](https://safe.global/) lo implementa mediante módulos de sesión conectables a su arquitectura multisig.
- [ZeroDev Kernel](https://docs.zerodev.app/) ofrece un sistema de plugins de validación donde las session keys son un caso de uso central.
- [Biconomy](https://docs.biconomy.io/) incluye session keys como parte de su SDK para simplificar flujos de usuario en dApps.

Estos proyectos comparten la misma intuición —delegar permisos acotados a una clave secundaria con validación on-chain— pero cada uno lo implementa con su propia interfaz y estructura de módulos.

## Qué no son las session keys

Hay mecanismos relacionados que comparten la idea de delegar autorización sin ceder el control total, pero que no son session keys. Entender la diferencia ayuda a situar el patrón.

**`approve()` de ERC-20**: autorizas a un contrato concreto a gastar una cantidad de tus tokens. No hay clave secundaria ni firma delegada — la autorización se escribe directamente en el almacenamiento del contrato del token. El permiso es permanente hasta que lo revoques manualmente, y solo afecta a ese token concreto. Funciona con cualquier EOA sin necesidad de smart account.

**`permit()` de EIP-2612**: mejora `approve()` eliminando la transacción previa. En lugar de enviar un `approve()`, el usuario firma un mensaje off-chain con su clave privada, y esa firma se incluye en la misma llamada que ejecuta la operación. El mecanismo criptográfico es el mismo que usan las session keys —firmar off-chain, verificar on-chain— pero el alcance es igual de limitado que `approve()`: una única autorización de gasto sobre un token concreto.

**Multisig (ERC-1271 / Safe)**: múltiples claves que deben aprobar cada operación. Puede parecer similar porque hay varias claves involucradas, pero la diferencia es fundamental: en multisig todas las claves son propietarias con igual peso, no hay delegación con permisos acotados, y cada operación requiere N firmas manuales — no hay automatización.

Los tres mecanismos son anteriores a las session keys y funcionan sin smart account (salvo multisig). Las session keys generalizan la idea: en lugar de autorizar un recurso concreto o requerir múltiples propietarios, se delega a una clave secundaria la capacidad de actuar sobre la cuenta completa, con restricciones arbitrarias y durante un tiempo definido.

---
