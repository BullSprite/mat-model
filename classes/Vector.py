from classes.Point import Point
import numpy as np


class Vector:
    end: Point

    def __init__(self, point: Point) -> None:
        self.end = point

    def __str__(self) -> str:
        return str(self.end)

    def norm(self) -> float:
        return np.linalg.norm(self.end.values)

    def normalize(self) -> "Vector":
        return Vector(Point(self.end.values / self.norm()))

    def __mul__(self, other: float) -> "Vector":
        return Vector(Point(other * self.end.values))

    def __rmul__(self, other) -> "Vector":
        return Vector(Point(other * self.end.values))

    def __add__(self, other) -> "Vector":
        return Vector(Point(self.end.values + other.values))

    def cross(self, other) -> "Vector":
        return Vector(Point([np.cross(self.end.values, other.end.values)]))

    def cos_angle_between(self, v2) -> float:
        v1_u = self.normalize().end.values
        v2_u = v2.normalize().end.values
        return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))
