1def solution(n, bans):
    # 26의 거듭제곱 미리 계산
    pow26 = [1]
    for _ in range(11):
        pow26.append(pow26[-1] * 26)

    # 문자열 → 전체 주문서에서의 순서(index, 1-based)
    def get_index(s):
        L = len(s)
        idx = 0
        # 짧은 길이들
        for i in range(1, L):
            idx += pow26[i]
        # 같은 길이 내 사전순
        for i, ch in enumerate(s):
            idx += (ord(ch) - ord('a')) * pow26[L - i - 1]
        return idx + 1

    # index → 문자열
    def get_string(idx):
        # 길이 결정
        L = 1
        while idx > pow26[L]:
            idx -= pow26[L]
            L += 1

        idx -= 1  # 0-based
        res = []
        for i in range(L):
            base = pow26[L - i - 1]
            res.append(chr(ord('a') + idx // base))
            idx %= base
        return ''.join(res)

    # bans를 index로 변환
    ban_idx = [get_index(b) for b in bans]
    ban_idx.sort()

    # x번째 문자열에서 삭제된 개수
    def removed_before(x):
        # x보다 작은 ban 개수
        lo, hi = 0, len(ban_idx)
        while lo < hi:
            mid = (lo + hi) // 2
            if ban_idx[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    # 이분 탐색으로 실제 위치 찾기
    left, right = 1, 10**16
    while left < right:
        mid = (left + right) // 2
        if mid - removed_before(mid) >= n:
            right = mid
        else:
            left = mid + 1

    return get_string(left)
