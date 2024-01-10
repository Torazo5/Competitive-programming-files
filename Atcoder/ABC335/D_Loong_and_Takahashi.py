n = int(input())
grid = [[0] * n for _ in range(n)]
current = (n//2-1,n//2)
x= current[0]
y = current[1]
for i in range(1,n**2):
    if i%4 != 0:
        #its a decrease
        grid[x][y] = i
        if x > 0:
            x -=1
        if x == 0 and y> 0:
            y -= 1
        print(grid)
