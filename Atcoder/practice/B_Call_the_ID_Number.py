n = int(input())
a = list(map(int, input().split()))
called = set()
ans = []
length = 0
for i in range(n):
    if i+1 not in called:
        called.add(a[i])
for r in range(n):
    if r+1 not in called:
        ans.append(r+1)
        length += 1
print(length)
print(*ans)