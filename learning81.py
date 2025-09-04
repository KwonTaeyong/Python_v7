from math import ceil
from collections import defaultdict

def solution(edges, target):
    n = len(edges) + 1
    children = [[] for _ in range(n+1)]
    for p, c in edges:
        children[p].append(c)
    for u in range(1, n+1):
        children[u].sort()

    # 리프 판별
    is_leaf = [False]*(n+1)
    for u in range(1, n+1):
        if not children[u]:
            is_leaf[u] = True

    # 내부 노드는 target 0이어야 함(문제 조건과 일치하지 않으면 불가능)
    for u in range(1, n+1):
        if not is_leaf[u] and target[u-1] != 0:
            return [-1]

    # 리프별 방문 하한/상한 계산
    a = [0]*(n+1)  # ceil(t/3)
    b = [0]*(n+1)  # t
    total_b = 0
    for u in range(1, n+1):
        if is_leaf[u]:
            t = target[u-1]
            a[u] = (t + 2)//3
            b[u] = t
            if a[u] > b[u]:
                return [-1]
            total_b += b[u]

    # 각 내부 노드의 현재 포인터(초기: 가장 작은 자식)
    ptr = [0]*(n+1)

    # 리프 방문 시퀀스 생성(로터 라우터 시뮬)
    counts = [0]*(n+1)  # 리프별 현재 방문 횟수
    seq = []                      # 방문된 리프 노드 번호 시퀀스
    positions = defaultdict(list) # 리프별로 방문된 전역 인덱스들

    def drop_once():
        path = []
        u = 1
        while children[u]:
            path.append(u)
            u = children[u][ptr[u]]
        # 경로의 각 내부 노드 포인터를 다음 자식으로 회전
        for v in path:
            if children[v]:
                ptr[v] = (ptr[v] + 1) % len(children[v])
        return u  # leaf

    finished_at = None
    for _ in range(total_b):  # 상한을 넘어서는 순간 불가능, 최대 total_b 번만 확인
        leaf = drop_once()
        if not is_leaf[leaf]:  # 안전장치
            return [-1]
        seq.append(leaf)
        counts[leaf] += 1
        positions[leaf].append(len(seq)-1)

        # 상한 초과 즉시 불가능
        if counts[leaf] > b[leaf]:
            return [-1]

        # 모든 리프에 대해 하한/상한 만족하면 가장 이른 시점 -> 최소 드롭 수
        if all((not is_leaf[u]) or (a[u] <= counts[u] <= b[u]) for u in range(1, n+1)):
            finished_at = len(seq)
            break

    if finished_at is None:
        return [-1]

    N = finished_at

    # 방문 시퀀스 앞 N개에 대해, 리프별로 합을 맞추도록 사전순 최소 배정(그리디)
    answer = [0]*N
    for u in range(1, n+1):
        if is_leaf[u]:
            k = counts[u]
            S = target[u-1]
            poslist = positions[u]
            # k번 방문으로 합 S를 만들되, 각 스텝에서 가능한 최소 숫자 선택
            for j, p in enumerate(poslist):
                r = k - j - 1  # 남은 방문 수
                # 현재 선택 x 후 남은 합이 [r, 3r] 범위에 있어야 함
                chosen = None
                for x in (1, 2, 3):
                    rem = S - x
                    if r <= rem <= 3*r:
                        chosen = x
                        break
                if chosen is None:
                    return [-1]
                answer[p] = chosen
                S -= chosen
            if S != 0:
                return [-1]

    return answer
