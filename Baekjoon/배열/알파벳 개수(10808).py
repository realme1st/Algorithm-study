s= input()

cnt=[0]*26

for i in s:
    cnt[ord(i)-97]+=1


for i in cnt:
    print(i,end=" ")


# li = [0]*26
# for c in input():
#       li[ord(c)-ord('a')] += 1
# print(*li)