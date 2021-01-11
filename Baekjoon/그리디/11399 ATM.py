n= int(input())

time = list(map(int,input().split()))

time.sort()

result =0
pre=0;
for i in time:
    pre+=i
    result+=pre

print(result)
    