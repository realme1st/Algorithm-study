import sys
n= int(sys.stdin.readline())

building_list=[int(sys.stdin.readline()) for i in range(n)]

stack=[]
count=0

for i in range(n):
    while stack and stack[-1] <=building_list[i]:
        stack.pop()
    stack.append(building_list[i])
    count+= len(stack)-1

print(count)