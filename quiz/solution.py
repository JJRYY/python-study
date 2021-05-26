"""
배열 array의   i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 한다.
예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면
     a. array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
     b. a에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
     c. b에서 나온 배열의 3번째 숫자는 5입니다.

배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성하시오

입출력 예

array                        commands                       return
[1, 5, 2, 6, 3, 7, 4]  [[2, 5, 3], [4, 4, 1], [1, 7, 3]]    [5, 6, 3]


입출력 예 설명
[1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. [2, 3, 5, 6]의 세 번째 숫자는 5입니다.
[1, 5, 2, 6, 3, 7, 4]를 4번째부터 4번째까지 자른 후 정렬합니다. [6]의 첫 번째 숫자는   6입니다.
[1, 5, 2, 6, 3, 7, 4]를 1번째부터 7번째까지 자릅니다. [1, 2, 3, 4, 5, 6, 7]의   세 번째 숫자는 3입니다.

파일명 solution.py
def solution(array, commands):
	answer = []
	return answer

if __name__="__main__":
	array = [1, 5, 2, 6, 3, 7, 4]
	commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

	result = solution(array, commands)
	print(type(result), result) 	# list [5, 6, 3]
"""


def solution(array, commands):
    answer = []
    # for list_a in commands:
    #     temp = array[list_a[0]-1: list_a[1]]
    #     temp.sort()
    #     answer.append(temp[list_a[2]-1])
    for a, b, c in commands:
        answer += [sorted(array[a-1:b])[c-1]]
    return answer

def solution2(array, commands):
    return [sorted(array[a-1:b])[c-1] for a, b, c in commands]

if __name__ == "__main__":
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    result = solution(array, commands)
    print(type(result), result)