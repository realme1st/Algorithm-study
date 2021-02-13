test_case = int(input())

for _ in range(test_case):
    n, m =list(map(int,input().split(' ')))
    queue = list(map(int,input().split(' ')))
    queue = [(i, idx) for idx,i in enumerate(queue)] # 각각 튜플로 index랑 묶음

    # 튜플로 하면 좋은 점이 가장 큰 값을 구하거나 정렬에서 쉽게 됨

    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count+=1
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))