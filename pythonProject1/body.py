from point import Point
import numpy as np

class Body:
    def __init__(self, x: float = -11, y: float = 11, side_length: float = 2, num_points: int = 200): # начальные значения центра масс
        self.x = x
        self.y = y
        self.side_length = side_length
        self.body_points = []
        self.num_points = num_points

    def add_points_to_body(self) -> list[Point]:
        points = []
        for i in range(self.num_points):
                x = np.random.uniform(0, -self.side_length)+self.x
                y = np.random.uniform(0, self.side_length)+self.y
                points.append(Point(x, y))
        return points

