# 이것이 취업을 위한 알고리즘이다! -3. 구현
# 게임 개발

# 내 답안
n, m = map(int, input().split())
x, y, direction = map(int, input().split())
space = []
for i in range(n):
    space.append(list(map(int, input().split())))
    
space[x][y]=1
cnt = 1
time_cnt = 0

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

while True:
    nx = x+dx[direction]
    ny = y+dy[direction]
    if space[nx][ny]==0:
        x, y = nx, ny
        space[nx][ny]=1
        cnt+=1
        direction = (direction+1)%4
        time_cnt=0
    else:
        direction = (direction+1)%4
        time_cnt+=1
    if time_cnt==4: break
    print(space, direction)
print(cnt)

# 모범 답안 - 근데 내 코드가 더 이쁜 것 같음
n, m = map(int, input().split())
d = [[0]*m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1
array = []
for i in range(n):
    arrary.append(list(map(int, input().split())))
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -=1
    if direction == -1: direction = 3

cnt = 1
turn_time = 0
while True:
    turn_left()
    nx = x+dx[direction]
    ny = y+dy[direction]
    
    if d[nx][ny]==0 and array[nx][ny]==0:
        d[nx][ny]=1
        x = nx
        y = ny
        cnt+=1
        turn_time=0
        continue
    else: turn_time +=1
    
    if turn_time==4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny]==0: # 뒤로 갈 수 있다면 이동하기 - 그래도 이동할 수 없으면 탈출
            x = nx
            y = ny
        else:
            break
        turn_time=0
print(cnt)
