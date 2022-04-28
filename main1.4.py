num = input(('Введите любое положительное число: '))
x = [int(x) for x in str(num)]
x.sort()
print(x[-1])