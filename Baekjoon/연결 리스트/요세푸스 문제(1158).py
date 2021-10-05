
n,k=map(int,input().split())

data=[i for i in range(1,n+1)]
result=[]

temp=k-1

for i in range(n):
    if len(data) > temp:
        result.append(str(data.pop(temp)))
        temp+=k-1
    else:
        temp%=len(data)
        result.append(str(data.pop(temp)))
        temp+=k-1
print("<",", ".join(result),">",sep='')