def solution(n, m, tests):
    # 전체 좌표의 후보 영역 초기화
    possible_coords = {(x, y) for x in range(n + 1) for y in range(m + 1)}

    for x, y, d, flag in tests:
        if flag == 1:
            # 표지판에 도달한 경우
            reachable = set()
            for dx in range(-d, d + 1):
                dy = d - abs(dx)
                if 0 <= x + dx <= n and 0 <= y + dy <= m:
                    reachable.add((x + dx, y + dy))
                if 0 <= x + dx <= n and 0 <= y - dy <= m:
                    reachable.add((x + dx, y - dy))
            possible_coords &= reachable
        else:
            # 표지판에 도달하지 못한 경우
            unreachable = set()
            for dx in range(-d, d + 1):
                dy = d - abs(dx)
                if 0 <= x + dx <= n and 0 <= y + dy <= m:
                    unreachable.add((x + dx, y + dy))
                if 0 <= x + dx <= n and 0 <= y - dy <= m:
                    unreachable.add((x + dx, y - dy))
            possible_coords -= unreachable

    # 가능한 좌표 개수 반환
    return len(possible_coords)