def solution(board):
    # 보드를 문자열 배열로 받기 때문에 편하게 합친다.
    flat = "".join(board)
    cntO = flat.count('O')
    cntX = flat.count('X')
    
    # 1) 개수 규칙 위반
    if not (cntO == cntX or cntO == cntX + 1):
        return 0
    
    # 2) 승리 확인 함수
    def win(player):
        b = board
        # 가로
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] == player:
                return True
        # 세로
        for j in range(3):
            if b[0][j] == b[1][j] == b[2][j] == player:
                return True
        # 대각선
        if b[0][0] == b[1][1] == b[2][2] == player:
            return True
        if b[0][2] == b[1][1] == b[2][0] == player:
            return True
        return False
    
    O_win = win('O')
    X_win = win('X')
    
    # 3) 둘 다 이기는 경우 → 불가능
    if O_win and X_win:
        return 0
    
    # O가 이겼으면 O가 X보다 정확히 1개 많아야 함
    if O_win and cntO != cntX + 1:
        return 0
    
    # X가 이겼으면 O와 X 개수가 같아야 함
    if X_win and cntO != cntX:
        return 0
    
    # 모든 규칙을 통과한 경우
    return 1
