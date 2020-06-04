class Matrix:

    def __init__(self, my_m):
        self.my_m = my_m

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.my_m)):
            for j in range(len(self.my_m[0])):
                summ = other.my_m[i][j] + self.my_m[i][j]
                numbers.append(summ)
                if len(numbers) == len(self.my_m):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)

    def __str__(self):
        return str('\n'.join(['\t'.join([str(k) for k in i]) for i in self.my_m]))


test_matrix_1 = Matrix([
    [2, 3, 5],
    [2, 5, 2],
    [6, 1, 1],
])
test_matrix_2 = Matrix([
    [5, 7, 8],
    [2, 3, 9],
    [1, 1, 1],
]
)
print(f'Matrixa 1:\n {test_matrix_1}')
print()
print(f'Matrixa 2:\n {test_matrix_2}')
print()
print(f'Summ:\n {test_matrix_1 + test_matrix_2}')
