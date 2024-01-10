h,w = map(int, input().split())
from collections import deque
q = deque()
grid = []
visited = set()
for i in range(h):
    s = input()
    grid.append(s)
    for j in range(w):
        if s[j] == '#':
            q.append((i,j, 0))
            visited.add((i,j))
print(q)
#print(visited)
dist = 0
count = 0
direct = [[1,0], [0,1], [-1,0], [0,-1]]
while q:
    r,c, length = q.popleft()
    for dr, dc in direct:
        if (r+dr, c+dc) not in visited and 0 <= r+dr <= h-1 and 0<= c+dc <= w-1:
            #print('added', r+dr, c+dc, 'through', (r,c))
            dist = max(dist, length+1)
            q.append((r+dr, c+dc, length+1))
            visited.add((r+dr, c+dc))
print(dist)