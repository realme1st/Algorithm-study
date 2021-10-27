n,k=map(int,input().split())

coin=[int(input()) for i in range(n)]

count=0

coin.sort(reverse=True)

while True:
    for i in coin:
        if k<i:
            continue
        count+=k//i
        k%=i

    if k==0:
        break
print(count)
