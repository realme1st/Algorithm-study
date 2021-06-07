n = int(input())
m = int(input())

broken = [False] * 10 #고장난 버튼 판별 위함

if m > 0:
    a = list(map(int,input().split()))
else: # 고장난 버튼 없는 경우
    a = []

for x in a:
    broken[x] = True

def possible(c): # 채널 c 로 이동이 가능하면 그 때 c로 리턴
    if c ==0:
        if broken[0]:
            return 0
        else:
            return 1

    l = 0
    while c > 0:
        if broken[c%10]:
            return 0
        l +=1
        c //=10
    return l

ans = abs(n-100) # 숫자버튼을 안 누르는 경우 (정답 초기값)
for i in range(0,1000000+1):
    c = i
    l = possible(c)
    if l > 0:
        press = abs(c-n)
        if ans > l +press:
            ans = l+press

print(ans)