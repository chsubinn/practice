# 이것이 취업을 위한 코딩테스트다! -3. 구현
# 치킨 거리

# 내 답안: 3, 4번 케이스 실패
n, m = map(int,input().split())
city = [list(map(int, input().split())) for _ in range(n)] # 2차원 배열 입력 받는 코드 
house = []
chicken = []
for i in range(n):# map 돌면서 집과 치킨집의 위치 정보 저장
    for j in range(n):
        if city[i][j]==1:
            house.append((i, j))
        if city[i][j]==2:
            chicken.append([i, j])
            
if m < len(chicken):
    minimum=101
    for j in range (len(chicken)):
        for i in range (len(house)):
            dist = abs(house[i][0] - chicken[j][0])+abs(house[i][1]-chicken[j][1])
            minimum = min(dist,minimum)
        chicken[j].append(minimum)
    chicken = sorted(chicken, key=lambda ch: ch[2]) # 세 번째 항목 기준으로 오름차순 배열
    print(chicken)
    for k in range (len(chicken)-m):
        chicken.pop()
        print(chicken)
        
chic_dist = 0
for i in range (len(house)):# 각 집에 대해 치킨집들의 거리 측정
    minimum=101
    for j in range (len(chicken)):
        dist = abs(house[i][0] - chicken[j][0])+abs(house[i][1]-chicken[j][1])
        minimum = min(dist,minimum)
    chic_dist += minimum
print(chic_dist)



# 모범 답안: Combination 라이브러리 사용
from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c]==1:
            house.append((r,c))
        if data[c]==2:
            house.append((r,c))
candidates = list(combinataions(chicken, m))

def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx)+abs(hy-cy))
        result += temp
    return result
result = 1e9
for candiddate in candidates:
    result = min(result, get_su(candidate))
print(result)
        
