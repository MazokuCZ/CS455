from collections import defaultdict
from heapq import *

def dijkstra(edges, f, t):
    #creating queue
    g = defaultdict(list)
    for start,dest,cost in edges:
        g[start].append((cost,dest))
        
    #loop through heap priority queue
    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf"), None
    
def bell(edges, s, d):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen, mins = [(0,s,())], set(), {s: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == d: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf"), None
    
def main():
    edges = [
        ("A", "B", 1),
        ("A", "C", 3),
        ("C", "D", 2),
        ("C", "F", 2),
        ("F", "H", 1),
        ("F", "O", 3),
        ("F", "K", 2),
        ("H", "J", 5),
        ("H", "I", 5),
        ("K", "L", 5),
        ("K", "M", 3),
        ("M", "N", 1),
        ("M", "E", 6)
    ]
    
    edges2 = [
        ("X", "A", 5),
        ("X", "B", 5),
        ("X", "C", 9),
        ("A", "D", 3),
        ("D", "F", 1),
        ("F", "I", 2),
        ("F", "Z", 9),
        ("F", "J", 5),
        ("I", "Z", 4),
        ("B", "H", 20),
        ("B", "E", 5),
        ("C", "E", 2),
        ("E", "H", 12),
        ("E", "G", 7),
        ("G", "J", 8),
        ("H", "Z", 6),
        ("J", "Z", 11)
    ]

    print ("=== Dijkstra ===")
    print ("A -> E:")
    

    out = dijkstra(edges, "A", "E")
    data = {}
    data['cost']=out[0]
    aux=[]
    while len(out)>1:
        aux.append(out[0])
        out = out[1]
    aux.remove(data['cost'])
    aux.reverse()
    data['path']=aux
    print (data)
    
    print ("=== Bellford ===")
    print ("X(home) -> Z(stadium):")
    

    out = bell(edges2, "X", "Z")
    data = {}
    data['cost']=out[0]
    aux=[]
    while len(out)>1:
        aux.append(out[0])
        out = out[1]
    aux.remove(data['cost'])
    aux.reverse()
    data['path']=aux
    print (data)


main()