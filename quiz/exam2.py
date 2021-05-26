list_a = [[10, 20], [30, 40, 70, 110], [50, 60], [80, 90, 100]]
dict_a = {'k': {'a': 10, 'b': 20}, 'l': {'a': 10, 'b': 20, 'c': 40}, 'm': {'a': 10}}

for key in dict_a:
    output = key + " -> "
    for item in dict_a[key]:
        output += "{} : {} ".format(item, dict_a[key][item])
    print(output)


for a in list_a:
    output2 = ""
    for b in a:
        output2 += str(b) + " "
    print(output2)
