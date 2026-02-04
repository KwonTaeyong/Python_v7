def solution(grid):
    n = len(grid)
    m = len(grid[0])

    parent = {}
    size = {}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
            size[ra] += size[rb]

    # 각 칸의 두 삼각형을 노드로 만든다
    for i in range(n):
        for j in range(m):
            for t in (0, 1):
                idx = (i, j, t)
                parent[idx] = idx
                size[idx] = 1

    # 연결 처리
    for i in range(n):
        for j in range(m):
            diag = grid[i][j]

            # 오른쪽 칸
            if j + 1 < m:
                if diag == 1:  # /
                    union((i, j, 1), (i, j + 1, 0))
                else:          # \
                    union((i, j, 0), (i, j + 1, 1))

            # 아래 칸
            if i + 1 < n:
                if diag == 1:  # /
                    union((i, j, 0), (i + 1, j, 1))
                else:          # \
                    union((i, j, 1), (i + 1, j, 0))

    # 각 칸에서 하나만 선택하므로,
    # 두 삼각형 중 큰 쪽을 선택한 효과
    best = 0
    visited = set()

    for i in range(n):
        for j in range(m):
            a = find((i, j, 0))
            b = find((i, j, 1))
            if a not in visited:
                best = max(best, size[a])
                visited.add(a)
            if b not in visited:
                best = max(best, size[b])
                visited.add(b)

    return best
