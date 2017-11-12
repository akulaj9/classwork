import math

#--------------------------------------------------------------------------------
#print rectangle square
height = 10
width = 20
rectagle_scuare = height * width
print("Площадь прямоугольника при высоте %d см. и ширина %d см. равна %d кв.см." %
      (height, width, rectagle_scuare))

#--------------------------------------------------------------------------------
#print circle square
radius = 42
circle_square = radius**2 * math.pi
print("Площадь круга при радиусе %d см. равна %.2f" % (radius, circle_square))


print('Юникодный символ с кодом %d выглядит %s' % (0x26BD, '\u26BD'))

print('Юникодный символ с кодом %d выглядит %s' % (0x1F982, '\U0001F982'))

      #01234567
current_time = '18:38:01'
hours = int(current_time[:2])
print(hours)
minutes = int(current_time[3:5])
print(minutes)
seconds = int(current_time[6:])
print(seconds)
total_seconds = hours*3600 + minutes*60 + seconds
print(total_seconds)

current_time = '18:8:1'
lst = current_time.split(':')
hours = int(lst[0])
minutes = int(lst[1])
seconds = int(lst[2])
total_second = hours*3600 + minutes*60 + seconds
print(total_seconds)

