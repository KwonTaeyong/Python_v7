from collections import defaultdict

def solution(points, routes):
    # 포인트 번호 → 좌표
    pos = {i + 1: tuple(points[i]) for i in range(len(points))}

    robot_paths = []
    max_time = 0

    # 각 로봇의 전체 이동 경로 계산
    for route in routes:
        path = []
        r, c = pos[route[0]]
        path.append((r, c))

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
        max_time = max(max_time, len(path))

    answer = 0

    # 시간별 충돌 체크
    for t in range(max_time):
        counter = defaultdict(int)

        for path in robot_paths:
            if t < len(path):
                counter[path[t]] += 1

        # 2대 이상 있는 좌표 수만큼 더함
        for cnt in counter.values():
            if cnt >= 2:
                answer += 1

    return answer
