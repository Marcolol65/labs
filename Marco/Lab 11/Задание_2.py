from Задание_1 import dijk, PATH

graph = {
    'L': {'O': 14, 'V': 10, 'E': 17},
    'O': {'V': 1, 'E': 5, 'L': 14},
    'V': {'E': 8, 'O': 1, 'L': 10},
    'E': {'O': 5, 'L': 17 ,'V': 8}}


x, y = dijk(graph, 'L')
path = PATH('E', y)
path2 = set()

for i in range(len(path)-1):
    path2.add((path[i], path[i+1]))
    print(path[i], path[i+1], sep='-->')
