import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0

    # 최대 힙 구성 (음수로 변환)
    works = [-w for w in works]
    heapq.heapify(works)

    for _ in range(n):
        max_work = heapq.heappop(works)
        if max_work == 0:
            break
        heapq.heappush(works, max_work + 1)  # -1 감소 → +1

    return sum(w**2 for w in works)
