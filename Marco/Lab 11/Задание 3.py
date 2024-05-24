import matplotlib.pyplot as plt
import networkx as nx
from Задание_2 import path2

graph = {
    'L': {'O': 14, 'V': 10, 'E': 17},
    'O': {'V': 1, 'E': 5, 'L': 14},
    'V': {'E': 8, 'O': 1, 'L': 10},
    'E': {'O': 5, 'L': 17, 'V': 8}}

G = nx.DiGraph()

G.add_edge("L", "O", weight=14)
G.add_edge("L", "V", weight=10)
G.add_edge("L", "E", weight=17)
G.add_edge("O", "V", weight=1)
G.add_edge("O", "E", weight=5)
G.add_edge("O", "L", weight=14)
G.add_edge("V", "E", weight=8)
G.add_edge("V", "O", weight=1)
G.add_edge("V", "L", weight=10)
G.add_edge("E", "O", weight=5)
G.add_edge("E", "L", weight=17)
G.add_edge("E", "V", weight=8)

elarge = [(u, v) for (u, v, d, f) in G.edges(data=True) if (u, v) in path2]
esmall = [(u, v) for (u, v, d, f) in G.edges(data=True) if (u, v) not in path2]

pos = nx.spring_layout(G, seed=7)  #

nx.draw_networkx_nodes(G, pos, node_size=300)

nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
nx.draw_networkx_edges(G, pos, edgelist=esmall, width=2, alpha=0.5, edge_color="b", style="dashed")

nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()
