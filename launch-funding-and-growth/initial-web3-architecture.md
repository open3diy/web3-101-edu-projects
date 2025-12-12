# Arquitectura Web3 inicial: un enfoque práctico para la descentralización

Este documento presenta un mapa de arquitectura para lanzar un proyecto Web3. Más que una simple lista de tecnologías, el conjunto de herramientas aquí descrito conforma un **marco de trabajo (framework)** que modela el flujo de desarrollo y la operativa del proyecto desde su inicio. La elección de este stack define un camino pragmático que equilibra los ideales de descentralización con las realidades del ecosistema actual.

El principal desafío de cualquier equipo es gestionar la tensión entre el uso de infraestructura Web2 centralizada, necesaria para la agilidad y la experiencia de usuario, y el objetivo de construir un sistema resistente a la censura y sin puntos únicos de fallo. Por ello, el enfoque propuesto es un **modelo híbrido de descentralización progresiva**: se aceptan dependencias centralizadas para componentes no críticos (como la comunicación o el alojamiento de bots), mientras que las operaciones que custodian valor o gobiernan el protocolo se aseguran criptográficamente desde el primer día mediante herramientas como las wallets multifirma.

Este documento no incluye decisiones estratégicas ni desarrollo detallado; para ello puedes consultar [Alternativas Tecnológicas para un MVP Web3](./technological-alternatives-for-a-web3-mvp.md). Aquí se presentan los primeros pasos: una base que puede ayudarte a iniciar la idea de marca y crear la narrativa inicial, sobre la cual podrás crecer y evolucionar el proyecto.

A continuación, se detallan las herramientas esenciales que componen este framework, se explica cómo definen un flujo de trabajo Web3 y se analiza, de forma transparente, los límites y riesgos de cada componente.

## Herramientas fundamentales en un setup Web3 inicial

