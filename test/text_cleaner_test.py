import unittest
from utils import TextCleaner

class TextCleanerTest(unittest.TestCase):
    def setUp(self):
        self.cleaner = TextCleaner()

    def test_clean_for_dictionary_1(self):
        self.assertEqual(
            self.cleaner.clean_for_dictionary("Art, thy whom! she does."), 
            "art thy whom she does")

    def test_clean_for_dictionary_2(self):
        self.assertEqual(
            self.cleaner.clean_for_dictionary("Art, thy whom! she does.,!@!#$ lol"), 
            "art thy whom she does lol")

    def test_clean_for_eval_1(self):
        self.assertEqual(
            self.cleaner.clean_for_eval("Art, thy whom! she does., lol"), 
            "art , thy whom ! she does . , lol")

    def test_clean_for_eval_2(self):
        self.assertEqual(
            self.cleaner.clean_for_eval("Art, thy whom! she does!! lol"), 
            "art , thy whom ! she does ! ! lol")
