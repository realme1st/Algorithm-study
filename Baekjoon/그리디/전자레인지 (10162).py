t=int(input())

a=300
b=60
c=10

time=[a,b,c]
result=[]

for sec in time:
    ans=0
    ans+=t//sec
    t%=sec
    result.append(ans)

if t==0:
    print(*result)
else:
    print(-1)

    
    
