import heapq

def solution(n, works):
    # 작업량을 최대 힙으로 처리하기 위해 음수로 바꿔서 heap에 넣는다
    works = [-w for w in works]
    heapq.heapify(works)
    
    # n시간 동안 작업량을 줄여나간다
    for _ in range(n):
        # 가장 큰 작업량을 꺼내고, 1을 빼서 다시 넣는다
        largest_work = -heapq.heappop(works)
        if largest_work > 0:
            heapq.heappush(works, -(largest_work - 1))
    
    # 남은 작업량들의 제곱 합을 구한다
    result = sum(work ** 2 for work in works)
    return result