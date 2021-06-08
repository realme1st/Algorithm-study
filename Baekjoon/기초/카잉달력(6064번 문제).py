T = int(input())

for _ in range(T):
    M,N,x,y = map(int,input().split())
    x-=1
    y-=1
    k = x # 더 빠르게 하기 위함
    while k < N*M:
        if k%N == y:
            print(k+1)
            break
        k +=M
    else:
        print(-1)
