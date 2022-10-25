# 이것이 취업을 위한 알고리즘이다! -3. 구현
# 럭키 스트레이트

# 내 답안
n = input()
sum = 0

for i in range(len(n)):
    if i < len(n)/2:
        sum += int(n[i])
    else:
        sum -= int(n[i])
        
if sum==0:
    print("LUCKY")
else:
    print("READY")
    
# 모범 답안
