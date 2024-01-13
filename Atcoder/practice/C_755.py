n = int(input())

def dfs(s):
    if int(s) > n:
        #too big, go back on layer
        #nothing should be added to count
        return 0
    if all(s.count(c) > 0 for c in '753'):
        #7,5,3 are present in the string
        ret = 1
        #one found
    else:
        ret = 0
        #nothing is found yet
    for c in '753':
        ret += dfs(s+c)
    return ret
print(dfs('0'))