n,q = map(int, input().split())
from collections import deque
que = deque()
for num in range(n):
    que.append([n-num, 0])
#print(que)
for _ in range(q):
    a = list(map(str, input().split()))
    if a[0] == '1':
        if a[1] == 'U':
            que.append([que[-1][0], que[-1][1]+1])
        elif a[1] == 'D':
            que.append([que[-1][0], que[-1][1]-1])
        elif a[1] == 'L':
            que.append([que[-1][0]-1, que[-1][1]])
        elif a[1] == 'R':
            que.append([que[-1][0]+1, que[-1][1]])
        que.popleft()
    elif a[0] == '2':
        coords = que[-1*int(a[1])]
        print(*coords)