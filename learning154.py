def solution(visible, hidden, k):
    n = len(visible)
    m = len(visible[0])
    answer = 0

    for mask in range(1 << n):  # 행 뒤집기 상태
        row_cost = k * bin(mask).count("1")
        total = 0

        for j in range(m):
            no_flip = 0
            flip = -k  # 열 뒤집기 비용

            for i in range(n):
                flipped = (mask >> i) & 1
                if flipped == 0:
                    no_flip += visible[i][j]
                    flip += hidden[i][j]
                else:
                    no_flip += hidden[i][j]
                    flip += visible[i][j]

            total += max(no_flip, flip)

        answer = max(answer, total - row_cost)

    return answer
