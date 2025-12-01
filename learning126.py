def solution(e, starts):
    # 1. 약수 개수 계산 (sieve 방식)
    div_count = [0] * (e + 1)
    for i in range(1, e + 1):
        for j in range(i, e + 1, i):
            div_count[j] += 1

    # 2. 뒤에서부터 최댓값을 기록하는 best 배열
    best = [0] * (e + 1)
    best[e] = e
    max_div = div_count[e]

    for i in range(e - 1, 0, -1):
        if div_count[i] >= max_div:
            best[i] = i
            max_div = div_count[i]
        else:
            best[i] = best[i + 1]

    # 3. 쿼리 처리
    return [best[s] for s in starts]
