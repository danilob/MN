
#refering: https://www.programiz.com/python-programming/matrix
#exemple: https://www.youtube.com/watch?v=pf4l8gv_dCM (22'30'')

import numpy as np

#TODO: line criteria
# https://www3.nd.edu/~zxu2/acms40390F12/Lec-7.3.pdf

def checkLineCriteria(A,n):
    for i in range(0,n):
        v = A[i][i]
        sum = 0
        for j in range (0,n):
            if i != j:
                sum = A[i][j] + sum
        if (sum > v):
            return False
    return True

def getNorm(n,x,v):
    normNum = 0
    normDen = 0
    for i in range(0,n):
        t = abs(v[i]-x[i])
        if (t>normNum):
            normNum = t
        if (abs(v[i])>normDen):
            normDen = abs(v[i])
        x[i] = v[i]
    return normNum/normDen

def checkResult(A,x,b,n):
    print("Result of system:")
    result = []
    for i in range(0,n):
        sum = 0
        for j in range (0,n):
            sum = A[i][j]*x[j] + sum
        result.append(sum)
    print(result)
    print("Real result:")
    print(b)

def getGaussJacobi(n,A,b,e,imax):
    if (checkLineCriteria):
        print("The equation system has passed through line criteria.")
    else:
        print("The equation system has NOT passed through line criteria.")
        return
    for i in range(0,n):
        r = 1/(A[i][i])
        for j in range (0,n):
            if i != j:
                A[i][j] = A[i][j] * r
        b[i] = b[i]*r
        x[i] = b[i]
    k=0
    while 1:
        k = k + 1
        v = []
        for i in range(0,n):
            sum = 0
            for j in range(0,n):
                if i != j:
                    sum = sum+A[i][j]*x[j]
            v.append(b[i]-sum)
        norm = getNorm(n,x,v)
        #write k, x and norm
        print('Vec X: ',x)
        print('Norm: ',norm)
        print('k: ',k)
        if norm <= e or k >= imax:
            break
    return x

def getGaussSidel(n,A,b,e,imax):
    if (checkLineCriteria):
        print("The equation system has passed through line criteria.")
    else:
        print("The equation system has NOT passed through line criteria.")
        return
    for i in range(0,n):
        r = 1/(A[i][i])
        for j in range (0,n):
            if i != j:
                A[i][j] = A[i][j] * r
        b[i] = b[i]*r
        x[i] = b[i]
    k=0
    while 1:
        k = k + 1
        v = []
        for i in range(0,n):
            sum = 0
            for j in range(0,n):
                if i != j:
                    sum = sum+A[i][j]*x[j]
            v.append(x[i])
            x[i] = b[i]-sum
            
        norm = getNorm(n,v,x)
        #write k, x and norm
        print('Vec X: ',x)
        print('Norm: ',norm)
        print('k: ',k)
        if norm <= e or k >= imax:
            break
    return x

import sys
try:
    f = open(sys.argv[1],"r")
    n = int(f.readline())
    A = []
    b = []
    Ao = []
    bo = []
    for i in range(0,n):
        v = f.readline().replace("\n","").split(" ")
        bi = float(v.pop(-1))
        v = (np.array(v)).astype(np.float)
        b.append(bi)
        A.append(v)
        bo.append(bi)
        Ao.append(v)
    x = (np.array(f.readline().replace("\n","").split(" "))).astype(np.float)
    e = float(f.readline())
    imax = int(f.readline())
    f.close()
except Exception as E:
    print(E)
    A = [
    [10,2,2],
    [1,10,2],
    [2,-7,-10]
    ]

    Ao = [
        [10,2,2],
        [1,10,2],
        [2,-7,-10]
    ]

    b = [28,7,-17]
    bo = [28,7,-17]
    e = 0.0001
    x = [0,0,0]
    imax = 10

while 1:
    op = int(input('Put 0 to Gauss-Jacobi or 1 to Gauss-Sidel: '))
    if(op==0 or op==1):
        break
if(op==0):
    z = getGaussJacobi(n,A,b,e,imax)
else:
    z = getGaussSidel(n,A,b,e,imax)


checkResult(Ao,z,bo,n)
