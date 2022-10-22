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
