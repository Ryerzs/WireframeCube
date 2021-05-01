from node import *
from matrix import *
import math

class Cube():
    def __init__(self, r):
        self.r = r
        self.createCube(self.r)
    
    def createCube(self, r):
        r = r/2
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

    def rotate(self, axis, deg):
        theta = deg*math.pi/180
        c = math.cos(theta)
        s = math.sin(theta)
        if axis == 'x':
            A = [[math.cos(theta), -math.sin(theta), 0], [math.sin(theta), math.cos(theta), 0], [0, 0, 1]]
        elif axis == 'y':
            A = [[math.cos(theta), -math.sin(theta), 0], [math.sin(theta), math.cos(theta), 0], [0, 0, 1]]
        elif axis == 'z':
            A = [[c, -s, 0], [s, c, 0], [0, 0, 1]]
        pos = self.getPos()
        pos = transpose(pos)
        pos = matmul(A,pos)
        self.setPos(pos)