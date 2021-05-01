from graphics import *

class GNode:
    def __init__(self, win, node):
        self.win = win
        self.node = node
        self.setPos(self.node.pos)
        self.lines = []

    def drawEdges(self):
        for n in self.node.adjNodes:
            #Need to only draw line if line hasn't been drawn between this node

            #Save points so that it automatically updates
            pos1 = self.getPos()
            pos2 = n.getPos()
            p1 = Point(pos1[0], pos1[1])
            p2 = Point(pos2[0], pos2[1])
            self.lines.append(Line(p1, p2))
            self.lines[-1].setFill("white")
            self.lines[-1].draw(self.win)
            #
            #
            self.edgeDrawn(n,True)
            n.edgeDrawn(self,True)
            
    def edgeDrawn(self, node, b):
        for e in self.node.edges:
            if e[0] == node:
                e[1] = b

    def addAdjNodes(self,nodes):
        self.node.addAdjNodes(nodes)
    
    def getPos(self):
        return self.node.getPos()

    def setPos(self, pos):
        self.node.setPos(pos)
    
    def update(self):
        for line in self.lines:
            line.undraw()
        self.lines = []
        self.drawEdges()