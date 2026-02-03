def solution(points, routes):
    # 포인트 번호 → 좌표
    pos = {i + 1: tuple(points[i]) for i in range(len(points))}

    # 각 로봇의 시간별 위치 기록
    robot_paths = []

    for route in routes:
        path = []
        r, c = pos[route[0]]
        path.append((r, c))  # t = 0

        for i in range(1, len(route)):
            tr, tc = pos[route[i]]

            # r 먼저 이동
            while r != tr:
                r += 1 if tr > r else -1
                path.append((r, c))

            # c 이동
            while c != tc:
                c += 1 if tc > c else -1
                path.append((r, c))

        robot_paths.append(path)

    # 전체 최대 시간
    max_time = max(len(p) for p in robot_paths)

    answer = 0

    # 시간별 충돌 검사
    for t in range(max_time):
        counter = {}
        for path in robot_paths:
            if t < len(path):
                counter[path[t]] = counter.get(path[t], 0) + 1

        # 같은 좌표에 2대 이상 있으면 위험 1회
        for cnt in counter.values():
            if cnt >= 2:
                answer += 1

    return answer
