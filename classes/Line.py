from classes.Point import Point
from classes.Vector import Vector
from math import sqrt


class Line:
    start: Point
    end: Point

    def __init__(self, point1: Point, point2: Point) -> None:
        self.start = point1
        self.end = point2

    def invert(self) -> None:
        self.start, self.end = self.end, self.start
        # TODO: is I need this??

    def len(self) -> float:
        return sqrt(sum([(x - y) ** 2 for x, y in zip(self.start, self.end)]))

    def __str__(self) -> str:
        return f"{self.start} {self.end}"

    def to_vector(self) -> Vector:
        return Vector(self.end - self.start)
