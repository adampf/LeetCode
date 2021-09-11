# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

import unittest
import LC_1


class TestCalc(unittest.TestCase):

    def test_two_sum(self):

        print("starting unit test")
        self.assertEqual(LC_1.Solution.twoSum([2, 7, 11, 15], 9), [0, 1])
        print("Test #1 Passed")
        self.assertEqual(LC_1.Solution.twoSum([3, 2, 4], 6), [1, 2])
        print("Test #2 Passed")
        self.assertEqual(LC_1.Solution.twoSum([3, 3], 6), [0, 1])
        print("Test #3 Passed")


