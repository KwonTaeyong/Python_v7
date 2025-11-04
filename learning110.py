def solution(diffs, times, limit):
    n = len(diffs)
    # 검사 함수: level이면 전체 시간이 limit 이내인지
    def ok(level):
        total = 0
        for i in range(n):
            if diffs[i] <= level:
                total += times[i]
            else:
                e = diffs[i] - level
                # (e+1)*time_cur + e*time_prev
                total += (e + 1) * times[i]
                # 이전 퍼즐 시간이 필요 (i>=1은 보장: diffs[0]=1 이므로 level>=1이면 첫 퍼즐은 틀리지 않음)
                total += e * times[i - 1]
            if total > limit:  # 초과하면 더 이상 계산할 필요 없음
                return False
        return total <= limit

    lo = 1
    hi = max(diffs)  # level이 max(diffs) 이상이면 더 이상 시간 단축 없음
    ans = hi
    while lo <= hi:
        mid = (lo + hi) // 2
        if ok(mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return ans
