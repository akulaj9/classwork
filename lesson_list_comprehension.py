import math
import string
import random

lst = []
for i in range (1, 101):
    lst.append(i)

print(lst)

print("***************")

lst2 = [i for i in range(1, 101)]
print(lst2)

print("***************")

lst3 = [i**2 for i in range(1, 101)]
print(lst3)

print("***************")

lst4 = [i**2 for i in range(1, 101) if i**2 % 5 ==0]
print(lst4)

print("***************")

angles = [40, 45, 60]

results = [round(math.cos(math.pi*angles/180),2 ) for angles in angles]
print(results)

print("***************")

text = 'Согласно древней индийской легенде создатель шахмат за своё изобретение попросил у раджи незначительную, на первый взгляд, награду: столько пшеничных зёрен, сколько окажется на шахматной доске'

zipped = [c for c in text if not (c in 'уеыаоэяиюё')]
print(''.join(zipped))

zipped2 = [''.join([c for c in word if not (c in 'уеыаоэяиюё')]) if len(word)> 5 else word
           for word in text.split()]

print(' '.join(zipped2))
print(len(zipped2)/len(text))

print("***************")

alphabet = [chr(code) for code in range(ord('a'), ord('z')+1)]
print(''.join(alphabet))
print(string.ascii_lowercase)
print(string.digits)

my_digits = [str(i) for i in range(10)]
print(''.join(my_digits))
print(string.digits)

#######################
print(sum(lst2))
print(max(lst2))
print(min(lst2))
print(sum(lst2)/len(lst2))

lst_random = ([random.randint(10, 20) for i in range(100)])
print(sum(lst_random), lst_random)

print("***************")

lst5 = [1 for i in range(1, 101) if i%3 == 0]
print(sum(lst5), lst5)

print("***************")

lst6 = [5,2,3,4,1,6][::-1]
num_of_swaps = sum([1 for idx, elem in enumerate(lst6)if idx+1 != elem])
print(num_of_swaps)
print(num_of_swaps/len(lst6)> 0.8)

print("***************")

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

fact_10 = factorial(10)
print(fact_10)