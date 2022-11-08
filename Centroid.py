from Point import Point


class Centroid(Point):
    def __init__(self, x, y, index, color = 'black'):
        super().__init__(x, y)
        self.index = index
        self.color = color

    def update(self, x, y):
        self.x = x
        self.y = y
