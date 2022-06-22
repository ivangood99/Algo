from math import inf

n, m = map(int, input().split())
coins = [[0 for _ in range(m + 1)]]
dp = [[-inf for _ in range(m + 1)]]
prev = [[None for _ in range(m + 1)]]
for _ in range(n):
    coins.append([0] + list(map(int, input().split())))
    dp.append([-inf] + [0 for i in range(m)])
    prev.append([None for i in range(m + 1)])
dp[1][1] = coins[1][1]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i + j > 2:
            if dp[i - 1][j] < dp[i][j - 1]:
                dp[i][j] = dp[i][j - 1] + coins[i][j]
                prev[i][j] = [i, j - 1]
            else:
                dp[i][j] = dp[i - 1][j] + coins[i][j]
                prev[i][j] = [i - 1, j]
print(dp[n][m])
i, j = n, m
ans = ''
while prev[i][j] is not None:
    if prev[i][j][0] != i:
        ans += 'D'
        i -= 1
    else:
        ans += 'R'
        j -= 1
print(ans[::-1])

