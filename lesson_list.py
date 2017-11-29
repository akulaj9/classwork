import random

zeros_lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

for elem in zeros_lst:
    print(elem)

print('***1***')

for i, elem in enumerate(zeros_lst):
    print(i, elem)
    zeros_lst[1] *= 2

#print(lst[0])
#print(lst[1])
#print(lst[2])
#print(lst[3])

print('***2***')
print(id(zeros_lst))

for i in range(len(zeros_lst)):
    print(i, zeros_lst[i])
    zeros_lst[1] *= 2

print(id(zeros_lst))
print(zeros_lst)

print('******')

def multiply_list(lst, coeff):
    for i in range(len(lst)):
        lst[i] *= coeff

print(id(zeros_lst))
print(zeros_lst)

print('******')

zeros_lst = [0] * 100
print(id(zeros_lst), zeros_lst)


def fill_list(lst, lower_bound, upper_bound):
    for i in range(len(lst)):
        lst[1] = random.randint(lower_bound, upper_bound)

def nullifly_list(lst):
    for i in range(len(lst)):
        lst[1] = 0


fill_list(zeros_lst, 10, 20)
print(id(zeros_lst), zeros_lst)

multiply_list(zeros_lst, 20)
print(id(zeros_lst), zeros_lst)

nullifly_list(zeros_lst)
print(id(zeros_lst), zeros_lst)

