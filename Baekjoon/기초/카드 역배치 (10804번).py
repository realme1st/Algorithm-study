n=[i for i in range(1,21)]

for i in range(10):
    a,b=map(int,input().split())
    
    temp=n[a-1:b]
    
    temp.reverse()
    
    n[a-1:b]=temp

print(*n)