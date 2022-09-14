# 이것이 코딩테스트다 - 1.그리디 알고리즘
# 모험가 길드

# my solution
n = int(input())
people = list(map(int, input().split()))

people.sort()
result = 0

while n != 0:
    cnt = people[-1]
    if n < cnt :
        result += 0
    else:
        result += 1
        n -= cnt
        for i in range (cnt):
            people.pop()

print(result)
