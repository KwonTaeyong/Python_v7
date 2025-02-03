def solution(friends, gifts):
    n = len(friends)
    
    # 선물 받은 횟수와 준 횟수 초기화
    received = {friend: 0 for friend in friends}
    given = {friend: 0 for friend in friends}
    
    # 선물 주고받은 기록 분석
    for gift in gifts:
        giver, receiver = gift.split()
        given[giver] += 1
        received[receiver] += 1
    
    # 선물 지수 계산
    gift_index = {}
    for friend in friends:
        gift_index[friend] = given[friend] - received[friend]
    
    # 선물 받기 예측
    next_month_gifts = {friend: 0 for friend in friends}
    
    for i in range(n):
        for j in range(n):
            if i != j:
                giver = friends[i]
                receiver = friends[j]
                
                # 주고받은 선물의 차이를 바탕으로 예측
                if given[giver] > given[receiver]:
                    next_month_gifts[receiver] += 1
                elif given[giver] < given[receiver]:
                    next_month_gifts[giver] += 1
                else:
                    # 주고받은 선물이 같을 경우 선물 지수로 결정
                    if gift_index[giver] > gift_index[receiver]:
                        next_month_gifts[receiver] += 1
                    elif gift_index[giver] < gift_index[receiver]:
                        next_month_gifts[giver] += 1
    
    # 가장 많은 선물을 받을 친구가 받을 선물의 수를 반환
    return max(next_month_gifts.values())