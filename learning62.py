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
