numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number >= 100:\
        print("- 100 이상의 수: ", number)

print()

for number in numbers:
    if number % 2 == 1:
        print(number, " 는 홀수입니다.")
    else:
        print(number, " 는 짝수입니다.")

print()

for number in numbers:
    print(number, " 는", len(str(number)), "자릿수입니다.")

print()

list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]

for i in list_of_list:
    for j in i:
        print(j)

list_seq = [i for sub_list in list_of_list for i in sub_list]
print("list_seq ", list_seq)

print()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number in numbers:
    output[(number + 2) % 3].append(number)

print(output)