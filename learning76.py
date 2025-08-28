from bisect import bisect_left, bisect_right

def count_by_range(words, left, right):
    return bisect_right(words, right) - bisect_left(words, left)

def solution(words, queries):
    answer = []
    
    # 길이별로 단어 분류
    word_dict = {}
    reversed_dict = {}
    
    for word in words:
        l = len(word)
        if l not in word_dict:
            word_dict[l] = []
            reversed_dict[l] = []
        word_dict[l].append(word)
        reversed_dict[l].append(word[::-1])
    
    # 정렬
    for l in word_dict:
        word_dict[l].sort()
        reversed_dict[l].sort()
    
    # 쿼리 처리
    for q in queries:
        l = len(q)
        if l not in word_dict:
            answer.append(0)
            continue
        
        if q[0] != '?':  # 접미사가 '?'
            left = q.replace('?', 'a')
            right = q.replace('?', 'z')
            res = count_by_range(word_dict[l], left, right)
        else:  # 접두사가 '?'
            rq = q[::-1]
            left = rq.replace('?', 'a')
            right = rq.replace('?', 'z')
            res = count_by_range(reversed_dict[l], left, right)
        
        answer.append(res)
    
    return answer
