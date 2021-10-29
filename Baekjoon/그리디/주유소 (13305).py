n=int(input())

dist=list(map(int,input().split()))

cost=list(map(int,input().split()))

dist_cost=0

result=0
temp=0
for i in range(len(cost)-1):
    if cost[temp]<=cost[i+1]:
        dist_cost=dist[i]
        result+=cost[temp]*dist_cost
    else:
        
        dist_cost=dist[i]
        
        result+=cost[temp]*dist_cost
        temp=i+1
        
        

print(result)



    
