import random as rd
print("# random 모듈")

# random(): 0.0 <= x < 1.0 사이의 float를 리턴
print("- random():", rd.random())

# uniform(min, max): 지정한 범위 사이의 float를 리턴
print("- uniform(10, 20):", rd.uniform(10, 20))

# randrange(): 지정한 범위의 int를 리턴
# - randrange(max): 0부터 max 사이의 값을 리턴
# - randrange(min, max): min부터 max 사이의 값을 리턴
print("- randrange(10):", rd.randrange(10))

# choice(list): 리스트 내부에 있는 요소를 랜덤하게 선택
print("- choice([1, 2, 3, 4, 5]):", rd.choice(([1, 2, 3, 4, 5])))

# shuffle(list): 리스트의 요소들을 랜덤하게 섞음
print("- shuffle([1, 2, 3, 4, 5]):", rd.shuffle([1, 2, 3, 4, 5]))

# sample(list, k=<숫자>): 리스트의 요소 중에 k개를 뽑음
print("- sample([1, 2, 3, 4, 5], k=2:", rd.sample([1, 2, 3, 4, 5], k=2))