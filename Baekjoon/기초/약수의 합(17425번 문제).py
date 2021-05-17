t= int(input())

for i in range(t):
    ans=0
    n = int(input())
    for i in range(1,n+1):
        ans += i*(n//i)
    
    print(ans)
