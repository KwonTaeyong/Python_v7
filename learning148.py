def solution(heights):
    heights.sort()
    answer = 0
    
    for i in range(2, len(heights)):
        answer = max(answer, heights[i] - heights[i-2])
    
    return answer
