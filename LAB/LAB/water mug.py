from collections import deque

# Function to solve the Water Jug Problem
def water_jug_problem(jug1_cap, jug2_cap, target):
    queue = deque([(0, 0, [])])  # (Jug1, Jug2, Path)
    visited = set()

    while queue:
        jug1, jug2, path = queue.popleft()

        # Skip if already visited
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))

        # Store current state
        path = path + [(jug1, jug2)]

        # Check if target is reached
        if jug1 == target or jug2 == target:
            print("Solution Found:")
            for state in path:
                print(state)
            return

        # Possible operations
        next_states = [
            (jug1_cap, jug2),                     # Fill Jug1
            (jug1, jug2_cap),                     # Fill Jug2
            (0, jug2),                            # Empty Jug1
            (jug1, 0),                            # Empty Jug2
            # Pour Jug1 -> Jug2
            (jug1 - min(jug1, jug2_cap - jug2),
             jug2 + min(jug1, jug2_cap - jug2)),
            # Pour Jug2 -> Jug1
            (jug1 + min(jug2, jug1_cap - jug1),
             jug2 - min(jug2, jug1_cap - jug1))
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    print("No Solution Exists")


# Main Program
jug1_capacity = 4
jug2_capacity = 3
target = 2

water_jug_problem(jug1_capacity, jug2_capacity, target)
