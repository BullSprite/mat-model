import numpy as np

from classes.Point import Point
from classes.Triangel import Triangle
from classes.Vector import Vector
from classes.Line import Line
from typing import Iterator
from math import acos, log, tan


class Frame:
    points: list[Point]
    lines: list[Line]
    name: str

    def __init__(self, p1: Point, p2: Point, p3: Point, p4: Point):
        self.points = [p1, p2, p3, p4]
        self.lines = [Line(p1, p2), Line(p2, p3), Line(p3, p4), Line(p4, p1)]
        self.name = p1.name + p2.name + p3.name + p4.name

    def central_point(self) -> Point:
        central_point = Point(name='O')
        for point in self.points:
            central_point += point
        return central_point / 4

    def lines_iter(self) -> Iterator[Line]:
        return self.lines.__iter__()

    def points_iter(self) -> Iterator[Point]:
        return self.points.__iter__()

    def normal(self):
        points = []
        for line in self.lines_iter():
            points.append(Point([line.end.values[0] - line.start.values[0] / 2,
                                 line.end.values[1] - line.start.values[1] / 2,
                                 line.end.values[2] - line.start.values[2] / 2]))
        TP = Line(points[0], points[2]).to_vector()
        QR = Line(points[1], points[3]).to_vector()
        return (TP * QR).normalize()

    def __integral(self, line: Line, op):
        high_log = lambda x: log(abs((1 + tan(x / 2)) / (1 - tan(x / 2))))
        triangle = Triangle(line.start, line.end, op)
        height = triangle.get_height(op.name)
        intersect = triangle.get_height_intersect(op.name)
        HA = Line(intersect, triangle.points[0])
        HB = Line(intersect, triangle.points[1])
        AB = Line(triangle.points[0], triangle.points[1])
        amin = self.__angle_calculation(AB, HB, height, triangle)
        amax = self.__angle_calculation(AB, HA, height, triangle)
        return (height * (high_log(amax) - high_log(amin)))

    def __angle_calculation(self, v1: Vector, v2: Vector, height: float, triangle: Triangle):
        if v1.len() * v2.len() * v1.to_vector().cos_angle_between(v2.to_vector()) > 0:
            return (acos(height / triangle.lines[1].len()))
        else:
            return (-acos(height / triangle.lines[1].len()))

    def integral_summ(self, point_O: np.ndarray, num_f=1, num_p=1):
        op = Point(point_O, name='O')
        return sum(self.__integral(line, op) for line in self.lines_iter())
