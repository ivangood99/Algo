def lower_bound(x):
    left, right = -1, n
    while right - left > 1:
        middle = (left + right) // 2
        if arr[middle] >= x:
            right = middle
        else:
            left = middle
    return right


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
k = int(input())
ans = []
for _ in range(k):
    left, right = map(int, input().split())
    if left < arr[0]:
        left_ind = 0
    else:
        left_ind = lower_bound(left)
    if right > arr[n - 1]:
        right_ind = n
    else:
        right_ind = lower_bound(right + 1)
    ans.append(right_ind - left_ind)
print(*ans)