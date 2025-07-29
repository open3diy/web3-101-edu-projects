import networkx as nx
import matplotlib.pyplot as plt

from networkx.drawing.nx_pydot import graphviz_layout


G = nx.DiGraph()

def IPFS_draw(): 
    plt.figure(figsize=(6, 4))
    pos = graphviz_layout(G, prog="dot")  # dirección por defecto: top-down
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=1500, arrowsize=20)
    plt.title("Merkle DAG (top-down simulado)")
    plt.show()