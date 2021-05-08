from matrix import *

class Cube():
    def __init__(self, r):
        self.r = r
        self.createCube()
    
    def createCube(self):
        r = self.r/2
        n1 = Node([ r,  r,  r])
        n2 = Node([-r,  r,  r])
        n3 = Node([-r, -r,  r])
        n4 = Node([ r, -r,  r])
        n5 = Node([ r,  r, -r])
        n6 = Node([-r,  r, -r])
        n7 = Node([-r, -r, -r])
        n8 = Node([ r, -r, -r])

        n1.addAdjNodes([n2, n4, n5])
        n3.addAdjNodes([n2, n4, n7])
        n6.addAdjNodes([n2, n5, n7])
        n8.addAdjNodes([n4, n5, n7])
        self.nodes = [n1, n2, n3, n4, n5, n6, n7, n8]
    
    def getPos(self):
        out = []
        for n in self.nodes:
            out.append(n.getPos())
        return out

    def setPos(self, pos):
        if len(pos) == 3:
            pos = transpose(pos)
        for i in range(len(pos)):
            self.nodes[i].setPos(pos[i])

    def transform(self, A):
        pos = self.getPos()
        pos = transpose(pos)
        pos = matmul(A,pos)
        self.setPos(pos)


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