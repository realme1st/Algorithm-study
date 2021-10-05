import sys
k=int(sys.stdin.readline())

result=[]
for _ in range(k):
    data=int(sys.stdin.readline())
    if data!=0:
        result.append(data)
    else:
        result.pop()

print(sum(result))