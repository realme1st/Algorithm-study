n,m = map(int,input().split())

sol =0
for i in range(n):
    data = list(map(int,input().split()))
    if sol<min(data):
        sol = min(data)

print(sol)

