MOD = 1_000_000_007

def solution(n, count):
    # dp[i][j] = i까지 사용할 때 보이는 j개인 경우의 수
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    dp[1][1] = 1
    
    for i in range(2, n+1):
        for j in range(1, i+1):
            # 1) 가장 큰 i가 가장 왼쪽 → 보이는 수 증가
            dp[i][j] = dp[i-1][j-1]
            # 2) 기존 구조에 끼워넣기 → 보이는 수 그대로
            dp[i][j] += (2*i - 2) * dp[i-1][j]
            dp[i][j] %= MOD
    
    return dp[n][count] % MOD
