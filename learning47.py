def solution(sticker):
    n = len(sticker)
    if n == 1:
        return sticker[0]

    # Case 1: 첫 번째 스티커를 선택한 경우 (마지막 스티커는 못 씀)
    dp1 = [0] * n
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    for i in range(2, n - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])

    # Case 2: 첫 번째 스티커를 선택하지 않은 경우 (마지막 스티커 사용 가능)
    dp2 = [0] * n
    dp2[0] = 0
    dp2[1] = sticker[1]
    for i in range(2, n):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])

    return max(dp1[n - 2], dp2[n - 1])
def solution(sticker):
    n = len(sticker)
    if n == 1:
        return sticker[0]

    # Case 1: 첫 번째 스티커를 선택한 경우 (마지막 스티커는 못 씀)
    dp1 = [0] * n
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    for i in range(2, n - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])

    # Case 2: 첫 번째 스티커를 선택하지 않은 경우 (마지막 스티커 사용 가능)
    dp2 = [0] * n
    dp2[0] = 0
    dp2[1] = sticker[1]
    for i in range(2, n):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])

    return max(dp1[n - 2], dp2[n - 1])

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))  # 36
print(solution([1, 3, 2, 5, 4]))             # 8

