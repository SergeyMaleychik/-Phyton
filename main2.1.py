a = []
s1 = 123
s2 = 1.5
s3 = 'привет'
s4 = (1, 1)
s5 = [1, 2, 3]
s6 = set('abrakadabra')
a.extend([s1, s2, s3, s4, s5, s6])

print(a)
for el in a:
    print(type(el))