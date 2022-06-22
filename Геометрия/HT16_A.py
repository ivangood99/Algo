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


x, y, x1, y1, x2, y2 = map(float, input().split())
point_a = Point(x1, y1)
point_b = Point(x2, y2)
point_c = Point(x, y)
ca = Vector(point_c, point_a)
cb = Vector(point_c, point_b)
if cross_product(ca, cb) == 0 and dot_product(ca, cb) <= 0:
    print('YES')
else:
    print('NO')
