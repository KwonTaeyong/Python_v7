def solution(a):
    MOD = 10 ** 7 + 19
    from itertools import combinations
    from collections import defaultdict

    n = len(a)
    m = len(a[0])

    # 열마다 1의 개수
    col_sum = [sum(a[i][j] for i in range(n)) for j in range(m)]

    # 가능한 column 벡터: 길이 n짜리 0-1 벡터 중 1의 개수가 col_sum[j]인 것
    from itertools import combinations

    def generate_columns(n, ones):
        # 길이 n짜리 벡터에서 ones개의 1을 가진 모든 경우 (mod 2)
        result = []
        for indices in combinations(range(n), ones):
            col = [0] * n
            for idx in indices:
                col[idx] = 1
            result.append(col)
        return result

    # 전체 가능한 b를 구성할 수 있는 열들의 집합 (열 단위로 생성)
    all_columns = []
    for j in range(m):
        if col_sum[j] > n:
            return 0
        columns = generate_columns(n, col_sum[j])
        all_columns.append(columns)

    # 모든 열 조합에 대해 b 행렬을 구성
    # 이를 통해 XOR parity 조건을 만족하는 경우만 카운트
    from functools import reduce

    from collections import Counter

    dp = Counter()
    dp[tuple([0]*n)] = 1  # 초기 상태: 모든 행 0

    for j in range(m):
        next_dp = Counter()
        for col in all_columns[j]:
            for state in dp:
                new_state = tuple((state[i] ^ col[i]) for i in range(n))
                next_dp[new_state] = (next_dp[new_state] + dp[state]) % MOD
        dp = next_dp

    # 짝수 패리티: 모든 행의 합이 짝수 → 즉 XOR = 0
    return dp[tuple([0]*n)] % MOD
