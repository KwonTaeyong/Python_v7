from collections import deque

def solution(land, height):
    n = len(land)
    visited = [[-1]*n for _ in range(n)]
    group_id = 0
    group_map = {}
    
    # 상하좌우
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    
    # 1. 영역 그룹화 (높이 차가 height 이하인 경우만)
    def bfs(x, y, gid):
        queue = deque()
        queue.append((x, y))
        visited[x][y] = gid
        group_map[gid] = [(x, y)]
        while queue:
            cx, cy = queue.popleft()
            for dx, dy in dirs:
                nx, ny = cx+dx, cy+dy
                if 0<=nx<n and 0<=ny<n and visited[nx][ny] == -1:
                    if abs(land[cx][cy] - land[nx][ny]) <= height:
                        visited[nx][ny] = gid
                        group_map[gid].append((nx, ny))
                        queue.append((nx, ny))
    
    # 그룹 나누기
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                bfs(i, j, group_id)
                group_id += 1

    # 2. 그룹 간 사다리 비용 수집
    edges = []
    edge_set = set()  # 중복 제거용

    for gid in range(group_id):
        for x, y in group_map[gid]:
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<n:
                    ngid = visited[nx][ny]
                    if ngid != gid:
                        cost = abs(land[x][y] - land[nx][ny])
                        key = tuple(sorted((gid, ngid)))
                        if key not in edge_set:
                            edge_set.add(key)
                            edges.append((cost, gid, ngid))
    
    # 3. MST (크루스칼 알고리즘)
    edges.sort()  # 비용 기준 정렬
    
    parent = list(range(group_id))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[rb] = ra
        return True

    answer = 0
    for cost, a, b in edges:
        if union(a, b):
            answer += cost

    return answer
