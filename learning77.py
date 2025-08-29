def solution(sequence):
    n = len(sequence)
    
    # 펄스 수열 적용된 두 경우
    alt1 = [sequence[i] if i % 2 == 0 else -sequence[i] for i in range(n)]
    alt2 = [-sequence[i] if i % 2 == 0 else sequence[i] for i in range(n)]
    
    def kadane(arr):
        max_sum = arr[0]
        curr = arr[0]
        for x in arr[1:]:
            curr = max(x, curr + x)
            max_sum = max(max_sum, curr)
        return max_sum
    
    return max(kadane(alt1), kadane(alt2))
