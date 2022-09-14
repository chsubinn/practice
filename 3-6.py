# 이것이 코딩테스트다 - 1.그리디 알고리즘
# 곱하기 혹은 더하기

# my solution
S = input()
result = 1

for ch in S:
    if ch == '0': continue
    result *= int(ch)
print(result)
