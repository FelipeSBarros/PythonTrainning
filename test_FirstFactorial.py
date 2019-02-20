import unittest
from FirstFactorial import FirstFactorial

class FirstFactorialTeste(unittest.TestCase):
    def test_say_1_when_1(self):
        self.assertEqual(FirstFactorial(1), 1)

    def test_say_2_when_2(self):
        self.assertEqual(FirstFactorial(2), 2)

    def test_say_6_when_3(self):
        self.assertEqual(FirstFactorial(3), 6)

    def test_say_24_when_4(self):
        self.assertEqual(FirstFactorial(4), 24)

    def test_say_40320_when_8(self):
        self.assertEqual(FirstFactorial(8), 40320)