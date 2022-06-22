MAX_A = 100
arr = list(map(int, input().split()))
cnt = [0 for i in range(MAX_A + 1)]
for elem in arr:
    cnt[elem] += 1
for i in range(MAX_A + 1):
    for _ in range(cnt[i]):
        print(i, end = ' ')

