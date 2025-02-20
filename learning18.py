def solution(n, w, num):
    # 전체 상자들이 쌓이는 방식
    # 층마다 w개의 상자를 왼쪽에서 오른쪽, 오른쪽에서 왼쪽 번갈아가며 쌓음
    boxes = []
    layer = 0
    while len(boxes) < n:
        if layer % 2 == 0:
            # 왼쪽에서 오른쪽으로 채움
            boxes.extend(range(layer * w + 1, min((layer + 1) * w + 1, n + 1)))
        else:
            # 오른쪽에서 왼쪽으로 채움
            boxes.extend(range(min((layer + 1) * w + 1, n + 1), layer * w, -1))
        layer += 1
    
    # boxes는 1~n까지의 상자 번호가 왼쪽에서 오른쪽, 오른쪽에서 왼쪽으로 쌓인 순서를 나열한 리스트입니다.
    # 그 중에서 num이 몇 번째로 위치하는지 찾아 해당 상자를 꺼내기 위해 필요한 상자의 개수를 구합니다.
    
    # num이 boxes에서 몇 번째 위치에 있는지 확인
    idx = boxes.index(num)
    
    # 꺼내려는 상자와 그 위의 상자들이 몇 개가 있는지 구합니다.
    return idx + 1

# 테스트
n = 22
w = 6
num = 8
print(solution(n, w, num))  # 3

n = 13
w = 3
num = 6
print(solution(n, w, num))  # 4