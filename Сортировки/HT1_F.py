def rome_to_arabic(s):
    ans = 0
    arr = ["I", "V", "X", "L"]
    num = [1, 5, 10, 50]
    for i in range(len(s) - 1):
        if arr.index(s[i]) < arr.index(s[i + 1]):
            ans -= num[arr.index(s[i])]
        else:
            ans += num[arr.index(s[i])]
    ans += num[arr.index(s[-1])]
    return ans

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(str, input().split())))
arr = sorted(arr, key = lambda x: (x[0], rome_to_arabic(x[1])))
for i in range(len(arr)):
    print(arr[i][0], arr[i][1])
