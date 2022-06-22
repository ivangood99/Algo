def pfunction(s):
    p = [0 for _ in range(len(s))]
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[i] != s[k]:
            k = p[k - 1]
        if s[i] == s[k]:
            k += 1
        p[i] = k
    return p

s1 = input()
s2 = input()
p_lst = pfunction(s1 + "*" + s2)
ans = []
for i in range(len(p_lst)):
    if p_lst[i] == len(s1):
        ans.append(i - 2 * len(s1) + 1)
print(len(ans))
print(*ans)