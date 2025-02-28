def solution(sequence, k):
    # 슬라이딩 윈도우 초기화
    left = 0
    current_sum = 0
    answer = []
    
    # 슬라이딩 윈도우 기법
    for right in range(len(sequence)):
        # 오른쪽 포인터가 가리키는 값을 current_sum에 더함
        current_sum += sequence[right]
        
        # current_sum이 k보다 크면 왼쪽 포인터를 이동시켜 합을 줄임
        while current_sum > k and left <= right:
            current_sum -= sequence[left]
            left += 1
        
        # current_sum이 k와 같으면 부분 수열을 찾은 것
        if current_sum == k:
            # 부분 수열 길이 계산
            if not answer or (right - left) < (answer[1] - answer[0]):
                # 더 짧은 수열을 찾으면 갱신
                answer = [left, right]
    
    return answer
