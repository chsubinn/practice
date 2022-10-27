# 이것이 취업을 위한 코딩 테스트다! -3. 구현
# 자물쇠와 열쇠

# 모범 답안
def rotate_a_matrix_by_90_degree(a):
    n = len(a) #행
    m = len(a[0]) #열
    result = [[0] * n for _ in range (m)] # (n, m)에서 (m, n)으로 변경
    for i in range(n):
        for j in range(m):
            result[j][n-i-1]=a[i][j]
    return result

def check(new_lock):
    lock_length = len(new_lock)//3
    for i in range(lock_length, lock_length * 2): 
        # new_lock의 중간만 확인하기 위한 범위 설정
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j]!=1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0]*(n*3) for _ in range(n*3)] # 배열 생성
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
            
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        for x in range(n*2): 
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock)==True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]-=key[i][j]
    return False
