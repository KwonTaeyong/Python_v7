from math import ceil
from collections import defaultdict

def solution(edges, target):
    n = len(edges) + 1

    # 1) 트리 구성 (자식 오름차순)
    children = defaultdict(list)
    has_parent = [False] * (n + 1)
    for p, c in edges:
        children[p].append(c)
        has_parent[c] = True
    for u in range(1, n + 1):
        children[u].sort()

    # 리프 판정 및 내부 노드의 target 검증
    is_leaf = [False] * (n + 1)
    for u in range(1, n + 1):
        if len(children[u]) == 0:
            is_leaf[u] = True
        else:
            # 내부 노드는 target이 0이어야 함
            if target[u - 1] != 0:
                return [-1]

    # 2) 리프 방문 시퀀스 생성하면서 최소 필요 길이 N 탐색
    #    부모 포인터(현재 길)
    ptr = {u: 0 for u in children.keys()}  # 리프는 키로 없어도 무방

    visits = []                   # 방문 리프 시퀀스
    leaf_count = defaultdict(int) # 리프별 누적 방문 수
    need_min = {}                 # 리프별 하한 ceil(t/3)
    need_max = {}                 # 리프별 상한 t
    for u in range(1, n + 1):
        if is_leaf[u]:
            t = target[u - 1]
            need_min[u] = 0 if t == 0 else ceil(t / 3)
            need_max[u] = t

    # 드롭(리프 하나 얻고, 경로 포인터 회전)
    def drop_once():
        path = []
        u = 1
        while len(children[u]) > 0:
            path.append(u)
            idx = ptr[u]
            v = children[u][idx]
            u = v
        # 리프 u 도착 -> 경로의 포인터 회전
        for p in path:
            k = len(children[p])
            ptr[p] = (ptr[p] + 1) % k
        return u

    # 최소 N 찾기
    total_need_min = sum(need_min.values())

    # upper bound를 어느 정도 잡아두고 진행 (충분히 작음)
    # 최악 근사: (리프 수 L) * (max ceil(t/3))
    leaf_ids = [u for u in range(1, n + 1) if is_leaf[u]]
    if not leaf_ids:
        return [-1]  # 리프가 없는데 합은 1 이상 조건상 모순

    max_need_min = max(need_min[u] for u in leaf_ids) if leaf_ids else 0
    hard_cap = len(leaf_ids) * max_need_min + 10000  # 안전 마진

    satisfied_min = set()
    while True:
        # 모든 리프가 하한 충족했는지 확인
        if len(satisfied_min) == len(leaf_ids):
            break
        if len(visits) > hard_cap:
            return [-1]

        lf = drop_once()
        visits.append(lf)

        # 리프 누적 방문 업데이트와 즉시 불가능 판정
        leaf_count[lf] += 1
        if leaf_count[lf] > need_max[lf]:
            return [-1]  # t_i 를 초과 방문 -> 최소합(모두 1)도 넘음

        # 하한 충족 체크 (0도 포함: 0이면 방문 즉시 불가능 위에서 걸림)
        if leaf_count[lf] >= need_min[lf]:
            satisfied_min.add(lf)

        # target이 0인 리프는 절대 방문되면 안 됨
        if need_max[lf] == 0 and leaf_count[lf] > 0:
            return [-1]

    # 3) 사전순 최소 숫자 배치 (그리디)
    remain_sum = {u: target[u - 1] for u in leaf_ids}
    remain_vis = {u: leaf_count[u] for u in leaf_ids}

    answer = []
    for lf in visits:
        r = r
