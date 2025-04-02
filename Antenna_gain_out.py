import numpy as np
from typing import List
from Angle import angle
from Fi import fi
from Thetta import thetta


def antenna_gain_out(vector_a: List[float]) -> float:
    """
    Функция возвращает коэффициент усиления изулученного сигнала

    :param vector_a: вектор соединяющий положение самолета и точку на поверхности в декартовой системе координат спустя
     время на распространение сигнала

    """
    thetta_angle = thetta(vector_a)
    fi_angle = fi(vector_a)
    # ниже будет выражен коэффициент усиления в зависимости от углов tetta и fi,
    # в упрощенном виде зависимость сводится не к углам tetta и fi, а углу между OY и vector_a
    r = 1.
    x = r * np.sin(thetta_angle) * np.cos(fi_angle)
    y = r * np.sin(thetta_angle) * np.sin(fi_angle)
    z = r * np.cos(thetta_angle)
    decart_vector = [x, y, z]
    if angle([0., 1., 0.], decart_vector) <= np.pi:
        return 1.
    else:
        return 0.
