import scipy.linalg 
from random import randint

def createMatrix(n):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            if j >= i:
                
                matrix[i].append(str(randint(-64,64)))
            else:
                matrix[i].append(matrix[j][i])
    return matrix
def calculteQR(matriz): 
    Q, R = scipy.linalg.qr(matriz)
    for i in range(len(Q)):
        for j in range(len(Q)):
            Q[i][j]=round(Q[i][j], 2)
    for i in range(len(R)):
        for j in range(len(R)):
            R[i][j]=round(R[i][j], 2)

    return Q,R  
    
