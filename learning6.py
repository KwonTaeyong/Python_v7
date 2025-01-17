from collections import defaultdict, deque

def solution(edges):
    # Step 1: Create graph and in-degree count
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for a, b in edges:
        graph[a].append(b)
        in_degree[b] += 1
        if a not in in_degree:
            in_degree[a] = 0

    # Step 2: Find the generated node (node with in-degree = number of graphs)
    generated_node = None
    graph_count = 0

    for node, degree in in_degree.items():
        if degree == len(graph) - len(edges):
            generated_node = node
            break

    # Step 3: Traverse and classify each subgraph
    def classify_subgraph(start):
        visited = set()
        stack = [start]
        edges_count = 0
        nodes_count = 0