def solution(cpr):
    order = ["check", "call", "pressure", "respiration", "repeat"]
    return [order.index(step) + 1 for step in cpr]

    cpr = ["call", "respiration", "repeat", "check", "pressure"]
    print(solution(cpr))
# [2, 4, 5, 1, 3]