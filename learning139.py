import heapq

def solution(N, road, K):
    # 그래프 생성 (인접 리스트)
    graph = [[] for _ in range(N + 1)]
    
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    # 최단 거리 테이블 초기화
    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[1] = 0
    
    # 다익스트라 (우선순위 큐)
    pq = []
    heapq.heappush(pq, (0, 1))  # (거리, 마을)
    
    while pq:
        current_dist, now = heapq.heappop(pq)
        
        # 이미 더 짧은 경로가 있으면 무시
        if current_dist > dist[now]:
            continue
        
        for next_node, cost in graph[now]:
            new_dist = current_dist + cost
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
    
    # K 시간 이하로 도달 가능한 마을 수 계산
    answer = 0
    for i in range(1, N + 1):
        if dist[i] <= K:
            answer += 1
    
    return answer
