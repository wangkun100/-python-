import numpy as np
from sympy import *
import math
a,b,ra,rb,h,q,l1,l2,l3=symbols('a b ra rb h q l_b1 l_b2 l_b3')
f1 = h**2 - 2*h*ra*sin(b)*cos(a) + ra**2 - 2*ra*rb*cos(b) + rb**2 - l1**2
f2 = h**2 + h*q*ra*sin(a) + h*ra*sin(b)*cos(a) + q**2*ra**2/4 - q**2*ra*rb*cos(a)/2 + q**2*rb**2/4 + q*ra*rb*sin(a)*sin(b)/2 + ra**2/4 - ra*rb*cos(b)/2 + rb**2/4 - l2**2
f3 = h**2 - h*q*ra*sin(a) + h*ra*sin(b)*cos(a) + q**2*ra**2/4 - q**2*ra*rb*cos(a)/2 + q**2*rb**2/4 - q*ra*rb*sin(a)*sin(b)/2 + ra**2/4 - ra*rb*cos(b)/2 + rb**2/4 - l3**2

f1_a = diff(f1,a)
f1_b = diff(f1,b)
f1_h = diff(f1,h)
print(f1_a)
print(f1_b)
print(f1_h)
'''
2*h*ra*sin(a)*sin(b)
-2*h*ra*cos(a)*cos(b) + 2*ra*rb*sin(b)
2*h - 2*ra*sin(b)*cos(a)
'''


f2_a = diff(f2,a)
f2_b = diff(f2,b)
f2_h = diff(f2,h)
print(f2_a)
print(f2_b)
print(f2_h)
'''
h*q*ra*cos(a) - h*ra*sin(a)*sin(b) + q**2*ra*rb*sin(a)/2 + q*ra*rb*sin(b)*cos(a)/2
h*ra*cos(a)*cos(b) + q*ra*rb*sin(a)*cos(b)/2 + ra*rb*sin(b)/2
2*h + q*ra*sin(a) + ra*sin(b)*cos(a)
'''

f3_a = diff(f3,a)
f3_b = diff(f3,b)
f3_h = diff(f3,h)
print(f3_a)
print(f3_b)
print(f3_h)
'''
-h*q*ra*cos(a) - h*ra*sin(a)*sin(b) + q**2*ra*rb*sin(a)/2 - q*ra*rb*sin(b)*cos(a)/2
h*ra*cos(a)*cos(b) - q*ra*rb*sin(a)*cos(b)/2 + ra*rb*sin(b)/2
2*h - q*ra*sin(a) + ra*sin(b)*cos(a)
'''

