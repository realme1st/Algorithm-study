n,k = map(int,input().split())

result=0

while True:
    if n%k !=0:
        if n==1:
            break
        n-=1
        result+=1
    else:
        if n==1:
            break
        n /=k
        result+=1

print(result)