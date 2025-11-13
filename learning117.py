def solution(temperature, t1, t2, a, b, onboard):
    from collections import defaultdict
    INF = 10**18

    N = len(onboard)
    # dp: 현재 시각(분)에서의 실내온도 -> 최소 소비전력
    # 초기: 시간 0의 온도는 외기(temperature)
    dp = {temperature: 0}

    # we perform transitions for minutes i = 0 .. N-2 (action during minute i -> state at i+1)
    for i in range(0, N - 1):
        ndp = defaultdict(lambda: INF)
        for temp, cost in dp.items():
            # 1) AC off: temp moves 1 toward outside temperature (or stays if equal), cost 0
            if temp < temperature:
                nxt = temp + 1
            elif temp > temperature:
                nxt = temp - 1
            else:
                nxt = temp
            # enforce comfort constraint at minute i+1 if passenger on
            if not (onboard[i + 1] == 1 and not (t1 <= nxt <= t2)):
                if cost < ndp[nxt]:
                    ndp[nxt] = cost

            # 2) AC on & hold (desired == current): stays same, cost b
            nxt = temp
            new_cost = cost + b
            if not (onboard[i + 1] == 1 and not (t1 <= nxt <= t2)):
                if new_cost < ndp[nxt]:
                    ndp[nxt] = new_cost

            # 3) AC on & raise: temp + 1, cost a
            nxt = temp + 1
            new_cost = cost + a
            if not (onboard[i + 1] == 1 and not (t1 <= nxt <= t2)):
                if new_cost < ndp[nxt]:
                    ndp[nxt] = new_cost

            # 4) AC on & lower: temp - 1, cost a
            nxt = temp - 1
            new_cost = cost + a
            if not (onboard[i + 1] == 1 and not (t1 <= nxt <= t2)):
                if new_cost < ndp[nxt]:
                    ndp[nxt] = new_cost

        # 만약 어떤 온도도 가능한 상태로 이어지지 않으면(문제 조건상 없음), INF 처리
        dp = {k: v for k, v in ndp.items() if v < INF}

    # 결과: 마지막 시각(N-1)에 도달 가능한 상태 중 최소 비용
    if not dp:
        return -1  # 문제에서 불가능한 경우는 주어지지 않으므로 사실상 사용 안 됨
    return min(dp.values())
