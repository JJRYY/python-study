list_a = [1, 2, 3]

print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

print("# 리시트 중간에 요소 추가하기")
list_a.insert(0, 10)
print(list_a)

print("# 리스트의 요소 하나 제거하기")
del list_a[5]
print("del list_a[5]: ", list_a)

list_a.pop(2)
print("pop(2): ", list_a)

list_a.remove(10)
print("remove(10): ", list_a)

list_a.clear()
print("clear(): ", list_a)
print()

array = [273, 32, 103, 57, 52]
for element in array:
    print(element)