MOD = 1_000_000_007

def mat_mult(A, B):
    # A, B: n x n matrices (lists of lists), return (A @ B) % MOD
    n = len(A)
    # initialize result rows with zeros
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        Ci = C[i]
        for k in range(n):
            aik = Ai[k]
            if aik:
                Bk = B[k]
                # accumulate row
                mul = aik
                # localize for speed
                for j in range(n):
                    Ci[j] = (Ci[j] + mul * Bk[j]) % MOD
    return C

def mat_pow(mat, exp):
    n = len(mat)
    # identity
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        res[i][i] = 1
    base = mat
    while exp > 0:
        if exp & 1:
            res = mat_mult(res, base)
        base = mat_mult(base, base)
        exp >>= 1
    return res

def solution(grid, d, k):
    n = len(grid)
    m = len(grid[0])
    N = n * m
    p = len(d)
    # map (r,c) -> id
    def id_of(r, c): return r*m + c

    # build M_t matrices: N x N
    # M_t[u][v] = 1 if there's an edge u -> v when slope must equal d[t]
    M = []
    # neighbor offsets
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for t in range(p):
        Mt = [[0]*N for _ in range(N)]
        dt = d[t]
        for r in range(n):
            for c in range(m):
                u = id_of(r,c)
                hu = grid[r][c]
                row = Mt[u]
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < n and 0 <= nc < m:
                        v = id_of(nr, nc)
                        if grid[nr][nc] - hu == dt:
                            row[v] = 1
        M.append(Mt)

    # compute T = M0 * M1 * ... * M_{p-1}
    # multiply in order
    T = M[0]
    for t in range(1, p):
        T = mat_mult(T, M[t])

    # raise T to the k-th power
    Tk = mat_pow(T, k)

    # answer = sum of all entries of Tk (start at any position, end at any position)
    ans = 0
    for i in range(N):
        ans = (ans + sum(Tk[i])) % MOD
    return ans
