import numpy as np
from typing import List


def angle(vector_a: List[float], vector_b: List[float]) -> float:
    """
        Функция возращает угол между двумя векторами

        :param vector_a: вектор A
        :param vector_b: вектор B

        """
    return np.arccos(np.dot(vector_a, vector_b) /
                     (np.linalg.norm(vector_a) * np.linalg.norm(vector_b)))
