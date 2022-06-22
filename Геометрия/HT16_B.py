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


x1, y1, x2, y2 = map(float, input().split())
point_a = Point(x1, y1)
point_b = Point(x2, y2)
x3, y3, x4, y4 = map(float, input().split())
point_c = Point(x3, y3)
point_d = Point(x4, y4)
ac = Vector(point_a, point_c)
ab = Vector(point_a, point_b)
ad = Vector(point_a, point_d)
ca = Vector(point_c, point_a)
cd = Vector(point_c, point_d)
cb = Vector(point_c, point_b)
if cross_product(ab, ac) == 0 and cross_product(ab, ad) == 0:
    da = Vector(point_d, point_a)
    db = Vector(point_d, point_b)
    if dot_product(ca, cb) <= 0 or dot_product(da, db) <= 0 or dot_product(ac, ad) <= 0:
        print('YES')
    else:
        print('NO')
elif cross_product(ab, ac) * cross_product(ab, ad) <= 0 and cross_product(cd, ca) * cross_product(cd, cb) <= 0:
    print('YES')
else:
    print('NO')
