def s_calc():
    while 1:
        try:
            a = float(input("Введите делимое: "))
            c = float(input("Введите делитель: "))
            y = a / c
            break
        except ZeroDivisionError:
            print (f'Ошибка! Делить на ноль нельзя')
        if c != 0:
            y = a / c
    return y
print(s_calc())
