from classes.Scene import Scene
from tests import test
from classes.Frame import Frame
from classes.Point import Point
import numpy as np



def main():
    out = Scene('figures/sphere.dat')
    #print(out.parsed_list[1][3][2]==out.parsed_list[0][0][2])
    #print(solution(out.parsed_list[0][0]))
    #gen = next(out)
    print(out.collaction(0))


if __name__ == "__main__":
    main()
