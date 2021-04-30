from node import *

def createCube():
    n1 = Node(( 1/2,  1/2,  1/2))
    n2 = Node((-1/2,  1/2,  1/2))
    n3 = Node((-1/2, -1/2,  1/2))
    n4 = Node(( 1/2, -1/2,  1/2))
    n5 = Node(( 1/2,  1/2, -1/2))
    n6 = Node((-1/2,  1/2, -1/2))
    n7 = Node((-1/2, -1/2, -1/2))
    n8 = Node(( 1/2, -1/2, -1/2))

    n1.addAdjNodes([n2, n4, n5])
    n3.addAdjNodes([n2, n4, n7])
    n6.addAdjNodes([n2, n5, n7])
    n8.addAdjNodes([n4, n5, n7])
    return [n1, n2, n3, n4, n5, n6, n7, n8]


if __name__ == '__main__':
    nodes = createCube()