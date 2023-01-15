def color_node(graph):
    color_map = {}
    for node in graph:
        #neighbours_colors = set(color_map.get(neigh) for neigh in graph[node])
        neighbours_colors = set()
        for neigh in graph[node]:
             color = color_map.get(neigh)
             neighbours_colors.add(color)
        #color_map[node] = next(color for color in range(len(graph)) if color not in neighbours_colors)
        for color in range(len(graph)):
            if color not in neighbours_colors:
                color_map[node] = color
                break
    
    return color_map

graph = {'a':list('bcd'), 'b': list('ac'), 'c': list('abdef'),
         'd': list('ace') , 'e': list('def') , 'f': list('ce')
         }

print(color_node(graph))

'''
Output:
    {'a': 0, 'b': 1, 'c': 2, 'd': 1, 'e': 0, 'f': 1}
    
    
    
    Initialize an empty dictionary "color_map" which will be used to store the mapping of nodes to colors.
    Iterate over the nodes in the graph, sorting them by the number of connections in descending order.
    For each node, create a set of the colors of its neighbours (using a set comprehension and the "color_map" dictionary to look up the colors of the neighbours).
    Assign the next available color (from a range of possible colors) to the current node that is not in the set of neighboring colors using next() and generator comprehension.
    Finally, return the "color_map" dictionary.
    graph is defined as an adjacency list (also called edges) where keys are nodes and values is the neighbours of that node.
    finally a call of the function with the sample graph is done and printed.
'''