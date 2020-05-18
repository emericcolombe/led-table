from controllers.controller import TableController


class LedApplication:
    def __init__(self, controller: TableController) -> None:
        self.controller = controller

    def start(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError
