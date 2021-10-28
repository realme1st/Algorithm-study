n=int(input())

price=1000-n

coin=[500,100,50,10,5,1]

result=0
for i in coin:
    if price>0:
        result+=price//i
        price%=i

print(result)

