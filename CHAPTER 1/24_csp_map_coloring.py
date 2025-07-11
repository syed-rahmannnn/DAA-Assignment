colors = ['Red', 'Green', 'Blue']
regions = {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B']}
solution = {}

def assign(region):
    for color in colors:
        if all(solution.get(neigh) != color for neigh in regions[region]):
            return color

for region in regions:
    solution[region] = assign(region)

print(solution)