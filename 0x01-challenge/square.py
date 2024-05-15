#!/usr/bin/python3


class square:

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Area of the square"""
        if self.width == 0 and self.height == 0:
            return 0

        if self.width == 0:
            return self.height * self.height

        if self.height == 0:
            return self.width * self.width

        return self.width * self.height

    def PermiterOfMySquare(self):
        """Perimeter of the square"""
        if self.width == 0 and self.height == 0:
            return 0

        if self.width == 0:
            return 4 * self.height

        if self.height == 0:
            return 4 * self.width

        return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 and self.height == 0:
            return "0/0"

        if self.width == 0:
            return "0/{}".format(self.height)

        if self.height == 0:
            return "{}/0".format(self.width)

        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
