import sys
n = int(sys.stdin.readline())
for _ in range(n):
    left_stack = []
    right_stack = []
    data = list(sys.stdin.readline().rstrip())
    for i in data:
        if i == '-':
            if left_stack:
                left_stack.pop()
        elif i =='<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i =='>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)
    
    print(''.join(left_stack+list(reversed(right_stack))))