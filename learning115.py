from collections import deque

def solution(maze):
    n, m = len(maze), len(maze[0])
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]

    # 각 칸의 인덱스를 0~15 사이로 부여
    def idx(r, c): return r * m + c

    # 시작/도착 위치 찾기
    red_start = blue_start = red_goal = blue_goal = None
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1: red_start = (i, j)
            elif maze[i][j] == 2: blue_start = (i, j)
            elif maze[i][j] == 3: red_goal = (i, j)
            elif maze[i][j] == 4: blue_goal = (i, j)

    # BFS
    q = deque()
    visited = set()

    rsi, rsj = red_start
    bsi, bsj = blue_start
    mask_r = 1 << idx(rsi, rsj)
    mask_b = 1 << idx(bsi, bsj)

    q.append((rsi, rsj, bsi, bsj, mask_r, mask_b, 0))
    visited.add((rsi, rsj, bsi, bsj, mask_r, mask_b))

    def is_valid(r, c):
        return 0 <= r < n and 0 <= c < m and maze[r][c] != 5

    while q:
        rr, rc, br, bc, mr, mb, dist = q.popleft()

        # 둘 다 도착 시
        if (rr, rc) == red_goal and (br, bc) == blue_goal:
            return dist

        # 다음 이동 후보 (도착하면 제자리 유지)
        red_moves = []
        blue_moves = []

        if (rr, rc) == red_goal:
            red_moves = [(rr, rc)]
        else:
            for dr, dc in dirs:
                nr, nc = rr + dr, rc + dc
                if is_valid(nr, nc) and not (mr & (1 << idx(nr, nc))):
                    red_moves.append((nr, nc))

        if (br, bc) == blue_goal:
            blue_moves = [(br, bc)]
        else:
            for dr, dc in dirs:
                nr, nc = br + dr, bc + dc
                if is_valid(nr, nc) and not (mb & (1 << idx(nr, nc))):
                    blue_moves.append((nr, nc))

        # 두 수레의 가능한 이동 조합 모두 시도
        for nr, nc in red_moves:
            for nb_r, nb_c in blue_moves:
                # 같은 칸으로 이동 금지
                if (nr, nc) == (nb_r, nb_c):
                    continue
                # 서로 자리 바꾸기 금지
                if (nr, nc) == (br, bc) and (nb_r, nb_c) == (rr, rc):
                    continue

                nmr = mr | (1 << idx(nr, nc))
                nmb = mb | (1 << idx(nb_r, nb_c))
                state = (nr, nc, nb_r, nb_c, nmr, nmb)

                if state not in visited:
                    visited.add(state)
                    q.append((nr, nc, nb_r, nb_c, nmr, nmb, dist + 1))

    return 0
