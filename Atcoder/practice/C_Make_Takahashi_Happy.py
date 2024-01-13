# H, W <10と小さいのでDFSか

H, W = map(int, input().split())
A = []
for i in range(H):
    A.append(list(map(int, input().split())))

import sys
sys.setrecursionlimit(10**7)

def dfs(i, j, VISITED):
    global ans
    if i == H-1 and j == W-1:
        ans += 1
        return
    
    if i+1 < H and A[i+1][j] not in VISITED:
        VISITED.add(A[i+1][j])
        dfs(i+1, j, VISITED)
        VISITED.discard(A[i+1][j])
    
    if j+1 < W and A[i][j+1] not in VISITED:
        VISITED.add(A[i][j+1])
        dfs(i, j+1, VISITED)
        VISITED.discard(A[i][j+1])    
    
ans = 0
visited = set()
visited.add(A[0][0])
dfs(0, 0, visited)
print(ans)