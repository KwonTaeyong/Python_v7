def solution(n, w, num):
    # num이 위치한 층과 열
    floor = (num - 1) // w
    pos_in_row = (num - 1) % w
    if floor % 2 == 0:  # 짝수층 (왼→오)
        col = pos_in_row
    else:  # 홀수층 (오른→왼)
        col = w - 1 - pos_in_row

    total = 0
    max_floor = (n - 1) // w

    for f in range(floor, max_floor + 1):
        # 이 층에서의 시작 번호
        start = f * w + 1
        end = min((f + 1) * w, n)  # 마지막 층 조정
        length = end - start + 1

        if f % 2 == 0:  # 왼→오
            if col < length:  # 해당 열에 상자가 있는 경우
                total += 1
        else:  # 오른→왼
            if (w - 1 - col) < length:
                total += 1

    return total
