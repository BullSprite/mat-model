from classes.Triangel import Triangle
from classes.Frame import Frame
from classes.Point import Point
from classes.Line import Line
from classes.Vector import Vector
import numpy as np
from math import acos, log, tan


def angle_calculation(v1: Vector, v2: Vector, height: float, triangle: Triangle):
    if v1.len() * v2.len() * v1.to_vector().cos_angle_between(v2.to_vector()) > 0:
        return (acos(height / triangle.lines[1].len()))
    else:
        return (-acos(height / triangle.lines[1].len()))


def integral(line: Line, op):
    triangle = Triangle(line.start, line.end, op)
    height = triangle.get_height(op.name)
    intersect = triangle.get_height_intersect(op.name)
    HA = Line(intersect, triangle.points[0])
    HB = Line(intersect, triangle.points[1])
    AB = Line(triangle.points[0], triangle.points[1])
    amin = angle_calculation(AB, HB, height, triangle)
    amax = angle_calculation(AB, HA, height, triangle)
    return (height * (log(abs((1 + tan(amax / 2)) / (1 - tan(amax / 2)))) - log(
        abs((1 + tan(amin / 2)) / (1 - tan(amin / 2))))))


def solution(points: list[np.ndarray], point_O: np.ndarray, num_f=1, num_p=1):
    integ = 0
    op = Point(point_O, name='O')
    p = [Point(p, name=name) for p, name in zip(points, 'ABCD')]
    Sol_Frame = Frame(p[0], p[1], p[2], p[3])
    return sum(integral(line, op) for line in Sol_Frame.lines_iter())

