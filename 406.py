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
data = input()
result = []
value = 0

for x in data:
    if x.isalpha(): # 알파벳인지 확인: isalpha(), 숫자인지 확인: isdigit()
        result.append(x)
    else:
        value += int(x)
        
result.sort()
if value!=0:
    result.append(str(value)) # 리스트로 처리하면 문자열로 처리하는 것보다 간단하다.
print(''.join(result)) # 리스트에 있는 것 '' 로 합쳐서 출력
