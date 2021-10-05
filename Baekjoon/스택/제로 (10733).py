import sys
k=int(sys.stdin.readline())

result=[]
for _ in range(k):
    data=int(sys.stdin.readline())
    if data!=0:
        result.append(data)
    else:
        result.pop()

if len(result)==0:
    print(0)
else:
    print(sum(result))