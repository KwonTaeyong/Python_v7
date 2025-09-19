from itertools import product

def solution(users, emoticons):
    discounts = [10, 20, 30, 40]
    best_plus, best_sales = 0, 0
    
    # 모든 할인율 조합 탐색 (이모티콘 개수만큼)
    for discount_case in product(discounts, repeat=len(emoticons)):
        plus_cnt, sales = 0, 0
        
        # 각 사용자별 구매 행동 계산
        for user_discount, user_price in users:
            total = 0
            for emo_price, dc in zip(emoticons, discount_case):
                if dc >= user_discount:  # 할인율이 기준 이상이면 구매
                    total += emo_price * (100 - dc) // 100
            
            if total >= user_price:  # 서비스 가입
                plus_cnt += 1
            else:  # 그냥 구매
                sales += total
        
        # 최적값 갱신
        if plus_cnt > best_plus or (plus_cnt == best_plus and sales > best_sales):
            best_plus, best_sales = plus_cnt, sales
    
    return [best_plus, best_sales]
