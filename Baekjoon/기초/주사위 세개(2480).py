a,b,c=map(int,input().split())

sum=0
if a==b==c:
    sum=10000+a*1000
elif a==b or b==c:
    sum=1000 +b*100
elif a==c:
    sum=1000+a*100
else:
    sum=100*max(a,b,c)

print(sum)
