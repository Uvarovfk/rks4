def sinusoidal_pulse(t: float, w: float) -> complex:
    """
    Функция возращает значение сигнала в момент времени t
    : param t: момент времени
    : param w: частота сигнала
    """
    return np.sin(w*t) + 0j