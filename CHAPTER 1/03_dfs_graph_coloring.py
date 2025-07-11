def dfs(graph, node, color, colors):
    colors[node] = color
    for neighbor in graph[node]:
        if colors.get(neighbor) == color:
            return False
        if neighbor not in colors and not dfs(graph, neighbor, 1 - color, colors):
            return False
    return True

graph = {0: [1, 3], 1: [0, 2], 2: [1], 3: [0]}
colors = {}
print("Bipartite" if dfs(graph, 0, 0, colors) else "Not Bipartite")