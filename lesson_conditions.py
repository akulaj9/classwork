a = 10
b = 20

if b != 0:
    result = a/b
    print("Result:", result)
    print("Result: %f.2" % result)
else:
    print("Zero division eror")


print()

a = 10
b = 20

is_not_zero = b != 0

def is_not_zero(value):
    return value != 0

def is__zero(value):
    return value == 0

if is_not_zero(b):
    result = a/b
    print("Result:", result)
    print("Result: %f.2" % result)
else:
    print("Zero division eror")

if is_not_zero(b):
    print("Zero division eror")
else:
    result = a / b
    print("Result: %f.2" % result)

print()

s = 'Mark Zukerberg'
if s[0] == 'M' or s[0] == 'm':
    print("'m' is rhe first lettter")

print()

x = 10
if x >= 5 and x <= 20:
    print('INSIDE')
else:
    print('OUTSIDE')

print()

def is_millenial(year_of_birth):
    return year_of_birth > 1981 and year_of_birth <= 2000

if is_millenial (1996):
    print("I'm millenian!")
else:
    print("I'm NOT millenian!")

print()

def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print(is_leap_year(2100))
print(is_leap_year(2000))
