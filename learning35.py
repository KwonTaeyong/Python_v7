def solution(s):
    def expand_from_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # 길이 반환

    max_len = 0
    for i in range(len(s)):
        # 홀수 길이 팰린드롬
        len1 = expand_from_center(i, i)
        # 짝수 길이 팰린드롬
        len2 = expand_from_center(i, i + 1)
        max_len = max(max_len, len1, len2)

    return max_len
