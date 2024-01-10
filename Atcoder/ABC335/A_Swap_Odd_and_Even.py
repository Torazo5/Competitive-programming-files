s = input()
ans =''
for i in range(len(s)//2):
    ans += s[2*i+1]
    ans += s[2*i]
print(ans)