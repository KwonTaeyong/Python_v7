import sys
sys.setrecursionlimit(300000)

def solution(sales, links):
    from collections import defaultdict

    n = len(sales)
    tree = defaultdict(list)
    for a, b in links:
        tree[a-1].append(b-1)

    dp = [[0, 0] for _ in range(n)]

    def dfs(node):
        # 참석하는 경우
        dp[node][1] = sales[node]
        # 불참하는 경우
        dp[node][0] = 0

        # 자식이 없으면 리프노드 → 끝
        if not tree[node]:
            return

        extra = float('inf')  # 꼭 한 명 이상 자식이 참석하도록 하기 위해 조정값

        for child in tree[node]:
            dfs(child)

            dp[node][1] += min(dp[child][0], dp[child][1])  # 내가 참석할 경우 자식 자유
            dp[node][0] += min(dp[child][0], dp[child][1])  # 일단 자식 자유로 넣고...

            # 자식이 참석하면 괜찮음, 불참하면 보정이 필요함
            extra = min(extra, dp[child][1] - min(dp[child][0], dp[child][1]))

        # 내가 불참했을 경우: 자식 중 최소한 1명은 반드시 참석해야 함
        dp[node][0] += extra

    dfs(0)  # CEO는 항상 0번 인덱스
    return min(dp[0][0], dp[0][1])
