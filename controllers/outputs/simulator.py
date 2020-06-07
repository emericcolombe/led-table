# coding: utf-8
import time
from tkinter import *
from typing import List

from controllers.controller import TableController
from utils.primitives import Color, Led


class TableSimulator(TableController):

    def __init__(self, pixel_nb: int):
        super().__init__(pixel_nb)
        self._table_size = 500
        self._pixel_size = self._table_size / self._pixel_nb

        if self._pixel_size != round(self._pixel_size):
            raise Exception("Pixel size must be a whole number")
        else:
            self._pixel_size = int(self._pixel_size)

        self._window = Tk()

        self._canvas = Canvas(self._window,
                              width=self._table_size,
                              height=self._table_size,
                              background='grey')
        self._canvas.pack()
        self._canvas.bind("<Key>", self.key)
        self._create_grid()

    def set_pixel(self, x: int, y: int, color: Color, update=False):
        self._canvas.create_rectangle(x * self._pixel_size,
                                      y * self._pixel_size,
                                      x * self._pixel_size + self._pixel_size,
                                      y * self._pixel_size + self._pixel_size,
                                      fill=self.str_from_rgb(color))
        if update:
            self.update()

    def set_pixels(self, leds: List[Led], update=False):
        for led in leds:
            self.set_pixel(led.x,
                           led.y,
                           led.color)
        self.update()

    def _create_grid(self):
        for x in range(0, self._table_size, self._pixel_size):
            for y in range(0, self._table_size, self._pixel_size):
                self._canvas.create_rectangle(x,
                                              y,
                                              x + self._pixel_size,
                                              y + self._pixel_size,
                                              fill="white")
        self.update()

    def update(self):
        self._window.update()

    def key(self, event):
        print("pressed ", repr(event.char))

    @staticmethod
    def str_from_rgb(rgb: Color) -> str:
        """translates an rgb tuple of int to a tkinter friendly color code
        """
        return "#%02x%02x%02x" % (rgb.r, rgb.g, rgb.b)


if __name__ == '__main__':
    size = 10
    simulator = TableSimulator(size)
    while True:
        for y in range(0, size):
            for x in range(0, size):
                time.sleep(0.01)
                simulator.set_pixel(x, y, Color(255 - 25 * x, 0, x * 25), True)

        for y in range(0, size):
            for x in range(0, size):
                simulator.set_pixel(x, y, Color(255, 0, 255))
            time.sleep(0.05)
            simulator.update()
