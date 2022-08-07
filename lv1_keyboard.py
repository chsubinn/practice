def solution(numbers, hand):
    answer = ''
    
    # 키패드 좌표료 변경
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    
    # 시작 위치
    left_s = dic['*']
    right_s = dic['#']
    
    for i in numbers:
        now = dic[i]
        # 1, 4, 7을 누르는 경우 무조건 왼손
        if i in [1, 4, 7]:
            answer += 'L'
            left_s = now
            
        # 3, 6, 9를 누르는 경우 무조건 오른손
        elif i in [3, 6, 9]:
            answer += 'R'
            right_s = now
            
        # 2, 5, 8, 0을 누르는 경우
        else:
            left_d = 0
            right_d = 0
            
            # 좌표 거리 계산해주기
            for a, b, c in zip(left_s, right_s, now):
                left_d += abs(a-c)
                right_d += abs(b-c)
            
            # 왼손이 더 가까운 경우
            if left_d < right_d:
                answer += 'L'
                left_s = now
                
            # 오른손이 더 가까운 경우
            elif left_d > right_d:
                answer += 'R'
                right_s = now
            
            # 두 거리가 같은 경우
            else:
                # 왼손잡이 경우
                if hand == 'left':
                    answer += 'L'
                    left_s = now
                    
                # 오른손잡이 경우
                else:
                    answer += 'R'
                    right_s = now
            
    return answer

#my solution

def get_dst (i, loc):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    x = loc//3
    y = loc%3
    for di, dj in dx, dy:
        if phone[x+dx][y+dy]==
        

def solution(numbers, hand):
    answer = ''
    phone = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 1]]
    left = 9, right = 11
    for i in numbers:
        if i==1, 4, 7: 
            answer+="L"
        elif i==3, 6, 9: 
            answer+="R"
            phone[right]=0, phone[i-1]=1
            right = i-1
        else:
            left_dst = get_dst(i, left, phone)
            right_dst = get_dst(i, right, phone)
            if left_dst > right_dst: 
                answer+="R"
                phone[right]=0, phone[i-1]=1
                right=i-1
            elif left_dst<right_dst:
                answer+="L"
                phone[left]=0, phone[i-1]=1
                left = i-1
            else:
                answer+= "R" if hand=="right" else "L"
    return answer
