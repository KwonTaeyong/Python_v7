def solution(x1, x2, x3, x4):
    # OR 연산자 (∨)를 사용하여 각 괄호 부분을 계산
    part1 = x1 or x2
    part2 = x3 or x4
    
    # AND 연산자 (∧)를 사용하여 최종 결과 계산
    answer = part1 and part2
    
    return answer