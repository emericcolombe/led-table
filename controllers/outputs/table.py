import enum
import socket
from typing import List

from controllers.controller import TableController
from utils.primitives import Color, Led


class MessageType(enum.Enum):
    # Message Types
    SET_SOME = 0
    SET_ALL = 1


class Table(TableController):
    def __init__(self, pixel_nb: int):
        super().__init__(pixel_nb)
        self.socket = None  # type: Optional[socket]
        self.message = bytearray()

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        ip = '192.168.1.59'
        port = 5045

        print("Connecting...")
        self.socket.connect((ip, port))
        print("Connected !")

    def set_pixels(self, leds: List[Led], update=False):

        self.message.append(MessageType.SET_SOME.value)
        self.message.append(len(leds))
        for led in leds:
            self.message.append(self.xy_to_index(led.x, led.y))
            self.message.append(led.color.r)
            self.message.append(led.color.g)
            self.message.append(led.color.b)

        # print(len(leds))
        # print(len(self.message))

        if update:
            self.update()

    def set_all(self, color: Color):
        message = bytearray()
        message.append(MessageType.SET_ALL.value)
        message.append(self._pixel_nb)
        for i in range(0, self._pixel_nb):
            message.append(color.r)
            message.append(color.g)
            message.append(color.b)
            # print("LED{}".format(led.index))

        self.socket.send(message)

    def update(self):
        self.socket.send(self.message)
        self.message.clear()

    def xy_to_index(self, x: int, y: int) -> int:
        if not self.upside_down:
            leds_before_column = self._pixel_nb * (self._pixel_nb - 1 - x)
            if x % 2 == 0:
                index = leds_before_column + y
            else:
                index = leds_before_column + self._pixel_nb - 1 - y
        else:
            index = x * self._pixel_nb
            if x % 2 == 0:
                index += y
            else:
                index += self._pixel_nb

        return index
