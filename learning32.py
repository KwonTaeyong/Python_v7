from collections import deque

def solution(grid):
    N, M = len(grid), len(grid[0])
    visited = [[[False, False] for _ in range(M)] for _ in range(N)]
    
    # 삼각형 인접 정보
    def get_neighbors(i, j, d):
        neighbors = []
        val = grid[i][j]

        if val == 1:
            if d == 0:
                # / 방향, 삼각형 0 (↖)
                if j > 0:
                    neighbors.append((i, j-1, 1))  # 좌측 삼각형 1
                if i > 0:
                    neighbors.append((i-1, j, 1))  # 위쪽 삼각형 1
            else:
                # / 방향, 삼각형 1 (↘)
                if j < M - 1:
                    neighbors.append((i, j+1, 0))  # 우측 삼각형 0
                if i < N - 1:
                    neighbors.append((i+1, j, 0))  # 아래 삼각형 0
        else:
            if d == 0:
                # \ 방향, 삼각형 0 (↙)
                if j > 0:
                    neighbors.append((i, j-1, 1))  # 좌측 삼각형 1
                if i < N - 1:
                    neighbors.append((i+1, j, 1))  # 아래 삼각형 1
            else:
                # \ 방향, 삼각형 1 (↗)
                if j < M - 1:
                    neighbors.append((i, j+1, 0))  # 우측 삼각형 0
                if i > 0:
                    neighbors.append((i-1, j, 0))  # 위쪽 삼각형 0

        # 같은 칸의 다른 삼각형과는 항상 연결되어 있음
        neighbors.append((i, j, 1 - d))
        return neighbors
    
    def bfs(start_i, start_j, start_d):
        q = deque()
        q.append((start_i, start_j, start_d))
        visited[start_i][start_j][start_d] = True
        size = 1

        while q:
            i, j, d = q.popleft()
            for ni, nj, nd in get_neighbors(i, j, d):
                if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj][nd]:
                    visited[ni][nj][nd] = True
                    q.append((ni, nj, nd))
                    size += 1
        return size

    max_size = 0
    for i in range(N):
        for j in range(M):
            for d in range(2):
                if not visited[i][j][d]:
                    max_size = max(max_size, bfs(i, j, d))

    return max_size
