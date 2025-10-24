from itertools import permutations

def solution(n, submit):
    # 가능한 모든 후보 (1~9, 중복 없이 4자리)
    candidates = [''.join(map(str, p)) for p in permutations(range(1, 10), 4)]

    # 단서 생성 함수
    def get_hint(secret, guess):
        s = b = 0
        for i in range(4):
            if secret[i] == guess[i]:
                s += 1
            elif guess[i] in secret:
                b += 1
        return f"{s}S {b}B"
    
    while candidates:
        guess = candidates[0]  # 첫 번째 후보를 시도
        result = submit(int(guess))
        if result == "4S 0B":
            return int(guess)

        # 모순되지 않는 후보만 남기기
        new_candidates = []
        for cand in candidates:
            if get_hint(cand, guess) == result:
                new_candidates.append(cand)
        candidates = new_candidates
    
    return 0
