
import matplotlib.pyplot as plt

import os



image_name = "trajectory.png"


def trajectory_plotter(point_coordinates: [], x_limits: [] = None, y_limits: [] = None):
    plt.figure(figsize=(10, 10))
    for point_num, point in enumerate(point_coordinates):
        x_vals = [cord[0] for cord in point]
        y_vals = [cord[1] for cord in point]
        plt.plot(x_vals, y_vals)

    if x_limits is not None:
        plt.xlim(x_limits[0], x_limits[1])

    if y_limits is not None:
        plt.ylim(y_limits[0], y_limits[1])

    plt.grid(True)
    plt.savefig(os.path.join(image_name))
    plt.show()