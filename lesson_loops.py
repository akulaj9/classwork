import random
print('hello world')
print('hello world')
print('hello world')

print()

for i in range(10):
    if i % 2 == 0:
        print('hello world', i)

print()

for i in range(10, 20, 2):
      print('hello world', i)

print()

for i in range(0, 1001, 10):
    print(i, 'yw')

print()

for symbol in 'abcd':
    print(symbol)

for elem in [1, 2, 3]:
    print(elem)

print()

s = 'Вы перешли в режим инкогнито'
num_of_spaces = 0
for symbol in s:
    if symbol == ' ':
        #num_of_spaces = num_of_spaces + 1
        num_of_spaces +=1
        #print("вы нашли пробел!", num_of_spaces)
print('Num of spaces:', num_of_spaces)

print()

def sum_of_n(num_limit):
    total_sum = 0
    for i in range(1, num_limit+1):
        total_sum +=i

    return total_sum

print('sum of first %d numbers is equal to %d' % (1000, sum_of_n(1000)))

print()

total_height = 0
for i in range(12):
    height = random.randint(160, 185)
    total_height += height

print("Total height = %d" % total_height)
print("Avr_height = %f" % (total_height / 12))


def find_avr_of_n(num_limit, lower_bound, upper_bound):
    total_sum = 0
    for i in range(num_limit):
        height = random.randint(lower_bound, upper_bound)
        total_sum += height

        return total_sum / num_limit

print("Avr. value = %.2f" % find_avr_of_n(13, 160, 185))

print()

def find_max_of_n(num_limit, lower_bound, upper_bound):
    curr_max = lower_bound
    for i in range(num_limit):

        rand_number = random.randint(lower_bound, upper_bound)
        print('rand. number: ', rand_number)

        if rand_number > curr_max:
            curr_max = rand_number

    return curr_max

result = find_max_of_n(10, 100, 200)
print("Max value: %d" % result)

print()

def find_min_of_n(num_limit, lower_bound, upper_bound):
    curr_min = upper_bound
    for i in range(num_limit):

        rand_number = random.randint(lower_bound, upper_bound)
        print('rand. number: ', rand_number)

        if rand_number < curr_min:
            curr_min = rand_number

    return curr_min

result = find_min_of_n(10, 100, 200)
print("Min value: %d" % result)
