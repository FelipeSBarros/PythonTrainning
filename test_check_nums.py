from unittest import TestCase
from CheckNums import CheckNums

class testCheckNums(TestCase):
    def test_say_true_if_n1_gt_n2(self):
        self.assertEqual(CheckNums(1, 2), 'true')

    def test_say_false_if_n12_gt_n1(self):
        self.assertEqual(CheckNums(2, 1), 'false')

    def test_say_neg1_if_n2_eq_n1(self):
        self.assertEqual(CheckNums(2, 2), '-1')

    def test_say_neg1_if_n1_eq_n2(self):
        self.assertEqual(CheckNums(20, 20), '-1')