# coding: utf-8


class Color:
    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b

    @classmethod
    def black(cls):
        return cls(0, 0, 0)

    def __str__(self) -> str:
        return "r: {} g: {} b: {}".format(self.r, self.g, self.b)


class Led:
    def __init__(self, x: int, y: int, color: Color):
        self._x = x
        self._y = y
        self._color = color

    @property
    def position(self):
        return self._x, self._y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    def __str__(self) -> str:
        return "x: {} y: {}".format(self._x, self._y)


