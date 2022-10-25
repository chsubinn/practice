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
  
