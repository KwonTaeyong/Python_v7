def possible(structure):
    for x, y, a in structure:
        if a == 0:  # 기둥
            if y == 0 or [x, y-1, 0] in structure or [x-1, y, 1] in structure or [x, y, 1] in structure:
                continue
            return False
        else:  # 보
            if ([x, y-1, 0] in structure or [x+1, y-1, 0] in structure) or \
               ([x-1, y, 1] in structure and [x+1, y, 1] in structure):
                continue
            return False
    return True

def solution(n, build_frame):
    structure = []
    for x, y, a, b in build_frame:
        if b == 1:  # 설치
            structure.append([x, y, a])
            if not possible(structure):
                structure.remove([x, y, a])
        else:  # 삭제
            structure.remove([x, y, a])
            if not possible(structure):
                structure.append([x, y, a])
    return sorted(structure)
