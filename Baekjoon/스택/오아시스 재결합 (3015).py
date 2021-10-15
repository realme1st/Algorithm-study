n=int(input())

ans=0
stack=[]
# stack에 추가 되는 수는 튜플형식(a,b) a는 수를 나타내고 b는 앞자리까지의 영향력을 나타냄

for _ in range(n):
    h=int(input())
    # 스택의 제일 끝자리보다 큰 수가 들어왔을 시, stack[-1] 수의 앞자리 영향력을 더해준다.
    while stack and stack[-1][0]<h:
        ans+= stack.pop()[1]
    
    if stack and stack[-1][0]==h:
        cnt =stack.pop()[1]
        ans+=cnt
        # len(stack)이 0이 아니라면, stack에 수가 들어왔을 시, stack[-1]과 새로운 수의 관계를 더해준다.
        if len(stack)!=0:
            ans+=1
        stack.append((h,cnt+1))
    else:
        # len(stack)이 0이 아니라면, stack에 수가 들어왔을 시, stack[-1]과 새로운 수의 관계를 더해준다.
        if len(stack)!=0:
            ans+=1
        stack.append((h,1))

print(ans)