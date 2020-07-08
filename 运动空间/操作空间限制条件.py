import numpy as np
from sympy import *
import math
from math import *

def Angle(a,b,ra,rb,h):

    q = 3**0.5

    # 动平台三个点
    b1 = np.array([h*sin(b)*cos(a) + rb*cos(b),-h*sin(a),h*cos(a)*cos(b) - rb*sin(b)])
    b2 = np.array([h*sin(b)*cos(a) + q*rb*sin(a)*sin(b)/2 - rb*cos(b)/2,-h*sin(a) + q*rb*cos(a)/2,h*cos(a)*cos(b) + q*rb*sin(a)*cos(b)/2 + rb*sin(b)/2])
    b3 = np.array([h*sin(b)*cos(a) - q*rb*sin(a)*sin(b)/2 - rb*cos(b)/2,-h*sin(a) - q*rb*cos(a)/2,h*cos(a)*cos(b) - q*rb*sin(a)*cos(b)/2 + rb*sin(b)/2])

    # 定平台三个点
    a1 = np.array([ra,0,0])
    a2 = np.array([-ra/2,q*ra/2,0])
    a3 = np.array([-ra/2,-q*ra/2,0])

    # 动平台单位法向量
    n_b = np.array([(q*rb*(-q*rb*sin(a)*cos(b)/2 + 3*rb*sin(b)/2)*cos(a)/2 + q*rb*(q*rb*sin(a)*cos(b)/2 + 3*rb*sin(b)/2)*cos(a)/2)*(((-q*rb*sin(a)*sin(b)/2 - 3*rb*cos(b)/2)*(q*rb*sin(a)*cos(b)/2 + 3*rb*sin(b)/2) - (q*rb*sin(a)*sin(b)/2 - 3*rb*cos(b)/2)*(-q*rb*sin(a)*cos(b)/2 + 3*rb*sin(b)/2))**2 + (-q*rb*(-q*rb*sin(a)*sin(b)/2 - 3*rb*cos(b)/2)*cos(a)/2 - q*rb*(q*rb*sin(a)*sin(b)/2 - 3*rb*cos(b)/2)*cos(a)/2)**2 + (q*rb*(-q*rb*sin(a)*cos(b)/2 + 3*rb*sin(b)/2)*cos(a)/2 + q*rb*(q*rb*sin(a)*cos(b)/2 + 3*rb*sin(b)/2)*cos(a)/2)**2)**(-0.5),((-q*rb*sin(a)*sin(b)/2 - 3*rb*cos(b)/2)*(q*rb*sin(a)*cos(b)/2 + 3*rb*sin(b)/2) - (q*rb*sin(a)*sin(b)/2 - 3*rb*cos(b)/2)*(-q*rb*sin(a)*cos(b)/2 + 3*rb*sin(b)/2))*(((-q*rb*sin(a)*sin(b)/2 - 3*rb*cos(b)/2)*(q*rb*sin(a)*cos(b)/2 + 3*rb*sin(b)/2) - (q*rb*sin(a)*sin(b)/2 - 3*rb*cos(b)/2)*(-q*rb*sin(a)*cos(b)/2 + 3*rb*sin(b)/2))**2 + (-q*rb*(-q*rb*sin(a)*sin(b)/2 - 3*rb*cos(b)/2)*cos(a)/2 - q*rb*(q*rb*sin(a)*sin(b)/2 - 3*rb*cos(b)/2)*cos(a)/2)**2 + (q*rb*(-q*rb*sin(a)*cos(b)/2 + 3*rb*sin(b)/2)*cos(a)/2 + q*rb*(q*rb*sin(a)*cos(b)/2 + 3*rb*sin(b)/2)*cos(a)/2)**2)**(-0.5),(-q*rb*(-q*rb*sin(a)*sin(b)/2 - 3*rb*cos(b)/2)*cos(a)/2 - q*rb*(q*rb*sin(a)*sin(b)/2 - 3*rb*cos(b)/2)*cos(a)/2)*(((-q*rb*sin(a)*sin(b)/2 - 3*rb*cos(b)/2)*(q*rb*sin(a)*cos(b)/2 + 3*rb*sin(b)/2) - (q*rb*sin(a)*sin(b)/2 - 3*rb*cos(b)/2)*(-q*rb*sin(a)*cos(b)/2 + 3*rb*sin(b)/2))**2 + (-q*rb*(-q*rb*sin(a)*sin(b)/2 - 3*rb*cos(b)/2)*cos(a)/2 - q*rb*(q*rb*sin(a)*sin(b)/2 - 3*rb*cos(b)/2)*cos(a)/2)**2 + (q*rb*(-q*rb*sin(a)*cos(b)/2 + 3*rb*sin(b)/2)*cos(a)/2 + q*rb*(q*rb*sin(a)*cos(b)/2 + 3*rb*sin(b)/2)*cos(a)/2)**2)**(-0.5)])
    # 求动平台转角角度
    l_b1 = -a1 + b1
    l_b2 = -a2 + b2
    l_b3 = -a3 + b3
    t_b1 = math.acos(np.dot(l_b1, n_b) / (np.dot(l_b1, l_b1)**0.5))
    t_b2 = math.acos(np.dot(l_b2, n_b) / (np.dot(l_b2, l_b2)**0.5))
    t_b3 = math.acos(np.dot(l_b3, n_b) / (np.dot(l_b3, l_b3)**0.5))

    # 定平台转角角度
    n_a = np.array([0,0,1])
    l_a1 = l_b1
    l_a2 = l_b2
    l_a3 = l_b3
    t_a1 = math.acos(np.dot(l_a1, n_a) / (np.dot(l_a1, l_a1)**0.5))
    t_a2 = math.acos(np.dot(l_a2, n_a) / (np.dot(l_a2, l_a2)**0.5))
    t_a3 = math.acos(np.dot(l_a3, n_a) / (np.dot(l_a3, l_a3)**0.5))

    t = [t_b1,t_b2,t_b3,t_a1,t_a2,t_a3]
    return t

