n=int(input())

data=list(map(int,input().split()))

data.sort()

result=0
temp=0
for i in data:
    temp+=i
    result+=temp

print(result)