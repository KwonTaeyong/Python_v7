def rotate(matrix):
    # 시계 방향 90도 회전
    return list(zip(*matrix[::-1]))


def check(new_lock, n):
    # 중앙의 lock 부분이 모두 1인지 확인
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    m = len(key)
    n = len(lock)

    # 큰 자물쇠 (lock을 가운데에 배치)
    big_lock = [[0]*(n*3) for _ in range(n*3)]

    # lock을 중앙에 복사
    for i in range(n):
        for j in range(n):
            big_lock[i+n][j+n] = lock[i][j]

    # 키 회전 4번 시도
    for _ in range(4):
        key = rotate(key)

        # 이동 범위: (0 ~ 2n+m)
        for x in range(0, n*2 + 1):
            for y in range(0, n*2 + 1):

                # 1) key 삽입
                for i in range(m):
                    for j in range(m):
                        big_lock[x+i][y+j] += key[i][j]

                # 2) lock이 열리는지 확인
                if check(big_lock, n):
                    return True

                # 3) 원상 복구
                for i in range(m):
                    for j in range(m):
                        big_lock[x+i][y+j] -= key[i][j]

    return False
