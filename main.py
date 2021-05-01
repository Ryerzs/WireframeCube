from cube import *

if __name__ == '__main__':
    cube = Cube(1)
    cube.rotate('z', 90)
    print(cube.getPos())
    