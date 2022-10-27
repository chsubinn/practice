# 이것이 취업을 위한 코딩테스트다! -3. 구현
# 뱀

# 내 답안 - 뱀의 머리 정보만 있어서 틀림
n = int(input())
k = int(input())
data = [[0]*(n+1) for _ in range(n+1)] # 맵 생성
info = [] # 방향 전환 정보 저장

for _ in range(k): # 사과
    a, b = map(int, input().split())
    data[a][b]=2
l = int(input())
for _ in range(l): # 방향 전환
    x, c = input().split()
    info.append((int(x), c))
    
cnt = 0
dir = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 1, 1
data[x][y] = 1

while True:
    if cnt==info[0][0] and info[0][1]=='D':
        dir=(dir+1)%4
        info.pop(0)
    if cnt==info[0][0] and info[0][1]=='L':
        dir=(dir-1)%4
        info.pop(0)
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx>0 and ny>0 and nx<n+1 and ny<n+1 and data[nx][ny]!=1:
        if data[nx][ny]!=2:
            data[x][y]=0
        data[nx][ny]=1
        x, y = nx, ny
    else:
        cnt+=1
        break
print(cnt)
        
# 모범 답안






