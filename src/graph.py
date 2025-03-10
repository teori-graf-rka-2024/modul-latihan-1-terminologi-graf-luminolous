import networkx as nx
import matplotlib.pyplot as plt

def create_graph(edges: list[tuple[int, int]]) -> nx.Graph:
    # Membuat graf dari daftar edge
    G = nx.Graph()
    G.add_edges_from(edges)
    return G

def get_degree(G: nx.Graph, node: int) -> int:
    # Mengembalikan derajat dari node tertentu
    return G.degree[node]

def dfs_traversal(G: nx.Graph, start: int) -> list[int]:
    # Traversal DFS mulai dari node start
    return list(nx.dfs_preorder_nodes(G, start))

def bfs_traversal(G: nx.Graph, start: int) -> list[int]:
    # Traversal BFS mulai dari node start
    return list(nx.bfs_tree(G, start))

def find_shortest_path(G: nx.Graph, source: int, target: int) -> list[int]:
    # Mencari jalur terpendek antara source dan target
    return nx.shortest_path(G, source, target)

def visualize_graph(G: nx.Graph) -> None:
    # Visualisasi graf menggunakan matplotlib
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700)
    plt.show()