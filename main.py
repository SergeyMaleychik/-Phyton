x = int(input('колличество километров в первый день: '))
y = int(input('колличество километров в последний день: '))
day = 1
while y - x > 0:
    x = x + (x * 0.1)
    day += 1
print("Спортсмен достиг результата на " +  str(day) + ' день')


