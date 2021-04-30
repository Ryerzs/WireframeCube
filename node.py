

class Node:
    def __init__(self, pos):
        self.pos = pos
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
    def addAdjNodes(self,nodes):
        for n in nodes:
            if n == self:
                return
            for e in self.adjNodes:
                if e == n:
                    return
            self.adjNodes.append(n)
            n.addAdjNodes([self]) 
