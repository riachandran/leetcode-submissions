import networkx as nx
import numpy as np

def get_graph_path(graph, start_node, end_node, num_walks):
    if start_node == end_node:
        return 0
    path_length = 0
    for _ in range(num_walks):
        current_node = start_node
        path = 0
        while current_node != end_node:
            neighbors = list(graph.neighbors(current_node))
            if not neighbors: break
            current_node = np.random.choice(neighbors)
            path +=1
        path_length += path
    
    return path_length / num_walks if path_length > 0 else float('inf')

def compute_all_distance(graph,num_walks):
    nodes = list(graph.nodes())
    distance = {i: {j: 0 for j in nodes} for i in nodes}
    for i in nodes:
        for j in nodes:
            if i != j:
                distance[i][j] = get_graph_path(graph, i, j, num_walks)

    return distance

graph = nx.erdos_renyi_graph(5, 0.5)
distances = compute_all_distance(graph, 1000)
print("Graph:")
print(graph.nodes())
print(graph.edges())
print("Distance:")
print(compute_all_distance(graph, 100))
for i in distances:
        for j in distances[i]:
            print(f"Expected random walk distance from {i} to {j}: {distances[i][j]:.2f}")
