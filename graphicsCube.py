from cube import *
from graphicsNode import *

class GCube():
    def __init__(self, win, r):
        self.win = win
        self.createCube(r)
        self.draw()
    
    def createCube(self, r):
        self.cube = Cube(r)
        self.gNodes = []
        for n in self.cube.nodes:
            self.gNodes.append(GNode(self.win, n))
    
    def draw(self):
        for n in self.gNodes:
            n.drawEdges()
    
    def getPos(self):
        return self.cube.getPos()

    def setPos(self, pos):
        self.cube.setPos(pos)

    def transform(self, A):
        self.cube.transform(A)
    
    def update(self):
        for n in self.gNodes:
            n.update()