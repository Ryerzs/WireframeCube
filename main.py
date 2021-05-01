from cube import *

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
    cube = Cube(1)
    A = rotationMatrix('z',90)
    cube.transform(A)
    print(cube.getPos())
    