import numpy as np
from function import function_a, function_b


def dif_sys_func(t: float, point_coordinates: tuple) -> np.ndarray:
    return np.array([function_a(t) * point_coordinates[0], function_b(t) * point_coordinates[1]])


def runge_kutta(time_limits: tuple = (0, 5), points0: tuple = (0, 0), h: float = 1, f=dif_sys_func):
    time = np.arange(time_limits[0], time_limits[1], h)
    points = np.zeros((len(time), len(points0)))
    points[0] = points0
    for i in range(1, len(time)):
        t = time[i]
        k1 = h * f(t, points[i - 1])
        k2 = h * f(t + h / 2, points[i - 1] + k1 / 2)
        k3 = h * f(t + h, points[i - 1] - k1 + 2 * k2)
        points[i] = points[i - 1] + (k1 + 4 * k2 + k3) / 6

    return points