import random
# x = 10
#
# while x > 0:
#     print('Hello world!', x)
#     x -= 1
#     # x = x -1
#
# print()
#
# x = 10
# while x < 100:
#     print('Hello world!', x)
#     x += random.randint(0, 5)

print()

# def fill_truck(volume_capacity, lower_bound, upper_bound):
#     current_capacity = 0
#
#     while current_capacity < volume_capacity:
#         random_box = random.randint(lower_bound, upper_bound)
#         if random_box <= (volume_capacity - current_capacity):
#             current_capacity += random_box
#             print('Current capacity = %d, last box = %d' % (current_capacity, random_box))
#         else:
#             print('Sskipped box %d' % random_box)
#
# fill_truck(1000, 1, 20)

print()

print("Привет, Богатырь!")
print("1: Налево пойдешь - коня найдешь")
print("2: Направо пойдешь - полцарства найдешь")
print("3: Прямо пойдешь - мешок денег найдешь")
print("4: Назад пойдешь - жену найдешь")

while True:
    user_choice = input("Сделай свой выбор [1..4], q = выход: ")
    # print (user_choice)

    if user_choice == 'q':
        print("Заходи еще!")
        break

    valid_input = True
    if not user_choice.isnumeric():
        valid_input = False

    elif not (1 <= int(user_choice)<= 4):
        valid_input = False

    if not valid_input:
        print('Сделай правильный выбор [1..4], q = выход!!!')
        continue


    user_choice = int (user_choice)
    if user_choice == 1:
        print("Лошадку жалко :(")

    elif user_choice == 2:
        print("Молодец!")

    elif user_choice == 3:
         print("10% за подсказку!")

    elif user_choice == 4:
        print("Совет да любовь!!")

       # else:
        #    print('Сделай правильный выбор [1..4], q = выход!!!')
    #else:
     #   print('Сделай правильный выбор [1..4], q = выход!!!')


    #else:
    #    print('Сделай правильный выбор [1..4], q = выход!!!')


