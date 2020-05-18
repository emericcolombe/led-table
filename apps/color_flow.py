import time

from apps.app import LedApplication
from controllers.controller import TableController
from utils.primitives import Color


class ColorFlow(LedApplication):
    def __init__(self, controller: TableController) -> None:
        super().__init__(controller)
        self._running = False

    def start(self):
        self._running = True
        while self._running:
            for y in range(0, self.controller.size):
                for x in range(0, self.controller.size):
                    time.sleep(0.01)
                    self.controller.set_pixel(x, y, Color(255 - 25 * x, 0, x * 25), True)

            for y in range(0, self.controller.size):
                for x in range(0, self.controller.size):
                    self.controller.set_pixel(x, y, Color(255, 0, 255))
                time.sleep(0.05)
                self.controller.update()

    def stop(self):
        self._running = False
