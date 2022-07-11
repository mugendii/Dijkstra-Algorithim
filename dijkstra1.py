import sys
# import
graph ={


        'A': {'B': 1, 'C': 4, 'D': 2},
        'B': {'A': 9, 'E': 5},
        'C': {'A': 4, 'F': 15},
        'D': {'A': 10, 'F': 7},
        'E': {'B': 3, 'J': 7},
        'F': {'C': 11, 'D': 14, 'K': 3, 'G': 9},
        'G': {'F': 12, 'I': 4},
        'H': {'J': 13},
        'I': {'G': 6, 'J': 7},
        'J': {'H': 2, 'I': 4},
        'K': {'F': 6}
}

def Dijkstra(graph,start,node):
 print("initial_graph()")

predesessor = 'A'   #starting point

shortest_path = {}

unvisited_node = {}

queue = []

graph = graph

for node in graph:
    shortest_path[node] = float("inf")
    unvisited_node[node] = None
    queue.append(node)

shortest_path[predesessor] = 0
# evaluate shortest distance which wasn't marked as current
while queue:
    key_min = queue[0]
    min_val = shortest_path[key_min]
    for n in range(1, len(queue)):
        if shortest_path[queue[n]] < min_val:
            key_min = queue[n]
            min_val = shortest_path[key_min]
    current_node = key_min
    queue.remove(current_node)
    print(current_node)

    for i in graph[current_node]:
        alternate = graph[current_node][i] + shortest_path[current_node]
        if shortest_path[i] > alternate:
            shortest_path[i] = alternate
            unvisited_node[i] = current_node

x = 'H'
print('The path between A to H')
print(x, end='<-')
while True:
    x = unvisited_node[x]
    if x is None:
        print("")
        break
    print(x, end='<-')