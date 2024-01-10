N = int(input())

for x in range(N + 1):
    for y in range(N + 1):
        for z in range(N+1):
            #print(x,y,z)
            if x+y+z <= N:
                print(x,y,z)
n,q = map(int, input().split())
from collections import deque
que = deque()
for num in range(1,n + 1):
    que.append([num,0])
print(que)
count = 0
direct = {'U':[0,1], 'D':[0,-1], 'L':[-1,0], 'R':[0,1]}
for _ in range(q):
    a = list(map(str, input().split()))
    if a[0] == '1':
        if count == 0:
            if a[1] == 'U':
                que.append([que[0][0], que[0][1] + 1])
            elif a[1] == 'D':
                que.append([que[0][0], que[0][1] - 1])
            elif a[1] == 'L':
                que.append([que[0][0]- 1, que[0][1]])
            elif a[1] == 'R':
                que.append([que[0][0] +1, que[0][1]])
            count += 1
        else:
            if a[1] == 'U':
                que.append([que[-1][0], que[-1][1] + 1])
            elif a[1] == 'D':
                que.append([que[-1][0], que[-1][1] - 1])
            elif a[1] == 'L':
                que.append([que[-1][0]- 1, que[-1][1]])
            elif a[1] == 'R':
                que.append([que[-1][0] +1, que[-1][1]])
        que.popleft()
        print(que)
    elif a[0] == '2':
        coords = que[5-int(a[1])]
        print(*coords)