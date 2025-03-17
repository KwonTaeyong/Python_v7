def solution(n, times):
    # 이진 탐색의 초기 범위 설정
    low, high = 1, min(times) * n  # 최소 시간 1, 최대 시간은 가장 느린 심사관이 n명을 다 처리하는 시간
    
    while low <= high:
        mid = (low + high) // 2
        # 주어진 시간(mid)에서 각 심사관이 심사할 수 있는 사람 수의 합 계산
        people = sum(mid // time for time in times)
        
        if people >= n:  # 만약 사람이 n명 이상 심사될 수 있으면 시간을 줄여본다
            high = mid - 1
        else:  # 사람이 부족하면 시간을 늘려본다
            low = mid + 1
    
    return low
