from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque()

    queue.append((0, 0))

    while queue:
        jug1, jug2 = queue.popleft()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        print(f"Jug1: {jug1} liters, Jug2: {jug2} liters")

        # ✅ Condition: one jug has 'target' and the other is 0
        if (jug1 == target and jug2 == 0) or (jug2 == target and jug1 == 0):
            print(f"✅ Reached the target: {jug1} liters and {jug2} liters (one jug is empty!)")
            return True

        next_states = [
            (jug1_capacity, jug2),  
            (jug1, jug2_capacity),  
            (0, jug2),              
            (jug1, 0),              
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1))
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)

    print("❌ Target cannot be reached.")
    return False

# 🚀 Take user input
jug1_capacity = int(input("Enter Jug1 capacity: "))
jug2_capacity = int(input("Enter Jug2 capacity: "))
target = int(input("Enter the target amount: "))

water_jug_bfs(jug1_capacity, jug2_capacity, target)
