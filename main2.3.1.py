my_list = ('весна', 'лето', 'осень', 'зима')
a = int(input("Введите месяц в виде целого числа от 1 до 12: "))
if a == 3 or a == 4 or a == 5:
    print(my_list[0])
elif a == 6 or a == 7 or a == 8:
    print(my_list[1])
elif a == 9 or a == 10 or a == 11:
    print(my_list[2])
elif a == 1 or a == 2 or a == 12:
    print(my_list[3])