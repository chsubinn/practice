##############################
#  프로그래머스 lv1 모의고사   #
##############################
#solution
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
    
#my solution
def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5] #5
    two = [2, 1, 2, 3, 2, 4, 2, 5] #8
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] #10
    score = [0, 0, 0]
    
    #enumerate를 쓰면 cnt를 따로 할 필요없이 answers에서 바로 index를 뽑아낼 수 있다. 또, 직접 list의 길이를 넣지말고 len(list) 함수 활용
    cnt = 0
    for ans in answers:
        if (ans == one[cnt%5]): score[0]+=1
        if (ans == two[cnt%8]): score[1]+=1
        if (ans == three[cnt%10]): score[2]+=1
        cnt+=1
        
    cnt = 0
    for s in score:
        if (s==max(score)):
            cnt+=1
            answer.append(cnt)
    return answer
