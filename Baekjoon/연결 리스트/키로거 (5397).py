import sys

n= int(sys.stdin.readline())

for _ in range(n):
    stack_1=[]
    stack_2=[]
    l=list(sys.stdin.readline().rstrip())
    for command in l:
        if command == '<' and stack_1:
            stack_2.append(stack_1.pop())
        elif command=='<' and not stack_1:
            continue
        elif command =='>' and stack_2:
            stack_1.append(stack_2.pop())
        elif command =='-' and stack_1:
            stack_1.pop()
        else:
            stack_1.append(command)

    print("".join(stack_1+list(reversed(stack_2))))
