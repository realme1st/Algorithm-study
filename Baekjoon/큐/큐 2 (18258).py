import sys
from collections import deque

n=int(sys.stdin.readline())
li=deque()
for _ in range(n):
    command = sys.stdin.readline().rstrip().split()

    if command[0]=='push':
        li.append(command[1])
    elif command[0]=='pop':
        if li:
            print(li.popleft())
        else:
            print(-1)
    elif command[0]=='size':
        print(len(li))
    elif command[0]=='empty':
        if len(li)==0:
            print(1)
        else:
            print(0)
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

