N = int(input())
arr = list(map(int, input().split()))
for i in range(N - 1):
    for j in range(i + 1, N):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(*arr)
