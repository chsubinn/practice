# 이것이 코딩테스트다 -1.그리디 알고리즘
# 만들 수 없는 금액

# my solution
n = int(input())
coins = list(map(int, input().split()))

coins.sort()
if coins[0]-1 != 0 and coins[0]-1 not in coins:
    result = coins[0]-1
    
else:
    cnt = 0
    for c in coins:
       if c==coins[-1]: break
       cnt += c
    if cnt < coins[-1]-1 and coins[-1]-1 not in coins:
        result = coins[-1]-1
    
print(result)
