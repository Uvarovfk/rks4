def calculate_delay(vector_a: list[float], vector_b: list[float], speed_of_ligt: float) -> float:
    import numpy as np
    """
    Функция возращает задержку времени на распространение сигнала

    :param vector_a: список, состоящий из 3 координат положения радиолокатора
    :param vector_b: список, состоящий из 3 координат точки на поверхности
    :param speed_of_ligt: скорость света

    """
    a1 = np.array(vector_a)
    b1 = np.array(vector_b)
    return 2 * (np.linalg.norm(a1 - b1)) / speed_of_ligt
