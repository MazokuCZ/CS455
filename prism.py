from collections import defaultdict
import heapq

def create_spanning_tree(graph, starting_vertex):
    mst = defaultdict(set)
    visited = set([starting_vertex])
    edges = [
        (cost, starting_vertex, to)
        for to, cost in graph[starting_vertex].items()
    ]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[frm].add(to)
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))

    return mst

graph = {
    'Home': {'A': 5, 'B': 5, 'C': 9},
    'A': {'D': 3},
    'B': {'E': 5, 'I': 20},
    'C': {'E': 2,},
    'D': {'F': 1},
    'E': {'B': 4, 'D': 1, 'F': 1},
    'F': {'H': 2, 'Stadium': 9, 'J': 5},
    'G': {'J': 8},
    'H': {'Stadium': 4},
    'I': {'Stadium': 6},
    'J': {'Stadium': 11},
    'Stadium': {'I': 6, 'H': 4, 'J': 11},
    
}

thisdict = dict(create_spanning_tree(graph, 'Home'))
for x, y in thisdict.items():
  print('Edge:',x,'is connected to edge(s):', y)