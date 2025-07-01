import math

def solution(n, stations, w):
    answer = 0
    coverage = 2 * w + 1  # 한 기지국이 커버하는 아파트 수
    start = 1  # 현재 탐색 시작 위치

    for station in stations:
        left = station - w  # 현재 기지국이 커버하는 시작
        if start < left:
            gap = left - start
            answer += math.ceil(gap / coverage)
        start = station + w + 1  # 다음 탐색 시작 위치

    # 마지막 기지국 이후에 남은 아파트 구간도 처리
    if start <= n:
        gap = n - start + 1
        answer += math.ceil(gap / coverage)

    return answer
