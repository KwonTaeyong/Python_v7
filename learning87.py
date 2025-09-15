from collections import defaultdict, deque

def solution(edges, target):
    n = len(edges) + 1
    children = defaultdict(list)
    indeg = [0] * (n+1)
    for p,c in edges:
        children[p].append(c)
        indeg[c] += 1
    for v in children:
        children[v].sort()
    # 리프 판정
    leafs = [i for i in range(1, n+1) if i not in children]

    # step1: 리프 방문 시퀀스 구하기
    seq = []
    pointer = {v:0 for v in children}
    def drop():
        cur = 1
        while cur in children:
            idx = pointer[cur]
            nxt = children[cur][idx]
            pointer[cur] = (idx+1)%len(children[cur])
            cur = nxt
        return cur
    # 최대 필요한 횟수 = sum(target)
    for _ in range(sum(target)):
        seq.append(drop())

    # step2: 최소 N 찾기
    need = [0]*(n+1)
    for i in range(1,n+1):
        need[i] = target[i-1]
    cnt = [0]*(n+1)
    N = 0
    for i,v in enumerate(seq):
        cnt[v]+=1
        if cnt[v] >= need[v]:
            if all(cnt[x]>=need[x] for x in leafs):
                N = i+1
                break
    if N==0: return [-1]

    # step3: 배정
    res = []
    remain = need[:]
    left = [0]*(n+1)
    total = [0]*(n+1)
    for v in seq[:N]:
        total[v]+=1
    for v in leafs:
        if total[v]<need[v]: return [-1]

    for i in range(N):
        v = seq[i]
        left[v]+=1
        # 남은 방문 횟수
        remain_visit = total[v]-left[v]+1
        # 남은 합
        remain_sum = remain[v]
        # 최소 넣을 수 있는 값 = max(1, remain_sum - (remain_visit-1)*3)
        val = max(1, remain_sum - (remain_visit-1)*3)
        if val>3: return [-1]
        res.append(val)
        remain[v]-=val

    return res
