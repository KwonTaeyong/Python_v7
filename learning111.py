def solution(n, tops):
    MOD = 10007
    # a[k]: k번째 아래 방향 정삼각형을 3번 방법으로 덮은 경우의 수
    # b[k]: k번째 아래 방향 정삼각형을 1,2,4번 방법으로 덮은 경우의 수
    a = [0]*n
    b = [0]*n

    a[0] = 1
    b[0] = 3 if tops[0] == 1 else 2

    for k in range(1, n):
        a_k = (a[k-1] + b[k-1]) % MOD
        if tops[k] == 1:
            b_k = (a[k-1]*2 + b[k-1]*3) % MOD
        else:
            b_k = (a[k-1] + b[k-1]*2) % MOD
        a[k] = a_k
        b[k] = b_k

    return (a[-1] + b[-1]) % MOD
