def solution(cookie):
    n = len(cookie)
    answer = 0

    for m in range(n - 1):
        l = m
        r = m + 1
        left_sum = cookie[l]
        right_sum = cookie[r]

        while True:
            if left_sum == right_sum:
                answer = max(answer, left_sum)

            if left_sum <= right_sum:
                l -= 1
                if l < 0:
                    break
                left_sum += cookie[l]
            else:
                r += 1
                if r >= n:
                    break
                right_sum += cookie[r]

    return answer
