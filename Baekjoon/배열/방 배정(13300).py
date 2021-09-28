n,k = map(int,input().split())

students = [[0]*6 for i in range(2)]

for i in range(n):
    s,y =map(int,input().split())
    students[s][y-1]+=1

ans =0

for gender in students:
    for classes in gender:
        if classes % k==0:
            ans+=classes//k
        else:
            ans+=classes//k +1

print(ans)

