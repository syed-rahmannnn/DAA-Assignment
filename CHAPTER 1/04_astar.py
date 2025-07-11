from queue import PriorityQueue

def astar(start, goal, graph, h):
    open_set = PriorityQueue()
    open_set.put((h[start], start))
    came_from, g_score = {}, {start: 0}
    while not open_set.empty():
        _, current = open_set.get()
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1] + [goal]
        for neighbor, cost in graph[current]:
            tentative = g_score[current] + cost
            if tentative < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative
                open_set.put((tentative + h[neighbor], neighbor))
    return []

graph = {'A': [('B', 1), ('C', 4)], 'B': [('D', 5)], 'C': [('D', 1)], 'D': []}
heuristic = {'A': 7, 'B': 6, 'C': 2, 'D': 0}
print(astar('A', 'D', graph, heuristic))