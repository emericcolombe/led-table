import enum
import socket
from typing import List

from controllers.controller import TableController
from utils.primitives import Color, Led, Position


class MessageType(enum.Enum):
    # Message Types
    SET_SOME = 0
    SET_ALL = 1


class Table(TableController):
    def __init__(self, pixel_nb: int):
        super().__init__(pixel_nb)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        ip = '192.168.1.59'
        port = 5045

        self.socket.connect((ip, port))

    def set_pixel(self, x: int, y: int, color: Color, update=False):
        pass

    def set_pixels(self, leds: List[Led], update=False):
        message = bytearray()
        message.append(MessageType.SET_SOME.value)
        message.append(len(leds))
        for led in leds:
            message.append(self.xy_to_index(led.position))
            message.append(led.color.r)
            message.append(led.color.g)
            message.append(led.color.b)
            # print("LED{}".format(led.index))

        self.socket.send(message)

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
        pass

    @staticmethod
    def xy_to_index(position: Position) -> int:
        # TODO: Convert xy position to led index on led band
        print(position)
        return 203948
