import sys
n=int(sys.stdin.readline())
result=[]

for _ in range(n):
    command = list(sys.stdin.readline().split())

    if command[0]=='push':
        result.append(command[1])
    elif command[0]=='top':
        if result:
            print(result[-1])
        else:
            print(-1)
    elif command[0]=='size':
        print(len(result))
    elif command[0]=='pop':
        if result:
            print(result.pop())
        else:
            print(-1)
    elif command[0]=='empty':
        if result:
            print(0)
        else:
            print(1)    
