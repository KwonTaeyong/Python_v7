import sys
sys.setrecursionlimit(10**7)

def solution(nodeinfo):
    # 1. 노드에 번호 붙이기
    nodes = []
    for i, (x, y) in enumerate(nodeinfo):
        nodes.append((i+1, x, y))
    
    # 2. y 내림차순, x 오름차순 정렬
    nodes.sort(key=lambda v: (-v[2], v[1]))  

    # 3. 트리 구성
    class Node:
        def __init__(self, idx, x, y):
            self.idx = idx
            self.x = x
            self.y = y
            self.left = None
            self.right = None

    root = Node(*nodes[0])

    # 노드 삽입 함수
    def insert(parent, child):
        if child[1] < parent.x:
            # 왼쪽
            if parent.left:
                insert(parent.left, child)
            else:
                parent.left = Node(*child)
        else:
            # 오른쪽
            if parent.right:
                insert(parent.right, child)
            else:
                parent.right = Node(*child)

    # 루트 외 노드 삽입
    for node in nodes[1:]:
        insert(root, node)

    # 4. 전위/후위 순회
    preorder_list = []
    postorder_list = []

    def preorder(node):
        if node:
            preorder_list.append(node.idx)
            preorder(node.left)
            preorder(node.right)

    def postorder(node):
        if node:
            postorder(node.left)
            postorder(node.right)
            postorder_list.append(node.idx)

    preorder(root)
    postorder(root)

    return [preorder_list, postorder_list]
