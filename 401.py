# 이것이 취업을 위한 코딩이다! - 3. 구현
# 상하좌우

# 내 답안
n = int(input())
plans = input().split()
x, y = 1, 1

for p in plans:
    if p=='L':
        if y-1!=0: y-=1
    elif p=='R':
        if y+1<n+1: y+=1
    elif p=='U':
        if x-1!=0: x-=1
    elif p=='D':
        if x+1<n+1: x+=1
    else:
        continue

print("{0} {1}".format(x, y))

# 모범 답안
n = int(input())
plans = input().split()
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range (len(move_types)):
        if plan == move_types[i]:
            nx = x+dx[i]
            ny = y+dy[i]
            
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print("{0} {1}".format(x, y))
