from itertools import combinations

def solution(n, q, ans):
    answer = 0

    # 1 ~ n 중 5개 선택하는 모든 조합 확인
    for comb in combinations(range(1, n + 1), 5):
        valid = True
        code_set = set(comb)

        for i in range(len(q)):
            # q[i]와 comb의 교집합 크기 확인
            inter = len(code_set.intersection(q[i]))
            if inter != ans[i]:
                valid = False
                break

        if valid:
            answer += 1
            
    # test commit for GitHub grass 🌿

    # return
    return answer
