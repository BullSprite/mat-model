from classes.Frame import Frame
from classes.Point import Point


class Object_parser:

    def __init__(self, file):
        parsed_dict = {}
        with open(file, 'r') as text:
            object_num = int(text.readline())
            for i in range(0, object_num):
                parsed_dict['object' + str(i)] = {}
                modules_num = int(text.readline())
                for j in range(0, modules_num):
                    parsed_dict['object' + str(i)]['module' + str(j)] = []
                    text.readline()
                    lines_num = int(text.readline())
                    text.readline()
                    for k in range(0, lines_num):
                        points = []
                        line = text.readline().strip().split()
                        for start, name in zip(range(0, 12, 3), 'ABCD'):
                            points.append(Point([x for x in map(float, line[start: start + 3])],
                                                name=name + str(i) + str(j) + str(k)))
                        parsed_dict['object' + str(i)]['module' + str(j)].append(
                            Frame(points[0], points[1], points[2], points[3]))
        self.parsed_dict = parsed_dict
