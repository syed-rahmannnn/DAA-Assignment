game_tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}

def traverse(node):
    print(node)
    for child in game_tree[node]:
        traverse(child)

traverse('A')