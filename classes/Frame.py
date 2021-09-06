from classes.Point import Point
from classes.Triangel import Triangle
from classes.Line import Line


class Frame:
    points: list[Point]
    lines: list[Line]
    name: str

    def __init__(self, p1: Point, p2: Point, p3: Point, p4: Point):
        self.points = [p1, p2, p3, p4]
        self.lines = [Line(p1, p2), Line(p2, p3), Line(p3, p4), Line(p4, p1)]
        self.name = p1.name + p2.name + p3.name + p4.name

    def lines_iter(self) -> Iterator[Line]:
        return self.lines.__iter__()

    def points_iter(self) -> Iterator[Point]:
        return self.points.__iter__()
