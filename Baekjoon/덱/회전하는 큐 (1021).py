from collections import deque
import sys

n,m = map(int,sys.stdin.readline().split())

select=list(map(int,sys.stdin.readline().split()))

li =deque([i for i in range(1,n+1)])

count =0

for i in select:
    while True:
        if li[0]==i:
            li.popleft()
            break
        else:
            if li.index(i) <len(li)/2:
                while li[0] !=i:
                    li.append(li.popleft())
                    count+=1
            else:
                while li[0]!=i:
                    li.appendleft(li.pop())
                    count+=1

print(count)

