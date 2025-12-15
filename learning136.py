import sys
sys.setrecursionlimit(10**7)

def solution(sales, links):
    n = len(sales)
    sales = [0] + sales  # 1-indexed
    
    # 트리 구성
    tree = [[] for _ in range(n + 1)]
    for a, b in links:
        tree[a].append(b)
    
    dp = [[0, 0] for _ in range(n + 1)]
    
    def dfs(u):
        # 참석하는 경우
        dp[u][1] = sales[u]
        
        # 참석하지 않는 경우
        dp[u][0] = 0
        extra_cost = float('inf')
        must_select = False
        
        for v in tree[u]:
            dfs(v)
            
            # u가 참석하는 경우
            dp[u][1] += min(dp[v][0], dp[v][1])
            
            # u가 참석하지 않는 경우
            dp[u][0] += dp[v][0]
            
            if dp[v][1] <= dp[v][0]:
                must_select = True
            else:
                extra_cost = min(extra_cost, dp[v][1] - dp[v][0])
        
        # 자식 중 아무도 참석하지 않으면 한 명 강제 선택
        if not must_select and tree[u]:
            dp[u][0] += extra_cost
    
    dfs(1)
    return min(dp[1][0], dp[1][1])
