# Backtracking + CSP for Map Coloring Problem

class MapColoringCSP:
    def __init__(self, regions, neighbors, colors):
        self.regions = regions  # list of regions (variables)
        self.neighbors = neighbors  # adjacency list of neighbors
        self.colors = colors  # available colors
        self.assignment = {}  # current color assignments

    def is_consistent(self, region, color):
        # Check if the color assignment is consistent (no two adjacent regions have the same color)
        for neighbor in self.neighbors.get(region, []):
            if neighbor in self.assignment and self.assignment[neighbor] == color:
                return False
        return True

    def select_unassigned_variable(self):
        # Select a region with the smallest domain (MRV heuristic)
        unassigned = [r for r in self.regions if r not in self.assignment]
        return min(unassigned, key=lambda r: len(self.colors) - sum(self.is_consistent(r, color) for color in self.colors))

    def backtrack(self):
        # If all regions are assigned, we have a solution
        if len(self.assignment) == len(self.regions):
            return self.assignment

        # Select the next unassigned variable (region) using MRV heuristic
        region = self.select_unassigned_variable()

        for color in self.colors:
            if self.is_consistent(region, color):
                # Try assigning the color
                self.assignment[region] = color

                # Recursively attempt to assign colors to the rest of the regions
                result = self.backtrack()
                if result:
                    return result

                # If it fails, backtrack (remove the assignment)
                del self.assignment[region]

        return None

    def solve(self):
        return self.backtrack()

# Example map (regions and neighbors)
regions = ['A', 'B', 'C', 'D', 'E']
neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D']
}
colors = ['Red', 'Green', 'Blue', 'Yellow']  # 4 colors

# Initialize the CSP problem
map_coloring_problem = MapColoringCSP(regions, neighbors, colors)

# Solve the problem
solution = map_coloring_problem.solve()

# Print the result
if solution:
    print("Solution found:", solution)
else:
    print("No solution found.")
