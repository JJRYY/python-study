minCnt = 2
maxCnt = 10
allCnt = 100
memo = {}

def seat(restCnt, sitCnt):
    key = str([restCnt, sitCnt])
    # 종료 조건
    if key in memo:
        return memo[key]
    if restCnt < 0:
        return 0    # 무효이므로 0을 리턴
    if sitCnt == 0:
        return 1    # 유효하므로 수를 세기 위해 1을 리턴
    # 재귀 처리
    count = 0
    for i in range(sitCnt, maxCnt + 1):
        count += seat(restCnt - i, i)
    # 메모화 처리
    memo[key] = count
    # 종료
    return count

print(seat(allCnt, minCnt))
