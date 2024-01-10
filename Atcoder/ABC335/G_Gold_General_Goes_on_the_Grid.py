n, h,w = map(int, input().split())
walls = []
for _ in range(n):
    x,y = map(int, input().split())
    walls.append((x,y))

from collections import deque

q = deque([(0,0,0)])
visited = set((0,0))
ans = -1
direct = [[1,0], [0,1], [-1,0], [0,-1], [1,1], [-1,1]]
while q:
    r,c,length = q.popleft()
    #print(q)
    if length > 400:
        break
    if r == h and c == w:
        #reached goal
        ans = length
        break
    for dr, dc in direct:
        if (r+dr, c+dc) not in walls and (r+dr,c+dc) not in visited:
            q.append((r+dr, c+dc, length+1))
            visited.add((r+dr, c+dc))
    
print(ans)