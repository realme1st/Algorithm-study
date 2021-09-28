a,b,c=[int(input()) for _ in range(3)]

n=a*b*c
cnt = [0]*10

while n!=0:
    cnt[n%10]+=1
    n//=10

for i in range(10):
    print(cnt[i])

