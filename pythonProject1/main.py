from body import Body
from trace_plt import trajectory_plotter
from trace import Trajectory
from current_lines import StreamLine
from space import Space
from point import Point

import numpy as np
from velocity_fields import plot_velocity_field

time = (0.1, 0.5)
t = np.arange(time[0], time[1], 0.1)
square = Body(side_length=2, num_points=200)
trajectory = Trajectory(time)

points = trajectory.create_trajectory(square)
space_points_list = [Point(-25, 0), Point(0, 25)]
space = Space(space_points_list)
space.get_bounding_conditions()
space_bounding_x = space.x
space_bounding_y = space.y
trajectory_plotter(points, space_bounding_x, space_bounding_y)
stream_line = StreamLine(trajectory)
stream_line.calculate_tangents()
for t_ in t[::1]:
    plot_velocity_field(t_,x_range = space_bounding_x, y_range = space_bounding_y)