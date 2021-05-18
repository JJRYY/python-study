even_list = []
odd_list = []

for i in range(101):
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("짝수", even_list)
print("홀수", odd_list)

even_list = [i for i in range(101) if i % 2 == 0]
print(even_list)

even_list = [i for i in range(101) if i % 2 == 1]
print(odd_list)

list_a = [273, 32, 103, "문자열", True, False]
list_b = [i for i in list_a]
print(type(list_b), list_b)