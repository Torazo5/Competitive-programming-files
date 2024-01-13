R,C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
grid = []
for _ in range(R):
    s = input()
    grid.append(s)

from collections import deque
N = len(grid)
#print('N', N)
q = deque([(sx-1,sy-1,0)])
visit = set((sx-1,sy-1))
direct = [[1,0], [0,1], [-1, 0], [0,-1]]
while q:
    r,c,length = q.popleft()
    print(q)
    if r== gy-1 and c == gx-1:
        #print('END')
        print(length)
        break
    if (r >= R-1 or c >= C-1 or grid[r][c] == '#'):
        continue
    for dr, dc in direct:
        if (r+dr, c+dc) not in visit:
            q.append((r+dr, c+dc, length+1))
            visit.add((r+dr, c+dc))