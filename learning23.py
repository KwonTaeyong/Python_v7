def solution(data, col, row_begin, row_end):
    # col은 1-based index이므로 0-based index로 변환
    col -= 1
    
    # 데이터 정렬
    # 1. col 번째 컬럼을 기준으로 오름차순 정렬
    # 2. col 번째 값이 동일하면 첫 번째 컬럼을 기준으로 내림차순 정렬
    sorted_data = sorted(data, key=lambda x: (x[col], -x[0]))
    
    # 누적된 XOR 값 초기화
    result = 0
    
    # row_begin부터 row_end까지 S_i 계산
    for i in range(row_begin - 1, row_end):
        # S_i 계산: 각 컬럼의 값을 i로 나눈 나머지의 합
        S_i = sum([sorted_data[i][j] % (i + 1) for j in range(len(sorted_data[i]))])
        
        # XOR 연산
        result ^= S_i
    
    return result
