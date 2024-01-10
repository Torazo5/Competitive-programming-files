n, q = map(int, input().split())
import heapq
called = []
heapq.heapify(called)

lowest_id = 1
for _ in range(q):
  a = list(map(int, input().split()))
  if a[0] == 1:
    #call an id
    called.append(lowest_id)
    lowest_id += 1
  elif a[0] == 2:
    #guy has come to the place
    called.remove(a[1])
  else:
    #print 
    print(min(called))