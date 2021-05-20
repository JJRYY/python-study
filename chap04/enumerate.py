example_list = ["요소A", "요소B", "요소C"]

print("# 단순 출력")
print(example_list)
print()

print("#enumerate() 함수 적용 출력")
print(enumerate(example_list))
print()

print("# list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))
print()

print("# 반복문과 조합하기")
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i, value))

print()

example_dictionary = {
    "키A": "값A",
    "키B": "값B",
    "키C": "값C"
}

print("#딕셔너리의 items() 함수")
print("items():", example_dictionary.items())
print()

print("#딕셔너리의 items() 함수와 반복문 조합하기")
for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, element))
print()

array = [i * i for i in range(0, 20, 2)]
print(array)
print()

array = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in array if fruit != "초콜릿"]
print(output)
print()

output = [i for i in range(1, 101) if str("{:b}".format(i)).count('0') == 1]

for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계:", sum(output))

