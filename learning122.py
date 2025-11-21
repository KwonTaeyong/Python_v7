def solution(book_time):
    # 24시간 = 1440분, 끝+청소 포함하면 최대 1440+10까지 필요
    timeline = [0] * (1440 + 11)

    def to_min(time):
        h, m = map(int, time.split(":"))
        return h * 60 + m

    for start, end in book_time:
        s = to_min(start)
        e = to_min(end) + 10  # 청소시간 포함

        timeline[s] += 1
        timeline[e] -= 1

    max_rooms = 0
    current = 0
    for t in timeline:
        current += t
        max_rooms = max(max_rooms, current)

    return max_rooms
