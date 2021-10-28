n=int(input())
data=[int(input()) for i in range(n)]
data.sort()

w=data[0]*n

for i in range(1,n):
    temp=data[i]*(n-i)
    if w <temp:
        w=temp

print(w)