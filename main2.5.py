my_list = [5, 4, 3, 2, 1]
print(f"Рейтинг {my_list} ")
a = int(input("Введите число "))
while a != 000:
    for el in range(len(my_list)):
        if my_list[el] == a:
            my_list.insert(el + 1, a)
            break
        elif my_list[0] < a:
            my_list.insert(0, a)
        elif my_list[-1] > a:
            my_list.append(a)
        elif my_list[el] > a and my_list[el + 1] < a:
            my_list.insert(el + 1,a)
    print(f"текущий список - {my_list}")
    a = int(input("Введите число (000 - выход) "))