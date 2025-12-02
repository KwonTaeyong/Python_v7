from collections import Counter

def solution(str1, str2):
    def make_multiset(s):
        s = s.lower()
        elems = []
        for i in range(len(s) - 1):
            a, b = s[i], s[i+1]
            if a.isalpha() and b.isalpha():
                elems.append(a + b)
        return Counter(elems)

    A = make_multiset(str1)
    B = make_multiset(str2)

    # 교집합 크기: 각 키에 대해 min(counts)
    inter = 0
    # 합집합 크기: 각 키에 대해 max(counts)
    union = 0

    all_keys = set(A.keys()) | set(B.keys())
    for k in all_keys:
        inter += min(A.get(k, 0), B.get(k, 0))
        union += max(A.get(k, 0), B.get(k, 0))

    # 둘 다 공집합인 경우 유사도 1로 정의
    if union == 0:
        return 65536

    jaccard = inter / union
    return int(jaccard * 65536)

# 간단한 테스트
if __name__ == "__main__":
    tests = [
        ("FRANCE", "french", 16384),
        ("handshake", "shake hands", 65536),
        ("aa1+aa2", "AAAA12", 43690),
        ("E=M*C^2", "e=m*c^2", 65536),  # 둘 다 유효한 쌍 없음 -> 1 * 65536
    ]
    for s1, s2, expected in tests:
        print(s1, s2, "=>", solution(s1, s2), "expected:", expected)
