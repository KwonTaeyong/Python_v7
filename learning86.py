from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    # 원형을 일자로 펼치기
    weak_extended = weak + [w + n for w in weak]
    
    answer = len(dist) + 1  # 최댓값보다 큰 수로 초기화
    
    # 친구 투입 순서 모든 경우
    for friends in permutations(dist, len(dist)):
        # 시작 위치를 weak 배열의 각 지점으로 시도
        for start in range(length):
            count = 1  # 투입한 친구 수
            # 첫 번째 친구가 점검할 수 있는 최대 위치
            position = weak_extended[start] + friends[count - 1]
            
            # 취약 지점들을 차례대로 확인
            for index in range(start, start + length):
                if weak_extended[index] > position:
                    # 다음 친구 투입
                    count += 1
                    if count > len(dist):  # 친구 다 써도 안되면 종료
                        break
                    position = weak_extended[index] + friends[count - 1]
            
            answer = min(answer, count)
    
    # 모든 경우를 해도 불가능하면 -1
    if answer > len(dist):
        return -1
    return answer
