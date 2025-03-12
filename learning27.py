def solution(s):
    # 결과를 담을 리스트
    answer = [0, 0]
    
    # 계속해서 변환하는 과정을 반복
    while s != "1":
        # 현재 문자열에서 0의 개수 세기
        zero_count = s.count('0')
        
        # 0을 제거한 새로운 문자열 만들기
        s = s.replace('0', '')
        
        # 변환된 문자열의 길이를 2진법으로 변환
        s = bin(len(s))[2:]  # bin() 함수는 '0b'로 시작하므로 앞의 '0b'는 제외
        
        # 변환 횟수와 제거된 0의 개수 업데이트
        answer[0] += 1
        answer[1] += zero_count
    
    return answer