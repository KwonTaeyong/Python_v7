import heapq

def _cost_for_requests(reqs_of_type, m):
    """주어진 유형의 요청 목록(reqs_of_type: [(a,b),...])에 대해 멘토 m명일 때 총 대기시간을 계산."""
    if m <= 0:
        return float('inf')
    if not reqs_of_type:
        return 0
    heap = []  # busy mentors' free times (min-heap)
    total_wait = 0
    for arrival, duration in reqs_of_type:
        # release mentors finished by arrival
        while heap and heap[0] <= arrival:
            heapq.heappop(heap)
        busy = len(heap)
        free = m - busy
        if free > 0:
            # 바로 시작
            heapq.heappush(heap, arrival + duration)
        else:
            # 모두 바쁨 -> 가장 빨리 끝나는 멘토 기다림
            earliest = heapq.heappop(heap)
            total_wait += earliest - arrival
            # 그 멘토는 이제 earliest부터 duration 동안 일함
            heapq.heappush(heap, earliest + duration)
    return total_wait

def solution(k, n, reqs):
    # reqs: [[a,b,c], ...] sorted by a
    # 그룹화: 각 유형별 요청 리스트 (a, b)
    type_reqs = [[] for _ in range(k+1)]  # 1..k
    for a, b, c in reqs:
        type_reqs[c].append((a, b))
    # generate all compositions of n into k positive integers (each >=1)
    best = float('inf')
    distrib = [1]*k  # 초기값: 모두 1명씩 배정 (남은 = n-k)
    def dfs(idx, remaining):
        nonlocal best
        if idx == k:
            if remaining != 0:
                return
            # 계산
            total = 0
            for i in range(k):
                m = distrib[i]
                total += _cost_for_requests(type_reqs[i+1], m)
                # 가지치기: 이미 커지면 멈춤
                if total >= best:
                    break
            if total < best:
                best = total
            return
        # idx번째(0-based)에 최소 1 명 이미 할당되어 있다고 가정하고
        # remaining은 남은 멘토 수 to distribute for indices idx..k-1
        # we must ensure each remaining position gets at least 1
        # but we already placed 1 for each position initially in distrib; so remaining is (n - sum(distrib[0:idx]))
        # We'll assign extra x >= 0 to current position
        max_extra = remaining  # can give all remaining
        for extra in range(max_extra + 1):
            distrib[idx] = 1 + extra
            # remaining - extra will be distributed to next indices
            # but need to ensure that for remaining positions there is at least 1 each:
            # however we maintain with base 1 in distrib for each slot, so remaining counts are consistent.
            dfs(idx+1, remaining - extra)
        # restore not necessary
    # initial remaining = n - k because distrib initialized with 1 per type
    dfs(0, n - k)
    return best if best != float('inf') else 0
