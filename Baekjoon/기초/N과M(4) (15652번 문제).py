n,m=map(int,input().split())

a=[0]*m

def go(index,selected,n,m):
    if selected ==m:
        print(" ".join(map(str,a)))
        return
    
    if index >n:
        return

    a[selected]=index
    go(index,selected+1,n,m)

    go(index+1,selected,n,m)
go(1,0,n,m)

