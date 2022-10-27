# 이것이 취업을 위한 알고리즘이다! -3. 구현
# 문자열 압축

# 내 답안
def solution(s):
    answer = ''
    min = 1000
    for i in range (1, len(s)//2+1):
        sum=0
        for j in range (len(s)//i+1):
            if s[j*i:(j+1)*i]==s[(j+1)*i: (j+2)*i]:
                sum += 2
            else:
                if sum > 1:
                    answer+=str(sum)
                answer+=s[j*i:(j+1)*i]
                sum=0
        if len(answer) < min:
            min = len(answer)
        answer=''
    return min
  
# 모범 답안
def solution(s):
    answer = len(s)
    for step in range (1, len(s)//2+1):
        compressed=""
        prev = s[0:step]
        count=1
        for j in range (step, len(s), step): # step만큼 증가시키며 이전 문자열과 비교
            if prev == s[j:j+step]:
                count+=1
            else:
                compressed += str(count)+prev if count>=2 else prev
                prev = s[j:j+step]
                count=1
        compressed += str(count)+prev if count>=2 else prev
        answer = min(answer, len(compressed))
    return
  
