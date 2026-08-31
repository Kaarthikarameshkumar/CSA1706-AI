start = [
    [1, 2, 0],
    [3, 4, 6],
    [7, 5, 8]
]

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def moves(state):
    x, y = find_blank(state)

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    new_states = []

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]

            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

            new_states.append(new_state)

    return new_states


def state_to_tuple(state):
    return tuple(tuple(row) for row in state)


def dfs(state, path, depth, visited):

    if state == goal:
        return path + [state]

    if depth == 0:
        return None

    visited.add(state_to_tuple(state))

    for next_state in moves(state):

        if state_to_tuple(next_state) not in visited:

            result = dfs(next_state, path + [state], depth - 1, visited)

            if result:
                return result

    return None


solution = dfs(start, [], 30, set())

if solution:
    print("Solution Found")

    for step, state in enumerate(solution):
        print("\nStep", step)
        for row in state:
            print(row)
else:
    print("No Solution")
