def flatten(data):
    list_a = []
    for i in data:
        if type(i) == list:
            list_a += flatten(i)
        else:
            list_a.append(i)
    return list_a

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본:", example)
print("변환:", flatten(example))