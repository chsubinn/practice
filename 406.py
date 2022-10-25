# 이것이 취업을 위한 알고리즘이다! -3. 구현
# 문자열 재정렬

# 내 답안
str = input()
sum = 0
answer = ''
for s in str:
    if ord(s) >= ord('A') and ord(s) <= ord('Z'):
        answer += s
    else:
        sum += int(s)

answer=sorted(answer)
answer=''.join(sorted(answer))	
print(answer+'{0}'.format(sum))

# 모범 답안
