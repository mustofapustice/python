# Reading Number of vertices and edges
v, e = map(int, input().split())

# Initializing the matrix with infinities
# m = [[float('inf') if i != j else 0 for i in range(v)] for j in range(v)]
m = []
for j in range(v):
    row = []
    for i in range(v):
        if i != j:
             row.append(float('inf'))
        else: 
            row.append(0)
    m.append(row)
# Reading edges and updating the matrix
for i in range(e):
    src, dst, wt = map(int, input().split())
    m[src][dst] = wt
# [[7, 5, inf, inf],
#  [inf, 0, inf, 2], 
#  [inf, 3, 0, inf],
#  [4, inf, 1, 0  ]]

# Floyd-Warshall Algorithm
for k in range(v):
    for i in range(v):
        for j in range(v):
            m[i][j] = min(m[i][j], m[i][k] + m[k][j])

# Printing the final matrix
for i in range(v):
    for j in range(v):
        print(m[i][j], end=' ')
    print()

'''
Input: 
    4 6
    0 1 5
    1 3 2
    2 1 3
    0 0 7
    3 0 4
    3 2 1

Output:
    7 5 8 7 
    6 0 3 2 
    9 3 0 5 
    4 4 1 0 

'''

