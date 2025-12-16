import math

def solution(n, stations, w):
    answer = 0
    cover = 2 * w + 1
    prev = 1  # 아직 커버되지 않은 첫 아파트

    for s in stations:
        left = s - w
        if prev < left:
            gap = left - prev
            answer += math.ceil(gap / cover)
        prev = s + w + 1

    # 마지막 기지국 이후 처리
    if prev <= n:
        gap = n - prev + 1
        answer += math.ceil(gap / cover)

    return answer
