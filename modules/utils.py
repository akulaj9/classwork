def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end='\t')
        print()

if __name__ == '__name__':
    print_matrix([[1,2,3],
              [4,5,6],
              [7,8,9]])

    print('hello from utils')
    print("__name__:", __name__)

