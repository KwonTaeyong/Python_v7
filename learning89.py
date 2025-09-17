import bisect

def solution(land, P, Q):
    arr = []
    for row in land:
        arr.extend(row)
    arr.sort()
    n = len(arr)

    # prefix sum
    prefix = [0] * (n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] + arr[i]

    def cost(h):
        # arr에서 h 이하인 원소 개수 = idx
        idx = bisect.bisect_left(arr, h)
        
        # h보다 작은 쪽 → 블록 추가
        left_count = idx
        left_sum = prefix[idx]
        add_blocks = h * left_count - left_sum
        
        # h 이상인 쪽 → 블록 제거
        right_count = n - idx
        right_sum = prefix[n] - left_sum
        remove_blocks = right_sum - h * right_count
        
        return add_blocks * P + remove_blocks * Q

    # 후보 높이는 arr 안의 값들만 보면 충분
    answer = float("inf")
    for h in set(arr):   # 중복 제거
        answer = min(answer, cost(h))
    
    return answer
