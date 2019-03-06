from unittest import TestCase
from LetterCapitalize import LetterCapitalize

class TestLetterCapitalize(TestCase):
    def test_say_AaBb_when_aabb(self):
        self.assertEqual(LetterCapitalize("aa bb"), "Aa Bb")

    def test_say_HelloWorld_when_helloworld(self):
        self.assertEqual(LetterCapitalize("hello world"), "Hello World")

    def test_say_IRanThere_when_iranthere(self):
        self.assertEqual(LetterCapitalize("i ran there"), "I Ran There")