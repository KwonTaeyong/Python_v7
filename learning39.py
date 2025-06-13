def solution(n, cores):
    if n <= len(cores):
        return n  # 처음 n개는 코어 순서대로 할당됨

    def count_jobs_done(time):
        # 주어진 시간까지 처리된 총 작업 수
        return sum((time // core) + 1 for core in cores)

    left = 0
    right = max(cores) * n
    time_point = 0

    while left <= right:
        mid = (left + right) // 2
        total = count_jobs_done(mid)
        if total >= n:
            time_point = mid
            right = mid - 1
        else:
            left = mid + 1

    # time_point 시점 이전까지 처리된 작업 수
    work_done_before = sum((time_point - 1) // core + 1 for core in cores)
    remaining = n - work_done_before

    for idx, core in enumerate(cores):
        if time_point % core == 0:
            remaining -= 1
            if remaining == 0:
                return idx + 1  # 코어 번호는 1부터 시작
