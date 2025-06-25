from collections import deque

def bfs(start_r, start_c, grid, n, m):
    visited = [[set() for _ in range(m)] for _ in range(n)]
    queue = deque()
    queue.append((start_r, start_c, 1, frozenset([(start_r, start_c)])))
    visited[start_r][start_c].add(1)
    
    results = set()
    results.add((start_r, start_c, 1))
    
    while queue:
        r, c, size, visited_path = queue.popleft()
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                if grid[nr][nc] == '#':
                    continue
                new_size = size
                new_path = set(visited_path)
                if (nr, nc) not in new_path:
                    if grid[nr][nc] == '.':
                        new_size += 1
                    new_path.add((nr, nc))
                    if new_size not in visited[nr][nc]:
                        visited[nr][nc].add(new_size)
                        queue.append((nr, nc, new_size, frozenset(new_path)))
                        results.add((nr, nc, new_size))
    return results

def solution(grid):
    n, m = len(grid), len(grid[0])
    snowballs = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'o':
                snowballs.append((i, j))
    
    sb1_states = bfs(*snowballs[0], grid, n, m)
    sb2_states = bfs(*snowballs[1], grid, n, m)
    
    snowman_set = set()
    for r1, c1, s1 in sb1_states:
        for r2, c2, s2 in sb2_states:
            if (r1, c1) == (r2, c2):
                continue
            # 머리가 더 작거나 같을 때만 눈사람 가능
            if s1 <= s2:
                snowman_set.add((s2, s1))
            elif s2 <= s1:
                snowman_set.add((s1, s2))
    
    return len(snowman_set)
