def solution(board):
    N = len(board)
    answer = 0

    def can_remove(block):
        coords = [(r, c) for r in range(N) for c in range(N) if board[r][c] == block]
        rows = [r for r, _ in coords]
        cols = [c for _, c in coords]

        min_r, max_r = min(rows), max(rows)
        min_c, max_c = min(cols), max(cols)

        empty = []
        for r in range(min_r, max_r + 1):
            for c in range(min_c, max_c + 1):
                if board[r][c] == 0:
                    empty.append((r, c))
                elif board[r][c] != block:
                    return False

        # 빈 칸 위에 다른 블록이 있으면 안 됨
        for r, c in empty:
            for k in range(r):
                if board[k][c] != 0:
                    return False

        return True

    changed = True
    while changed:
        changed = False
        blocks = set()
        for i in range(N):
            for j in range(N):
                if board[i][j] != 0:
                    blocks.add(board[i][j])

        for block in blocks:
            if can_remove(block):
                for i in range(N):
                    for j in range(N):
                        if board[i][j] == block:
                            board[i][j] = 0
                answer += 1
                changed = True
                break  # 하나 제거하면 다시 처음부터 검사

    return answer
