def solution(points, routes):
    from collections import defaultdict

    # 1. 포인트 번호 → 좌표 매핑
    point_pos = {i+1: tuple(p) for i, p in enumerate(points)}

    # 2. 로봇별 경로 좌표 리스트 생성
    robots_paths = []
    for route in routes:
        path = []
        # 시작 포인트
        cur_r, cur_c = point_pos[route[0]]
        path.append((cur_r, cur_c))
        # 이동
        for nxt in route[1:]:
            nxt_r, nxt_c = point_pos[nxt]
            # r 좌표 이동 (우선)
            while cur_r != nxt_r:
                cur_r += 1 if cur_r < nxt_r else -1
                path.append((cur_r, cur_c))
            # c 좌표 이동
            while cur_c != nxt_c:
                cur_c += 1 if cur_c < nxt_c else -1
                path.append((cur_r, cur_c))
        robots_paths.append(path)

    # 3. 시간 단위 시뮬레이션
    answer = 0
    t = 0
    while True:
        positions = defaultdict(int)
        active = False
        for path in robots_paths:
            if t < len(path):
                positions[path[t]] += 1
                active = True
        # 모든 로봇 끝나면 종료
        if not active:
            break
        # 4. 충돌 체크
        for pos, cnt in positions.items():
            if cnt >= 2:
                answer += 1
        t += 1

    return answer
