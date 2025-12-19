import heapq

def solution(jobs):
    n = len(jobs)
    
    # 작업에 작업번호를 붙임
    jobs = [(jobs[i][0], jobs[i][1], i) for i in range(n)]
    # 요청 시각 기준 정렬
    jobs.sort()
    
    heap = []
    time = 0
    idx = 0
    total_turnaround = 0
    
    while idx < n or heap:
        # 현재 시점까지 들어온 작업을 모두 힙에 추가
        while idx < n and jobs[idx][0] <= time:
            s, l, i = jobs[idx]
            heapq.heappush(heap, (l, s, i))
            idx += 1
        
        if heap:
            # 우선순위가 가장 높은 작업 수행
            l, s, i = heapq.heappop(heap)
            time += l
            total_turnaround += time - s
        else:
            # 처리할 작업이 없으면 다음 작업 시점으로 점프
            time = jobs[idx][0]
    
    return total_turnaround // n
