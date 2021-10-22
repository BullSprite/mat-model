import math
import sys
import os

from classes.Point import Point
from classes.Scene import Scene
import numpy as np
from numba import jit
import matplotlib.pyplot as plt
from classes.Vector import Vector


@jit(nopython=True)
def find_fi(k, f):
    return np.linalg.solve(k, f)


def get_result(k, f, scene, file, num):
    len_scene = len(scene)
    res = find_fi(k, f)[:len_scene]
    ax = plt.axes(projection='3d')
    points = [x.central_point for x in scene]
    zline = [point.values[2] for point in points]
    xline = [point.values[0] for point in points]
    yline = [point.values[1] for point in points]
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.scatter3D(xline, yline, zline, c=res, s=75 * 450 / len_scene, cmap=plt.cm.get_cmap("turbo"))
    plt.show()
    plt.plot(res)
    plt.show()
    with open(f'results/out_{num}_{file[:-4]}.txt', 'w') as f:
        f.write(str(len_scene) + '\n')
        for num in res:
            try:
                f.write(str(num[0]) + '\n')
            except:
                f.write(str(num) + '\n')

def func(p1, p2):
    return (np.exp(-1j * Vector(p1 - p2).norm())) / Vector(p1 - p2).norm()

def func1(p1, p2):
    return 1

def main():
    for file in os.listdir('figures'):
        if 'sphere' in file:
            scene = Scene(f'figures/{file}')
            """k = scene.calculate_all_k(n_proc=15, func=func1)
            f = np.array([[1.0]] * len(scene)) # + [[0.0]])
            get_result(k, f, scene, file, '1')
            q1 = Point(1.1, 0, 0)
            f1 = []
            for i in range(len(scene)):
                xmy = math.sqrt(sum(p ** 2 for p in (scene[i].central_point - q1)))
                f1.append([1 / (math.pi * 4 * xmy)])
            #f1.append([0])
            f1 = np.array(f1)
            get_result(k, f1, scene, file, '2_q1')
            q2 = Point(2, 0, 0)
            f2 = []
            for i in range(len(scene)):
                xmy = math.sqrt(sum(p ** 2 for p in (scene[i].central_point - q2)))
                f2.append([1 / (math.pi * 4 * xmy)])
            #f2.append([0])
            f2 = np.array(f2)
            get_result(k, f2, scene, file, '2_q2')"""
            q1 = Point(2, 0, 0)
            k1 = scene.calculate_all_k(n_proc=15, func=func)
            w = [0.2, 0.5, 0.8, 1.4, 1.6, 1.8]
            f3 = []
            for i in range(len(scene)):
                xmy = sum(np.exp(-1j * wn * Vector(scene[i].central_point - q1).norm()) for wn in w)
                f3.append(xmy)
            f3 = np.array(f3)
            get_result(k1, f3, scene, file, '3_q1')

if __name__ == "__main__":
    main()
