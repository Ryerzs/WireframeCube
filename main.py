from node import *
from matrix import *
import math

def createCube():
    n1 = Node([ 1/2,  1/2,  1/2])
    n2 = Node([-1/2,  1/2,  1/2])
    n3 = Node([-1/2, -1/2,  1/2])
    n4 = Node([ 1/2, -1/2,  1/2])
    n5 = Node([ 1/2,  1/2, -1/2])
    n6 = Node([-1/2,  1/2, -1/2])
    n7 = Node([-1/2, -1/2, -1/2])
    n8 = Node([ 1/2, -1/2, -1/2])

    n1.addAdjNodes([n2, n4, n5])
    n3.addAdjNodes([n2, n4, n7])
    n6.addAdjNodes([n2, n5, n7])
    n8.addAdjNodes([n4, n5, n7])
    return [n1, n2, n3, n4, n5, n6, n7, n8]

def getPos(nodes):
    pos = []
    for n in nodes:
        pos.append(n.pos)
    return pos


if __name__ == '__main__':
    theta = 5*math.pi/180
    Az = [[math.cos(theta), -math.sin(theta), 0], [math.sin(theta), math.cos(theta), 0], [0, 0, 1]]
    nodes = createCube()
    pos = getPos(nodes)
    pos = transpose(pos)
    for i in range(45):
        pos = matmul(Az,pos)
        print(pos)