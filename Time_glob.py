def time_glob(index: int, t_start: float, dis: float) -> float:
    """
        Функция возвращает момент времени, соответсвующий отсчету index

        :param index: номер отсчета
        :param t_start: начальный момент времени
        :param dis: период дискретизации
        """
    return t_start + index * dis
