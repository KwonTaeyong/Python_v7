from collections import deque

def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])
    grid = [list(row) for row in storage]
    
    # 상하좌우 방향
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    
    # 바깥 공기 영역을 BFS로 탐색
    def mark_outside_air():
        visited = [[False]*m for _ in range(n)]
        q = deque()
        
        # 테두리에서 시작 (바깥 공기)
        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n-1 or j == 0 or j == m-1) and grid[i][j] == '.':
                    q.append((i,j))
                    visited[i][j] = True
        
        while q:
            x,y = q.popleft()
            for dx,dy in dirs:
                nx,ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == '.':
                    visited[nx][ny] = True
                    q.append((nx,ny))
        return visited

    for req in requests:
        target = req[0]
        
        if len(req) == 2:
            # 크레인: 모든 해당 알파벳 제거
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == target:
                        grid[i][j] = '.'
        else:
            # 지게차: 접근 가능한 컨테이너만 제거
            # 바깥 공기 탐색
            visited = mark_outside_air()
            
            to_remove = []
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == target:
                        for dx, dy in dirs:
                            nx, ny = i + dx, j + dy
                            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                                # 창고 밖과 맞닿음
                                to_remove.append((i,j))
                                break
                            elif grid[nx][ny] == '.' and visited[nx][ny]:
                                # 바깥 공기와 맞닿음
                                to_remove.append((i,j))
                                break
            # 제거
            for x,y in to_remove:
                grid[x][y] = '.'
    
    # 남은 컨테이너 수
    answer = sum(row.count('.') ^ len(row) for row in grid)  # 잘못된 표현 방지
    answer = sum(1 for i in range(n) for j in range(m) if grid[i][j] != '.')
    return answer
