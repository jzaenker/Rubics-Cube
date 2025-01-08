import unittest
import numpy as np
import copy
from rubics.rc import rc

class CubeTest(unittest.TestCase):

    def cube_equal(self, cube1, cube2):
        np.testing.assert_array_equal(cube1.back, cube2.back)
        np.testing.assert_array_equal(cube1.front, cube2.front)
        np.testing.assert_array_equal(cube1.top, cube2.top)
        np.testing.assert_array_equal(cube1.bottom, cube2.bottom)
        np.testing.assert_array_equal(cube1.left, cube2.left)
        np.testing.assert_array_equal(cube1.right, cube2.right)

    def cube_not_equal(self, cube1, cube2):
        np.testing.assert_raises(AssertionError, np.testing.assert_array_equal, cube1.back, cube2.back)
        np.testing.assert_raises(AssertionError, np.testing.assert_array_equal, cube1.front, cube2.front)
        np.testing.assert_raises(AssertionError, np.testing.assert_array_equal, cube1.top, cube2.top)
        np.testing.assert_raises(AssertionError, np.testing.assert_array_equal, cube1.bottom, cube2.bottom)
        np.testing.assert_raises(AssertionError, np.testing.assert_array_equal, cube1.left, cube2.left)
        np.testing.assert_raises(AssertionError, np.testing.assert_array_equal, cube1.right, cube2.right)

    def test_back(self):
        cube1 = rc()
        cube1.shuffle()
        cube2 = copy.copy(cube1)

        for i in range(4):
            cube2.handle_back_left()
        self.cube_equal(cube1, cube2)

        for i in range(4):
            cube2.handle_back_right()
        self.cube_equal(cube1, cube2)

        for i in range(2):
            cube2.handle_back_left()
            cube2.handle_back_right()
        self.cube_equal(cube1, cube2)

    def test_front(self):
        cube1 = rc()
        cube1.shuffle()
        cube2 = copy.copy(cube1)

        for i in range(4):
            cube2.handle_front_left()
        self.cube_equal(cube1, cube2)

        for i in range(4):
            cube2.handle_front_right()
        self.cube_equal(cube1, cube2)

        for i in range(2):
            cube2.handle_front_left()
            cube2.handle_front_right()
        self.cube_equal(cube1, cube2)

    def test_top(self):
        cube1 = rc()
        cube1.shuffle()
        cube2 = copy.copy(cube1)

        for i in range(4):
            cube2.handle_top_left()
        self.cube_equal(cube1, cube2)

        for i in range(4):
            cube2.handle_top_right()
        self.cube_equal(cube1, cube2)

        for i in range(2):
            cube2.handle_top_left()
            cube2.handle_top_right()
        self.cube_equal(cube1, cube2)

    def test_bottom(self):
        cube1 = rc()
        cube1.shuffle()
        cube2 = copy.copy(cube1)

        for i in range(4):
            cube2.handle_bottom_left()
        self.cube_equal(cube1, cube2)

        for i in range(4):
            cube2.handle_bottom_right()
        self.cube_equal(cube1, cube2)

        for i in range(2):
            cube2.handle_bottom_left()
            cube2.handle_bottom_right()
        self.cube_equal(cube1, cube2)

    def test_right(self):
        cube1 = rc()
        cube1.shuffle()
        cube2 = copy.copy(cube1)

        for i in range(4):
            cube2.handle_right_up()
        self.cube_equal(cube1, cube2)

        for i in range(4):
            cube2.handle_right_down()
        self.cube_equal(cube1, cube2)

        for i in range(2):
            cube2.handle_right_up()
            cube2.handle_right_down()
        self.cube_equal(cube1, cube2)

    def test_left(self):
        cube1 = rc()
        cube1.shuffle()
        cube2 = copy.copy(cube1)

        for i in range(4):
            cube2.handle_left_up()
        self.cube_equal(cube1, cube2)

        for i in range(4):
            cube2.handle_left_down()
        self.cube_equal(cube1, cube2)

        for i in range(2):
            cube2.handle_left_up()
            cube2.handle_left_down()
        self.cube_equal(cube1, cube2)

    def test_shuffle(self):
        cube1 = rc()
        cube2 = rc()
        cube2.shuffle()
        self.cube_not_equal(cube1, cube2)

    def test_solve(self):
        cube1 = rc()
        cube2 = rc()
        cube2.shuffle()
        cube2.solve()
        self.cube_equal(cube1, cube2)

if __name__ == '__main__':
    unittest.main()