def solution(grid):
    n = len(grid)
    m = len(grid[0])
    
    # 각 칸당 2개의 삼각형
    def tid(i, j, t):
        return (i * m + j) * 2 + t

    size = 2 * n * m
    parent = list(range(size))
    cnt = [1] * size

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
            cnt[ra] += cnt[rb]

    for i in range(n):
        for j in range(m):
            d = grid[i][j]

            if d == 1:  # /
                # triangle 0: up, left
                # triangle 1: down, right
                if i > 0:
                    union(tid(i, j, 0), tid(i - 1, j, 1))
                if j > 0:
                    union(tid(i, j, 0), tid(i, j - 1, 1))
                if i < n - 1:
                    union(tid(i, j, 1), tid(i + 1, j, 0))
                if j < m - 1:
                    union(tid(i, j, 1), tid(i, j + 1, 0))

            else:  # \
                # triangle 0: up, right
                # triangle 1: down, left
                if i > 0:
                    union(tid(i, j, 0), tid(i - 1, j, 1))
                if j < m - 1:
                    union(tid(i, j, 0), tid(i, j + 1, 1))
                if i < n - 1:
                    union(tid(i, j, 1), tid(i + 1, j, 0))
                if j > 0:
                    union(tid(i, j, 1), tid(i, j - 1, 0))

    answer = 0
    for i in range(size):
        if parent[i] == i:
            answer = max(answer, cnt[i])

    return answer
