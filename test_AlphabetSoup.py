from unittest import TestCase
from AlphabetSoup import AlphabetSoup

class TestAlphabetSoup(TestCase):
    def test_say_ab_when_ba(self):
        self.assertEqual(AlphabetSoup('ba'), "ab")

    def test_say_abcd_when_cdba(self):
        self.assertEqual(AlphabetSoup('cdba'), "abcd")