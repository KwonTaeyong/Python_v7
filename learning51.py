from collections import defaultdict, Counter

def solution(s, query):
    n = len(s)
    parent = list(range(n + 1))  # 1-based index
    groups = {}  # group_id -> set of indices
    group_chars = {}  # group_id -> Counter of characters
    group_order = []  # maintain group creation order
    deleted = set()

    # Initialize each character as its own group
    for i in range(1, n + 1):
        groups[i] = {i}
        group_chars[i] = Counter(s[i - 1])
        group_order.append(i)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return
        # maintain older group
        if group_order.index(rx) < group_order.index(ry):
            old, new = rx, ry
        else:
            old, new = ry, rx

        for idx in groups[new]:
            parent[idx] = old
        groups[old] |= groups[new]
        group_chars[old] += group_chars[new]
        del groups[new]
        del group_chars[new]
        group_order.remove(new)
        deleted.add(new)

    result = []

    for q in query:
        parts = q.split()
        if parts[0] == '1':
            x, y = int(parts[1]), int(parts[2])
            if find(x) == find(y):
                result.append("YES")
            else:
                result.append("NO")

        elif parts[0] == '2':
            x, word = int(parts[1]), parts[2]
            rx = find(x)
            move_set = set(word)
            new_id = n + len(group_order) + 1  # ensure unique
            moved = set()
            new_counter = Counter()
            for idx in sorted(groups[rx]):
                if s[idx - 1] in move_set:
                    moved.add(idx)
                    new_counter[s[idx - 1]] += 1

            if not moved:
                continue

            for idx in moved:
                groups[rx].remove(idx)
                group_chars[rx][s[idx - 1]] -= 1
                if group_chars[rx][s[idx - 1]] == 0:
                    del group_chars[rx][s[idx - 1]]

            groups[new_id] = moved
            group_chars[new_id] = new_counter
            group_order.append(new_id)
            for idx in moved:
                parent[idx] = new_id

            if not groups[rx]:
                deleted.add(rx)
                del groups[rx]
                del group_chars[rx]
                group_order.remove(rx)

        elif parts[0] == '3':
            x, y, word = int(parts[1]), int(parts[2]), parts[3]
            move_set = set(word)
            moved = defaultdict(set)
            moved_counter = defaultdict(Counter)
            for i in range(x, y + 1):
                if s[i - 1] in move_set:
                    ri = find(i)
                    moved[ri].add(i)
                    moved_counter[ri][s[i - 1]] += 1

            if not moved:
                continue

            new_id = n + len(group_order) + 1
            groups[new_id] = set()
            group_chars[new_id] = Counter()
            group_order.append(new_id)

            for gid in moved:
                for idx in moved[gid]:
                    groups[gid].remove(idx)
                    group_chars[gid][s[idx - 1]] -= 1
                    if group_chars[gid][s[idx - 1]] == 0:
                        del group_chars[gid][s[idx - 1]]
                    parent[idx] = new_id
                    groups[new_id].add(idx)
                    group_chars[new_id][s[idx - 1]] += 1

                if not groups[gid]:
                    deleted.add(gid)
                    del groups[gid]
                    del group_chars[gid]
                    group_order.remove(gid)

        elif parts[0] == '4':
            x, y = int(parts[1]), int(parts[2])
            union(x, y)

        elif parts[0] == '5':
            for gid in group_order:
                if gid in deleted:
                    continue
                chars = group_chars[gid]
                entry = []
                for ch in sorted(chars):
                    entry.append(f"{ch} {chars[ch]}")
                result.append(' '.join(entry))

    return result
