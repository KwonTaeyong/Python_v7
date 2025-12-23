def solution(clockHands):
    n = len(clockHands)
    INF = float('inf')
    answer = INF

    # 시계 돌리기
    def rotate(board, x, y, cnt):
        for _ in range(cnt):
            board[x][y] = (board[x][y] + 1) % 4
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    board[nx][ny] = (board[nx][ny] + 1) % 4

    # 첫 행 모든 경우 탐색
    from itertools import product
    for first in product(range(4), repeat=n):
        board = [row[:] for row in clockHands]
        cnt = 0

        # 첫 행 적용
        for j in range(n):
            if first[j]:
                rotate(board, 0, j, first[j])
                cnt += first[j]

        # 2행부터 처리
        for i in range(1, n):
            for j in range(n):
                if board[i-1][j] != 0:
                    need = (4 - board[i-1][j]) % 4
                    rotate(board, i, j, need)
                    cnt += need

        # 마지막 행 체크
        if all(board[n-1][j] == 0 for j in range(n)):
            answer = min(answer, cnt)

    return answer
