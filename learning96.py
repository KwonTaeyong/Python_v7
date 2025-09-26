from collections import deque

def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    grid = [list(row) for row in storage]  # 2D 배열로 변환
    
    # 방향 (상하좌우)
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    
    def remove_with_crane(ch):
        for i in range(n):
            for j in range(m):
                if grid[i][j] == ch:
                    grid[i][j] = '.'
    
    def remove_with_forklift(ch):
        # 외부와 연결된 빈칸 탐색
        visited = [[False]*m for _ in range(n)]
        q = deque()
        
        # 바깥과 닿아있는 빈 공간부터 탐색
        for i in range(n):
            for j in [0, m-1]:
                if grid[i][j] == '.':
                    visited[i][j] = True
                    q.append((i,j))
        for j in range(m):
            for i in [0, n-1]:
                if grid[i][j] == '.':
                    visited[i][j] = True
                    q.append((i,j))
        
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and grid[nx][ny] == '.':
                        visited[nx][ny] = True
                        q.append((nx,ny))
        
        # 이제 각 컨테이너가 접근 가능한지 확인
        to_remove = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == ch:
                    # 4방향 중 하나라도 외부와 연결된 빈칸 or 창고 경계면이면 접근 가능
                    for dx, dy in dirs:
                        nx, ny = i+dx, j+dy
                        if not (0 <= nx < n and 0 <= ny < m):
                            # 경계
                            to_remove.append((i,j))
                            break
                        if visited[nx][ny]:
                            # 외부와 연결
                            to_remove.append((i,j))
                            break
        # 제거
        for x, y in to_remove:
            grid[x][y] = '.'
    
    # 요청 처리
    for req in requests:
        if len(req) == 2:   # 크레인
            remove_with_crane(req[0])
        else:               # 지게차
            remove_with_forklift(req[0])
    
    # 남은 컨테이너 수 세기
    answer = sum(row.count(ch) for row in grid for ch in row if ch != '.')
    return answer
