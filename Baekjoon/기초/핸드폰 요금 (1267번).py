n=int(input())

b=list(map(int,input().split()))
y_cost=0
m_cost=0

for time in b:
    y_cost+=(time//30+1)*10
    m_cost+=(time//60+1)*15

if y_cost>m_cost:
    print('M',m_cost,end=" ")
elif y_cost <m_cost:
    print("Y",y_cost,end=' ')
else:
    print('Y','M',y_cost,end=' ')