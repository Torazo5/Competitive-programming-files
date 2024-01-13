N = int(input())
S = input()
from collections import deque
stack = deque()

for i in range(N):
    stack.append(S[i])
    
    if len(stack) >= 3: 
        if stack[-3] == 'f' and stack[-2] == 'o' and stack[-1] == 'x':
            stack.pop()
            stack.pop()
            stack.pop()
            
    #print(stack)

print(len(stack))