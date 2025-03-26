from typing import Callable, List
import numpy as np
from calculate_delay import calculate_delay
def Function(T: float, pulse: Callable[[float], complex], Theta: List[List[float]], G: List[List[float]],
             M: List[List[List[float]]], Tstart:float, dT: float, dis: float, fx: Callable[[float],float],
             fy: Callable[[float],float], fz: Callable[[float],float]) -> List[List[complex] | int]:

    """
    Функция возращает кортеж из 3 элементов:
     1) список, состоящий из оцифровок суммарной амплитуды принятого сигнала
     2) длину принятого сигнала в отсчетах
     3) номер отсчета начала приема сигнала

    :param T: момент времени излучения импульса
    :param pulse: функция, описывающая импульс радиолокатора
    :param: Theta: матрица состоящая из сдвигов фаз для каждой точки поверхности
    :param: G: матрица состоящая из коэффициента усиления для каждой точки поверхности
    :param M: матрица с координатами(X,Y,Z) каждого элемента матрицы
    """

    l = 0  # счетчик
    r = 0  # счетчик
    n = len(M)
    m = len(M[0])
    Amplitude = np.zeros((n * m, int(dT / dis), 2))  # матрица, содеращая в себе амплитуду и номер отсчета времени приема принятого отраженного сигнала от каждой(всего nxm) точки
    v = (fx(T), fy(T), fz(T))  # интерполированное значение координат положения самолета в момент времени T
    Time_Global = [0] * 10000  # Вводится список состоящий из мементов времени
    for k in range(10000):
        Time_Global[k] = Tstart + dis * k
    # запись амплитуды принятого отраженного сигнала в А и соотвеатвующий ей номер отсчета k

    for i in range(n):
        for j in range(m):
            delay = calculate_delay(v, M[i][j], 1000.)
            for k in range(int((T-Tstart)/dis), int((T-Tstart)/dis)+int(delay/dis)+int(dT/dis)+1,1):
                if T + delay <= Time_Global[k] and Time_Global[k] <= T + delay + dT:
                    Amplitude[l][r][0] = k
                    Amplitude[l][r][1] = pulse(Time_Global[k] - T - delay, 30/dT) * np.exp(1j * Theta[i][j]) * G[i][j]  # записывается амплитуда принятого сигнала с учетом сдвига по фазе и коэффициента усиления точки поверхности
                    r = r + 1
            l = l + 1
            r = 0
    max_num_samples = 0  # максимальный номер отсчета
    min_num_samples = None  # минимальный номер отсчета

    # суммирование амплитуд, соотвествующих одному и тому же моменту времени k

    for i in range(n * m):
        for j in range(int(dT / dis)):
            if Amplitude[i][j][0] >= max_num_samples:
                max_num_samples = Amplitude[i][j][0]
            if min_num_samples is None or Amplitude[i][j][0] <= min_num_samples:
                if min_num_samples != 0:
                    min_num_samples = Amplitude[i][j][0]

    u = int(max_num_samples + 1) - int(min_num_samples)  # длительность приема одного импульса в количестве отсчетов
    sum_amplitude = [0] * u  # список состоящий из суммарных амплитуд.
    s = 0  # счетчик
    # заполнение списка sum. Kаждая следующая амплитуда соответсвует следующему номеру отсчета k
    for i in range(int(min_num_samples), int(max_num_samples + 1), 1):
        for j in range(n * m):
            for k in range(int(dT / dis)):
                if int(Amplitude[j][k][0]) == i:
                    sum_amplitude[s] = sum_amplitude[s] + Amplitude[j][k][1]
        s = s + 1
    # на выходе функции 1) список амплитуд, каждая следующая амплитуда соответсвует следующему номеру отсчета k
    # 2) количество отсчетов 3) номер минимального отсчета(первого отсчета)
    return [sum_amplitude, int(max_num_samples - min_num_samples + 1), int(min_num_samples)]
