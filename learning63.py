import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    visited = dict()
    idx = 0

    for op in operations:
        if op[0] == 'I':
            num = int(op[2:])
            heapq.heappush(min_heap, (num, idx))
            heapq.heappush(max_heap, (-num, idx))
            visited[idx] = True
            idx += 1

        elif op == "D 1":  # 최댓값 삭제
            while max_heap:
                value, i = heapq.heappop(max_heap)
                if visited.get(i, False):
                    visited[i] = False
                    break

        elif op == "D -1":  # 최솟값 삭제
            while min_heap:
                value, i = heapq.heappop(min_heap)
                if visited.get(i, False):
                    visited[i] = False
                    break

    # 최종 유효한 값들 중 최대, 최소 찾기
    max_val, min_val = None, None

    while max_heap:
        value, i = heapq.heappop(max_heap)
        if visited.get(i, False):
            max_val = -value
            break

    while min_heap:
        value, i = heapq.heappop(min_heap)
        if visited.get(i, False):
            min_val = value
            break

    if max_val is None or min_val is None:
        return [0, 0]
    else:
        return [max_val, min_val]
