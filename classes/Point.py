import numpy as np
from typing import Iterator


class Point:
    values: np.ndarray
    name: str = None

    # TODO: add new checks for inputs
    def __init__(self, *args, **kwargs) -> None:
        if len(args) > 3:
            raise Exception("Too many arguments for Vector")
        elif len(args) == 1:
            if isinstance(args[0], list):
                self.values = np.array(args[0])
            elif isinstance(args[0], np.ndarray):
                self.values = args[0]
            else:
                raise TypeError

            if len(self.values) > 3:
                raise ValueError
            self.values = np.append(self.values, [0] * (3 - len(self.values)))
        else:
            self.values = np.array([0, 0, 0])
            for arg, i in zip(args, range(3)):
                self.values[i] += arg

        if "name" in kwargs:
            self.name = kwargs["name"]

    def __iter__(self) -> Iterator[int]:
        return self.values.__iter__()

    def __str__(self) -> str:
        return f"{self.name}: {self.values}"

    def __sub__(self, other: "Point") -> "Point":
        return Point([p1 - p2 for p1, p2 in zip(self.values, other.values)])

    def __add__(self, other: "Point") -> "Point":
        return Point([p1 + p2 for p1, p2 in zip(self.values, other.values)])
