import networkx as nx
import matplotlib.pyplot as plt

def draw_DAG(edges):

    # Crear grafo dirigido acíclico
    G = nx.DiGraph()


    G.add_edges_from(edges)

    # Dibujar
    plt.figure(figsize=(6,4))
    pos = nx.nx_agraph.graphviz_layout(G, prog='dot')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, arrowsize=20)
    plt.title("Ejemplo de DAG")
    plt.show()

