def solution(n, costs):
    # 부모 배열 초기화 (Union-Find)
    parent = [i for i in range(n)]

    # find 연산 (경로 압축)
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    # union 연산
    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            parent[root_b] = root_a
            return True
        return False

    # 1. 비용 기준으로 정렬
    costs.sort(key=lambda x: x[2])

    answer = 0
    for a, b, cost in costs:
        # 2. 사이클이 없는 경우만 연결
        if union(a, b):
            answer += cost

    return answer
