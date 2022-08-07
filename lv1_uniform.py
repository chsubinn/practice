 ##########################
 # 프로그래머스 lv1 체육복 #
 #########################
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    _reserve = [r for r in reserve if r not in lost] #lost랑 reserve에 중복되어있는 것을 제외하고 다시 저장한다.
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

# my solution - test case 17-20 통과 못함
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    answer = 0
    students = {}
    for i in range(1, n+1):
        if i in lost: students[i]=0
        else: students[i]=1
        if i in reserve: students[i]=2
    for i in lost:
        for j in reserve:
            if (j+1==i or j-1==i) and students[j]>1: 
                students[i]+=1
                students[j]-=1
    for i in students:
        if students[i]>0: answer+=1

    return answer
