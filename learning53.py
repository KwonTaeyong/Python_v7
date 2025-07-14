def solution(n, costs):
    # 1. 부모 테이블 초기화
    parent = [i for i in range(n)]
    
    # 2. Find 함수
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # 경로 압축
        return parent[x]

    # 3. Union 함수
    def union(a, b):
        a_root = find(a)
        b_root = find(b)
        if a_root != b_root:
            parent[b_root] = a_root
            return True
        return False

    # 4. 비용 기준으로 정렬
    costs.sort(key=lambda x: x[2])

    # 5. MST 구성
    total_cost = 0
    for a, b, cost in costs:
        if union(a, b):
            total_cost += cost

    return total_cost
