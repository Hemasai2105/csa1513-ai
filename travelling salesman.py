from itertools import permutations

# Function to solve TSP using brute-force
def tsp(graph, start):
    n = len(graph)
    cities = list(range(n))
    cities.remove(start)

    min_cost = float('inf')
    best_path = []

    # Try all possible orders of visiting the cities
    for perm in permutations(cities):
        current_cost = 0
        k = start
        path = [start]

        # Calculate cost for this permutation
        for j in perm:
            current_cost += graph[k][j]
            path.append(j)
            k = j

        # Add cost to return to start city
        current_cost += graph[k][start]
        path.append(start)

        # Update minimum if current is better
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = path

    return min_cost, best_path

# Sample graph as adjacency matrix
graph = [
    [0, 10, 15, 20],   # Distances from city 0
    [10, 0, 35, 25],   # Distances from city 1
    [15, 35, 0, 30],   # Distances from city 2
    [20, 25, 30, 0]    # Distances from city 3
]

# Start the tour from city 0
cost, path = tsp(graph, 0)

# Display result
print("Minimum cost:", cost)
print("Best path:", path)
