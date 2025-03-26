from Function import Function
from sinusoidal_pulse import sinusoidal_pulse
import numpy as np
from scipy import interpolate
from numpy import random
import matplotlib.pyplot as plt

n = 20 # количество строк матрицы G, M и Thetta
m = 20 # количество столбцов матрицы G, M и Thetta

G = np.zeros((n, m)) # матрица значений G(коэффициента усиления от каждого элемента поверхности)
M = np.zeros((n, m, 3)) # матрица координат точек на поверхности размером nXm, содержащая 3 координаты: X,Y,Z
Theta = np.random.rand(n, m) # матрица значений Thetta(сдвига фаз в градусах от каждого элемента поверхности)

# заполняем матрицу M
for i in range(n):
    for j in range(m):
        M[i][j][0] = i * 50
        M[i][j][1] = j * 50
        M[i][j][2] = 0

# заполняем матрицу G:

for i in range(n):
    for j in range(m):
        G[i][j] = 1

# заполняем матрицу Thetta:

for i in range(n):
    for j in range(m):
        Theta[i][j] = 1

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

a = Function(5, sinusoidal_pulse, 0.01/0.01, Theta, G, M,4., .1, 0.01, fx, fy, fz)[1]
b = Function(5, sinusoidal_pulse, 0.01/0.01, Theta, G, M,4., .1, 0.01, fx, fy, fz)[2]
с1 = Function(5, sinusoidal_pulse, 0.01/0.01, Theta, G, M,4, .1, 0.01, fx, fy, fz)[0]
go = [0]*a
for i in range(a):
    go[i] = i+b
plt.plot(go, с1)
plt.show()
