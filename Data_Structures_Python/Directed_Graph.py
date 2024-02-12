class DirectedGraph:
    def __init__(self):
        self.adjacencyList = {}
    
    def __str__(self):
        for x in self.adjacencyList:
            print(f"{x}, {self.adjacencyList[x]}")

    def add_vertex(self, x):
        self.adjacencyList.setdefault(x, [])
        
    def add_edge(self, x, y):
        self.add_vertex(x)
        self.adjacencyList[x].append(y)