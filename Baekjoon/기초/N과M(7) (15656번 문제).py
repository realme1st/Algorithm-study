n,m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()

a=[0]*m

def go(index,n,m):
    if index ==m:
        print(" ".join(map(str,a)))
        return
    
    for i in range(n):
        a[index] =num[i]
        go(index+1,n,m)

go(0,n,m)