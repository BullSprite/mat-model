from classes.Frame import Frame
from classes.Point import Point


class Scene:
    objects: list

    def __init__(self, file):
        self.objects = self.__parse(file)

    def __parse(self, file):
        parsed_list = []
        with open(file, 'r') as text:
            object_num = int(text.readline())
            for object in range(0, object_num):
                parsed_list.append([])
                modules_num = int(text.readline())
                for module in range(0, modules_num):
                    parsed_list[object].append([])
                    text.readline()
                    lines_num = int(text.readline())
                    text.readline()
                    for lines in range(0, lines_num):
                        points = []
                        line = text.readline().strip().split()
                        idx = f'{str(object)}_{str(module)}_{str(lines)}'
                        for start, name in zip(range(0, 12, 3), 'ABCD'):
                            points.append(Point([x for x in map(float, line[start: start + 3])],
                                                name=name + idx))
                        parsed_list[object][module].append(
                            Frame(points[0], points[1], points[2], points[3], index=idx))
        return parsed_list

    def collaction(self, n_frame, n_obj=0, n_module=0):
        frame = self.objects[n_obj][n_module][n_frame]
        return sum(frame.integral_summ(other) for other in self)

    def __iter__(self):
        return next(self)

    def __next__(self):
        for object in self.objects:
            for module in object:
                for frame in module:
                    yield frame
