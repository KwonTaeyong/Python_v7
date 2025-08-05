import sys
sys.setrecursionlimit(100000)

def solution(k, num, links):
    n = len(num)
    tree = [[] for _ in range(n)]
    parent = [-1] * n

    # 트리 구성 및 루트 찾기
    for i, (l, r) in enumerate(links):
        if l != -1:
            tree[i].append(l)
            parent[l] = i
        if r != -1:
            tree[i].append(r)
            parent[r] = i

    root = parent.index(-1)

    # 체크 함수: 최대 그룹 인원을 mid로 가정했을 때 그룹 나누기 가능한지 판단
    def check(mid):
        group_count = 0

        def dfs(u):
            nonlocal group_count
            total = num[u]
            children = []
            for v in tree[u]:
                children.append(dfs(v))

            # 자식들을 더한 뒤 그룹 분리 조건
            for child_sum in children:
                if total + child_sum <= mid:
                    total += child_sum
                else:
                    group_count += 1  # 그룹 나누기
            return total

        total_sum = dfs(root)
        return (group_count + 1) <= k  # 루트 포함

    # 이분 탐색: 최소 최대 그룹 인원 찾기
    left, right = max(num), sum(num)
    answer = right

    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
