n = int(input())
lst = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp[0] = 1
prev = [None for _ in range(n)]
for i in range(1, n):
    max_prev = dp[0]
    prev_ind = 0
    for j in range(i):
        if dp[j] >= max_prev and lst[j] < lst[i]:
            max_prev = dp[j]
            prev_ind = j
    if prev_ind == 0 and lst[0] >= lst[i]:
        dp[i] = 1
    else:
        dp[i] = max_prev + 1
        prev[i] = prev_ind
max_len = 0
last_ind = 0
for i in range(n):
    if dp[i] > max_len:
        max_len = dp[i]
        last_ind = i
ans = []
print(max_len)
while last_ind is not None:
    ans.append(lst[last_ind])
    last_ind = prev[last_ind]
ans.reverse()
print(*ans)
print(prev)