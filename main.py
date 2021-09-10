from solution import solution
import numpy as np


def main():
    frame = np.array([[2., 2, 0],
                      [4, 2, 0],
                      [4, 4, 0],
                      [2, 4, 0]])
    point = np.array([3., 3, 0])
    frame_number = 1
    point_number = 1

    result_f = solution(frame, point, frame_number, point_number)
    result = 7.04429  # Результат из стандартной функции R
    assert ((((result_f - result) ** 2) / (result ** 2)) * 100) < 1

    frame = np.array([[2., 2, 0],
                      [3, 2, 0],
                      [3, 3, 0],
                      [2, 3, 0]])
    point = np.array([2.5, 2.5, 0])
    frame_number = 1
    point_number = 1

    result = 3.522703  # Результат из стандартной функции R
    result_f = solution(frame, point, frame_number, point_number)
    assert ((((result_f - result) ** 2) / (result ** 2)) * 100) < 1

    frame = np.array([[2.4, 2.4, 0],
                      [2.6, 2.4, 0],
                      [2.6, 2.6, 0],
                      [2.4, 2.6, 0]])
    point = np.array([2.5, 2.5, 0])
    frame_number = 1
    point_number = 1

    result = 0.7045407  # Результат из стандартной функции R
    result_f = solution(frame, point, frame_number, point_number)
    assert ((((result_f - result) ** 2) / (result ** 2)) * 100) < 1

    frame = np.array([[-0.1, -0.1, 0],
                      [0.1, -0.1, 0],
                      [0.1, 0.1, 0],
                      [-0.1, 0.1, 0]])
    point = np.array([0., 0, 0])
    frame_number = 1
    point_number = 1

    result = 0.7045407  # Результат из стандартной функции R
    result_f = solution(frame, point, frame_number, point_number)
    assert ((((result_f - result) ** 2) / (result ** 2)) * 100) < 1

    frame = np.array([[-0.1, 0, -0.1],
                      [0.1, 0, -0.1],
                      [0.1, 0, 0.1],
                      [-0.1, 0, 0.1]])
    point = np.array([0, 0., 0])
    frame_number = 1
    point_number = 1

    result = 0.7045407  # Результат из стандартной функции R
    result_f = solution(frame, point, frame_number, point_number)
    assert ((((result_f - result) ** 2) / (result ** 2)) * 100) < 1

if __name__ == "__main__":
    main()
