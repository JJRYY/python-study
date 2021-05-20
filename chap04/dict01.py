# 딕셔너리 선언
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

# 출력
print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient:", dictionary["ingredient"])
for ingredient in dictionary["ingredient"]:
    print("ingredient:", "index", dictionary["ingredient"].index(ingredient), "->", ingredient)
print("origin: ", dictionary["origin"])
print()

# 값 변경
dictionary["name"] = "8D 건조 망고"
print("name:", dictionary["name"])
print(dictionary)

# # 입력받기
# key = input("> 접근하고자 하는 키: ")
#
# # 출력
# if key in dictionary:
#     print(dictionary[key])
# else:
#     print("존재하지 않는 키에 접근하고 있습니다.")

# 존재하지 않는 키에 접근
value = dictionary.get("존재하지 않는 키")
print("값:", value)

# none 확인 방법
if value == None:
    print("존재하지 않는 키에 접근했습니다.")
print()

# for 반복문 사용
for key in dictionary:
    print(key, ":", dictionary[key])

pets = [
    {"name":"구름", "age": 5},
    {"name":"초코", "age": 3},
    {"name":"아지", "age": 1},
    {"name":"호랑이", "age": 1}
]
print("우리 동네 애완 동물")
for i in pets:
    print(i["name"], str(i["age"]) + "살")

print()

numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1

print(counter)
print()

character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    if type(character[key]) is dict:
        for items in character[key]:
            print(items, ":", character[key][items])
    elif type(character[key]) is list:
        for skill in character[key]:
            print(key, ":", skill)
    else:
        print(key, ":", character[key])

print()

