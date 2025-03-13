import math

def solution(fees, records):
    # fees -> 기본 시간, 기본 요금, 단위 시간, 단위 요금
    basic_time, basic_fee, unit_time, unit_fee = fees
    
    # 차량별 입차/출차 기록을 저장
    car_times = {}
    car_entries = {}
    
    # records를 순회하면서 입차/출차 정보를 처리
    for record in records:
        time, car_number, action = record.split()
        hour, minute = map(int, time.split(":"))
        total_minutes = hour * 60 + minute
        
        if action == "IN":
            car_entries[car_number] = total_minutes  # 차량 입차 시간 기록
        else:  # "OUT"
            in_time = car_entries.pop(car_number)  # 차량 입차 시간
            parked_time = total_minutes - in_time  # 주차 시간 계산
            
            if car_number not in car_times:
                car_times[car_number] = 0
            car_times[car_number] += parked_time  # 차량의 총 주차 시간 누적
    
    # 입차된 상태로 끝났다면 23:59에 출차된 것으로 간주
    for car_number, entry_time in car_entries.items():
        total_minutes = 23 * 60 + 59  # 23:59
        parked_time = total_minutes - entry_time
        if car_number not in car_times:
            car_times[car_number] = 0
        car_times[car_number] += parked_time
    
    # 요금을 계산하여 리스트에 담기
    result = []
    for car_number in sorted(car_times.keys()):
        parked_time = car_times[car_number]
        
        if parked_time <= basic_time:
            result.append(basic_fee)
        else:
            # 초과 시간 계산
            over_time = parked_time - basic_time
            extra_fee = math.ceil(over_time / unit_time) * unit_fee
            result.append(basic_fee + extra_fee)
    
    return result
