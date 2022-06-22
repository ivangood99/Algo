def zfunction(s):
    z = [0 for _ in range(len(s))]
    left = 0
    right = 0
    for i in range(1, len(s)):
        z[i] = max(0, min(right - i, z[i - left]))
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left = i
            right = i + z[i]
    return z

s = input()
print(*zfunction(s)[1:])