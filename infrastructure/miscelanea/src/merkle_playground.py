import hashlib
from graphviz import Digraph

leaves = None
levels = None

def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

def build_merkle_tree(leaves):
    levels = []
    current = [hash_data(x) for x in leaves]
    levels.append(current)
    while len(current) > 1:
        next_level = []
        for i in range(0, len(current), 2):
            left = current[i]
            right = current[i+1] if i+1 < len(current) else left
            combined = hash_data(left + right)
            next_level.append(combined)
        current = next_level
        levels.append(current)
    return levels

def draw_merkle_tree(levels, leaves):
    dot = Digraph()
    node_ids = {}

    # Nivel 0: hojas
    for i, leaf in enumerate(leaves):
        h = hash_data(leaf)
        node_id = f"L0_{i}"
        label = f"{leaf}\\n{h[:12]}..."
        dot.node(node_id, label)
        node_ids[(0, i)] = node_id

    # Niveles intermedios
    for level_idx in range(1, len(levels)):
        for idx, val in enumerate(levels[level_idx]):
            node_id = f"L{level_idx}_{idx}"
            label_hash = f"{val[:12]}..."

            # Agregar etiqueta del dato combinado solo si no es la raíz
            if level_idx < len(levels) - 1:
                left_i = idx * 2
                right_i = left_i + 1 if left_i + 1 < len(levels[level_idx - 1]) else left_i
                left_data = leaves[left_i] if level_idx == 1 else f"L{level_idx-1}_{left_i}"
                right_data = leaves[right_i] if level_idx == 1 else f"L{level_idx-1}_{right_i}"
                label = f"{leaves[left_i]} + {leaves[right_i]}\\n{label_hash}"
            else:
                label = f"raíz\\n{label_hash}"

            dot.node(node_id, label)
            node_ids[(level_idx, idx)] = node_id

            # Conexión con hijos
            child_idx = idx * 2
            for j in [0, 1]:
                if child_idx + j < len(levels[level_idx - 1]):
                    child_node = node_ids[(level_idx - 1, child_idx + j)]
                    dot.edge(child_node, node_id)

    return dot

