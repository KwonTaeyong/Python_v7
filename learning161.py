def solution(land, P, Q):
    heights = [h for row in land for h in row]

    lo = min(heights)
    hi = max(heights)

    def cost(H):
        total = 0
        for h in heights:
            if h < H:
                total += (H - h) * P
            else:
                total += (h - H) * Q
        return total

    answer = cost(lo)

    while lo <= hi:
        mid = (lo + hi) // 2
        c_mid = cost(mid)
        c_next = cost(mid + 1)

        answer = min(answer, c_mid, c_next)

        if c_next < c_mid:
            lo = mid + 1
        else:
            hi = mid - 1

    return answer
