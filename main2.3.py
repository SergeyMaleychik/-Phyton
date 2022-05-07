my_dict = {1 : 'весна', 2 : 'лето', 3 : 'осень', 4 : 'зима'}
a = input("Введите месяц в виде целого числа от 1 до 12: ")
if a == 3 or a == 4 or a == 5:
    print(my_dict.get(1))
elif a == 6 or a == 7 or a == 8:
    print(my_dict.get(2))
elif a == 9 or a == 10 or a == 11:
    print(my_dict.get(3))
elif a == 12 or a == 1 or a == 2:
    print(my_dict.get(4))
