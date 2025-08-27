def solution(n, bans):
    bans = set(bans)
    max_len = 11
    pow26 = [1] * (max_len + 2)
    for i in range(1, max_len + 2):
        pow26[i] = pow26[i - 1] * 26

    # prefix p로 시작하는 문자열 개수
    def count_with_prefix(p):
        L = len(p)
        if L > max_len:
            return 0
        # p 자신
        total = 1
        # p 뒤에 붙는 길이들
        remain = max_len - L
        if remain > 0:
            total += (pow26[remain + 1] - 26) // 25  # 등비수열 합
        # ban 제외
        # (단순히 bans 중 p로 시작하는 것 세면 안됨 → 전체를 미리 count)
        for b in bans:
            if b.startswith(p) and len(b) <= max_len:
                total -= 1
        return total

    prefix = ""
    while True:
        for c in map(chr, range(ord('a'), ord('z') + 1)):
            cnt = count_with_prefix(prefix + c)
            if n <= cnt:
                prefix += c
                # prefix 자체가 ban이 아니면 1개 차감
                if prefix not in bans:
                    if n == 1:
                        return prefix
                    n -= 1
                break
            else:
                n -= cnt
