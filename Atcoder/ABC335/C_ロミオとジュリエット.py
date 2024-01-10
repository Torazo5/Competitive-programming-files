n = int(input())

G = [[] for i in range(n+1)]

for i in range(n-1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
#print(G)
from collections import deque
que = deque()
que.append((1,0))
visited = set()
visited.add(1)
count = 0
max_dist = -1
furthest_node = -1
while que:
    current,length = que.popleft()
    #print(que)
    for next_node in G[current]:
        #print('CHECKING', next_node)
        if next_node not in visited:
            if length+1 >= max_dist:
                #this one is max so far
                max_dist = length+1
                furthest_node = next_node
            que.append((next_node,length+1))
            visited.add(next_node)

#bfs again from furthest node

visited = set()
visited.add(furthest_node)
que.append((furthest_node, 0))
furthest_node2 = -1
max_dist = -1
while que:
    current, length = que.popleft()
    for next_node in G[current]:
        if next_node not in visited:
            if length+1 >= max_dist:
                #this one is max so far
                max_dist = length+1
                furthest_node2 = next_node
            visited.add(next_node)
            que.append((next_node,length+1))
print(furthest_node, furthest_node2)