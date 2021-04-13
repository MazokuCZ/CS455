class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []
 
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
 
 
    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])
 
    def apply_union(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
  
    def kruskal(self):
        result = []
        r = ["Home", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "Stadium"]
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("Edge:",r[u],'is connected to edge:', r[v],'with cost',end =" ")
            print("-",weight)

g = Graph(12)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 5)
g.add_edge(0, 3, 9)
g.add_edge(1, 4, 3)
g.add_edge(2, 5, 5)
g.add_edge(2, 9, 20)
g.add_edge(3, 5, 2)
g.add_edge(4, 6, 1)
g.add_edge(5, 9, 12)
g.add_edge(5, 7, 7)
g.add_edge(6, 8, 2)
g.add_edge(6, 9, 11)
g.add_edge(6, 10, 5)
g.add_edge(7, 10, 8)
g.add_edge(8, 11, 4)
g.add_edge(9, 11, 6)
g.add_edge(10, 11, 11)
g.kruskal()
