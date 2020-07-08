import numpy as np
from sympy import *
import math

def J(a,b,h,ra,rb):

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
    # print(J)
    J = np.array(J, dtype='float')
    J = np.matrix(J)
    J1 = J.I
    # print(J1)
    return J1

def F(a,b,h,ra,rb,l1,l2,l3):

    q = 3 ** 0.5
    f1 = h**2 - 2*h*ra*sin(b)*cos(a) + ra**2 - 2*ra*rb*cos(b) + rb**2 - l1**2
    f2 = h**2 + h*q*ra*sin(a) + h*ra*sin(b)*cos(a) + q**2*ra**2/4 - q**2*ra*rb*cos(a)/2 + q**2*rb**2/4 + q*ra*rb*sin(a)*sin(b)/2 + ra**2/4 - ra*rb*cos(b)/2 + rb**2/4 - l2**2
    f3 = h**2 - h*q*ra*sin(a) + h*ra*sin(b)*cos(a) + q**2*ra**2/4 - q**2*ra*rb*cos(a)/2 + q**2*rb**2/4 - q*ra*rb*sin(a)*sin(b)/2 + ra**2/4 - ra*rb*cos(b)/2 + rb**2/4 - l3**2

    F = np.array([[f1],[f2],[f3]])
    # print(F)

    return F


print(F(0,0,75.9934208,70,45,80,80,80))




