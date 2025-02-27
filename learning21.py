def solution(board):
    # O와 X의 개수를 셈
    countO = 0
    countX = 0
    
    # 가로, 세로, 대각선 승리 여부 확인
    def check_win(player):
        # 가로, 세로, 대각선에 대해 승리 조건 확인
        for i in range(3):
            if board[i][0] == player and board[i][1] == player and board[i][2] == player:
                return True
            if board[0][i] == player and board[1][i] == player and board[2][i] == player:
                return True
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return True
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return True
        return False

    # "O"와 "X"의 개수를 셈
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                countO += 1
            elif board[i][j] == 'X':
                countX += 1

    # "O"와 "X"의 개수 차이가 1을 초과하면 안 됨
    if countO > countX + 1 or countX > countO:
        return 0

    # "O"와 "X"의 승리 여부 확인
    winO = check_win('O')
    winX = check_win('X')

    # "O"가 이겼을 때는 "X"는 이길 수 없음
    # "X"가 이겼을 때는 "O"는 이길 수 없음
    if winO and countO != countX:
        return 0
    if winX and countO != countX + 1:
        return 0

    # "O"와 "X"가 동시에 이길 수 없음
    if winO and winX:
        return 0

    # 모든 규칙을 만족하면 정상적인 게임 상태
    return 1
