def lagrange(x, y, value, n):
    yp = 0
    # loop over all points
    for i in range(n):
        pro = 1
        # loop over all points again
        for j in range(n):
            # check if i is not equal to j
            if i != j:
                pro *= (value - x[j]) / (x[i] - x[j])
        yp += pro * y[i]
    return yp

n = 4
# input x values
x = [5, 6, 9, 11]
# input y values
y = [12, 13, 14, 16]
value = 10
print(lagrange(x, y, value, n))

'''
Output: 
    Value of f(10) is :  14.666666666666666
    
'''