import time

from apps.app import LedApplication
from controllers.controller import TableController
from utils.primitives import Color, Led


class ColorFlow(LedApplication):
    def __init__(self, controller: TableController) -> None:
        super().__init__(controller)
        self._running = False

    def start(self):
        self._running = True
        while self._running:
            for y in range(0, self.controller.size):
                for x in range(0, self.controller.size):
                    self.controller.set_pixels([Led(x, y, Color(255 - 25 * x, 0, x * 25))], True)

            time.sleep(0.5)
            for y in range(0, self.controller.size):
                for x in range(0, self.controller.size):
                    self.controller.set_pixels([Led(x, y, Color(255, 0, 255))])
                self.controller.update()

            time.sleep(0.5)

    def stop(self):
        self._running = False
