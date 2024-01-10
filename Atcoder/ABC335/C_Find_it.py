
n = int(input())
a = list(map(int, input().split()))


G = [[] for _ in range(n)]
for i in range(n):
    G[i].append(a[i]-1)

#print(G)
from collections import deque
que = deque([0])
visited = set()
trace = []
while que:
    current = que.popleft()
    #print(current, visited)
    if current not in visited:
        trace.append(current)#indexing things
        que.append(G[current][0])
        visited.add(current)
    else:
        #current in visited
        ans = []
        for num in (trace[trace.index(current):]):
            ans.append(num+1)
        print(len(ans))
        print(*ans)