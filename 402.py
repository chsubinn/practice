# 이것이 취업을 위한 코딩이다 ! - 3. 구현
# 시각

# 내 답안
n = int(input())
answer = 0
H, M, S = 23, 59, 59

for h in range(n + 1):
    for m in range(M+1):
        for s in range(S+1):
            if h==n or m==n or s==n or h%10==n or h//10==n or m%10==n or m//10==n or s%10==n or s//10==n: # 하수
                answer+=1
print(answer)


# 모범 답안
h = int(input())
count = 0

for i in range (h+1):
    for j in range (60):
        for k in range (60):
            if str(h) in str(i)+str(j)+str(k): # 천재
                count +=1    
print(count)
