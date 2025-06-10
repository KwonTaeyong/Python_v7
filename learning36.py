def solution(scores):
    wanho = scores[0]
    scores.sort(key=lambda x: (-x[0], x[1]))  # 근무 태도는 내림차순, 동료 평가는 오름차순

    max_peer = 0
    filtered = []
    for a, b in scores:
        if b < max_peer:
            continue  # 이미 더 높은 동료 평가를 가진 사람이 존재
        max_peer = max(max_peer, b)
        filtered.append((a, b))

    # 완호가 인센티브 받을 수 없는지 체크
    if not any(a == wanho[0] and b == wanho[1] for a, b in filtered):
        return -1

    # 유효한 사람들의 점수 합 리스트
    sums = [a + b for a, b in filtered]
    wanho_sum = sum(wanho)

    # 동석차 고려 석차 계산
    rank = 1
    prev = -1
    count = 0
    for s in sorted(sums, reverse=True):
        if s != prev:
            rank += count
            count = 1
            prev = s
        else:
            count += 1

        if s == wanho_sum:
            return rank

    return -1  # fallback
