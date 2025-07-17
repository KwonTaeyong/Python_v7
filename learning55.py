def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)  # 도착지점도 포함
    left = 1
    right = distance
    answer = 0

    while left <= right:
        mid = (left + right) // 2  # 최소 거리 후보
        prev = 0
        remove_count = 0

        for rock in rocks:
            if rock - prev < mid:
                remove_count += 1  # 너무 가까우면 이 바위 제거
            else:
                prev = rock  # 이 바위를 통과 기준으로 유지

        if remove_count > n:
            right = mid - 1  # 너무 많이 제거해야 함 -> 거리 줄이기
        else:
            answer = mid  # 거리 가능한 경우, 더 큰 거리도 시도
            left = mid + 1

    return answer
