from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

# Take input from user
graph = {}
n = int(input("Enter the number of nodes: "))

for i in range(n):
    node = input(f"Enter the name of node {i+1}: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start_node = input("Enter the starting node for BFS: ")

print("\nBreadth-First Search Traversal:")
bfs(graph, start_node)
