import enum
from typing import List

from controllers.controller import TableController
from controllers.outputs.simulator import TableSimulator
from controllers.outputs.table import Table
from utils.primitives import Color, Led


class DispatcherConfig(enum.Enum):
    # Output configuration
    TABLE = 0
    SIMULATOR = 1
    TABLE_AND_SIMULATOR = 2


class LedDispatcher(TableController):

    def __init__(self, pixel_nb: int, config: DispatcherConfig):
        super().__init__(pixel_nb)

        self.active_controllers = []  # type: List[TableController]

        if config == DispatcherConfig.TABLE or config == DispatcherConfig.TABLE_AND_SIMULATOR:
            table = Table(pixel_nb)
            table.connect()
            self.active_controllers.append(table)

        if config == DispatcherConfig.SIMULATOR or config == DispatcherConfig.TABLE_AND_SIMULATOR:
            self.active_controllers.append(TableSimulator(pixel_nb))

    def set_pixel(self, x: int, y: int, color: Color, update=False):
        for controller in self.active_controllers:
            controller.set_pixel(x, y, color, update)

    def set_pixels(self, leds: List[Led], update=False):
        for controller in self.active_controllers:
            controller.set_pixels(leds, update)

    def update(self):
        for controller in self.active_controllers:
            controller.update()
