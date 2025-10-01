from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])  # 행, 열 크기
    visited = [[False] * m for _ in range(n)]  # 방문 체크
    directions = [(1,0), (-1,0), (0,1), (0,-1)]  # 남,북,동,서 이동
    
    # BFS 큐 (행, 열, 거리)
    queue = deque([(0, 0, 1)])
    visited[0][0] = True
    
    while queue:
        x, y, dist = queue.popleft()
        
        # 목표 지점 도착 시
        if x == n-1 and y == m-1:
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 맵 범위 안, 벽이 아니고, 방문 안 한 곳
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
    
    return -1  # 도달 불가 시
