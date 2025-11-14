import heapq

def calc_wait(req_list, m):
    # 요청 리스트 req_list를 멘토 m명이 처리할 때 총 대기시간 계산
    # 멘토들의 다음 가능한 시간을 나타내는 min-heap
    pq = [0] * m
    heapq.heapify(pq)
    
    wait = 0
    
    for start, duration in req_list:
        free_time = heapq.heappop(pq)
        if free_time <= start:
            # 바로 상담 가능
            new_free = start + duration
        else:
            # 기다려야 한다
            wait += free_time - start
            new_free = free_time + duration
        heapq.heappush(pq, new_free)
    
    return wait


def solution(k, n, reqs):
    # 1. 유형별 요청 분류
    type_reqs = [[] for _ in range(k + 1)]
    for a, b, c in reqs:
        type_reqs[c].append((a, b))
    
    # 2. 각 유형별로 멘토 i명을 배정했을 때의 대기시간을 미리 계산
    #   최대 멘토 수는 n이지만, 한 유형에 너무 많이 줄 필요는 없음
    #   해당 유형의 요청 수보다 많이 줄 필요도 없음.
    max_mentors = n
    
    wait_table = [dict() for _ in range(k + 1)]
    
    for t in range(1, k + 1):
        req_list = type_reqs[t]
        count_requests = len(req_list)
        for m in range(1, max_mentors + 1):
            if m > count_requests:
                # 멘토 수가 요청 수보다 많으면 대기는 0
                wait_table[t][m] = 0
            else:
                wait_table[t][m] = calc_wait(req_list, m)
    
    # 3. 멘토 배분 완전탐색
    # 먼저 각 유형 최소 1명 배정 → 남은 (n - k)명 분배
    answer = float('inf')
    mentors = [1] * (k + 1)  # type 1~k 사용
    
    def dfs(type_idx, left):
        nonlocal answer
        
        if type_idx > k:
            if left == 0:
                total_wait = 0
                for t in range(1, k + 1):
                    m = mentors[t]
                    total_wait += wait_table[t][m]
                answer = min(answer, total_wait)
            return
        
        # 현재 유형 type_idx에 추가로 배정할 수 있는 멘토는 left까지
        for extra in range(left + 1):
            mentors[type_idx] = 1 + extra
            dfs(type_idx + 1, left - extra)
    
    dfs(1, n - k)
    return answer
