from classes.Triangel import Triangle
from classes.Frame import Frame
from classes.Point import Point
from classes.Line import Line
import numpy as np
from math import acos, log, tan

def solution(points: list[np.ndarray], point_O: np.ndarray, num_f=1, num_p=1):
    integ = 0
    op = Point(point_O, name='O')
    p = [Point(p,name=name) for p, name in zip(points, 'ABCD')]
    Sol_Frame = Frame(p[0], p[1], p[2], p[3])
    for line in Sol_Frame.lines_iter():
        triangle = Triangle(line.start, line.end, op)
        height = triangle.get_height(op.name)
        intersect = triangle.get_height_intersect(op.name)
        HA = Line(intersect, triangle.points[0])
        HB = Line(intersect, triangle.points[1])
        AB = Line(triangle.points[0], triangle.points[1])
        if AB.len()*HB.len()*AB.to_vector().cos_angle_between(HB.to_vector()) > 0:
            amin = acos(height/triangle.lines[1].len())
        else:
            amin = -acos(height/triangle.lines[1].len())
        if AB.len()*HA.len()*AB.to_vector().cos_angle_between(HA.to_vector()) > 0:
            amax = acos(height/triangle.lines[2].len())
        else:
            amax = -acos(height/triangle.lines[2].len())
        integ += height*(log(abs((1+tan(amax/2))/(1-tan(amax/2))))-log(abs((1+tan(amin/2))/(1-tan(amin/2)))))
    return integ
