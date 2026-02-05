def solution(s):
    n = len(s)
    answer = 1  # 최소 길이는 1

    def expand(left, right):
        nonlocal answer
        while left >= 0 and right < n and s[left] == s[right]:
            answer = max(answer, right - left + 1)
            left -= 1
            right += 1

    for i in range(n):
        # 홀수 길이 팰린드롬
        expand(i, i)
        # 짝수 길이 팰린드롬
        expand(i, i + 1)

    return answer
