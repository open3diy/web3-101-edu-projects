# Web3 - 101 - Proyectos educativos

## Contexto

Este es contenido dentro de [Open3DIY.org](https://github.com/open3diy/org/blob/main/README.md) y se relaciona con [web3 - 101](https://github.com/open3diy/web3-101/blob/main/README.md).

Este contenido tiene un enfoque educativo para divulgar el potencial de la Web3.

**En este repositorio exploramos la evolución de internet hacia la Web3!**.

Web3 representa la evolución de internet hacia un modelo descentralizado basado en tecnologías como blockchain, contratos inteligentes y redes peer-to-peer. Su propósito es devolver a los usuarios el control sobre sus datos y transacciones sin intermediarios centralizados.

Esto tiene aplicaciones en identidades digitales, economías descentralizadas, almacenamiento distribuido, cadena de suministro, Tokenización del mundo real y dApps.

## Propósito

**Mi propósito aquí** es la divulgación de la web3 en una serie de vídeos educativos que podrás ver en el canal de YouTube [Proyectos web3](https://www.youtube.com/@proyectos-web3).

## Solución

La solución que aplico es la formación continua, enriquecida y validada con prácticas reflejadas en [web3 - 101](https://github.com/open3diy/web3-101/blob/main/README.md), que funciona como el laboratorio del canal.

## Índice de contenido

A continuación encontrarás un listado actualizado de todos los contenidos publicados en este repositorio:

**Introducción a la web3**:

* [El punto único de fallo (SPOF) y la descentralización](./1_intro/1_1_Single-Point-of-Failure-SPOF-and-Decentralization.md).  
  > Explica cómo los sistemas centralizados presentan riesgos del punto único de fallo y cómo la descentralización mitiga estos problemas. Además veremos los principios fundamentales de la descentralización y la Web3.
* [Entendiendo los sistemas centralizadas, distribuidos y descentralizados](./1_intro/1_2_Centralized-and-decentralized-systems.md).  
  > Analiza y compara los modelos de sistemas centralizados, distribuidos y descentralizados, destacando sus diferencias clave para comprender cómo cada enfoque impacta en el rendimiento, la seguridad, la resistencia a la censura y la resiliencia.

**La tecnología de la web3**:

* [Introducción a redes P2P](./web3-infrastructure-technology/_misc/p2p_overview.md)  
  > Presenta los conceptos básicos de las redes peer-to-peer y su importancia en la infraestructura de la web3.
* [Primera aproximación a IPFS](./web3-infrastructure-technology/first-approach-to-IPFS.md).  
  > Primera presentación y práctica con IPFS (InterPlanetary File System), siendo un protocolo y red para almacenar y compartir contenido de forma descentralizada. Es clave en la web3 para el almacenamiento distribuido y resistente a la censura.

**Conceptos técnicos clave en la web3**:

* [Jugando y entendiendo un árbol de Merkle](./web3-infrastructure-technology/_misc/merkle_playground.ipynb)  
  > Permite experimentar con árboles de Merkle para comprender su uso en la verificación de datos y blockchain.
* [Jugando y entendiendo un DAG](./web3-infrastructure-technology/_misc/dag_playground.ipynb).  
  > Ofrece una introducción práctica a los grafos acíclicos dirigidos (DAG) y su relevancia en tecnologías descentralizadas.

## Licencia

Ver la licencia de [open3diy](https://github.com/open3diy/org/blob/main/LICENSE).

El contenido es académico y libre de restricciones de propiedad intelectual, lo que significa que puede usarse o difundirse libremente, incluso con fines comerciales, sin necesidad de atribución ni limitación alguna, conforme a la licencia Creative Commons CC0 1.0 Universal.

Debes considerar que el canal de YouTube [Proyectos web3](https://www.youtube.com/@proyectos-web3) tiene una licencia ya definida de `Creative Commons de YouTube`.

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
pip install notebook ipykernel multiformats graphviz networkx matplotlib pydot ipympl pygraphviz pyvis networkx bokeh networkx base58
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
