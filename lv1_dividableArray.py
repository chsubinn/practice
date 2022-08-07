######################################
# 프로그래머스 lv1 나누어떨어지는 배열 #
#####################################

def solution(arr, divisor): 
    return sorted([n for n in arr if n%divisor == 0]) or [-1]


#my solution
def solution(arr, divisor):
    answer = []
    arr.sort()
    for a in arr:
        if a%divisor == 0:
            answer.append(a)
            
    if not answer: answer.append(-1)
    return answer
