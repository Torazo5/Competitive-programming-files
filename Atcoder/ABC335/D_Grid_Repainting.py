h, w = map(int, input().split())
grid = []
walls = 0
for _ in range(h):
    s = input()
    for letter in s:
        if letter == '#':
            walls += 1
    grid.append(s)

from collections import deque
q = deque([(0,0,1)])
visited = set()
direct = [[1,0], [0,1], [-1,0], [0,-1]]
ans = -1
while q:
    r,c, length = q.popleft()
    if r == h-1 and c == w-1:
        ans = (h*w - length - walls)
        break
    for dr, dc in direct:
        if 0 <= r+dr <= h-1 and 0 <= c+dc <= w-1 and grid[r][c] == "." and (r+dr, c+dc) not in visited:
            visited.add((r+dr, c+dc))
            q.append((r+dr, c+dc, length +1)) 
print(ans)