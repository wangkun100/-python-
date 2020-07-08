import numpy as np
import xlrd
import matplotlib.pyplot as plt

path = 'C:\\Users\\坤宇\\Desktop\\python运动学求解\\操作空间边界点含角度\\103.97.xlsx'
data = xlrd.open_workbook(path)
sheet = data.sheet_by_index(0)

x = sheet.col_values(1)
x = x[1:]
x = list(map(float,x))

y = sheet.col_values(2)
y = y[1:]
y = list(map(float,y))


plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()