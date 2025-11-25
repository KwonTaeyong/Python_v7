def solution(storey):
    answer = 0
    
    while storey > 0:
        digit = storey % 10  # 현재 자리 숫자
        next_digit = (storey // 10) % 10  # 다음 자리 숫자
        
        if digit < 5:
            answer += digit
            storey //= 10  # 자리 이동
        elif digit > 5:
            answer += (10 - digit)
            storey = storey // 10 + 1  # 올림 처리
        else:  # digit == 5
            # 다음 자리 숫자가 5 이상이면 올림이 유리
            if next_digit >= 5:
                answer += 5
                storey = storey // 10 + 1
            else:
                answer += 5
                storey //= 10
                
    return answer
