# Instrucciones para GitHub Copilot

## Contexto del Repositorio

Este es un repositorio educativo en español dedicado a la divulgación de Web3. Es parte de [Open3DIY.org](https://github.com/open3diy/org) y se relaciona con [web3-101](https://github.com/open3diy/web3-101).

### Propósito

- **Educación**: Divulgar el potencial de la Web3 a través de contenido educativo
- **Canal de YouTube**: El contenido se publica en [Proyectos web3](https://www.youtube.com/@proyectos-web3)
- **Laboratorio práctico**: Prácticas validadas reflejadas en el repositorio web3-101

### Temas Principales

1. **Introducción a Web3**: Descentralización, SPOF, sistemas distribuidos
2. **Tecnología Web3**: Redes P2P, IPFS, almacenamiento distribuido
3. **Conceptos técnicos**: Árboles de Merkle, DAG, blockchain

## Estructura del Repositorio

```
/
├── 1_intro/                           # Contenidos de introducción a Web3
├── web3-infrastructure-technology/    # Tecnologías de infraestructura
├── _recycle-bin/                      # Contenido archivado
├── README.md                          # Índice principal del contenido
└── .github/                          # Configuración de GitHub
```

## Guías de Contribución

### Idioma

- **Contenido principal**: Español (todos los artículos, documentación y README)
- **Código y comentarios**: Español preferiblemente
- **Commits**: En español

### Formato de Contenido

- **Markdown**: Usar Markdown para toda la documentación
- **Jupyter Notebooks**: Para contenido interactivo (`.ipynb`)
- **Estilo**: Seguir `.markdownlint.json` para linting de Markdown

### Entorno de Desarrollo

**Python**:
- Usar entorno virtual `.venv-web3-edu-projects`
- Paquetes requeridos: notebook, ipykernel, multiformats, graphviz, networkx, matplotlib, pydot, ipympl, pygraphviz, pyvis, bokeh, base58

**Node.js**:
- Usar nvm con la versión especificada en `.nvmrc`

**Dependencias del sistema**:
- Ver `apt.txt` para dependencias del sistema
- Graphviz y PyGraphviz requeridos para visualizaciones

### Convenciones de Código

1. **Notebooks de Jupyter**:
   - Incluir explicaciones claras en español
   - Proporcionar ejemplos prácticos e interactivos
   - Usar visualizaciones cuando sea apropiado

2. **Documentación Markdown**:
   - Estructura clara con títulos jerárquicos
   - Incluir ejemplos de código cuando sea relevante
   - Referencias a conceptos relacionados

3. **Contenido educativo**:
   - Explicar conceptos desde lo básico
   - Usar analogías y ejemplos del mundo real
   - Incluir ejercicios prácticos cuando sea posible

### Licencia

- **Licencia**: Creative Commons CC0 1.0 Universal
- El contenido es de uso libre, incluso con fines comerciales
- Sin necesidad de atribución ni limitación alguna

## Sugerencias para GitHub Copilot

Al trabajar en este repositorio:

1. **Usar español** para comentarios, documentación y mensajes
2. **Enfoque educativo**: El contenido debe ser claro y accesible
3. **Contexto Web3**: Familiarizarse con blockchain, descentralización, P2P, IPFS
4. **Notebooks interactivos**: Priorizar la experimentación y visualización
5. **Referencias académicas**: Incluir referencias cuando sea apropiado
6. **Mejora continua**: El contenido se actualiza constantemente

## Enlaces Útiles

- [Repositorio principal web3-101](https://github.com/open3diy/web3-101)
- [Comunidad y referencias](https://github.com/open3diy/web3-101/blob/main/COMMUNITY.md)
- [Canal de YouTube](https://www.youtube.com/@proyectos-web3)
- [Open3DIY.org](https://github.com/open3diy/org)
