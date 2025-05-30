import heapq

def dijkstra(start, graph, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    hq = [(0, start)]
    
    while hq:
        d, node = heapq.heappop(hq)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            if dist[neighbor] > dist[node] + weight:
                dist[neighbor] = dist[node] + weight
                heapq.heappush(hq, (dist[neighbor], neighbor))
    return dist

def solution(n, roads):
    from collections import defaultdict

    # 그래프와 역방향 그래프
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)

    for idx, (u, v, l, t) in enumerate(roads):
        cost = l + t
        graph[u].append((v, cost))
        graph[v].append((u, cost))
        reverse_graph[u].append((v, cost))  # for dist_to_end
        reverse_graph[v].append((u, cost))

    # 1번 지점에서 각 노드까지의 최단 거리
    dist_from_start = dijkstra(1, graph, n)

    # n번 지점에서 각 노드까지의 최단 거리 (역방향으로)
    dist_to_end = dijkstra(n, reverse_graph, n)

    min_dist = dist_from_start[n]
    result = []

    # 각 도로 검사
    for idx, (u, v, l, t) in enumerate(roads):
        cost = l + t

        # 경로 1: u → v
        path1 = dist_from_start[u] + cost + dist_to_end[v]
        # 경로 2: v → u
        path2 = dist_from_start[v] + cost + dist_to_end[u]
        # 교통량 감소 시: cost 대신 L만 쓰면 됨
        new_path1 = dist_from_start[u] + l + dist_to_end[v]
        new_path2 = dist_from_start[v] + l + dist_to_end[u]

        if path1 == min_dist or path2 == min_dist:
            result.append(idx + 1)
        elif new_path1 < min_dist or new_path2 < min_dist:
            result.append(idx + 1)

    return sorted(result) if result else [-1]
