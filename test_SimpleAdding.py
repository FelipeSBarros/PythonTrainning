from unittest import TestCase
from SimpleAdding import SimpleAdding

class TesteSimpleAdding(TestCase):
    def test_say_1_when_1(self):
        self.assertEqual(SimpleAdding(1), 1)

    def test_say_3_when_2(self):
        self.assertEqual(SimpleAdding(2), 3)

    def test_say_6_when_3(self):
        self.assertEqual(SimpleAdding(3), 6)

    def test_say_10_when_4(self):
        self.assertEqual(SimpleAdding(4), 10)

    def test_say_15_when_5(self):
        self.assertEqual(SimpleAdding(5), 15)