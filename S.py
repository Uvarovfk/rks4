from typing import List


def rotation_matrix(fi: float, o: float, y: float) -> List[List[float]]:
    import numpy as np
    """
    Функция возвращает матрицу поворота, в зависимости от входных параметров

    :param fi: угол относительно курса
    :param o: угол тангажа
    :param y: угол крена
    """
    # ~в радианы перевести в начале функции: сделано
    fi = fi * np.pi / 180  # угол относительно курса в радианах
    o = o * np.pi / 180  # угол тангажа в радианах
    y = y * np.pi / 180  # угол крена в радианах

    s = [[np.cos(fi) * np.cos(y) + np.sin(fi) * np.sin(o) * np.sin(y), -np.sin(fi) * np.cos(y) + np.cos(fi) * np.sin(o) * np.sin(y), np.cos(o) * np.sin(y)],
         [np.sin(fi) * np.cos(o), np.cos(fi) * np.cos(o), np.sin(o)],
         [np.cos(fi) * np.sin(y) - np.sin(fi) * np.sin(o) * np.cos(y), -np.sin(fi) * np.sin(y) - np.cos(fi) * np.sin(o), np.cos(o) * np.cos(y)]]

    return s
