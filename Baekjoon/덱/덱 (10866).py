import sys
from collections import deque

n= int(sys.stdin.readline())

li=deque()

for i in range(n):
    command = sys.stdin.readline().rstrip().split()

    if command[0]=='push_front':
        li.appendleft(command[1])
    elif command[0] =='push_back':
        li.append(command[1])
    elif command[0] =='pop_front':
        if li:
            print(li.popleft())
        else:
            print(-1)
    elif command[0] =='pop_back':
        if li:
            print(li.pop())
        else:
            print(-1)
    elif command[0]=='size':
        print(len(li))
    elif command[0]=='empty':
        if li:
            print(0)
        else:
            print(1)
    elif command[0]=='front':
        if li:
            print(li[0])
        else:
            print(-1)
    elif command[0]=='back':
        if li:
            print(li[-1])
        else:
            print(-1)