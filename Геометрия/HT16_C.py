from math import atan2, pi

EPS = 10 ** (-8)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vec):
        return Point(self.x + vec.x, self.y + vec.y)

    def __eq__(self, other):
        return other.x == self.x and other.y == self.y


class Vector:
    def __init__(self, a, b):
        if type(a) is Point:
            self.x = b.x - a.x
            self.y = b.y - a.y
        else:
            self.x = a
            self.y = b

    def add(self, vec):
        return Vector(self.x + vec.x, self.y + vec.y)

    def div(self, k):
        return Vector(self.x / k, self.y / k)


def dot_product(a, b):
    return a.x * b.x + a.y * b.y


def cross_product(a, b):
    return a.x * b.y - a.y * b.x


n, x, y = map(float, input().split())
n = int(n)
point_o = Point(x, y)
pts = []
for _ in range(n):
    x, y = map(float, input().split())
    pts.append(Point(x, y))
pts.append(pts[0])
sum = 0
flag = False
for i in range(n):
    oa = Vector(point_o, pts[i])
    ob = Vector(point_o, pts[i + 1])
    angle = atan2(cross_product(oa, ob), dot_product(oa, ob))
    sum += angle
    if abs(abs(angle) - pi) < EPS or point_o == pts[i]:
        flag = True
if flag or abs(abs(sum) - 2 * pi) < EPS:
    print('YES')
else:
    print('NO')
