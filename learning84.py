def solution(n, count):
    MOD = 1_000_000_007
    if count > n or count < 1:
        return 0
    # dp[i][j] = i개의 높이(1..i)를 배치했을 때, 보이는 서로다른 높이 수가 j인 경우의 수
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    for i in range(2, n + 1):
        mul = (2 * i - 2) % MOD
        for j in range(1, i + 1):
            dp[i][j] = (dp[i-1][j-1] + mul * dp[i-1][j]) % MOD
    return dp[n][count]
