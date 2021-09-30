from classes.Point import Point
from classes.Line import Line
from classes.helpers import prod
from math import sqrt, copysign
from typing import Iterator
import re


class Triangle:
    points: list[Point]
    lines: list[Line]
    name: str

    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.points = [p1, p2, p3]
        self.lines = [Line(p1, p2), Line(p2, p3), Line(p3, p1)]
        self.name = p1.name + p2.name + p3.name

    def __str__(self):
        return f"{self.name}: {self.points}"

    def perimeter(self) -> float:
        return sum([x.len() for x in self.lines_iter()])

    def area(self) -> float:
        half_perimeter = self.perimeter() / 2
        return sqrt(half_perimeter * prod([(half_perimeter - line.len()) for line in self.lines_iter()]))

    def get_height(self, name: str) -> float:
        if name not in self.points_names():
            raise ValueError("No such points in triangle")
        base = next(l for l in self.lines_iter() if name not in l.name)
        return 2 * self.area() / base.len()

    def get_height_intersect(self, name: str) -> Point:
        if name not in self.points_names():
            raise ValueError("No such points in triangle")
        base = next(l for l in self.lines if name not in l.name)
        sign = copysign(1, self.get_angle_cos(re.split('[^A-Z]+', base.name)[0] + re.split('[A-Z]+', base.name)[1]))
        side = next(l for l in self.lines if name in l.name and base.name[0] in l.name)
        return (sign * base.to_vector().normalize() *
                sqrt(side.len() ** 2 - self.get_height(name) ** 2) + base.start).end

    def get_angle_cos(self, name: str) -> float:
        if name not in self.points_names():
            raise ValueError("No such points in triangle")
        sides_len = [line.len() for line in self.lines if name in line.name]
        sides_sum_2 = sum([side_len ** 2 for side_len in sides_len])
        op_side_len_2 = next(line.len() for line in self.lines if name not in line.name) ** 2
        return (sides_sum_2 - op_side_len_2) / (2 * prod(sides_len))

    def points_names(self):
        return [p.name for p in self.points].__iter__()

    def lines_names(self):
        return [l.name for l in self.lines].__iter__()

    def lines_iter(self) -> Iterator:
        return self.lines.__iter__()

    def points_iter(self) -> Iterator:
        return self.points.__iter__()
