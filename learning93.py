from collections import defaultdict, Counter

def solution(s, query):
    n = len(s)
    parent = list(range(n+1))        # union-find parent
    comp = {}                        # root -> Counter(알파벳 빈도)
    alive = set()                    # 존재하는 root 순서
    result = []

    # 초기화: 각 문자 하나씩 root로
    for i, ch in enumerate(s, 1):
        comp[i] = Counter({ch: 1})
        alive.add(i)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry: return rx
        # 먼저 생성된 root가 남음 (문제 조건)
        if rx < ry:   # rx가 먼저 생성
            parent[ry] = rx
            comp[rx] += comp[ry]
            del comp[ry]
            alive.discard(ry)
            return rx
        else:
            parent[rx] = ry
            comp[ry] += comp[rx]
            del comp[rx]
            alive.discard(rx)
            return ry

    next_id = n+1   # 새 문자열 root id

    for q in query:
        parts = q.split()
        t = parts[0]

        if t == "1":   # 같은 문자열 확인
            x, y = map(int, parts[1:3])
            result.append("YES" if find(x) == find(y) else "NO")

        elif t == "2":  # 특정 문자 이동
            x, word = int(parts[1]), parts[2]
            r = find(x)
            new_root = next_id; next_id += 1
            comp[new_root] = Counter()
            alive.add(new_root)

            for ch in word:
                if comp[r][ch] > 0:
                    cnt = comp[r][ch]
                    comp[new_root][ch] += cnt
                    comp[r][ch] -= cnt
                    if comp[r][ch] == 0: del comp[r][ch]

            if not comp[r]:
                alive.discard(r)
                del comp[r]

        elif t == "3":  # 범위 x~y에서 이동
            x, y = int(parts[1]), int(parts[2])
            word = parts[3]
            new_root = next_id; next_id += 1
            comp[new_root] = Counter()
            alive.add(new_root)

            for i in range(x, y+1):
                r = find(i)
                for ch in word:
                    if comp[r].get(ch, 0) > 0:
                        cnt = comp[r][ch]
                        comp[new_root][ch] += cnt
                        comp[r][ch] -= cnt
                        if comp[r][ch] == 0: del comp[r][ch]
                if not comp[r]:
                    alive.discard(r)
                    del comp[r]

        elif t == "4":  # 합치기
            x, y = map(int, parts[1:3])
            union(x, y)

        elif t == "5":  # 최종 결과
            for r in sorted(alive):   # 생성 순서대로
                items = []
                for ch in sorted(comp[r].keys()):
                    items.append(f"{ch} {comp[r][ch]}")
                result.append(" ".join(items))

    return result
