import string
import random
import math

password = 'acvXyz42'
result = all(  any(1 for c in password if c in pattern)
               for pattern in (string.digits, string.ascii_lowercase, string.ascii_uppercase))
print(result)

dots = [[random.random(), random.random()] for i in range(100000)]
my_pi = sum(1 for dot in dots if math.sqrt((0.5-dot[0])**2 + (0.5-dot[1])**2) <= 0.5)/(len(dots)*0.5**2)
print(my_pi)

lst = ['aaa', 'b', 'cc']
lst.sort(key=len)
print(lst)
lst.sort()
print(lst)

print("*****************")

planets = ['mercrury', 'venus', 'earth', 'mars', 'jupiter', 'saturn']
planets.sort()
print(planets)

print("*****************")

planets = [['mercrury', 4524],
           ['earth', 765333],
           ['mars', 7456733],
           ['jupiter', 56563333],
           ['venus', 73566],
           ['saturn', 683333333]]


planets.sort()
print(planets)

def get_distance(planet_info):
    return planet_info[1]

planets.sort(key=get_distance)
print(planets)

print("*****************")

pois = [7, 8, 11, 12, 5, 0, 123, 9]
pois.sort()
print(pois)

def get_distance_from_our_location(coord):
    return abs(coord - 10)

pois.sort(key=get_distance_from_our_location)
print(pois)

pois.sort(key=lambda elem: abs(elem-10))
print(pois)

##################################
print("*****************")

group = [
    ['Пасибаева Ольга', '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0'],
    ['Семков Дмитрий', '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'],
    ['Ивасюк Дарья', '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'],
    ['Филипчук Алексей', '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,0,0,0,0,0'],
    ['Чугунова Кристина', '1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'],
    ['Азаренков Артур', '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0'],
    ['Николаева Евгения', '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'],
    ['Кучанский Александр', '1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'],
    ['Макеев Александр', '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0'],
    ['Берёза Дмитрий ', '1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'],
    ['Алохин Эдгар', '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'],
    ['Пекарский Ярослав', '1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'],
    ['Доманина Дария', '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0']
]


def print_full_names(group):
    print('--- students ---')
    for i in range(len(group)):
        print(group[i][0])

print_full_names(group)

def print_full_names_sorted(group):
    group.sort(key=lambda elem: elem[0].split()[1])
    print_full_names(group)

print_full_names_sorted(group)

def print_ranks(group):
    print('--- students ranks ----')
    for i in range(len(group)):
        #print(group[i][1])
        total_rank = group[i][1].count('1')
        print(group[i][0], total_rank)
        group[i][1] = total_rank

print_ranks(group)

def get_ranks_sorted(group):
    group.sort(key=lambda elem: elem[1], reverse=True)
    print('--- students rank sorted ---')
    for i in range(len(group)):
        print(group[i][0], group[i][1])

get_ranks_sorted(group)


def print_top_n(students_rank, n=3):
    print('--- Top %d students ---' % n)
    for i in range(n):
        print(group[i][0], group[i][1])

print_top_n(group, 5)
