from collections import defaultdict, deque

def solution(points, routes):
    # 포인트 번호를 좌표로 변환하기 위한 딕셔너리 생성
    point_coords = {i + 1: (r, c) for i, (r, c) in enumerate(points)}

    # 각 로봇별로 경로를 계산
    robot_paths = []
    for route in routes:
        path = []
        for i in range(len(route) - 1):
            start = point_coords[route[i]]
            end = point_coords[route[i + 1]]
            path.extend(get_path(start, end))
        path.append(point_coords[route[-1]])  # 마지막 포인트 추가
        robot_paths.append(path)

    # 각 시간별 로봇 위치를 기록하기 위한 딕셔너리
    time_positions = defaultdict(list)

    # 최대 이동 시간을 계산
    max_time = max(len(path) for path in robot_paths)

    # 각 시간에 로봇의 위치를 기록
    for robot_id, path in enumerate(robot_paths):
        for t, position in enumerate(path):
            time_positions[t].append(position)

    # 충돌 위험 상황 계산
    danger_count = 0
    for t in range(max_time):
        position_counts = defaultdict(int)
        for position in time_positions[t]:
            position_counts[position] += 1
        danger_count += sum(count - 1 for count in position_counts.values() if count > 1)

    return danger_count

def get_path(start, end):
    """
    두 좌표(start, end) 사이의 최단 경로를 생성합니다.
    r 좌표를 먼저 이동한 후 c 좌표를 이동하는 규칙을 따릅니다.
    """
    path = []
    sr, sc = start
    er, ec = end

    # r 좌표 이동
    if sr < er:
        path.extend((r, sc) for r in range(sr + 1, er + 1))
    else:
        path.extend((r, sc) for r in range(sr - 1, er - 1, -1))

    # c 좌표 이동
    if sc < ec:
        path.extend((er, c) for c in range(sc + 1, ec + 1))
    else:
        path.extend((er, c) for c in range(sc - 1, ec - 1, -1))

    return path

# 테스트 코드
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