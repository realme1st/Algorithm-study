import sys

n= int(sys.stdin.readline())

for _ in range(n):
    flag=0
    li=[]
    command=sys.stdin.readline().rstrip()
    for i in command:
        if i =='(':
            li.append(i)
        elif i==')':
            if li:
                li.pop()
            else:
                flag+=1
                break
    
    if li or flag!=0:
        print("NO")
    else:
        print("YES")

    