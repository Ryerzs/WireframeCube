

class Node:
    def __init__(self):
        self.adjNodes = []
        self.edges = []
        pass
    def drawEdge(self):
        for node in self.adjNodes:
            self.edgeDrawn(node,True)
            node.self.edgeDrawn(self,True)
    def edgeDrawn(self, node, b):
        for e in self.edges:
            if e[0] == node:
                e[1] = b

        
