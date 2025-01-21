from collections import defaultdict, deque

def solution(points, routes):
    # 각 포인트 번호를 좌표로 매핑
    point_map = {i + 1: (r, c) for i, (r, c) in enumerate(points)}

    # 각 로봇의 이동 경로를 계산
    robot_paths = []
    for route in routes:
        path = []
        for i in range(len(route) - 1):
            start = point_map[route[i]]
            end = point_map[route[i + 1]]
            path.extend(get_path(start, end))
        path.append(point_map[route[-1]])  # 마지막 포인트 추가
        robot_paths.append(path)

    # 모든 로봇의 이동 경로를 시간에 따라 추적
    time_map = defaultdict(int)
    max_time = 0
    for path in robot_paths:
        time = 0
        for pos in path:
            time_map[(time, pos)] += 1
            time += 1
        max_time = max(max_time, time)

    # 충돌 위험 계산
    danger_count = 0
    for (time, pos), count in time_map.items():
        if count > 1:
            danger_count += 1

    return danger_count

def get_path(start, end):
    """
    주어진 시작 좌표(start)와 끝 좌표(end) 사이의 최단 경로를 계산합니다.
    r 좌표를 먼저 이동하고, 그다음 c 좌표를 이동합니다.
    """
    sr, sc = start
    er, ec = end
    path = []

    # r 좌표 이동
    if sr < er:
        for r in range(sr, er):
            path.append((r, sc))
    elif sr > er:
        for r in range(sr, er, -1):
            path.append((r, sc))

    # c 좌표 이동
    if sc < ec:
        for c in range(sc, ec):
            path.append((er, c))
    elif sc > ec:
        for c in range(sc, ec, -1):
            path.append((er, c))

    return path

# 테스트 케이스
print(solution(
    [[3, 2], [6, 4], [4, 7], [1, 4]],
    [[4, 2], [1, 3], [2, 4]]
))  # 1

print(solution(
    [[3, 2], [6, 4], [4, 7], [1, 4]],
    [[4, 2], [1, 3], [4, 2], [4, 3]]
))  # 9

print(solution(
    [[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]],
    [[2, 3, 4, 5], [1, 3, 4, 5]]
))  # 0