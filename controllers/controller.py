from typing import List

from utils.primitives import Color, Led


class TableController:
    """
    Interface for led controllers (table, simulator etc)
    """

    def __init__(self, pixel_nb: int):
        self._pixel_nb = pixel_nb
        self.upside_down = False

    def set_pixels(self, leds: List[Led], update=False):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    @property
    def size(self) -> int:
        return self._pixel_nb
