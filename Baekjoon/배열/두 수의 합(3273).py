n=int(input())

b=list(map(int,input().split()))

x=int(input())

cnt=0

for i in b:
    if x-i in b:
        cnt+=1

print(cnt//2)