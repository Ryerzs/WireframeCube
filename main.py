from node import *

if __name__ == '__main__':
    node1 = Node()
    node2 = Node()
    print(node1.adjNodes)
    print(node2.adjNodes)
    node1.addAdjNode(node2)
    print(node1.adjNodes)
    print(node2.adjNodes)