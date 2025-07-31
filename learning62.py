<<<<<<< HEAD
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def solution(t):
    n = len(t) + 1
    graph = defaultdict(list)

    for u, v in t:
        graph[u].append(v)
        graph[v].append(u)

    max_size = 0

    def dfs(node, parent):
        nonlocal max_size
        size = 1
        high_degree_count = 0
        if len(graph[node]) >= 3:
            high_degree_count = 1

        for child in graph[node]:
            if child == parent:
                continue
            child_size, child_high = dfs(child, node)
            size += child_size
            high_degree_count += child_high

        if high_degree_count <= 1:
            max_size = max(max_size, size)
        return size, high_degree_count

    dfs(0, -1)
    return max_size
=======
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    # 음식 시간과 인덱스를 함께 저장하는 최소 힙 구성
    food_q = []
    for i, time in enumerate(food_times):
        heapq.heappush(food_q, (time, i + 1))  # (먹는 시간, 음식 번호)

    total_food = len(food_times)
    previous = 0  # 이전에 다 먹은 음식의 시간

    # 한 바퀴 돌며 제거할 수 있는 음식 그룹만큼 제거
    while True:
        if not food_q:
            return -1

        # 현재 가장 적은 음식 시간
        time, _ = food_q[0]
        # 이번 레벨에서 전체 음식 시간 차이만큼 소요 시간 계산
        spend = (time - previous) * total_food
        if k >= spend:
            k -= spend
            previous = time
            while food_q and food_q[0][0] == time:
                heapq.heappop(food_q)
                total_food -= 1
        else:
            break

    # 남은 음식 정렬 후 k번째 음식 반환
    result = sorted(food_q, key=lambda x: x[1])  # 음식 번호 기준 정렬
    return result[k % total_food][1]
>>>>>>> 06fe0e5 (코딩테스트 연습)
