import time

import enum

from apps.app import LedApplication
from controllers.controller import TableController
from utils.primitives import Led, Color


class Snake(LedApplication):
    def __init__(self, controller: TableController) -> None:
        super().__init__(controller)

    def start(self):
        # TODO: Code snake ¯\_(ツ)_/¯
        step = 0.5
        snake = SnakeBody(self.controller)
        time.sleep(2)

        for _ in range(0, 3):
            snake.move()
            time.sleep(step)
        snake.set_direction(SnakeDirection.DOWN)

        for _ in range(0, 5):
            snake.move()
            time.sleep(step)
        snake.set_direction(SnakeDirection.LEFT)

        for _ in range(0, 5):
            snake.move()
            time.sleep(step)

    def stop(self):
        pass


class SnakeDirection(enum.Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class SnakeBody:

    def __init__(self, controller: TableController) -> None:
        super().__init__()
        self.ui = controller

        self.body = [(5, 2), (4, 2), (3, 2), (2, 2)]
        self.move_direction = SnakeDirection.RIGHT

        self.head_color = Color(0, 0, 255)
        self.body_color = Color(255, 0, 0)
        self.bg_color = Color.black()

        self.draw_body()

    def move(self):
        prev_head_x, prev_head_y = self.body[0]
        if self.move_direction == SnakeDirection.UP:
            new_head = (prev_head_x, prev_head_y - 1)
            self.body.insert(0, new_head)
            prev_tail = self.body.pop()
        elif self.move_direction == SnakeDirection.DOWN:
            new_head = (prev_head_x, prev_head_y + 1)
            self.body.insert(0, new_head)
            prev_tail = self.body.pop()
        elif self.move_direction == SnakeDirection.LEFT:
            new_head = (prev_head_x - 1, prev_head_y)
            self.body.insert(0, new_head)
            prev_tail = self.body.pop()
        elif self.move_direction == SnakeDirection.RIGHT:
            new_head = (prev_head_x + 1, prev_head_y)
            self.body.insert(0, new_head)
            prev_tail = self.body.pop()
        else:
            raise Exception("Error, wrong orientation")

        self.ui.set_pixels([
            Led(prev_head_x, prev_head_y, self.body_color),
            Led(new_head[0], new_head[1], self.head_color),
            Led(prev_tail[0], prev_tail[1], self.bg_color),
        ], True)

    def set_direction(self, new_direction: SnakeDirection):
        self.move_direction = new_direction

    def draw_body(self):
        head_x, head_y = self.body[0]
        body_pixels = [Led(head_x, head_y, self.head_color)]
        for x, y in self.body[1:]:
            body_pixels.append(Led(x, y, self.body_color))

        self.ui.set_pixels(body_pixels, True)

