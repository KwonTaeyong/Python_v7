from collections import deque

def solution(maze):
    n, m = len(maze), len(maze[0])

    # 방향 벡터 (상하좌우)
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]

    # 시작 / 도착 위치 찾기
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1: red_start = (i, j)
            if maze[i][j] == 2: blue_start = (i, j)
            if maze[i][j] == 3: red_end   = (i, j)
            if maze[i][j] == 4: blue_end  = (i, j)

    # 방문 체크는 bitmask로 (4x4=16칸)
    def pos_to_bit(x, y):
        return 1 << (x*m + y)

    # BFS state: (red_x, red_y, blue_x, blue_y, red_visit_mask, blue_visit_mask, turns)
    q = deque()
    visited = set()

    rmask = pos_to_bit(*red_start)
    bmask = pos_to_bit(*blue_start)

    init = (*red_start, *blue_start, rmask, bmask, 0)
    q.append(init)
    visited.add(init[:-1])  # turns 제외

    def can_move(nx, ny):
        return 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != 5

    while q:
        rx, ry, bx, by, rmask, bmask, t = q.popleft()

        # 둘 다 목적지 도착
        if (rx, ry) == red_end and (bx, by) == blue_end:
            return t

        # 다음 턴 이동 후보
        for drx, dry in dirs + [(0,0)]:   # (0,0)은 도착지에 있을 때만 유효
            nrx, nry = rx + drx, ry + dry
            for dbx, dby in dirs + [(0,0)]:
                nbx, nby = bx + dbx, by + dby

                # 도착한 말은 움직이지 않아야 한다
                if (rx, ry) == red_end and (drx, dry) != (0,0): continue
                if (bx, by) == blue_end and (dbx, dby) != (0,0): continue

                # 이동 불가능 좌표 체크
                if not can_move(nrx, nry): continue
                if not can_move(nbx, nby): continue

                # 방문했던 칸 재방문 금지
                if rmask & pos_to_bit(nrx, nry): continue
                if bmask & pos_to_bit(nbx, nby): continue

                # 두 말이 같은 칸으로 이동 금지
                if (nrx, nry) == (nbx, nby): continue

                # 자리 교환 금지
                if (nrx, nry) == (bx, by) and (nbx, nby) == (rx, ry):
                    continue

                # 새로운 방문 mask
                new_rmask = rmask | pos_to_bit(nrx, nry)
                new_bmask = bmask | pos_to_bit(nbx, nby)

                state = (nrx, nry, nbx, nby, new_rmask, new_bmask)

                if state in visited: continue
                visited.add(state)

                q.append((nrx, nry, nbx, nby, new_rmask, new_bmask, t+1))

    return 0
