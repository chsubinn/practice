#####################################
# 프로그래머스 lv1 완주하지 못한 선수 #
#####################################
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion): #zip 내장함수를 사용하면 participant, completion의 내용물이 (p, c) 형태로 만들어진다
        if p != c:
            return p
    return participant[-1]

# my solution
def solution(participant, completion):
    answer = ''
    check = {} #dictionary
    for p in participant:
        check[p] = 0
    for c in completion: 
        check[c] += 1
    for p in participant: #동명이인들이 완주를 못한 경우에는 check에 표시되는 값이 음수가 된다.
        check[p] -= 1
    for ch in check:
        if check[ch]!=0: answer = ch
    return answer

# zero Efficienty 
def solution(participant, completion):
    answer = ''
    for i in completion:
        participant.remove(i)
    answer = participant[0]
    return answer
