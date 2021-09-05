from classes.Point import Point
import numpy as np


class Vector():
    end: Point

    def __init__(self, point: Point) -> None:
        self.end = point

    def __str__(self) -> str:
        return str(self.end)

    def norm(self) -> float:
        return np.linalg.norm(self.end.values)

    def normalize(self) -> "Vector":
        return Vector(Point(self.end.values / self.norm()))
