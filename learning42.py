def solution(land, P, Q):
    N = len(land)
    height_list = [height for row in land for height in row]
    min_h, max_h = min(height_list), max(height_list)

    def get_cost(target):
        cost = 0
        for h in height_list:
            if h < target:
                cost += (target - h) * P
            elif h > target:
                cost += (h - target) * Q
        return cost

    answer = float('inf')
    left, right = min_h, max_h

    while left <= right:
        mid = (left + right) // 2
        cost1 = get_cost(mid)
        cost2 = get_cost(mid + 1)

        answer = min(answer, cost1, cost2)

        if cost1 < cost2:
            right = mid - 1
        else:
            left = mid + 1

    return answer
