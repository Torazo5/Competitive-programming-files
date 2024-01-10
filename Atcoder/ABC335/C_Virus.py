from collections import deque
import math
n,d = map(int, input().split())
positions = []
G = [[] for i in range(n)] 
for _ in range(n):
    x,y = map(int, input().split())
    positions.append((x,y))
for i in range(n):
    for r in range(n):
        dist = math.dist(positions[i], positions[r])
        if dist <= d and i != r:
            G[i].append(r)
            
que = deque([0])
visited = set([0])
while que:
    current = que.popleft()
    for neighbour in G[current]:
        if neighbour not in visited:
            visited.add(neighbour)
            que.append(neighbour)

for i in range(n):
    if i in visited:
        print('Yes')
    else:
        print('No')