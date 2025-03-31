'''
# Description:
This program finds the shortest path between nodes in a weighted graph using Dijkstra's algorithm. It calculates both the shortest distance and the path taken from a given starting node to a target node (or all nodes if no target is specified).

#What It Does:

Graph Representation:
 - The graph is stored as a dictionary where each node has a list of connected nodes along with their respective edge weights.
 - Dijkstra’s Algorithm Implementation:
 - Initializes all distances to infinity except for the starting node (set to 0).
 - Iteratively selects the unvisited node with the smallest distance.
 - Updates distances to neighboring nodes if a shorter path is found.
 - Maintains a record of the shortest path sequence for each node.

Output:
 - If a target node is specified, it prints the shortest distance and path to that node.
 - If no target is given, it prints the shortest paths to all nodes.

Example Usage:
Running shortest_path(my_graph, 'A', 'F') gives:

A-F distance: 6  
Path: A -> B -> F  

This program efficiently finds the optimal path in a weighted graph, making it ideal for route planning, network optimization, and problem-solving in graph theory. 🚀
'''

my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target = ''):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)
    
    while unvisited:
        current = min(unvisited, key=distances.get)
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)
    
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    return distances, paths
    
shortest_path(my_graph, 'A', 'F')