import sys
n= int(sys.stdin.readline())

data=[]
count=0
answer=[]
temp=True
for _ in range(n):
    command = int(sys.stdin.readline())
    while count<command:
        count+=1
        data.append(count)
        answer.append('+')
    
    if command in data:
        data.pop()
        answer.append('-')
    else:
        temp=False
    
if temp==False:
    print("NO")
else:
    for i in data:
        print(i)
        
    
    
    