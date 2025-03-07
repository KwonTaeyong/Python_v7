def solution(numbers):
    answer = [-1] * len(numbers)  # 뒷 큰수를 저장할 배열, 기본값은 -1
    stack = []  # 스택 초기화
    
    # 배열을 오른쪽에서 왼쪽으로 탐색
    for i in range(len(numbers) - 1, -1, -1):
        # 스택에서 현재 값보다 작은 값들은 모두 제거
        while stack and stack[-1] <= numbers[i]:
            stack.pop()
        
        # 스택에 값이 남아 있으면, 그 값이 뒷 큰 수
        if stack:
            answer[i] = stack[-1]
        
        # 현재 값을 스택에 추가
        stack.append(numbers[i])
    
    return answer