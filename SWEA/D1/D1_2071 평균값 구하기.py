t = int(input())

for i in range(t):
    numbers = list(map(int,input().split()))
    averge = round(sum(numbers)/len(numbers))
    
    print("#{} {}".format(i+1,averge))
    