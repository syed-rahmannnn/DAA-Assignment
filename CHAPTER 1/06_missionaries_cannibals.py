def is_valid(state):
    M1, C1, B, M2, C2 = state
    return all(x >= 0 and x <= 3 for x in [M1, C1, M2, C2]) and            (M1 == 0 or M1 >= C1) and (M2 == 0 or M2 >= C2)

def successors(state):
    moves = [(1,0), (0,1), (1,1), (2,0), (0,2)]
    M1, C1, B, M2, C2 = state
    new_states = []
    for m, c in moves:
        if B == 1:
            new_state = (M1 - m, C1 - c, 0, M2 + m, C2 + c)
        else:
            new_state = (M1 + m, C1 + c, 1, M2 - m, C2 - c)
        if is_valid(new_state):
            new_states.append(new_state)
    return new_states

def solve():
    start = (3,3,1,0,0)
    goal = (0,0,0,3,3)
    visited, queue = set(), [(start, [start])]
    while queue:
        (state, path) = queue.pop(0)
        if state == goal:
            for p in path: print(p)
            return
        for s in successors(state):
            if s not in visited:
                visited.add(s)
                queue.append((s, path + [s]))

solve()