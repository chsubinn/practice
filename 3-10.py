
# 초안
def solution(food_times, k):
    answer = 0
    time = 0
    n = len(food_times)
    mod = 0
    
    while time != k:
        while True:
            if food_times[(time+mod)%n] == 0: 
                mod += 1
            else: break
        
        food_times[(time+mod)%n] -= 1
        time += 1
        print("time: {0}, mod: {1}, total: {2}".format(time, mod, time+mod))
        print(food_times)
        
    if food_times[(time+mod)%n]==0:answer=(time+mod)%n+2
    else: answer = (time+mod)%n+1
    
    return answer
