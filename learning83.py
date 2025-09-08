MOD = 10**9 + 7

def mat_mul(A, B):
    # multiply matrices A (r x m) and B (m x c)
    r = len(A); m = len(A[0]); c = len(B[0])
    C = [[0]*c for _ in range(r)]
    for i in range(r):
        Ai = A[i]
        Ci = C[i]
        for k in range(m):
            a = Ai[k]
            if a:
                Bk = B[k]
                ak = a
                for j in range(c):
                    Ci[j] = (Ci[j] + ak * Bk[j]) % MOD
    return C

def mat_pow(mat, exp):
    # square matrix power (mat is k x k)
    k = len(mat)
    # identity
    res = [[0]*k for _ in range(k)]
    for i in range(k): res[i][i] = 1
    base = mat
    while exp > 0:
        if exp & 1:
            res = mat_mul(res, base)
        base = mat_mul(base, base)
        exp >>= 1
    return res

def solution(n):
    # returns number of tilings for 3 x n modulo 1e9+7
    # base cases:
    base = [0, 1, 3, 10, 23, 62, 170]  # index by n (0 unused)
    if n <= 6:
        return base[n] % MOD

    # recurrence: a(n) = 1*a(n-1) + 2*a(n-2) + 6*a(n-3) + 1*a(n-4) + 0*a(n-5) -1*a(n-6)
    # coefficients for companion matrix (from top row): [1, 2, 6, 1, 0, MOD-1]
    coeffs = [1, 2, 6, 1, 0, (MOD-1)]

    # build 6x6 companion matrix M so that:
    # [a(n), a(n-1), ..., a(n-5)]^T = M * [a(n-1), a(n-2), ..., a(n-6)]^T
    k = 6
    M = [[0]*k for _ in range(k)]
    # first row = coeffs
    for j in range(k):
        M[0][j] = coeffs[j] % MOD
    # subdiagonal = identity to shift previous values
    for i in range(1,k):
        M[i][i-1] = 1

    # we want a(n). Let v6 = [a(6), a(5), ..., a(1)]^T (column)
    v6 = [[base[6-i]] for i in range(6)]  # careful: i from 0 => a6, a5, ..., a1

    # compute M^(n-6) * v6
    P = mat_pow(M, n-6)
    res_vec = mat_mul(P, v6)  # result is k x 1
    ans = res_vec[0][0] % MOD
    return ans
