#########################
# 문자열 내 p와 y의 개수 #
#########################

def solution(s):
    return s.lower().count('p') == s.lower().count('y')


#my solution
def solution(s):
    answer = True
    s = s.upper()
    p = 0
    y = 0
    for c in s:
        if c=='P': p+=1
        if c=='Y': y+=1
    
    if p==y: return True
    else: return False
    
