import sys

with open('/home/jesus/projects/open3diy.org/web3-101-edu-projects/infrastructure/identity/did-protocols.md', 'r') as f:
    content = f.read()

split_marker = "## Anatomía de un DID\n"
parts = content.split(split_marker)

if len(parts) < 2:
    print("Marker not found!")
    sys.exit(1)

new_content = parts[0] + split_marker + """
Para que el ecosistema funcione de manera interoperable, todos los identificadores siguen una sintaxis estándar y universal, similar a cómo funcionan las URLs en la web tradicional, pero diseñados para la descentralización.

La estructura básica se compone de tres partes: `did:metodo:identificador_unico`.

El prefijo siempre es `did`, indicando el tipo de esquema. El método define la infraestructura subyacente donde vive y se gestiona este identificador. Finalmente, el identificador único es la cadena específica que te representa dentro de ese método.

Por ejemplo, `did:ethr:0x123...` indica un identificador registrado en la red Ethereum, mientras que `did:web:example.com` apunta a un identificador alojado en un dominio web tradicional.

## Métodos DID: Diversidad de enfoques

No existe una única forma de implementar un DID. Diferentes casos de uso requieren distintos equilibrios entre descentralización, privacidad, costo y facilidad de adopción. Por ello, el ecosistema ha desarrollado múltiples métodos que podemos agrupar conceptualmente.

**Métodos basados en Blockchain**:

Utilizan redes públicas como Ethereum o Bitcoin para registrar los identificadores. Ofrecen la máxima descentralización y seguridad criptográfica, ya que no dependen de ningún servidor central. Son ideales para organizaciones o identidades públicas que interactúan con contratos inteligentes, aunque suelen implicar costos de transacción y cierta latencia.

**Métodos basados en Web**:

Aprovechan la infraestructura de internet existente, como dominios y conexiones seguras. Son muy fáciles de adoptar para empresas que ya poseen dominios reconocidos, permitiendo una transición suave hacia la identidad descentralizada. Su principal desventaja es que dependen de sistemas tradicionales, lo que introduce cierto grado de centralización.

**Métodos criptográficos y efímeros**:

Diseñados para la máxima privacidad y comunicación directa. No utilizan blockchains ni servidores públicos; el identificador se deriva directamente de una clave criptográfica y solo se comparte con la contraparte necesaria. Son perfectos para mensajería privada o interacciones de un solo uso donde se busca evitar el rastreo.

## El DID Document y la Resolución

El identificador por sí solo es solo una cadena de texto. Su verdadero valor reside en el DID Document, el archivo al que apunta.

En lugar de pensar en el DID Document como un archivo técnico complejo, podemos verlo como un perfil criptográfico público. Este documento no contiene tus datos personales, sino las herramientas matemáticas necesarias para que otros puedan verificar que un mensaje o credencial realmente proviene de ti. También incluye las direcciones técnicas donde otros pueden comunicarse contigo de forma segura.

Una de las grandes ventajas de este sistema es la rotación de claves. Si sospechas que tu clave privada ha sido comprometida, puedes actualizar tu DID Document con una nueva clave pública. Tu identificador sigue siendo el mismo, pero la cerradura matemática cambia, manteniendo tu reputación e historial intactos.

**El proceso de resolución**:

Para conectar el identificador con su documento, se utiliza un proceso llamado resolución. Independientemente de si tu DID vive en Ethereum, en un servidor web o en una red directa, el proceso de resolución estandariza la forma en que las aplicaciones buscan y obtienen tu DID Document. Esto garantiza que cualquier aplicación Web3 pueda interactuar con cualquier DID, sin importar la tecnología subyacente.

## Comunicación y Patrones Avanzados

Una vez que las identidades pueden descubrirse y verificarse mutuamente, necesitan una forma de interactuar de manera segura y estructurada.

**DIDComm**:

Es el protocolo estándar para la mensajería segura entre DIDs. Si los identificadores son como números de teléfono, DIDComm es la aplicación de mensajería cifrada de extremo a extremo que los utiliza. Permite que dos identidades negocien credenciales, soliciten verificaciones o intercambien datos privados con la garantía de que solo el destinatario previsto puede leer el mensaje y que el remitente es auténtico.

**Estructuras organizativas**:

La flexibilidad de los DIDs permite modelar estructuras complejas del mundo real. Por ejemplo, una empresa puede establecer identificadores jerárquicos, donde un identificador corporativo raíz delega permisos limitados a los identificadores de sus distintos departamentos o empleados.

**Identidades multifirma**:

Para identidades de alto valor, como la tesorería de una organización descentralizada, se pueden configurar identificadores que requieren múltiples aprobaciones. En este escenario, el documento especifica que cualquier actualización o acción requiere la firma criptográfica de varias partes, eliminando los puntos únicos de fallo y distribuyendo la confianza.

## Referencias y Especificaciones

- [W3C DID Core 1.0](https://www.w3.org/TR/did-core/) - Especificación fundamental
- [DID Method Registry](https://www.w3.org/TR/did-spec-registries/) - Lista oficial de métodos
- [DIDComm Messaging](https://identity.foundation/didcomm-messaging/spec/) - Protocolo de mensajería
- [Universal Resolver](https://github.com/decentralized-identity/universal-resolver) - Implementación de referencia
- [DIF (Decentralized Identity Foundation)](https://identity.foundation/) - Comunidad y grupos de trabajo

---

Este documento proporciona la base técnica para implementar sistemas de identidad descentralizada. Para casos de uso prácticos y integración con aplicaciones Web3, consulta [9-1-ecosystem-DApps.md](../101/9-1-ecosystem-DApps.md).
"""

with open('/home/jesus/projects/open3diy.org/web3-101-edu-projects/infrastructure/identity/did-protocols.md', 'w') as f:
    f.write(new_content)

print("File updated successfully!")
