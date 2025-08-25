def solution(visible, hidden, k):
    n, m = len(visible), len(visible[0])
    answer = -10**9

    from functools import lru_cache

    # 경로 최대합 구하기 (down/right 경로 제한 아님, 모든 상하좌우 가능, 단 재방문 X)
    # 사실 n,m 작지 않아서 완전 탐색 불가 -> 여기서는 단순 dp (down/right만 허용) 버전 예시
    def max_path_sum(grid):
        dp = [[-10**9]*m for _ in range(n)]
        dp[0][0] = grid[0][0]
        for i in range(n):
            for j in range(m):
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j] + grid[i][j])
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j-1] + grid[i][j])
        return dp[-1][-1]

    # 행 뒤집기 부분탐색
    for mask in range(1<<n):
        grid = [[0]*m for _ in range(n)]
        flip_count = 0
        for i in range(n):
            row_flip = (mask>>i)&1
            if row_flip:
                flip_count += 1
            for j in range(m):
                if row_flip:
                    grid[i][j] = hidden[i][j]
                else:
                    grid[i][j] = visible[i][j]
        # DP로 경로 합
        best = max_path_sum(grid)
        total = best - flip_count*k
        answer = max(answer, total)

    return answer
