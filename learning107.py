import sys
sys.setrecursionlimit(300000)

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
    def add(self, i, delta):
        # i: 0-based index
        i += 1
        n = self.n
        bit = self.bit
        while i <= n:
            bit[i] += delta
            i += i & -i
    def sum_prefix(self, i):
        # sum of [0..i] (0-based). if i < 0 -> 0
        if i < 0:
            return 0
        i += 1
        s = 0
        bit = self.bit
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s
    def range_sum(self, l, r):
        # sum [l..r], 0-based
        if r < l:
            return 0
        return self.sum_prefix(r) - self.sum_prefix(l - 1)

def solution(values, edges, queries):
    n = len(values)
    # build adjacency
    g = [[] for _ in range(n)]
    for u,v in edges:
        u -= 1; v -= 1
        g[u].append(v)
        g[v].append(u)

    parent = [-1]*n
    depth = [0]*n
    order = []
    tin = [0]*n
    tout = [0]*n
    # root is node 0 (1번)
    def dfs(u, p):
        parent[u] = p
        tin[u] = len(order)
        order.append(u)
        for v in g[u]:
            if v == p: continue
            depth[v] = depth[u] + 1
            dfs(v, u)
        tout[u] = len(order)
    dfs(0, -1)

    # map initial values into euler-order array
    euler_vals = [0]*n
    for idx, node in enumerate(order):
        euler_vals[idx] = values[node]

    # Fenwick on euler order to answer subtree sums
    bit = Fenwick(n)
    for i, val in enumerate(euler_vals):
        bit.add(i, val)

    # maintain current value per node for updates (node-indexed)
    cur = values[:]  # current node values (0-based nodes)

    answer = []
    for q in queries:
        u = q[0]
        w = q[1]
        u -= 1
        if w == -1:
            # type1: subtree sum of u
            l = tin[u]
            r = tout[u] - 1
            s = bit.range_sum(l, r)
            answer.append(s)
        else:
            # type2: perform rotation along path root(0) -> u
            # gather path from root to u
            path = []
            node = u
            while node != -1:
                path.append(node)
                node = parent[node]
            path.reverse()  # now path[0] = root (0), ..., path[-1] = u

            # store old values along path
            old_vals = [cur[node] for node in path]
            # new values: root gets w, path[i] (i>=1) gets old_vals[i-1]
            new_vals = [None] * len(path)
            new_vals[0] = w
            for i in range(1, len(path)):
                new_vals[i] = old_vals[i-1]

            # apply updates: for each node in path, update cur and BIT by delta
            for node, nv, ov in zip(path, new_vals, old_vals):
                if nv != ov:
                    delta = nv - ov
                    cur[node] = nv
                    # update BIT at position tin[node]
                    bit.add(tin[node], delta)
            # done
    return answer
