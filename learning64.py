def solution(cookie):
    n = len(cookie)
    max_sum = 0

    for m in range(n - 1):  # m은 중심점, m+1과 쌍을 이룰 수 있어야 함
        l, r = m, m + 1
        left_sum = cookie[l]
        right_sum = cookie[r]

        while l >= 0 and r < n:
            if left_sum == right_sum:
                max_sum = max(max_sum, left_sum)
                l -= 1
                r += 1
                if l >= 0:
                    left_sum += cookie[l]
                if r < n:
                    right_sum += cookie[r]
            elif left_sum < right_sum:
                l -= 1
                if l >= 0:
                    left_sum += cookie[l]
            else:
                r += 1
                if r < n:
                    right_sum += cookie[r]

    return max_sum
