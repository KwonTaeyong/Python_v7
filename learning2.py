def solution(diffs, times, limit):
    def can_complete_with_level(level):
        total_time = 0
        prev_time = 0  # 이전 퍼즐의 소요 시간

        for i in range(len(diffs)):
            diff = diffs[i]
            time_cur = times[i]

            if diff <= level:
                total_time += time_cur
            else:
                num_mistakes = diff - level
                total_time += (time_cur + prev_time) * num_mistakes + time_cur

            prev_time = time_cur

            # 제한 시간 초과 시 중단
            if total_time > limit:
                return False

        return total_time <= limit

    # 이진 탐색으로 최소 숙련도 찾기
    left, right = 1, max(diffs)
    while left < right:
        mid = (left + right) // 2
        if can_complete_with_level(mid):
            right = mid  # 숙련도를 낮춰봄
        else:
            left = mid + 1  # 숙련도를 높여야 함

    return left
