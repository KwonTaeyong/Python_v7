def solution(info, n, m):
    # DP 테이블을 큰 값으로 초기화
    max_trace = 121  # 최대 흔적 값은 120 이하이므로 121로 설정
    dp = [[float('inf')] * max_trace for _ in range(max_trace)]
    
    # 초기 상태: A와 B 도둑 모두 0개의 흔적을 남긴 상태
    dp[0][0] = 0
    
    # 물건을 하나씩 처리하면서 DP 갱신
    for a_trace, b_trace in info:
        # 현재 물건을 처리할 때, 이전 상태에서 물건을 하나씩 추가해서 갱신
        for a in range(max_trace-1, -1, -1):
            for b in range(max_trace-1, -1, -1):
                if dp[a][b] == float('inf'):
                    continue
                # A 도둑이 물건을 훔쳤을 경우
                if a + a_trace < max_trace:
                    dp[a + a_trace][b] = min(dp[a + a_trace][b], dp[a][b])
                # B 도둑이 물건을 훔쳤을 경우
                if b + b_trace < max_trace:
                    dp[a][b + b_trace] = min(dp[a][b + b_trace], dp[a][b])
    
    # 최종 결과: A 도둑의 흔적이 n 미만, B 도둑의 흔적이 m 미만인 경우 중 최소값을 찾음
    answer = float('inf')
    for a in range(n):
        for b in range(m):
            answer = min(answer, dp[a][b])
    
    return -1 if answer == float('inf') else answer
