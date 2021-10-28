import sys
t= int(input())



for _ in range(t):
    data=[]
    count=1
    n=int(input())
    for i in range(n):
        a,b=map(int,sys.stdin.readline().split())
        data.append((a,b))

    data.sort(key=lambda x: x[0])
    
    min_data=data[0][1]
    for i in data[1:]:
        if min_data>i[1]:
            count+=1
            min_data=i[1]

    print(count)