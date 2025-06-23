class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

def solution(words):
    root = TrieNode()

    # 1. Trie에 단어 삽입
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1

    # 2. 각 단어별로 입력해야 할 최소 글자 수 계산
    answer = 0
    for word in words:
        node = root
        for i, char in enumerate(word):
            node = node.children[char]
            if node.count == 1:
                answer += i + 1
                break
        else:
            # 끝까지 가도 count == 1이 없으면 전체 입력
            answer += len(word)
    
    return answer
