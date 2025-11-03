from itertools import permutations

def solution(n, submit):
    # 1. 가능한 모든 비밀번호 후보 (1~9, 서로 다른 4자리)
    candidates = [''.join(p) for p in permutations('123456789', 4)]
    
    def get_hint(secret, guess):
        s = sum(a == b for a, b in zip(secret, guess))
        b = sum(min(secret.count(x), guess.count(x)) for x in secret) - s
        return f"{s}S {b}B"
    
    while True:
        # 2. 후보 중 하나를 선택 (여기선 단순히 첫 번째)
        guess = candidates[0]
        result = submit(int(guess))
        if result == "4S 0B":
            return int(guess)
        
        # 3. 필터링
        new_candidates = []
        for cand in candidates:
            if get_hint(cand, guess) == result:
                new_candidates.append(cand)
        candidates = new_candidates
        
        # 4. 남은 후보가 1개면 종료
        if len(candidates) == 1:
            return int(candidates[0])
