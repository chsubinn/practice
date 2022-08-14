n = int(input())
arr = list(map(int, input().split())) 
min = 10000
for i in range(n):
  if (arr[i]<min):
    min=arr[i]

print(min)
