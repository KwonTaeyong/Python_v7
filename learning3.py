from collections import defaultdict

def solution(points, routes):
    def calculate_path(start, end):
        """
        두 좌표 사이의 최단 경로를 계산하여 경로상 모든 좌표를 반환합니다.
        """
        path = []
        curr_r, curr_c = start
        target_r, target_c = end

        # r 좌표 먼저 이동
        while curr_r != target_r:
            if curr_r < target_r:
                curr_r += 1
            else:
                curr_r -= 1
            path.append((curr_r, curr_c))

        # c 좌표 이동
        while curr_c != target_c:
            if curr_c < target_c:
                curr_c += 1
            else:
                curr_c -= 1
            path.append((curr_r, curr_c))

        return path

    # 포인트 번호 -> 좌표 매핑
    point_map = {i + 1: (r, c) for i, (r, c) in enumerate(points)}

    # 로봇 경로 계산
    robot_paths = []
    for route in routes:
        path = []
        for i in range(len(route) - 1):
            start_point = point_map[route[i]]
            end_point = point_map[route[i + 1]]
            path.extend(calculate_path(start_point, end_point))
        robot_paths.append(path)

    # 시간별 위치 추적
    time_positions = defaultdict(list)
    max_time = 0
    for robot_id, path in enumerate(robot_paths):
        for time, position in enumerate(path):
            time_positions[time].append(position)
            max_time = max(max_time, time)

    # 위험 상황 계산
    danger_count = 0
    for time in range(max_time + 1):
        position_count = defaultdict(int)
        for position in time_positions[time]:
            position_count[position] += 1

        # 동일 위치에 로봇이 2대 이상인 경우 위험 상황 발생
        for count in position_count.values():
            if count > 1:
                danger_count += 1

    return danger_count