

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
    def addAdjNode(self,node):
        if node == self:
            return
        for e in self.adjNodes:
            if e == node:
                return
        self.addNodes.append(node)
        node.setAdjNode(self) 