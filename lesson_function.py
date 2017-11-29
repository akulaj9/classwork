import math
def hello(name):
    print('Hello, %s!!!' % (name))

hello('world')
hello('Allce')
hello('Eugenia')

def pretty_print(value):
    print('------------------------')
    print('Value: %s' % value)
    print('------------------------')

def rectangls_square(height, width):
    result = height * width
    return result

result1 = rectangls_square(10, 20)
pretty_print(result1)

def square_square(side):
    return rectangls_square(side, side)

pretty_print(square_square(50))

def add_and_multiply(x, y):
    result_add = x + y
    result_mult = x * y
    return result_add, result_mult, x**y

result2, result3, result4 = add_and_multiply(2, 3)
pretty_print(result2)
pretty_print(result3)
pretty_print(result4)


def celcius2faringeheit(degrees):
   return degrees * 9/5 + 32

print("%.2f" % celcius2faringeheit(36.6))
result = round(celcius2faringeheit(36.6))


def circle_square(radius):
    return math.pi * radius**2
print("%.2f" % circle_square(20))







