a,b,c=[int(input()) for _ in range(3)]

n= a*b*c

ans=[0]*10

for i in str(n):
    ans[int(i)]+=1

for i in ans:
    print(i)