from math import sqrt

EPS = 10 ** (-7)
N_ITERATIONS = 100

def foo(x):
    return x * x + sqrt(x)

c = float(input())
left = 0
right = 10 ** 6
for _ in range(N_ITERATIONS):
    middle = (left + right) / 2.0
    if (foo(middle) - c < 0):
        left = middle
    else:
        right = middle
print(right)
