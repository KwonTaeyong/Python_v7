def solution(n, control):
    for c in control:
        if c == 'w':
            n += 1
        elif c == 's':
            n -= 1
        elif c == 'd':
            n += 10
        elif c == 'a':
            n -= 10
    return n

def solution(n, control):
    move = {'w': 1, 's': -1, 'd': 10, 'a': -10}
    return n + sum(move[c] for c in control)
