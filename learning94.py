import sys
sys.setrecursionlimit(10**7)

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(n+1)
    def add(self, i, delta):
        # 1-based index
        n = self.n
        while i <= n:
            self.bit[i] += delta
            i += i & -i
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s
    def range_sum(self, l, r):
        if r < l:
            return 0
        return self.sum(r) - self.sum(l-1)

def solution(values, edges, queries):
    n = len(values)
    # adjacency
    g = [[] for _ in range(n+1)]
    for a,b in edges:
        g[a].append(b)
        g[b].append(a)

    # parent, build using stack BFS/DFS from root=1
    parent = [0]*(n+1)
    order = [1]
    parent[1] = 0
    for u in order:
        for v in g[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            order.append(v)

    # Euler tour (tin,tout) iterative dfs using stack to compute subtree ranges
    tin = [0]*(n+1)
    tout = [0]*(n+1)
    t = 0
    stack = [(1, 0, False)]  # (node, parent, visited_children?)
    while stack:
        node, par, visited = stack.pop()
        if not visited:
            t += 1
            tin[node] = t
            stack.append((node, par, True))
            for v in g[node]:
                if v == par: continue
                stack.append((v, node, False))
        else:
            tout[node] = t

    # current values (1-indexed nodes)
    curVal = [0]*(n+1)
    for i in range(1, n+1):
        curVal[i] = values[i-1]

    # Fenwick initialized with euler positions
    fw = Fenwick(n)
    for node in range(1, n+1):
        fw.add(tin[node], curVal[node])

    answer = []
    for q in queries:
        u, w = q[0], q[1]
        if w == -1:
            # type 1 query: subtree sum of u
            s = fw.range_sum(tin[u], tout[u])
            answer.append(s)
        else:
            # type 2 query: rotate along path root->u, root becomes w
            # build path nodes from u up to root, then reverse to get root->u
            path = []
            cur = u
            while cur != 0:
                path.append(cur)
                cur = parent[cur]
            path.reverse()  # now root..u

            prev = w
            for node in path:
                old = curVal[node]
                new = prev
                if new != old:
                    delta = new - old
                    fw.add(tin[node], delta)
                    curVal[node] = new
                prev = old
            # end of type2
    return answer
