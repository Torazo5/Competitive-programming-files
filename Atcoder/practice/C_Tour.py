# Cast a spell
import sys
sys.setrecursionlimit(10000)
# Read the input
n,m=map(int,input().split())
G=[[] for i in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    G[a-1].append(b-1)
#print(G)
def dfs(v):
    if temp[v]:
        #if we have visited we leave this layer
        return
    temp[v] = True
    for vv in G[v]:
        dfs(vv)
ans = 0
for i in range(n):
    temp = [False]*n
    dfs(i)
    ans += sum(temp)
print(ans)