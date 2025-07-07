from collections import deque

def solution(grid):
    n, m = len(grid), len(grid[0])
    snowballs = []

    # 눈덩이 위치 추출
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'o':
                snowballs.append((i, j))

    # 각 눈덩이에서 도달 가능한 (x, y, 크기) 저장
    def bfs(start_x, start_y):
        visited = [[[False] * 11 for _ in range(m)] for _ in range(n)]
        q = deque()
        q.append((start_x, start_y, 1))
        visited[start_x][start_y][1] = True
        results = dict()  # {(x, y): set of sizes}

        while q:
            x, y, size = q.popleft()
            if (x, y) not in results:
                results[(x, y)] = set()
            results[(x, y)].add(size)

            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if grid[nx][ny] == '#':
                        continue
                    if grid[nx][ny] == '.':
                        nsize = size + 1
                    else:
                        nsize = size
                    if nsize <= 10 and not visited[nx][ny][nsize]:
                        visited[nx][ny][nsize] = True
                        q.append((nx, ny, nsize))
        return results

    path1 = bfs(*snowballs[0])
    path2 = bfs(*snowballs[1])

    snowmen = set()

    for (x1, y1), sizes1 in path1.items():
        for (x2, y2), sizes2 in path2.items():
            if abs(x1 - x2) + abs(y1 - y2) == 1:  # 인접해야 눈사람 가능
                for s1 in sizes1:
                    for s2 in sizes2:
                        if s1 <= s2:
                            snowmen.add((s2, s1))  # (몸통, 머리)

    return len(snowmen)
