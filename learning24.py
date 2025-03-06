from itertools import product
from bisect import bisect_left, bisect_right

def solution(info, query):
    # info 배열을 기반으로 조건을 만족하는 사람들의 데이터를 저장할 딕셔너리 생성
    data = {}
    
    # info 데이터를 처리하여 딕셔너리에 저장
    for i in info:
        i = i.split()  # ['java', 'backend', 'junior', 'pizza', '150']
        score = int(i[-1])  # 점수
        conditions = i[:-1]  # ['java', 'backend', 'junior', 'pizza']
        
        # 가능한 모든 조건에 대해 점수를 추가
        for comb in product(*[(c, '-') for c in conditions]):
            key = comb
            if key not in data:
                data[key] = []
            data[key].append(score)
    
    # 각 조건별 점수를 정렬 (이진 탐색을 위해)
    for key in data:
        data[key].sort()
    
    # query를 처리하여 결과를 반환
    result = []
    
    for q in query:
        q = q.split()
        q_conditions = tuple(q[i] if q[i] != "and" else "-" for i in range(0, len(q), 2))  # 조건 부분 추출
        score_threshold = int(q[-1])  # 점수 부분 추출
        
        # 해당 조건에 맞는 리스트를 찾고, 이진 탐색으로 점수 이상인 사람을 찾음
        if q_conditions in data:
            scores = data[q_conditions]
            idx = bisect_left(scores, score_threshold)
            result.append(len(scores) - idx)
        else:
            result.append(0)
    
    return result