**[GitHub](https://github.com)**:

Sirve como repositorio de código, sistema de control de versiones y entorno para automatizaciones de despliegue. Permite publicar una página estática informativa mediante GitHub Pages, útil como primera landing. Aunque no es descentralizado, es el estándar de facto por su ecosistema.  

**[Cloudflare](https://cloudflare.com)**:

Punto de gestión DNS y seguridad del dominio Web2. Toda aplicación Web3 que se expone en la web tradicional necesita resolver un dominio HTTP, por lo que sigue siendo imprescindible. Ofrece velocidad, protección y fácil administración.  

**[ENS (Ethereum Name Service)](https://ens.domains)**:

Proporciona un identificador Web3 que puede mapearse a direcciones, perfiles, contenidos IPFS o servicios. Funciona como un puente entre identidad descentralizada y contenido distribuido.  

**[MetaMask](https://metamask.io)**:

Wallet utilizada para identidad operativa, firma de transacciones y despliegue de contratos. Es el punto de acceso al ecosistema Web3 para operaciones técnicas del proyecto.  

**[X.com (antes Twitter)](https://x.com)**:

Red social clave para la difusión y posicionamiento del proyecto en el ecosistema Web3. Permite construir comunidad, compartir avances y conectar con otros actores del sector. Aunque es una plataforma centralizada, su alcance y relevancia la hacen indispensable para la comunicación pública y la generación de confianza en las primeras etapas.

**[Discord](https://discord.com)**:

Espacio de comunidad ampliamente usado en Web3, con soporte para bots, roles automáticos y validaciones por wallet. Es la herramienta principal para comunicación directa con usuarios.  

**[Snapshot](https://snapshot.org)**:

Plataforma de votación sin gas basada en firmas que facilita mecanismos de gobernanza desde fases tempranas sin emitir un token o montar un sistema de votación on-chain.  

**[Safe (antes Gnosis Safe)](https://safe.global)**:

Es el estándar de facto para la gestión de tesorería y operaciones críticas. Como wallet multifirma (multisig), requiere que múltiples miembros aprueben una transacción antes de ejecutarla, eliminando el riesgo de que una sola persona controle los fondos o el protocolo.

**Infraestructura para bots y automatización**:

Herramientas como [Replit](https://replit.com), [Railway](https://railway.app) o [Fly.io](https://fly.io/) permiten alojar procesos automatizados (bots) que gestionan roles en Discord, verificaciones o tareas recurrentes. 

Son componentes centralizados, pero útiles para la operativa diaria de la comunidad.

**Plataformas de Despliegue Frontend**:

Para alojar la interfaz de la DApp, servicios como [Vercel](https://vercel.com) o [Netlify](https://www.netlify.com) ofrecen integración continua y despliegue global desde un repositorio de GitHub. Aunque son centralizados, su eficiencia es clave para la experiencia de usuario. La alternativa descentralizada es alojar el frontend en IPFS.

**Entornos de despliegue de contratos**:

[Hardhat](https://hardhat.org), [Foundry](https://book.getfoundry.sh/) o [Remix](https://remix.ethereum.org) permiten compilar, probar y desplegar contratos. Remix es útil en prototipos rápidos; Hardhat y Foundry para desarrollos complejos.

**Exploradores de bloques ([Etherscan](https://etherscan.io), [Basescan](https://basescan.org))**:

Son la fuente de verdad pública para verificar transacciones, consultar estados de contratos y auditar la actividad on-chain. Son una herramienta indispensable para la transparencia del ecosistema.

**Indexación y consulta de datos ([The Graph](https://thegraph.com))**:

Para que una DApp muestre datos históricos de la blockchain de forma eficiente (ej. transacciones de un usuario, propietarios de NFTs), se necesita un indexador. The Graph es el protocolo estándar para crear "subgraphs", que son APIs abiertas y descentralizadas para consultar datos on-chain.

**Oráculos ([Chainlink](https://chain.link))**:

Los contratos inteligentes no pueden acceder a datos del mundo exterior (precios, resultados deportivos, etc.). Los oráculos como Chainlink resuelven este problema, proveyendo flujos de datos externos de forma segura y descentralizada, lo que es vital para cualquier aplicación DeFi.

**Herramientas de monitoreo y debugging ([Tenderly](https://tenderly.co))**:

Servicios como Tenderly ofrecen simulación de transacciones, debugging profundo y visualización de errores on-chain.  

**Sistemas de identidad descentralizada ([Sign-In With Ethereum](https://login.xyz))**:

Proveen autenticación sin cuentas Web2. Sign-In With Ethereum permite que los usuarios accedan a servicios con su wallet.  

**Documentación del proyecto ([Notion](https://notion.so), GitHub Wiki, IPFS)**:

Aunque el objetivo sea la descentralización, se requiere documentación interna. Puede alojarse en Notion, GitHub Wiki o versiones inmutables en IPFS.

## Cómo estas herramientas permiten aplicar un marco de trabajo Web3

El principio básico del trabajo en Web3 es que cada pieza del sistema pueda ser verificada, auditada y no dependa exclusivamente de la confianza en un propietario central. El uso combinado de estas herramientas permite operar siguiendo estos principios sin imponer un framework específico.

- El repositorio en GitHub hace verificable el desarrollo.
- La identidad mediante MetaMask y ENS reemplaza contraseñas por firmas criptográficas.
- El contenido en IPFS reduce dependencia de servidores.
- Las votaciones en Snapshot permiten procesos de decisión comunitarios.
- La comunicación en Discord facilita interacción abierta entre participantes.
- El despliegue reproducible con Hardhat o Foundry asegura trazabilidad técnica.
- El dominio en Cloudflare, unido a ENS, mantiene un puente híbrido práctico.

## El verdadero desafío: descentralizar la operación

La intención de descentralizar un proyecto choca con limitaciones prácticas. Muchas herramientas indispensables para un uso operacional no soportan en todos los casos una wallet multisign.

**Repositorios**:

GitHub no es descentralizado. La única forma de aportar resiliencia parcial es permitir forks públicos o migrar a protocolos distribuidos como Radicle. Aun así, GitHub sigue siendo necesario por su ecosistema.

**Dominios**:

Un dominio gestionado en Cloudflare depende siempre de su infraestructura. ENS mitiga este problema, aunque la resolución completa todavía necesita capas Web2.

**Cuentas**:

La wallet es controlada por claves privadas. Si solo una persona la posee, el proyecto depende de ella. La solución es usar multisig con Safe.

**Comunidad**:

Discord no es descentralizado. Puede mitigar el riesgo repartiendo permisos, pero sigue dependiendo del servicio.

**Almacenamiento**:

IPFS, por sí solo, no garantiza la persistencia del contenido si no existen nodos replicando activamente los archivos (*pinning*). Para asegurar durabilidad, se puede recurrir a Filecoin, donde es posible gestionar el almacenamiento mediante una wallet multifirma. Sin embargo, servicios de *pinning* como Pinata, Infura, Fleek, NFT.Storage o Web3.Storage, aunque facilitan la integración y el acceso, requieren cuentas Web2 para su administración y mantenimiento, lo que introduce un componente centralizado en la gestión del almacenamiento descentralizado.

**Snapshot**:

Aunque las decisiones se firman criptográficamente, la interfaz depende de infraestructura Web2.

**Correos electrónicos**:

Casi todos estos servicios exigen correos tradicionales. No existe un reemplazo descentralizado funcional para el email.

## Cómo aproximarse a una descentralización realista

La clave es la **descentralización progresiva y consciente**. En lugar de aspirar a una pureza total desde el inicio, se deben tomar medidas estratégicas para mitigar los riesgos de la centralización:

- **Uso de Safe (multisig)** para la gestión de la tesorería, la propiedad de los contratos inteligentes y el dominio ENS. Esta es la medida más crítica.
- **Organización en GitHub** con varios administradores y políticas de ramas protegidas para el código principal.
- **Permisos distribuidos en Discord**, asignando roles de moderación a miembros de confianza de la comunidad.
- **Replicación del contenido de IPFS** en múltiples servicios de *pinning* o nodos propios para evitar un único punto de fallo.
- **Documentación duplicada** en repositorios públicos (GitHub) y en almacenamiento inmutable (Arweave/IPFS) para garantizar su preservación.
- **Transparencia radical**: documentar públicamente qué componentes están centralizados y cuál es la hoja de ruta para descentralizarlos en el futuro.

---
