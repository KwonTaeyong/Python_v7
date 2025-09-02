def rotate(key):
    """열쇠를 시계 방향으로 90도 회전"""
    M = len(key)
    return [[key[M - j - 1][i] for j in range(M)] for i in range(M)]

def check(new_lock, M, N):
    """자물쇠 중앙 영역이 모두 1인지 확인"""
    for i in range(N):
        for j in range(N):
            if new_lock[M-1+i][M-1+j] != 1:
                return False
    return True

def solution(key, lock):
    M = len(key)
    N = len(lock)

    # 자물쇠 확장 (M-1 만큼 패딩)
    new_size = N + 2*(M-1)
    new_lock = [[0]*new_size for _ in range(new_size)]

    # 중앙에 lock 배치
    for i in range(N):
        for j in range(N):
            new_lock[M-1+i][M-1+j] = lock[i][j]

    # key를 4번 회전하면서 모든 위치 확인
    for _ in range(4):
        key = rotate(key)
        for x in range(new_size - M + 1):
            for y in range(new_size - M + 1):
                # key 덮어쓰기
                for i in range(M):
                    for j in range(M):
                        new_lock[x+i][y+j] += key[i][j]

                if check(new_lock, M, N):
                    return True

                # 다시 원래대로 복구
                for i in range(M):
                    for j in range(M):
                        new_lock[x+i][y+j] -= key[i][j]

    return False
