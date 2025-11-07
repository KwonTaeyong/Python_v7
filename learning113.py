def solution(heights):
    heights.sort()
    n = len(heights)
    
    # 중간을 기준으로 좌우 분할
    left = heights[:(n+1)//2]     # 작은 절반
    right = heights[(n+1)//2:]    # 큰 절반
    
    # 결과 순서를 만들기 (지그재그 형태)
    arranged = []
    for i in range(len(right)):
        arranged.append(left[i])
        arranged.append(right[i])
    if len(left) > len(right):
        arranged.append(left[-1])
    
    # 인접한 차이의 최소값 계산
    min_diff = float('inf')
    for i in range(1, len(arranged)):
        min_diff = min(min_diff, abs(arranged[i] - arranged[i-1]))
    
    return min_diff
