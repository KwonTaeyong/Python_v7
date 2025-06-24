from bisect import bisect_left, bisect_right

def count_by_range(words, left, right):
    return bisect_right(words, right) - bisect_left(words, left)

def solution(words, queries):
    answer = []
    
    # 길이별로 나누고 정렬
    word_dict = {}
    reversed_dict = {}
    
    for word in words:
        l = len(word)
        word_dict.setdefault(l, []).append(word)
        reversed_dict.setdefault(l, []).append(word[::-1])
    
    for l in word_dict:
        word_dict[l].sort()
        reversed_dict[l].sort()
    
    for query in queries:
        l = len(query)
        
        if query[0] != '?':  # 접미사 '?', 예: fro??
            left = query.replace('?', 'a')
            right = query.replace('?', 'z')
            answer.append(count_by_range(word_dict.get(l, []), left, right))
        else:  # 접두사 '?', 예: ???do -> od???
            reversed_query = query[::-1]
            left = reversed_query.replace('?', 'a')
            right = reversed_query.replace('?', 'z')
            answer.append(count_by_range(reversed_dict.get(l, []), left, right))
    
    return answer
