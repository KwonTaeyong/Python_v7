import sys
sys.setrecursionlimit(10**7)

class Node:
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.idx = idx
        self.left = None
        self.right = None

def insert(parent, child):
    if child.x < parent.x:
        if parent.left is None:
            parent.left = child
        else:
            insert(parent.left, child)
    else:
        if parent.right is None:
            parent.right = child
        else:
            insert(parent.right, child)

def preorder(node, result):
    if not node:
        return
    result.append(node.idx)
    preorder(node.left, result)
    preorder(node.right, result)

def postorder(node, result):
    if not node:
        return
    postorder(node.left, result)
    postorder(node.right, result)
    result.append(node.idx)

def solution(nodeinfo):
    nodes = []
    for i, (x, y) in enumerate(nodeinfo):
        nodes.append(Node(x, y, i + 1))

    # y 내림차순, x 오름차순 정렬
    nodes.sort(key=lambda n: (-n.y, n.x))

    root = nodes[0]

    for node in nodes[1:]:
        insert(root, node)

    pre = []
    post = []

    preorder(root, pre)
    postorder(root, post)

    return [pre, post]
