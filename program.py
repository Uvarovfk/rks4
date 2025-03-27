from Function import function
from sinusoidal_pulse import sinusoidal_pulse
from scipy import interpolate
import matplotlib.pyplot as plt
import random

n = 5  # количество строк матрицы G_matrix, M_matrix и Thetta_matrix
m = 5  # количество столбцов матрицы G_matrix, M_matrix и Thetta_matrix

G_matrix = [[0. for z1 in range(m)] for y1 in
            range(n)]  # матрица значений коэффициентов усиления от каждого элемента поверхности
M_matrix = [[[0. for z2 in range(3)] for y2 in range(m)] for x2 in
            range(n)]  # матрица координат точек на поверхности размером nXm, содержащая 3 координаты: X,Y,Z
Theta_matrix = [[0. for z3 in range(m)] for y3 in
                range(n)]  # матрица значений сдвига фаз в радианах от каждого элемента поверхности

# заполняем матрицу M_matrix:
for i in range(n):
    for j in range(m):
        M_matrix[i][j][0] = i * 150
        M_matrix[i][j][1] = j * 150
        M_matrix[i][j][2] = 0

# заполняем матрицу G_matrix:
for i in range(n):
    for j in range(m):
        G_matrix[i][j] = random.randint(1, 10)

for i in range(n):
    for j in range(m):
        if i > int(n/2):
            G_matrix[i][j] = 10


# заполняем матрицу Thetta_matrix:

for i in range(n):
    for j in range(m):
        Theta_matrix[i][j] = random.randint(0, 1)

N = 100  # количество точек на траектории

X_Plane = [0] * N  # Список из X компоненты координат положения самолета
Y_Plane = [0] * N  # Список из Y компоненты координат положения самолета
Z_Plane = [0] * N  # Список из X компоненты координат положения самолета
t_Plane = [0] * N  # Список моментов времени, которым соответсвуют X,Y,Z координаты

# заполняем координаты положения самолета
for i in range(N):
    X_Plane[i] = 10000
for i in range(N):
    Y_Plane[i] = i*20 + 1000
for i in range(N):
    Z_Plane[i] = 10000
for i in range(N):
    t_Plane[i] = i

# интерполируем координаты положения самолета

fx = interpolate.interp1d(t_Plane, X_Plane, kind='cubic')
fy = interpolate.interp1d(t_Plane, Y_Plane, kind='cubic')
fz = interpolate.interp1d(t_Plane, Z_Plane, kind='cubic')

# строим график
# задаем необходимые значения
t = 10  # момент времени излучения
dis = 0.01  # период дискретизации
d_t = 1.  # длительность импульса
w = 5*3.14/d_t  # частота импульса
t_start = 0.  # начальный момент времени

a0 = function(t, sinusoidal_pulse, w, Theta_matrix, G_matrix, M_matrix, t_start, d_t, dis, fx, fy, fz)[0]
a1 = function(t, sinusoidal_pulse, w, Theta_matrix, G_matrix, M_matrix, t_start, d_t, dis, fx, fy, fz)[1]
a2 = function(t, sinusoidal_pulse, w, Theta_matrix, G_matrix, M_matrix, t_start, d_t, dis, fx, fy, fz)[2]

go = [0] * a1

for i in range(a1):
    go[i] = i + a2
plt.plot(go, a0)

print(a1)  # количество отсчетеов
print(a2)  # начальный момент приема сигнала
plt.show()
