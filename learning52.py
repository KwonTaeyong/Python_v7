def solution(sticker):
    n = len(sticker)
    if n == 1:
        return sticker[0]

    # case1: 첫 번째 스티커를 사용하는 경우 (마지막은 사용 불가)
    dp1 = [0] * n
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    for i in range(2, n - 1):  # 마지막 제외
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])

    # case2: 첫 번째 스티커를 사용하지 않는 경우 (마지막 사용 가능)
    dp2 = [0] * n
    dp2[0] = 0
    dp2[1] = sticker[1]
    for i in range(2, n):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])

    return max(dp1[n - 2], dp2[n - 1])
