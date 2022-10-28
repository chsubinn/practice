# 이것이 취업을 위한 코딩테스트다! -3. 구현
# 외벽 점검

# 모범 답안
def solution(n, weak, dist):
    # 원형을 배열로 변형-두 배 크기의 배열
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n) 
    
    answer = len(dist)+1 # 최솟값과 비교하기 위해
    for start in range(length):
        for friends in list(permutations(dist, len(dist))): # 순열 
            count = 1 # 투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start]+friends[count-1]
            for index in range(start, start + length):
                #점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]: 
                    count += 1
                    if count>len(dist):
                        break
                    position = weak[index] + friends[count-1]
            answer = min(answer, count)
        if answer > len(dist):
            return -1
        return answer
