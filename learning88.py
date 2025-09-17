def solution(heights):
    n = len(heights)
    heights.sort()

    for i in range(1, n):
        if heights[i] == heights

def solution(heights):
    n = len(heights)
    heights.sort()

    # 중복이 있으면 무조건 0
    for i in range(1, n):
        if heights[i] == heights[i-1]:
            return 0

    def can(d):
        # 홀/짝 번갈아 배치: 중앙값 기준으로 나눔
        arr = []
        left = heights[:n//2]
        right = heights[n//2:]
        # 큰쪽/작은쪽 번갈아 배치
        for i in range(n//2):
            arr.append(left[i])
            arr.append(right[i])
        if n % 2 == 1:
            arr.append(right[-1])

        # 인접 차이 확인
        for i in range(1, n):
            if abs(arr[i] - arr[i-1]) < d:
                return False
        return True

    lo, hi = 0, heights[-1] - heights[0]
    ans = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if can(mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return ans
