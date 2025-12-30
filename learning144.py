def solution(n, costs):
    # 부모 노드 찾기 (경로 압축)
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]

    # 두 집합 합치기
    def union(parent, a, b):
        a = find(parent, a)
        b = find(parent, b)
        if a != b:
            parent[b] = a
            return True
        return False

    # 1. 비용 기준으로 정렬
    costs.sort(key=lambda x: x[2])

    parent = [i for i in range(n)]
    answer = 0
    count = 0

    # 2. 하나씩 다리 선택
    for a, b, cost in costs:
        if union(parent, a, b):
            answer += cost
            count += 1
            # MST는 n-1개의 간선만 필요
            if count == n - 1:
                break

    return answer
