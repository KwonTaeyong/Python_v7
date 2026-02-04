def solution(coin, cards):
    n = len(cards)
    target = n + 1

    # 처음 카드 n/3장
    hand = set(cards[:n//3])
    idx = n // 3

    wait = set()
    round_cnt = 0

    while True:
        # 카드 없으면 종료
        if idx >= n:
            break

        # 라운드 시작
        round_cnt += 1

        # 카드 2장 공개
        c1, c2 = cards[idx], cards[idx+1]
        idx += 2

        # 일단 wait 후보로
        wait.add(c1)
        wait.add(c2)

        used = False

        # 1️⃣ 손패끼리 (0코인)
        for x in list(hand):
            if target - x in hand and target - x != x:
                hand.remove(x)
                hand.remove(target - x)
                used = True
                break

        # 2️⃣ 손패 + wait (1코인)
        if not used and coin >= 1:
            for x in list(hand):
                y = target - x
                if y in wait:
                    hand.remove(x)
                    wait.remove(y)
                    coin -= 1
                    used = True
                    break

        # 3️⃣ wait + wait (2코인)
        if not used and coin >= 2:
            for x in list(wait):
                y = target - x
                if y in wait and y != x:
                    wait.remove(x)
                    wait.remove(y)
                    coin -= 2
                    used = True
                    break

        # 못 냈으면 종료
        if not used:
            round_cnt -= 1
            break

    return round_cnt
