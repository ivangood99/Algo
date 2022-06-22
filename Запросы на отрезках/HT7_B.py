GEN_A_K = 23
GEN_A_B = 21563
GEN_A_MOD = 16714589

GEN_U_K = 17
GEN_U_B = 751

GEN_V_K = 13
GEN_V_B = 593


def gen_next(mode = 0, prev = 0, prev_ans = 0, n_it = 0, size = 0):
    if mode == 1:
        return (GEN_U_K * prev + GEN_U_B + prev_ans + 2 * n_it) % size + 1
    elif mode == 2:
        return (GEN_V_K * prev + GEN_V_B + prev_ans + 5 * n_it) % size + 1
    else:
        return (GEN_A_K * prev + GEN_A_B) % GEN_A_MOD


n, m, a_0 = map(int, input().split())
u, v = map(int, input().split())
lst = [a_0]
for i in range(1, n):
    lst.append(gen_next(mode = 0, prev = lst[i - 1]))
max_pow = [0, 0]
for i in range(2, n + 1):
    max_pow.append(max_pow[i - 1])
    if (1 << (max_pow[i] + 1)) <= i:
        max_pow[i] += 1
max_k = max_pow[n]
min_dp = [[None for i in range(max_k + 1)] for k in range(n)]
for i in range(n):
    min_dp[i][0] = lst[i]
for j in range(1, max_k + 1):
    for i in range(n):
        if i + (1 << (j - 1)) < n:
            min_dp[i][j] = min(min_dp[i][j - 1], min_dp[i + (1 << (j - 1))][j - 1])
        else:
            min_dp[i][j] = min_dp[i][j - 1]
for i in range(m):
    k = max_pow[abs(u - v) + 1]
    ans = min(min_dp[min(u, v) - 1][k], min_dp[max(u, v) - (1 << k)][k])
    if i != m - 1:
        u = gen_next(mode = 1, prev = u, prev_ans = ans, n_it = i + 1, size = n)
        v = gen_next(mode = 2, prev = v, prev_ans = ans, n_it = i + 1, size = n)
print(u, v, ans)
