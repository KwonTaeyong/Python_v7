def solution(land, P, Q):
    arr = []
    for row in land:
        arr.extend(row)
    arr.sort()

    def cost(h):
        total = 0
        for v in arr:
            if v < h:
                total += (h - v) * P
            else:
                total += (v - h) * Q
        return total

    left, right = arr[0], arr[-1]

    # 삼분 탐색
    while left + 3 < right:
        m1 = (2 * left + right) // 3
        m2 = (left + 2 * right) // 3
        if cost(m1) <= cost(m2):
            right = m2
        else:
            left = m1

    # 근처 범위에서 정확한 최소값 검색
    answer = float('inf')
    for h in range(left, right + 1):
        answer = min(answer, cost(h))

    return answer
