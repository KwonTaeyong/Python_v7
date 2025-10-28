from collections import defaultdict, Counter

def solution(points, routes):
    # 포인트 번호 → 좌표 매핑
    point_dict = {i + 1: tuple(p) for i, p in enumerate(points)}
    
    # 각 로봇의 시간별 경로 저장
    robot_paths = []
    max_time = 0  # 전체 시뮬레이션 시간
    
    for route in routes:
        path = []
        # 첫 포인트부터 시작
        r, c = point_dict[route[0]]
        path.append((r, c))
        
        # 다음 포인트들로 이동
        for nxt in route[1:]:
            nr, nc = point_dict[nxt]
            # r 좌표 먼저 이동
            while r != nr:
                r += 1 if nr > r else -1
                path.append((r, c))
            # 그 다음 c 좌표 이동
            while c != nc:
                c += 1 if nc > c else -1
                path.append((r, c))
        robot_paths.append(path)
        max_time = max(max_time, len(path))
    
    # 시간별 로봇 위치 기록
    time_positions = defaultdict(list)
    for path in robot_paths:
        for t in range(len(path)):
            time_positions[t].append(path[t])
        # 로봇이 끝난 후에는 더 이상 추가하지 않음
    
    # 충돌 위험 계산
    answer = 0
    for t in range(max_time):
        if t not in time_positions:
            continue
        cnt = Counter(time_positions[t])
        # 같은 위치에 2대 이상 있는 곳마다 1씩 추가
        for v in cnt.values():
            if v >= 2:
                answer += 1
    
    return answer
