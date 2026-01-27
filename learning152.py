import math

def solution(players, m, k):
    answer = 0
    
    # expire[i] : i시에 반납되는 서버 수
    expire = [0] * (24 + k + 1)
    active = 0  # 현재 운영 중인 서버 수
    
    for hour in range(24):
        # 만료된 서버 반납
        active -= expire[hour]
        
        # 현재 시간에 필요한 서버 수
        required = math.ceil(players[hour] / m)
        
        # 부족하면 증설
        if active < required:
            add = required - active
            answer += add
            active += add
            expire[hour + k] += add  # k시간 뒤 반납
    
    return answer
