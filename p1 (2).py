# input from file
# with open("test.txt",'r',encoding='utf-8') as g:
#     s = list(map(int,g.readlines()))
# ways of input
# n = int(input("Enter number of element: "))
# s = list(map(int, input("Enter array elements: ").split()[:n]))




from itertools import product 

A = [1, 2, 3, 4]
print("\nElements of A: " + str(A))

ur = [(i,j) for i,j in product(A,repeat = 2)]
print("Total pairs in Universal relation R = ", len(ur))
print("Universal relation of R= " + str(ur))

R1 = [(i,j) for i,j in product(A,repeat=2) if j%i == 0]
R2 = [(i,j) for i,j in product(A,repeat=2) if i<=j]

print("Total pairs in Relation R1 = ", len(R1))
print("Relation R1 = " + str(R1))
print("Total pairs in Relation R2 = ", len(R2))
print('Relation R2 = ' + str(R2))



'''

Output:
Elements of A: [1, 2, 3, 4]
Total pairs in Universal relation R =  16
Universal relation of R= [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4)]
Total pairs in Relation R1 =  8
Relation R1 = [(1, 1), (2, 1), (2, 2), (3, 1), (3, 3), (4, 1), (4, 2), (4, 4)]
Total pairs in Relation R2 =  10
Relation R2 = [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
'''