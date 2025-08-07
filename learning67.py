def solution(board, skill):
    n = len(board)
    m = len(board[0])
    diff = [[0] * (m + 1) for _ in range(n + 1)]

    for type_, r1, c1, r2, c2, degree in skill:
        delta = -degree if type_ == 1 else degree

        diff[r1][c1] += delta
        diff[r1][c2 + 1] -= delta
        diff[r2 + 1][c1] -= delta
        diff[r2 + 1][c2 + 1] += delta

    # 가로 누적합
    for i in range(n + 1):
        for j in range(1, m + 1):
            diff[i][j] += diff[i][j - 1]

    # 세로 누적합
    for j in range(m + 1):
        for i in range(1, n + 1):
            diff[i][j] += diff[i - 1][j]

    # 원래 board에 누적합 적용
    answer = 0
    for i in range(n):
        for j in range(m):
            board[i][j] += diff[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer
