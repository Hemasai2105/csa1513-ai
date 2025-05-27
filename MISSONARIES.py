from collections import deque

def is_valid(state, total_m, total_c):
    m_left, c_left, boat = state
    m_right = total_m - m_left
    c_right = total_c - c_left

    # Check counts are in valid range
    if (m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0):
        return False

    # Check missionaries are not outnumbered on both sides
    if (m_left > 0 and m_left < c_left):
        return False
    if (m_right > 0 and m_right < c_right):
        return False

    return True

def get_successors(state, boat_capacity):
    successors = []
    m_left, c_left, boat = state
    moves = []

    # Generate all possible moves (1 to boat_capacity)
    for m in range(boat_capacity + 1):
        for c in range(boat_capacity + 1):
            if (m + c >= 1 and m + c <= boat_capacity):
                moves.append((m, c))

    for m, c in moves:
        if boat == 1:
            # Boat is on the left side, move people to the right
            new_state = (m_left - m, c_left - c, 0)
        else:
            # Boat is on the right side, move people to the left
            new_state = (m_left + m, c_left + c, 1)

        if is_valid(new_state, total_m, total_c):
            successors.append(new_state)

    return successors

def missionaries_and_cannibals(total_m, total_c, boat_capacity):
    initial_state = (total_m, total_c, 1)  # (M_left, C_left, boat_position)
    goal_state = (0, 0, 0)

    queue = deque()
    queue.append((initial_state, [initial_state]))
    visited = set()

    while queue:
        (current_state, path) = queue.popleft()

        if current_state[:2] == goal_state[:2]:
            print("✅ Solution found! Path:")
            for step in path:
                m_left, c_left, boat = step
                side = "Left" if boat == 1 else "Right"
                print(f"Missionaries Left: {m_left}, Cannibals Left: {c_left}, Boat: {side}")
            return

        for successor in get_successors(current_state, boat_capacity):
            if successor not in visited:
                visited.add(successor)
                queue.append((successor, path + [successor]))

    print("❌ No solution found.")

# 🚀 Take user input
total_m = int(input("Enter the number of Missionaries: "))
total_c = int(input("Enter the number of Cannibals: "))
boat_capacity = int(input("Enter the boat capacity: "))

missionaries_and_cannibals(total_m, total_c, boat_capacity)
