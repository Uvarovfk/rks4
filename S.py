

def rotation_matrix(psi: float, thetta: float, gamma: float):
    import numpy as np
    """
    Функция возвращает матрицу поворота, в зависимости от входных параметров
     тангаж, рысканье и угол крена самолета задаются в ГСК, аналогично тангаж... РЛ задаются в системе самолета
    :param psi: угол относительно курса; z
    :param thetta: угол тангажа; x
    :param y: угол крена; y
    """
    # ~в радианы перевести в начале функции: сделано
    psi = psi * np.pi / 180  # угол относительно курса в радианах
    thetta = thetta * np.pi / 180  # угол тангажа в радианах
    gamma = gamma * np.pi / 180  # угол крена в радианах

    s = [[np.cos(psi) * np.cos(gamma) + np.sin(psi) * np.sin(thetta) * np.sin(gamma),
          -np.sin(psi) * np.cos(gamma) + np.cos(psi) * np.sin(thetta) * np.sin(gamma), -np.cos(thetta) * np.sin(gamma)],
         [np.sin(psi) * np.cos(thetta), np.cos(psi) * np.cos(thetta), np.sin(thetta)],
         [np.cos(psi) * np.sin(gamma) - np.sin(psi) * np.sin(thetta) * np.cos(gamma), -np.sin(psi) * np.sin(gamma) -
          np.cos(psi) * np.sin(thetta)
          * np.cos(gamma),
          np.cos(thetta) * np.cos(gamma)]]

    k = np.eye(3)

    for i in range(3):
        for j in range(3):
            k[i][j] = s[i][j]

    return k
