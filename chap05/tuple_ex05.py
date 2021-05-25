list_a = ['a', 'b', 'c']

for e in list_a:
    print(e)

for i, v in enumerate(list_a):
    print(i, v, sep=':')

a, b = 97, 40
x, y = divmod(a, b)
print("x = {}, y = {}".format(x, y))