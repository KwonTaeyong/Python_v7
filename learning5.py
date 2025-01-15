def solution(wallet, bill):
    # answer: 접은 횟수를 저장할 변수
    answer = 0
    
    # 지폐가 지갑에 들어갈 수 있는지 확인하는 함수
    def can_fit(wallet, bill):
        # 지갑의 크기보다 지폐의 크기가 작으면 들어갈 수 있음
        return (bill[0] <= wallet[0] and bill[1] <= wallet[1]) or (bill[0] <= wallet[1] and bill[1] <= wallet[0])
    
    # bill이 wallet에 들어갈 수 있도록 접기
    while not can_fit(wallet, bill):
        # 길이가 긴 쪽을 반으로 접기
        if bill[0] > bill[1]:
            bill[0] //= 2  # 가로 길이 반으로 접기
        else:
            bill[1] //= 2  # 세로 길이 반으로 접기
        answer += 1  # 접은 횟수 증가
    
    return answer