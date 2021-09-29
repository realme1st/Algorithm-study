n= [int(input()) for _ in range(9)]

total=sum(n)

for i in range(9):
    for j in range(i+1,9):
        if 100 == total - (n[i]+n[j]):
            num1,num2 = n[i],n[j]
            
n.remove(num1)
n.remove(num2)
n.sort()

for i in n:
    print(i)