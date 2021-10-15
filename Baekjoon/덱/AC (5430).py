import sys
from collections import deque

t= int(sys.stdin.readline())

for i in range(t):
    command =sys.stdin.readline().rstrip()
    n=int(sys.stdin.readline())

    arr=sys.stdin.readline().rstrip()[1:-1].split(",")

    li = deque(arr)

    rev,front,back=0,0,len(li)-1
    flag=0

    if n==0:
        li=[]
        front=0
        back=0
    
    for j in command:
        if j=='R':
            rev+=1
        elif j=='D':
            if len(li)<1:
                flag=1
                print('error')
                break
            else:
                if rev%2==0:
                    li.popleft()
                else:
                    li.pop()
    
    if flag==0:
        if rev%2==0:
            print('['+",".join(li)+']')
        else:
            li.reverse()
            print('['+",".join(li)+']')


