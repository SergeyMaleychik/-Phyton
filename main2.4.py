a = input("введите предложение :").split(' ')
for i, item in enumerate(a):
    if len(str(item)) <= 10:
        print(i + 1, item)
    elif len(str(item)) >= 10:
        print(i + 1, item[:2])
