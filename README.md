# Web3 - 101 - Proyectos educativos

## Contexto

Este es contenido dentro de [Open3DIY.org](https://github.com/open3diy/org/blob/main/README.md) y se relaciona con [web3 - 101](https://github.com/open3diy/web3-101/blob/main/README.md).

Este contenido tiene un enfoque educativo para divulgar el potencial de la Web3.

**En este repositorio exploramos la evolución de internet hacia la Web3!**.

Web3 representa la evolución de internet hacia un modelo descentralizado basado en tecnologías como blockchain, contratos inteligentes y redes peer-to-peer. Su propósito es devolver a los usuarios el control sobre sus datos y transacciones sin intermediarios centralizados.

Esto tiene aplicaciones en identidades digitales, economías descentralizadas, almacenamiento distribuido, cadena de suministro, Tokenización del mundo real y dApps.

## Propósito

**Mi propósito aquí** es la divulgación de la web3 en una serie de vídeos educativos.

## Solución

La solución que aplico es la formación continua, enriquecida y validada con prácticas reflejadas en [web3 - 101](https://github.com/open3diy/web3-101/blob/main/README.md), que funciona como el laboratorio del canal.

## Licencia

Ver la licencia de [open3diy](https://github.com/open3diy/org/blob/main/LICENSE).

El canal de YouTube [Proyectos web3](https://www.youtube.com/@proyectos-web3) tiene una licencia `Creative Commons de YouTube`.

El contenido es académico y libre de restricciones de propiedad intelectual, lo que significa que puede usarse o difundirse libremente, pero no puede ser apropiado ni reclamado como propio por ninguna entidad, incluida una empresa.

No se permite el uso comercial del contenido, y cualquier reproducción parcial o completa debe incluir una mención adecuada del canal [Proyectos web3](https://www.youtube.com/@proyectos-web3) o de este repositorio de github.

## Referencias

Las referencias las podemos encontrar en [la comunidad](https://github.com/open3diy/web3-101/blob/main/COMMUNITY.md).

## Contribuir

### Preparar el entorno local

Es necesario instalar previamente:

* python / entornos virtuales python.

  ```bash
  sudo apt install python3 python3-dev python3-venv
  ```

* Graphviz y PyGraphviz:

  ```bash
  sudo apt install graphviz libgraphviz-dev pkg-config
  ```

* nvm: <https://github.com/nvm-sh/nvm>.

**Entorno virtual python**.

Se creará un entorno virtual de python propio al repositorio, siguiendo los siguientes pasos.

```bash
python3 -m venv .venv-web3-edu-projects
```

Al abrir vscode normalmente se activa el entorno virtual, pero si no es el caso, en terminal para activarlo:

```bash
source .venv-web3-edu-projects/bin/activate
```

Instalar paquetes necesarios:

```bash
pip install notebook ipykernel multiformats graphviz networkx matplotlib pydot ipympl pygraphviz pyvis networkx bokeh networkx

```

Instalar extensión de vscode `Jupyter`.

### Iniciar vscode

Desde la carpeta del proyecto, abrir terminal y ejecutar:

```bash
nvm use
code .
```

## Notas adicionales

En este repositorio se aplica la mejora continua, por lo tanto, podríamos ver mejoras de los artículos aquí expuestos que no se reflejen en vídeos del canal [Proyectos web3](https://www.youtube.com/@proyectos-web3).

> En cualquier caso, si es relevante se crearán nuevos vídeos aclaratorios que mejoren la explicación.
