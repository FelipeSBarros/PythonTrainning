import unittest
from LetterChanges import LetterChanges

class TestLetterChanges(unittest.TestCase):
    def test_say_b_when_a(self):
        """Must return b when a"""
        self.assertEqual(LetterChanges('a'), 'b')

    def test_say_c_when_b(self):
        """Must return c when b"""
        self.assertEqual(LetterChanges('b'), 'c')

    def test_say_d_when_c(self):
        """Must return d when c"""
        self.assertEqual(LetterChanges('c'), 'd')

    def test_say_a_when_z(self):
        """Must return d when c"""
        self.assertEqual(LetterChanges('z'), 'A')

    def test_say_bca_when_abz(self):
        """Must return d when c"""
        self.assertEqual(LetterChanges('bac'), 'cbd')

    def test_say_Ifmmp_when_hello(self):
        """Must return d when c"""
        self.assertEqual(LetterChanges('hello*3'), 'Ifmmp*3')

    def test_say_gvO_when_fun(self):
        """Must return d when c"""
        self.assertEqual(LetterChanges('fun times!'), "gvO Ujnft!")
