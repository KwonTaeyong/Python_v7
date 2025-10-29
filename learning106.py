from collections import deque
import math

def solution(n, z, roads, queries):
    # S = { z } U { z - w for each road weight w }
    weights = set()
    for u,v,w in roads:
        weights.add(w)
    S = set([z])
    for w in weights:
        S.add(z - w)   # all positive because w < z

    # MAXD bound: choose z*z (safe because z <= 50 -> 2500)
    MAXD = z * z

    INF = 10**9
    # min_terms[d] = minimal number of summands from S to make sum exactly d (<= MAXD)
    min_terms = [INF] * (MAXD + 1)
    min_terms[0] = 0
    # BFS-like (unweighted for number of items): we want minimal number of items to reach each sum
    q = deque([0])
    while q:
        cur = q.popleft()
        cur_k = min_terms[cur]
        for s in S:
            nxt = cur + s
            if nxt <= MAXD and min_terms[nxt] > cur_k + 1:
                min_terms[nxt] = cur_k + 1
                q.append(nxt)

    answer = []
    for c in queries:
        if c == 0:
            answer.append(0)
            continue

        # minimal possible turns due to z-per-turn bound
        T0 = (c + z - 1) // z  # ceil(c / z)
        found = -1
        # search a small window of T values starting from T0
        # We search up to T0 + z because D = z*T - c has residue fixed mod z and minimal representative
        # of that residue is <= z*z, so scanning z consecutive T suffices to find D <= MAXD when possible.
        for T in range(T0, T0 + z + 1):
            D = z * T - c
            if D < 0:
                continue
            if D > MAXD:
                # if D exceeds MAXD for this T, larger T will only increase D;
                # but we still continue since adding z to T increases D by z and might match a representable D
                pass
            # we need D representable with at most T summands
            if D <= MAXD and min_terms[D] <= T:
                found = T
                break
        answer.append(found)
    return answer
