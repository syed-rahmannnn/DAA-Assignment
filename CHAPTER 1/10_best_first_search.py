from queue import PriorityQueue

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristic[start], start))
    while not pq.empty():
        _, current = pq.get()
        if current in visited:
            continue
        print(current, end=" ")
        if current == goal:
            break
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))

graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
heuristic = {'A': 3, 'B': 2, 'C': 1, 'D': 0}
best_first_search(graph, 'A', 'D', heuristic)