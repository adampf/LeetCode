# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

from unittest import TestCase
import LC_66_E


class TestLC_66_E(TestCase):

    def test(self):
        self.assertEqual(LC_66_E.Solution.plusOne([1, 2, 3]), [1, 2, 4])
        self.assertEqual(LC_66_E.Solution.plusOne([4, 3, 2, 1]), [4, 3, 2, 2])
        self.assertEqual(LC_66_E.Solution.plusOne([0]), [1])
        self.assertEqual(LC_66_E.Solution.plusOne([9]), [1, 0])
        self.assertEqual(LC_66_E.Solution.plusOne([9, 9]), [1, 0, 0])
        self.assertEqual(LC_66_E.Solution.plusOne([9, 9, 9, 9]), [1, 0, 0, 0, 0])
        self.assertEqual(LC_66_E.Solution.plusOne([9, 4, 5, 0]), [9, 4, 5, 1])
        self.assertEqual(LC_66_E.Solution.plusOne([9, 4, 5, 0, 4]), [9, 4, 5, 0, 5])
        self.assertEqual(LC_66_E.Solution.plusOne([9, 4, 5, 0, 0, 4]), [9, 4, 5, 0, 0, 5])
        self.assertEqual(LC_66_E.Solution.plusOne([9, 4, 5, 0, 9, 0, 4]), [9, 4, 5, 0, 9, 0, 5])
        self.assertEqual(LC_66_E.Solution.plusOne([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), [9, 8, 7, 6, 5, 4, 3, 2, 1, 1])
        self.assertEqual(LC_66_E.Solution.plusOne([9, 2, 3, 9]), [9, 2, 4, 0])
        self.assertEqual(LC_66_E.Solution.plusOne([9, 4, 5, 0, 9]), [9, 4, 5, 1, 0])
        self.assertEqual(LC_66_E.Solution.plusOne([8, 9, 9, 9]), [9, 0, 0, 0])
        self.assertEqual(LC_66_E.Solution.plusOne([9, 8, 9, 9]), [9, 9, 0, 0])
