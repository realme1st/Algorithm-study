a,b= [list(input()) for _ in range(2)]

li_1=[0]*26
li_2 =[0]*26

cnt=0

for i in a:
    li_1[ord(i)-97]+=1

for i in b:
    li_2[ord(i)-97]+=1

for i in range(26):
    cnt+=abs(li_1[i]-li_2[i])
print(cnt)