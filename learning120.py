.def solution(n):
    MOD = 1_000_000_007
    
    if n == 1:
        return 0
    if n == 2:
        return 3
    if n == 3:
        return 10  # f(3) = 10
    
    # dp 배열 준비
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[2] = 3
    dp[3] = 10   # 문제 예시 참고
    
    for i in range(4, n + 1):
        dp[i] = (4 * dp[i - 2] - dp[i - 4]) % MOD
    
    return dp[n]
