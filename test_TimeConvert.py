from unittest import TestCase
from TimeConvert import TimeConvert

class TestTimeConvert(TestCase):
    def test_say_1_when_60(self):
        self.assertEqual(TimeConvert(60), 1)

    def test_say_colon59_when_59(self):
        self.assertEqual(TimeConvert(59), '0:59')

    def test_say_1colon3_when_63(self):
        self.assertEqual(TimeConvert(63), '1:3')

    def test_say_2colon6_when_126(self):
        self.assertEqual(TimeConvert(126), '2:6')

    def test_say_colon45_when_45(self):
        self.assertEqual(TimeConvert(45), '0:45')

    def test_say_colon60_when_60(self):
        self.assertEqual(TimeConvert(60), '1:0')