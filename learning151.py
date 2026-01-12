def solution(m, n, startX, startY, balls):
    answer = []

    for bx, by in balls:
        candidates = []

        # 1. 왼쪽 벽 (x = 0)
        if not (startY == by and bx < startX):
            dx = startX + bx
            dy = startY - by
            candidates.append(dx*dx + dy*dy)

        # 2. 오른쪽 벽 (x = m)
        if not (startY == by and bx > startX):
            dx = (2*m - bx) - startX
            dy = startY - by
            candidates.append(dx*dx + dy*dy)

        # 3. 아래 벽 (y = 0)
        if not (startX == bx and by < startY):
            dx = startX - bx
            dy = startY + by
            candidates.append(dx*dx + dy*dy)

        # 4. 위 벽 (y = n)
        if not (startX == bx and by > startY):
            dx = startX - bx
            dy = (2*n - by) - startY
            candidates.append(dx*dx + dy*dy)

        answer.append(min(candidates))

    return answer
