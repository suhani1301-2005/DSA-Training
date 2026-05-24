'''
consider this graph

text
     A------B
     |      |
     |      |
     C------D

A-B, A-C, B-D, C-D 

Adjancency matrix

    A   B   C   D   E
A   0  1   1    1   0
B   1  0   0    0   1
C   1  0   0    1   0
D   1  0   1    0   1
E   0  1   0    1   0
     
''' 

class Graph:
    def __init__(self,vertices):
        #Total number of vertices
        self.V = vertices

        #Creates adjacency matrix with all 0's
        self.matrix = [[0 for _ in range(vertices)] 
                        for _ in range(vertices)]

    def display(self):
        for row in self.matrix:
            print(row)

    def add_edge(self,u,v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    def remove_edge(self,u,v):
        self.matrix

g = Graph(4)

g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,0)
g.add_edge(1,3)
g.add_edge(2,0)
g.add_edge(2,3)
g.add_edge(3,1)
g.add_edge(3,2)
print("Adjancency matrix ")
g.display()
