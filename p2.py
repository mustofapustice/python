# for custom input
# n = int(input("Enter number of elements in A: "))
# A = list(map(int, input("Enter array elements: ").split()[:n]))
# m = int(input("Enter number of elements in B: "))
# B = list(map(int, input("Enter elements: ").split()[:m]))


import numpy as np

A = [1, 2, 3]
B = [1, 2]
output = []
for i in A:
    for j in B:
        if i > j:
            output.append((i, j))
print('All elements in set A = ', A)
print('All elements in set B = ', B)
print('Total order pair = ', len(output))
print('R = ', output)

# output2 = [1 if i > j else 0 for i in A for j in B]
output2 = []
for i in A:
    for j in B:
        if i > j:
            output2.append(1)
        else:
            output2.append(0)
rm = np.array(output2).reshape(len(A), len(B))
print('Relation Matrix = \n', rm)



'''
Output:
All elements in set A =  [1, 2, 3]
All elements in set B =  [1, 2]
Total order pair =  3
R =  [(2, 1), (3, 1), (3, 2)]
Relation Matrix = 
[[0 0]
 [1 0]
 [1 1]]
 
'''