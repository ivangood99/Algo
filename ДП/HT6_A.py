n, k = map(int, input().split())
coins = list(map(int, input().split()))
coins.append(0)
dp = [0 for _ in range(k)]
prev = []
for i in range(1, n):
    max_prev = dp[-1]
    prev_ind = i - 1
    for j in range(2, k + 1):
        if dp[-j] > max_prev:
            max_prev = dp[-j]
            prev_ind = i - j
    dp.append(max_prev + coins[i - 1])
    prev.append(prev_ind)
dp = dp[k - 1:]
ans = [n]
last = n - 2
while last >= 0:
    ans.append(prev[last] + 1)
    last = prev[last] - 1
print(dp[-1])
print(len(ans) - 1)
ans.reverse()
print(*ans)

