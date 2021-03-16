def push(x):
    stack.append(x)

def pop():
    if(not stack):
        return -1
    else:
        return stack.pop()

def size():
    return len(stack)

def empty():
    return 0 if stack else 1

def top():
    return stack[-1] if stack else -1

N = int(input())
stack = []

for i in range(N):
    command = input().split()

    if command[0] =='push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if len(stack) ==0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] =='size':
        print(len(stack))
    elif command[0] =='empty':
        if len(stack) ==0:
            print(1)
        else:
            print(0)
    elif command[0] =='top':
        if len(stack) ==0:
            print(-1)
        else:
            print(stack[-1])