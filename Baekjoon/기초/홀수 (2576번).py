n= [int(input()) for _ in range(7)]
sum=0
min_num=100
for num in n:
    if num%2==1:
        sum+=num
        if min_num > num:
            min_num=num

if sum==0:
    print(-1)
else:
    print(sum)
    print(min_num)


