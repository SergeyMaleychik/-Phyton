def first_func(var_1, var_2, var_3):
    y = var_1, var_2, var_3
    z = sorted(y)
    a = sum(z[1::])
    return a
print(first_func(2, 1, 3))