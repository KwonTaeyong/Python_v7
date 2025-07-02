from collections import defaultdict
import bisect

def solution(words, queries):
    # 단어 길이별로 분리하여 정방향/역방향 리스트 저장
    word_dict = defaultdict(list)
    reversed_dict = defaultdict(list)

    for word in words:
        word_dict[len(word)].append(word)
        reversed_dict[len(word)].append(word[::-1])

    # 단어 사전 정렬 (이진 탐색용)
    for length in word_dict:
        word_dict[length].sort()
        reversed_dict[length].sort()

    result = []

    for q in queries:
        length = len(q)
        if q[0] != '?':
            # 접두사 검색: fro??
            prefix = q.replace('?', '')
            left = bisect.bisect_left(word_dict[length], prefix + 'a' * (length - len(prefix)))
            right = bisect.bisect_right(word_dict[length], prefix + 'z' * (length - len(prefix)))
            result.append(right - left)
        else:
            # 접미사 검색: ??odo → odo??
            rev_q = q[::-1]
            prefix = rev_q.replace('?', '')
            left = bisect.bisect_left(reversed_dict[length], prefix + 'a' * (length - len(prefix)))
            right = bisect.bisect_right(reversed_dict[length], prefix + 'z' * (length - len(prefix)))
            result.append(right - left)

    return result
