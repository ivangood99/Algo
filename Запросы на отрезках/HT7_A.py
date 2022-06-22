GEN_ARRAY_A_MOD = 1 << 16;
GEN_ARRAY_B_MOD = 1 << 30;

n, x, y, a_0 = map(int, input().split())
m, z, t, b_0 = map(int, input().split())
arr_a = [a_0]
arr_b = [b_0]
arr_c = [b_0 % n]
res = 0
arr_sum = [0, a_0]
for i in range(1, n):
    arr_a.append((arr_a[i - 1] * x % GEN_ARRAY_A_MOD + y) % GEN_ARRAY_A_MOD)
    arr_sum.append(arr_sum[i] + arr_a[i])
for i in range(1, 2 * m):
    arr_b.append((arr_b[i - 1] * z % GEN_ARRAY_B_MOD + t) % GEN_ARRAY_B_MOD)
    arr_c.append(arr_b[i] % n)
for i in range(m):
    res += arr_sum[max(arr_c[2 * i], arr_c[2 * i + 1]) + 1]
    res -= arr_sum[min(arr_c[2 * i], arr_c[2 * i + 1])]
print(res)