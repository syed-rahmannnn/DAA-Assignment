def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

def move(state, pos1, pos2):
    lst = list(state)
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return ''.join(lst)

def get_neighbors(state):
    idx = state.index('0')
    moves = []
    if idx >= 3: moves.append(move(state, idx, idx - 3))
    if idx <= 5: moves.append(move(state, idx, idx + 3))
    if idx % 3 > 0: moves.append(move(state, idx, idx - 1))
    if idx % 3 < 2: moves.append(move(state, idx, idx + 1))
    return moves

def bfs(start, goal):
    visited = set()
    queue = [(start, [start])]
    while queue:
        state, path = queue.pop(0)
        if state == goal:
            for p in path: print_board(p)
            return
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

bfs("724506831", "123456780")