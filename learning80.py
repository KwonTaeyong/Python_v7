def solution(sequence):
    n = len(sequence)
    
    # 펄스 패턴 두 가지
    pulse1 = [1 if i % 2 == 0 else -1 for i in range(n)]
    pulse2 = [-1 if i % 2 == 0 else 1 for i in range(n)]
    
    # sequence 에 곱한 결과
    arr1 = [sequence[i] * pulse1[i] for i in range(n)]
    arr2 = [sequence[i] * pulse2[i] for i in range(n)]
    
    # 카데인 알고리즘으로 최대 부분합 찾기
    def kadane(arr):
        max_sum = arr[0]
        curr_sum = arr[0]
        for x in arr[1:]:
            curr_sum = max(x, curr_sum + x)
            max_sum = max(max_sum, curr_sum)
        return max_sum
    
    return max(kadane(arr1), kadane(arr2))
