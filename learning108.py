from collections import deque

def solution(grid):
    n = len(grid)
    m = len(grid[0])
    
    # 상하좌우
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    
    # 눈덩이 위치 찾기
    balls = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'o':
                balls.append((i, j))
    (r1, c1), (r2, c2) = balls
    
    def bfs(start_r, start_c):
        visited = [[[False]*(n*m+2) for _ in range(m)] for _ in range(n)]
        q = deque()
        q.append((start_r, start_c, 1))
        visited[start_r][start_c][1] = True
        sizes = set([1])
        while q:
            r, c, size = q.popleft()
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != '#':
                    new_size = size
                    if grid[nr][nc] == '.':
                        new_size += 1
                    if not visited[nr][nc][new_size]:
                        visited[nr][nc][new_size] = True
                        sizes.add(new_size)
                        q.append((nr, nc, new_size))
        return sizes

    s1 = bfs(r1, c1)
    s2 = bfs(r2, c2)
    
    # 눈사람 조합 계산
    snowmen = set()
    for body in s1:
        for head in s2:
            if body >= head:
                snowmen.add((body, head))
    for body in s2:
        for head in s1:
            if body >= head:
                snowmen.add((body, head))
    return len(snowmen)
