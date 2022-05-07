a = []
s1 = 123
s2 = 1.5
s3 = 'привет'
s4 = (1, 1)
s5 = [1, 2, 3]
s6 = set('abrakadabra')
s7 = 666
a.extend([s1, s2, s3, s4, s5, s6, s7])

my_list = a
for i in range(0, len(my_list)-1, 2):
    my_list[i], my_list[i + 1] = my_list [i + 1], my_list[i]
    i += 2
print(my_list)

