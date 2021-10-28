n=int(input())

arr=[]
for i in range(n):
    a,b=map(int,input().split())
    arr.append((a,b))

arr.sort(key=lambda x: (x[1],x[0]))

count=1

prev=arr[0][1]

for sch in arr[1:]:
    if prev <=sch[0]:
        prev=sch[1]
        count+=1

print(count)