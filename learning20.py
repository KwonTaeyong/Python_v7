def solution(temperature, t1, t2, a, b, onboard):
    # 실내 온도를 추적할 변수
    current_temp = temperature
    total_power = 0
    
    # 각 분마다 수행
    for i in range(len(onboard)):
        if onboard[i] == 1:
            # 승객 탑승 중일 때, 실내 온도를 t1 ~ t2 사이로 유지해야 함
            if current_temp < t1:
                # 실내 온도가 너무 낮으면, 에어컨을 켜서 올림
                desired_temp = t1
                if current_temp != desired_temp:
                    total_power += a  # 에어컨을 켰을 때의 소비 전력
                current_temp += 1  # 온도가 1도 상승
            elif current_temp > t2:
                # 실내 온도가 너무 높으면, 에어컨을 켜서 내림
                desired_temp = t2
                if current_temp != desired_temp:
                    total_power += a  # 에어컨을 켰을 때의 소비 전력
                current_temp -= 1  # 온도가 1도 하강
            else:
                # 실내 온도가 이미 범위 내에 있으면, 에어컨을 끄고 b 소비 전력
                total_power += b  # 에어컨이 켜져 있어도 희망 온도와 같으면 소비 전력 b
        else:
            # 승객이 탑승하지 않으면, 실내 온도가 실외 온도와 같아지도록 함
            if current_temp < temperature:
                current_temp += 1  # 실내 온도가 1도 상승
            elif current_temp > temperature:
                current_temp -= 1  # 실내 온도가 1도 하강
            # 에어컨이 꺼져 있을 때는 전력 소비가 없다.
    
    return total_power
