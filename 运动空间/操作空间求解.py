import numpy as np
from sympy import *
import math
import pandas as pd
from 操作空间限制条件 import *
import xlrd
import xlwt

angle_min = -math.pi/3
angle_max = math.pi/3
l_min = 90
l_max = 130
ra = 70
rb = 45

step = 0.001

def Flag(lj,aj,z,ra,rb):


    x = lj*cos(aj)
    y = lj*sin(aj)
    # print(x,y)

    p = P(x,y,z)

    l = Length(p[0], p[1], ra, rb, p[2])
    for i in l:
        if i > l_max or i < l_min:
            return 1

    angle = Angle(p[0], p[1], ra, rb, p[2])
    for i in angle:
        if i < angle_min or i > angle_max:
            return  1

    return 0


def IsBarrier(lj,aj,z,ra,rb):

    f1 = Flag(lj,aj,z,ra,rb)
    f2 = Flag(lj+step,aj,z,ra,rb)
    if f1 == 0 and f2 == 1:
        return 0
    elif f1 == 1:
        return -1
    elif f2 == 0:
        return 1

df = pd.DataFrame(columns=['x', 'y', 'z','aj','lj','a','b','l1','l2','l3'])

def barrierPoint(writer,z):
    num = 0
    lj = 0
    aj = 0
    while(aj<2*math.pi):
        while True:
            x = lj * cos(aj)
            y = lj * sin(aj)
            p = P(x, y, z)
            i = IsBarrier(lj,aj,z,ra,rb)
            if i==0:
                num = num +1
                point = [x,y,z]
                print("捕捉到边界:")
                print(point)
                l = Length(p[0], p[1], ra, rb, p[2])
                df.loc[num] = [x,y,z,aj,lj,p[0],p[1],l[0],l[1],l[2]]
                break
            if i==-1:
                lj = lj-step
            if i==1:
                lj = lj+step
            if lj < 0:
                print("达不到")
                aj = 2 * math.pi
                break

        aj = aj + 0.017
    sheet_name = str(z)
    df.to_excel(writer, sheet_name = sheet_name)


def barrierPoints(list):

    for z in list:
        z = round(z, 2)
        name = str(z)
        path = 'C:\\Users\\坤宇\\Desktop\\python运动学求解\\操作空间边界点含角度\\'+ name +'.xlsx'
        writer = pd.ExcelWriter(path)
        barrierPoint(writer,z)
        writer.save()


list = np.linspace(87,127,100)
barrierPoints(list)





e




