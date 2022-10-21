
# 초안 - 시간 초과 ^^
def solution(food_times, k):
    answer = 0
    time = 0
    n = len(food_times)
    
    while (time!=k): # 직접 food_times를 돌면서 먹방 시간을 뺴준다.
        for i in range (n):
            if food_times[i]!=0:
                food_times[i]-=1
            else:
                continue
            answer = i+1
            print("time: {0}, i: {1}, food_times: {2}, answer: {3}".format(time, i, food_times, answer))
            time+=1
        
    answer += 1
    if answer > n:
        answer -= n
    
    return answer

# 답안
import heapq

def solution(food_times, k):
    if sum(food_times)<=k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1)) # (먹는 시간, 음식 번호) 형태로 힙에 삽입

    sum_value = 0
    previous = 0
    length = len(food_times)
    
    while sum_value+((q[0][0]- previous)*length) <= k: 
        now = heapq.heappop(q)[0]
        print("before>>>sum_value: {0}, length: {1}, previous: {2}, now: {3}".format(sum_value, length, previous, now))
        sum_value+=(now-previous) * length
        length -= 1
        previous = now
        print("after>>>sum_value: {0}, length: {1}, previous: {2}, now: {3}".format(sum_value, length, previous, now))
    
    result = sorted(q, key =lambda x: x[1]) # 음식 번호 기준으로 정렬
    return result[(k-sum_value)%length][1]




