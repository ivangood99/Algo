EPS = 10 ** (-15)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vec):
        return Point(self.x + vec.x, self.y + vec.y)


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


n = int(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
point_a = Point(x1, y1)
point_b = Point(x2, y2)
sum = 0
for i in range(2, n):
    x3, y3 = map(float, input().split())
    point_c = Point(x3, y3)
    ab = Vector(point_a, point_b)
    ac = Vector(point_a, point_c)
    sum += cross_product(ab, ac) / 2
    point_b = Point(x3, y3)
print(abs(sum))