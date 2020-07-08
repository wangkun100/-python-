import numpy as np
import xlrd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import xlwt
import pandas as pd
from math import *

xs = []
ys = []
zs = []
ajs = []
ljs = []
l1s = []
l2s = []
l3s = []


listz = np.linspace(87,127,100)
for z in listz:
    z = round(z, 2)
    z_name = str(z)
    path = 'C:\\Users\\坤宇\\Desktop\\python运动学求解\\操作空间边界点含角度\\'+ z_name + '.xlsx'
    data = xlrd.open_workbook(path)
    sheet = data.sheet_by_index(0)

    x = sheet.col_values(1)
    x = x[1:]
    x = list(map(float, x))
    xs.extend(x)

    y = sheet.col_values(2)
    y = y[1:]
    y = list(map(float, y))
    ys.extend(y)

    z = sheet.col_values(3)
    z = z[1:]
    z = list(map(float, z))
    zs.extend(z)

    aj = sheet.col_values(6)
    aj = aj[1:]
    aj = list(map(float, aj))
    ajs.extend(aj)

    lj = sheet.col_values(7)
    lj = lj[1:]
    lj = list(map(float, lj))
    ljs.extend(lj)

    l1 = sheet.col_values(8)
    l1 = l1[1:]
    l1 = list(map(float, l1))
    l1s.extend(l1)

    l2 = sheet.col_values(9)
    l2 = l2[1:]
    l2 = list(map(float, l2))
    l2s.extend(l2)

    l3 = sheet.col_values(10)
    l3 = l3[1:]
    l3 = list(map(float, l3))
    l3s.extend(l3)


oh = xs
for i in range(0, len(xs)):
    oh[i] = 200 * (cos(ajs[i]) * cos(ljs[i])) -  zs[i]
print(min(oh))


def plot2(x,y,x_label,y_label):

    plt.scatter(x, y, s=30, c='r')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

# plot2(ajs,ljs,'α/rad','β/rad')
# plot2(ajs,zs,'α/rad','Z/mm')
# plot2(ljs,zs,'β/rad','Z/mm')
# plot2(xs,zs,'X/mm','Z/mm')
# plot2(ys,zs,'Y/mm','Z/mm')
# plot2(xs,ys,'X/mm','Y/mm')

# plot2(ajs,l1s,'α/rad','L1/mm')
# plot2(ljs,l1s,'β/rad','L1/mm')

def plot3(x,y,z,x_label,y_label,z_label):

    ax = plt.figure().add_subplot(111, projection='3d')
    ax.scatter(x, y, z, s=40, c='r', marker='.')

    # 设置坐标轴
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_zlabel(z_label)
    plt.show()

# plot3(ajs,ljs,zs,'α/rad','β/rad','Z/mm')


# plot3(xs,ys,zs,'X/mm','Y/mm','Z/mm')

