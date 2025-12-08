from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    # 가능한 모든 컬럼 조합을 담을 리스트
    combs = []
    for i in range(1, col + 1):
        combs.extend(combinations(range(col), i))

    candidate_keys = []

    for comb in combs:
        # 1) 유일성 검사
        temp = set()
        for r in relation:
            temp.add(tuple(r[c] for c in comb))

        if len(temp) != row:  # 유일하지 않으면 후보키 불가
            continue

        # 2) 최소성 검사: 이미 등록된 후보키가 현재 조합의 부분집합이면 탈락
        is_minimal = True
        for key in candidate_keys:
            if set(key).issubset(comb):
                is_minimal = False
                break

        if is_minimal:
            candidate_keys.append(comb)

    return len(candidate_keys)
