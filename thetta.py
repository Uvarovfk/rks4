import numpy as np
from typing import List


def thetta(vector: List[float]) -> float:
    x = vector[0]
    y = vector[1]
    z = vector[2]
    if z > 0:
        return np.arctan(((x**2 + y**2)**0.5)/z)

    if z < 0:
        return np.pi + np.arctan(((x**2 + y**2)**0.5)/z)

    if z == 0 and (x**2 + y**2)**0.5 != 0.:
        return np.pi/2

    if x == 0 and y == 0 and z == 0:
        return 0

