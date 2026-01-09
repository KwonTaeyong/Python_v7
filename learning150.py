def solution(edges, target):
    from collections import defaultdict

    n = len(target)
    tree = defaultdict(list)

    for p, c in edges:
        tree[p - 1].append(c - 1)

    # 자식 노드 정렬
    for k in tree:
        tree[k].sort()

    # 각 노드가 현재 가리키는 자식 인덱스
    idx = {k: 0 for k in tree}

    # 리프 판별
    is_leaf = [True] * n
    for p, c in edges:
        is_leaf[p - 1] = False

    leaf_count = [0] * n
    leaf_order = []

    # Step 1: 공을 떨어뜨리며 리프 도달 순서 기록
    while True:
        if all(leaf_count[i] == target[i] for i in range(n) if is_leaf[i]):
            break

        cur = 0
        path = []

        while not is_leaf[cur]:
            path.append(cur)
            nxt = tree[cur][idx[cur]]
            cur = nxt

        # 리프 도착
        leaf_count[cur] += 1
        if leaf_count[cur] > target[cur]:
            return [-1]

        leaf_order.append(cur)

        # 경로상의 노드들 방향 갱신
        for node in path:
            idx[node] = (idx[node] + 1) % len(tree[node])

    # Step 2: 숫자 배정
    result = []
    need = {i: target[i] for i in range(n) if is_leaf[i]}
    cnt = defaultdict(int)

    for leaf in leaf_order:
        cnt[leaf] += 1

    # 각 리프별 숫자 리스트 만들기
    assign = {}
    for leaf in cnt:
        k = cnt[leaf]
        s = need[leaf]
        if not (k <= s <= 3 * k):
            return [-1]

        nums = [1] * k
        s -= k
        i = 0
        while s > 0:
            add = min(2, s)
            nums[i] += add
            s -= add
            i += 1
        assign[leaf] = nums

    # 리프 방문 순서대로 숫자 출력
    pos = defaultdict(int)
    for leaf in leaf_order:
        result.append(assign[leaf][pos[leaf]])
        pos[leaf] += 1

    return result
