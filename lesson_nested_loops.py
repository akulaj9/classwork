def print_cinema_seats(rows=15, seats=25):
    for i in range (1, rows+1):
        print('Row %d:\t ' % i, end='')
        for j in range (1, seats+1):
            is_vip_seat = (5 <= i <= 10) and (10 <= j <=15)
            if is_vip_seat:
                print('[%5s]' % j, end='')
            else:
                print('%s' % j, end='')
        print()

print_cinema_seats(15, 20)
print_cinema_seats(3, 4)
print_cinema_seats()


def calc_table(rows=10, columns=10):
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            print(i*j, end='\t')
        print()

calc_table()
calc_table(5, 5)

print("*************************")

def chees_table():
    for i in range(1, 8+1):
        for symbol in 'ABCDEFGH':
            print(symbol+str(i), end='\t')
        print()


chees_table()