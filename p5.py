import numpy as np

def intersection(mat1, mat2):
    # intersect = [[(mat1[i][j] and mat2[i][j]) for j in range(len(mat1[0]))] for i in range(len(mat1))]
    intersect = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] and mat2[i][j])
        intersect.append(row)
    return intersect
def union(mat1, mat2):
    # uni = [[(mat1[i][j] or mat2[i][j]) for j in range(len(mat1[0]))] for i in range(len(mat1))]
    uni = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[i])):
            row.append(mat1[i][j] or mat2[i][j])
        uni.append(row)   
    return uni

matrix1 = [[1, 0, 1],
           [1, 0, 0],
           [0, 1, 1]]
matrix2 = [[1, 0, 1],
           [0, 1, 1],
           [1, 0, 1]]
v = ['p', 'q', 'r']
# For displaying inputs...
rm1 = np.array(matrix1).reshape(3, 3)
rm2 = np.array(matrix2).reshape(3, 3)
print("Matrix A = \n", rm1)
print("Matrix B = \n", rm2)

mi = intersection(matrix1, matrix2)
mis = np.array(mi).reshape(3, 3)
# r1 = [(v[i], v[j]) for i in range(len(mi)) for j in range(len(mi[0])) if mi[i][j] == 1]
r1 = []
for i in range(len(mi)):
    for j in range(len(mi[0])):
        if mi[i][j] == 1:
           r1.append((v[i], v[j])) 
          
print("Matrix intersection = \n", mis)
print(r1)

mu = union(matrix1, matrix2)
mus = np.array(mu).reshape(3, 3)
# r2 = [(v[i], v[j]) for i in range(len(mu)) for j in range(len(mu[0])) if mu[i][j] == 1]
r2 = []
for i in range(len(mu)):
    for j in range(len(mu[0])):
        if mu[i][j] == 1:
            r2.append((v[i],v[j]))
print("Matrix Union = \n", mus)
print(r2)



'''
Output:
Matrix A = 
[[1 0 1]
 [1 0 0]
 [0 1 1]]
Matrix B = 
[[1 0 1]
 [0 1 1]
 [1 0 1]]
Matrix intersection = 
 [[1 0 1]
 [0 0 0]
 [0 0 1]]
[('p', 'p'), ('p', 'r'), ('r', 'r')]
Matrix Union = 
[[1 0 1]
 [1 1 1]
 [1 1 1]]
[('p', 'p'), ('p', 'r'), ('q', 'p'), ('q', 'q'), ('q', 'r'), ('r', 'p'), ('r', 'q'), ('r', 'r')]


'''