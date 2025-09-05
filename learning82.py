from collections import Counter, defaultdict

def solution(s, query):
    n = len(s)
    parent = list(range(n+1))
    members = {i: {i} for i in range(1, n+1)}
    count = {i: Counter([s[i-1]]) for i in range(1, n+1)}
    order = {i: i for i in range(1, n+1)}
    alive = set(range(1, n+1))
    result = []
    next_order = n+1

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        nonlocal next_order
        x, y = find(x), find(y)
        if x == y: return
        # 생성 순서 비교
        if order[x] > order[y]:
            x, y = y, x
        # y를 x에 합침
        for ch, c in count[y].items():
            count[x][ch] += c
        members[x] |= members[y]
        parent[y] = x
        alive.discard(y)
    
    def counter_to_string(c):
        parts = []
        for ch in sorted(c.keys()):
            if c[ch] > 0:
                parts.append(f"{ch} {c[ch]}")
        return " ".join(parts)

    for q in query:
        parts = q.split()
        if parts[0] == "1":
            x, y = int(parts[1]), int(parts[2])
            result.append("YES" if find(x) == find(y) else "NO")

        elif parts[0] == "2":
            x = int(parts[1])
            word = set(parts[2])
            root = find(x)
            move_ids = {i for i in members[root] if s[i-1] in word}
            if not move_ids: continue
            # 새 집합 생성
            new_root = min(move_ids)  # 대표 하나 선택
            parent[new_root] = new_root
            members[new_root] = move_ids
            count[new_root] = Counter(s[i-1] for i in move_ids)
            order[new_root] = next_order
            next_order += 1
            alive.add(new_root)
            # 기존 집합에서 제거
            members[root] -= move_ids
            for i in move_ids:
                parent[i] = new_root
                count[root][s[i-1]] -= 1
            # 비면 제거
            if not members[root]:
                alive.discard(root)

        elif parts[0] == "3":
            x, y = int(parts[1]), int(parts[2])
            word = set(parts[3])
            move_ids = {i for i in range(x, y+1) if find(i) in alive and s[i-1] in word}
            if not move_ids: continue
            new_root = min(move_ids)
            parent[new_root] = new_root
            members[new_root] = move_ids
            count[new_root] = Counter(s[i-1] for i in move_ids)
            order[new_root] = next_order
            next_order += 1
            alive.add(new_root)
            # 기존 집합에서 제거
            for i in move_ids:
                old = find(i)
                members[old].discard(i)
                count[old][s[i-1]] -= 1
                parent[i] = new_root
                if not members[old]:
                    alive.discard(old)

        elif parts[0] == "4":
            x, y = int(parts[1]), int(parts[2])
            union(x, y)

        elif parts[0] == "5":
            # 생성 순서대로 출력
            sorted_roots = sorted(alive, key=lambda r: order[r])
            for r in sorted_roots:
                result.append(counter_to_string(count[r]))

    return result
