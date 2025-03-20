def Function(T: float, pulse: Callable[[float], complex]) -> Tuple[List(complex), int, int]:
    """
    Функция возращает кортеж из 3 элементов:
     1) список состоящий из оцифровок суммарной амплитуды принятого сигнала
     2) длину принятого сигнала в отсчетах
     3) номер отсчета начала приема сигнала

    :param T: момент времени излучения импульса
    :param pulse: функция, описывающая импульс радиолокатора
    """
    l = 0  # счетчик
    r = 0  # счетчик
    A = np.zeros((n * m, int(dT / dis),
                  2))  # матрица, содеращая в себе амплитуду и номер отсчета времени приема принятого отраженного сигнала от каждой(всего nxm) точки
    v = (fx(T), fy(T), fz(T))  # интерполированное значение координат положения самолета в момент времени T

    # запись амплитуды принятого отраженного сигнала в А и соотвеатвующий ей номер отсчета k

    for i in range(n):
        for j in range(m):
            for k in range(P):
                delay = calculate_delay(v, M[i][j])
                if Time_Global[k] >= T + delay and Time_Global[k] <= T + delay + dT:
                    A[l][r][0] = k
                    A[l][r][1] = pulse(Time_Global[k] - T - delay) * np.exp(1j * Theta[i][j]) * G[i][
                        j]  # записывается амплитуда принятого сигнала с учетом сдвига по фазе и коэффициента усиления точки поверхности
                    r = r + 1
            l = l + 1
            r = 0
    # ~локальные переменные не должны с зарезервированными словами:сделано
    # ~(вместо "max" прописать "max_num_samples"):сделано
    max_num_samples = 0  # максимальный номер отсчета
    min_num_samples = None  # минимальный номер отсчета

    # суммирование амплитуд, соотвествующих одному и тому же моменту времени k

    for i in range(n * m):
        for j in range(int(dT / dis)):
            if A[i][j][0] >= max_num_samples:
                max_num_samples = A[i][j][0]
            if min_num_samples is None or A[i][j][0] <= min_num_samples:
                min_num_samples = A[i][j][0]

    u = int(max_num_samples + 1) - int(min_num_samples)  # длительность приема одного импульса в количестве отсчетов
    sum = np.zeros(u)  # список состоящий из суммарных амплитуд.
    s = 0  # счетчик
    # заполнение списка sum. Kаждая следующая амплитуда соответсвует следующему номеру отсчета k
    for i in range(int(min_num_samples), int(max_num_samples + 1), 1):
        for j in range(n * m):
            for k in range(int(dT / dis)):
                if int(A[j][k][0]) == i:
                    sum[s] = sum[s] + A[j][k][1]
        s = s + 1
    # на выходе функции 1) список амплитуд, каждая следующая амплитуда соответсвует следующему номеру отсчета k
    # 2) количество отсчетов 3) номер минимального отсчета(первого отсчета)
    return (sum, max_num_samples - min_num_samples + 1, min_num_samples)