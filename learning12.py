from itertools import combinations

def solution(n, q, ans):
    # 가능한 모든 비밀 코드 조합 생성 (1부터 n까지 중 5개 선택)
    all_combinations = list(combinations(range(1, n + 1), 5))
    
    valid_count = 0

    # 각 조합이 조건을 만족하는지 확인
    for comb in all_combinations:
        is_valid = True

        for i in range(len(q)):
            # q[i]와 comb의 교집합 개수 계산
            intersection_count = len(set(q[i]) & set(comb))
            
            # 교집합 개수가 ans[i]와 다르면 조건 불만족
            if intersection_count != ans[i]:
                is_valid = False
                break

        # 모든 조건을 만족하면 유효한 조합으로 간주
        if is_valid:
            valid_count += 1

    return valid_count

# 예제 테스트
n = 10
q = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [3, 7, 8, 9, 10],
    [2, 5, 7, 9, 10],
    [3, 4, 5, 6, 7]
]
ans = [2, 3, 4, 3, 3]

result = solution(n, q, ans)
print(result)  # 출력: 3