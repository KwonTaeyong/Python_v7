def solution(n, times):
    left = 1
    right = max(times) * n
    answer = right

    while left <= right:
        mid = (left + right) // 2

        # mid 시간 동안 처리 가능한 사람 수
        total = 0
        for t in times:
            total += mid // t
            






            
                break

        if total >= n:
            answer = mid
            right = mid - 1  # 더 작은 시간 탐색
        else:
            left = mid + 1   # 시간이 부족하므로 늘림

    return answer
