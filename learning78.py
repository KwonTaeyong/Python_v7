from collections import deque
import math

def solution(board):
    n = len(board)
    # 방향: 상, 하, 좌, 우
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    # 각 좌표(y,x), 각 방향별 최소비용
    cost = [[[math.inf]*4 for _ in range(n)] for _ in range(n)]
    
    q = deque()
    
    # 시작점 (0,0)에서 우측, 하향 두 가지 방향 시작
    for d in [1,3]:  # 하(1), 우(3)
        cost[0][0][d] = 0
        q.append((0,0,d,0))  # y,x,방향,비용
    
    answer = math.inf
    
    while q:
        y,x,d,c = q.popleft()
        
        # 목적지 도착
        if (y,x) == (n-1,n-1):
            answer = min(answer, c)
            continue
        
        for nd, (dy,dx) in enumerate(directions):
            ny, nx = y+dy, x+dx
            if 0<=ny<n and 0<=nx<n and board[ny][nx] == 0:
                # 비용 계산
                if nd == d:  # 직선
                    nc = c + 100
                else:        # 코너
                    nc = c + 600
                
                if cost[ny][nx][nd] > nc:
                    cost[ny][nx][nd] = nc
                    q.append((ny,nx,nd,nc))
    
    return answer
