from apps.app import LedApplication
from controllers.controller import TableController
import tkinter as tk
from tkcolorpicker import askcolor

from utils.primitives import Led, Color


class ColorPick(LedApplication):
    def __init__(self, controller: TableController) -> None:
        super().__init__(controller)
        self.root = None  # type: Optional[Tk]

    def start(self):
        self.root = tk.Tk()
        rgb = askcolor((255, 255, 0), self.root)[0]
        led_list = []
        for i in range(0, self.controller.size):
            for j in range(0, self.controller.size):
                led_list.append(Led(i, j, Color(rgb[0], rgb[1], rgb[2])))

        self.controller.set_pixels(led_list)

        while True:
            pass

    def stop(self):
        self.root.destroy()

