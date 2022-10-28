# 이것이 취업을 위한 코딩이다! -3. 구현
# 왕실의 나이트

# 내 답안
loc = input()
x, y = int(loc[1]), ord(loc[0])-96
cnt = 0
dx2 = [0, 0, 0, 0, -2, -2, 2, 2]
dy2 = [2, 2, -2, -2, 0, 0, 0, 0]
dx1 = [-1, 1, -1, 1, 0, 0, 0, 0]
dy1 = [0, 0, 0, 0, -1, 1, -1, 1]
print(x, y)
for i in range(len(dx1)):
    nx = x+dx2[i]
    ny = y+dy2[i]
    if nx>0 and nx<=8 and ny>0 and ny<=8:
        nx += dx1[i]
        ny += dy1[i]
        if nx>0 and nx<=8 and ny>0 and ny<=8:
            cnt+=1
            print("x: {0}+{1}+{2}={3} y: {4}+{5}+{6}={7}".format(x, dx2[i], dx1[i], nx, y, dy2[i], dy1[i], ny))
print(cnt)

# 모범 답안
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a'))+1 # 일반적으로 아스키 코드표의 dec을 외우고 있는 경우는 잘 없으므로 ord('a')를 통해 찾아주기

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] # 굳이 단계별로 진행 안해도 된다. 이동 후 위치 바로 찍어주기

result = 0
for step in steps:
    next_row = row+step[0]
    next_column = column+step[1]
    
    if next_row >= 1 and next_row<=8 and next_column >=1 and next_column <=8:
        result+=1
print(result)
