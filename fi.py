import numpy as np
from typing import List


def fi(vector: List[float]) -> float:
    """
    Функция возвращает угол фи в сферических координатах вектора

    :param vector: вектор в декартовой системе координат

    """
    x = vector[0]
    y = vector[1]
    if x > 0:
        return np.arctan(y/x)

    if x < 0 and y >= 0:
        return np.arctan(y/x)+np.pi

    if x < 0 and y < 0:
        return np.arctan(y/x) - np.pi

    if x == 0 and y > 0:
        return np.pi/2

    if x == 0 and y < 0:
        return -np.pi/2

    if x == 0 and y == 0:
        return 0
