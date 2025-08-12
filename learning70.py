MOD = 1_000_000_007

from functools import lru_cache

def count_c_ways(b):
    """
    정의 그대로의 과정으로 가능한 서로 다른 c 배열의 '개수'를 센다 (mod MOD).
    - 스택엔 '블록 합'만 저장.
    - i를 0..n-1로 진행하며, 현재 i가 포함된 블록 X(항상 스택 맨 오른쪽)과
      왼쪽 블록 Y의 합이 같으면 (합치기 / 그냥 진행) 두 가지 분기.
    - 합치면 c에 i가 추가되지만, 우리는 '개수'만 세므로 i 자체를 담을 필요는 없음.
      (분기 수만 정확히 카운트하면 됨)
    """
    n = len(b)

    @lru_cache(maxsize=None)
    def dfs(i, stack):
        # stack: tuple of block sums (왼->오)
        if i == n:
            return 1  # 모든 i 처리 완료 → c 하나 완성

        # 보장: 현재 i는 항상 stack의 '마지막 블록'(우측 끝)에 들어 있음.
        # 그러나 i가 현재 어떤 블록에 있는지 추적을 안 했는데?
        # 트릭: "항상 새 원소를 넣고 시작"으로 모델링.
        # 이유: 문제 절차에서 'i 증가' 시 X는 b[i]를 포함하는 새 블록이 되므로,
        #       dfs의 한 step은 "새 원소 b[i]를 오른쪽에 추가한 뒤, 같은 합이면 합칠지 분기"로 볼 수 있다.
        if not stack or (len(stack) > 0 and (True)):
            # 새 b[i]로 블록 추가
            stack = stack + (b[i],)

        # 이제 while 가능: (왼쪽 이웃과 합이 같으면) 합치거나/그냥 진행
        # 단, "그냥 진행"을 택하는 순간 i를 증가시키고 그 상태로 넘어가므로,
        # 여기서는 '합칠 수 있는 시점'마다 두 갈래:
        #   - stop: i+1로 넘어감
        #   - merge: 두 블록 합치고(오른쪽에 i 유지), 다시 같은 체크 반복
        # 반복적 분기가 있는 구조라 재귀로 처리
        res = 0

        # 내부 재귀: 현재 스택 상태에서 "추가 merge를 계속할지/멈출지" 분기
        def branch(cur_stack):
            nonlocal res, i
            # 현재 상태에서 '멈추면' i를 1 올려 다음으로 진행
            res_stop = dfs(i + 1, cur_stack) % MOD

            # '멈추지 않고' 합칠 수 있으면: merge한 뒤 다시 같은 분기
            res_merge = 0
            if len(cur_stack) >= 2 and cur_stack[-1] == cur_stack[-2]:
                merged = cur_stack[:-2] + (cur_stack[-1] + cur_stack[-2],)
                # merge를 했으니 여전히 현재 i가 포함된 블록이 오른쪽 끝이며,
                # 다시 같은 조건으로 합칠지/멈출지 분기
                # (주의: 여러 번 연쇄로 합칠 수 있음)
                # 여기서도 '멈추기' 선택은 다음 dfs(i+1, …) 호출에 반영됨.
                # 따라서 res_merge는 branch(merged) 결과 자체.
                res_merge = branch(merged) % MOD

            return (res_stop + res_merge) % MOD

        res = branch(stack) % MOD
        return res

    return dfs(0, tuple()) % MOD


def solution(a, s):
    ans = []
    idx = 0
    for length in s:
        b = a[idx:idx+length]
        idx += length
        ans.append(count_c_ways(b))
    return ans


# ---- 예시 테스트 ----
if __name__ == "__main__":
    a = [1,1,1,1,1,1,2,5,8,2,1,1,4,8,8,8,12,6,6]
    s = [4,3,1,5,6]
    print(solution(a, s))  # 기대: [6,3,1,5,9]

    # 추가 간단 검증
    print(count_c_ways([1,1,1,1]))  # 6
    print(count_c_ways([1,1,2]))    # 3
    print(count_c_ways([5]))        # 1
