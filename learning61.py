import sys
sys.setrecursionlimit(10**6)

def solution(sales, links):
    from collections import defaultdict

    n = len(sales)
    tree = defaultdict(list)

    for a, b in links:
        tree[a - 1].append(b - 1)  # 0-indexed로 변환

    dp = [[0, 0] for _ in range(n)]  # [불참, 참석]

    def dfs(node):
        # 참석하는 경우: 본인 매출액
        dp[node][1] = sales[node]

        if not tree[node]:  # 자식 없음 (리프)
            dp[node][0] = 0
            return

        extra = float('inf')  # 최소 한 명은 참석시켜야 하므로 추가 비용 추적
        total0 = 0  # 모든 자식의 불참 상태 비용 누적

        for child in tree[node]:
            dfs(child)
            # 자식이 참석하든 불참하든 최소 비용
            total0 += min(dp[child][0], dp[child][1])
            # 자식이 반드시 참석해야 하는 추가 비용 계산
            extra = min(extra, dp[child][1] - min(dp[child][0], dp[child][1]))

        dp[node][0] = total0 + (extra if extra > 0 else 0)
        dp[node][1] += total0  # node 참석할 경우 자식은 자유롭게 선택 가능

    dfs(0)  # CEO는 항상 1번, index 0

    return min(dp[0][0], dp[0][1])
