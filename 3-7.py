# 이것이 코딩테스트다 -1. 그리디 알고리즘
# 문자열 뒤집기

# my solution
S = input()

if S[0]=="0": result = S.count("01")
else: result = S.count("10")
    
print(result)

