import numpy as np
from typing import List
from Angle import angle
from Fi import fi
from Thetta import thetta


def antenna_gain_in(vector_a: List[float]) -> float:
    thetta_angle = thetta(vector_a)
    fi_angle = fi(vector_a)
    # ниже будет выражен коэффициент усиления в зависимости от углов tetta и fi,
    # в упрощенном виде зависимость сводится не к углам tetta и psi, а углу между OY и vector_a
    r = 1.

    x = r * np.sin(thetta_angle) * np.cos(fi_angle)
    y = r * np.sin(thetta_angle) * np.sin(fi_angle)
    z = r * np.cos(thetta_angle)
    decart_vector = [x, y, z]
    if angle([0., 1., 0.], decart_vector) <= np.pi/2:
        return 1000000000.
    else:
        return 0.
