from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        count = 0
        for i in matrix[1:]:
            count += len(i)
        if len(matrix[0]) == count / (len(matrix) - 1):
            self.matrix = matrix
        else:
            raise ValueError('fail initialization matrix')

    def __add__(self, other):
        result = []
        for i in range(len(self.matrix)):
            x = []
            for j in range(len(self.matrix[i])):
                x.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(x)
        x = Matrix(result)
        return x

    def __str__(self):
        return '| ' + ' |\n| '.join([' '.join(['%d' % i for i in row]) for row in self.matrix]) + ' |'


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print()
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """