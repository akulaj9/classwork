def print_cinema_seats(rows, seats):
    for i in range (1, rows+1):
        print('Row %d:\t ' % i, end='')
        for j in range (1, seats+1):
            print('%d' % j, end=' ')
        print()

print_cinema_seats(15, 20)
print_cinema_seats(3, 4)
print_cinema_seats()


def calt_table(rows=10, columns=10):
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            print(i*j, end='\t')

calc_table()
calc_table(5, 5)