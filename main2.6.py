a = []
b = []
number = 0
while True:
    a1 = input('Введите название товара \n')
    a2 = input('Введите цену товара \n')
    a3 = input('Введите колличетво товара \n')
    a4 = input('Введите единицу измерения товара \n')
    a5 = input('Завершить(да/нет) \n')
    if a5 == 'да':
        number += 1
        a.append(number)
        a.append(a1)
        a.append(a2)
        a.append(a3)
        a.append(a4)
        b.append(tuple([number, {'название': a1, 'цена': a2, 'количество': a2, 'ед': a4}]))
        print(a)
        print(b)
        break
    if a5 == 'нет':
        number += 1
        a.append(number)
        a.append(a1)
        a.append(a2)
        a.append(a3)
        a.append(a4)
        b.append(tuple([number, {'название': a1, 'цена': a2, 'количество': a2, 'ед': a4}]))
    print(a)
    print(b)
numdergood = a[0::5]
name = a[1::5]
price = a[2::5]
coll = a[3::5]
edizm = a[4::5]

ny_dict2 = {'название': a[1::5], 'цена': a[2::5], 'количество': a[3::5], 'ед': a[4::5]}
print(ny_dict2)
