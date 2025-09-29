def solution(n, t, m, timetable):
    # 문자열 시간을 분으로 변환
    def to_minutes(time_str):
        h, m = map(int, time_str.split(":"))
        return h * 60 + m

    # 분을 HH:MM 문자열로 변환
    def to_str(minutes):
        h = minutes // 60
        m = minutes % 60
        return f"{h:02d}:{m:02d}"

    # 크루 도착 시간 정렬
    crews = sorted([to_minutes(time) for time in timetable])
    
    # 셔틀 시작 시간
    start = 9 * 60  # 09:00 -> 540분
    idx = 0  # 크루 인덱스
    
    for i in range(n):  # n번 셔틀 운행
        shuttle_time = start + i * t
        cnt = 0
        last_boarded = None
        
        # 해당 셔틀에 탈 수 있는 크루 태움
        while cnt < m and idx < len(crews) and crews[idx] <= shuttle_time:
            last_boarded = crews[idx]
            idx += 1
            cnt += 1

        # 마지막 셔틀이라면 조건 체크
        if i == n - 1:
            if cnt < m:  # 자리가 남았음
                return to_str(shuttle_time)
            else:  # 꽉 찼음 → 마지막 탄 사람보다 1분 일찍
                return to_str(last_boarded - 1)
