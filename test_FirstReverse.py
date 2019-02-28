import unittest
from FirstReverse import FirstReverse

class FirstReverseTest(unittest.TestCase):

    def test_say_a_when_a(self):
        self.assertEqual(FirstReverse('a'), 'a')

    def test_say_ba_when_ab(self):
        self.assertEqual(FirstReverse('ab'), 'ba')

    def test_say_cba_when_abc(self):
        self.assertEqual(FirstReverse('abc'), 'cba')

    def test_say_etybredoc_when_coderbyte(self):
            self.assertEqual(FirstReverse('coderbyte'), 'etybredoc')

    def test_say_edoC_evoL_I_when_I_Love_Code(self):
            self.assertEqual(FirstReverse('I Love Code'), 'edoC evoL I')