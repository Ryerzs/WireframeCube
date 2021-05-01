

class Node:
    def __init__(self, pos):
        self.setPos(pos)
        self.adjNodes = []
        self.edges = []

    def drawEdge(self):
        for node in self.adjNodes:
            #draw here
            #
            #
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
    
    def getPos(self):
        return self.pos

    def setPos(self, pos):
        self.pos = pos