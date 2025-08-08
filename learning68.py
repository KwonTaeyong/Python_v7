def solution(s):
    answer = []
    
    for string in s:
        stack = []
        count_110 = 0

        # "110" 제거
        for c in string:
            stack.append(c)
            if len(stack) >= 3 and stack[-3:] == ['1', '1', '0']:
                stack.pop()
                stack.pop()
                stack.pop()
                count_110 += 1
        
        # stack에는 "110"이 제거된 상태의 문자들이 남아 있음
        # 이제 "110"을 어디에 끼워넣을지 결정해야 함
        # 기준: 가장 마지막 0 뒤에 끼운다
        idx = len(stack)
        for i in range(len(stack)-1, -1, -1):
            if stack[i] == '0':
                idx = i + 1
                break
        
        # "110"을 count_110개 삽입
        result = stack[:idx] + ['110'] * count_110 + stack[idx:]
        answer.append(''.join(result))
    
    return answer
