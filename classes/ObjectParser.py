from classes.Frame import Frame
from classes.Point import Point


class ObjectParser:

    def __init__(self, file):
        self.parsed_list = []
        with open(file, 'r') as text:
            object_num = int(text.readline())
            for object in range(0, object_num):
                self.parsed_list.append([])
                modules_num = int(text.readline())
                for module in range(0, modules_num):
                    self.parsed_list[object].append([])
                    text.readline()
                    lines_num = int(text.readline())
                    text.readline()
                    for lines in range(0, lines_num):
                        points = []
                        line = text.readline().strip().split()
                        for start, name in zip(range(0, 12, 3), 'ABCD'):
                            points.append(Point([x for x in map(float, line[start: start + 3])],
                                                name=name + str(object) + str(module) + str(lines)))
                        self.parsed_list[object][module].append(
                            Frame(points[0], points[1], points[2], points[3]))

