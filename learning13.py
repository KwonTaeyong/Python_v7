from collections import deque

# 네 방향 탐색 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# DFS를 활용하여 접근 가능한 모든 컨테이너를 찾기
def bfs(storage, n, m, start, container_type):
    visited = [[False] * m for _ in range(n)]
    queue = deque([start])
    visited[start[0]][start[1]] = True
    accessible_containers = []

    while queue:
        x, y = queue.popleft()
        accessible_containers.append((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if storage[nx][ny] == container_type:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
    return accessible_containers

def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])
    
    # 창고의 상태를 2D 리스트로 초기화
    storage = [list(row) for row in storage]
    
    # 모든 요청을 처리
    for request in requests:
        container_type = request[0]
        if len(request) == 1:
            # 지게차 방식: 접근 가능한 컨테이너만 꺼낸다.
            accessible_containers = []
            for i in range(n):
                for j in range(m):
                    if storage[i][j] == container_type:
                        # 외부와 연결된 컨테이너 찾기
                        if i == 0 or i == n-1 or j == 0 or j == m-1:
                            accessible_containers += bfs(storage, n, m, (i, j), container_type)
            # 해당 접근 가능한 컨테이너들을 꺼내기
            for x, y in accessible_containers:
                storage[x][y] = '.'
        
        elif len(request) == 2:
            # 크레인 방식: 해당 종류의 모든 컨테이너를 꺼낸다.
            for i in range(n):
                for j in range(m):
                    if storage[i][j] == container_type:
                        storage[i][j] = '.'
    
    # 남은 컨테이너 수 계산
    remaining_containers = sum(row.count(container) for row in storage for container in row if container != '.')
    
    return remaining_containers
