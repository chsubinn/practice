# 이것이 코딩테스트다 -1.그리디 알고리즘
# 볼링공 고르기

# my solution
n, m = map(int, input().split())
balls = list(map(int, input().split()))

#전체 경우의 수 세기
result = 0
cnt = n - 1
while cnt > 0:
    result += cnt
    cnt -= 1

#무게가 같은 경우 전체 경우의 수에서 제외
for i in range (n-1):
    for j in range (i+1, n):
        if balls[i]==balls[j] and i!=j:
            result-=1
        print("({0}, {1}) -> result: {2}".format(i+1, j+1, result))

print(result)
