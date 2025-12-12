def solution(board):
    N = len(board)
    answer = 0

    # 블록의 5가지 제거 패턴 정의
    PATTERNS = [
        [(0,0),(0,1),(1,1),(1,2)],
        [(0,1),(1,1),(1,0),(2,0)],
        [(0,1),(1,1),(1,2),(2,1)],
        [(1,0),(1,1),(2,1),(2,2)],
        [(0,0),(1,0),(1,1),(2,1)]
    ]

    def can_fill(r, c):
        """ (r, c) 위에 검은 블록을 떨어뜨릴 수 있는지 = 위가 모두 0인가 """
        for i in range(r):
            if board[i][c] != 0:
                return False
        return True

    def check(r, c):
        """ (r,c)를 포함하는 3x3 영역에서 제거할 블록 탐색 """
        block_num = board[r][c]
        coords = []

        # 3x3 범위에서 block_num의 좌표들을 수집
        for i in range(r, r+3):
            for j in range(c, c+3):
                if i < N and j < N and board[i][j] == block_num:
                    coords.append((i, j))

        # 블록 크기가 반드시 3~4 칸
        if not (3 <= len(coords) <= 4):
            return False

        # 각 패턴과 매칭 시도
        for pattern in PATTERNS:
            # 패턴의 기준 (r,c)를 기준으로 모든 좌표 만들어보기
            valid = True
            empty_blocks = []
            for (dr, dc) in [(x, y) for x in range(3) for y in range(3)]:
                nr, nc = r + dr, c + dc
                if nr >= N or nc >= N:
                    valid = False
                    break

            if not valid:
                continue

            # 패턴에 해당하는 4칸이 모두 block_num인지 체크
            blocks = [(r+pr, c+pc) for (pr, pc) in pattern]
            if any(board[x][y] != block_num for x, y in blocks):
                continue

            # 패턴에서 block이 아닌 2칸 찾기
            pattern_set = set(blocks)
            empty_blocks = []
            for i in range(r, r+3):
                for j in range(c, c+3):
                    if (i, j) not in pattern_set:
                        if board[i][j] != 0:
                            valid = False
                            break
                        empty_blocks.append((i, j))
                if not valid:
                    break

            if not valid:
                continue

            # 빈칸(2곳) 위로 검은 블록 떨어뜨릴 수 있어야 함
            if all(can_fill(x, y) for x, y in empty_blocks):
                return True

        return False

    while True:
        removed = False
        
        for r in range(N):
            for c in range(N):
                if board[r][c] != 0:
                    if check(r, c):
                        # 해당 블록 삭제
                        target = board[r][c]
                        for i in range(N):
                            for j in range(N):
                                if board[i][j] == target:
                                    board[i][j] = 0
                        answer += 1
                        removed = True

        if not removed:
            break

    return answer
