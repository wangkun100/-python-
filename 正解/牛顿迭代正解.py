from J矩阵与F矩阵 import *
import numpy as np
from sympy import *
import math

def zj(l1, l2 ,l3):
    ra = 70
    rb = 45

    X = np.array([[0],[0],[3]])
    a = X[0][0]
    b = X[1][0]
    h = X[2][0]

    i=0

    while True:

        j = J(a,b,h,ra,rb)
        # j = J(0,0,3,20,16)
        f = F(a,b,h,ra,rb,l1,l2,l3)

        X = X - np.dot(j,f)

        if abs(float(f[0][0])) < 1e-4 and abs(float(f[1][0])) < 1e-4 and abs(float(f[2][0])) < 1e-4:
            # print("结束")
            # print(X)
            break
        else:
            i = i+1
            # print("第%d次计算"%(i))
            # print(X)
            a = float(X[0][0])
            b = float(X[1][0])
            h = float(X[2][0])

    print(X,i)

    return X,i

zj(90, 90 ,90)
zj(98, 75 ,93)
zj(90, 91 ,106)
zj(84, 98 ,95)
zj(80, 85 ,90)


