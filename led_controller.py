#!/usr/bin/env python
from apps.color_flow import ColorFlow
from apps.color_pick import ColorPick
from apps.snake import Snake
from controllers.dispatcher import LedDispatcher, DispatcherConfig

if __name__ == "__main__":
    table = LedDispatcher(10, DispatcherConfig.TABLE)

    # app = ColorFlow(table)
    # app = ColorPick(table)
    app = Snake(table)
    app.start()
