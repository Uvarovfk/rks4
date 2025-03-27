from Function import Function
from sinusoidal_pulse import sinusoidal_pulse
import numpy as np
from scipy import interpolate
from numpy import random
import matplotlib.pyplot as plt

n = 40 # количество строк матрицы G, M и Thetta
m = 10 # количество столбцов матрицы G, M и Thetta



G_matrix = [[0 for z in range(m)] for y in range(n)]  # матрица значений G(коэффициента усиления от каждого элемента поверхности)
M_matrix = [[[0 for z in range(3)] for y in range(m)] for x in range(n)] # матрица координат точек на поверхности размером nXm, содержащая 3 координаты: X,Y,Z
Theta_matrix = [[0 for z in range(m)] for y in range(n)] # матрица значений Thetta(сдвига фаз в градусах от каждого элемента поверхности)


# заполняем матрицу M_matrix:
for i in range(n):
    for j in range(m):
        M_matrix[i][j][0] = i * 50
        M_matrix[i][j][1] = j * 50
        M_matrix[i][j][2] = 0

# заполняем матрицу G_matrix:

for i in range(n):
    for j in range(m):
        G_matrix[i][j] = 1

# заполняем матрицу Thetta_matrix:

for i in range(n):
    for j in range(m):
        Theta_matrix[i][j] = 1

N = 10 # количество точек на траектории

X_Plane = [0]*N # Список из X компоненты координат положения самолета
Y_Plane = [0]*N # Список из Y компоненты координат положения самолета
Z_Plane = [0]*N # Список из X компоненты координат положения самолета
t_Plane = [0]*N # Список моментов времени, которым соответсвуют X,Y,Z координаты

# заполняем координаты положения самолета
for i in range(N):
    X_Plane[i] = 1
for i in range(N):
    Y_Plane[i] = i
for i in range(N):
    Z_Plane[i] = 1
for i in range(N):
    t_Plane[i] = i

# интерполируем координаты положения самолета

fx = interpolate.interp1d(t_Plane, X_Plane, kind='cubic')
fy = interpolate.interp1d(t_Plane, Y_Plane, kind='cubic')
fz = interpolate.interp1d(t_Plane, Z_Plane, kind='cubic')

# строим график

a1 = Function(5, sinusoidal_pulse, 0.1/0.01, Theta_matrix, G_matrix, M_matrix, 4., .1, 0.01, fx, fy, fz)[1]
a2 = Function(5, sinusoidal_pulse, 0.1/0.01, Theta_matrix, G_matrix, M_matrix, 4., .1, 0.01, fx, fy, fz)[2]
a3 = Function(5, sinusoidal_pulse, 0.1/0.01, Theta_matrix, G_matrix, M_matrix, 4., .1, 0.01, fx, fy, fz)[0]
go = [0]*a1
for i in range(a1):
    go[i] = i+a2
plt.plot(go, a3)
plt.show()
