import heapq

def solution(n, roads):
    MOD = 10**9 + 7  # 필요 없음, 그냥 안전용
    graph = [[] for _ in range(n + 1)]
    rev_graph = [[] for _ in range(n + 1)]
    
    # roads[i] = [U, V, L, T]
    for i, (u, v, L, T) in enumerate(roads, start=1):
        w = L + T
        graph[u].append((v, w, i))
        graph[v].append((u, w, i))
        rev_graph[v].append((u, w, i))
        rev_graph[u].append((v, w, i))
    
    def dijkstra(start, graph):
        INF = float('inf')
        dist = [INF] * (n + 1)
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w, _ in graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        return dist
    
    # 1 → n
    dist_from_start = dijkstra(1, graph)
    dist_from_end = dijkstra(n, graph)
    shortest = dist_from_start[n]
    
    result = []
    for i, (u, v, L, T) in enumerate(roads, start=1):
        w = L + T
        # 도로가 최단 경로에 포함되는지 검사
        if dist_from_start[u] + w + dist_from_end[v] == shortest or \
           dist_from_start[v] + w + dist_from_end[u] == shortest:
            result.append(i)
    
    return result if result else [-1]
