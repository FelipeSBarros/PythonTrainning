from unittest import TestCase
from SimpleSimbols import SimpleSimbols

class TestSimpleSimbles(TestCase):
    def test_simpleSimble(self):
        self.assertEqual(SimpleSimbols("+a+"), True)

    def test_simpleSimble_false(self):
        self.assertEqual(SimpleSimbols("a+"), False)

    def test_simpleSimble_false(self):
          self.assertEqual(SimpleSimbols("+d+=3=+s+"), True)

    def test_simpleSimble_false(self):
        self.assertEqual(SimpleSimbols("f++d+"), False)