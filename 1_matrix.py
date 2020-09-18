# реализуем класс Matrix, прегружаем методы, выводим результат работы программы ввиде новой матрицы

class Matrix:
    def __init__(self, list_1, list_2):  # перегружаем __init__
        self.list_1 = list_1
        self.list_2 = list_2

    def __str__(self):  # приводим матрицу в привычный вид
        matrix_1 = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix_1]))

    def __add__(self):  # реализуем сложение двух объектов класса Matrix
        matrix_1 = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matrix_1[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str("\n".join(["\t".join([str(j) for j in i]) for i in matrix_1]))


my_matrix_sum = Matrix([[5, 18, 11],
                        [6, 17, 23],
                        [41, 50, 9]],
                       [[45, 8, 2],
                        [6, 7, 93],
                        [24, 5, 97]])

print(f"Результат сложения двух матриц на основе значений list_1 и list_2:\n{my_matrix_sum.__add__()}")
