from math import ceil

def solution(edges, target):
    # 노드 수
    n = len(target)
    # 자식 리스트 생성 (1-indexed 노드)
    children = [[] for _ in range(n+1)]
    parent = [0]*(n+1)
    for u,v in edges:
        children[u].append(v)
        parent[v] = u
    # 자식들을 번호 오름차순으로 정렬 (문제 명세)
    for i in range(1, n+1):
        children[i].sort()
    # 리프 목록과 인덱스 매핑
    is_leaf = [False]*(n+1)
    leaf_ids = []
    for i in range(1, n+1):
        if len(children[i]) == 0:
            is_leaf[i] = True
            leaf_ids.append(i)
    # 최대 시뮬레이션 횟수: 합(target) (각 드랍 최소 1)
    maxDrops = sum(target)
    if maxDrops == 0:
        return [-1]  # 문제에서 합은 >=1 이라지만 안전 처리

    # 포인터 초기화: 각 노드가 자식 리스트의 인덱스 (0..deg-1)
    ptr = [0]*(n+1)

    # 방문 시퀀스(리프 노드 번호) 저장
    visit_seq = []
    # 리프별 현재 카운트
    count_by_leaf = {leaf:0 for leaf in leaf_ids}

    # helper: 현재 카운트가 목표 가능한지 검사
    def feasible_counts(counts):
        # 모든 리프에 대해 ceil(target/3) <= count <= target
        for leaf in leaf_ids:
            t = target[leaf-1]
            c = counts.get(leaf, 0)
            if c < ceil(t/3) or c > t:
                return False
        return True

    # 시뮬레이션
    for t in range(1, maxDrops+1):
        # 한 번 드랍: 루트에서 포인터 따라 이동
        node = 1
        path = []  # 포인터를 advance할 노드들 (루트 포함, 리프 제외)
        while children[node]:
            path.append(node)
            child_idx = ptr[node]
            node = children[node][child_idx]
        # node는 리프
        visit_seq.append(node)
        count_by_leaf[node] += 1
        # 경로의 각 노드 포인터 advance
        for p in path:
            if len(children[p]) > 1:
                ptr[p] = (ptr[p] + 1) % len(children[p])
            # 자식이 1이면 ptr 유지 (같은 0)
        # 이 시점에 가능한지 검사 (최소 t 인지 확인)
        if feasible_counts(count_by_leaf):
            N = t
            # 이제 사전순 최소 숫자열 구성
            # 남은 방문수와 남은 합 초기화
            rem_v = {}
            rem_s = {}
            for leaf in leaf_ids:
                rem_v[leaf] = count_by_leaf.get(leaf,0)
                rem_s[leaf] = target[leaf-1]
            result = []
            possible = True
            for pos in range(N):
                leaf = visit_seq[pos]
                rv = rem_v[leaf]
                rs = rem_s[leaf]
                # try choose smallest x in 1..3 that keeps feasible for remainder
                chosen = None
                for x in (1,2,3):
                    if x > rs: 
                        continue
                    if rv-1 == 0:
                        # 마지막 visit for this leaf: must match exactly
                        if rs - x == 0:
                            chosen = x
                            break
                        else:
                            continue
                    # remaining sum after choosing x must be between (rv-1)*1 and (rv-1)*3
                    low = (rv-1) * 1
                    high = (rv-1) * 3
                    if low <= rs - x <= high:
                        chosen = x
                        break
                if chosen is None:
                    possible = False
                    break
                # assign
                result.append(chosen)
                rem_v[leaf] -= 1
                rem_s[leaf] -= chosen
            if not possible:
                return [-1]
            # 최종 점검: 모든 rem_v=0 and rem_s=0
            for leaf in leaf_ids:
                if rem_v[leaf] != 0 or rem_s[leaf] != 0:
                    return [-1]
            return result
    # 끝까지 못 찾으면 불가능
    return [-1]
