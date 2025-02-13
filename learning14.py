import math

def solution(players, m, k):
    # 최소 증설 횟수를 기록할 변수
    total_additional_servers = 0
    
    # 각 시간대에 필요한 서버 수를 추적하는 배열
    active_servers = [0] * 24
    
    for i in range(24):
        # 현재 시간대의 이용자 수
        current_players = players[i]
        
        # 필요한 서버 수는 players[i]를 m으로 나누고 올림 처리한 값
        needed_servers = math.ceil(current_players / m)
        
        # 현재 시간대에서 이미 남아있는 서버를 차감
        available_servers = sum(active_servers[max(0, i - k + 1):i + 1])
        
        # 부족한 서버 수
        additional_servers = max(0, needed_servers - available_servers)
        
        # 부족한 서버가 있으면 그만큼 증설
        if additional_servers > 0:
            total_additional_servers += additional_servers
            # 증설된 서버는 k시간 동안 사용 가능하므로 활성화
            for j in range(i, min(i + k, 24)):
                active_servers[j] += additional_servers
        
    return total_additional_servers