# t = Angle(0,0,75,50,50)
# print(t)

def Length(a,b,ra,rb,h):

    q = 3**0.5
    l_1 = (h**2 - 2*h*ra*sin(b)*cos(a) + ra**2 - 2*ra*rb*cos(b) + rb**2)**0.5
    l_2 = (h**2 + h*q*ra*sin(a) + h*ra*sin(b)*cos(a) + q**2*ra**2/4 - q**2*ra*rb*cos(a)/2 + q**2*rb**2/4 + q*ra*rb*sin(a)*sin(b)/2 + ra**2/4 - ra*rb*cos(b)/2 + rb**2/4)**0.5
    l_3 = (h**2 - h*q*ra*sin(a) + h*ra*sin(b)*cos(a) + q**2*ra**2/4 - q**2*ra*rb*cos(a)/2 + q**2*rb**2/4 - q*ra*rb*sin(a)*sin(b)/2 + ra**2/4 - ra*rb*cos(b)/2 + rb**2/4)**0.5

    l = [l_1,l_2,l_3]


    return l

# l = Length(0,0,7,3,3)
# print(l)

def P(x,y,z):

    # p = np.array([h*sin(b)*cos(a),-h*sin(a),h*cos(a)*cos(b)])
    b = atan2(x, z)
    a = atan2(-y*cos(b) ,z)
    h = z/(cos(a)*cos(b))

    p = [a,b,h]
    # print(p)

    return p

def P1(x,y,z,l):

    # x_p = (h - l) * cos(a) * sin(b)
    # y_p = (l - h) * sin(a)
    # z_p = (h - l) * cos(a) * cos(b)

    b = float(atan2(-x, -z))
    a = float(atan2(y * cos(b), -z))
    h_l = float(z/(cos(a)*cos(b)))
    h = h_l + l

    p = [a,b,h]
    # print(p)

    return p

#
# p = P(-22.80676024,53.76254912,87)
# print(p)
# l = Length(p[0], p[1], 70, 45, p[2])
# print(l)
# angle = Angle(p[0], p[1], 70, 45, p[2])
# print(angle)

# p1 = P1(233.658738214428,15.9133295082140, -50,150)
# print(p1)
# l = Length(p1[0], p1[1], 70, 45, p1[2])
# print(l)

# l =  Length(0.1,0.1,70,45,86.46)
# print(l)

# l = Length(-0.0542146763020910, 14.8333790330574, 70, 45,56.9376269407708)
# print(l)