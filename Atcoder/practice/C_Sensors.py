class UnionFind():
  def __init__(self, n):
    self.n = n
    self.parent_size = [-1] * n
  def merge(self, a, b):
    x, y = self.leader(a), self.leader(b)
    if x == y:
      return
    if abs(self.parent_size[x]) < abs(self.parent_size[y]):
      x, y = y, x
    self.parent_size[x] += self.parent_size[y]
    self.parent_size[y] = x
    return
  def same(self, a, b):
    return self.leader(a) == self.leader(b)
  def leader(self, a):
    if self.parent_size[a] < 0:
      return a
    self.parent_size[a] = self.leader(self.parent_size[a])
    return self.parent_size[a]
  def size(self, a):
    return abs(self.parent_size[self.leader(a)])
  def groups(self):
    result = [[] for _ in range(self.n)]
    for i in range(self.n):
      result[self.leader(i)].append(i)
    return [r for r in result if r != []]

h,w = map(int, input().split())
direct = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
dots = set()
for i in range(h):
    s = input()
    for r in range(w):
        if s[r] == '#':
            dots.add((i,r))
u = UnionFind(h*w+2)
#print(dots)
for dot in dots:
    for di,dj in direct:
       check = (dot[0]+di,dot[1]+dj)
       #print(dot, check)
       if check in dots:
            #neighbour exists
            #print(dot[0]*+dot[1], (check)[0]*4+(check)[1])
            u.merge(dot[0]*w+dot[1], (check)[0]*w+(check)[1])
groups = u.groups()
#print(groups)
total = 0
ans = 0
for group in groups:
    if len(group) > 1:
        total += len(group)
        ans += 1
#print(ans, total)
#print(dots, len(dots))
ans += len(dots)-total
print(ans)