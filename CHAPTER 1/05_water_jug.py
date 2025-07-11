def water_jug():
    visited = set()
    queue = [(0, 0)]
    while queue:
        a, b = queue.pop(0)
        if (a, b) in visited:
            continue
        visited.add((a, b))
        print(f"A: {a}L, B: {b}L")
        if a == 2 or b == 2:
            print("Goal reached")
            return
        queue += [
            (4, b), (a, 3), (0, b), (a, 0),
            (min(a + b, 4), max(0, a + b - 4)),
            (max(0, a + b - 3), min(a + b, 3))
        ]

water_jug()