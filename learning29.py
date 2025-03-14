def solution(alp, cop, problems):
    # 최대 가능한 알고력, 코딩력은 150
    max_alp = 150
    max_cop = 150
    
    # dp 배열을 무한으로 초기화, dp[알고력][코딩력] = 최소 시간
    dp = [[float('inf')] * (max_cop + 1) for _ in range(max_alp + 1)]
    
    # 초기 상태
    dp[alp][cop] = 0
    
    # 문제의 정보에 따라 dp를 갱신
    for i in range(max_alp + 1):
        for j in range(max_cop + 1):
            # 현재 알고력과 코딩력에서의 최소 시간
            current_time = dp[i][j]
            
            # 각 문제에 대해 풀 수 있는지 확인
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                # 이 문제를 풀 수 있으면
                if i >= alp_req and j >= cop_req:
                    new_alp = min(i + alp_rwd, max_alp)  # 알고력의 최대 값 150을 초과하지 않도록
                    new_cop = min(j + cop_rwd, max_cop)  # 코딩력의 최대 값 150을 초과하지 않도록
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], current_time + cost)
            
            # 알고력과 코딩력을 올리기 위해 공부하는 시간을 고려한 이동
            if i < max_alp:
                dp[i + 1][j] = min(dp[i + 1][j], current_time + 1)
            if j < max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], current_time + 1)
    
    # 모든 문제를 풀 수 있는 최소 시간을 구합니다.
    result = float('inf')
    for i in range(max_alp, max_alp + 1):
        for j in range(max_cop, max_cop + 1):
            result = min(result, dp[i][j])
    
    return result
