import math

# Minimax with Alpha-Beta Pruning and Trace
def minimax(depth, node_index, is_max, values, alpha, beta, max_depth, path):
    indent = "  " * depth
    node_name = f"N{node_index} (depth={depth})"

    if depth == max_depth:
        print(f"{indent}Visited leaf {node_name} = {values[node_index]}")
        return values[node_index]

    if is_max:
        best = -math.inf
        print(f"{indent}MAX node {node_name}, alpha={alpha}, beta={beta}")
        for i in range(2):
            child_index = node_index * 2 + i
            val = minimax(depth + 1, child_index, False, values, alpha, beta, max_depth, path + [child_index])
            best = max(best, val)
            alpha = max(alpha, best)
            print(f"{indent}MAX node {node_name} updated best={best}, alpha={alpha}")
            if beta <= alpha:
                print(f"{indent}❌ Pruning at {node_name}, beta={beta} <= alpha={alpha}")
                break
        return best
    else:
        best = math.inf
        print(f"{indent}MIN node {node_name}, alpha={alpha}, beta={beta}")
        for i in range(2):
            child_index = node_index * 2 + i
            val = minimax(depth + 1, child_index, True, values, alpha, beta, max_depth, path + [child_index])
            best = min(best, val)
            beta = min(beta, best)
            print(f"{indent}MIN node {node_name} updated best={best}, beta={beta}")
            if beta <= alpha:
                print(f"{indent}❌ Pruning at {node_name}, beta={beta} <= alpha={alpha}")
                break
        return best

# ------------------------
# 🌟 USER INPUT SECTION
# ------------------------

max_depth = int(input("Enter the depth of the game tree (e.g., 3): "))
num_leaves = 2 ** max_depth

print(f"Enter {num_leaves} leaf node values (space-separated):")
values = list(map(int, input().split()))

if len(values) != num_leaves:
    print(f"Error: You must enter exactly {num_leaves} values.")
else:
    print("\n--- TRACE OUTPUT ---\n")
    optimal_value = minimax(0, 0, True, values, -math.inf, math.inf, max_depth, path=[])
    print("\n✅ The optimal value is:", optimal_value)
