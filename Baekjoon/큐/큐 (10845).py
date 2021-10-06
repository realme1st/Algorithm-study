import sys
n= int(sys.stdin.readline())
li=[]
for i in range(n):
    command=sys.stdin.readline().rstrip().split()

    if command[0]=='push':
        li.append(command[1])
    elif command[0]=='pop':
        if li:
            print(li.pop(0))
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
        if not li:
            print(-1)
    elif command[0]=='back':
        if li:
            print(li[-1])
        if not li:
            print(-1)