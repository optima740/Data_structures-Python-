class Vertex:
    
    def __init__(self, val):
        self.Value = val

class SimpleGraph:
    
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for i in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        # метод добавления новой вершины
        # с значением value
        # в свободное место массива vertex
        for i in range(len(self.vertex)):
            if self.vertex[i] != None and self.vertex[i].Value == v:
                return
            if self.vertex[i] == None:
                my_vertex = Vertex(v)
                self.vertex[i] = my_vertex
                return

    def AddEdge(self, v1, v2):
        # добавление ребра между вершинами v1 и v2
        index_v1 = v1
        index_v2 = v2
        if index_v1 != None and index_v2 != None:
            self.m_adjacency[index_v1][index_v2] = 1
            self.m_adjacency[index_v2][index_v1] = 1

    def IsEdge(self, v1, v2):
        # True если есть ребро между вершинами v1 и v2
        index_v1 = v1
        index_v2 = v2
        if (index_v1 != None and index_v2 != None) and (self.m_adjacency[index_v1][index_v2] == 1) and (self.m_adjacency[index_v2][index_v1] == 1):
            return True
        else:
            return False

    def RemoveVertex(self, v):
        #метод удаления вершины со всеми её рёбрами
        index_vertext = v
        if index_vertext != None:
            for vert in self.vertex:
                if vert != None and self.IsEdge(index_vertext, self.vertex.index(vert)) == True:
                    self.RemoveEdge(index_vertext, self.vertex.index(vert))
            self.vertex[index_vertext] = None
        
    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        index_v1 = v1
        index_v2 = v2
        if index_v1 != None and index_v2 != None:
            self.m_adjacency[index_v1][index_v2] = 0
            self.m_adjacency[index_v2][index_v1] = 0

    def PrintAllAdjacency(self):
        print('Vertext:')
        for vert in self.vertex:
            if vert != None:
                print(vert.Value,' ', end ='')
            else:
                print('None ', end='')
        print()
        print('m_adjacency:')
        for i in self.m_adjacency:
            for j in i:
                print ("{:4d}".format(j), end ="")
            print()
            
"""
my_graph = SimpleGraph(5)
my_graph.AddVertex('A')
my_graph.AddVertex('B')
my_graph.AddVertex('C')
my_graph.AddVertex('D')
my_graph.AddVertex('E')

my_graph.PrintAllAdjacency()

my_graph.AddEdge(0,1)
my_graph.AddEdge(0,2)
my_graph.AddEdge(0,3)
my_graph.AddEdge(1,0)
my_graph.AddEdge(1,3)
my_graph.AddEdge(1,4)
my_graph.AddEdge(2,0)
my_graph.AddEdge(2,3)
my_graph.AddEdge(3,3)
my_graph.AddEdge(3,0)
my_graph.AddEdge(3,1)
my_graph.AddEdge(3,2)
my_graph.AddEdge(3,4)
my_graph.AddEdge(4,3)
my_graph.AddEdge(4,1)
my_graph.RemoveVertex(4)
my_graph.RemoveVertex(3)

my_graph.PrintAllAdjacency()
"""
