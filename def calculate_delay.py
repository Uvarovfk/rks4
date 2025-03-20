def calculate_delay(A: List[float], B: List[float], c: float) -> float:

    """
    Функция возращает задержку времени на распространение сигнала

    :param A: список, состоящий из 3 координат положения радиолокатора
    :param B: список, состоящий из 3 координат точки на поверхности
    :param c: скорость света

    """
    return 2 * np.linalg.norm(A-B)/(c)