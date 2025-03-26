def calculate_delay(a: list[float], b: list[float], c: float) -> float:
    import numpy as np
    """
    Функция возращает задержку времени на распространение сигнала

    :param A: список, состоящий из 3 координат положения радиолокатора
    :param B: список, состоящий из 3 координат точки на поверхности
    :param c: скорость света

    """
    a1 = np.array(a)
    b1 = np.array(b)
    return 2 * (np.linalg.norm(a1 - b1)) / c
