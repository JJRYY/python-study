key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}
for i in range(4):
    character[key_list[i]] = value_list[i]

print(character)
print()


limit = 10000
i = 1
sum_value = 0
while True:
    sum_value += i
    i += 1
    if sum_value >= limit:
        break

print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i-1, limit, sum_value))
print()

max_value = 0
temp = 0
a = 0
b = 0

for i in range(1, 100):
    j = 100 - i
    temp = i * j
    if max_value < temp:
        a = i
        b = j
        max_value = temp

print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))