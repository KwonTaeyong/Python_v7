def solution(s):
    n = len(s)
    pos = [[] for _ in range(26)]
    
    # 각 문자 위치 기록
    for i, ch in enumerate(s):
        pos[ord(ch) - 97].append(i)

    total = 0
    for idx_list in pos:
        if len(idx_list) <= 1:
            continue  # 등장 횟수가 1 이하이면 아름다움 기여 없음
        
        # 왼쪽/오른쪽 경계 확장
        for k in range(len(idx_list)):
            i = idx_list[k]
            prev = idx_list[k-1] if k > 0 else -1
            next = idx_list[k+1] if k+1 < len(idx_list) else n
            
            # i를 한쪽 끝으로 하는 부분문자열 개수
            total += (i - prev) * (next - i) - 1  # -1은 모든 글자 같을 때 제외

    return total
