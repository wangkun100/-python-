import numpy as np
from math import *

def CondJ(a,b,h,ra,rb):

    q = 3**0.5
    f1_a = 2*h*ra*sin(a)*sin(b)
    f1_b = -2*h*ra*cos(a)*cos(b) + 2*ra*rb*sin(b)
    f1_h = 2*h - 2*ra*sin(b)*cos(a)

    f2_a = h*q*ra*cos(a) - h*ra*sin(a)*sin(b) + q**2*ra*rb*sin(a)/2 + q*ra*rb*sin(b)*cos(a)/2
    f2_b = h*ra*cos(a)*cos(b) + q*ra*rb*sin(a)*cos(b)/2 + ra*rb*sin(b)/2
    f2_h = 2*h + q*ra*sin(a) + ra*sin(b)*cos(a)

    f3_a = -h*q*ra*cos(a) - h*ra*sin(a)*sin(b) + q**2*ra*rb*sin(a)/2 - q*ra*rb*sin(b)*cos(a)/2
    f3_b = h*ra*cos(a)*cos(b) - q*ra*rb*sin(a)*cos(b)/2 + ra*rb*sin(b)/2
    f3_h = 2*h - q*ra*sin(a) + ra*sin(b)*cos(a)

    J = np.array([[f1_a, f1_b, f1_h], [f2_a, f2_b, f2_h], [f3_a, f3_b, f3_h]])
    J = np.dot(J,J.T)
    a, b = np.linalg.eig(J)
    return (max(a)/min(a))**0.5

# a = CondJ(0,0,87,70,40)
# print(a)


def aimfunc(Phen, CV):

    f = []

    x1 = Phen[:, [0]]  # 获取表现型矩阵的第一列，得到所有个体的x1的值
    x2 = Phen[:, [1]]

    for i in range(0,len(x1)):

        result1 = CondJ(0,0,100,float(x1[i]),float(x2[i]))
        result2 = CondJ(0, 0, 110, float(x1[i]), float(x2[i]))
        result3 = CondJ(0, 0, 90, float(x1[i]), float(x2[i]))
        result = (result1 + result2 + result3)*100
        # print(result)

        f.append(result)

    f = np.array([f])

    f = f.T

    return [f,CV]

# Phen = np.array([[10,20],[30,40]])
# CV = np.array([[0],[0]])
#
# (f,cv) = aimfunc(Phen,CV)
# print(f)

