import sys

n= int(sys.stdin.readline())
stack_1=[]
answer=[]
top_list=list(sys.stdin.readline().split())

for i in range(n):
    while stack_1:
        if stack_1[-1][1] > top_list[i]:
            answer.append(stack_1[-1][0]+1)
            break
        else:
            stack_1.pop()
    
    if not stack_1:
        answer.append(0)
    stack_1.append([i,top_list[i]])

print(*answer)





