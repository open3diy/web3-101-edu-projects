import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from matplotlib.animation import FuncAnimation
import random
from heapq import heappush, heappop


def run(title, interval=1250, origin=0, total_nodes=8, async_mode=False, simulate_delay=False):
    if origin < 0 or origin >= total_nodes:
        raise ValueError(f"El nodo de origen {origin} está fuera del rango válido (0 a {total_nodes - 1})")
    # Crear grafo con 'total_nodes' nodos conectados entre sí (red P2P)
    G = nx.generators.random_graphs.erdos_renyi_graph(n=total_nodes, p=0.4, seed=42)
    pos = nx.spring_layout(G, seed=42, k=0.8)

    # Simulación de propagación tipo IPFS
    content_origin = origin
    propagation_schedule = []

    if async_mode:
        received_time = {n: float('inf') for n in G.nodes}
        received_time[content_origin] = 0
        has_content = {n: False for n in G.nodes}
        has_content[content_origin] = True

        delivered = set([content_origin])
        propagation_schedule_dict = {}
        event_queue = []

        for neighbor in G.neighbors(content_origin):
            delay = random.uniform(0, 0.1) if simulate_delay else 0
            arrival_time = delay
            if received_time[neighbor] > arrival_time:
                received_time[neighbor] = arrival_time
                heappush(event_queue, (arrival_time, content_origin, neighbor))

        while event_queue:
            arrival_time, src, dst = heappop(event_queue)
            if dst in delivered:
                continue
            received_time[dst] = arrival_time
            delivered.add(dst)
            bucket = round(arrival_time / 0.05)
            propagation_schedule_dict.setdefault(bucket, []).append((src, dst))
            for neighbor in G.neighbors(dst):
                if neighbor not in delivered:
                    delay = random.uniform(0, 0.1) if simulate_delay else 0
                    heappush(event_queue, (arrival_time + delay, dst, neighbor))

        for t in sorted(propagation_schedule_dict):
            propagation_schedule.append(propagation_schedule_dict[t])

    else:
        has_content = {n: False for n in G.nodes}
        has_content[content_origin] = True
        propagation_queue = [content_origin]
        propagation_schedule = []

        while propagation_queue:
            current = propagation_queue.pop(0)
            neighbors = list(G.neighbors(current))
            random.shuffle(neighbors)
            round_transfers = []
            for neighbor in neighbors:
                if not has_content[neighbor]:
                    has_content[neighbor] = True
                    propagation_queue.append(neighbor)
                    round_transfers.append((current, neighbor))
            if round_transfers:
                propagation_schedule.append(round_transfers)

    # Resetear estado
    has_content = {n: (n == content_origin) for n in G.nodes}

    step_duration = 5

    fig, ax = plt.subplots(figsize=(8, 6))
    transfers = []

    def update(frame):
        ax.clear()
        nx.draw_networkx_nodes(
            G, pos,
            node_color=["green" if has_content[n] else "lightgray" for n in G.nodes],
            node_size=900,
            ax=ax
        )
        nx.draw_networkx_edges(G, pos, ax=ax)
        nx.draw_networkx_labels(G, pos, ax=ax)

        current_round = frame // step_duration
        progress = (frame % step_duration) / step_duration

        if current_round < len(propagation_schedule):
            for src, dst in propagation_schedule[current_round]:
                x_src, y_src = pos[src]
                x_dst, y_dst = pos[dst]
                x = x_src + (x_dst - x_src) * progress
                y = y_src + (y_dst - y_src) * progress
                ax.plot(x, y, marker="s", color="black", markersize=14, alpha=0.2)
                ax.plot(x, y, marker="s", color="gray", markersize=10)
                if simulate_delay:
                    ax.text(x, y + 0.03, f"{received_time[dst]*1000:.0f}ms", fontsize=8, ha='center')
                if frame % step_duration == step_duration - 1:
                    if not has_content[dst]:
                        has_content[dst] = True
                        transfers.append((src, dst))

        for src, dst in transfers:
            x = [pos[src][0], pos[dst][0]]
            y = [pos[src][1], pos[dst][1]]
            ax.plot(x, y, color='blue', linewidth=2.5, alpha=0.6)

        ax.set_title(title)
        ax.axis('off')

    total_frames = (len(propagation_schedule) + 2) * step_duration
    ani = FuncAnimation(fig, update, frames=total_frames, interval=interval//step_duration, repeat=False)
    return fig, ani
