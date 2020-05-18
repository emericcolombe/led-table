import time

from apps.app import LedApplication
from controllers.controller import TableController
from utils.primitives import Led, Color, Position


class Snake(LedApplication):
    def __init__(self, controller: TableController) -> None:
        super().__init__(controller)

    def start(self):
        # TODO: Code snake ¯\_(ツ)_/¯
        step = 0.3
        self.controller.set_pixels([Led(Position(0, 0), Color(0, 0, 255))])
        time.sleep(step)
        for i in range(0, self.controller.size - 1):
            ledsToSwitch = [Led(Position(i, 0), Color.black()),
                            Led(Position(i + 1, 0), Color(255 - 25 * i, 0, i * 25))]
            self.controller.set_pixels(ledsToSwitch)
            time.sleep(step)
        self.controller.set_pixels([Led(Position(9, 0), Color(0, 0, 0))])
        time.sleep(step)

    def stop(self):
        pass
