from graphicsModel import *
import math

def rotationMatrix(axis, deg):
    theta = deg*math.pi/180
    c = math.cos(theta)
    s = math.sin(theta)
    if axis == 'x':
        A = [[1, 0, 0], [0, c, -s], [0, s, c]]
    elif axis == 'y':
        A = [[c, 0, s], [0, 1, 0], [-s, 0, c]]
    elif axis == 'z':
        A = [[c, -s, 0], [s, c, 0], [0, 0, 1]]
    return A

def transformationMatrix(A,B):
    return matmul(A,B)

if __name__ == '__main__':
    win = GraphWin("Wireframe cube", 640, 640, autoflush=False)
    win.setCoords(-2,-2,2,2)
    win.setBackground("black")
    cube = GCube(win, 1)
    Az = rotationMatrix('z',0.5)
    Ax = rotationMatrix('x',0.8)
    A  = transformationMatrix(Az,Ax)
    while(1):
        cube.transform(A)
        cube.update()
        update(50)
    