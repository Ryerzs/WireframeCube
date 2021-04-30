
def transpose(mat):
    newMat = []
    if len(mat) != 0:
        for col in range(len(mat[0])):
            newRow = []
            for row in range(len(mat)):
                newRow.append(mat[row][col])
            newMat.append(newRow)
    return newMat

#Assuming n0<n1
def powers(mat,n0,n1):
    newMat = []
    for i in mat:
        newRow = []
        for deg in range(n0,n1+1):
            newRow.append(i**deg)
        newMat.append(newRow)
    return newMat        

#Assuming A is nxp, and B is pxm
def matmul(A, B):
    newMat = []
    p = len(B)
    n = len(A)
    if n==0 or p==0:
        return []
    m = len(B[0])
    for row in range(n):
        newRow = []
        for col in range(m):
            newRow.append(0)
            for A_i in range(p):
                newRow[col] += A[row][A_i]*B[A_i][col]
        newMat.append(newRow)
    return newMat

#invert 2x2 matrix
def invert(mat):
    detMat = det(mat)
    return[[ mat[1][1]/detMat, -mat[0][1]/detMat],
           [-mat[1][0]/detMat,  mat[0][0]/detMat]]

def det(mat):
    return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]

def loadtxt(path):
    file = open(path, mode="r", encoding="utf-8")
    return [[float(string) for string in line.split()] for line in file]