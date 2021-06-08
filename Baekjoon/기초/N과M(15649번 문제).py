n,m = map(int,input().split())#n까지 m개

c = [False]*(n+1) # c[i]: i를 사용했으면 True

a = [0] *m #a: 고른 수열을 저장

def go(index,n,m):
    if index == m:
        print(" ".join(map(str,a)))
        return
    for i in range(1,n+1):
        if c[i]:
            continue
        c[i] = True
        a[index] = i
        go(index+1,n,m)
        c[i] = False

go(0,n,m)

#go 함수 index번째 수를 결정