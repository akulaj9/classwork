import random
matrix = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

print(type(matrix[0]), matrix[0])
print(type(matrix[1]), matrix[1])
print(type(matrix[0][0]), matrix[0][0])
print(type(matrix[0][1]), matrix[0][1])
print(type(matrix[0][2]), matrix[0][2])
print(type(matrix[1][1]), matrix[1][1])

def print_matrix(matrix):
    print("ID:", id(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[1])):
            print(matrix[i][j], end=' | ')
        print()

print_matrix(matrix)

def multiply_matrix_by_n(matrix, coef):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] *= coef

multiply_matrix_by_n(matrix, 10)
print_matrix(matrix)

def fill_matrix(matrix, lower_bound, upper_bound):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = random.randint(lower_bound, upper_bound)

fill_matrix(matrix, 10, 100)
print_matrix(matrix)
