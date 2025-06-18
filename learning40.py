def solution(n, s):
    if s < n:
        return [-1]
    
    q, r = divmod(s, n)
    # q를 n - r개, q+1을 r개 만든 후 정렬
    return [q] * (n - r) + [q + 1] * r


print(solution(2, 9))  # [4, 5]
print(solution(2, 1))  # [-1]
print(solution(2, 8))  # [4, 4]
