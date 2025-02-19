import bisect

# 알파벳 소문자 리스트
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def generate_all_strings():
    """1부터 11까지 길이의 문자열을 사전 순으로 모두 생성한다."""
    result = []
    # 길이가 1부터 11까지
    for length in range(1, 12):
        # 길이별로 가능한 모든 문자열을 추가
        for i in range(26 ** length):
            s = ""
            n = i
            for _ in range(length):
                s = alphabet[n % 26] + s
                n //= 26
            result.append(s)
    return result

def solution(n, bans):
    # 모든 가능한 주문을 생성합니다.
    all_orders = generate_all_strings()

    # 삭제된 주문들을 set으로 변환하여 빠르게 찾을 수 있도록 합니다.
    ban_set = set(bans)

    # 삭제된 주문들을 제외한 유효한 주문들을 구합니다.
    valid_orders = [order for order in all_orders if order not in ban_set]

    # 유효한 주문 중 n번째 주문을 찾습니다.
    return valid_orders[n - 1]

# 테스트
n = 30
bans = ["d", "e", "bb", "aa", "ae"]
print(solution(n, bans))  # "ah"

n = 7388
bans = ["gqk", "kdn", "jxj", "jxi", "fug", "jxg", "ewq", "len", "bhc"]
print(solution(n, bans))  # "jxk"
