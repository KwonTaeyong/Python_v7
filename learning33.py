def solution(n, tops):
    MOD = 10007
    dp = [0] * (n + 2)  # dp[0] ~ dp[n]
    dp[0] = 1

    for i in range(1, n + 1):
        dp[i] = (2 * dp[i - 1]) % MOD  # 정삼각형 1개 / 세로 마름모
        if tops[i - 1] == 1:
            dp[i] = (dp[i] + dp[i - 1]) % MOD  # 위쪽 삼각형 → 세로 마름모 추가 가능
        if i >= 2:
            dp[i] = (dp[i] + dp[i - 2]) % MOD  # 가로 마름모

    return dp[n]
