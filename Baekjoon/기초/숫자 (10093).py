a,b = map(int,input().split())
n1=min(a,b)
n2=max(a,b)
if n2-n1 <=1:
    print(0)
else:
    print(n2-n1-1)
for i in range(n1+1,n2):
    print(i,end=" ")