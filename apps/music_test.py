# Print out realtime audio volume as ascii bars
import time

import numpy as np
import sounddevice as sd
from apps.app import LedApplication
from controllers.controller import TableController
from utils.primitives import Led, Color

duration = 100  # seconds


class MusicTest(LedApplication):

    def __init__(self, controller: TableController) -> None:
        super().__init__(controller)

    def start(self):
        with sd.Stream(callback=self.print_sound):
            time.sleep(5)
            sd.sleep(duration * 1000)

    def stop(self):
        pass

    def print_sound(self, indata, outdata, frames, time, status):
        volume_norm = int(np.linalg.norm(indata)) + 1

        print("{}".format(volume_norm))

        ledsToSwitch = []
        for i in range(0, volume_norm):
            # print("{}".format(i))
            ledsToSwitch.append(Led(int(i), 0,
                                    Color(0, 0, 255)))

        # print(ledsToSwitch)
        self.controller.set_pixels(ledsToSwitch)

        print("|" * int(volume_norm))



