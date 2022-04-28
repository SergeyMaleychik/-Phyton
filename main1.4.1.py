x = input(('Введите любое положительное число: '))
i = int(x)
r = -1
while i > 10:
    d = i % 10
    i //= 10
    if d > r:
        r = d
print(r)
