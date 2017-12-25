class Shape(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

s1 = Shape(1, 1)
s2 = Shape(1, 1)
print(s1 == s2)