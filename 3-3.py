# 이것이 코딩테스트다 - 1.그리디 알고리즘
# 숫자 카드 게임

# my solution
n, m = map(int, input().split())
values = []

for i in range(n):
    data = list(map(int, input().split()))
    values.append(min(data))

print(max(values))

# simple solution 1 : 위 방법에서 새로운 리스트를 정의하지 않고 내장 함수를 사용하는 방법
n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    result = max(result, min(data)) # max 함수와 min 함수의 다양한 표현: min(자료형), min(변수, 변수)

print(result)

# simple solution 2 : 2중 반복문 구조를 이용하면 min(자료형) 대신 min(변수, 변수) 형태를 이용하여 이중으로 탐색한다
