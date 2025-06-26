import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    # 최소 힙 구성: (음식 시간, 인덱스)
    food_heap = []
    for i, time in enumerate(food_times):
        heapq.heappush(food_heap, (time, i + 1))  # 음식 번호는 1부터

    total_time = 0      # 지금까지 제거한 시간
    previous = 0        # 직전 최소 음식 시간
    length = len(food_times)

    # 전체 그룹 제거 (한 바퀴씩 도는 시간 단축)
    while food_heap:
        # 가장 작은 음식 시간에서 previous(이전에 제거한 시간)를 뺀 것이 현재 라운드에서 제거할 시간
        time_to_consume = (food_heap[0][0] - previous) * length
        if k >= time_to_consume:
            k -= time_to_consume
            previous, _ = heapq.heappop(food_heap)  # 현재 음식 제거
            length -= 1  # 음식 하나 줄어듦
        else:
            # 현재 그룹 내에서 못 없애는 경우: 남은 음식 정렬 후 k번째
            remaining = sorted(food_heap, key=lambda x: x[1])  # 번호순 정렬
            return remaining[k % length][1]

    return -1
