from collections import deque

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False]*m for _ in range(n)]
    column_sum = [0]*m  # 각 열별로 얻을 수 있는 석유량
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                q = deque([(i, j)])
                visited[i][j] = True
                size = 0
                columns = set()
                
                while q:
                    x, y = q.popleft()
                    size += 1
                    columns.add(y)
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                
                # 이 덩어리의 크기를 포함된 모든 열에 더하기
                for c in columns:
                    column_sum[c] += size

    return max(column_sum)
