import pytest
import networkx as nx
from graph import *

def main():
    edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (2, 5)]

    G = create_graph(edges)
    print("Graf berhasil dibuat!")

    node = 2
    degree = get_degree(G, node)
    print(f"Derajat node {node}: {degree}")

    start_node = 1
    dfs_result = dfs_traversal(G, start_node)
    print(f"Hasil DFS dari node {start_node}: {dfs_result}")

    bfs_result = bfs_traversal(G, start_node)
    print(f"Hasil BFS dari node {start_node}: {bfs_result}")

    source = 1
    target = 4
    shortest_path = find_shortest_path(G, source, target)
    print(f"Jalur terpendek dari {source} ke {target}: {shortest_path}")

    print("Menampilkan visualisasi graf...")
    visualize_graph(G)

if __name__ == "__main__":
    main()