from Function import function
from sinusoidal_pulse import sinusoidal_pulse
from scipy import interpolate
import matplotlib.pyplot as plt
import random

n = 5  # количество строк матрицы G_matrix, M_matrix и Thetta_matrix
m = 5  # количество столбцов матрицы G_matrix, M_matrix и Thetta_matrix

G_matrix = [[0. for _ in range(m)] for _ in
            range(n)]  # матрица значений коэффициентов усиления от каждого элемента поверхности
M_matrix = [[[0. for _ in range(3)] for _ in range(m)] for _ in
            range(n)]  # матрица координат точек на поверхности размером nXm, содержащая 3 координаты: X,Y,Z
Theta_matrix = [[0. for _ in range(m)] for _ in
                range(n)]  # матрица значений сдвига фаз в радианах от каждого элемента поверхности

# заполняем матрицу M_matrix:
for i in range(n):
    for j in range(m):
        M_matrix[i][j][0] = i + 10000
        M_matrix[i][j][1] = j + 10000
        M_matrix[i][j][2] = 0

# заполняем матрицу G_matrix:
for i in range(n):
    for j in range(m):
        G_matrix[i][j] = 1

# заполняем матрицу Thetta_matrix:

for i in range(n):
    for j in range(m):
        Theta_matrix[i][j] = 0

N = 10  # количество точек на траектории

X_plane = [0.] * N  # Список из X компоненты координат положения самолета
Y_plane = [0.] * N  # Список из Y компоненты координат положения самолета
Z_plane = [0.] * N  # Список из X компоненты координат положения самолета

psi_plane = [0.] * N  # список из углов рысканья самолета
thetta_plane = [0.] * N  # список из углов тангажа самолета
gamma_plane = [0.] * N  # список из углов крена самолета

psi_radio = [0.] * N  # список из углов рысканья радиолокатора
thetta_radio = [0.] * N  # список из углов тангажа радиолокатора
gamma_radio = [0.] * N  # список из углов крена радиолокатора

t_Plane = [0.] * N  # Список моментов времени, которым соответсвуют X,Y,Z координаты

# заполняем координаты положения самолета

for i in range(N):
    X_plane[i] = 0.
for i in range(N):
    Y_plane[i] = i * 8000
for i in range(N):
    Z_plane[i] = 550000  # высота полета
for i in range(N):
    t_Plane[i] = i
# заполняем крен, тангаж и рысканье самолета

for i in range(N):
    psi_plane[i] = 0.  # расканье самолета
for i in range(N):
    thetta_plane[i] = 0.  # тангаж самолета
for i in range(N):
    gamma_plane[i] = 0  # крен самолета

# заполняем крен, тангаж и рысканье радиолокатора

for i in range(N):
    psi_radio[i] = 90.  # рысканье радиолокатора
for i in range(N):
    thetta_radio[i] = -45.  # тангаж радиолокатора
for i in range(N):
    gamma_radio[i] = 0  # крен радиолокатора

# интерполируем координаты положения самолета

fx = interpolate.interp1d(t_Plane, X_plane, kind='linear')
fy = interpolate.interp1d(t_Plane, Y_plane, kind='linear')
fz = interpolate.interp1d(t_Plane, Z_plane, kind='linear')

# интерполируем рысканье, тангаж, крен самолета

Psi_plane = interpolate.interp1d(t_Plane, psi_plane, kind='linear')
Thetta_plane = interpolate.interp1d(t_Plane, thetta_plane, kind='linear')
Gamma_plane = interpolate.interp1d(t_Plane, gamma_plane, kind='linear')

# интерполируем рысканье, тангаж, крен радиолокатора

Psi_radio = interpolate.interp1d(t_Plane, psi_radio, kind='linear')
Thetta_radio = interpolate.interp1d(t_Plane, thetta_radio, kind='linear')
Gamma_radio = interpolate.interp1d(t_Plane, gamma_radio, kind='linear')

# задаем необходимые значения
t = 1.  # момент времени излучения
d_t = 1. / 200000000  # длительность импульса в секундах
dis = d_t / 300  # период дискретизации в секундах

w = 1*3.1415 / d_t  # частота импульса
t_start = 0.  # начальный момент времени

# строим график
a0 = function(t, sinusoidal_pulse, w, Theta_matrix, G_matrix, M_matrix, t_start, d_t, dis, fx, fy, fz, Psi_plane,
              Thetta_plane, Gamma_plane, Psi_radio, Thetta_radio, Gamma_radio)[0]
a1 = function(t, sinusoidal_pulse, w, Theta_matrix, G_matrix, M_matrix, t_start, d_t, dis, fx, fy, fz, Psi_plane,
              Thetta_plane, Gamma_plane, Psi_radio, Thetta_radio, Gamma_radio)[1]
a2 = function(t, sinusoidal_pulse, w, Theta_matrix, G_matrix, M_matrix, t_start, d_t, dis, fx, fy, fz, Psi_plane,
              Thetta_plane, Gamma_plane, Psi_radio, Thetta_radio, Gamma_radio)[2]

go = [0] * a1

for i in range(a1):
    go[i] = i + a2
plt.plot(go, a0)

print(a1)  # количество отсчетеов
print(a2)  # начальный момент приема сигнала
plt.show()
