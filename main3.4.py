def my_func(x, y):
    z = x**y
    return z
print(my_func(float(input()),int(input())))

def my_func_2(x, y):
    x = 1
    for i in range (0,y):
        x *= x
    return x
print(my_func(float(input()), int(input())))

