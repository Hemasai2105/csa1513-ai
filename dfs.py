def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    print(start, end=" ")
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Take input from user
graph = {}
n = int(input("Enter the number of nodes: "))

for i in range(n):
    node = input(f"Enter the name of node {i+1}: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start_node = input("Enter the starting node for DFS: ")

print("\nDepth-First Search Traversal:")
dfs(graph, start_node)
