class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix
        self.__validate_matrix()

    def __validate_matrix(self):
        if len(self.matrix) == 0:
            raise Exception('Матрица не должна быть пустой!')
        len_i = len(self.matrix[0])
        if len(self.matrix) > 1:
            for i in range(1, len(self.matrix)):
                if len(self.matrix[i]) != len_i:
                    raise Exception('Строки в матрице не могут быть разной длины!')

    def __str__(self):
        lengths = list(map(lambda column: max([len(str(v)) for v in column]), zip(*self.matrix)))
        rows = map(lambda arr: " ".join([str(v).ljust(lengths[i]) for i, v in enumerate(arr)]), self.matrix)
        return "\n".join(rows)

    @staticmethod
    def __align_matrix(matrix, height, width):
        new_matrix = [i.copy() for i in matrix]
        if width > len(new_matrix[0]):
            repeats = width - len(new_matrix[0])
            for i in new_matrix:
                for j in range(repeats):
                    i.append(0)
        if height > len(new_matrix):
            for i in range(height - len(new_matrix)):
                new_matrix.append([0 for i in range(width)])
        return new_matrix

    def __add__(self, other):
        max_height = max(len(self.matrix), len(other.matrix))
        max_width = max(len(self.matrix[0]), len(other.matrix[0]))
        aligned_matrix = self.__align_matrix(self.matrix, max_height, max_width)
        aligned_other = self.__align_matrix(other.matrix, max_height, max_width)
        return Matrix([list(map(sum, zip(*i))) for i in zip(aligned_matrix, aligned_other)])


list_1 = [[31, 22], [37, 43], [51, 86]]
list_2 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
list_3 = [[3, 5, 8, 3], [8, 3, 7, 1]]

first_matrix = Matrix(list_1)
second_matrix = Matrix(list_2)
third_matrix = Matrix(list_3)

print(first_matrix)
print()
print(second_matrix)
print()
print(third_matrix)
print()
print(f'Сумма 1 и 2 матриц равна: \n{first_matrix + second_matrix}')
print()
print(f'Сумма 1 и 3 матриц равна: \n{first_matrix + third_matrix}')
print()
print(f'Сумма 2 и 3 матриц равна: \n{second_matrix + third_matrix}')
