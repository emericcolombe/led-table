import unittest

from controllers.outputs.table import Table


class Coordinates(unittest.TestCase):

    def __init__(self, method_name: str = ...) -> None:
        super().__init__(method_name)
        self.table = None

    def setUp(self) -> None:
        self.table = Table(10)

    def test_xy_to_index_top_left(self):
        self.assertEqual(90, self.table.xy_to_index(0, 0))

    def test_xy_to_index_top_right(self):
        self.assertEqual(9, self.table.xy_to_index(self.table.size - 1, 0))

    def test_xy_to_index_bottom_left(self):
        self.assertEqual(99, self.table.xy_to_index(0, self.table.size - 1))

    def test_xy_to_index_bottom_right(self):
        self.assertEqual(0, self.table.xy_to_index(self.table.size - 1, self.table.size - 1))

    def test_xy_to_index_01(self):
        self.assertEqual(91, self.table.xy_to_index(0, 1))

    def test_xy_to_index_10(self):
        self.assertEqual(89, self.table.xy_to_index(1, 0))


if __name__ == '__main__':
    unittest.main()
