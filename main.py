from solution import solution
import numpy as np


def main():
    print(solution([np.array([2,2,0]),
              np.array([4,2,0]),
              np.array([4,4,0]),
              np.array([2,4,0])],
             np.array([3,3,0])))

if __name__ == "__main__":
    main()
