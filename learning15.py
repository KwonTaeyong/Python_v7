def solution(schedules, timelogs, startday):
    # 상품을 받을 직원 수
    answer = 0
    
    # 평일을 계산하기 위한 리스트 (startday 기준으로 월~금 인덱스 찾기)
    weekdays = [(startday + i - 1) % 7 for i in range(5)]
    
    for i in range(len(schedules)):
        expected_time = schedules[i]  # 출근 희망 시각
        latest_time = expected_time + 10  # 출근 인정 시각
        
        valid = True  # 상품 수령 가능 여부
        
        for day in weekdays:
            if timelogs[i][day] > latest_time:  # 출근 인정 시각을 초과하면 지각
                valid = False
                break
        
        if valid:
            answer += 1  # 모든 평일에 늦지 않았으면 상품 받을 직원으로 추가
    
    return answer
