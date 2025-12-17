from collections import deque

def solution(grid):
    n, m = len(grid), len(grid[0])
    grid = [list(row) for row in grid]

    # 눈덩이 위치 찾기
    snowballs = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'o':
                snowballs.append((i, j))

    # BFS로 한 눈덩이가 도달 가능한 눈(.) 개수 계산
    def max_size(start):
        q = deque([start])
        visited = set([start])
        snow = 0

        while q:
            x, y = q.popleft()
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if (nx, ny) not in visited and grid[nx][ny] != '#':
                        visited.add((nx, ny))
                        q.append((nx, ny))
                        if grid[nx][ny] == '.':
                            snow += 1

        return snow + 1  # 초기 크기 1 포함

    a = max_size(snowballs[0])
    b = max_size(snowballs[1])

    # 가능한 눈사람 종류 세기
    max_body = max(a, b)
    max_head = min(a, b)

    answer = 0
    for body in range(1, max_body + 1):
        answer += min(body, max_head)

    return answer
