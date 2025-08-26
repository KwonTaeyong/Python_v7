from collections import deque

def solution(grid):
    N, M = len(grid), len(grid[0])
    # 각 칸을 두 삼각형으로 나눠서 번호를 붙임
    # node_id = (i * M + j) * 2 + t   (t=0,1)
    total_nodes = N * M * 2
    adj = [[] for _ in range(total_nodes)]

    def node_id(i, j, t):
        return (i * M + j) * 2 + t

    # 인접 관계 설정
    for i in range(N):
        for j in range(M):
            d = grid[i][j]
            a, b = node_id(i, j, 0), node_id(i, j, 1)
            # 현재 칸의 두 삼각형이 어떤 방향인지 매핑
            if d == -1:  # '\'
                # a: 위-왼쪽 삼각형, b: 아래-오른쪽 삼각형
                if i > 0:  # 위쪽 칸과 연결
                    adj[a].append(node_id(i-1, j, 1))
                    adj[node_id(i-1, j, 1)].append(a)
                if j > 0:  # 왼쪽 칸과 연결
                    adj[a].append(node_id(i, j-1, 1))
                    adj[node_id(i, j-1, 1)].append(a)
                if i < N-1:
                    adj[b].append(node_id(i+1, j, 0))
                    adj[node_id(i+1, j, 0)].append(b)
                if j < M-1:
                    adj[b].append(node_id(i, j+1, 0))
                    adj[node_id(i, j+1, 0)].append(b)
            else:  # '/'
                # a: 위-오른쪽 삼각형, b: 아래-왼쪽 삼각형
                if i > 0:
                    adj[a].append(node_id(i-1, j, 0))
                    adj[node_id(i-1, j, 0)].append(a)
                if j < M-1:
                    adj[a].append(node_id(i, j+1, 1))
                    adj[node_id(i, j+1, 1)].append(a)
                if i < N-1:
                    adj[b].append(node_id(i+1, j, 1))
                    adj[node_id(i+1, j, 1)].append(b)
                if j > 0:
                    adj[b].append(node_id(i, j-1, 0))
                    adj[node_id(i, j-1, 0)].append(b)

    visited = [-1] * total_nodes
    answer = 0

    # BFS로 이분 그래프 색칠
    for start in range(total_nodes):
        if visited[start] == -1:
            q = deque([start])
            visited[start] = 0
            cnt = [1, 0]
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if visited[v] == -1:
                        visited[v] = 1 - visited[u]
                        cnt[visited[v]] += 1
                        q.append(v)
            answer = max(answer, max(cnt))

    return answer
