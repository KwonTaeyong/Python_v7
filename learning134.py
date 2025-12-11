import heapq

def solution(jobs):
    n = len(jobs)
    # 작업 번호 추가해 [요청시각, 소요시간, 작업번호] 형태로 만든다.
    jobs = sorted([[s, l, i] for i, (s, l) in enumerate(jobs)], key=lambda x: x[0])

    hq = []  # 우선순위 큐: (소요시간, 요청시각, 작업번호)
    t = 0    # 현재 시간
    idx = 0  # 아직 큐에 넣지 않은 작업 index
    total_turnaround = 0

    while idx < n or hq:
        # 현재 시간 t 이하에 도착한 작업을 모두 큐에 넣기
        while idx < n and jobs[idx][0] <= t:
            s, l, i = jobs[idx]
            heapq.heappush(hq, (l, s, i))  # 우선순위: l -> s -> i
            idx += 1

        if hq:
            # 우선순위 가장 높은 작업 꺼내기
            l, s, i = heapq.heappop(hq)
            t += l  # 작업 수행
            total_turnaround += (t - s)
        else:
            # 큐가 비면 다음 작업 시작 시간으로 점프
            t = jobs[idx][0]

    return total_turnaround // n
