import numpy as np
from sympy import *

a,b,ra,rb,h,q=symbols('a b ra rb h q')
R = np.array([[cos(b),sin(a)*sin(b),cos(a)*sin(b)],[0,cos(a),-sin(a)],[-sin(b),cos(b)*sin(a),cos(b)*cos(a)]])
b1 = np.array([rb,0,0])
b2 = np.array([-rb/2,q*rb/2,0])
b3 = np.array([-rb/2,-q*rb/2,0])
a1 = np.array([ra,0,0])
a2 = np.array([-ra/2,q*ra/2,0])
a3 = np.array([-ra/2,-q*ra/2,0])
p = np.array([h*sin(b)*cos(a),-h*sin(a),h*cos(a)*cos(b)])


x = np.dot(R,b1)-a1+p
xt = x.T
l_1 = simplify(np.dot(x,xt))
print(l_1)

x = np.dot(R,b2)-a2+p
xt = x.T
l_2 = simplify(np.dot(x,xt))
print(l_2)

x = np.dot(R,b3)-a3+p
xt = x.T
l_3 = simplify(np.dot(x,xt))
print(l_3)

