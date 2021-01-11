n,k = map(int,input().split())
num=0
money = []
for i in range(n):
    money.append(int(input()))



for i in range(n-1,-1,-1):
    if k==0:
        break
    if money[i]>k:
        continue
    num+=k//money[i]
    k%=money[i]
    
print(num)