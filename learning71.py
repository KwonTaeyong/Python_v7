def possible(answer):
    for x, y, a in answer:
        if a == 0:  # 기둥
            if y == 0 or (x, y-1, 0) in answer or (x-1, y, 1) in answer or (x, y, 1) in answer:
                continue
            return False
        else:  # 보
            if (x, y-1, 0) in answer or (x+1, y-1, 0) in answer or ((x-1, y, 1) in answer and (x+1, y, 1) in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = set()
    for x, y, a, b in build_frame:
        if b == 1:  # 설치
            answer.add((x, y, a))
            if not possible(answer):
                answer.remove((x, y, a))
        else:  # 삭제
            if (x, y, a) in answer:
                answer.remove((x, y, a))
                if not possible(answer):
                    answer.add((x, y, a))
    return sorted(map(list, answer))
