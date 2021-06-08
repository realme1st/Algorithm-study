n,m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()

a=[0]*m

def go(index,selected,n,m):
    if selected ==m:
        print(" ".join(map(str,a)))
        return
    
    if index > n-1:
        return
    
    a[selected] = num[index]
    go(index,selected+1,n,m)
    go(index+1,selected,n,m)

go(0,0,n,m)