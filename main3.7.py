
def int_func(text):
    return text.title()
string = input().split()
lst = []
for i in string:
    lst.append(int_func(i))
print(' '.join(lst))