from typing import Callable, List
import numpy as np
from calculate_delay import calculate_delay


def function(t: float,
             pulse: Callable[[float, float], complex],
             w: float, theta_matrix: List[List[float]], g_matrix: List[List[float]], m_matrix: List[List[List[float]]],
             t_start: float, d_t: float, dis: float, fx: Callable[[float], float],
             fy: Callable[[float], float], fz: Callable[[float], float]) -> List[List[complex] | int]:

    """
        Функция возращает список из 3 элементов:
     1) список, состоящий из оцифровок суммарной амплитуды принятого сигнала
     2) длину принятого сигнала в отсчетах
     3) номер отсчета начала приема сигнала


    :param: theta_matrix: матрица состоящая из сдвигов фаз для каждой точки поверхности
    :param: g_matrix: матрица состоящая из коэффициента усиления для каждой точки поверхности
    :param t: момент времени излучения импульса
    :param w: частота сигнала
    :param pulse: функция, описывающая импульс радиолокатора
    :param: theta_matrix: матрица состоящая из сдвигов фаз для каждой точки поверхности
    :param t_start: начальный момент времени
    :param d_t: время излучения импульса
    :param dis: период дискретизации
    :param fx: Функция интерполирующая координату x
    :param fy: Функция интерполирующая координату y
    :param fz: Функция интерполирующая координату z

    """

    l1 = 0  # счетчик
    r = 0  # счетчик
    n = len(m_matrix)
    m = len(m_matrix[0])

    # матрица, содеращая в себе амплитуду и номер отсчета времени приема принятого сигнала от каждой(всего nxm) точки
    amplitude = np.zeros((n * m, int(d_t / dis), 2))

    vector = [fx(t), fy(t), fz(t)]  # интерполированное значение координат положения самолета в момент времени T

    time_global: List[float] = [0] * 10000  # Вводится список состоящий из мементов времени

    for k in range(10000):
        time_global[k] = t_start + dis * k

    # запись амплитуды принятого отраженного сигнала в А и соотвеатвующий ей номер отсчета k

    for i in range(n):
        for j in range(m):
            delay = calculate_delay(m_matrix[i][j], vector,  1000.)
            t1, t2, t3 = (t - t_start) / dis, delay / dis, d_t / dis
            for k in range(int(t1), int(t1) + int(t2) + int(t3) + 1, 1):
                if t + delay <= time_global[k] and time_global[k] <= t + delay + d_t:
                    amplitude[l1][r][0] = k
                    # записывается амплитуда сигнала с учетом сдвига по фазе и коэффициента усиления точки поверхности
                    pulse1 = pulse(time_global[k] - t - delay, w)
                    amplitude[l1][r][1] = pulse1 * np.exp(1j * theta_matrix[i][j]) * g_matrix[i][j]
                    r = r + 1
            l1 += 1
            r = 0
    max_num_samples = 0  # максимальный номер отсчета
    min_num_samples = None  # минимальный номер отсчета

    # суммирование амплитуд, соотвествующих одному и тому же моменту времени k

    for i in range(n * m):
        for j in range(int(d_t / dis)):
            if amplitude[i][j][0] >= max_num_samples:
                max_num_samples = amplitude[i][j][0]

            if min_num_samples is None or amplitude[i][j][0] <= min_num_samples:
                if min_num_samples != 0:
                    min_num_samples = amplitude[i][j][0]

    u = int(max_num_samples + 1) - int(min_num_samples)  # длительность приема одного импульса в количестве отсчетов

    sum_amplitude = [0] * u  # список состоящий из суммарных амплитуд.

    s = 0  # счетчик
    # заполнение списка sum. Kаждая следующая амплитуда соответсвует следующему номеру отсчета k

    for i in range(int(min_num_samples), int(max_num_samples + 1), 1):
        for j in range(n * m):
            for k in range(int(d_t / dis)):
                if int(amplitude[j][k][0]) == i:
                    sum_amplitude[s] = sum_amplitude[s] + amplitude[j][k][1]
        s = s + 1
    # на выходе функции 1) список амплитуд, каждая следующая амплитуда соответсвует следующему номеру отсчета k
    # 2) количество отсчетов 3) номер минимального отсчета(первого отсчета)

    return [sum_amplitude, int(max_num_samples - min_num_samples + 1), int(min_num_samples)]
